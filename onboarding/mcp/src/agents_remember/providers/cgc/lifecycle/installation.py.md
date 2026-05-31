# mcp/src/agents_remember/providers/cgc/lifecycle/installation.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/installation.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00|
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC layout and backend settings come from the CGC core module. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py) |
| CGC backend install/start behavior is delegated to the backend module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker runner image build and command helpers live in the runner module. | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Update History

- 2026-05-31T12:30+02:00 — Removed the standalone public `cgc_patch` action (patch state now only surfaces as a docker-image field of install/status/doctor); narrowed `layout` params from `Any` to `CgcRuntimeLayout` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: Fixed `commands` types in `cgc_install_dry_run_result`/`cgc_install_preflight` to `list[dict[str, Any]]`; behavior-preserving (commit `0549b28`).
- 2026-05-28T13:40+02:00: Updated after the remaining host-venv patch/status helper functions were removed from CGC lifecycle installation.
- 2026-05-28T12:32+02:00: Updated after CGC status began reporting watcher container state, last refresh, indexing state, and requiring the watcher to be alive.
- 2026-05-26T12:51+02:00: Updated after CGC install/status/doctor switched from host venvs to the Docker runner image.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC install, status, patch, and doctor logic extracted out of provider lifecycle.
