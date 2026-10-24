# docs/install/hermes.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The Hermes install page: what to copy from the repository's `.hermes/` starter package, how
to render it, where the project context file and the user-level config merge sit, and how
Hermes finds the skills. It closes the install with the `c-13-install-and-onboard` skill.

## What The Page Establishes

- The install is: copy `.hermes/` to the workspace root, run the copied
  `.hermes/render-starter` with a single `--repo` list (the page shows
  `--repo my-app shared-lib`), merge `.hermes/config.yaml` into `~/.hermes/config.yaml`,
  then start or reload Hermes from that workspace once.
- The renderer infers the workspace root from the copied `.hermes/` folder, fills path and
  repository placeholders, writes the installed `HERMES.md`, and validates that each named
  repository exists. The manual alternative is the same replacements by hand with the
  directive carried or merged into `HERMES.md` and no placeholder left behind.
- An existing workspace `HERMES.md` is merged, not replaced, before the renderer is rerun.
  The template is kept under `.hermes/` in the source checkout so the repository root stays
  reserved for its own `AGENTS.md`.
- Package contents the page names: `.hermes/HERMES.md` (template for the highest-priority
  project context file), `.hermes/config.yaml` (merge template for the user-level config),
  `.hermes/mcp/agents-remember-settings.json`, and `.hermes/skills/` (exposed through
  `skills.external_dirs`).
- Hermes reads `.hermes.md` or `HERMES.md` as highest-priority project context files and also
  supports `AGENTS.md` and `CLAUDE.md`; the template exists because `HERMES.md` is loaded
  before `AGENTS.md`. A repository's root `AGENTS.md` is not overwritten for this wiring.
- MCP: Hermes reads server configuration from `~/.hermes/config.yaml` under `mcp_servers`;
  the page prints the `uvx ... --config <projects>/.hermes/mcp/agents-remember-settings.json`
  entry to merge, and `/reload-mcp` for edits made while Hermes is running.
- Skills: the copied package carries one flat folder per skill under `.hermes/skills/`. A
  shared skills directory can be declared with `harnessSkillRoot` or added to
  `skills.external_dirs` in `~/.hermes/config.yaml`; `skills_install()` is for manual
  maintenance and non-package installs, not first-run setup.
- After the restart, `c-13-install-and-onboard` runs or verifies `runtime_install()` and
  then handles memory and onboarding. The closing sentence states that nothing provider-side
  starts because the two former search providers are retired.

## Boundaries

Provider setup is not among the install steps. The page names no provider id, setting or
command and gives no enable, start, index or query step; the retirement appears only in that
one sentence.

The page is instructions, not proof: it does not show that the config merge was accepted,
that `/reload-mcp` succeeded, that the renderer ran, or that `runtime_install()` executed.
Hermes' own context-file precedence and skill discovery are stated as the page's account of
that harness.

## Evidence

- Copy `.hermes/`, render with `--repo`, merge `config.yaml` into the user config, start or reload once. [1]
- Package contents: `HERMES.md`, `config.yaml` merge template, authority settings, skills exposed through `skills.external_dirs`. [2]
- `c-13-install-and-onboard` runs or verifies `runtime_install()` and covers memory and onboarding; nothing provider-side starts. [3]
- `HERMES.md` is loaded before `AGENTS.md`; root `AGENTS.md` is not overwritten. [4]
- MCP lives under `mcp_servers` in the user config with the printed `uvx` entry and `/reload-mcp`. [5]
- Skill layout, `harnessSkillRoot` / `skills.external_dirs`, and the no-install first-run rule are stated. [6]
