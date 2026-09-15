from __future__ import annotations

import base64
import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


class JiraError(RuntimeError):
    pass


def adf_to_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if not isinstance(value, dict):
        return ""
    parts: list[str] = []

    def visit(node: Any) -> None:
        if not isinstance(node, dict):
            return
        if node.get("type") == "text":
            parts.append(str(node.get("text", "")))
        for child in node.get("content", []):
            visit(child)
        if node.get("type") in {"paragraph", "heading", "listItem"}:
            parts.append("\n")

    visit(value)
    return "".join(parts).strip()


def text_to_adf(text: str) -> dict[str, Any]:
    paragraphs = []
    for line in text.splitlines():
        content = [{"type": "text", "text": line}] if line else []
        paragraphs.append({"type": "paragraph", "content": content})
    return {"type": "doc", "version": 1, "content": paragraphs or [{"type": "paragraph", "content": []}]}


class JiraClient:
    def __init__(self, base_url: str, email: str, api_token: str, timeout: int = 30) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        credentials = base64.b64encode(f"{email}:{api_token}".encode("utf-8")).decode("ascii")
        self.headers = {"Accept": "application/json", "Authorization": f"Basic {credentials}"}

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> Any:
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        headers = dict(self.headers)
        if data is not None:
            headers["Content-Type"] = "application/json"
        request = Request(self.base_url + path, data=data, headers=headers, method=method)
        try:
            with urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
                return json.loads(raw) if raw else None
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")[:1000]
            raise JiraError(f"Jira {method} {path} failed with HTTP {exc.code}: {detail}") from exc
        except URLError as exc:
            raise JiraError(f"Jira {method} {path} failed: {exc.reason}") from exc

    def get_issue(self, issue_key: str, extra_fields: list[str] | None = None) -> dict[str, Any]:
        fields = ["summary", "description", "issuetype", "status", "priority", "labels", "components", "fixVersions", "issuelinks", "subtasks"]
        if extra_fields:
            fields.extend(extra_fields)
        key = quote(issue_key, safe="-")
        return self._request("GET", f"/rest/api/3/issue/{key}?fields={quote(','.join(fields), safe=',')}")

    def get_all_comments(self, issue_key: str) -> list[dict[str, Any]]:
        key = quote(issue_key, safe="-")
        start_at = 0
        comments: list[dict[str, Any]] = []
        while True:
            page = self._request("GET", f"/rest/api/3/issue/{key}/comment?startAt={start_at}&maxResults=100")
            values = page.get("comments", [])
            comments.extend(values)
            start_at += len(values)
            if start_at >= page.get("total", 0) or not values:
                return comments

    def get_linked_issues(self, issue: dict[str, Any], limit: int) -> list[dict[str, Any]]:
        result = []
        for link in issue.get("fields", {}).get("issuelinks", [])[:limit]:
            linked = link.get("outwardIssue") or link.get("inwardIssue")
            if not linked or not linked.get("key"):
                continue
            related = self.get_issue(linked["key"])
            related["linkType"] = link.get("type", {}).get("name", "relates to")
            result.append(related)
        return result

    def add_comment(self, issue_key: str, text: str) -> None:
        key = quote(issue_key, safe="-")
        self._request("POST", f"/rest/api/3/issue/{key}/comment", {"body": text_to_adf(text)})
