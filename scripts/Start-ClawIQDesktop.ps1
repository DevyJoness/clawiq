[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$repo = Split-Path $PSScriptRoot -Parent
$electron = Join-Path $repo 'node_modules\electron\dist\electron.exe'
if (-not (Test-Path -LiteralPath $electron)) { throw 'Выполните npm.cmd ci в папке clawiq.' }
Start-Process -FilePath $electron -WindowStyle Hidden -ArgumentList @(('"'+$repo+'"')) -WorkingDirectory $repo
