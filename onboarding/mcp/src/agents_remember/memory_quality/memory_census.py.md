# mcp/src/agents_remember/memory_quality/memory_census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/memory_census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-09 |
| lastVerifiedCommitHash | `8133b6a9de2f787cb6c4527621a70123357aff31` |
| lastVerifiedCommitDate | 2026-09-08T13:24:49+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Memory quality overview](overview.md)

## Purpose

Builds the deterministic governed-memory census from the contract-owned exact Git scope. The census reads exact code and memory trees, classifies file sidecars, inline onboarding, route overviews, and entity rows, and emits a structural worklist without making semantic acceptance or final-certification decisions.

## Code Commentary

### Logic

`_Tree` reads exact Git members and metadata without silently normalizing paths. `_Census` records governed identities, presence, source paths, and reasons across sidecars, inline blocks, route overviews, edited documents, and entity rows. `build_memory_census` assembles the ordered result from the route-owned `MemoryCensusScope`.

### Invariants And Boundaries

- Exact Git tree membership and UTF-8 relative paths are validated before a row is emitted.
- Missing pre-existing artifacts become structural blockers requiring canonical curator disposition.
- The census is a derived preparation worklist; it does not publish semantic judgments, coherence, or certification.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; the repository source is the governing evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The census module has no external domain dependency. | `build_memory_census` | mcp/src/agents_remember/memory_quality/memory_census.py:478-511 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact Git members and metadata are read through the private tree reader. | `_Tree` | mcp/src/agents_remember/memory_quality/memory_census.py:45-125 |
| Structural rows are accumulated for sidecars, inline onboarding, route overviews, and entities. | `sidecars`; `inline`; `overviews`; `entities` | mcp/src/agents_remember/memory_quality/memory_census.py:261-382; mcp/src/agents_remember/memory_quality/memory_census.py:422-475 |
| The route-owned scope is converted into one ordered census result. | `build_memory_census` | mcp/src/agents_remember/memory_quality/memory_census.py:478-511 |

## Cross-Repo References

None; this module consumes the resolved local code/memory pair only.

## Update History

- 2026-09-09T02:44:55+02:00 — CCR-L38 bounded inherited citation repair: simplified the four anchors to resolvable method identifiers within the existing behavior-bearing ranges; source-sha256=2bbd75f359b0ab57e3c07ffd51253e93e9084a32905742a1a552fac0a14f52dd; verification metadata remains unchanged.

- 2026-09-09T02:43:28+02:00 — CCR-L38 bounded inherited citation repair: restored code-identifier backticks for the four `_Census` anchors so the cited ranges resolve to the behavior-bearing methods; source-sha256=2bbd75f359b0ab57e3c07ffd51253e93e9084a32905742a1a552fac0a14f52dd; verification metadata remains unchanged.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited-source reconciliation: created the previously absent governed sidecar from source bytes matching code commit `8133b6a9de2f787cb6c4527621a70123357aff31` (candidate-tree source SHA-256 `2bbd75f359b0ab57e3c07ffd51253e93e9084a32905742a1a552fac0a14f52dd`). No future candidate verification stamp was used.
