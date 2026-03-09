# Run once as Administrator to register the Vox heartbeat task
# Usage: Right-click PowerShell -> Run as Administrator, then run this script

$scriptPath = "F:\My Drive\Obsidian\Codex.os\.claude\scripts\heartbeat.ps1"
$taskName = "VoxHeartbeat"

# Remove existing task if present
if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    Write-Host "Removed existing task."
}

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument "-WindowStyle Hidden -NonInteractive -ExecutionPolicy Bypass -File `"$scriptPath`""

# Run every 30 minutes
$trigger = New-ScheduledTaskTrigger -RepetitionInterval (New-TimeSpan -Minutes 30) -Once -At (Get-Date)

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 5) `
    -StartWhenAvailable `
    -DontStopOnIdleEnd

# Run as current user (needed for desktop notifications)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Principal $principal `
    -Description "Vox heartbeat — checks calendar every 30 min, fires prep brief if meeting approaching"

Write-Host "VoxHeartbeat task registered. Runs every 30 minutes, Mon-Fri 8am-7pm."
Write-Host "To test now: Start-ScheduledTask -TaskName VoxHeartbeat"
Write-Host "To remove: Unregister-ScheduledTask -TaskName VoxHeartbeat -Confirm:`$false"
