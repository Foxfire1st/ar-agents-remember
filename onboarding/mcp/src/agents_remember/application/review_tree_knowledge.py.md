# mcp/src/agents_remember/application/review_tree_knowledge.py

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

**Since MIK-L31 it also answers the focused expression cards, and it settles the wire casing.** A query that names
invariants (`invariants=`, ruling 2026-09-30T05:36:19 Q2) gets only those invariants' realization and proof
entries, on both code sides with their excerpts (filled by `review_tree_entries.py`, answered through `_focused` since
MIK-L32); the leaf-wide view carries no entries. Every wire key is snake_case (MIK-L25 review F9, carried to and settled by L31):
`snake_keys` re-keys the currentness documents and the worklist's own documents, which their owners spell in
camelCase.

**Since MIK-L32 it also answers the unexplained-changes lane (MIK-R32).** `lane=files` answers only the lane's two
destinations (`unexplained_lane`), and `file=<path>` only one changed path's classification (`classify_changed_path`)
or, for a path the comparison did not change, a `refused` result carrying the typed refusal (`_file_view`). Both are
served by `review_unexplained_lane.py` over the one classification of `review_lane_classification.py`. The worklist
view of rule 3 stays in the leaf-wide view beside them (MIK-R32's substitution: MIK-R25's worklist view stays, and the
lane is the separate review destination).

## Code Commentary

### Logic

- **The comparison a query names (pinned since review F11, 2026-09-30T06:10:21).** Without a number,
  `_resolved` takes `resolve_review_candidate`'s own resolution (live, or `recorded=` for the latest record). A
  leaf-wide read that names a number is pinned to that comparison: when the number is the one the review resolves
  to now, `_comparison` uses that resolution as it is (a live leaf keeps its computed worklist); any other number is
  reopened through `reopen_review_trees` with the leaf's recorded contract. A focused read (the cards' named
  invariants, `lane`, or `file`; `ReviewTreesQuery.focused` since MIK-L32) needs only the trees, so it always
  reopens. A resolution without trees answers `knowledge_unavailable_refusal` (a
  legacy comparison is refused) or `None` (`_resolved` is annotated `| None` since review R2-1), which
  `read_review_trees` reports as `not-converted`. The non-current numbered read costs one extra live resolution
  (about 5.5 s on the scratch leaf; review R2-6, accepted as a note).
- **Focused reads (MIK-R31, MIK-R32).** `read_review_trees` dispatches on the one question a query asks: `file`
  first (`_file_view`), then `lane`, then `invariants`. `_focused` (it replaces L31's `_entries_view`) returns the
  record, the knowledge and code sides and exactly one answer: `entries=tree_entries(...)` for the cards,
  `lane=unexplained_lane(trees)` for the lane, or `file_classification` for one path; no diff, currentness or
  worklist. `_file_view` returns `state: "refused"` with the comparison and the owner's `ReviewRefusal` when
  `classify_changed_path` refuses (a path the change inventory does not list, or unreadable trees).
- **`_view`** fills `ReviewTreesResult`: the record, the knowledge sides, the reopened code sides (review F4), the
  diff when both sides are available, the currentness (re-keyed by `snake_keys`) and the worklist; `entries` stays
  empty on the leaf-wide view.
- **One wire casing (review F9).** `snake_keys` recursively re-spells every identifier-shaped camelCase key
  (`_IDENTIFIER_KEY`, `^[a-z][A-Za-z0-9]*$`) in snake_case (`_snake`); a key that is not identifier-shaped (a path, an
  ID) is never rewritten. The real leaf-wide body has no camelCase key (`codeTree` → `code_tree`, `staleMembers` →
  `stale_members`, `ownerKind` → `owner_kind`).
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
  index's `history_rows_about` for each item subject **and for the subject its `facts.row` names**
  (`_row_subjects`; an unexplained hunk is answered by a `hunk:…` row, MIK-R10; PS-1 from L10's post-sync review,
  fixed here and accepted at 05:36:19), without a currency mark; `changes` is the worklist's own gate linkage. Items,
  rows, changes and incomplete entries are re-keyed by `snake_keys`.
- **Only an owner's latest attempt's row is shown (L37, decision record DEC-0AEQ28; INV-MS9BMJ).** `_history_rows` passes the
  rows about a subject through `_governing`: of one owner's rows, only the row from that owner's latest attempt
  file (`owner_history_attempt`). A leaf that continued after a closeout answers the subject again in its next
  attempt, and that judgment governs. Another owner's row about the subject is still shown, and the superseded row
  stays in its frozen file and in the knowledge diff.

### Conventions

- Git is asked with `--no-color --no-ext-diff`, so the patch is the repository's own text.

### Invariants And Boundaries

- **No database other than the derived index is opened on a review path** (ruling 22:22:37 Q1). Proved by
  `test_no_review_path_opens_a_database_other_than_the_derived_index` (every `apsw.Connection` and
  `sqlite3.connect` recorded; every open is inside `runtime/knowledge-index`) and the worker's real run (135 opens,
  4 distinct, all in the index cache).
- History rows carry no current or stale mark until MIK-R09 supplies the rule.
- **Candidate invariant (not ingested): card planning marks come only from a leaf-wide read of the same
  comparison.** The server half is here: a numbered leaf-wide read answers for exactly that comparison (the live
  resolution only when it is that number). Proved by the route case (the numbered read's worklist is `computed`)
  and the client half on `FamilyReviewCenter.tsx` (`pinnedWorklist`).

### Todos

- **Resolved by MIK-L31:** the panel that renders rules 2 and 3 (`dashboard/src/panels/review/LeafKnowledgeChanges.tsx`,
  ruling 22:22:37 Q2) and the mixed key casing (review F9: `snake_keys` at the route boundary, and the adapter's types
  in `dashboard/src/data/reviewTrees.ts`).

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R25@v1` (rules 2 and 3) with its rulings in `25_reviewer-on-git-trees.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The route's port: refused, not converted, one focused answer (a file, the lane, the cards) or the tree view. [1]
- A numbered leaf-wide read pinned to that comparison, live only when it is the current number; a focused read always reopens. [2]
- The leaf-wide view with its re-keyed currentness; one focused answer (the cards' entries, the lane, or one file's classification or refusal). [3]
- One snake_case wire convention, identifier-shaped keys only. [4]
- The knowledge diff and its two groupings. [5]
- Every changed indexed file with its patch, from `--name-status -z`. [6]
- A sidecar's changed realization and proof entries. [7]
- MIK-R03 currentness per side at that side's own code tree. [8]
- The worklist view, its binding to the four trees, and the history rows about each item's subject and its `facts.row` subject. [9]
- The record IDs of one kind the currentness reads. [10]
- The lane and one file served on the live tree leaf; an unchanged path refused. [11]
- The tree view on the fixture: diff groups, currentness per side, worklist. [12]
- No review path opens a database other than the derived index. [13]
- The pinned numbered read keeps a live leaf's computed worklist; the cards read and the key-length bound at the route. [14]

- Rows found by the subject an item's `facts.row` names. [15]

- Each owner's row about a subject from that owner's latest attempt file. [16]
- A leaf's next attempt's row replaces its earlier row in the worklist view; another owner's row stays. [17]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
