# mcp/src/agents_remember/application/knowledge_paging/tree_read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_paging/tree_read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T21:41:17+02:00 |
| lastVerifiedCommitHash | `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4`|
| lastVerifiedCommitDate | 2026-09-29T22:20:46+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The mounted `knowledge_read` over a converted memory tree: pages and continuations (MIK-R02).** A read of a memory tree is always a bounded page of one selection, and a continuation is accepted whichever surface minted it: a view token resumes that view's walk; a scope token (from the published-intent block, or an earlier scope page) answers `state: "page"` with the scope page as `payload`.

## Code Commentary

### Logic

- `read_tree_page(request, selected, context, *, extras, workspace_root)`: a fresh read is a view walk bound to the code tree the caller named, and only that one (`_at_code_tree`). A resume decodes the token (`read_continuation`), then checks the memory tree, threshold and policy, the named subject (`_subject_refusal`), the ordering and the code tree, all before any selection is read.
- **The ordering (rulings Q5 and F1).** `DEFAULT_ORDERING = "stable_ordering"` applies only when `orderingInput` is absent (`None`); an empty string keeps the base refusal `unadmitted_ordering_input` on every path. A view token's seed carries the effective ordering, and a resume reads in it.
- **The code tree (rulings Q6, F2, F4 and 21:32:34).** The token binds only the Git tree ID. On resume the objects are read from the caller's `repositoryRoot`, else the mount's workspace, and `_missing_code_tree` checks `git cat-file -e <tree>^{tree}`: a root that does not hold it, or no known root, is refused `selected_input_unavailable`, naming the root and `repositoryRoot` as the relocation input.
- `_view_response`/`_view_page` and `_scope_response`: each prepares the page extras once (`_TreeRead.prepared`: `memoryTree`, `indexComplete`, and the caller's `TreeExtras` of proofs and currentness) and lets `cut_page` render candidates, so the extras count toward the threshold.
- `_refused` adds `threshold` to every refusal (ruling F8). The architect's R2-3 fix reworded the F4 detail for a missing root.

### Conventions

- `ToolReadRequest` is a `Protocol` of the tool arguments; `ReadSubject` is the caller's subject or the token's seed.

### Invariants And Boundaries

- **No partial page on a refusal**, and nothing is kept between calls.
- `limit` does not bound a tree read; the threshold does (ruling Q4).
- **Base defect, not fixed (carried to L01):** a `repositoryRoot` whose repository has no commit raises `ValidationError` from `open_read_context`, at base and here.

### Todos

- None recorded here; the base defect above belongs to L01's read-surface work.

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
| The module statement: any surface's token, bound ordering and code tree, threshold on every response. | "over a converted memory tree: pages and continuations" | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:1-19 |
| The default ordering, applied only when none is named. | `DEFAULT_ORDERING`; `_requested_subject` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:88-88; mcp/src/agents_remember/application/knowledge_paging/tree_read.py:220-229 |
| The subject a page is read about. | `ReadSubject` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:124-143 |
| The dispatch and the checks before any selection. | `read_tree_page` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:175-217 |
| The walk's code tree, and a root that does not hold it. | `_at_code_tree`; `_missing_code_tree`; `_holds_tree` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:232-276 |
| A view page and a resumed scope page. | `_view_response`; `_scope_response` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:315-444 |
| Every refusal states the threshold. | `_refused` | mcp/src/agents_remember/application/knowledge_paging/tree_read.py:447-456 |

## Cross-Repo References

No meaningful cross-repo references found: the code tree is read from the caller's `repositoryRoot` or the mount's workspace, both the same code repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T21:41:17+02:00 — 260928-MIK-L02 curator (uncommitted change set on `ar/260928-mik-l02`, code base `a4eba7b7b5b5ffee7277f6c19086697925a22df2` plus the staged delta): created this card for the new file MIK-R02 adds. It records the architect rulings of 2026-09-29 19:56:40 (Q4, Q5, Q6), 20:40:40 (F1 the empty ordering is refused; F2 no local path; F3 currentness at the walk's tree; F4 the named relocation refusal; F8 refusals state the threshold) and 21:32:34 (the tree ID plus a root check is the accepted binding; R2-3 cosmetic fixed). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
