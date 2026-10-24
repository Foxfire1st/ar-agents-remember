# docs/install/openclaw.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The OpenClaw install page: what to copy from the repository's `.openclaw/` starter package,
how to render it, which registry file the MCP definition merges into, and how the workspace
`AGENTS.md` carries the first-action directive.

## What The Page Establishes

- OpenClaw uses an agent workspace whose files and skill folders carry the wiring; MCP server
  definitions live in the OpenClaw config registry under `mcp.servers`.
- The install is: copy `.openclaw/` to the shared workspace root, run the copied
  `.openclaw/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), merge `.openclaw/openclaw.merge.json` into
  `~/.openclaw/openclaw.json`, then restart the gateway or start OpenClaw.
- The renderer infers the workspace root from the copied `.openclaw/` folder, fills path and
  repository placeholders, validates that each named repository exists, and leaves the merge
  file ready. The manual alternative is the same replacements by hand with no placeholder
  left behind.
- Package contents the page names: `.openclaw/openclaw.merge.json` (points
  `agents.defaults.workspace` at the package workspace and registers the server under
  `mcp.servers`), `.openclaw/mcp/agents-remember-settings.json`, `.openclaw/workspace/AGENTS.md`,
  and `.openclaw/workspace/skills/`. Where an OpenClaw workspace already exists, the page says
  to copy the contents of `.openclaw/workspace/` into it instead of changing
  `agents.defaults.workspace`.
- Instruction surface: the workspace `AGENTS.md` bootstrap file is the first-action
  authority, pointing at the readable `ar-coordination/AGENTS.md` path. The page states that
  OpenClaw's documented file-based hook surface is for gateway automation and lifecycle
  events, not a project-local MCP starter, which is why the package uses the bootstrap file.
  A target repository's root `AGENTS.md` is not overwritten.
- MCP: the registry entry under `mcp.servers` is printed, with the verification commands
  `openclaw mcp status --verbose`, `openclaw mcp doctor`, and
  `openclaw mcp probe agents-remember` for a live connection.
- Skills: OpenClaw loads bundled, managed/local (`~/.openclaw/skills`) and workspace skills
  (`<workspace>/skills`) with workspace skills taking precedence; the package uses
  `.openclaw/workspace/skills`. First-run setup does not install skills, and starter copies
  are kept current with the repository's skill-sync script. `openclaw skills list` and
  `openclaw skills check` inspect visibility.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id for those
retired search providers, no provider setting and no provider command, and gives no enable,
start, index or query step. Its only other use of the word "provider" is OpenClaw's own
model-provider timeout configuration in the long-running-turns section, which is the
harness's model routing and not the retired search providers.

The page is instructions, not proof: it does not show that the registry merge was accepted,
that the gateway restarted, that the bootstrap file loaded, that the probe connected, or that
`runtime_install()` executed. OpenClaw's registry layout and discovery order are the page's
account of that harness.

## Evidence

- Copy `.openclaw/` to the shared workspace root, render with `--repo`, merge the registry template, restart the gateway or start OpenClaw. [1]
- Package contents and the copy-into-existing-workspace alternative. [2]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [3]
- Workspace `AGENTS.md` is the first-action authority; the file-based hook surface is scoped to gateway automation. [4]
- `mcp.servers` registration plus status/doctor/probe commands. [5]
- Workspace skill precedence, flat package layout, and skill list/check commands. [6]
- The long-running-turns section configures model-provider timeouts and a gateway restart. [7]
