# mcp/tests/test_leaf_structural_coverage.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_leaf_structural_coverage.py`                  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-11T22:28+02:00                                       |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                   |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[tests overview](overview.md)

## Purpose

This focused coverage module reaches cross-package leaf seams that are intentionally smaller than
the domain suites. It retains the layering, context-resolution, provider, evidence, catalog, and
worktree edge coverage and now exercises L19's structural migration/topology/gate paths plus the
non-Windows quality-scratch boundary needed by the targeted 100% changed-code coverage contract.

## Code Commentary

### Logic

The first half covers the pre-existing wrapper-adjacent seams: layering CLI/rendering, coordination
context resolution, gate vocabulary, drift cleanup, catalog behavior, evidence/control clients,
provider status, and contract-reader failure modes. The L19 extension groups four current
boundaries: terminal/control-plane migrations; task-document topology and role validation;
structural gate authorization and lifecycle results; and the platform branch that leaves inherited
temp variables intact on Windows while production normalizes non-Windows scratch.

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
| The suite complements the layering unit tests with wrapper-adjacent seams. | `test_layering_cli_and_edges`; `test_layering_render_and_stale` | mcp/tests/test_leaf_structural_coverage.py:84-121; mcp/tests/test_leaf_structural_coverage.py:141-168 |
| The L19 extension covers migration, task-topology, and structural-gate branches. | `test_terminal_catalog_migration_maps_every_legacy_identity`; `test_task_document_topology_children_and_refusals`; `test_structural_gate_authorization_decision_and_listing` | mcp/tests/test_leaf_structural_coverage.py:855-939; mcp/tests/test_leaf_structural_coverage.py:996-1047; mcp/tests/test_leaf_structural_coverage.py:1097-1189 |
| The platform branch preserves inherited temp paths only on native Windows. | `test_quality_environment_has_a_windows_branch` | mcp/tests/test_leaf_structural_coverage.py:1327-1332 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the appended structural
  migration, topology, gate, identity-migration, and quality-environment branch coverage. This is a
  focused coverage companion; verification metadata remains pinned until closeout.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the structural-coverage suite;
  F-4 cycle-coverage note reflected. Verification metadata pinned until closeout stamps the L9
  code commit.
