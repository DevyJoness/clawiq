# ClawIQ desktop 0.4.0

Windows Electron preview: personal chat, sessions sidebar, image attachment и route explanation. Приложение не требует Telegram.

## Работа

Запустите Ollama, откройте ClawIQ.cmd или ClawIQ.exe. Напишите запрос. На код выбирается установленная qwen2.5-coder:14b либо qwen3:14b; обычный текст/анализ — qwen3:14b; прикреплённое PNG/JPEG — qwen2.5vl:7b. Перед отправкой проверяется availability модели. Это эвристический router foundation, не доказательство оптимальности модели для любой задачи.

Новый разговор создаёт отдельный контекст. История восстанавливается после restart. «Удалить разговор» удаляет соответствующий локальный session JSON. Изображение используется только в текущем запросе и не сохраняется; для следующего vision запроса его нужно приложить заново.

Нет веб-поиска, cloud calls и tools. Research intent классифицируется, но ответ явно ограничен локальным анализом и непроверенной актуальностью. Модель может ошибаться; маршрут показывает выбранный путь, не гарантирует правильность ответа.

## Проверки и сборка

```powershell
npm.cmd run test:desktop
npm.cmd run build:windows
```

Сборка: dist/clawiq/win-unpacked. Запускайте ClawIQ.exe вместе со всей папкой. Модели не встроены. Сборка unsigned, installer/auto-update пока отсутствуют. Local sessions: Electron app.getPath('userData')/sessions; на Windows обычно %APPDATA%/clawiq-desktop/sessions.

Smoke использует временное хранилище, проверяет IPC create/read/list/delete и изоляцию UI; не делает платные provider calls. Изображение экрана сохраняется в temp/clawiq-desktop.png.
