. "$PSScriptRoot\ClawIQ.Common.ps1"

Write-Status "Stopping Gateway..."
Stop-Gateway

Write-Status "Stopping Ollama..."
Stop-Ollama

Write-Host ""
Write-Host "ClawIQ STOPPED" -ForegroundColor Yellow
