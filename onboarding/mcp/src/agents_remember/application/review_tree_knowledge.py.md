# mcp/src/agents_remember/application/review_tree_knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_tree_knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T03:46:54+02:00 |
| lastVerifiedCommitHash | `8a2d4b478971bf40cca0f24d5e5d24a0844bd563`|
| lastVerifiedCommitDate | 2026-09-30T04:16:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The reviewer's tree view (MIK-R25 rules 2 and 3): knowledge as a Git diff, currentness per side, the
worklist.** For a leaf whose memory is converted, this answers what the landed review composition does not already
show, and nothing more:

- **the knowledge diff** — the Git diff of the two memory trees over the files the index reads (records, sidecars,
  history files), grouped by record and by source path;
- **currentness per side** — every invariant and family of each side through the one MIK-R03 state function,
  against that side's own code tree (before at B, after at C);
- **the worklist view** — the leaf's current MIK-R08 items, the history rows about their subjects (shown without a
  current or stale mark until MIK-R09 supplies one), and the gate linkage of each changed hunk.

`read_review_trees` is the port behind `GET /api/review/trees` (`serving/review_trees.py`), composed in
`cli/dashboard.py`. Each memory side is read through the index of its tree; no database copy is read or made.

## Code Commentary

### Logic

- **The comparison a query names.** `_comparison` reopens a recorded number through `reopen_review_trees` (with the
  leaf's recorded contract), or takes `resolve_review_candidate`'s own resolution (live, or `recorded=` for the
  latest record). A resolution without trees answers `knowledge_unavailable_refusal` (a legacy comparison is
  refused) or `None`, which `read_review_trees` reports as `not-converted`.
- **`_view`** fills `ReviewTreesResult`: the record, the knowledge sides, the reopened code sides (review F4), the
  diff when both sides are available, the currentness and the worklist.
- **The diff (rule 2).** `_name_status` parses `git diff --name-status -z -M` over the knowledge and onboarding
  roots; `_changed_files` keeps the paths `is_indexed_path` accepts and attaches each patch, truncated at
  `PROSE_MAX_LENGTH - 200`. `_Groups.add` files a change as history (under `knowledge/history/`), as a record
  (a knowledge file whose schema names a record kind), as a source (an onboarding sidecar with a `path`), or as
  other; a sidecar's changed `realizes`/`proves` entries (`_changed_entries`: added, removed or changed) are also
  listed under the invariant they name, so a record's code-side changes are visible from both groupings. The
  accumulator split (`_Groups`, `_name_status`) is ruling 22:22:37's complexity action; every function is radon A or
  B.
- **Currentness (rule 2).** `side_currentness` calls `invariant_currentness` for each available side with that
  side's code tree and the index's `record_ids("invariant")`/`record_ids("family")`, adding `indexState`; an
  unread side answers `unverifiableReason`.
- **The worklist (rule 3).** `worklist_view` computes the leaf's worklist without persisting it
  (`leaf_worklist(contract, persist=False)`) for a live leaf, or reads the persisted one for a record. `bound` says
  whether its recorded pairing is exactly this comparison's four trees (`_bound`); `_history_rows` reads the after
  index's `history_rows_about` for each item subject, without a currency mark; `changes` is the worklist's own
  gate linkage.

### Conventions

- Git is asked with `--no-color --no-ext-diff`, so the patch is the repository's own text.

### Invariants And Boundaries

- **No database other than the derived index is opened on a review path** (ruling 22:22:37 Q1). Proved by
  `test_no_review_path_opens_a_database_other_than_the_derived_index` (every `apsw.Connection` and
  `sqlite3.connect` recorded; every open is inside `runtime/knowledge-index`) and the worker's real run (135 opens,
  4 distinct, all in the index cache).
- History rows carry no current or stale mark until MIK-R09 supplies the rule.

### Todos

- **L31 (ruling 22:22:37 Q2; review F9 at 23:15:34):** the panel that renders rules 2 and 3, and the mixed key
  casing of the `/api/review/trees` body (snake_case model fields such as `knowledge_sides` and `history_rows`, beside the camelCase
  keys of the embedded currentness documents and of the worklist items and changes).

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` (rules 2 and 3) with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route's port: refused, not converted, or the tree view. | `read_review_trees` | mcp/src/agents_remember/application/review_tree_knowledge.py:72-92 |
| A recorded number reopened, or the review's own resolution; a legacy comparison refused. | `_comparison` | mcp/src/agents_remember/application/review_tree_knowledge.py:95-113 |
| The view: record, sides, code sides, diff, currentness, worklist. | `_view` | mcp/src/agents_remember/application/review_tree_knowledge.py:116-137 |
| The knowledge diff and its two groupings. | `knowledge_tree_diff`; `_Groups` | mcp/src/agents_remember/application/review_tree_knowledge.py:143-216 |
| Every changed indexed file with its patch, from `--name-status -z`. | `_changed_files`; `_name_status` | mcp/src/agents_remember/application/review_tree_knowledge.py:219-271 |
| A sidecar's changed realization and proof entries. | `_changed_entries` | mcp/src/agents_remember/application/review_tree_knowledge.py:317-334 |
| MIK-R03 currentness per side at that side's own code tree. | `side_currentness` | mcp/src/agents_remember/application/review_tree_knowledge.py:340-362 |
| The worklist view, its binding to the four trees, and the history rows about its subjects. | `worklist_view`; `_bound`; `_history_rows` | mcp/src/agents_remember/application/review_tree_knowledge.py:368-436 |
| The record IDs of one kind the currentness reads. | `record_ids` | mcp/src/agents_remember/memory/knowledge_index/query.py:288-292 |
| The tree view on the fixture: diff groups, currentness per side, worklist. | `test_the_tree_view_shows_the_knowledge_diff_currentness_per_side_and_the_worklist` | mcp/tests/test_review_git_trees.py:453-493 |
| No review path opens a database other than the derived index. | `test_no_review_path_opens_a_database_other_than_the_derived_index` | mcp/tests/test_review_git_trees.py:644-669 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new file MIK-R25 adds, recording rulings 22:22:37 (Q1, Q2 and the complexity split) and 23:15:34 (F4, F9 carried to L31). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
