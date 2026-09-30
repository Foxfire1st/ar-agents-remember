# mcp/src/agents_remember/application/knowledge_leaf/pages.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_leaf/pages.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T02:10:00+02:00 |
| lastVerifiedCommitHash | `3772cdcd008fcacdc5a86e264a3ef63e879ea544`|
| lastVerifiedCommitDate | 2026-09-30T02:36:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Pages of the family-complete leaf read, cut by the shared threshold (MIK-R01 with MIK-R02).** The same `PreparedLeaf` builds page 1 inside a `read_ar_files` block and every page of `knowledge_read`'s `source_context` view, so both surfaces return one selection under one manifest (rule 6).

## Code Commentary

### Logic

- **`LeafRequest`.** The index path, the memory tree ID, the index state, the seed path, the code tree entries are observed at (MIK-R03; its ID is what the walk binds) and an optional continuation to resume.
- **`prepare_leaf(request)`** opens the index with `expected_key` set to the memory tree, then:
  - a path with no live entry returns `registration_absent_refusal(path=…, with_proofs=True)`, whose wording names "realization or proof claim" (ruling N6, 2026-09-30 00:08:39);
  - otherwise it computes the selection's currentness once (`_currentness`), the rows (`leaf_rows`) and the counts (`leaf_counts`);
  - it binds the page with a `PageBinding`: the memory tree, policy `family-complete-leaf` / `v1`, the structure's manifest digest and the code tree ID;
  - a resumed read is checked with L02's `position_refusal` against the manifest and the row total;
  - queued seeds (`rest`) have the first one's manifest computed (`_next_manifest`), and a queued seed that selects nothing is refused `continuation_binding_mismatch` rather than skipped.
- **`_currentness`.** `invariant_currentness` at the code tree, with each family header's `FamilyCurrentness` counting live members only. A failure in `CURRENTNESS_FAILURES` returns the rows with states unset and the reason in `problem`: currentness is advisory beside the answer (L03 ruling N2).
- **`PreparedLeaf`.** It has the shape of L02's `PreparedScope`, so `block_pages` cuts either:
  - `render(cut)` is the seed's page (`_page`);
  - `deferred()` is the seed's counts and a position-0 continuation when the block is already full;
  - `collapsed(queued)` is this seed and the queued seeds as one deferred entry, whose single continuation walks them all.
  - Every token is minted with `response="leaf"` and `view=LEAF_VIEW` (`source_context`).
- **The page (`_page`).**
  - `seed`, `state: "page"` and `memoryTreeId` (rule 9); `manifestDigest`; `rows`; `counts` with the walk's `rowsReturned` and `rowsRemaining`; `hasMore`, `enumerationComplete` and `indexState`; `continuation`, `continuationOperation: "knowledge_read"` and `continuationView: "source_context"`; and `page`, L02's page block.
  - **The header reference is a literal first row** (carried obligation 1, L02 ruling Q3 of 2026-09-29 19:56:40): `_page` pops `headerReference` out of `page` and places the `family_header_reference` row at `rows[0]`. It repeats an identity already returned and is not counted as a returned row.
  - `enumerationComplete` is true only when the cut is complete *and* the index is `complete`: a page from a partial index is never presented as complete.
  - When this seed is done and a queued seed follows, the token moves on to it with that seed's manifest, and the page names it as `continuationSeed`.
- **No local path in the token** (carried obligation 4, 2026-09-29 21:17:07). The continuation carries the seed path, the tree, the manifest and the code tree ID, never a repository root; `tree_read` resolves the repository from `repositoryRoot` or the mount workspace.

### Conventions

- `LEAF_VIEW` = `source_context` is the one view a leaf walk resumes on.
- A leaf has one declared row order; an ordering is not part of its binding (ruling Q7).

### Invariants And Boundaries

- **Every page continuing a family starts with a header reference row** (candidate invariant).
- **Both surfaces return one selection:** page 1 of the block and every `source_context` page come from one `PreparedLeaf`, under one manifest digest. Page-1 cuts may differ between surfaces, because the envelopes differ; the selection does not.
- **A queued seed is never silently dropped.**

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
| The module statement: one prepared leaf for both surfaces, and the header reference as a literal first row. | "Pages of the family-complete leaf read" | mcp/src/agents_remember/application/knowledge_leaf/pages.py:1-16 |
| The view a leaf walk resumes on, and the request. | `LEAF_VIEW`; `LeafRequest` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:63-81 |
| The prepared leaf with its page, deferred and collapsed forms, each minting a `leaf` token. | `PreparedLeaf`; `_first_continuation` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:84-140 |
| The preparation: `registration_absent` naming proof claims too, the binding, and the position check of a resumed walk. | `prepare_leaf`; `registration_absent_refusal` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:143-184 |
| Currentness computed once per selection, advisory on failure, family headers counting live members. | `_currentness` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:187-209 |
| The first queued seed's manifest, and the refusal of a queued seed that selects nothing. | `_next_manifest` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:212-229 |
| The token after a page: within the seed, or moving on to the next queued seed. | `_continuation` | mcp/src/agents_remember/application/knowledge_leaf/pages.py:232-247 |
| The page: the reference row first, the counts with the walk's position, and a partial index never complete. | `_page`; "headerReference" | mcp/src/agents_remember/application/knowledge_leaf/pages.py:250-277 |

## Cross-Repo References

No meaningful cross-repo references found: the pages read one memory tree's derived index.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T02:10:00+02:00 — 260928-MIK-L01 curator (uncommitted change set on `ar/260928-mik-l01`, code base `7127756cd132d1103cd0a24bc7dc6884ddb663ee` plus the staged delta): created this card for the new file MIK-R01 adds. It records the carried obligations (the header reference as a literal first row, 2026-09-29 19:56:40; no local path in the token, 2026-09-29 21:17:07), and the rulings of 2026-09-29 23:21:57 (Q4 one selection by manifest, Q7 one declared order) and 2026-09-30 00:08:39 (N6 the `registration_absent` wording). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
