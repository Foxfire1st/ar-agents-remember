# mcp/src/agents_remember/worktrees/sync_transaction_cutover.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

The memory cutover preflight of one fresh sync: judge the exact memory sides before any ref, journal or branch moves, and refuse by name a side that would leave or bypass the text format.

## Code Commentary

`sync_side_outcome(repository, memory)` probes the layout marker on `preSyncHead`, `sourceCommit` and, for a merge, their merge base, and returns `admit`, `legacy` or `out-of-format` with the judged sides named. A merge with any converted side is admitted (the crossing sync, or all converted); three unconverted sides are `legacy`. A fast-forward is admitted when both sides are converted or when an unconverted target takes a converted source (the line converts by taking it); a converted target with an unconverted source is `out-of-format`; two unconverted sides are `legacy`.

`cutover_locked(memory, fetch)` answers nothing for no memory side, `already-current` or `skip`. It maps `legacy` and `out-of-format` to the refusal `sync-unconverted-memory-locked` (`sync-` plus `CUTOVER_LOCK_CODE`) with the central `legacy_format_refusal` detail naming the line and the judged sides. A `LayoutProbeError` or `CrossingSyncError` refuses by name and is never read as converted or unconverted.

## Relationships

Only fresh admission asks it: `sync_transaction._admit_participating_sides` calls `cutover_locked` before the participating-side preflight, the preview and parking, so an in-flight continue or cancel is never re-judged. `activation/atomic_series_activation_transaction.py` mirrors the same judgment before publishing a series' reconciling selection. `cutover_lock.py` owns the code and the refusal text; the probes come from `knowledge_validation.has_layout_marker` and `knowledge_crossing.merge_base`; the result shape comes from `sync_transaction_authority.command_result`.

## Evidence

- The outcome names the judged sides and admits crossing, adoption or all-converted shapes. [1]
- Legacy and out-of-format outcomes and unanswered probes refuse before anything moves. [2]
- Fresh admission asks the preflight before the participating-side checks. [3]
