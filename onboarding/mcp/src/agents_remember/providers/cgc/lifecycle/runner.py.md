# mcp/src/agents_remember/providers/cgc/lifecycle/runner.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/runner.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Install/status/doctor behavior consumes runner image build and status helpers. | `cgc_install_commands`; `cgc_status`; `cgc_doctor` | mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:52-64; mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:317-352; mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:388-440 |
| Watcher process control consumes Docker watcher command helpers. | `cgc_start_watch_process`; `cgc_start_all_watch_process` | mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:89-101; mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:104-116 |
| Refresh and bounded query commands run through Docker command helpers. | `cgc_refresh_command`; `cgc_run_command` | mcp/src/agents_remember/providers/cgc/lifecycle/query.py:51-60; mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py:34-50 |

## Update History

- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped CGC lifecycle citation claims; final exact frozen-snapshot check is clean.
- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/providers/cgc/lifecycle/runner.py` since the L2 base commit is the
  whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s) with no token change
  whatsoever. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Removed the dead `cgc_runner_dockerfile()` text helper and tightened the `layout` param of `cgc_runner_image_build`/`cgc_watcher_inspect`/`cgc_watcher_running`/`cgc_runner_image_status` from `Any` to `CgcRuntimeLayout` (now imported from `core`); corrected Logic prose that implied the module "generates" the Dockerfile to reflect the static Dockerfile provider asset (1.0.0 review remediation).
- 2026-05-30T21:33+02:00: Documented the `no_cache` build path — `--no-cache` plus bypassing the skip-if-tag-exists shortcut for a from-scratch image rebuild. Verified against `8927f03`.
- 2026-05-26T13:58+02:00: Updated after CGC runner commands moved from `host.docker.internal` to the shared CGC Docker network and began passing host UID/GID into containers.
- 2026-05-26T12:51+02:00: Created when CGC provider execution moved from host venvs to a Docker runner image/container.
