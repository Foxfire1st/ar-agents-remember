# mcp/README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/README.md`                            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T11:55+02:00 |
| lastVerifiedCommitHash | `38c56316207997da98d8408e1a3ada3c7525f4c6` |
| lastVerifiedCommitDate | 2026-07-03T11:47:48+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/README.md` is the PyPI-facing README for the installable
`agents-remember-mcp` package and the de-facto pre-MCP bootstrap doc. It opens
with the package-first, one-restart Quickstart, then documents requirements,
install/run (uvx-first for the server; since 260703 L3 also the umbrella CLI:
unpinned `uv tool install agents-remember-mcp` + `agents-remember dashboard`
with daemon mode and the rc-period pre-release note), a starter settings block,
harness registration, the post-restart MCP calls, and the high-level tool
surface.

## Code Commentary

### Logic

The README is self-contained for the bootstrap so it works from the rendered
PyPI page without a source checkout. It now leads with the same package-first
three-step Quickstart as the root docs: (1) copy the harness-native starter
package from the source repo and render the copied package. The
`render-starter` script is a convenience that infers the workspace root from
the copied harness folder, accepts one explicit `--repo` list, and fills path,
repository, and hook-command placeholders; the docs also allow manual
placeholder replacement; (2) wire
`agents-remember-mcp` with `uvx agents-remember-mcp@latest --config
<abs settings.json>` using the copied package's settings file and restart the
harness once; (3) invoke the copied `c-13-install-and-onboard` skill to run or
verify `runtime_install()`, choose new vs existing memory, bootstrap onboarding,
and start provider indexing when enabled. It explicitly says
`skills_install()` is maintenance/manual only in the normal package-based
first-run path because the copied starter package already provides the initial
skills and harness files. The Requirements section clarifies that Claude Code
hooks do not require `jq`; `jq` was only a legacy starter one-liner dependency,
and current starter packages use Python renderers and Python hook scripts.

The Install And Run section (260703 L3) adds the mission-control CLI story after
the server forms: the package ships the umbrella `agents-remember` CLI carrying
the `dashboard` subcommand — install unpinned as a uv tool (latest stable,
first-class; pinning `==X.Y.Z` / `uvx --from` is the debugging path), `dashboard`
discovers `--config` itself (nearest `.claude/mcp/agents-remember-settings.json`
or the `.mcp.json`-recorded path), `--daemon` detaches it with `--status`/`--stop`
management and state under `<coordinationRoot>/logs/dashboard/`, and the
`"dashboard": {"autoStart": true}` settings key has every MCP boot ensure the
daemon with restart-on-version-mismatch. One pre-release note covers the rc
period: `3.0.0rcN` is skipped by default resolution — `--prerelease allow` for
the tool install, an explicit pin for the registration instead of `@latest`.

Beyond the Quickstart the README now carries the operational detail a first-run
needs: a **Settings file location** table mapping each harness starter package
to its package-provided settings path, a **Harness Setup** section that tells
readers to prefer the copied starter package because it carries skills,
hooks/rules/instructions, and the settings template together, an **Install
Order And First Operations** section spelling out the strict package + MCP
wiring → one harness restart → runtime/onboarding order, and the
`runtime_install` flags (`install_provider_deps`, `no_cache` to force a
from-scratch image rebuild). The skills note says copied packages already
include the harness-native skills while `skills_install()` remains available
for manual maintenance and non-package installs, copying one flat folder per
skill at `<skill-root>/<name>/`. The README keeps the upgrade callout that
`timeoutCaps.providerSeconds` was renamed to `providerSetupSeconds` (old key
rejected with `ConfigError`; `providerSetupSeconds` caps only image build /
dependency install; `0` means unlimited), plus Troubleshooting for uvx index
lag, `degraded` providers / Ollama recovery, and the git-identity placeholder
for memory/worktree commits. The settings guidance keeps the workspace-first
default: `coordinationRoot` defaults to `<workspace>/ar-coordination/`, inside
the workspace and never the user's home directory.

### Invariants And Boundaries

- Keep this README focused on the MCP package and its bootstrap, not the whole
  product manual.
- Keep it self-contained for pip/PyPI readers: inline the starter settings and
  use absolute GitHub URLs (no source-checkout-relative `../` links that 404 on
  the PyPI page).
- Keep the run command aligned with `agents_remember.mcp.server.main()`, which
  requires `--config`; both `uvx agents-remember-mcp` and the pip console command
  invoke it.
- Keep requirements practical and package-level: Python 3.11+, uv/pip, an
  MCP-capable harness, Git, and Docker (plus Ollama for the grepai embedder) only
  when provider tools are enabled.
- Keep the Settings file location guidance accurate for package-first setup:
  the copied starter package owns the expected settings path, and that path
  must stay under the harness registration folder, not loose in the workspace
  root and not inside `ar-coordination/`.
- Keep the skill-install note correct: starter packages provide first-run
  skills. `skills_install()` remains maintenance/manual; when used, it copies
  one flat folder per skill (`<skill-root>/<name>/`, matching the skill's
  lowercase `name`) and has **no layout option** (the `tree`/`flat` `layout`
  input was removed in 2.0.0).
- Keep the install-order rationale intact: package + MCP wiring → one harness
  restart → runtime/onboarding. `runtime_install` can build provider images,
  but indexing starts later through `c-13-install-and-onboard`, so "providers
  last" means indexing, not image builds.
- Keep the benchmark-safety callout intact: `codex_benchmark_prepare`/
  `codex_benchmark_run` are opt-in, refused unless settings set
  `"benchmarksEnabled": true`; a real run (`dry_run=false`) clones third-party
  repos and runs the Codex CLI, and `codex_sandbox` defaults to Codex's `default`
  sandbox with `danger-full-access` reserved for trusted local runs (full host
  access). The README must keep warning that benchmark execution runs untrusted
  code.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The run command requires an absolute `--config` path and rejects coordinator `system/settings.json`; `uvx agents-remember-mcp` and the pip console script both call `server.main()`. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py); [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The PyPI package declares the `agents-remember-mcp` console script and uses this README as project metadata. | [pyproject.toml](agents-remember/mcp/pyproject.toml) |
| The Quickstart has the user copy a harness starter package, render it either with the local `render-starter` convenience script or by manual placeholder replacement, wire MCP, restart once, and then hand post-restart setup off to the copied `c-13-install-and-onboard` skill, which runs or verifies `runtime_install()` and does not call `skills_install()` in package-based first-run setup. | [`c-13-install-and-onboard` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-13-install-and-onboard/SKILL.md) |
| The tool surface the README summarizes is exposed by the server/payload layer and catalogued in the tool reference. | [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py); [mcp-tools.md](agents-remember/docs/reference/mcp-tools.md) |
| The `providerSeconds` → `providerSetupSeconds` rename and the fail-loud `ConfigError` on the old key are enforced in MCP config. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The `runtime_install` flags the README documents (`install_provider_deps`, `no_cache`) and the runner-integrity manifest behind `runnerIntegrityFailed` are owned by the install/runtime layer. | [runtime.py](agents-remember/mcp/src/agents_remember/install/runtime.py) |

## Update History

- 2026-07-03T11:55+02:00 — 260703 L3: Install And Run gains the umbrella-CLI story — unpinned
  `uv tool install agents-remember-mcp` first-class, discovery-backed flag-free `dashboard`,
  daemon mode + the `dashboard.autoStart` settings key, pinning as the debugging path, and the
  rc-period pre-release note (`--prerelease allow` / explicit registration pin). Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-11T14:07+02:00: Re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-11T06:47+02:00: No content impact: the Tool Surface bullet changed from "chat/direct closeout and worktree-backed task workflows" to "worktree-backed closeout and task workflows" (issue #62 worktree-only closeout); the bootstrap structure this sidecar describes is unchanged.
- 2026-06-06T18:42+02:00: Refined the PyPI-facing quickstart memory so the renderer is an optional convenience script for placeholder replacement and manual replacement is explicit. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:19+02:00: Refined the PyPI-facing quickstart memory after renderers dropped the separate workspace-root flag; copied packages now infer the workspace root and accept one `--repo` list. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T16:45+02:00: Updated the PyPI-facing quickstart memory for harness-local `render-starter` scripts and the Claude Code `jq` correction; the setup path now renders copied package placeholders, repository scope, and hook commands before MCP wiring. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T19:25+02:00: Corrected the PyPI-facing package README for the 2.3.1 patch release: package-first starter package setup, one restart, `c-13-install-and-onboard` after MCP wiring, and `skills_install()` as maintenance/manual only. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — documented the workspace-first settings default: `coordinationRoot` at `<workspace>/ar-coordination/` and the settings file under `<workspace>/<harness-folder>/mcp/`, inside the workspace and never the user's home directory. fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T11:00+02:00: Removed the stale `tree`/`flat` skill-layout language after confirming `skills_install` has no `layout` arg (removed in 2.0.0) — it copies one flat folder per skill at `<skill-root>/<name>/`. Updated the Logic note and the skill-install invariant; `README.md`, `docs/getting-started.md`, `docs/reference/mcp-tools.md`, and the per-harness install pages were corrected in the same pass (docs/** are outside file-level onboarding). Verification metadata stays pinned until closeout. fix/skills-install-layout-docs branch.
- 2026-05-31T12:30+02:00 — Captured the README's new benchmark-safety callout (1.0.0 review remediation): `codex_benchmark_prepare`/`codex_benchmark_run` are opt-in behind `benchmarksEnabled: true`, real runs run untrusted code, and `codex_sandbox` defaults to `default` with `danger-full-access` opt-in.
- 2026-05-30T21:22+02:00: Verified against `57944df` after the 0.9.0–0.9.4 run. Documented the README sections added since `412342847` — Settings file location (the `mcp`-parent rule that lets `skills_install` infer its target), Install Order And First Operations (scaffolding → skills → providers, `runnerIntegrityFailed`, `install_provider_deps`/`no_cache`), the `tree` vs `flat` skill-layout note, the `providerSeconds` → `providerSetupSeconds` rename, and Troubleshooting — and added matching invariants and references.
- 2026-05-29T14:15+02:00: Rewrote the README as a self-contained, uvx-first bootstrap — added the 3-step "ask your agent to" Quickstart (hands off to `c-13-install-and-onboard` skill), inlined a starter `settings.json`, switched project-doc links to absolute GitHub URLs, and linked the MCP tool reference. Metadata pending closeout refresh.
- 2026-05-28T15:52+02:00: Updated after the MCP package README added the canonical source checkout link.
- 2026-05-28T15:43+02:00: Created after the MCP package gained a dedicated README and `pyproject.toml` started using it as package metadata. Verification metadata remains pinned until closeout commits the source change.
