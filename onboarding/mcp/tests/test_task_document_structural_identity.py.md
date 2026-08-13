# mcp/tests/test_task_document_structural_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_structural_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate |  2026-08-13T00:18:59+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Holds the task-document identity, topology, migration, structural-gate, and structural-lifecycle
coverage split out of the general leaf structural-coverage suite so both responsibility units stay
below the repository's 1,200-line hard limit.

## Code Commentary

L23 supplies an enclosure reports root to the Windows quality-environment case while preserving inherited Windows temp-variable behavior.

### Logic

The suite proves legacy terminal rows resolve to sprint/master/leaf task identities, task topology
fails closed, structural gates authorize only canonical relations, lifecycle routing preserves the
same identity, and the quality environment keeps the native-Windows temporary-directory branch.

### Conventions

Tests exercise structural addresses through task-document references; they never make runtime or
session identifiers part of the agent-facing contract.

### Invariants And Boundaries

- Sprint roles bind to the sprint document, managers to the master document, and leaf roles to the
  leaf document.
- Replacement does not change the structural address.
- This is a responsibility split only; it does not weaken or duplicate the assertions.

### Todos

None.

## Docs References

No Domain Documentation source is configured for this repository-local structural test suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Migration and topology use canonical task-document identity. | `test_terminal_catalog_migration_maps_every_legacy_identity`; `test_task_document_topology_children_and_refusals` | mcp/tests/test_task_document_structural_identity.py:20-103; mcp/tests/test_task_document_structural_identity.py:161-211 |
| Structural gates and lifecycles fail closed around the same topology. | `test_structural_gate_authorization_decision_and_listing`; `test_structural_lifecycle_gate_and_context_refusals` | mcp/tests/test_task_document_structural_identity.py:262-353; mcp/tests/test_task_document_structural_identity.py:355-390 |
| The native-Windows scratch branch remains explicit. | `test_quality_environment_has_a_windows_branch` | mcp/tests/test_task_document_structural_identity.py:491-496 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed a return statement after an unconditional fixture exception; structural identity and native-Windows environment coverage remain unchanged.
- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from the task-identity half of
  `test_leaf_structural_coverage.py`; preserved the structural contract while bringing both test
  responsibility units below the hard file-size gate.
