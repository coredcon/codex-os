# Vox Heartbeat — runs every 30 min via Task Scheduler
# Checks calendar; fires prep brief if meeting within 30 minutes

$now = Get-Date
$hour = $now.Hour
$day = $now.DayOfWeek

# Only run Mon-Fri, 8am-7pm
if ($day -eq 'Saturday' -or $day -eq 'Sunday') { exit 0 }
if ($hour -lt 8 -or $hour -gt 19) { exit 0 }

$vaultPath = "F:\My Drive\Obsidian\Codex.os"
$briefPath = "$vaultPath\00 Inbox\vox-brief.md"

$prompt = @"
HEARTBEAT MODE. Ignore startup ritual. Do exactly this and nothing else:

1. Call gcal_list_events on asporkable@gmail.com for the next 60 minutes.
2. If any event starts within the next 30 minutes:
   - Write a brief to: $briefPath
   - Format: "## Vox Meeting Brief — [event name] at [time]\n- What: [1 line]\n- Context: [1 line of relevant background if known]\n- Have ready: [1 thing]"
   - Output exactly the word: BRIEF_READY
3. If no upcoming event: output exactly the word: SILENT

No other output. No vault loading. No daily note. No session digest.
"@

try {
    $result = & claude --print --system-prompt "You are Vox, a personal assistant. You have access to Google Calendar via MCP tools." $prompt 2>$null

    if ($result -match "BRIEF_READY") {
        # Toast notification via .NET (no BurntToast required)
        Add-Type -AssemblyName System.Windows.Forms
        Add-Type -AssemblyName System.Drawing

        $notify = New-Object System.Windows.Forms.NotifyIcon
        $notify.Icon = [System.Drawing.SystemIcons]::Information
        $notify.BalloonTipTitle = "Vox"
        $notify.BalloonTipText = "Meeting brief ready in your Obsidian inbox"
        $notify.BalloonTipIcon = "Info"
        $notify.Visible = $true
        $notify.ShowBalloonTip(8000)

        Start-Sleep -Seconds 9
        $notify.Visible = $false
        $notify.Dispose()
    }
} catch {
    # Fail silently — heartbeat should never interrupt
    Add-Content -Path "$vaultPath\.claude\scripts\heartbeat-errors.log" -Value "[$now] Error: $_"
}
