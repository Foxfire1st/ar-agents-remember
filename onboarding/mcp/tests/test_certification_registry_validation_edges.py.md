# mcp/tests/test_certification_registry_validation_edges.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_certification_registry_validation_edges.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T11:33+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Proves typed, exhaustive semantic findings at the certification-registry validation boundary,
including exact budget refusal and profile, member, prerequisite, and artifact edge cases.

## Code Commentary

### Logic

The suite constructs one raw-overflow canonical payload and then varies portable registry profiles,
rail member collections, applicability, prerequisite populations, artifact producers, and
cross-gate artifact flow. Each case asserts the stable finding vocabulary returned by the generic
validator.

### Conventions

The local `_codes` helper projects only typed finding codes. Registry construction remains in the
shared portable support owner and does not introduce a repository profile.

### Invariants And Boundaries

- A registry over the work budget publishes one typed budget finding with the measured count.
- Duplicate profile gates and every selected empty gate remain visible.
- Duplicate rail members retain the exact field path.
- Applicability and prerequisite validity are checked per selected profile.
- Each artifact identity has one producer.
- Gate 3 requires a declared Gate 2 artifact, and an earlier gate cannot consume a later artifact
  or prerequisite.

### Todos

Keep new semantic categories independently falsifiable rather than folding them into aggregate
error prose.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Work-budget refusal, duplicate/empty profile gates, and duplicate member paths publish stable typed findings. | `test_validation_budget_refusal_publishes_one_typed_finding`; `test_profiles_report_duplicate_gates_and_every_empty_gate`; `test_duplicate_rail_members_are_reported_by_field` | mcp/tests/test_certification_registry_validation_edges.py:28-71 |
| Unknown applicability profiles and per-profile prerequisite absence are rejected. | `test_unknown_applicability_profile_refuses_and_skips_profile_iteration`; `test_prerequisite_must_exist_in_every_consumer_profile` | mcp/tests/test_certification_registry_validation_edges.py:74-120 |
| Artifact producer uniqueness and both cross-gate artifact-direction rules are explicit. | `test_artifact_identity_has_exactly_one_producer`; `test_gate_three_without_gate_two_artifact_is_reported`; `test_earlier_gate_cannot_consume_a_later_gate_artifact` | mcp/tests/test_certification_registry_validation_edges.py:123-167 |

## Cross-Repo References

No external repository implementation is consumed.

| Finding | Anchor | Source |
| --- | --- | --- |
| Portable builders name a sample repository and generic profile only. | `certification_registry_test_support` | mcp/tests/test_certification_registry_validation_edges.py:16-21 |

## Update History

- 2026-09-01T11:33+02:00 — Created for CCR-L11 Attempt 10 exhaustive registry-validation edge
  evidence. Verification remains closeout-owned until the source candidate is committed.
