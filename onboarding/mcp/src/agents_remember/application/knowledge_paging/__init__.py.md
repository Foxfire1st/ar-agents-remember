# mcp/src/agents_remember/application/knowledge_paging/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Bounded continuation accepted by the mounted read (MIK-R02@v2): the package's front door.** Every bounded read of a converted memory tree is cut by one declared token threshold into pages of whole rows, and each page carries the one continuation that the mounted `knowledge_read` resumes, whichever surface minted it. The package re-exports the threshold, the pager types and `page_block`.

## Code Commentary

### Logic

- **Module map.** `threshold` (the one constant), `pager` (cutting whole rows), `bindings` (minting and refusing a continuation), `scope_pages` (the scope read behind the published-intent block), `block_pages` (one bound for a whole `read_ar_files` knowledge block), `view_pages` (the named views), `currentness` (MIK-R03 state computed once per page) and `tree_read` (the converted-tree branch of `knowledge_read`). The token model is `models/knowledge/continuation.py`.
- **Two responses are paged today:** the selective scope read behind the published-intent block, and the named views of `knowledge_read`.
- **The seam for MIK-R01 and MIK-R05.** A response owner that pages supplies its ordered selection as `PageRow` values (a family header row carries its `reference`, members name the family as `group`), a manifest digest over that order, and a policy name and version; route-chain entries are further rows after the family content, so they count toward the same threshold and resume through the same token.
- `tree_read` is imported by its own module path, not re-exported, because it depends on the published-intent route, which in turn pages through `scope_pages` (an import cycle otherwise).

### Conventions

- The docstring is the package's design statement; the per-module docstrings carry each rule's detail.

### Invariants And Boundaries

- **No cursor state is kept on the server.** The token is the whole state of a walk.
- **What is selected does not change.** Rows are the scope read's items and the view renderer's rows, in their existing order.
- **Inert before MIK-R37.** Only a converted memory tree (the layout marker present) reaches this code; a read of an unconverted database keeps its own budgets and cursors, and the worker and both review rounds measured unconverted reads byte-identical to base.

### Todos

- MIK-R01 (L01) makes the header reference a literal first row of its own row list (ruling Q3, 19:56:40), carries the pre-existing first-64-rows projection cap (Q7), and takes the more-than-64-seeds edge (R2-1, ruling 21:32:34).

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
| The package statement: one threshold, whole-row pages, one continuation any surface's page resumes. | "Bounded pages of a memory tree's knowledge" | mcp/src/agents_remember/application/knowledge_paging/__init__.py:1-27 |
| The re-exported names. | `KNOWLEDGE_PAGE_THRESHOLD_TOKENS`; `cut_page` | mcp/src/agents_remember/application/knowledge_paging/__init__.py:45-55 |

## Cross-Repo References

No meaningful cross-repo references found: the package pages one memory tree's derived index and names no other repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q1 the whole block is bounded; Q3 the interim header reference; Q7 carried to L01) and 21:32:34 (the 64-seed edge carried to L01). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
