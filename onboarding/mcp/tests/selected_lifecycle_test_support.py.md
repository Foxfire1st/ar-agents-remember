# mcp/tests/selected_lifecycle_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/selected_lifecycle_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-11T23:05:00+00:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Builds the selected lifecycle fixture door through the real task, route-review, atomic-series and
door owners. The fixture keeps its authored prerequisites distinct from certification execution and
returns a declared waiting door whose declared identity is never the synthetic `test-fixture:` form.

## Code Commentary

### Logic

`declare_selected_candidate` reloads the contract and preserves an existing door. For an undeclared
leaf it resolves the actual terminal leaf document, writes fixture requirements and a completed
setup step, obtains canonical task context, and activates atomic series selection under the
integration authority lock when the master is atomic. It authors a route-review record plus fixture
judgment/priority rows and, for external memory, fixture curator evidence, then invokes the actual
door owner with the fixture manager's task identity. It requires a waiting door whose declared
identity is not the synthetic `test-fixture:` form. The authored prerequisites are test setup; this
helper does not run full memory certification.

`selected_closeout_operation_input` declares the prepared candidate before normalizing input through
the shared closeout-input owner. `selected_contract` reuses the public-entrypoint fixture, reloads
the contract and requires its live waiting door with a non-synthetic declarer. Existing doors are
never silently replaced to make later mutations current.

### Conventions

Callers install profiles and prepare candidate bytes before declaration. Scenario mutations stay in
consumer tests. Fixture actor and scheduling data belong to the isolated task world and grant no
host lifecycle authority.

### Invariants And Boundaries

- Declared fixture doors come from the actual owner; existing doors are preserved.
- The fixture never invents a synthetic declarer identity, so downstream declaration provenance
  assertions still see the real actor.
- The helpers do not replace the selected-operation guard or implement a parallel production
  closeout workflow.
- Completion bookkeeping for integration is not part of this module: the former
  `ready_selected_integration`, `finish_closeout_for_integration`,
  `completed_selected_closeout_for_integration`, `selected_successor` and
  `replace_selected_fixture_generation` helpers were deleted deliberately by commit `173bb01e`
  (2026-09-10, the detached-lifecycle-worker deletion), not lost. `git log -S
  'finish_closeout_for_integration' -- mcp/tests` names that commit.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this file. | N/A | N/A |

## Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described
above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Task, route-review, series and door owners declare the prepared candidate while preserving existing doors. | `declare_selected_candidate` | mcp/tests/selected_lifecycle_test_support.py:46-141 |
| Input normalization follows explicit declaration. | `selected_closeout_operation_input` | mcp/tests/selected_lifecycle_test_support.py:144-149 |
| Public-entrypoint fixture reuse requires a live non-synthetic waiting door. | `selected_contract` | mcp/tests/selected_lifecycle_test_support.py:152-162 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file
establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History
- 2026-09-11T23:05:00+00:00: Curator content reconciliation: the module now holds only the declaration, operation-input and contract helpers. Recorded that the integration-completion and successor-generation helpers (`ready_selected_integration`, `finish_closeout_for_integration`, `completed_selected_closeout_for_integration`, `selected_successor`, `replace_selected_fixture_generation`) were deleted deliberately by `173bb01e`, and removed their claims. The retained claims keep their behavior at their current extents.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `selected_closeout_operation_input` repointed to mcp/tests/selected_lifecycle_test_support.py:144-149. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `selected_contract` repointed to mcp/tests/selected_lifecycle_test_support.py:152-162. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented real selected authority, authored fixture prerequisites and completion bookkeeping. Related lifecycle-test histories remain at their existing owners. This source verification makes no gate or acceptance claim.
