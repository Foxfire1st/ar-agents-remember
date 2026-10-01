# mcp/src/agents_remember/memory_quality/style/citations/claim_change_router.py

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

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `LocalCitation` (lines 27-31). [1]
- Defines the class `CitationPartition` (lines 34-38). [2]
- Defines the class `ClaimRoute` (lines 41-46). [3]
- Defines the class `PathRead` (lines 49-52). [4]
- Defines the class `RepositoryRouteMetrics` (lines 55-70). [5]
- Defines the class `RepositoryChanges` (lines 73-173) — One working census and one object comparison per distinct resolved commit.. [6]
- Defines the class `ClaimChangeRouter` (lines 176-241). [7]
- Defines the function `partition_citations` (lines 244-255). [8]
- Defines the function `classify_citation` (lines 258-277). [9]
- Defines the function `_status_paths` (lines 280-296). [10]
- Defines the function `_name_status_paths` (lines 299-321). [11]
- Defines the function `_nul_fields` (lines 324-330). [12]
- Defines the function `_under` (lines 333-338). [13]
- Defines the function `_git_error` (lines 341-343). [14]
