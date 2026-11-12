# mcp/src/agents_remember/providers/cgc/lifecycle/runner.py

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`runner.py` owns the Docker runner image build and the watcher and image inspection
helpers for CodeGraphContext provider execution.

## Code Commentary

### Logic

The module builds the CGC runner image from the static `python:3.12-slim`
Dockerfile provider asset (resolved via `provider_asset_path`, no longer via a
`cgc_runner_dockerfile()` text helper), which installs the pinned
CodeGraphContext dependency set, copies the generated patch script into the build
context, applies the managed CGC patches inside the image, and records the image
lock after successful builds. When `no_cache` is set the build adds `--no-cache`
and bypasses the skip-if-tag-exists shortcut so the image is rebuilt from
scratch; otherwise an existing tagged image short-circuits the build. The image build,
status, and watcher inspect/running helpers take their `layout` argument typed as
`CgcRuntimeLayout` (imported from `core`) rather than a loose `Any`. Runtime helpers
build no watcher, bounded-command or visualizer command lines: Compose rendering lives
in `compose.py`, and `compose_runtime.py` plans and executes it. That render carries
the host-user block, the CGC environment variables, the Docker network and the FalkorDB
host name, and runs as the host UID/GID when supported so mounted runtime files remain
user-owned.

### Invariants And Boundaries

- CGC provider execution is Docker-owned; this module must not create or call a
  host Python virtual environment.
- The CGC patch set is baked into the runner image during image build.
- Docker runner containers must join the same network as FalkorDB and must not
  rely on host loopback access to the backend.
- Docker runner containers should run as the host user on POSIX hosts so
  mounted provider runtime files stay removable by runtime install.
- Runtime state remains under `providers/runners/codegraphcontext/`; durable
  backend data remains under `providers/data/codegraphcontext/`.
- Backend container lifecycle remains in `backend.py`.

## Evidence

### Repo-Internal References

- Install/status/doctor behavior consumes runner image build and status helpers. [1]
- Watcher process control consumes only this module's `cgc_watcher_running` inspection helper; its removal command is Compose's `rm -sf` on the watcher service, built in `process_control.py`, so this module builds no watcher command. [2]
