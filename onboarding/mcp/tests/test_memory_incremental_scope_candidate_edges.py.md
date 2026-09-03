# mcp/tests/test_memory_incremental_scope_candidate_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_incremental_scope_candidate_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `1ad9d51f743c5b17de51cc46d8b29e004736022d` |
| lastVerifiedCommitDate | 2026-09-02T06:25:51+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Edge coverage for the CCR-R06@v2 candidate observation owner: contract admission refusals,
typed-refusal preservation versus owner-failure wrapping, owner composition, closeout-door
baseline binding and mismatch matrix, and the R01/R02 task-observation refusals
cit:([`test_scope_candidate_requires_one_external_memory_leaf`, `test_scope_candidate_preserves_typed_refusal_and_wraps_owner_failures`, `test_task_pair_refuses_invalid_door_authority`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:137-172, 222-229).

## Code Commentary

### Logic

`test_scope_candidate_requires_one_external_memory_leaf` parameterizes contract mutations and
asserts `candidate-not-external-leaf` / `candidate-memory-root-missing`
cit:([`test_scope_candidate_requires_one_external_memory_leaf`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:137-148).
`test_scope_candidate_preserves_typed_refusal_and_wraps_owner_failures` proves an already-typed
`ScopeUnprovenError` from the pair owner propagates unchanged while an `OSError` is wrapped as
`candidate-owner-unavailable` cit:([`test_scope_candidate_preserves_typed_refusal_and_wraps_owner_failures`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:150-172).
`test_scope_candidate_composes_exact_pair_code_memory_and_task_owners` monkeypatches each canonical
owner and asserts the composed `ScopeCandidateIdentity` carries the exact pair, code/memory
candidate trees, and task pair cit:([`test_scope_candidate_composes_exact_pair_code_memory_and_task_owners`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:175-219).
`test_task_pair_refuses_invalid_door_authority` / `test_task_pair_binds_door_baseline_and_requires_same_current_document`
mutate the door's intent, identity fields, candidate trees, and document ref and assert
`task-base-*` refusals, then prove a valid baseline binds
cit:([`test_task_pair_refuses_invalid_door_authority`, `test_task_pair_binds_door_baseline_and_requires_same_current_document`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:222-283).
A `_FakeTopology` drives `test_current_task_observation_handles_authored_and_legacy_graphs` and the
refusal cases for missing document, missing structural parent, and intent/source drift
cit:([`_FakeTopology`, `test_current_task_observation_refuses_missing_document`, `test_current_task_observation_refuses_owner_intent_and_source_drift`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:284-453).
`test_unclassified_git_status_and_candidate_tree_helper_fail_closed` covers the unclassified Git
status refusal path cit:([`test_unclassified_git_status_and_candidate_tree_helper_fail_closed`], mcp/tests/test_memory_incremental_scope_candidate_edges.py:455-474).

### Conventions

- Every failure asserts `ScopeUnprovenError.failure.code`, keeping the refusal vocabulary typed and
  stable.
- Owner calls are isolated with monkeypatches so each refusal is attributable to one authority.

## Invariants And Boundaries

- A non-external/non-leaf contract and a missing door, intent, topology, document, or parent each
  fail closed before any identity is consumed.
- Unknown Git statuses are refused, never guessed; the scratch-index candidate helper fails closed.
- The suite never mints a private topology or intent identity.

## Docs References

No configured Domain Documentation applies; the refusals follow the CCR-R06@v2 packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| Refusal vocabulary is repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Production candidate observation under test. | `observe_scope_candidate`, `observe_contract_task`, `observe_contract_task_pair`, `_parse_name_status` | mcp/src/agents_remember/memory_quality/incremental_scope/candidate.py:51-296 |
| Companion primary suite for the same surface. | — | mcp/tests/test_memory_incremental_scope_candidate.py |

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 1ad9d51f743c5b17de51cc46d8b29e004736022d (CCR-R06@v2/L26): created the card for the new candidate-observation edge suite of the R06v2 successor leaf; no prior sidecar existed.