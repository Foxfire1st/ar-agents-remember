# test_heap_diag.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_heap_diag.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:18:47Z |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d` |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_heap_diag.py` proves that the daemon heap diagnostic remains opt-in and that its expensive snapshot/report work does not monopolize the serving event loop.

## Code Commentary

### Logic

The suite verifies flag and interval parsing, portable `malloc_trim` behavior, report baselines and growth diffs, and procfs RSS parsing. Its async cases assert that snapshots and report formatting run in worker threads, preserve previous-snapshot chaining, and leave heartbeat scheduling responsive while a CPU-bound report is running.

### Conventions

Thread-placement assertions are paired with an observable event-loop responsiveness test so worker-thread usage is not treated as a sufficient proxy for the actual latency property.

### Invariants And Boundaries

Tests keep `tracemalloc` cleanup local and cancel diagnostic loops in `finally` blocks. They test the opt-in helper rather than enabling diagnostics for unrelated serving tests.

### Todos

No durable follow-up is recorded here.

## Docs References

The configured Domain Documentation registry has no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured for this repository-local suite. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The paired source sidecar records the module's flag parsing, snapshots, reporting, and optional trim resolution while the new source remains uncommitted. | L19-L33 | [heap_diag.py onboarding](../src/agents_remember/serving/heap_diag.py.md) |

## Cross-Repo References

No meaningful cross-repository boundary participates in this suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The tests exercise repository-local serving diagnostics. | — | — |

## Update History

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_heap_diag.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 3 line(s)
  with no token change whatsoever. Checked by parsing both revisions and comparing the abstract
  syntax trees (identical) and the comment tokens (identical), so no symbol, signature, default,
  decorator, control-flow branch, docstring, or assertion this card describes has moved, and every
  claim this card makes about its own source still holds.

- 2026-07-24T13:18:47Z — Created for 260718-CHATS-L5I: recorded regression coverage for disabled-by-default diagnostics, allocator trimming, report content, off-loop execution, and responsiveness. Verification metadata remains empty until the code commit.
