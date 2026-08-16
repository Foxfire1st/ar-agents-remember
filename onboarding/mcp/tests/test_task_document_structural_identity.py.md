# mcp/tests/test_task_document_structural_identity.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_task_document_structural_identity.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T08:41+02:00 |
| lastVerifiedCommitHash |  `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate |  2026-08-16T10:54:02+02:00|
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
the same identity. The parent-resolution refusal fixture explicitly declares a non-atomic execution
nature, ensuring the test reaches missing-parent and ambiguous-parent topology behavior instead of
accidentally entering the newer atomic-master classification path.

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
| Migration and topology use canonical task-document identity. | `test_terminal_catalog_migration_maps_every_legacy_identity`; `test_task_document_topology_children_and_refusals` | mcp/tests/test_task_document_structural_identity.py:20-102; mcp/tests/test_task_document_structural_identity.py:161-210 |
| Parent-resolution refusals isolate non-atomic master topology explicitly. | `test_task_document_topology_parent_fail_closed_paths` | mcp/tests/test_task_document_structural_identity.py:213-259 |
| Structural gates and lifecycles fail closed around the same topology. | `test_structural_gate_authorization_decision_and_listing`; `test_structural_lifecycle_gate_and_context_refusals` | mcp/tests/test_task_document_structural_identity.py:262-352; mcp/tests/test_task_document_structural_identity.py:355-389 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## R39 Removed Host-Environment Surface

The obsolete Windows branch test for the deleted host quality-environment builder was removed.
Structural-identity tests no longer imply that lifecycle acceptance may construct or inherit a
host test environment.

## Update History

- 2026-08-16T01:45+02:00 — Documented why the parent-refusal fixture explicitly declares non-atomic execution nature; verification remains closeout-owned.
- 2026-08-16T00:45+02:00 — Kept the fail-closed topology proof current by making the master fixture state its non-atomic execution nature explicitly; behavior remains unchanged and verification remains closeout-owned.
- 2026-08-14T11:27+02:00 — R39 curator: removed the stale host-environment interpretation.
  Verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed a return statement after an unconditional fixture exception; structural identity and native-Windows environment coverage remain unchanged.
- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from the task-identity half of
  `test_leaf_structural_coverage.py`; preserved the structural contract while bringing both test
  responsibility units below the hard file-size gate.
