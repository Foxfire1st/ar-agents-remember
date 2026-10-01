# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

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

## Evidence

### Repo-Internal References

- Shared process helpers provide durable namespace checks and command execution. [1]
- CGC backend startup is delegated to the backend module. [2]
- Docker watcher command construction lives in the runner module. [3]
- `cgc_index_concurrency` is also imported by `refresh.py` to report `indexConcurrency` in the refresh-all result. [4]
