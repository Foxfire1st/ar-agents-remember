# heap_diag.py

## Governing Overview

[serving overview](overview.md)

## Purpose

`heap_diag.py` provides opt-in dashboard heap tracing and the glibc trim helper used by native MCP calls and the dashboard.

## Code Commentary

### Logic

`AR_HEAP_DIAG` starts `tracemalloc` only when explicitly enabled. `heap_diag_loop` samples slowly, takes and formats snapshots in worker threads, and logs RSS, traced heap, GC counters, and allocation growth against the prior snapshot. `AR_MALLOC_TRIM` enables the dashboard's periodic trim work. Native calls attempt trim after their scopes unwind. The helper calls `malloc_trim(0)` when available, returns one for release, zero when no pages were released, and `None` when the hook is unavailable.

### Conventions

Environment parsing is deliberately local and truthy-only. The diagnostic carries no serving authority and is never a default-on observer.

### Invariants And Boundaries

Dashboard tracing and periodic trim scheduling each require their own opt-in flag. Snapshot/report formatting is off the event loop, but its GIL-atomic remainder is documented as bounded rather than hidden.

### Todos

No durable follow-up is recorded here.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. This is repository-local operational diagnostics.

No relevant external documentation is configured for this opt-in daemon diagnostic.

### Repo-Internal References

The dashboard lifespan owns its periodic scheduling. Native call finalization owns the per-call trim attempt.



### Cross-Repo References

No meaningful cross-repository boundary participates in this module.

The diagnostic is wholly repository-local.

- The app lifespan starts the diagnostic and trim loops only when their flags are enabled. Anchor: `start_heap_tracing` [1]
