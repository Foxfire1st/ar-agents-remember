# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T06:20+02:00|
| lastVerifiedCommitHash | `6beccd0545a2d5c161059715d5ed7830917eba03` |
| lastVerifiedCommitDate | 2026-06-09T22:39:28+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`process_control.py` owns CodeGraphContext watcher container start/stop
lifecycle and all-root start/stop aggregation.

## Code Commentary

### Logic

The module builds dry-run Docker watcher commands, starts the managed FalkorDB
backend when settings-backed roots require it, starts `cgc watch` inside the
CGC runner image, records provider state, removes watcher containers on stop,
marks stopped state, and aggregates start/stop results across configured roots.
Watcher startup renders the Compose override with backend host ports from the
backend start result so repeated settings-backed starts keep the same
FalkorDB/browser port mappings. Every watcher `up` (start, start-all, and
their dry-run plans) passes `--remove-orphans`: the render always lists every
configured watcher service, so Compose removes exactly the watcher containers
of repos that were dropped from MCP settings instead of leaving them running
against the shared backend.

`cgc_index_concurrency(layout_count)` bounds how many repos reindex
simultaneously. Each CGC indexer self-throttles to ~10 in-flight FalkorDB
queries and uses up to ~10 parser threads; reindexing all repos in parallel
(`max_workers=len(layouts)`) would peg the CPU and overrun the shared FalkorDB
query queue on a workspace with many repos. The default cap is
`DEFAULT_CGC_INDEX_CONCURRENCY` (2). The env var `AR_CGC_INDEX_CONCURRENCY`
overrides the cap (non-integer values are silently ignored in favour of the
default). The function returns at least 1 and at most `layout_count`.
`cgc_parallel_layout_action_results` now calls `cgc_index_concurrency` to set
`max_workers` instead of always using `len(layouts)`.

### Invariants And Boundaries

- Long-running watcher start/stop operations require a durable process
  namespace even though Docker owns the actual watcher lifetime.
- Backend lifecycle is delegated to `backend.py`.
- Refresh and bounded query behavior live in sibling lifecycle modules.
- Host PIDs are not a managed CGC contract; watcher state is tracked by Docker
  container name.
- Watcher `up` should render dependency backend ports from the current start
  result when available.
- `--remove-orphans` is safe here only because the render is always complete:
  if a future change renders a partial service set, the flag would delete the
  watchers that were merely omitted.
- The parallel reindex fan-in is capped by `cgc_index_concurrency` (default 2)
  to prevent FalkorDB query queue saturation on large workspaces; override with
  `AR_CGC_INDEX_CONCURRENCY` on machines with more resources.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Shared process helpers provide durable namespace checks and command execution. | [process_status.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/process_status.py); [command_runner.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/command_runner.py) |
| CGC backend startup is delegated to the backend module. | [backend.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| Docker watcher command construction lives in the runner module. | [runner.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |
| `cgc_index_concurrency` is also imported by `refresh.py` to report `indexConcurrency` in the refresh-all result. | [refresh.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py) |
| Unit tests protect the cap defaults, env-override, and boundary conditions. | [test_cgc_index_concurrency.py](agents-remember/mcp/tests/test_cgc_index_concurrency.py) |

## Update History

- 2026-06-10T06:20+02:00 — Body-quality pass: merged the `--remove-orphans` semantics into Logic and added the complete-render precondition to Invariants (documentation only).
- 2026-06-09T22:10+02:00 — All watcher `up` invocations (start, start-all, and their dry-run plans) now pass `--remove-orphans`; the render always contains every configured watcher service, so Compose removes exactly the watcher containers of repos no longer in MCP settings.
- 2026-06-01T00:00+02:00 — Added `cgc_index_concurrency` (default 2, `AR_CGC_INDEX_CONCURRENCY` override) to bound `cgc_parallel_layout_action_results` fan-in and prevent FalkorDB queue saturation; updated Logic, added fan-in Invariant, added cross-references.
- 2026-05-31T12:30+02:00 — Removed already-running watcher detection from start preflight: `cgc_running_process_result` (and its `cgc_watcher_inspect` use / `alreadyRunning` short-circuit) deleted; layout params now typed `CgcRuntimeLayout` (1.0.0 review remediation).
- 2026-05-29T18:35+02:00: `cgc_backend_all_error` now accepts `dict | None` with a `None` guard (closes a latent crash when start-all returns a doctor-failure); extracted `_cgc_start_all_live` to reduce `cgc_start_all` complexity; behavior-preserving (commits `0549b28`, `e3dab63`).
- 2026-05-27T00:25+02:00: Updated after watcher startup began reusing
  backend start-result port mappings in its Compose render.
- 2026-05-26T12:51+02:00: Updated after watcher start/stop moved from host PIDs to Docker watcher containers.
- 2026-05-25T21:14+02:00: Split from `process.py` so watcher process control is separate from refresh and bounded query commands.
