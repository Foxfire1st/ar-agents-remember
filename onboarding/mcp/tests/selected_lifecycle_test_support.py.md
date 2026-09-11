# mcp/tests/selected_lifecycle_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/selected_lifecycle_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:46:49+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Builds selected lifecycle fixtures through the real task, door, admission and journal owners. It keeps those fixtures separate from bare journal/component repositories and distinguishes completion bookkeeping from certification execution.

## Code Commentary

### Logic

`declare_selected_candidate` reloads the contract and preserves an existing door. For an undeclared leaf it resolves the actual leaf document, writes fixture requirements and a completed setup step, obtains canonical task context and activates atomic series selection under the integration authority lock when required. It authors route-review and scheduling rows plus fixture curator evidence, then invokes the actual door owner with the fixture manager's task identity. It requires a waiting door whose declared identity is not the synthetic `test-fixture:` form. The authored prerequisites are test setup; this helper does not run full memory certification.

`selected_closeout_operation_input` declares the prepared candidate before normalizing input. `selected_contract` reuses the public-entrypoint fixture and forwards optional candidate-file setup before the initial declaration. Existing doors are never silently replaced to make later mutations current.

`ready_selected_integration` records a completed contract edge using the actual integration-target commit. `completed_selected_closeout_for_integration` delegates to `finish_closeout_for_integration`, which starts the real journal/runtime and drives approval and contract-finalization progress before finishing the record. It checks durable door-publication proof and the exact finalized contract hash. These are bookkeeping fixtures, not execution of code gates, memory gates or protected-ref writers.

`selected_successor` observes the current candidate tree, calls actual preparation with the prior record and returns the queued candidate plus an initial-selection callback. `replace_selected_fixture_generation` makes the prior fixture terminal and calls actual terminal replacement with that callback, publishing the successor and its selected references together.

### Conventions

Callers install profiles and prepare candidate bytes before declaration. Scenario mutations stay in consumer tests. Fixture actor and scheduling data belong to the isolated task world and grant no host lifecycle authority.

### Invariants And Boundaries

- Declared fixture doors come from the actual owner; existing doors are preserved.
- Completion bookkeeping retains real commit identities and journal transitions but makes no certification claim.
- Successor generations receive actual prepared references through the store initial-selection callback.
- The helpers do not replace the selected-operation guard or implement a parallel production closeout workflow.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this file. | N/A | N/A |

## Repo-Internal References

These source anchors establish the actual owner calls, fixture inputs and execution limits described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Task, route-review, series and door owners declare the prepared candidate while preserving existing doors. | `declare_selected_candidate` | mcp/tests/selected_lifecycle_test_support.py:66-161 |
| Input normalization follows explicit declaration. | `selected_closeout_operation_input` | mcp/tests/selected_lifecycle_test_support.py:164-169 |
| Candidate-file setup is forwarded before initial declaration. | `selected_contract` | mcp/tests/selected_lifecycle_test_support.py:172-181 |
| Contract-only integration setup uses the actual target-branch commit. | `ready_selected_integration` | mcp/tests/selected_lifecycle_test_support.py:184-191 |
| Completion setup drives real journal bookkeeping and verifies the door proof. | `finish_closeout_for_integration` | mcp/tests/selected_lifecycle_test_support.py:202-241 |
| Successor preparation supplies initial selection to the store transaction. | `selected_successor` | mcp/tests/selected_lifecycle_test_support.py:244-259 |
| Terminal replacement consumes the prepared successor and callback together. | `replace_selected_fixture_generation` | mcp/tests/selected_lifecycle_test_support.py:262-272 |

## Cross-Repo References

The modeled or temporary repositories belong to this isolated test composition. This file establishes no external repository or host lifecycle authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence is required. | N/A | N/A |

## Update History

- 2026-09-06T14:46:49+00:00 — Created after reviewing actual source at `c69d5171187fa1957025e393270db9f5a864ab14`. Documented real selected authority, authored fixture prerequisites and completion bookkeeping. Related lifecycle-test histories remain at their existing owners. This source verification makes no gate or acceptance claim.
