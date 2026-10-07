$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
Push-Location $repo
try {
  node --test tests/clawiq_*.test.mjs
  if ($LASTEXITCODE -ne 0) { throw 'Node tests failed' }
  if ($env:CLAWIQ_TEST_PYTHON) { & $env:CLAWIQ_TEST_PYTHON -m unittest discover -s tests -p test_jira_qa.py }
  else { python -m unittest discover -s tests -p test_jira_qa.py }
  if ($LASTEXITCODE -ne 0) { throw 'Python tests failed' }
} finally { Pop-Location }
