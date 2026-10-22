$ErrorActionPreference = 'Stop'
$taskRoot = $PSScriptRoot

Write-Host 'No.33 candidate v0.2 - standard-library verification'
python (Join-Path $taskRoot 'verify_exhaustive.py')
if ($LASTEXITCODE -ne 0) { throw 'Exhaustive verification failed.' }
python (Join-Path $taskRoot 'audit_bitmasks.py')
if ($LASTEXITCODE -ne 0) { throw 'Separate bit-mask verification failed.' }
Write-Host 'PASS - finite checks only; read PROOF.md for universal bounds. Public release remains HOLD.'
