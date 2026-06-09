# mcp/src/agents_remember/providers/cgc/lifecycle/installation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/installation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T06:20+02:00|
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03` |
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`installation.py` owns CodeGraphContext install, status, and doctor
operations.

## Code Commentary

### Logic

The module installs the CGC Docker runner image, cleans old source artifacts,
reports Docker-image patch status as a field of install/status/doctor results,
initializes runtime layout state, and runs doctor checks through the runner
image. Status now inspects the watcher container, requires it to be running for
`ok`, includes normalized container state, reports `lastRefresh` from runtime
state, and exposes an `indexingState` field for MCP current-state consumers.

`indexingState` comes from a real probe chain, not container liveness alone.
`cgc_indexing_state_probe()` first checks scan markers in the watcher's
container logs since container start: `Performing initial scan` without a
matching `Initial scan complete` means `indexing`. Otherwise
`cgc_graph_content_state()` queries the backend with `GRAPH.RO_QUERY`, counting
File nodes in the repo's graph, and classifies the result as `indexed`,
`empty`, `backend-unreachable`, or `unknown`. A running watcher over an empty
graph therefore reports `empty`, the state that exposed the 2026-06-09
silent-data-loss incident instead of masking it.
Install-all also coordinates backend installation and per-root install results
from settings. There is no longer a standalone public `patch` action: managed
patches are baked into the runner image during build, so patch state surfaces
only as a Docker-image marker within the install/status/doctor results. Host
site-packages patch inspection and host-venv patch application helpers have been
removed from this lifecycle path.

### Invariants And Boundaries

- Patches are owned by the Docker runner image build; status should report the
  Docker-image patch mode rather than inspecting host site-packages.
- CGC lifecycle code must not inspect, create, or patch a coordination-root
  host venv as an executable fallback.
- Runtime source artifacts under the code repository are cleanup targets; active
  provider runtime belongs under coordinator provider roots.
- Process start/stop and bounded CGC commands belong in sibling lifecycle
  modules and must use Docker runner commands.
- CGC status should not be ok when the runner image exists but the repo watcher
  container is not running.
- Graph content probes must use `GRAPH.RO_QUERY`, never `GRAPH.QUERY`: a plain
  query auto-creates an empty graph key as a side effect, so a read probe would
  manufacture the very `empty` state it is checking for.
- `redis-cli` exits 0 even when the server returns an error reply, so probe
  classification must inspect the reply text rather than trust the exit code.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC layout and backend settings come from the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| CGC backend install/start behavior is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker runner image build and command helpers live in the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-06-10T06:20+02:00 — Body-quality pass: merged the 2026-06-09 probe-chain mechanics into Logic and promoted the `GRAPH.RO_QUERY` and redis-cli exit-code rules to Invariants (documentation only).
- 2026-06-09T22:10+02:00 — `cgc_status` now derives `indexingState` from a real probe instead of hardcoded `"unknown"`: `cgc_indexing_state_probe()` reports `indexing` when the watcher's container logs show `Performing initial scan` without `Initial scan complete` since container start, otherwise `cgc_graph_content_state()` runs `GRAPH.RO_QUERY` (read-only on purpose — plain `GRAPH.QUERY` auto-creates empty graph keys) counting File nodes: `indexed` / `empty` / `backend-unreachable` / `unknown`. redis-cli exits 0 on error replies, so classification inspects reply text, not just the return code.
- 2026-05-31T12:30+02:00 — Removed the standalone public `cgc_patch` action (patch state now only surfaces as a docker-image field of install/status/doctor); narrowed `layout` params from `Any` to `CgcRuntimeLayout` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Fixed `commands` types in `cgc_install_dry_run_result`/`cgc_install_preflight` to `list[dict[str, Any]]`; behavior-preserving (commit `0549b28`).
- 2026-05-28T13:40+02:00: Updated after the remaining host-venv patch/status helper functions were removed from CGC lifecycle installation.
- 2026-05-28T12:32+02:00: Updated after CGC status began reporting watcher container state, last refresh, indexing state, and requiring the watcher to be alive.
- 2026-05-26T12:51+02:00: Updated after CGC install/status/doctor switched from host venvs to the Docker runner image.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC install, status, patch, and doctor logic extracted out of provider lifecycle.
