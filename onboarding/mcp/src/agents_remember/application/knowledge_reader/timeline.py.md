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
  those changes are read. On real data an invariant view reads 7 blobs (28.6 KB) instead of about 2,590
  (19.1 MB), with the same events.
- **Moved or re-anchored (F5).** `_entry_change` says `moved` only when the source path or the sidecar
  changes; a locator, blob or content change at the same path is `re-anchored`.
- **Ordering.** `_newest_first` puts uncommitted events first, then orders by the commit's position in
  `rev-list` (not by date, so two commits in the same second still order correctly), then by source.
- **Each source reports its own state.** `_timeline` records `read` with its event count, or `unavailable`
  with the reason; a source that could not be read never reads as "no history".
- **The cache (F7).** `TIMELINES` is a `BoundedMemo` of 256 timelines keyed by (memory repository, revision,
  tree key, record). The tree key covers a working tree's uncommitted state. A timeline with any source that
  was not `read` is never remembered, so the next read asks again. Callers do not mutate the shared answer.

### Conventions

- `git log --raw --no-abbrev` with a record separator and field separators, parsed by `_commit` and `_raw`.
- Blobs are read in one batch per source (`read_git_blobs_bytes`).

### Invariants And Boundaries

- **A failed source is shown as unavailable, never as empty:** each of the three sources carries its own
  state. Proved by `test_a_complete_timeline_is_served_again_from_the_bounded_cache` (an injected `_log`
  failure answers `unavailable` and is not cached; the next read recomputes `read`), and by the dashboard's
  `timeline-source-unavailable` case.
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

- The module's own statement of the three sources and the cache. [1]
- The bounded cache of complete timelines (F7). [2]
- A timeline served from the cache, remembered only when every source was read. [3]
- The three sources, each with its own state. [4]
- Uncommitted first, then by position in the history. [5]
- The record file's events, found by ID, with renames paired and the uncommitted state. [6]
- The meaning diff. [7]
- History rows dated by their file's last commit. [8]
- Entry events: `-G` without `--pickaxe-all`, plus the current sidecars' log (F1). [9]
- Moved against re-anchored (F5). [10]
- The converted part of the history, cached per commit. [11]
- The three-source, re-anchor and cache cases. [12]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
