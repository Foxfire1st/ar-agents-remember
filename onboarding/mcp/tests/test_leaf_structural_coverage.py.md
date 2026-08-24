# mcp/tests/test_leaf_structural_coverage.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_leaf_structural_coverage.py`                  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-08-24T21:23+02:00 |
| lastVerifiedCommitHash | `b99501852bcfa5f499a25e7183063751f6133a28` |
| lastVerifiedCommitDate | 2026-08-24T21:21:58+02:00 |
| governingOverview      | `overview.md`                                                |

## Governing Overview

[tests overview](overview.md)

## Purpose

This focused coverage module reaches cross-package leaf seams that are intentionally smaller than
the domain suites. It retains layering, context-resolution, provider, evidence, catalog, and
worktree edge coverage. Task-document identity, topology, and structural-gate branches now live in
`test_task_document_structural_identity.py`.

## Code Commentary

### Logic

The first half covers the pre-existing wrapper-adjacent seams: layering CLI/rendering, coordination
context resolution, gate vocabulary, drift cleanup, catalog behavior, evidence/control clients,
provider status, and contract-reader failure modes. The identity and lifecycle extension is split
into its own responsibility unit rather than keeping an ever-growing mixed structural suite.

### Conventions

These tests import narrow production modules at the point of use and use mocks only to force
otherwise rare branches. They are coverage companions, not an alternative behavioral authority to
the focused domain suites or the new refusal matrix.

### Invariants And Boundaries

- This suite exists because the diff-coverage floor is 100% with no exemption list: any new
  structural seam must be reached here or in a domain suite.
- Passing this module alone does not certify L19: the targeted gate may conservatively expand to
  its derived full selection when coverage fragments cannot be merged narrowly.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite complements the layering unit tests with wrapper-adjacent seams. | `test_layering_cli_and_edges`; `test_layering_render_and_stale` | mcp/tests/test_leaf_structural_coverage.py:83-119; mcp/tests/test_leaf_structural_coverage.py:140-167 |
| The L19 extension covers migration, task-topology, and structural-gate branches. | `test_terminal_catalog_migration_maps_every_legacy_identity`; `test_task_document_topology_children_and_refusals`; `test_structural_gate_authorization_decision_and_listing` | mcp/tests/test_task_document_structural_identity.py:20-159; mcp/tests/test_task_document_structural_identity.py:161-260; mcp/tests/test_task_document_structural_identity.py:262-390 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260824-PDLS Cohort Extraction

The unknown gate-kind assertion moved unchanged to the bounded direct cohort. The remaining
structural-coverage vocabulary tests retain their existing ownership.

## Update History

- 2026-08-24T21:23+02:00 — Moved one gate-kind assertion to the bounded direct cohort.

- 2026-08-12T08:41+02:00 — 260731-EFA-L20 citation maintenance: re-anchored the split suite's native-Windows quality-environment test after dead-code removal; the assertion contract is unchanged.
- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: moved the task-document identity/topology half
  into its own one-to-one test card and refreshed all surviving citations; both files are below the
  hard size limit.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the appended structural
  migration, topology, gate, identity-migration, and quality-environment branch coverage. This is a
  focused coverage companion; verification metadata remains pinned until closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the structural-coverage suite;
  F-4 cycle-coverage note reflected. Verification metadata pinned until closeout stamps the L9
  code commit.
