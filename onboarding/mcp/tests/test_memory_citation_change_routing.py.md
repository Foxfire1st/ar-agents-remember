# mcp/tests/test_memory_citation_change_routing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_change_routing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Owns citation-check registration, bounded source-view caching, and routing across code, memory,
dependency, dirty, untracked, ignored, and failure histories. It is the routing half split from the
larger provenance-history suite to satisfy the file-size gate without changing behavior.

## Code Commentary

### Logic

`RegistrationAndLimitsTests` pins registration and the bounded revision cache. `ChangeRoutingTests`
uses the shared real-Git fixture to prove each evidence kind is evaluated against its own history,
that relevant dirty shapes reach semantic authority, and that census failures fail explicitly.

### Conventions

The shared `ChangeDetectionCase`, `ProvenanceTree`, and `git` fixtures remain in the history suite;
this module imports them rather than copying a second fixture implementation.

### Invariants And Boundaries

- Routing never treats untracked or ignored evidence as proven unchanged.
- Code, memory, and dependency claims resolve against distinct histories.
- The split changes ownership only, not the checker contract.

### Todos

None.

## Docs References

No Domain Documentation source is configured for these repository-local regressions.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Registration and bounded cache behavior remain explicit. | `RegistrationAndLimitsTests` | mcp/tests/test_memory_citation_change_routing.py:20-47 |
| Routing tests cover dirty, untracked, failure, and separated-history paths. | `ChangeRoutingTests` | mcp/tests/test_memory_citation_change_routing.py:49-364 |
| Shared real-Git fixtures remain single-owned by the history suite. | `ChangeDetectionCase`; `ProvenanceTree`; `git` | mcp/tests/test_memory_citation_change_detection.py:24-35; mcp/tests/test_memory_citation_change_detection.py:37-105; mcp/tests/test_memory_citation_change_detection.py:108-121 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 made the census-failure mock assert the one invoked status path directly and removed the script-only main guard; the explicit-failure routing contract is unchanged.
- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from the registration/routing half of
  `test_memory_citation_change_detection.py`; retained shared real-Git fixtures and brought both
  test responsibility units below the hard file-size gate.
