# mcp/src/agents_remember/application/knowledge_leaf/currentness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_leaf/currentness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T02:10:00+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The `currentness` block beside leaf pages, cut to what each page returns (MIK-R03 with MIK-R01).** A leaf page states each entry's and member's state in its own rows; the response also carries the `currentness` block every read of a converted tree carries (MIK-R03 rule 4). Each prepared leaf already computed its selection's currentness once, at the walk's code tree, so a candidate page's block is the subset its rows name.

## Code Commentary

### Logic

- **`LeafCurrentness(code_tree, leaves)`** gathers the invariants and families of every prepared leaf, first occurrence by ID, and the first leaf's `problem`, if any.
- **`subset(answer)`** names records by walking the answer's `rows` lists (`_rows`, `_named`):
  - an invariant is named by its `member` or `member_reference` row, or by an entry row's `invariant`;
  - a family is named by its `family_header` row or the page's `family_header_reference` row, and a named family brings all its members' states (its header counts its stale members);
  - an advertised family is not selected, so it names nothing.
  - This is the same rule L02's `WalkCurrentness` applies to rows that name records by projected UUID.
- **`document(answer, beside)`** is the block of one answer. A block that also carries scope pages (identity seeds) merges `beside`'s scope subset in by ID (`_merged`). With no leaves at all it returns the scope block alone. Splitting `_merged` out keeps `document` at or below 10 under radon (ruling N1, 2026-09-30 00:08:39).

### Conventions

- Computed once per prepared leaf, never once per cutting iteration; the block is measured inside the page, so it counts toward the threshold (L02 ruling F3).

### Invariants And Boundaries

- Currentness is advisory beside the rows; it never edits them and never refuses the read (MIK-R03).
- A retired member is not selected, so it is not in the block.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R01@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`01_family-complete-leaf-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module statement: the subset a page's rows name, and the merge with scope pages. | "block beside leaf pages, cut to what each page returns" | mcp/src/agents_remember/application/knowledge_leaf/currentness.py:1-16 |
| The gathered currentness of every leaf, and one answer's subset. | `LeafCurrentness`; `subset` | mcp/src/agents_remember/application/knowledge_leaf/currentness.py:39-69 |
| One answer's block, merged with the scope subset beside it. | `document`; `_merged` | mcp/src/agents_remember/application/knowledge_leaf/currentness.py:71-93 |
| Which rows name which records. | `_named`; `_rows` | mcp/src/agents_remember/application/knowledge_leaf/currentness.py:96-122 |

## Cross-Repo References

No meaningful cross-repo references found: the block is cut from currentness already computed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): created this card for the new file MIK-R01 adds. It records the architect ruling of 2026-09-30 00:08:39 (N1: `_merged` extracted for radon). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
