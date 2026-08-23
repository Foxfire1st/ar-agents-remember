# mcp/tests/test_lifecycle_operation_dispositions_l2.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_operation_dispositions_l2.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T17:03+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces completed-closeout disposition authorization, publication, and recovery at the public and
durable-state boundaries.

## Code Commentary

### Logic

The principal forcing seams are `test_completed_unintegrated_disposition_preserves_artifacts`,
`test_sprint_orchestrator_status_payload_executes_public_disposition`,
`test_completed_disposition_is_not_advertised_or_executable_by_leaf`,
`test_status_keeps_completed_closeout_actionable_beside_newer_cancelled_integrate`, and
`test_public_disposition_recovers_before_and_after_contract_publication`. The suite directly calls
`completed_disposition_authorized` to prove that both a standalone task owner and its sprint
orchestrator may disposition a completed closeout, while a leaf worker may not. It then forces the
same authority boundary through advertised public controls, executable refusal, immutable artifact
preservation, coexistence with a newer cancelled integration, and recovery across contract-
publication crash cuts.

### Conventions

Tests address operations by task/contract plus kind and generation, assert durable evidence and public legal controls, and compare state across failure cuts. Helpers remain test-only and invoke the same public/domain seams as production.

### Invariants And Boundaries

- A passing assertion must prove the advertised action executes or terminates safely; payload shape alone is insufficient.
- Completed-disposition controls are owner-scoped: standalone ownership and sprint orchestration
  authorize them, while leaf execution is neither advertised nor accepted.
- Queue projection is never accepted as lifecycle evidence, and private operation identifiers do not cross the public test boundary.
- Failure-path assertions check non-mutation or exact same-generation recovery, not merely an exception string.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to these repository-internal forcing tests.

## Repo-Internal References

The test source is the direct evidence for the regression contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The file defines five public completed-closeout disposition forcing seams covering artifact preservation, sprint-orchestrator execution, leaf refusal, multi-operation status projection, and interrupted publication recovery. | L75-L188; L191-L225; L228-L265; L268-L314; L317-L403 | `mcp/tests/test_lifecycle_operation_dispositions_l2.py` |
| `completed_disposition_authorized` is imported directly and asserts standalone-owner and sprint-orchestrator authorization plus leaf-worker denial before the corresponding public control paths are exercised. | L10-L12; L84-L85; L198-L199; L235-L265 | `mcp/tests/test_lifecycle_operation_dispositions_l2.py` |
| A disposition interrupted before contract publication remains recoverable through the returned public control arguments; a cut after the write is observed as successful, and both paths end with proven durable publication. | L317-L403 | `mcp/tests/test_lifecycle_operation_dispositions_l2.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this test file.

## Update History

- 2026-08-23T17:03+02:00 — 260821-CLIVE-L2: reconciled the reviewed post-clearance
  authorization assertions and direct production-helper import; verification fields remain
  closeout-owned.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
