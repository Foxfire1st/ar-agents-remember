# mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T17:20+02:00 |
| lastVerifiedCommitHash | `270704b86116728a64ada83ee258a0e7726206b4` |
| lastVerifiedCommitDate | 2026-09-14T18:18:08+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Cheap exact-path routing before citation claims pay for structural history reads.

## Code Commentary

### Logic

Module-level surface:

- `LocalCitation` (class, lines 27-31)
- `CitationPartition` (class, lines 34-38)
- `ClaimRoute` (class, lines 41-46)
- `PathRead` (class, lines 49-52)
- `RepositoryRouteMetrics` (class, lines 55-70)
- `RepositoryChanges` (class, lines 73-173) — One working census and one object comparison per distinct resolved commit.
- `ClaimChangeRouter` (class, lines 176-241)
- `partition_citations` (function, lines 244-255)
- `classify_citation` (function, lines 258-277)
- `_status_paths` (function, lines 280-296)
- `_name_status_paths` (function, lines 299-321)
- `_nul_fields` (function, lines 324-330)
- `_under` (function, lines 333-338)
- `_git_error` (function, lines 341-343)

This router can skip semantic history only after proving an exact local path unchanged across
its verified object history, HEAD membership, and current working state. Dirty or untracked paths,
paths absent from HEAD (including ignored untracked evidence), and changed history require semantic
comparison; Git census failures remain errors. Code and memory each have a distinct repository
comparison cache, memory history resolves through the code-to-memory mapping, and dependency
citations stay partitioned for their own history owner. The shortcut never grants a semantic
no-impact judgment from a missing or unreadable observation.

cit:([`RepositoryChanges`], mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:73-173)
cit:([`ClaimChangeRouter`], mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:176-241)
cit:([`partition_citations`], mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:244-255)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `LocalCitation` (lines 27-31). | `LocalCitation` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:27-31 |
| Defines the class `CitationPartition` (lines 34-38). | `CitationPartition` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:34-38 |
| Defines the class `ClaimRoute` (lines 41-46). | `ClaimRoute` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:41-46 |
| Defines the class `PathRead` (lines 49-52). | `PathRead` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:49-52 |
| Defines the class `RepositoryRouteMetrics` (lines 55-70). | `RepositoryRouteMetrics` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:55-70 |
| Defines the class `RepositoryChanges` (lines 73-173) — One working census and one object comparison per distinct resolved commit.. | `RepositoryChanges` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:73-173 |
| Defines the class `ClaimChangeRouter` (lines 176-241). | `ClaimChangeRouter` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:176-241 |
| Defines the function `partition_citations` (lines 244-255). | `partition_citations` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:244-255 |
| Defines the function `classify_citation` (lines 258-277). | `classify_citation` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:258-277 |
| Defines the function `_status_paths` (lines 280-296). | `_status_paths` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:280-296 |
| Defines the function `_name_status_paths` (lines 299-321). | `_name_status_paths` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:299-321 |
| Defines the function `_nul_fields` (lines 324-330). | `_nul_fields` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:324-330 |
| Defines the function `_under` (lines 333-338). | `_under` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:333-338 |
| Defines the function `_git_error` (lines 341-343). | `_git_error` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:341-343 |

## Update History

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): the three `RepositoryChanges` history reads (`_working_paths`, `_head_paths`,
  `_historical_paths`) now hand the runner one `GitRunnerOptions(timeout=GIT_METADATA_TIMEOUT_SECONDS)`
  object instead of a `timeout=` keyword. No content impact: this card stated no `run_git` call form,
  so every claim above still holds. The migration grew the `kernel.git_command` import block by four
  lines, so all fourteen symbol ranges in the Logic list, the three `cit` lines and the reference
  table were re-derived against the current file — each one moved by exactly +4 (`LocalCitation`
  23-27 → 27-31, `RepositoryChanges` 69-169 → 73-173, `_git_error` 337-339 → 341-343) — and
  `kernel/git_command.py` now declares `GitRunnerOptions` at `:115-128` with `run_git` at `:149-213`,
  and verification metadata remains closeout-owned.

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
