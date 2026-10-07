/** Pure local-first routing. No provider credentials or network calls. */
export function classifyRequest(text, hasImage = false) {
  if (hasImage) return { kind: 'vision', reason: 'К запросу приложено изображение: нужна локальная vision-модель.' };
  if (/\b(code|debug|javascript|python|typescript|sql)\b|код|программ|ошибк|отлад|рефактор/iu.test(text)) return { kind: 'coding', reason: 'Запрос связан с кодом или отладкой.' };
  if (/найди|поищи|интернет|актуальн|сегодня|новост|search|latest/iu.test(text)) return { kind: 'research', reason: 'Нужна проверка источников. В этом релизе доступен только локальный анализ; веб-поиск не подключён.' };
  if (/архитектур|сравни|проанализ|план|объясни|reason|analys|compare/iu.test(text)) return { kind: 'analysis', reason: 'Запрос требует анализа, объяснения или планирования.' };
  return { kind: 'conversation', reason: 'Обычный разговор: достаточно локальной текстовой модели.' };
}
export function chooseRoute(text, hasImage, models) {
  const task = classifyRequest(text, hasImage);
  const candidates = task.kind === 'vision' ? ['qwen2.5vl:7b']
    : task.kind === 'coding' ? ['qwen2.5-coder:14b', 'qwen3:14b'] : ['qwen3:14b'];
  const model = candidates.find(name => models.includes(name));
  if (!model) throw new Error(task.kind === 'vision' ? 'Нужна локальная модель qwen2.5vl:7b. Установите её через Ollama.' : 'Нужна локальная модель qwen3:14b. Установите её через Ollama.');
  return { ...task, provider: 'ollama', model, local: true, toolsAvailable: false };
}
