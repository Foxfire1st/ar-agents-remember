# mcp/src/agents_remember/serving/intent_summary_cache.py

## Governing Overview

[Owning route overview](overview.md)

## Purpose

Reuse native intent summaries through dependency-observed app-owned caching, with comparison-specific keys and finite age/size bounds.

## Code Commentary

A SummaryKey is repository/master/leaf plus optional recorded comparison number; two numbers are different questions. Both port input discovery and native production receive that complete key.

The cache key also contains a clock-derived age window. `_window` uses the current clock alone, so an evicted admission record cannot recreate an old answer’s window. `_kept` is a bounded inspection record of last admitted windows, not age authority; nonpositive configured max age uses the 900-second default.

Each native production clears and reports resolved dependencies. Unavailable results also observe initial repository object stores so later object availability can invalidate reuse. Newly discovered repositories absent from initial observations prevent retention until a complete read; additional resolved inputs participate in validation. A refused/unavailable result may settle with unknown working-tree status, while counted results may not.

The app-owned ChangesetCache response wrapper owns conditional HTTP handling. The adapter serializes the typed result; retained_inputs counts kept intent-summary keys rather than filesystem dependency records.

## Invariants And Boundaries

No count, path authority or atomic workspace snapshot is invented here. Age windows, complete dependency observations and the full numbered question all constrain reuse; a missing/unknown summary is not admitted as counted merely because its dependencies were cacheable.

## Evidence

- The port and key include optional recorded comparison identity. [4]
- The clock independently controls age windows and the admission table stays bounded. [5]
- Production and reuse preserve the exact question, additional dependencies and refusal-only unknown-status retention. [6]
