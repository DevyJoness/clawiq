# Setup

Обновлено: 2026-10-07.

## Desktop

Windows, Node.js 24, npm, Ollama. Проверенные локальные модели: qwen3:14b и qwen2.5vl:7b. Требования RAM/VRAM зависят от размера/quantization модели; не объявляем поддержку неизвестного hardware без smoke.

```powershell
git clone https://github.com/DevyJoness/clawiq.git
cd clawiq
npm.cmd ci
ollama pull qwen3:14b
ollama pull qwen2.5vl:7b
npm.cmd start
```

Убедитесь, что Ollama слушает 127.0.0.1:11434 и ollama list показывает нужные модели. Если она не запущена — запустите приложение Ollama или ollama serve; не запускайте второй serve на занятом порту. Никакой OpenAI API key для текущего desktop не требуется.

UI launcher: scripts/Start-ClawIQDesktop.ps1. Portable release не требует установленного Node, но требует Ollama и моделей.

## Legacy OpenClaw

OpenClaw остаётся integration target для skills/actions; сейчас desktop его не запускает. Legacy Start-ClawIQ.ps1 ожидает Node в Program Files, глобальный npm OpenClaw и пользовательскую Ollama installation. Эти scripts не являются переносимым production installer. Не используйте legacy Telegram channel с Lucy token.

## Jira QA

Python 3.11+, отдельный ignored .env, установка не нужна для стандартной библиотеки. Пример .env содержит placeholders, не доказательство действующих credentials. См. JIRA_QA_WEBHOOK.md. Adapter не включён по умолчанию. Cloud tunnel и permissions проверяются отдельно перед deployment.

## Тестирование

```powershell
npm.cmd test
python -m unittest discover -s tests -p test_jira_qa.py
npm.cmd run test:desktop
```

Если python указывает на неработающий WindowsApps alias, установите настоящий Python или задайте CLAWIQ_TEST_PYTHON для scripts/Test-ClawIQ.ps1.

Порты: Ollama 11434; legacy Gateway 18789; isolated Jira QA 8787. Desktop использует IPC и file assets, HTTP порт ему не нужен. Lucy ports — в её собственных docs.
