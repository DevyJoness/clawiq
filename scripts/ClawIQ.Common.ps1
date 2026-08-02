# Общие функции ClawIQ

$GatewayPort = 18789
$OllamaPort = 11434

$Node = "$env:ProgramFiles\nodejs\node.exe"
$OpenClaw = "$env:APPDATA\npm\node_modules\openclaw\dist\index.js"
$OllamaExe = "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"

function Write-Status($Text) {
  Write-Host "[ClawIQ] $Text" -ForegroundColor Cyan
}

function Test-Port($Port) {
  try {
    $null = Test-NetConnection -ComputerName 127.0.0.1 -Port $Port -WarningAction SilentlyContinue -InformationLevel Quiet
    return $?
  }
  catch {
    return $false
  }
}

function Wait-Port($Port, $Timeout = 30) {
  $Start = Get-Date

  while (-not (Test-Port $Port)) {
    Start-Sleep 1

    if (((Get-Date) - $Start).TotalSeconds -gt $Timeout) {
      throw "Timeout waiting for port $Port"
    }
  }
}

function Start-Ollama {
  if (Test-Port $OllamaPort) {
    Write-Status "Ollama already running."
    return
  }

  Write-Status "Starting Ollama..."

  Start-Process $OllamaExe

  Wait-Port $OllamaPort

  Write-Status "Ollama Ready."
}

function Stop-Ollama {
  Get-Process ollama -ErrorAction SilentlyContinue | Stop-Process -Force
}

function Start-Gateway {
  if (Test-Port $GatewayPort) {
    Write-Status "Gateway already running."
    return
  }

  Write-Status "Starting Gateway..."

  Start-Process `
    -WindowStyle Hidden `
    -FilePath $Node `
    -ArgumentList "`"$OpenClaw`" gateway --port $GatewayPort"

  Wait-Port $GatewayPort

  Write-Status "Gateway Ready."
}

function Stop-Gateway {
  Get-CimInstance Win32_Process |
  Where-Object {
    $_.CommandLine -like "*openclaw*" -and
    $_.CommandLine -like "*gateway*"
  } |
  ForEach-Object {
    Stop-Process -Id $_.ProcessId -Force
  }
}
