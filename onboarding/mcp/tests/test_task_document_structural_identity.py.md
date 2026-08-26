# mcp/tests/test_task_document_structural_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_structural_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-19T22:32+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Holds the task-document identity, topology, migration, structural-gate, and structural-lifecycle
coverage split out of the general leaf structural-coverage suite so both responsibility units stay
below the repository's 1,200-line hard limit.

## Code Commentary

### Logic

The suite proves legacy terminal rows resolve to sprint/master/leaf task identities, task topology
fails closed, structural gates authorize only canonical relations, and lifecycle routing preserves
the same identity. Since 260815-DAG-L13 the parent-resolution fixture proves the effective-nature
split directly: a nature-less standalone master resolves at master altitude with no parent edge,
and only an explicit `organizational` standalone master still reaches the missing-parent refusal.

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
| Parent-resolution refusals isolate non-atomic master topology explicitly. | `test_task_document_topology_parent_fail_closed_paths` | mcp/tests/test_task_document_structural_identity.py:213-269 |
| Structural gates and lifecycles fail closed around the same topology. | `test_structural_gate_authorization_decision_and_listing`; `test_structural_lifecycle_gate_and_context_refusals` | mcp/tests/test_task_document_structural_identity.py:271-362; mcp/tests/test_task_document_structural_identity.py:364-399 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## R39 Removed Host-Environment Surface

The obsolete Windows branch test for the deleted host quality-environment builder was removed.
Structural-identity tests no longer imply that lifecycle acceptance may construct or inherit a
host test environment.

## 2026-08-26 Public Master-Discovery Boundary

The missing-repository regression now calls the public
`repository_master_documents(topology, repository)` helper rather than reaching into
`TaskDocumentTopology._master_documents`. It preserves the empty-result behavior while pinning
the supported application boundary instead of a private implementation detail.

## Update History

- 2026-08-26T10:44:52+02:00 — Updated the absent-repository master-discovery assertion to the public helper boundary.
- 2026-08-19T22:32+02:00 — 260815-DAG-L13: the parent-resolution fixture now proves the
  effective-nature split — a nature-less standalone master resolves at master altitude, and only
  an explicit `organizational` standalone still fails closed. Also re-ranged the reference rows to
  the current test positions. Verification remains closeout-owned.

- 2026-08-16T01:45+02:00 — Documented why the parent-refusal fixture explicitly declares non-atomic execution nature; verification remains closeout-owned.
- 2026-08-16T00:45+02:00 — Kept the fail-closed topology proof current by making the master fixture state its non-atomic execution nature explicitly; behavior remains unchanged and verification remains closeout-owned.
- 2026-08-14T11:27+02:00 — R39 curator: removed the stale host-environment interpretation.
  Verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed a return statement after an unconditional fixture exception; structural identity and native-Windows environment coverage remain unchanged.
- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from the task-identity half of
  `test_leaf_structural_coverage.py`; preserved the structural contract while bringing both test
  responsibility units below the hard file-size gate.
