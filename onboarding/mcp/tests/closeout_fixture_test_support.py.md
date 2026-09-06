# mcp/tests/closeout_fixture_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/closeout_fixture_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T14:56:02+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Provides waiting-door, publicly selected-operation, pending-memory, and writer-component fixtures for closeout boundary tests. The separate entry points preserve which authority is real in each scenario: scheduling alone, actual public journal selection, or concrete code/memory/ledger writer behavior.

## Code Commentary

### Logic

`selected_fixture` preserves the small waiting-door fixture for a requested memory mode; it does not claim or start a closeout operation. `_selected_fixture` builds the external-memory world, optionally installs the requested repository profile, stages its code and performs the real review/declaration flow.

`_public_apply` calls the actual configured closeout tool with explicit messages and approval. `_start_selected` intercepts only detached worker launch, requires one queued public result and one launch request, then opens the real store and starts `OperationRuntime`. `_committed_state` captures code/memory HEADs, ledger bytes and contract status for unchanged-state assertions.

`_PendingMemory` accepts only a Gate-5 handoff, optionally invokes the actual memory checker phase, and always returns a pending failure result. Its finalizer raises because this fixture has not accepted Gate 5. `_with_memory_owner` substitutes this downstream boundary on the existing selected executor while preserving the other bound services.

The `_component_code_and_memory` and `_component_ledger` helpers invoke real writer owners using explicit closeout input. Their resulting commits are component-test evidence; they do not establish selected lifecycle completion or Gate-5 acceptance. `running_code_operation` separately builds an internal-memory candidate, reviews/declares it, admits the operation through the existing support owner, and starts the actual runtime/store for worker tests.

### Conventions

Choose the fixture entry point that matches the boundary under test. Scenario-specific mutations remain in callers; this module does not implement production behavior.

### Invariants And Boundaries

- Waiting-door selection alone grants no operation, commit or certification authority.
- Public selected-operation fixtures obtain journal authority through the actual configured apply path; detached launch is the explicit injected boundary.
- Pending memory never reports an accepted Gate 5 or permits finalization, including when it invokes the real checker phase.
- Concrete writer calls exercise component behavior without claiming lifecycle completion or accepted memory semantics.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for these repository-owned test contracts. The retained CLIVE history records the fixture's earlier scheduling-only role.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source governs this helper. | N/A | N/A |

## Repo-Internal References

The separate helpers make scheduling, selected lifecycle admission, pending downstream work and writer-component evidence explicit. Their source boundaries should remain visible in each consuming test.

| Finding | Anchor | Source |
| --- | --- | --- |
| The original fixture remains a waiting-door composition only. | `selected_fixture` | mcp/tests/closeout_fixture_test_support.py:33-36 |
| The external-memory candidate uses actual profile installation, staging and review/declaration. | `_selected_fixture` | mcp/tests/closeout_fixture_test_support.py:39-47 |
| The public tool receives explicit commit messages and closeout approval. | `_public_apply` | mcp/tests/closeout_fixture_test_support.py:50-58 |
| One intercepted launch leads to actual store/runtime startup after queued public admission. | `_start_selected` | mcp/tests/closeout_fixture_test_support.py:61-69 |
| Commit and ledger observations support unchanged-state assertions. | `_committed_state` | mcp/tests/closeout_fixture_test_support.py:72-79 |
| The downstream memory fixture remains pending and rejects finalization. | `_PendingMemory` | mcp/tests/closeout_fixture_test_support.py:82-104 |
| Only the selected executor's continuation service is replaced. | `_with_memory_owner` | mcp/tests/closeout_fixture_test_support.py:107-112 |
| Code and memory commits are produced by actual component writers. | `_component_code_and_memory` | mcp/tests/closeout_fixture_test_support.py:115-126 |
| The ledger component writes the exact supplied code-to-memory mapping. | `_component_ledger` | mcp/tests/closeout_fixture_test_support.py:129-138 |
| Worker fixtures start a real internal-memory operation and runtime. | `running_code_operation` | mcp/tests/closeout_fixture_test_support.py:141-158 |

## Cross-Repo References

No independent cross-repository protocol is established here. Temporary external-memory fixtures exercise the repository's own contract and ledger writers.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository evidence is required. | N/A | N/A |

## Current Contract — 260821 CLIVE Final

The CLIVE waiting-door behavior remains the contract of `selected_fixture`: it derives selection from current door/projection truth rather than a retained queue lifecycle row. The selected-operation and writer helpers now have distinct, broader test roles described above.

### Current Invariants

- `selected_fixture` creates waiting-door source state for the requested memory mode without granting claim, operation, commit or certification authority.
- Helpers that start selected lifecycle work use the canonical admission/store owners; component writer helpers do not claim that authority or accepted Gate-5 execution.
## Update History

- 2026-09-06T14:56:02+00:00 — Bound the reviewed card body and active citations to actual source commit c69d5171187fa1957025e393270db9f5a864ab14 after checking source-byte equality. Preserved prior history; this verifies memory claims and does not assert additional test execution.

- 2026-09-06T14:02:39+00:00 — L33 candidate curation: Separated preserved waiting-door setup from actual public selected operations, pending-memory handoff and component-only writer fixtures; refreshed all source anchors without granting fixture output acceptance authority. Reviewed uncommitted source matching run28; existing verification commit/date remain unchanged. This records source behavior, not test execution or acceptance.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; test verification metadata awaits closeout.
