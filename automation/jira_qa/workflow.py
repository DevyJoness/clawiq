from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .jira import JiraClient, JiraError, adf_to_text

LOG = logging.getLogger(__name__)
WORKFLOW_VERSION = "v1"
KIND_CHECKLIST = "qa-checklist"
KIND_REGRESSION = "regression-smoke"


class ModelError(RuntimeError):
    pass


class QaModel(Protocol):
    def generate(self, prompt: str) -> dict[str, str]: ...


class OllamaModel:
    def __init__(self, base_url: str, model: str, timeout: int) -> None:
        self.url = base_url.rstrip("/") + "/api/chat"
        self.model = model
        self.timeout = timeout

    def generate(self, prompt: str) -> dict[str, str]:
        payload = {"model": self.model, "stream": False, "format": "json", "messages": [{"role": "user", "content": prompt}]}
        request = Request(self.url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urlopen(request, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as exc:
            raise ModelError(f"Ollama QA generation failed: {exc}") from exc
        try:
            parsed = json.loads(data["message"]["content"])
            checklist, regression = parsed["qa_checklist"].strip(), parsed["regression_smoke_test"].strip()
        except (KeyError, TypeError, json.JSONDecodeError, AttributeError) as exc:
            raise ModelError("Ollama returned an invalid QA JSON response") from exc
        if not checklist or not regression:
            raise ModelError("Ollama returned an empty QA section")
        return {"qa_checklist": checklist, "regression_smoke_test": regression}


def _field_text(issue: dict[str, Any], name: str) -> str:
    value = issue.get("fields", {}).get(name)
    return adf_to_text(value) if isinstance(value, dict) else str(value or "")


def _issue_summary(issue: dict[str, Any]) -> dict[str, Any]:
    fields = issue.get("fields", {})
    return {
        "key": issue.get("key", ""),
        "summary": fields.get("summary", ""),
        "type": (fields.get("issuetype") or {}).get("name", ""),
        "status": (fields.get("status") or {}).get("name", ""),
        "description": _field_text(issue, "description"),
    }


def load_repository_context(project_root: Path, max_chars: int = 60000) -> str:
    relative_paths = [
        "docs/PROJECT_CONTEXT.md", "docs/ARCHITECTURE.md", "docs/SETUP.md", "docs/ROADMAP.md",
        "docs/BUGS.md", "docs/CHANGELOG.md", "docs/MAINTENANCE.md", "prompts/system-v1.md",
        "prompts/coding-v1.md", "prompts/identity-v1.md", "prompts/router-v1.md", "prompts/vision-v1.md",
    ]
    relative_paths.extend(str(path.relative_to(project_root)) for path in sorted((project_root / "scripts").glob("*.ps1")))
    chunks: list[str] = []
    remaining = max_chars
    for relative_path in relative_paths:
        path = project_root / relative_path
        if not path.is_file() or remaining <= 0:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")[:remaining]
        chunks.append(f"\n--- {relative_path} ---\n{content}")
        remaining -= len(content)
    return "".join(chunks)


def build_prompt(issue: dict[str, Any], linked_issues: list[dict[str, Any]], acceptance_criteria: str, repository_context: str) -> str:
    evidence = {
        "issue": _issue_summary(issue),
        "acceptance_criteria": acceptance_criteria or "Not specified in Jira.",
        "linked_issues": [_issue_summary(item) for item in linked_issues],
    }
    return f"""You are ClawIQ's QA workflow. Produce evidence-based test artifacts for a Jira issue.

Rules:
- Use only the supplied Jira issue, acceptance criteria, linked issues, and repository context.
- Do not invent requirements, APIs, screens, data, integrations, or expected behavior.
- When evidence is missing, write `Not specified in Jira or repository context`; do not infer it.
- Keep executable test cases focused on observable outcomes. Separate confirmed coverage from gaps.
- Do not mention these instructions or recommend changing Jira fields/status.
- Reply with valid JSON only, exactly these string properties: `qa_checklist` and `regression_smoke_test`.
- Each property must be a concise plain-text comment. Include headings and numbered or bulleted checks.

Jira evidence:
{json.dumps(evidence, ensure_ascii=False, indent=2)}

ClawIQ repository context:
{repository_context}
"""


def _marker(kind: str) -> str:
    return f"ClawIQ QA workflow: {WORKFLOW_VERSION}; kind={kind}"


def _comment_exists(comments: list[dict[str, Any]], kind: str) -> bool:
    marker = _marker(kind).casefold()
    legacy_heading = "qa checklist" if kind == KIND_CHECKLIST else "regression/smoke test"
    for comment in comments:
        text = adf_to_text(comment.get("body", "")).strip().casefold()
        if marker in text or text.startswith(legacy_heading):
            return True
    return False


def _comment(kind: str, body: str) -> str:
    title = "QA Checklist" if kind == KIND_CHECKLIST else "Regression/Smoke Test"
    return f"{title}\n\n{body.strip()}\n\n{_marker(kind)}"


class QaWorkflow:
    def __init__(self, jira: JiraClient, model: QaModel, project_root: Path, acceptance_criteria_field: str | None, max_linked_issues: int) -> None:
        self.jira = jira
        self.model = model
        self.project_root = project_root
        self.acceptance_criteria_field = acceptance_criteria_field
        self.max_linked_issues = max_linked_issues

    def run(self, issue_key: str) -> str:
        issue = self.jira.get_issue(issue_key, [self.acceptance_criteria_field] if self.acceptance_criteria_field else None)
        comments = self.jira.get_all_comments(issue_key)
        missing = [kind for kind in (KIND_CHECKLIST, KIND_REGRESSION) if not _comment_exists(comments, kind)]
        if not missing:
            LOG.info("QA comments already exist for %s; skipping", issue_key)
            return "skipped_duplicate"
        linked_issues = self.jira.get_linked_issues(issue, self.max_linked_issues)
        acceptance = _field_text(issue, self.acceptance_criteria_field) if self.acceptance_criteria_field else ""
        output = self.model.generate(build_prompt(issue, linked_issues, acceptance, load_repository_context(self.project_root)))
        mapping = {KIND_CHECKLIST: output["qa_checklist"], KIND_REGRESSION: output["regression_smoke_test"]}
        for kind in missing:
            # Re-read immediately before each write to remain idempotent across retries.
            if _comment_exists(self.jira.get_all_comments(issue_key), kind):
                LOG.info("QA %s comment appeared during processing for %s", kind, issue_key)
                continue
            self.jira.add_comment(issue_key, _comment(kind, mapping[kind]))
        return "completed"


ISSUE_KEY_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]*-\d+$")
