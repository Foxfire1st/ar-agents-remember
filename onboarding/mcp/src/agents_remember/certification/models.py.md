# mcp/src/agents_remember/certification/models.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/certification/models.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:02:26+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
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

The shared frozen base, gate/rail identity and semantic-text values now come from
`models/certification/base.py`; their model-layer home preserves the original constraints.

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
- The gate manifest validates its internal identities, digest and enforcing disposition. The result-publication owner compares it with the complete planned rail catalog and rejects omitted, unplanned or duplicate results.
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
| Closed gate, rail-class and status vocabularies prevent undeclared contract states. | `GateId`; `RailClass`; `RailStatus` | mcp/src/agents_remember/models/certification/base.py:9-9; mcp/src/agents_remember/certification/models.py:22-28; mcp/src/agents_remember/certification/models.py:30-30 |
| The shared frozen base and semantic-text validator preserve the original wire constraints. | `FrozenContractModel`; `_require_semantic_text`; `SemanticText` | mcp/src/agents_remember/models/certification/base.py:30-33; mcp/src/agents_remember/models/certification/base.py:21-24; mcp/src/agents_remember/models/certification/base.py:27-27 |
| Rail definitions bind identity, ownership, authority, prerequisites, adapters, evidence, and artifacts. | `RailDefinition` | mcp/src/agents_remember/certification/models.py:93-114 |
| Deterministic same-gate dependencies compile into canonical execution waves. | `canonical_execution_waves` | mcp/src/agents_remember/certification/models.py:187-209 |
| Gate and certification plans validate complete catalogs, waves, identities, and digests. | `GatePlan`; `CertificationPlan` | mcp/src/agents_remember/certification/models.py:250-269; mcp/src/agents_remember/certification/models.py:303-319 |
| Result models enforce legal status payloads, unique members, exact identities, and manifest disposition. | `RailResult`; `GateResultManifest` | mcp/src/agents_remember/certification/models.py:386-410; mcp/src/agents_remember/certification/models.py:434-456 |
| `CandidateIdentity` carries a validated kind and nonblank value; exact Git-tree restrictions are imposed by certificate owners. | `CandidateIdentity` | mcp/src/agents_remember/certification/models.py:38-42 |
| Full planned catalog comparison is owned by result publication. | `_validate_result_catalog` | mcp/src/agents_remember/certification/results.py:149-180 |

## Cross-Repo References

No cross-repository implementation boundary is owned here. Candidate identity is repository-neutral; concrete rail inventory remains repository-profile data.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository implementation is referenced. | N/A | N/A |

## Update History

- 2026-09-06T15:02:26+00:00 — Reviewed the complete card and current source at c69d5171187fa1957025e393270db9f5a864ab14; corrected identity/observation ownership claims, retained the moved model semantics, and regenerated each active source range from its unique current construct. All prior history is preserved.

- 2026-09-06T14:48:58+00:00 — Repaired the shared primitive ownership references against `c69d5171187fa1957025e393270db9f5a864ab14`; broader domain-plan/result commentary remains assigned to its source-card review. Prior verification stamps and all earlier history are preserved.


- 2026-09-01T03:11+02:00 — Created for the immutable five-gate registry, plan, and result model
  vocabulary. Verification remains closeout-owned until the source candidate is committed.
