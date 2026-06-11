# mcp/src/agents_remember/providers/cgc/lifecycle/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                                  |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`runner.py` owns the Docker runner image and command construction for
CodeGraphContext provider execution.

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
`CgcRuntimeLayout` (imported from `core`) rather than a loose `Any`. Runtime helpers build Docker command lines for
bounded CGC commands, visualizer commands, and long-running watcher containers.
Those commands mount the provider instance root and code repository at their
host paths, run as the host UID/GID when supported so mounted runtime files
remain user-owned, set CGC environment variables through `-e`, join the CGC
Docker network, and route FalkorDB access through the backend container name.

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Install/status/doctor behavior consumes runner image build and status helpers. | [installation.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py) |
| Watcher process control consumes Docker watcher command helpers. | [process_control.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py) |
| Refresh and bounded query commands run through Docker command helpers. | [refresh.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py); [query.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/query.py) |

## Update History

- 2026-05-31T12:50+02:00 — Removed the dead `cgc_runner_dockerfile()` text helper and tightened the `layout` param of `cgc_runner_image_build`/`cgc_watcher_inspect`/`cgc_watcher_running`/`cgc_runner_image_status` from `Any` to `CgcRuntimeLayout` (now imported from `core`); corrected Logic prose that implied the module "generates" the Dockerfile to reflect the static Dockerfile provider asset (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `no_cache` build path — `--no-cache` plus bypassing the skip-if-tag-exists shortcut for a from-scratch image rebuild. Verified against `8927f03`.
- 2026-05-26T13:58+02:00: Updated after CGC runner commands moved from `host.docker.internal` to the shared CGC Docker network and began passing host UID/GID into containers.
- 2026-05-26T12:51+02:00: Created when CGC provider execution moved from host venvs to a Docker runner image/container.
