# docs/install/vscode-copilot.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The VS Code + GitHub Copilot install page: what to copy from the two part starter packages
(`.github-vscode/` and `.vscode/`), how to render the copy, and which installed files carry
the instruction, the hook, the skills and the workspace MCP registration.

## What The Page Establishes

- The install is: copy `.vscode/` to the workspace root, copy the contents of
  `.github-vscode/` into the workspace `.github/` folder, then run the copied
  `.github/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), then open or restart the workspace in VS Code once.
- The rename is deliberate: `.github-vscode/` exists only so the templates do not mix with
  this repository's real `.github/workflows/`, while VS Code and Copilot still expect the
  installed files under `.github/`.
- The renderer infers the workspace root from the copied `.github/` folder, fills path and
  repository placeholders, writes the OS-specific Python hook command, and validates that
  each named repository exists. The manual alternative is the same replacements by hand with
  no placeholder left behind.
- Package contents the page names: `copilot-instructions.md` (template for the installed
  always-on repository instruction), `hooks/agents-remember-session-start.json` and sibling
  hook files (templates for the installed `SessionStart` context injection), `skills/`
  (templates for Copilot's default project skill root), plus `.vscode/mcp.json` and
  `.vscode/mcp/agents-remember-settings.json`.
- Skills: VS Code discovers project skills from `.github/skills`, `.claude/skills` and
  `.agents/skills`, and personal skills from `~/.copilot/skills`, `~/.claude/skills` and
  `~/.agents/skills`. First-run setup does not install skills; the page also shows pointing
  `chat.agentSkillsLocations` at installed runtime roots and using
  `chat.useCustomizationsInParentRepositories` for nested repositories.
- Instructions: the Agents Remember instruction is installed as
  `.github/copilot-instructions.md`, kept separate from repository-specific guidance. Hooks:
  workspace hooks are discovered from `.github/hooks/*.json`, and the `SessionStart` hook
  runs the Python script that emits the first-action directive as additional context.
- MCP: workspace config lives at `.vscode/mcp.json`; the page prints the `uvx ...
  --config <projects>/.vscode/mcp/agents-remember-settings.json` registration.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step; the retirement appears only in that
one sentence.

The page is instructions, not proof: it does not show that the two-folder copy happened, that
the hook fired, that VS Code accepted `.vscode/mcp.json`, that the renderer ran, or that
`runtime_install()` executed. VS Code's discovery paths and settings keys are the page's
account of that harness.

## Evidence

- Copy `.vscode/` and the contents of `.github-vscode/` into `.github/`, render, then open or restart VS Code once. [1]
- The `.github-vscode/` name avoids the source checkout's own workflows while the install target is `.github/`. [2]
- Package contents: instruction template, hook templates, skill templates, `.vscode` MCP files. [3]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [4]
- Skill roots, `chat.agentSkillsLocations`, the instruction file and `SessionStart` hook discovery. [5]
- Workspace MCP config path and the `uvx` registration. [6]
