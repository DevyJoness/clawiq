@echo off
cd /d "%~dp0"
if exist "dist\clawiq\win-unpacked\ClawIQ.exe" (
  start "" "dist\clawiq\win-unpacked\ClawIQ.exe"
) else (
  powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\Start-ClawIQDesktop.ps1"
)
