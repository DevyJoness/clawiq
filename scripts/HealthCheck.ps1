. "$PSScriptRoot\ClawIQ.Common.ps1"

Write-Host ""

if (Test-Port 11434) {
  Write-Host "Ollama : OK" -ForegroundColor Green
}
else {
  Write-Host "Ollama : DOWN" -ForegroundColor Red
}

if (Test-Port 18789) {
  Write-Host "Gateway: OK" -ForegroundColor Green
}
else {
  Write-Host "Gateway: DOWN" -ForegroundColor Red
}
