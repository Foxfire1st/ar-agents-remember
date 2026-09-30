# mcp/src/agents_remember/application/knowledge_reader/timeline.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_reader/timeline.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:06:02+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the three sources and the cache. | "The timeline of a truth view, newest first, from its three sources" | mcp/src/agents_remember/application/knowledge_reader/timeline.py:1-25 |
| The bounded cache of complete timelines (F7). | `TIMELINES` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:62-62 |
| A timeline served from the cache, remembered only when every source was read. | `record_timeline` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:83-106 |
| The three sources, each with its own state. | `_timeline` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:109-134 |
| Uncommitted first, then by position in the history. | `_newest_first`; `_ranks` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:140-151; mcp/src/agents_remember/application/knowledge_reader/timeline.py:154-159 |
| The record file's events, found by ID, with renames paired and the uncommitted state. | `_record_events`; `_paired`; `_uncommitted_record` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:167-199; mcp/src/agents_remember/application/knowledge_reader/timeline.py:202-209; mcp/src/agents_remember/application/knowledge_reader/timeline.py:212-232 |
| The meaning diff. | `meaning_diff` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:235-245 |
| History rows dated by their file's last commit. | `_history_events`; `_last_change` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:261-282; mcp/src/agents_remember/application/knowledge_reader/timeline.py:285-296 |
| Entry events: `-G` without `--pickaxe-all`, plus the current sidecars' log (F1). | `_entry_events`; `_entry_commits` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:310-326; mcp/src/agents_remember/application/knowledge_reader/timeline.py:361-377 |
| Moved against re-anchored (F5). | `_entry_change` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:411-422 |
| The converted part of the history, cached per commit. | `_range`; `_converted_range` | mcp/src/agents_remember/application/knowledge_reader/timeline.py:445-448; mcp/src/agents_remember/application/knowledge_reader/timeline.py:452-464 |
| The three-source, re-anchor and cache cases. | `test_an_invariant_truth_view_has_every_field_state_link_and_a_three_source_timeline`; `test_the_timeline_labels_moves_and_re_anchors_and_reads_only_the_sidecars_naming_them`; `test_a_complete_timeline_is_served_again_from_the_bounded_cache` | mcp/tests/test_knowledge_reader.py:801-838; mcp/tests/test_knowledge_reader.py:849-880 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new module MIK-R29 adds, recording rulings 09:42:58 F1 (`--pickaxe-all` dropped), F5 (re-anchored, not moved), F7 (the bounded per-tree cache) and F11 (a failed source named), and 10:44:14 F17 (a failed timeline is not cached and the tree key is in the cache key, tested). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
