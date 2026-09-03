# mcp/tests/test_evidence_dependencies.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_evidence_dependencies.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

The focused dependency-mutation, cycle, and currentness matrix for CCR-R03@v1: proves every
evidence record type owns exactly one versioned policy, declarations are canonical and
fingerprint-stable, missing/extra/wrong-type/duplicate dependencies fail closed, record closures
refuse cycles without scanning for historical files, and each domain seam (route review, door,
curator coherence, operation, memory-quality controller) refuses missing or stale declared inputs
cit:(["Direct-input evidence declarations remain typed, bounded, and acyclic."], mcp/tests/test_evidence_dependencies.py:1).

## Code Commentary

### Logic

`test_every_record_type_has_one_versioned_policy` pins the policy registry to the closed
`EvidenceRecordType` literal cit:([`test_every_record_type_has_one_versioned_policy`], mcp/tests/test_evidence_dependencies.py:88-90).
`test_builder_canonicalizes_edges_and_fingerprint_uses_only_declared_inputs` proves canonical order
and that the fingerprint ignores unrelated publication time
cit:([`test_builder_canonicalizes_edges_and_fingerprint_uses_only_declared_inputs`], mcp/tests/test_evidence_dependencies.py:92-100).
`test_memory_quality_attestation_binds_pair_trees_report_and_checker` proves the attestation
declaration round-trips through `require_memory_quality_attestation_dependencies` and stales on a
changed code tree cit:([`test_memory_quality_attestation_binds_pair_trees_report_and_checker`], mcp/tests/test_evidence_dependencies.py:102-157).
`test_missing_extra_wrong_type_and_duplicate_dependencies_fail_closed` forces each typed refusal
status (`evidence-dependencies-missing`, `-required-missing`, `-undeclared-extra`,
`-record-type-mismatch`, duplicate-identity validation) cit:([`test_missing_extra_wrong_type_and_duplicate_dependencies_fail_closed`], mcp/tests/test_evidence_dependencies.py:159-187).
`test_supplied_record_closure_refuses_cycles_without_scanning_for_external_roots` proves a
self-referencing door declaration fails the graph validator while an external root and shared
consumer stay valid — no historical file search cit:([`test_supplied_record_closure_refuses_cycles_without_scanning_for_external_roots`], mcp/tests/test_evidence_dependencies.py:202-242).
`test_door_and_operation_dependencies_refuse_missing_or_stale_inputs` forces
`closeout-door-dependencies-stale`, `lifecycle-operation-candidate-dependencies-missing`,
`-door-dependency-missing`, and `-dependencies-stale`
cit:([`test_door_and_operation_dependencies_refuse_missing_or_stale_inputs`], mcp/tests/test_evidence_dependencies.py:244-297).
`test_route_review_dependency_and_content_addressing_guards` drives
`route-review-task-intent-missing`, `evidence-dependencies-missing`,
`route-review-dependencies-stale`, and the record self-digest/partial-shape refusals
cit:([`test_route_review_dependency_and_content_addressing_guards`], mcp/tests/test_evidence_dependencies.py:299-355).
`test_curator_dependency_currentness_and_attestation_refusal` and
`test_door_transition_projects_dependency_refusal` force the coherence and door-source refusal
projections, while `test_memory_quality_candidate_guards_are_exact` forces the controller's
candidate-tree guards (`memory-quality-candidate-changed`) cit:([`test_curator_dependency_currentness_and_attestation_refusal`, `test_door_transition_projects_dependency_refusal`, `test_memory_quality_candidate_guards_are_exact`], mcp/tests/test_evidence_dependencies.py:357-412; mcp/tests/test_evidence_dependencies.py:414-468).

### Conventions

- Shared fixtures (`_route_review`, `_door`) build policy-valid declarations so each case isolates
  one refusal.
- Production helpers (`require_evidence_dependencies`, `validate_evidence_dependency_graph`,
  `build_evidence_dependencies`) are exercised directly, never reimplemented in the test.
- The suite is registered as a unit-regression lane in `test-evidence-lanes.toml` and as a consumer
  of `evidence-lifecycle.toml` for the touched production modules.

## Invariants And Boundaries

- Policy registry exactly equals the closed record-type literal at all times.
- Missing, extra, wrong-type, duplicate, or cyclic dependencies refuse; external roots are legal.
- Digest shape (`git-object` 40-hex, `sha256` 64-hex) and canonical ordering are structural
  contracts.
- Every domain currentness seam refuses stale declarations; unchanged upstream semantics do not
  stale unrelated evidence.

## Docs References

No configured Domain Documentation applies; the matrix follows the CCR-R03@v1 packet.

| Finding | Anchor | Source |
| --- | --- | --- |
| The mutation matrix is repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The dependency encoding under test. | `EvidenceDependencies`, `EvidenceDependencyPolicy`, `build_evidence_dependencies`, `require_evidence_dependencies`, `validate_evidence_dependency_graph` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:99-119; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:122-213; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:228-324 |
| The attestation, door, operation, and route-review binders under test. | `memory_quality_attestation_dependencies`; `closeout_door_dependencies`; `lifecycle_operation_dependencies`; `build_route_review` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:91-129; mcp/src/agents_remember/models/lifecycles/door.py:161-202; mcp/src/agents_remember/models/lifecycles/operation.py:428-484; mcp/src/agents_remember/worktrees/route_review.py:56-116 |
| The controller candidate guards under test. | `_curator_candidate_inputs`; `_require_same_curator_candidate` | mcp/src/agents_remember/application/memory_quality/controller.py:433-479 |
| Companion coverage for the route-review record shape. | `test_route_review_dependency_and_content_addressing_guards` | mcp/tests/test_evidence_dependencies.py:299-354 |

## Update History

- 2026-09-03T13:30+02:00 - 260831-CCR-L27 Gate-5 memory pass: repaired citation
  rows -- module-docstring prose quote anchored to the docstring literal, route-review
  row re-pointed to the file that actually carries the anchor, and comma-separated
  source cells split into ';'-separated path:start-end citations.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): created the card for the new evidence-dependency mutation/cycle/currentness matrix of the R03 leaf; no prior sidecar existed.