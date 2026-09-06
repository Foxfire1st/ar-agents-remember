# mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Cheap exact-path routing before citation claims pay for structural history reads.

## Code Commentary

### Logic

Module-level surface:

- `LocalCitation` (class, lines 23-27)
- `CitationPartition` (class, lines 30-34)
- `ClaimRoute` (class, lines 37-42)
- `PathRead` (class, lines 45-48)
- `RepositoryRouteMetrics` (class, lines 51-66)
- `RepositoryChanges` (class, lines 69-169) — One working census and one object comparison per distinct resolved commit.
- `ClaimChangeRouter` (class, lines 172-237)
- `partition_citations` (function, lines 240-251)
- `classify_citation` (function, lines 254-273)
- `_status_paths` (function, lines 276-292)
- `_name_status_paths` (function, lines 295-317)
- `_nul_fields` (function, lines 320-326)
- `_under` (function, lines 329-334)
- `_git_error` (function, lines 337-339)

This router can skip semantic history only after proving an exact local path unchanged across
its verified object history, HEAD membership, and current working state. Dirty or untracked paths,
paths absent from HEAD (including ignored untracked evidence), and changed history require semantic
comparison; Git census failures remain errors. Code and memory each have a distinct repository
comparison cache, memory history resolves through the code-to-memory mapping, and dependency
citations stay partitioned for their own history owner. The shortcut never grants a semantic
no-impact judgment from a missing or unreadable observation.

cit:([`RepositoryChanges`], mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:69-169)
cit:([`ClaimChangeRouter`], mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:172-237)
cit:([`partition_citations`], mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:240-251)

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
| Defines the class `LocalCitation` (lines 23-27). | `LocalCitation` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:23-27 |
| Defines the class `CitationPartition` (lines 30-34). | `CitationPartition` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:30-34 |
| Defines the class `ClaimRoute` (lines 37-42). | `ClaimRoute` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:37-42 |
| Defines the class `PathRead` (lines 45-48). | `PathRead` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:45-48 |
| Defines the class `RepositoryRouteMetrics` (lines 51-66). | `RepositoryRouteMetrics` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:51-66 |
| Defines the class `RepositoryChanges` (lines 69-169) — One working census and one object comparison per distinct resolved commit.. | `RepositoryChanges` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:69-169 |
| Defines the class `ClaimChangeRouter` (lines 172-237). | `ClaimChangeRouter` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:172-237 |
| Defines the function `partition_citations` (lines 240-251). | `partition_citations` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:240-251 |
| Defines the function `classify_citation` (lines 254-273). | `classify_citation` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:254-273 |
| Defines the function `_status_paths` (lines 276-292). | `_status_paths` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:276-292 |
| Defines the function `_name_status_paths` (lines 295-317). | `_name_status_paths` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:295-317 |
| Defines the function `_nul_fields` (lines 320-326). | `_nul_fields` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:320-326 |
| Defines the function `_under` (lines 329-334). | `_under` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:329-334 |
| Defines the function `_git_error` (lines 337-339). | `_git_error` | mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py:337-339 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
