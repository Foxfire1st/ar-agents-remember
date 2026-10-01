# mcp/README.md

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
- Keep requirements practical and package-level: Python `>=3.13,<3.14`, uv/pip, an
  MCP-capable harness, Git, and Docker (plus Ollama for the grepai embedder) only
  when provider tools are enabled.
- Keep the Linux/WSL development-runtime section aligned with the canonical exact 3.13.15
  source-build contract. `scripts/bootstrap-mcp-venv.sh` is the supported project-venv path;
  system Python and uv-managed standalone interpreters are not substitutes.
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

## Evidence

### Repo-Internal References

- The run command requires an absolute `--config` path and rejects coordinator `system/settings.json`; `uvx agents-remember-mcp` and the pip console script both call `server.main()`. [1]
- The PyPI package declares the `agents-remember-mcp` console script and uses this README as project metadata. [2]
- The Quickstart has the user copy a harness starter package, render it either with the local `render-starter` convenience script or by manual placeholder replacement, wire MCP, restart once, and then hand post-restart setup off to the copied `c-13-install-and-onboard` skill, which runs or verifies `runtime_install()` and does not call `skills_install()` in package-based first-run setup. [3]
- The tool surface the README summarizes is exposed by the server/payload layer and catalogued in the tool reference. [4]
- The `providerSeconds` → `providerSetupSeconds` rename and the fail-loud `ConfigError` on the old key are enforced in MCP config. [5]
- The `runtime_install` flags the README documents (`install_provider_deps`, `no_cache`) and the runner-integrity manifest behind `runnerIntegrityFailed` are owned by the install/runtime layer. [6]
- Requirements and the development-runtime section state the bounded package line and canonical exact source build. [7]

## 260821-DAGQC-L2 Memory-Quality Call Grammar

The package quickstart now demonstrates the canonical `memory_quality_check` request object with an
explicit mode instead of the removed flat wait/run-id surface. This is a contract replacement, not
a compatibility example: sync/start execution fields and poll identity are separate strict shapes.
