$scriptPath = Split-Path -Path $MyInvocation.MyCommand.Path
$clarans = "$scriptPath\src\Clarans"
$clustering = "$scriptPath\src-py\src-clustering"
$visualisation = "$scriptPath\src-py\src-vis"

Write-Host "Running clarans (.NET)"
Set-Location $clarans
dotnet run -c Release

Write-Host "Running clustering algorithms"
Set-Location $clustering
python main.py

Write-Host "Running visualisation"
Set-Location $visualisation
python main.py

Set-Location $scriptPath


