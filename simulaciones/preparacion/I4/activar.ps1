# Activación local para esta terminal; no modifica PATH global.
$runtimeI4 = 'C:\Users\amoji\.cache\codex-runtimes\codex-primary-runtime\dependencies\python'
if (-not (Test-Path -LiteralPath "$runtimeI4\python.exe")) {
    throw 'El runtime Python verificado ya no está disponible.'
}
$env:PATH = "$runtimeI4;$env:PATH"
python --version
