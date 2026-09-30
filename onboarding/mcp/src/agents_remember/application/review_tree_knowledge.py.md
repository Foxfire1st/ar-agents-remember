# mcp/src/agents_remember/application/review_tree_knowledge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_tree_knowledge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
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

**Since MIK-L31 it also answers the focused expression cards, and it settles the wire casing.** A query that names
invariants (`invariants=`, ruling 2026-09-30T05:36:19 Q2) gets only those invariants' realization and proof
entries, on both code sides with their excerpts (`_entries_view`, filled by `review_tree_entries.py`); the
leaf-wide view carries no entries. Every wire key is snake_case (MIK-L25 review F9, carried to and settled by L31):
`snake_keys` re-keys the currentness documents and the worklist's own documents, which their owners spell in
camelCase.

## Code Commentary

### Logic

- **The comparison a query names (pinned since review F11, 2026-09-30T06:10:21).** Without a number,
  `_resolved` takes `resolve_review_candidate`'s own resolution (live, or `recorded=` for the latest record). A
  leaf-wide read that names a number is pinned to that comparison: when the number is the one the review resolves
  to now, `_comparison` uses that resolution as it is (a live leaf keeps its computed worklist); any other number is
  reopened through `reopen_review_trees` with the leaf's recorded contract. A cards read (named invariants) needs
  only the trees, so it always reopens. A resolution without trees answers `knowledge_unavailable_refusal` (a
  legacy comparison is refused) or `None` (`_resolved` is annotated `| None` since review R2-1), which
  `read_review_trees` reports as `not-converted`. The non-current numbered read costs one extra live resolution
  (about 5.5 s on the scratch leaf; review R2-6, accepted as a note).
- **The cards read (MIK-R31).** When `query.invariants` is set, `read_review_trees` returns `_entries_view`: the
  record, the knowledge and code sides, and `entries=tree_entries(trees, query.invariants)`, with no diff,
  currentness or worklist.
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
| The route's port: refused, not converted, or the tree view. | `read_review_trees` | mcp/src/agents_remember/application/review_tree_knowledge.py:90-112 |
| A numbered leaf-wide read pinned to that comparison, live only when it is the current number; a cards read always reopens. | "def _comparison("; "def _resolved(" | mcp/src/agents_remember/application/review_tree_knowledge.py:115-149 |
| The leaf-wide view with its re-keyed currentness; the cards view with only the entries. | "def _view("; "def _entries_view(" | mcp/src/agents_remember/application/review_tree_knowledge.py:152-188 |
| One snake_case wire convention, identifier-shaped keys only. | `snake_keys`; `_snake`; `_IDENTIFIER_KEY` | mcp/src/agents_remember/application/review_tree_knowledge.py:86-87; mcp/src/agents_remember/application/review_tree_knowledge.py:191-204 |
| The knowledge diff and its two groupings. | `knowledge_tree_diff`; `_Groups` | mcp/src/agents_remember/application/review_tree_knowledge.py:210-227; mcp/src/agents_remember/application/review_tree_knowledge.py:230-283 |
| Every changed indexed file with its patch, from `--name-status -z`. | `_changed_files`; `_name_status` | mcp/src/agents_remember/application/review_tree_knowledge.py:286-301; mcp/src/agents_remember/application/review_tree_knowledge.py:304-338 |
| A sidecar's changed realization and proof entries. | `_changed_entries` | mcp/src/agents_remember/application/review_tree_knowledge.py:384-401 |
| MIK-R03 currentness per side at that side's own code tree. | `side_currentness` | mcp/src/agents_remember/application/review_tree_knowledge.py:407-429 |
| The worklist view, its binding to the four trees, and the history rows about each item's subject and its `facts.row` subject. | "def worklist_view("; "def _bound("; "def _history_rows("; `_row_subjects` | mcp/src/agents_remember/application/review_tree_knowledge.py:435-460; mcp/src/agents_remember/application/review_tree_knowledge.py:463-475; mcp/src/agents_remember/application/review_tree_knowledge.py:478-516 |
| The record IDs of one kind the currentness reads. | `record_ids` | mcp/src/agents_remember/memory/knowledge_index/query.py:288-292 |
| The tree view on the fixture: diff groups, currentness per side, worklist. | `test_the_tree_view_shows_the_knowledge_diff_currentness_per_side_and_the_worklist` | mcp/tests/test_review_git_trees.py:462-505 |
| No review path opens a database other than the derived index. | `test_no_review_path_opens_a_database_other_than_the_derived_index` | mcp/tests/test_review_git_trees.py:656-681 |
| The pinned numbered read keeps a live leaf's computed worklist; the cards read and the key-length bound at the route. | `test_the_tree_view_route_serves_the_port_and_refuses_when_unwired` | mcp/tests/test_review_git_trees.py:730-776 |
| Rows found by the subject an item's `facts.row` names. | `test_history_rows_are_found_by_the_row_subject_an_item_names` | mcp/tests/test_review_git_trees.py:886-897 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose and Logic record the cards read (`invariants=`, ruling 05:36:19 Q2; `_entries_view`), the comparison pinning (review F11 at 06:10:21, R2-1's `| None` annotation at 06:47:03, R2-6 accepted), the one snake_case wire casing (`snake_keys`, MIK-L25 review F9 carried to L31) and the `facts.row` history lookup (PS-1, accepted at 05:36:19); the L31 Todo is marked resolved and a candidate invariant (card planning marks from the same comparison only) is recorded. **Reopened claims reworded and re-anchored:** the `_comparison`, `_view` and worklist rows now name `_resolved`, `_entries_view` and `_row_subjects` and are anchored on line-exact quotes; this pass's three generated bullets for them were removed. Three rows added (`snake_keys`, the route case, the row-subject case).
- 2026-09-30T07:53:24+00:00: Generated citation repair: `_changed_files`; `_name_status` repointed to mcp/src/agents_remember/application/review_tree_knowledge.py:286-301; mcp/src/agents_remember/application/review_tree_knowledge.py:304-338. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:53:24+00:00: Generated citation repair: `_changed_entries` repointed to mcp/src/agents_remember/application/review_tree_knowledge.py:384-401. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T07:53:24+00:00: Generated citation repair: `side_currentness` repointed to mcp/src/agents_remember/application/review_tree_knowledge.py:407-429. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T03:46:54+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): created this card for the new file MIK-R25 adds, recording rulings 22:22:37 (Q1, Q2 and the complexity split) and 23:15:34 (F4, F9 carried to L31). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
