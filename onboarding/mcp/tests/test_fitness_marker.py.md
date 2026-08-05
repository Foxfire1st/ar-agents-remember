# mcp/tests/test_fitness_marker.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_fitness_marker.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

The ``fitness`` marker selects exactly the inherited S1-S4 acceptance surface.

## Code Commentary

### Logic

Module-level surface:

- `collect_nodes` (function, lines 59-89)
- `selector_contribution` (function, lines 92-93)
- `FitnessMarkerContractTests` (class, lines 96-123)

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
| Defines the function `collect_nodes` (lines 59-89). | `collect_nodes` | mcp/tests/test_fitness_marker.py:59-89 |
| Defines the function `selector_contribution` (lines 92-93). | `selector_contribution` | mcp/tests/test_fitness_marker.py:92-93 |
| Defines the class `FitnessMarkerContractTests` (lines 96-123). | `FitnessMarkerContractTests` | mcp/tests/test_fitness_marker.py:96-123 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
