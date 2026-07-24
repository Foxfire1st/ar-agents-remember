# heap_diag.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/heap_diag.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:18:47Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

`heap_diag.py` provides the dashboard daemon's opt-in heap-growth evidence and optional glibc arena reclamation. It keeps diagnostic cost out of normal serving while giving an operator a bounded way to distinguish Python-object retention from allocator fragmentation.

## Code Commentary

### Logic

`AR_HEAP_DIAG` starts `tracemalloc` only when explicitly enabled. `heap_diag_loop` samples slowly, takes and formats snapshots in worker threads, and logs RSS, traced heap, GC counters, and allocation growth against the prior snapshot. `AR_MALLOC_TRIM` independently enables a cached best-effort `malloc_trim(0)` call on glibc; unsupported platforms return `None` rather than claiming reclamation occurred.

### Conventions

Environment parsing is deliberately local and truthy-only. The diagnostic carries no serving authority and is never a default-on observer.

### Invariants And Boundaries

The module must not start tracing, allocate diagnostic work, or schedule a loop unless its opt-in flag is present. Snapshot/report formatting is off the event loop, but its GIL-atomic remainder is documented as bounded rather than hidden.

### Todos

No durable follow-up is recorded here.

## Docs References

The configured Domain Documentation registry has no entries. This is repository-local operational diagnostics.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is configured for this opt-in daemon diagnostic. | — | — |

## Repo-Internal References

The serving lifespan owns scheduling; this module owns only flags, snapshots, formatting, and allocator trimming.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The app lifespan starts the diagnostic and trim loops only when their flags are enabled. | L683-L712 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The paired test sidecar records disabled-by-default behavior, report output, worker-thread placement, and loop responsiveness while its source is still uncommitted. | L19-L33 | [test_heap_diag.py onboarding](../../../tests/test_heap_diag.py.md) |

## Cross-Repo References

No meaningful cross-repository boundary participates in this module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The diagnostic is wholly repository-local. | — | — |

## Update History

- 2026-07-24T13:18:47Z — Created for 260718-CHATS-L5I: documented the opt-in heap diagnostic, worker-thread report path, and optional glibc arena reclamation. Verification metadata remains empty until the code commit.
