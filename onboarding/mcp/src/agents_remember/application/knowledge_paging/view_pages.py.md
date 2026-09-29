# mcp/src/agents_remember/application/knowledge_paging/view_pages.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/view_pages.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Pages of a named view of a memory tree, cut by the shared threshold (MIK-R02).** The view renderer hands back one row-limited slice at a time; on a converted tree this module reads the whole ordered row list and the pager cuts it by tokens.

## Code Commentary

### Logic

- `VIEW_POLICY`/`VIEW_POLICY_VERSION` come from the views' `TRAVERSAL_POLICY`.
- `read_whole_view(database_path, context, request)`: walks the renderer's own 64-row slices to the end. `WholeView.manifest_digest` digests each row's identity (subject, fact kind, position; a curation row's work item and disposition) under `VIEW_RENDERER_VERSION`, independent of how anchors resolved.
- `view_rows(whole, family)`: in a family view every row belongs to the one family, and the first row carries the family's reference, so every later page starts with it.
- `family_reference(index_path, tree_key, family_revision_id)`: the family's revision ID, text ID and title, read from the index (the real family view has no `joint_guarantee` row to take it from).
- `view_page_payload(whole, cut, continuation, *, index_complete)`: the view's own payload type with the page slice as `rows`, `counts.rows_returned`/`rows_remaining` for the page, the shared token in `continuation`, and completeness false on a partial index.

### Conventions

- The page is validated as the view's own payload type, so its validator (rows remaining exactly when a continuation is carried) still holds.

### Invariants And Boundaries

- What is selected and how it is ordered do not change; the rows are the renderer's rows.

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
| The module statement: the whole row list, cut by tokens. | "Pages of a named view of a memory tree" | mcp/src/agents_remember/application/knowledge_paging/view_pages.py:1-14 |
| The manifest digest over each row's identity. | `WholeView`; `_row_identity` | mcp/src/agents_remember/application/knowledge_paging/view_pages.py:57-70; mcp/src/agents_remember/application/knowledge_paging/view_pages.py:176-186 |
| Walking the renderer's slices to the end. | `read_whole_view` | mcp/src/agents_remember/application/knowledge_paging/view_pages.py:73-94 |
| A family view's rows and its reference row. | `view_rows`; `family_reference` | mcp/src/agents_remember/application/knowledge_paging/view_pages.py:97-133 |
| The page as the view's own payload. | `view_page_payload` | mcp/src/agents_remember/application/knowledge_paging/view_pages.py:136-173 |

## Cross-Repo References

No meaningful cross-repo references found: the view is read from one memory tree's index.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect ruling of 2026-09-29 19:56:40 (Q3 the interim header reference, Q4 the threshold and not `limit`). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
