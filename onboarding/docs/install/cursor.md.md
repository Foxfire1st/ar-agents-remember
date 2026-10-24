# docs/install/cursor.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Cursor install page: what to copy from the repository's `.cursor/` starter package, how
to render it, and which Cursor surfaces carry the first-action directive, the project MCP
registration and the skills. It closes the install with the `c-13-install-and-onboard` skill.

## What The Page Establishes

- The install is: copy `.cursor/` to the workspace root, run the copied
  `.cursor/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), then open or restart the workspace in Cursor once.
- The renderer infers the workspace root from the copied `.cursor/` folder, fills path and
  repository placeholders, writes the Python hook command, and validates that each named
  repository exists. The manual alternative is the same replacements by hand with no
  placeholder left behind.
- Package contents the page names: `.cursor/rules/agents-remember.mdc` (an always-applied
  first-action instruction pointing at `ar-coordination/AGENTS.md`), `.cursor/hooks.json`
  with `.cursor/hooks/agents-remember-session-start.py` (project `sessionStart` hook),
  `.cursor/mcp.json` (project-local MCP registration), `.cursor/mcp/agents-remember-settings.json`,
  and `.cursor/skills/`.
- The always-applied rule is called the dependable instruction surface because Cursor
  documents `sessionStart` as fire-and-forget; the hook is described as the second carrier,
  not the guarantee. A repository's root `AGENTS.md` is not overwritten for this wiring, and
  an absolute path is needed when `ar-coordination` sits outside the workspace.
- Cursor loads skills from `.agents/skills`, `.cursor/skills`, `~/.agents/skills` and
  `~/.cursor/skills`, and also supports Claude and Codex compatibility folders. The copied
  package already carries one flat folder per skill in `.cursor/skills/`, so first-run setup
  does not install skills.
- MCP: project config lives at `.cursor/mcp.json`; the page prints the `uvx ...
  agents-remember-mcp --config <projects>/.cursor/mcp/agents-remember-settings.json`
  registration.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step; the retirement appears only in that
one sentence.

The page is instructions, not proof: nothing in it shows that the rule loaded, that the hook
fired, that Cursor accepted `.cursor/mcp.json`, that the renderer ran, or that
`runtime_install()` executed. Which surfaces Cursor honours, and whether the hook is
delivered, are the page's account of that harness.

## Evidence

- Copy `.cursor/`, render with `--repo`, open or restart the workspace in Cursor once. [1]
- Package contents: always-applied rule, `sessionStart` hook, project MCP registration, authority settings, skills. [2]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [3]
- The rule is the dependable surface; `sessionStart` is documented as fire-and-forget. [4]
- Project MCP config path and the `uvx` registration are printed. [5]
- Skill roots, flat package layout, and the no-install first-run rule are stated. [6]
