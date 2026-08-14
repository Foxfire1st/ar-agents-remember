# heap_diag.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/heap_diag.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:18:47Z |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for this opt-in daemon diagnostic. | — | — |

## Repo-Internal References

The serving lifespan owns scheduling; this module owns only flags, snapshots, formatting, and allocator trimming.

| Finding | Anchor | Source |
| --- | --- | --- |
| The app lifespan starts the diagnostic and trim loops only when their flags are enabled. | "def _serving_lifespan(" | mcp/src/agents_remember/serving/_app_lifespan.py:195-195 |
| The paired test sidecar records disabled-by-default behavior, report output, worker-thread placement, and loop responsiveness while its source is still uncommitted. | `### Logic` | onboarding/mcp/tests/test_heap_diag.py.md:23-26 |

## Cross-Repo References

No meaningful cross-repository boundary participates in this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The diagnostic is wholly repository-local. | — | — |

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 4 citation finding(s); scoped recheck clean.

- 2026-07-24T13:18:47Z — Created for 260718-CHATS-L5I: documented the opt-in heap diagnostic, worker-thread report path, and optional glibc arena reclamation. Verification metadata remains empty until the code commit.
