from __future__ import annotations

import logging

from .config import Settings
from .jira import JiraClient
from .server import QaWebhookServer
from .workflow import OllamaModel, QaWorkflow


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    settings = Settings.from_env()
    jira = JiraClient(settings.jira_base_url, settings.jira_email, settings.jira_api_token, settings.request_timeout_seconds)
    model = OllamaModel(settings.ollama_base_url, settings.ollama_model, settings.request_timeout_seconds)
    workflow = QaWorkflow(jira, model, settings.project_root, settings.acceptance_criteria_field, settings.max_linked_issues)
    QaWebhookServer(settings, workflow).serve_forever()


if __name__ == "__main__":
    main()
