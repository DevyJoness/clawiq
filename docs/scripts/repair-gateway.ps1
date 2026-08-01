Write-Host "========================================="
Write-Host " ClawIQ Gateway Repair"
Write-Host "========================================="
Write-Host ""

$userProfile = $env:USERPROFILE

$gatewayCmd = Join-Path $userProfile ".openclaw\gateway.cmd"
$gatewayVbs = Join-Path $userProfile ".openclaw\gateway.vbs"

if (!(Test-Path $gatewayCmd)) {
    Write-Host "gateway.cmd not found!" -ForegroundColor Red
    exit 1
}

if (!(Test-Path $gatewayVbs)) {
    Write-Host "gateway.vbs not found!" -ForegroundColor Red
    exit 1
}

Write-Host "Repairing gateway.cmd..."

@"
@echo off
rem OpenClaw Gateway (ClawIQ Repair)
set "TMPDIR=$($env:TEMP)"
set "OPENCLAW_GATEWAY_PORT=18789"
set "OPENCLAW_SYSTEMD_UNIT=openclaw-gateway.service"
set "OPENCLAW_WINDOWS_TASK_NAME=OpenClaw Gateway"
set "OPENCLAW_WINDOWS_TASK_HIDDEN_LAUNCHER=1"
set "OPENCLAW_SERVICE_MARKER=openclaw"
set "OPENCLAW_SERVICE_KIND=gateway"
"C:\Program Files\nodejs\node.exe" "%APPDATA%\npm\node_modules\openclaw\dist\index.js" gateway --port 18789
"@ | Set-Content $gatewayCmd -Encoding ASCII

Write-Host "Repairing gateway.vbs..."

@'
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run Chr(34) & WshShell.ExpandEnvironmentStrings("%USERPROFILE%") & "\.openclaw\gateway.cmd" & Chr(34), 0, False
'@ | Set-Content $gatewayVbs -Encoding ASCII

Write-Host ""
Write-Host "Gateway repaired successfully." -ForegroundColor Green

Write-Host ""
Write-Host "Testing scheduled task..."

schtasks /run /tn "OpenClaw Gateway"

Write-Host ""
Write-Host "Done."
