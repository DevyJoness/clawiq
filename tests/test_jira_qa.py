from __future__ import annotations

import json
from pathlib import Path
import sys
from http.server import ThreadingHTTPServer
from threading import Thread
import unittest
from unittest.mock import Mock
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from automation.jira_qa.jira import adf_to_text, text_to_adf
from automation.jira_qa.config import Settings
from automation.jira_qa.server import QaWebhookServer
from automation.jira_qa.workflow import (
    KIND_CHECKLIST,
    KIND_REGRESSION,
    QaWorkflow,
    _comment,
    _comment_exists,
    build_prompt,
)


def issue(key: str = "KAN-42") -> dict:
    return {
        "key": key,
        "fields": {
            "summary": "Add a local QA webhook",
            "description": {"type": "doc", "content": [{"type": "paragraph", "content": [{"type": "text", "text": "Accept requests securely."}]}]},
            "issuetype": {"name": "Story"},
            "status": {"name": "В процессе проверки"},
            "issuelinks": [],
        },
    }


class FakeJira:
    def __init__(self, comments: list[dict] | None = None) -> None:
        self.comments = comments or []
        self.added: list[str] = []

    def get_issue(self, key: str, extra_fields=None) -> dict:
        return issue(key)

    def get_all_comments(self, key: str) -> list[dict]:
        return self.comments + [{"body": text_to_adf(value)} for value in self.added]

    def get_linked_issues(self, source: dict, limit: int) -> list[dict]:
        return []

    def add_comment(self, key: str, text: str) -> None:
        self.added.append(text)


class FakeModel:
    def __init__(self) -> None:
        self.prompts: list[str] = []

    def generate(self, prompt: str) -> dict[str, str]:
        self.prompts.append(prompt)
        return {"qa_checklist": "1. Verify secure request validation.", "regression_smoke_test": "1. Verify the health endpoint."}


class JiraQaTests(unittest.TestCase):
    def test_adf_round_trip_preserves_text(self) -> None:
        self.assertEqual(adf_to_text(text_to_adf("First\n\nSecond")), "First\n\nSecond")

    def test_marker_detects_existing_comment(self) -> None:
        comments = [{"body": text_to_adf(_comment(KIND_CHECKLIST, "Existing."))}]
        self.assertTrue(_comment_exists(comments, KIND_CHECKLIST))
        self.assertFalse(_comment_exists(comments, KIND_REGRESSION))

    def test_prompt_declares_evidence_only_policy(self) -> None:
        prompt = build_prompt(issue(), [], "", "Repository context")
        self.assertIn("Do not invent requirements", prompt)
        self.assertIn("Not specified in Jira.", prompt)

    def test_workflow_posts_two_separate_comments(self) -> None:
        jira, model = FakeJira(), FakeModel()
        workflow = QaWorkflow(jira, model, Path(__file__).resolve().parents[1], None, 10)
        self.assertEqual(workflow.run("KAN-42"), "completed")
        self.assertEqual(len(jira.added), 2)
        self.assertIn("QA Checklist", jira.added[0])
        self.assertIn("Regression/Smoke Test", jira.added[1])
        self.assertEqual(len(model.prompts), 1)

    def test_workflow_skips_existing_pair_without_model_call(self) -> None:
        jira = FakeJira([
            {"body": text_to_adf(_comment(KIND_CHECKLIST, "Existing."))},
            {"body": text_to_adf(_comment(KIND_REGRESSION, "Existing."))},
        ])
        model = Mock()
        workflow = QaWorkflow(jira, model, Path(__file__).resolve().parents[1], None, 10)
        self.assertEqual(workflow.run("KAN-42"), "skipped_duplicate")
        model.generate.assert_not_called()
        self.assertEqual(jira.added, [])

    def test_webhook_requires_secret_and_queues_valid_event(self) -> None:
        settings = Settings(
            host="127.0.0.1", port=0, webhook_path="/webhooks/jira/qa-review", webhook_secret="test-secret",
            webhook_secret_header="X-ClawIQ-Webhook-Secret", review_status="В процессе проверки",
            jira_base_url="https://example.atlassian.net", jira_email="qa@example.com", jira_api_token="token",
            acceptance_criteria_field=None, ollama_base_url="http://127.0.0.1:11434", ollama_model="qwen3:14b",
            request_timeout_seconds=1, max_request_bytes=1000, max_linked_issues=1, project_root=Path.cwd(),
        )
        workflow = Mock()
        app = QaWebhookServer(settings, workflow)
        httpd = ThreadingHTTPServer(("127.0.0.1", 0), app.handler())
        thread = Thread(target=httpd.serve_forever, daemon=True)
        thread.start()
        url = f"http://127.0.0.1:{httpd.server_port}{settings.webhook_path}"
        body = json.dumps({"issueKey": "KAN-42", "event": "qa_review", "toStatus": "В процессе проверки"}).encode()
        try:
            with self.assertRaises(HTTPError) as rejected:
                urlopen(Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST"))
            self.assertEqual(rejected.exception.code, 401)
            request = Request(url, data=body, headers={"Content-Type": "application/json", "X-ClawIQ-Webhook-Secret": "test-secret"}, method="POST")
            with urlopen(request) as response:
                self.assertEqual(response.status, 202)
            # The worker is asynchronous; shutting down waits for its submitted work.
            app.executor.shutdown(wait=True)
            workflow.run.assert_called_once_with("KAN-42")
        finally:
            httpd.shutdown()
            httpd.server_close()


if __name__ == "__main__":
    unittest.main()
