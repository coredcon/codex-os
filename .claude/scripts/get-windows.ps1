# Get all process window titles — look for media players
Get-Process | Where-Object { $_.MainWindowTitle -ne "" } | ForEach-Object {
    "$($_.ProcessName)|$($_.MainWindowTitle)"
}
