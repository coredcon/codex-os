@echo off
start "" /min cmd /c "echo y | claude remote-control"
wezterm start --cwd "F:\My Drive\Obsidian\Codex.os" -- pwsh -NoExit -Command "claude --dangerously-skip-permissions --channels plugin:discord@claude-plugins-official"
