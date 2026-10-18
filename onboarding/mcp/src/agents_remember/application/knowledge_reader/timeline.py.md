# mcp/src/agents_remember/application/knowledge_reader/timeline.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The timeline of every truth view, newest first, from its three sources (MIK-R29 rule 4).**

1. **The record file's `git log`, with meaning diffs.** Each commit that changed the record's JSON file is one
   event, with every field whose value differs from the parent's (both values). A working-tree selection
   whose record file differs from `HEAD` adds one `uncommitted` event.
2. **History rows about it from every leaf** (MIK-R07), as the selected tree's index holds them, each dated by
   the last commit that changed its history file (a file not yet committed is `uncommitted`).
3. **`git log` of the sidecar entries that realize or prove it**: each commit in which one of those entries
   was `added`, `removed`, `moved` (to another source path or sidecar) or `re-anchored` (its locator, blob or
   content identity changed at the same path).

## Code Commentary

### Logic

- **Only the converted history.** `_converted_range` finds the first commit that added the layout marker and
  logs `<its parent>..<revision>`; it is cached per (repository, revision), because a commit's history never
  changes. No record or entry exists before conversion.
- **Record events.** `_record_events` logs every file of `<ID>-*.json` in the record's directory with
  `--no-renames`, so a slug rename is one commit that deletes one name and adds another, read as `renamed`
  (`_paired`); this replaced `--follow`, which ran rename detection over the conversion commit's thousands of
  files. `meaning_diff` compares every field but `schema`.
- **Entry events (ruling 2026-09-30T09:42:58, F1).** `_entry_commits` logs `-G<ids>` under `onboarding/`
  **without `--pickaxe-all`**, which lists only the files whose diff names an entry ID (the file an entry left
  and the file it entered), plus the log of the entries' current sidecars (re-anchors). Only sidecar blobs of
  those changes are read. The inherited F1 note records a historical comparison of 7 blobs (28.6 KB)
  against about 2,590 (19.1 MB), with the same events; those numbers are not a fresh measurement here.
- **Moved or re-anchored (F5).** `_entry_change` says `moved` only when the source path or the sidecar
  changes; a locator, blob or content change at the same path is `re-anchored`.
- **Ordering.** `_newest_first` puts uncommitted events first, then orders by the commit's position in
  `rev-list` (not by date, so two commits in the same second still order correctly), then by source.
- **Each collector has an explicit outcome.** `_timeline` marks a successfully returning
  collector `read` with its event count, catches its `READ_FAILURES` as `unavailable` with
  a reason, and marks every source unavailable when the selection has no commit.
- **The cache and page owner.** `TIMELINES` now uses resident-byte-weighted `TimelineMemo`,
  keyed by (memory repository, revision, captured tree key, record). `_full_timeline` freezes
  complete ordered events into an immutable manifest and retains it only when every source
  reports `read`. This replaces the former 256-entry `BoundedMemo`, rather than merely
  retaining that entry-count policy. The current owner uses an 8 MiB accounted resident-weight budget and retains
  at most one oversized complete history's anonymous spill storage, including on-disk offsets.
  No per-history disk cap is imposed. This is cache-retention accounting, not a total-process,
  concurrent/in-flight or uncached-build ceiling. [2] [3]
- **Tree-bound pages.** `record_timeline` returns at most fifty events and a continuation over
  the complete manifest. `_timeline_start` checks the held tree, timeline policy/version,
  record seed, manifest digest and position. A mismatch is an explicitly refused timeline,
  not a successful empty history. The complete manifest is acquired before token validation;
  on a miss this can build the full history, whereas a hit reuses it and decodes only the
  selected slice.
- **Deferred history and attempt provenance.** The supplied history callback is invoked only
  on a manifest miss. `_history_events` adds the attempt derived from each owner-history path
  alongside its existing path, owner and row context. An `OSError` while decoding a page
  discards that exact cached manifest without dropping a concurrent replacement, then
  propagates the failure. Cache eviction/clear releases cache ownership; it does not promise
  to forcibly close backing still held by an in-flight page.

### Conventions

- `git log --raw --no-abbrev` with a record separator and field separators, parsed by `_commit` and `_raw`.
- Blobs are read in one batch per source (`read_git_blobs_bytes`).

### Invariants And Boundaries

- **Raised collector failures are explicit:** `_timeline` catches each collector's `READ_FAILURES`
  and reports `unavailable` instead of a successful zero. The named
  `test_a_complete_timeline_is_served_again_from_the_bounded_cache` case injects an `_log`
  failure, asserts `unavailable`, and checks that the next read recomputes `read` rather than
  reusing the failed result. This describes current source assertions, not a test run here.
- **Related UI control.** The reader test supplies an explicit unavailable-entries fixture
  and checks the notice's source and detail; it does not observe a native Git timeout.
  `TimelineSection` renders that non-read source separately from event counts.
- The cache key includes the tree key: a dirty edit after a cached clean read is not served stale (proved by
  the published-tree case, F17).
- Reads only (`log`, `rev-list`, `rev-parse`, `cat-file`).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- Current cache owner, 8 MiB accounted resident-weight budget and at most one cached anonymous spill. [2]
- A complete manifest is reused; history acquisition, digesting and freezing happen on a miss, and only all-read sources are retained. [3]
- The page is at most fifty events or an explicitly refused continuation; an `OSError` during page decoding discards the exact manifest. [13]
- Continuations bind the tree, policy/version, record and complete manifest position. [14]
- History events retain file-based dating and include the attempt derived from their owning history path. [8]
- A controlled unavailable-entries fixture is checked for its source/detail notice, matching the actual non-read-source renderer, not a native Git-timeout observation. [15]

- The module's own statement of the three sources and the cache. [1]
- The three sources, each with its own state. [4]
- Uncommitted first, then by position in the history. [5]
- The record file's events, found by ID, with renames paired and the uncommitted state. [6]
- The meaning diff. [7]
- Entry events: `-G` without `--pickaxe-all`, plus the current sidecars' log (F1). [9]
- Moved against re-anchored (F5). [10]
- The converted part of the history, cached per commit. [11]
- The three-source, re-anchor and cache cases. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
