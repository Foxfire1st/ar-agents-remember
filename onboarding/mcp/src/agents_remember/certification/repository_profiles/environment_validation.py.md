# mcp/src/agents_remember/certification/repository_profiles/environment_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/repository_profiles/environment_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:39:50+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Certification contract overview](../overview.md)

## Purpose

Validates declared original producers and later consumers of reconstructed repository environments.

## Code Commentary

### Logic

`_validate_environments` reports duplicate environment IDs, invalid Gate-1 census producers and mismatched manifest publications. The producer must declare the environment artifact; its publication must belong exactly to Gate 1 with the declared byte bound. The reconstruction proof must be published by exactly the consuming gates and use a 4096-byte bound. Consumers must be nonempty, omit Gate 1, and form an ordered unique gate set.

`_validate_environment_artifacts` owns the census-publication and reconstruction-proof checks. `_validate_environments` invokes it before validating the consumer gate set; extracting the helper preserves separate finding codes and accumulation order.

`_validate_selected_producer` examines each selection: when a later environment consumer is applicable, its original Gate-1 producer must also be applicable and explicitly selected. Findings accumulate in the caller’s list.

### Conventions

Use these functions through the aggregate repository-profile validator and preserve the caller’s complete finding list.

### Invariants And Boundaries

- Profile validity establishes declaration coherence; actual reconstruction and proof-byte checking belong to the execution owner.
- Later consumers cannot be admitted without their original selected producer.
- Producer, proof and consumer failures retain separate finding codes.

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
| `_validate_environments` implements the described validation step. | `_validate_environments` | mcp/src/agents_remember/certification/repository_profiles/environment_validation.py:12-32 |
| `_validate_selected_producer` implements the described validation step. | `_validate_selected_producer` | mcp/src/agents_remember/certification/repository_profiles/environment_validation.py:74-90 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T21:39:50+00:00 — Reconciled the landed validation/helper extraction against IAS d3610903; retained ownership and refusal semantics and refreshed same-file evidence ranges. Verification stamps and final acceptance were not advanced.

- 2026-09-06T15:09:25+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented the declaration checks and their exact runtime limits.
