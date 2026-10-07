param(
  [int]$Port = 8787
)

$ErrorActionPreference = "Stop"
$projectRoot = Split-Path -Parent $PSScriptRoot
$env:CLAWIQ_JIRA_QA_PORT = $Port
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
  $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
  throw "Python 3.11+ was not found. Install it first; see docs/SETUP.md."
}

Push-Location $projectRoot
try {
  Write-Host "[ClawIQ] Starting local Jira QA webhook on 127.0.0.1:$Port" -ForegroundColor Cyan
  & $python.Source -m automation.jira_qa.main
}
finally {
  Pop-Location
}
