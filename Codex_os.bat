@echo off
REM Ensure QMD MCP daemon is running before Claude starts (avoids qmd-codex "failed" status)
start "" /min cmd /c "qmd mcp stop 2>nul & timeout /t 1 /nobreak >nul & qmd mcp --http --daemon"
timeout /t 4 /nobreak >nul
start "" /min cmd /c "echo y | claude remote-control"
wezterm start --cwd "F:\My Drive\Obsidian\Codex.os" -- pwsh -NoExit -Command "claude --dangerously-skip-permissions --channels plugin:discord@claude-plugins-official"
