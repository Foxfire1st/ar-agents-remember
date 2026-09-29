# mcp/src/agents_remember/application/knowledge_paging/block_pages.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/block_pages.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**One bounded knowledge block for several seeds (MIK-R02 rule 2 applied to `read_ar_files`).** The threshold bounds the whole knowledge block of a `read_ar_files` response, not each seed's page, so N seeds never make N thresholds (ruling Q1, 19:56:40). Source bytes and onboarding are not knowledge rows and are outside it.

## Code Commentary

### Logic

- `bounded_block(entries, envelope)`: seeds are laid out in request order. Each seed's page is cut against the rendered whole block: the seeds already laid out, this page, every block-level summary the envelope adds (the threshold and MIK-R03 `currentness`), and the entries still to come.
- **The tail.** Once a seed's next row no longer fits (`cut.blocked`) or a seed's page is partial, that seed and every later one are the tail: each returns `state: "deferred"` with only its counts and a position-0 continuation. `_tail` sizes the tail so the seed's next row still has room.
- **The collapse (ruling F2, 20:40:40).** When the deferred entries alone would not fit, the tail collapses into one deferred entry listing its `seeds`, whose single continuation walks every tail seed in turn (`PreparedScope.collapsed`).
- Entries that are not pages (a refusal, an unseedable path) are carried as they are.
- `alone` renders a seed's page as a block of its own, so `oversized_row` is flagged only for a row too large on its own; a row that merely does not fit beside other seeds is deferred.

### Conventions

- `envelope` is supplied by `published_intent._tree_block`, so the measured block is exactly the block returned.

### Invariants And Boundaries

- **The knowledge block stays within the threshold for any seed count the mounted tool can send** (`read_ar_files` caps files at 5; the reviewer measured 2 to 64 seeds within 7,499–7,901 tokens).
- Every seed's selection is returned exactly once across the block and its continuations.

### Todos

- **R2-1 (carried to L01, ruling 21:32:34):** a direct helper call with more than 64 queued seeds raises a `ValidationError` while minting the collapsed token (`rest` is capped at 64). It is not reachable through `read_ar_files`.
- R2-2 (accepted as documented in c-04): a collapsed entry's `counts` carries `total` and `returned` but no `remaining`.

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
| The module statement: the block, the tail, the collapse. | "One bounded knowledge block for several seeds" | mcp/src/agents_remember/application/knowledge_paging/block_pages.py:1-16 |
| Laying seeds out within one threshold. | `bounded_block` | mcp/src/agents_remember/application/knowledge_paging/block_pages.py:39-66 |
| Deferred entries, or one collapsed entry when those would not fit. | `_tail` | mcp/src/agents_remember/application/knowledge_paging/block_pages.py:69-80 |
| A seed's next row, and the smallest form of a later entry. | `_first_row`; `_placeholder` | mcp/src/agents_remember/application/knowledge_paging/block_pages.py:83-95 |
| The envelope the block is measured in. | `_tree_block` | mcp/src/agents_remember/application/published_intent.py:489-507 |

## Cross-Repo References

No meaningful cross-repo references found: the block holds one memory tree's pages.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q1 the whole block is bounded and the remaining seeds are deferred), 20:40:40 (F2 the tail collapse, `oversized_row` only alone) and 21:32:34 (R2-1 carried to L01, R2-2 accepted). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
