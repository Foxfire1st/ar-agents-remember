# mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py

## Governing Overview

[CGC Lifecycle Overview](overview.md)

## Purpose

`process_control.py` owns the CodeGraphContext watcher stop lifecycle and its
all-root aggregation.

## Code Commentary

### Logic

The module renders the Compose override, plans `rm -sf <watcher service>` for a dry
run, short-circuits when the watcher container is not running, removes the container
through `run_compose`, and records the stopped state — no pid, `alive: false`, the
container name, the returncode and `stoppedAt` — in the layout state file. `cgc_stop`
with settings and no `--repo-id` delegates to `cgc_stop_all`, which refuses
`--repo-id` and stops each configured layout in sequence through
`cgc_layout_action_results`. `cgc_all_result` aggregates those per-repo results with
the settings path, the dry-run flag and a count. Every non-dry-run stop requires a
durable process namespace.

`DEFAULT_CGC_INDEX_CONCURRENCY` (2) is still declared here and nothing reads it: the
fan-in helper, its `AR_CGC_INDEX_CONCURRENCY` override and the parallel action
results it bounded are gone with the refresh surface.

### Invariants And Boundaries

- Long-running watcher stop operations require a durable process namespace
  even though Docker owns the actual watcher lifetime.
- Host PIDs are not a managed CGC contract; watcher state is tracked by Docker
  container name.
- A stop of a container that is not running reports `ok: true` with the
  not-running message instead of failing.
- Nothing in this module starts, restarts or reindexes a watcher: the start,
  start-all, query and refresh paths are absent.

## Evidence

### Repo-Internal References

- Shared process helpers provide durable namespace checks and command execution. [1]
- Docker watcher inspection helpers live in the runner module; the stop command this module builds is Compose's own service removal. [3]
- `cgc_index_concurrency` had one other reader, the removed `refresh.py`, which reported `indexConcurrency` in the refresh-all result; no module reads it now. [4]

- cgc_backend_start is a retained backend implementation outside this process-control chain; this module retains the stop-class closure and delegates watcher service removal to Compose. [2]
