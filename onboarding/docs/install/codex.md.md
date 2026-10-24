# docs/install/codex.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Codex install page: the two things Codex needs (the Agents Remember MCP server in Codex
config, and Codex-visible skills and startup instructions from the `.codex/` starter
package), how to render that copied package, and where each file sits.

## What The Page Establishes

- The install is: copy `.codex/` to the workspace root, run the copied
  `.codex/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), then restart Codex once.
- The renderer infers the workspace root from the copied `.codex/` folder, fills path and
  repository placeholders, writes the Python hook command, and validates that each named
  repository exists. The manual alternative is the same replacements by hand with no
  placeholder left behind.
- Package contents the page names: `.codex/config.toml` (MCP registration and `SessionStart`
  hook registration), `.codex/hooks/agents-remember-session-start.*`,
  `.codex/mcp/agents-remember-settings.json`, and `.codex/skills/`.
- Instruction surface: a repository's own root `AGENTS.md` is not overwritten for this
  wiring. The copied `SessionStart` hook is the first-run instruction surface, and it emits
  the workspace directive that points at `ar-coordination/AGENTS.md`, with an absolute path
  required when the coordination runtime sits outside the workspace. The starter package
  already includes that hook, so first-run setup does not install hooks.
- Skills: the copied package carries one flat folder per skill under
  `.codex/skills/<skill-name>/`, and first-run setup does not install them.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step; the retirement appears only in that
one sentence.

The page is instructions, not proof: it does not show that the hook fired, that `config.toml`
was accepted, that the renderer ran, or that `runtime_install()` executed. What Codex does
with `config.toml`, `SessionStart` hooks and skill folders is the page's account of that
harness.

## Evidence

- Codex needs the MCP server in config plus skills and startup instructions from `.codex/`. [1]
- Copy `.codex/`, render with `--repo`, restart once; manual replacement is the stated alternative. [2]
- Package contents include `config.toml` with MCP and hook registration, the hook files, authority settings and skills. [3]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [4]
- The copied `SessionStart` hook is the first-run instruction surface; root `AGENTS.md` is left alone; skills stay flat under `.codex/skills/`. [5]
