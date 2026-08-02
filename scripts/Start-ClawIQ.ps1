. "$PSScriptRoot\ClawIQ.Common.ps1"

Clear-Host

Write-Host ""
Write-Host "========== ClawIQ ==========" -ForegroundColor Green
Write-Host ""

Start-Ollama
Start-Gateway

Write-Host ""
Write-Host "ClawIQ READY" -ForegroundColor Green
