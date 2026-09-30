# mcp/src/agents_remember/application/knowledge_paging/currentness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/currentness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R03 currentness for the pages of one walk, computed once and cut to each candidate page.** A bounded page that carries a `currentness` block is measured with it, so the block counts toward the threshold (ruling F3, 20:40:40).

## Code Commentary

### Logic

- `WalkCurrentness(index_path, tree_key, code_tree, candidates)` calls `knowledge_currentness.surface.evaluate_answer` once over every row the page could carry, at the walk's code tree: the tree the caller named on a fresh view read, the token's tree on a resumed page, and the source-resolution tree for the published-intent block.
- `subset(answer)` (since MIK-R01) returns the subset as a `Currentness` object, or `None` when the one evaluation failed; `document(answer)` renders it, or the failure document. `knowledge_leaf/currentness.py` merges this scope subset with a leaf subset when one `read_ar_files` block carries both identity seeds and path seeds. The rendered block is unchanged in output.
- `document(answer)` returns the subset block for one candidate answer: the same records and order `read_currentness` would compute for that answer, with each family's stale members counted over all its members. The reviewer compared 13 real pages and found them equal to `read_currentness`.
- A failure of the one evaluation (`CURRENTNESS_FAILURES`) becomes the `failure_document` for every candidate, so currentness never refuses a read.

### Conventions

- Once per page, never once per cutting iteration (ruling F3).

### Invariants And Boundaries

- Currentness is advisory beside the page; it never edits the rows and never refuses the read (MIK-R03).

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: once per walk page, cut to each candidate. | "Currentness for the pages of one walk" | mcp/src/agents_remember/application/knowledge_paging/currentness.py:1-11 |
| The one evaluation, and its failure document. | `WalkCurrentness`; `evaluate_answer` | mcp/src/agents_remember/application/knowledge_paging/currentness.py:30-70 |
| A candidate's subset block. | `document` | mcp/src/agents_remember/application/knowledge_paging/currentness.py:45-51 |
| The subset as an object, for the merge with a leaf subset (MIK-R01). | `subset` | mcp/src/agents_remember/application/knowledge_paging/currentness.py:53-70 |

## Cross-Repo References

No meaningful cross-repo references found: the evaluation reads one memory tree's index and one code tree.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): MIK-R01 splits `subset` out of `document`, so the leaf currentness can merge the scope subset of a mixed block. A Logic bullet and one row were added; the evaluation and `document` rows were normalised by the installed fixer. `document`'s output is unchanged.
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect ruling of 2026-09-29 20:40:40 (F3 currentness at the walk's code tree, once per page, counted in the threshold). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
