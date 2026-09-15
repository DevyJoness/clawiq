from __future__ import annotations

import hmac
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Lock
from typing import Any, Callable

from .config import Settings
from .workflow import ISSUE_KEY_PATTERN, QaWorkflow

LOG = logging.getLogger(__name__)


class QaWebhookServer:
    def __init__(self, settings: Settings, workflow: QaWorkflow) -> None:
        self.settings = settings
        self.workflow = workflow
        self.executor = ThreadPoolExecutor(max_workers=1, thread_name_prefix="jira-qa")
        self.pending: set[str] = set()
        self.pending_lock = Lock()

    def _run(self, issue_key: str) -> None:
        try:
            outcome = self.workflow.run(issue_key)
            LOG.info("QA workflow %s for %s", outcome, issue_key)
        except Exception:
            LOG.exception("QA workflow failed for %s", issue_key)
        finally:
            with self.pending_lock:
                self.pending.discard(issue_key)

    def submit(self, issue_key: str) -> bool:
        with self.pending_lock:
            if issue_key in self.pending:
                return False
            self.pending.add(issue_key)
        self.executor.submit(self._run, issue_key)
        return True

    def handler(self) -> type[BaseHTTPRequestHandler]:
        app = self

        class Handler(BaseHTTPRequestHandler):
            server_version = "ClawIQQaWebhook/1.0"

            def log_message(self, format: str, *args: Any) -> None:
                LOG.info("%s - %s", self.client_address[0], format % args)

            def respond(self, status: int, payload: dict[str, Any]) -> None:
                body = json.dumps(payload).encode("utf-8")
                self.send_response(status)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self) -> None:
                if self.path == "/healthz":
                    self.respond(200, {"status": "ok"})
                else:
                    self.respond(404, {"error": "not_found"})

            def do_POST(self) -> None:
                if self.path != app.settings.webhook_path:
                    self.respond(404, {"error": "not_found"})
                    return
                supplied = self.headers.get(app.settings.webhook_secret_header, "")
                if not hmac.compare_digest(supplied, app.settings.webhook_secret):
                    LOG.warning("Rejected webhook with invalid secret from %s", self.client_address[0])
                    self.respond(401, {"error": "unauthorized"})
                    return
                try:
                    if self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower() != "application/json":
                        raise ValueError("content type must be application/json")
                    content_length = int(self.headers.get("Content-Length", "0"))
                    if content_length <= 0 or content_length > app.settings.max_request_bytes:
                        raise ValueError("invalid request size")
                    payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
                    issue_key = str(payload["issueKey"]).upper()
                    event = payload.get("event")
                    to_status = payload.get("toStatus")
                    if event != "qa_review" or to_status != app.settings.review_status or not ISSUE_KEY_PATTERN.fullmatch(issue_key):
                        raise ValueError("unsupported QA event")
                except (UnicodeDecodeError, ValueError, KeyError, TypeError, json.JSONDecodeError):
                    self.respond(400, {"error": "invalid_request"})
                    return
                queued = app.submit(issue_key)
                self.respond(202, {"status": "queued" if queued else "already_queued", "issueKey": issue_key})

        return Handler

    def serve_forever(self) -> None:
        httpd = ThreadingHTTPServer((self.settings.host, self.settings.port), self.handler())
        LOG.info("Jira QA webhook listening on http://%s:%s%s", self.settings.host, self.settings.port, self.settings.webhook_path)
        try:
            httpd.serve_forever()
        finally:
            self.executor.shutdown(wait=False, cancel_futures=True)
