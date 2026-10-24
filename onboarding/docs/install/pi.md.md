# docs/install/pi.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Pi install page: what to copy from the repository's `.pi/` starter package, how to
render it, how the project settings load the startup extension and the MCP adapter, and
where Pi finds skills.

## What The Page Establishes

- Pi core has no built-in MCP client, so the starter package uses `pi-mcp-adapter` and keeps
  the package self-contained with Pi's own project override rather than a shared `.mcp.json`.
- The install is: copy `.pi/` to the workspace root, run the copied `.pi/render-starter`
  with a single `--repo` list (the page shows `--repo my-app shared-lib`), then start or
  reload Pi from the workspace once.
- The renderer infers the workspace root from the copied `.pi/` folder, fills path and
  repository placeholders, renders the project extension constant, and validates that each
  named repository exists. The manual alternative is the same replacements by hand with no
  placeholder left behind.
- Package contents the page names: `.pi/settings.json` (project settings that load the local
  extension, local skills and `npm:pi-mcp-adapter`), `.pi/extensions/agents-remember-start.ts`
  (a project-local `before_agent_start` extension injecting the mandatory first-action
  directive), `.pi/mcp/agents-remember-settings.json`, `.pi/mcp.json` (the Pi project
  override consumed by the adapter), and `.pi/skills/`.
- Skills: Pi loads skills from project `.pi/skills` and `.agents/skills`, global
  `~/.pi/agent/skills` and `~/.agents/skills`, settings entries, package entries and repeated
  `--skill <path>` flags. Pi can discover `SKILL.md` directories recursively, but skill names
  should still match their parent folder for clean validation. First-run setup does not
  install skills; the copied package already carries them.
- MCP: Pi installs missing project packages on startup; the page prints the `.pi/mcp.json`
  entry with `uvx ... --config <projects>/.pi/mcp/agents-remember-settings.json`, and points
  to `/mcp` for adapter status and `/mcp setup` to adopt existing host-specific configs.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step; the retirement appears only in that
one sentence.

The page is instructions, not proof: it does not show that Pi installed the adapter, that
the extension ran, that the renderer ran, or that `runtime_install()` executed. Pi's skill
roots, its package installation and its adapter behaviour are stated as the page's account
of that harness.

## Evidence

- Pi core has no built-in MCP client; the starter package uses `pi-mcp-adapter`. [1]
- Copy `.pi/`, render with `--repo`, start or reload Pi once; manual replacement is the stated alternative. [2]
- Package contents: settings, startup extension, authority settings, project MCP override, skills. [3]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [4]
- Skill roots, recursive discovery with the parent-folder naming rule, and the no-install first-run rule. [5]
- The `.pi/mcp.json` entry, `/mcp` and `/mcp setup`. [6]
