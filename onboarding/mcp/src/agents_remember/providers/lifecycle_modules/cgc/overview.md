# mcp/src/agents_remember/providers/lifecycle_modules/cgc/ - CGC Lifecycle Modules Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| sourceRoute            | `mcp/src/agents_remember/providers/lifecycle_modules/cgc/` |
| doc_type               | `route-overview`                           |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00                  |
| governingOverview      | `../overview.md`                           |

## Governing Overview

[Provider Lifecycle Modules Overview](../overview.md)

## Purpose

`cgc/` contains the CodeGraphContext provider lifecycle implementation. The
subpackage is the former flat `cgc_*` module group, now organized behind a CGC
package facade with prefix-free filenames.

## Hot Path Summary

`__init__.py` re-exports the CGC public lifecycle surface. `core.py` derives
settings and runtime layout, `backend.py` manages the FalkorDB Docker backend,
`installation.py` owns install/status/patch/doctor behavior, and `process.py`
owns watcher processes, bounded native commands, refresh, and visualization.

## Route Model

- `core.py` is configuration and layout only.
- `backend.py` owns the managed FalkorDB container and backend state.
- `installation.py` owns dependency install, local CGC patches, and status.
- `process.py` owns long-running watcher/server processes and bounded commands.

## Invariants And Boundaries

- Keep `__init__.py` as the package export facade.
- Do not put GrepAI behavior in this package.
- Long-running CGC process actions must keep durable namespace checks.
- Backend Docker lifecycle stays separate from process start/stop logic.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports the CGC package facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| Watcher aggregation imports CGC all-root start/status/stop behavior from this package. | [watchers.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/watchers.py) |

## Update History

- 2026-05-25T19:09+02:00: Created when flat `cgc_*` lifecycle modules moved under `lifecycle_modules/cgc/` with prefix-free filenames.
