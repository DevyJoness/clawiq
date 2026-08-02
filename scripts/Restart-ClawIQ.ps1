. "$PSScriptRoot\ClawIQ.Common.ps1"

Stop-Gateway
Stop-Ollama

Start-Sleep 2

Start-Ollama
Start-Gateway

Write-Host ""
Write-Host "ClawIQ RESTARTED" -ForegroundColor Green
