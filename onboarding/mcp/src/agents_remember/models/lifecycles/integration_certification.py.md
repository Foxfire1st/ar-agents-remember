# mcp/src/agents_remember/models/lifecycles/integration_certification.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/integration_certification.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:06:50+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing lifecycle overview](overview.md)

## Purpose

Binds full integration certification to its original operation-selected execution identity and preserves its original terminal attempts.

## Code Commentary

### Logic

`IntegrationCertificationSelection` binds operation key/generation, integration-authority digest, original frozen-run reference, profile, diff base, memory cap and optional completion fingerprint. Its mode is exactly `full`. Current terminals form the exact Gate-1-through-N code prefix; a later gate cannot follow an uncertified earlier terminal. Integration keeps original terminals within its own generation, so predecessor reuse references are refused in both current and historical entries. History contains only unique uncertified attempts.

`validate_integration_completion_identity` compares the proposed fingerprint, attested diff base and serialized memory cap with the original selection. `validate_integration_certification_transition` allows an unchanged no-op; a changed selection requires the live exact operation/generation and immutable execution authority. Terminals may append an exact suffix, or replace the last uncertified terminal at the same gate while appending that original to history.

### Conventions

The operation owner supplies actual authority and currentness. This file validates the selected shape and transition; the integration composition separately verifies completion output commits and original certificate bytes.

### Invariants And Boundaries

- Full mode is an immutable selected value, not proof that a full suite ran.
- Completion comparison uses the original fingerprint/base/cap, not a later candidate tree.
- Changing profile, base, cap, fingerprint or frozen authority in an existing selection is refused.
- Replacing an interrupted terminal must retain its exact original evidence; certified predecessors cannot be replaced.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-owned contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `IntegrationCertificationSelection` owns the described value or transition boundary. | `IntegrationCertificationSelection` | mcp/src/agents_remember/models/lifecycles/integration_certification.py:15-46 |
| `validate_integration_completion_identity` owns the described value or transition boundary. | `validate_integration_completion_identity` | mcp/src/agents_remember/models/lifecycles/integration_certification.py:49-68 |
| `validate_integration_certification_transition` owns the described value or transition boundary. | `validate_integration_certification_transition` | mcp/src/agents_remember/models/lifecycles/integration_certification.py:71-105 |

## Cross-Repo References

No cross-repository implementation boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T15:06:50+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented exact selection, refusal and transition ownership. Source verification does not assert runtime execution or CCR acceptance.
