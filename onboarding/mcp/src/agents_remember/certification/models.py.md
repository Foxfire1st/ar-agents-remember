# mcp/src/agents_remember/certification/models.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation could be checked.

### Repo-Internal References

- Closed gate, rail-class and status vocabularies prevent undeclared contract states. [1]
- The shared frozen base and semantic-text validator preserve the original wire constraints. [2]
- Rail definitions bind identity, ownership, authority, prerequisites, adapters, evidence, and artifacts. [3]
- Deterministic same-gate dependencies compile into canonical execution waves. [4]
- Gate and certification plans validate complete catalogs, waves, identities, and digests. [5]
- Result models enforce legal status payloads, unique members, exact identities, and manifest disposition. [6]
- `CandidateIdentity` carries a validated kind and nonblank value; exact Git-tree restrictions are imposed by certificate owners. [7]
- Full planned catalog comparison is owned by result publication. [8]

### Cross-Repo References

No cross-repository implementation boundary is owned here. Candidate identity is repository-neutral; concrete rail inventory remains repository-profile data.

No cross-repository implementation is referenced.
