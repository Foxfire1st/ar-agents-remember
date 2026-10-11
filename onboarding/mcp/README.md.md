# mcp/README.md

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/README.md` is the PyPI-facing README for the installable
`agents-remember-mcp` package and the de-facto pre-MCP bootstrap doc. It opens
with the package-first, one-restart Quickstart, then documents requirements,
install/run (local-wheel first for this checkout's server; since 260703 L3 also the umbrella CLI:
`uv tool install` of the locally built wheel + `agents-remember dashboard`
with daemon mode and the historical published pin named as the Python 3.13 artifact), a starter settings block,
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
placeholder replacement; (2) build the checkout's wheel (`uv build --wheel mcp`
at the repository root) and wire `agents-remember-mcp` with
`uvx --python 3.14 --from <abs built-wheel.whl> agents-remember-mcp --config
<abs settings.json>` using the copied package's settings file and restart the
harness once; (3) invoke the copied `c-13-install-and-onboard` skill to run or
verify `runtime_install()`, choose new vs existing memory and bootstrap onboarding.
Provider indexing is retired: no provider install, index or watch step runs, even
with old enabled settings. Copied starter packages already provide the initial
skills and harness files; the removed model-facing `skills_install` operation is
not a first-run or maintenance instruction. The Requirements section clarifies that Claude Code
hooks do not require `jq`; `jq` was only a legacy starter one-liner dependency,
and current starter packages use Python renderers and Python hook scripts.

The Install And Run section (260703 L3) adds the mission-control CLI story after
the server forms: the package ships the umbrella `agents-remember` CLI carrying
the `dashboard` subcommand — for this checkout build and sync the dashboard
bundle, build the wheel, install that local artifact as a uv tool
(`uv tool install --python 3.14 <wheel>`), and the `dashboard` subcommand
discovers `--config` itself (nearest `.claude/mcp/agents-remember-settings.json`
or the `.mcp.json`-recorded path), `--daemon` detaches it with `--status`/`--stop`
management and state under `<coordinationRoot>/logs/dashboard/`, and the
`"dashboard": {"autoStart": true}` settings key has every MCP boot ensure the
daemon with restart-on-version-mismatch. The published `3.0.0rc8` pin is named
as the historical Python 3.13 artifact, not as an installation example for this
Python 3.14 build; the source and published artifacts share the version string
while an official release of the 3.14 build is pending.

Beyond the Quickstart the README now carries the operational detail a first-run
needs: a **Settings file location** table mapping each harness starter package
to its package-provided settings path, a **Harness Setup** section that tells
readers to prefer the copied starter package because it carries skills,
hooks/rules/instructions, and the settings template together, an **Install
Order And First Operations** section spelling out the strict package + MCP
wiring → one harness restart → runtime/onboarding order, and the
`runtime_install` flags: `install_provider_deps` scopes the providers-tree copy
(dependency-skipped copies preserve live runner state), while `no_cache` rebuilds
nothing provider-side. Neither starts provider installation, indexing or watching.
The skills note says copied packages already include one flat folder per skill;
it advertises no separate skill-install tool. The README keeps the historical upgrade callout that
`timeoutCaps.providerSeconds` was renamed to `providerSetupSeconds` (old key
rejected with `ConfigError`; the former image-build/dependency cap is inactive
for retired providers), plus Troubleshooting for uvx index lag, read-only inspection
of pre-retirement provider containers, and the git-identity placeholder
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
- Keep requirements practical and package-level: Python `>=3.14,<3.15`, uv/pip, an
  MCP-capable harness and Git. Docker/Ollama requirements describe historical
  leftover containers, not enabled provider tools or a required new setup step.
- Host environment setup uses the PATH uv at `AR_UV_VERSION` or newer; it installs no uv.
  A self-updating uv works without a product-managed copy. The certified container still
  installs the exact contract uv; the host minimum does not relax the Python runtime pin.
- Keep the Linux/WSL development-runtime section aligned with the canonical exact 3.14.8
  source-build contract. `scripts/bootstrap-mcp-venv.sh` is the supported project-venv path;
  system Python and uv-managed standalone interpreters are not substitutes.
- Keep the Settings file location guidance accurate for package-first setup:
  the copied starter package owns the expected settings path, and that path
  must stay under the harness registration folder, not loose in the workspace
  root and not inside `ar-coordination/`.
- Keep the skill-install note correct: copied starter packages provide first-run
  skills in one flat folder per skill. Retained runtime copying behind the product
  does not make the removed skill-install tool callable.
- Keep the install-order rationale intact: package + MCP wiring → one harness
  restart → runtime/onboarding. The installer stops leftover watchers and reports
  old enabled provider keys as unused; it starts no retired provider setup. Its
  stop/report behavior is distinct from the separately requested destructive
  `providers-remove` CLI command.
- Keep the warning that benchmark execution runs untrusted code, but distinguish
  the retained runner/CLI from the removed benchmark MCP tools. The README's broad
  Tool Surface/benchmark callout is not the authoritative advertised roster;
  actual availability comes from the retained registrars and public-tool set.

### Provider retirement and README repair

The troubleshooting paragraph now treats Docker, Ollama and automatic model pulling
as pre-retirement history. Inspection does not restore a provider setup workflow:
`runtime_install` stops leftover watchers and reports unused keys, and container
removal is asked-only. Core by-path memory/onboarding does not depend on providers.
Do not reinterpret the historical setup descriptions or retained configuration knobs
as current install/start/index/watch authority.

## Evidence

### Repo-Internal References

- The run command requires an absolute `--config` path and rejects coordinator `system/settings.json`; `uvx agents-remember-mcp` and the pip console script both call `server.main()`. [1]
- The PyPI package declares the `agents-remember-mcp` console script and uses this README as project metadata. [2]
- The Quickstart has the user copy/render a starter package, wire MCP and restart once; the copied install/onboard skill owns runtime/memory/onboarding without provider installation or indexing. [3]
- The server/registrars and tool reference determine actual exposure; broad historical README labels are not a promise that removed tools remain callable. [4]
- The `providerSeconds` → `providerSetupSeconds` rename and the fail-loud `ConfigError` on the old key are enforced in MCP config. [5]
- The `runtime_install` flags the README documents (`install_provider_deps`, `no_cache`) and the runner-integrity manifest behind `runnerIntegrityFailed` are owned by the install/runtime layer. [6]

- Requirements and the development-runtime section state the bounded package line, the historical published range, and the canonical exact source build. [7]

- Host bootstrap accepts the contract uv minimum or newer, installs none, and permits self-updating installations. [13]

## 260821-DAGQC-L2 Memory-Quality Call Grammar

This dated section records the earlier replacement of flat wait/run-id grammar with
the strict `memory_quality_check` request object. The current README quickstart instead
shows `server_info`, `runtime_install` and `context_packet`; the historical wording
is not a claim that an MQC example remains in that section.

## 260928-MIK-L96 Host install and start

The package's install step provisions the host pinned by the build contract on a Node the product brings; `agents-remember dashboard --daemon` makes sure both the dashboard and the host run. A dashboard start never installs or upgrades the host and a dashboard stop or restart never stops it; `dashboard --status` shows both states.

- The dashboard command that starts both. [8]
- The host step of the install. [9]

## Current retirement evidence

- Package-first onboarding explicitly retires provider installation, indexing and watching. [10]
- Retained install knobs, unused provider keys and asked-only container removal do not re-enable provider setup. [11]
- The advertised families are the retained registrar tuple, not the README's broad historical tool labels. [12]
