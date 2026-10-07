# Testing

Current deterministic suite: core routing, independent conversations, restart context, failure exclusion, Jira QA mocks. Lucy suite находится в отдельном repo; legacy local tests сохраняются только для migration regression.

```powershell
npm.cmd test
python -m unittest discover -s tests -p test_jira_qa.py
npm.cmd run test:desktop
npm.cmd run build:windows
```

Windows GitHub Actions запускает Node 24 и Python 3.12 tests. Electron smoke локальный и packaged. Live Ollama smoke — отдельный запрос без cloud, не CI requirement.

Release checks: local chat и persistence, image model route, UI isolation, lack of Lucy data in packaged app, secret scan staged files, clean clone npm ci, tests, documented limitations. Проверка скриншота не заменяет accessibility/performance eval.

Future coverage: routing corpus/precision, actual vision responses, cancellation, recovery, cloud privacy boundary, OpenClaw permissions/approval, installer signing и cross-platform smoke.
