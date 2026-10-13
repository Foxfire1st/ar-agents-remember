# mcp/src/agents_remember/application/knowledge_paging/__init__.py

## Governing Overview

[application route overview](../overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [3]

## Purpose

**Bounded continuation accepted by the mounted read (MIK-R02@v2): the package's front door.** Every bounded read of a converted memory tree is cut by one declared token threshold into pages of whole rows, and each page carries the one continuation that the mounted `knowledge_read` resumes, whichever surface minted it. The package re-exports the threshold, the pager types, `CutBudget`, `cut_page` and `page_block`. Mounted `knowledge_read` pages naming responses; mounted `read_ar_files` is stateless naming with no continuation.

## Code Commentary

### Logic

- **Module map.** `threshold` (the one constant), `pager` (cutting whole rows), `bindings` (minting and refusing a continuation), `scope_pages` (the scope read behind the published-intent block), `block_pages` (retained internal published-intent block paging, not a mounted `read_ar_files` answer), `view_pages` (the named views), `currentness` (MIK-R03 state computed once per page) and `tree_read` (the converted-tree branch of `knowledge_read`). The token model is `models/knowledge/continuation.py`.
- **Retained paging computations:** family-complete leaf selections (including `knowledge_read`'s `source_context`), internal published-intent identity-scope selections, and named knowledge views. Their rich computations remain internal; the mounted knowledge read delivers names. `read_ar_files` no longer attaches or resumes a published-intent block.
- **The seam for MIK-R01 and MIK-R05.** A response owner that pages supplies its ordered selection as `PageRow` values (a family header row carries its `reference`, members name the family as `group`), a manifest digest over that order, and a policy name and version; route-chain entries are further rows after the family content, so they count toward the same threshold and resume through the same token.
- `tree_read` is imported by its own module path, not re-exported, because it depends on the published-intent route, which in turn pages through `scope_pages` (an import cycle otherwise).

### Conventions

- The docstring is the package's design statement; the per-module docstrings carry each rule's detail.

### Invariants And Boundaries

- **No cursor state is kept on the server.** The token is the whole state of a walk.
- **The seam does not decide what is selected.** Rows are the leaf read's rows (MIK-R01 owns their order and composition), the scope read's items and the view renderer's rows, each in its owner's order.
- **Historical pre-MIK-R37 preservation:** earlier unconverted-database budget/cursor and byte-identity observations describe that earlier stage only. Mounted knowledge reads now refuse legacy format before opening a canonical database; those historical measurements establish no current execution acceptance.

### Todos

- **Resolved by MIK-R01 (L01):** the header reference is the literal first row of a leaf page that continues a family (`knowledge_leaf/pages.py`); a view page still names it in `page.headerReference`. The first-64-rows projection cut is removed on converted trees (`knowledge_projection.py`, `whole_views`), and the more-than-64-seeds edge is the named refusal `seed_queue_exceeded` (`block_pages.py`), both accepted by the ruling of 2026-09-29 23:21:57.
- MIK-R05 route-chain entries are already part of the internal ordered selection after family content; the mounted naming projection changes representation, not selection.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R02@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`02_bounded-continuation-accepted-by-the-mounted-read.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The package statement: one threshold, whole-row pages, one continuation any surface's page resumes. [1]
- The re-exported names. [2]

### Cross-Repo References

No meaningful cross-repo references found: the package pages one memory tree's derived index and names no other repository.

No cross-repo boundary is crossed by this file.
