# mcp/README.md

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/README.md` is the PyPI-facing README for the installable
`agents-remember-mcp` package and the first-use MCP registration/Bootstrap guide. It opens
with server registration and the one-call Bootstrap Quickstart, then documents requirements,
install/run (local-wheel first for this checkout's server; since 260703 L3 also the umbrella CLI:
`uv tool install` of the locally built wheel + `agents-remember dashboard`
with daemon mode and the historical published pin named as the Python 3.13 artifact), an authority settings example,
harness registration, the post-restart Bootstrap call, and the high-level tool
surface.

## Code Commentary

### Logic

The README is self-contained so the rendered PyPI page can explain first use without an installed starter tree. Its Quickstart registers the MCP server with an absolute authority settings path, restarts the harness if needed, then calls role_start once for bootstrap with a fresh request UUID. The answer names the instructed seat and its dashboard/chat. Refusal recovery retries the same UUID; a source checkout uses its locally built wheel for the server. Skills are package-served MCP resources, and optional native files carry only the first-action directive. Bootstrap reads or initializes memory and settings, then tells the user to start Architect; it authors no onboarding/knowledge and starts no other role. Provider setup/index/watch stays retired.

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

The Settings File Location guidance separates MCP authority from the user's role-harness selections. Native harness registration points to an absolute MCP settings file; the normal first-run chain is registration, any required restart, then the Bootstrap call. The separate maintenance example retains server_info, runtime_install and context_packet for an explicitly requested runtime refresh. runtime_install retains provider-copy/cache knobs without starting provider install/index/watch. Host facts live in paseoRuntime in the active MCP authority file and are read at use time; user settings are a separate surface. The workspace-first coordinationRoot default, historical providerSeconds-to-providerSetupSeconds rename, unused-provider diagnostics, read-only container inspection and memory/worktree Git identity guidance remain.

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
- Keep MCP registration bound to its absolute authority settings file, separate from user role-harness settings.
- Keep skills package-served; optional native files carry the first-action directive rather than an installed skill tree.
- Keep registration → required harness restart → one Bootstrap call distinct from explicitly requested runtime maintenance. Provider stop/unused-key reporting is separate from the asked-only providers-remove CLI.
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


- The PyPI package declares the `agents-remember-mcp` console script and uses this README as project metadata. [2]
- The Quickstart registers MCP, restarts if needed, then makes one Bootstrap call; skills are package resources and maintenance remains separate. [3]

- The `providerSeconds` → `providerSetupSeconds` rename and the fail-loud `ConfigError` on the old key are enforced in MCP config. [5]
- The `runtime_install` flags the README documents (`install_provider_deps`, `no_cache`) and the runner-integrity manifest behind `runnerIntegrityFailed` are owned by the install/runtime layer. [6]



- Host bootstrap accepts the contract uv minimum or newer, installs none, and permits self-updating installations. [13]

## 260821-DAGQC-L2 Memory-Quality Call Grammar

This dated section records the earlier replacement of flat wait/run-id grammar with
the strict `memory_quality_check` request object. The current README Quickstart uses the Bootstrap role call; the separate maintenance example
shows `server_info`, `runtime_install` and `context_packet`; the historical wording
is not a claim that an MQC example remains in that section.

## 260928-MIK-L96 Host install and start

The package's explicit install step reads host facts from paseoRuntime in the active MCP authority file and provisions the host pinned by the build contract on a Node the product brings; `agents-remember dashboard --daemon` makes sure both the dashboard and the host run. A dashboard start never installs or upgrades the host and a dashboard stop or restart never stops it; `dashboard --status` shows both states.


- The host step of the install. [9]

## Current retirement evidence







- Requirements and the development-runtime section state the bounded package line, the historical published range, and the canonical exact source build. [7]
- The dashboard command ensures the dashboard and starts or adopts the configured host; this path does not install it. [8]
- Package-first onboarding explicitly retires provider installation, indexing and watching. [10]
- Retained install knobs, unused provider keys and asked-only container removal do not re-enable provider setup. [11]
- The advertised families are the retained registrar tuple, not the README's broad historical tool labels. [12]









- The run command requires absolute MCP authority settings, rejecting user settings and coordinator system/settings.json; the package console entry delegates to server.main(). [1]

- The reference catalog introduces the tool surface; actual server registration and its registrar tuple own the advertised families and signatures, rather than every historical catalog row. [4]
