from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path


def _env(name: str, default: str | None = None) -> str | None:
    value = os.environ.get(name, default)
    return value.strip() if value else value


def load_dotenv(path: Path) -> None:
    """Load a local .env without adding a runtime dependency."""
    if not path.is_file():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


@dataclass(frozen=True)
class Settings:
    host: str
    port: int
    webhook_path: str
    webhook_secret: str
    webhook_secret_header: str
    review_status: str
    jira_base_url: str
    jira_email: str
    jira_api_token: str
    acceptance_criteria_field: str | None
    ollama_base_url: str
    ollama_model: str
    request_timeout_seconds: int
    max_request_bytes: int
    max_linked_issues: int
    project_root: Path

    @classmethod
    def from_env(cls, project_root: Path | None = None) -> "Settings":
        root = project_root or Path(__file__).resolve().parents[2]
        load_dotenv(root / "automation" / "jira_qa" / ".env")
        secret = _env("CLAWIQ_JIRA_WEBHOOK_SECRET")
        jira_url = _env("CLAWIQ_JIRA_BASE_URL")
        email = _env("CLAWIQ_JIRA_EMAIL")
        token = _env("CLAWIQ_JIRA_API_TOKEN")
        missing = [name for name, value in {
            "CLAWIQ_JIRA_WEBHOOK_SECRET": secret,
            "CLAWIQ_JIRA_BASE_URL": jira_url,
            "CLAWIQ_JIRA_EMAIL": email,
            "CLAWIQ_JIRA_API_TOKEN": token,
        }.items() if not value]
        if missing:
            raise ValueError("Missing required environment variables: " + ", ".join(missing))
        path = _env("CLAWIQ_JIRA_QA_WEBHOOK_PATH", "/webhooks/jira/qa-review")
        if not path.startswith("/"):
            raise ValueError("CLAWIQ_JIRA_QA_WEBHOOK_PATH must start with '/'")
        return cls(
            host=_env("CLAWIQ_JIRA_QA_HOST", "127.0.0.1") or "127.0.0.1",
            port=int(_env("CLAWIQ_JIRA_QA_PORT", "8787") or 8787),
            webhook_path=path,
            webhook_secret=secret or "",
            webhook_secret_header=_env("CLAWIQ_JIRA_QA_SECRET_HEADER", "X-ClawIQ-Webhook-Secret") or "X-ClawIQ-Webhook-Secret",
            review_status=_env("CLAWIQ_JIRA_QA_REVIEW_STATUS", "В процессе проверки") or "В процессе проверки",
            jira_base_url=(jira_url or "").rstrip("/"),
            jira_email=email or "",
            jira_api_token=token or "",
            acceptance_criteria_field=_env("CLAWIQ_JIRA_ACCEPTANCE_CRITERIA_FIELD"),
            ollama_base_url=(_env("CLAWIQ_OLLAMA_BASE_URL", "http://127.0.0.1:11434") or "").rstrip("/"),
            ollama_model=_env("CLAWIQ_JIRA_QA_MODEL", "qwen3:14b") or "qwen3:14b",
            request_timeout_seconds=int(_env("CLAWIQ_JIRA_QA_TIMEOUT_SECONDS", "90") or 90),
            max_request_bytes=int(_env("CLAWIQ_JIRA_QA_MAX_REQUEST_BYTES", "16384") or 16384),
            max_linked_issues=int(_env("CLAWIQ_JIRA_QA_MAX_LINKED_ISSUES", "10") or 10),
            project_root=root,
        )
