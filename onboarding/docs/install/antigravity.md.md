# docs/install/antigravity.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Antigravity install page: what to copy from the repository's `.agents/` starter
package into a workspace, how to render that copy in place, and where Antigravity reads
its workspace context, skills and MCP registration. It closes the install with the
`c-13-install-and-onboard` skill.

## What The Page Establishes

- The install is: copy `.agents/` to the workspace root, run the copied
  `.agents/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), then start or reload Antigravity once from that workspace.
- The renderer is a convenience, not the only route. It infers the workspace root from the
  copied `.agents/` folder, fills path and repository placeholders, writes the installed
  `GEMINI.md`, and validates that each named repository exists. The manual alternative is
  to make the same replacements by hand and carry or merge the directive into `GEMINI.md`,
  checking that no placeholder token remains.
- An existing workspace `GEMINI.md` is merged, not replaced, before the renderer is rerun.
  The template is kept under `.agents/` in the source checkout so the repository root stays
  reserved for its own `AGENTS.md`.
- Package contents the page names: `.agents/GEMINI.md` (the mandatory first-action
  directive), `.agents/mcp_config.json` (workspace-local MCP registration),
  `.agents/mcp/agents-remember-settings.json` (MCP authority settings), and
  `.agents/skills/`.
- Antigravity reads workspace `GEMINI.md` and `AGENTS.md` and global `~/.gemini/GEMINI.md`.
  Workspace skills are discovered at `.agents/skills/<skill-name>/SKILL.md`; global skills
  live under `~/.gemini/antigravity/skills/` for the IDE and
  `~/.gemini/antigravity-cli/skills/` for the CLI. The copied package already carries one
  flat folder per skill, so first-run setup does not install skills.
- MCP: the CLI reads `.agents/mcp_config.json`, and the IDE exposes a raw config at
  `~/.gemini/config/mcp_config.json`. The page prints the `uvx ... agents-remember-mcp
  --config <projects>/.agents/mcp/agents-remember-settings.json` registration and sends the
  reader to `/mcp` or the IDE MCP Store's raw config view to confirm the server is visible.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The page's own closing sentence states that nothing
  provider-side starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, no provider
setting, no provider command, and gives no enable, start, index or query step; the retired
providers appear only in that one sentence scoping the install skill.

The page is instructions for a person and an agent. It is not evidence that a package was
copied, that a renderer ran, that Antigravity restarted, that an MCP server registered, or
that `runtime_install()` executed on any machine. Its statements about Antigravity's
discovery paths and IDE/CLI config locations are the page's account of that harness, not an
independent check of it.

## Evidence

- Copy `.agents/`, render with `--repo`, start or reload Antigravity once; manual replacement is the stated alternative. [1]
- The renderer writes `GEMINI.md`, validates each named repository, and an existing `GEMINI.md` is merged first. [2]
- The package is listed as `GEMINI.md`, `mcp_config.json`, `mcp/agents-remember-settings.json`, `skills/`. [3]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [4]
- Workspace and global instruction files, skill roots, MCP config location and the `uvx` registration are stated. [5]
