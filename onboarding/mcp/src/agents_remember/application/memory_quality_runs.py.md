# mcp/src/agents_remember/application/memory_quality_runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/memory_quality_runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-20T21:30+02:00 |
| lastVerifiedCommitHash | `de3a0fd9204f2e64755032274fb4e741bfddf6df` |
| lastVerifiedCommitDate | 2026-08-20T21:16:45+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[application/overview.md](overview.md)

## Purpose

Bounded background registry for long-running memory-quality checks (260815-DAG-L15-R7). The full
contract-scoped check exceeds the MCP client's request window; this registry runs it on a daemon
thread and lets the caller poll a bounded, evictable result. Runtime store only (doctrine D4): a
dropped or evicted run simply needs a rerun — the check is read-only plus one atomic checklist
write.

## Code Commentary

### Logic

`MAX_QUALITY_RUNS = 8` and `QUALITY_RUN_TTL_SECONDS = 1800` bound the registry. `start_quality_run`
is single-flight per key: a caller whose key already has a `running` run receives that run's
`(run_id, "running")` instead of starting a second worker, so two callers cannot race the same
checklist write. A new run records a `_QualityRun` (`run_id` = uuid hex[:16], `status: running`)
under the module lock, then a daemon thread (`quality-run-<run_id>`) executes the callable and
settles the record to `completed` (with the result) or `failed` (with the error text) — the run
record carries the failure, never an unhandled thread exception.

`poll_quality_run` returns the run envelope: `{"status": "running", "runId"}` while active,
`{"status": "failed", "runId", "error"}` on failure, and `{"status": "completed", "runId", **result}`
when done; `None` for an unknown/evicted run id. `_evict_locked` drops completed runs older than the
TTL, and when the registry is at capacity evicts the oldest completed run; running entries are never
evicted (peak = active runs + MAX, bounded in practice by single-flight per key × portfolio scale —
reviewer F6 observation).

### Conventions

- Module-level `_registry` dict + `threading.Lock`; all mutations happen under the lock.
- Runtime store only (D4): nothing here survives a process restart; an evicted run is `run-not-found`
  at the registration boundary and the caller reruns.
- The application wrappers in `application/memory_tools.py` own the envelope shape (`ok` header,
  `runId`, `run-not-found` semantics); this module returns the raw run state.

### Invariants And Boundaries

- Bounded by construction: MAX runs + TTL eviction, and the eviction policy never drops a running
  run.
- Single-flight per key is the concurrency contract — duplicate concurrent starts for the same key
  return the active run.
- This module holds no reference to the memory-quality checker itself; the caller supplies the
  callable (a lambda over `_run_quality_check` in `application/memory_tools.py`).
- Never the survival layer: dropped runs are expected behavior, not data loss (D4).

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The single-flight start and the daemon worker. | `start_quality_run` | mcp/src/agents_remember/application/memory_quality_runs.py:37-71 |
| The poll envelope and unknown-run `None`. | `poll_quality_run` | mcp/src/agents_remember/application/memory_quality_runs.py:74-85 |
| The TTL + capacity eviction (completed only). | `_evict_locked` | mcp/src/agents_remember/application/memory_quality_runs.py:88-99 |
| The application wrappers that own the wire envelope. | `start_memory_quality_check_run`; `poll_memory_quality_check_run` | mcp/src/agents_remember/application/memory_tools.py:250-279; mcp/src/agents_remember/application/memory_tools.py:280-301 |
| The forcing suite covers start/poll/completed/failed, single-flight, boundedness, and TTL eviction. | `MemoryQualityRunRegistryTests` | mcp/tests/test_memory_quality_runs.py:13-174 |

## Cross-Repo References

No cross-repo boundary applies to this runtime registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the bounded single-flight background run
  registry (MAX 8, TTL 30 min, completed-only eviction, runtime store per D4) behind the async
  memory-quality surface. Verified at code commit de3a0fd9.
