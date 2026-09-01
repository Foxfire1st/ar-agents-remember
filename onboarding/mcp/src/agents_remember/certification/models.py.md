# mcp/src/agents_remember/certification/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-01T03:11+02:00 |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`|
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Certification overview](overview.md)

## Purpose

Defines the closed, immutable vocabulary and data contracts for a repository-neutral five-gate
rail registry, its candidate-bound compiled plans, and complete typed terminal results.

## Code Commentary

### Logic

Strict frozen Pydantic models encode candidates, versioned rail identity, adapters, runtime input,
applicability, evidence, artifacts, profiles, registries, validation findings, compiled rails,
gate/certification plans, observations, rail results, and gate manifests. Model validators enforce
semantic text, digest self-consistency, complete gate catalogs, deterministic dependency waves,
unique result members, and status-specific payload shape.

### Conventions

The gate ids and rail classes are closed literals. Gate ordering is a barrier sequence; same-gate
dependencies are compiled into deterministic waves. Exact identity and digest fields are part of
the contract rather than incidental telemetry.

### Invariants And Boundaries

- Certifying profiles contain all five gates; diagnostic profiles may narrow only under explicit
  validation rules.
- Gates 1–4 use repository-profile authority; Gate 5 is memory-domain authority.
- Contract text is nonblank and unpadded; models are frozen and reject extra fields.
- Every plan is bound to the same registry digest, profile, and exact candidate identity.
- A gate result manifest names the full planned rail catalog and cannot omit failures or siblings.
- `pass`, `fail`, `blocked`, and `not-applicable` each carry only their legal evidence fields.

### Todos

Concrete repositories supply profiles and adapters outside these generic contracts.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closed gate, profile, authority, class, posture, and status vocabularies prevent undeclared contract states. | `GateId`; `RailClass`; `RailStatus` | mcp/src/agents_remember/certification/models.py:13-24 |
| Frozen strict models and semantic-text validation prohibit mutation, extras, blanks, and padded identifiers. | `FrozenContractModel`; `SemanticText` | mcp/src/agents_remember/certification/models.py:36-49 |
| Rail definitions bind identity, ownership, authority, prerequisites, adapters, evidence, and artifacts. | `RailDefinition` | mcp/src/agents_remember/certification/models.py:116-137 |
| Deterministic same-gate dependencies compile into canonical execution waves. | `canonical_execution_waves` | mcp/src/agents_remember/certification/models.py:210-270 |
| Gate and certification plans validate complete catalogs, waves, identities, and digests. | `GatePlan`; `CertificationPlan` | mcp/src/agents_remember/certification/models.py:273-370 |
| Result models enforce legal status payloads, unique members, exact identities, and manifest disposition. | `RailResult`; `GateResultManifest` | mcp/src/agents_remember/certification/models.py:373-501 |

## Cross-Repo References

No Agents Remember rail inventory appears in these models.

| Finding | Anchor | Source |
| --- | --- | --- |
| `CandidateIdentity` accepts an explicit repository and digest algorithm/value. | `CandidateIdentity` | mcp/src/agents_remember/certification/models.py:52-56 |

## Update History

- 2026-09-01T03:11+02:00 — Created for the immutable five-gate registry, plan, and result model
  vocabulary. Verification remains closeout-owned until the source candidate is committed.
