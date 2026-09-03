# mcp/src/agents_remember/models/lifecycles/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

Defines the strict structured contracts for curator source candidates, agent-owned judgments,
immutable coherence generations, the sole live authority manifest, optional attempt snapshots, and
the four-action public request/response API. Under CCR-R03@v1 the memory-quality attestation and
immutable coherence record additionally carry a typed direct-dependency declaration so evidence is
a content-addressed consumer of exactly its declared inputs
cit:([`CuratorQualityAttestation`, `CuratorCoherenceRecord`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:62-89; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:186-230).

## Code Commentary

### Logic

`CuratorQualityAttestation` accepts only the exact `ar-curator-memory-quality/v1` schema and checks
candidate count and uniqueness. `CuratorCoherenceRecord` keeps semantic requirement revision,
delivery attempt, and content identities in separate fields and requires the recorded judgment set
to exactly equal the source-candidate set. `CuratorCoherenceRequest` makes publication a strict
compare-and-swap shape while forbidding publication-only fields on status, prepare, and validate.

R03 binds the attestation's rendered report and inspected pair to a declared dependency
population: `memory_quality_attestation_dependencies` declares the candidate-state (pair contract
digest), exact code and memory candidate trees (git-object digests), the rendered-checklist bytes,
and both validator identities; `require_memory_quality_attestation_dependencies` rebuilds that
expected set from the attestation's current source facts and refuses
`memory-quality-attestation-dependencies-stale` on any mismatch
cit:([`memory_quality_attestation_dependencies`, `require_memory_quality_attestation_dependencies`], mcp/src/agents_remember/models/lifecycles/curator_coherence.py:91-130; mcp/src/agents_remember/models/lifecycles/curator_coherence.py:131-156).

### Conventions

All authority models are frozen and reject extra fields. Caller judgments omit lifecycle-owned
evidence digests; publication creates the recorded judgment form after reading the cited bytes.
Dependency declarations are built from the same canonical edge encoding shared by every record
type, never hand-written per domain.

### Invariants And Boundaries

- A requirement revision is not a delivery attempt or an evidence digest.
- Exactly one judgment exists for each `(sourceFile, onboardingFile, classification)` tuple.
- Markdown is not represented as an input model; it is projection output only.
- The stable manifest points to one content-addressed generation.
- Publication requires every expected identity and an authorized declared caller.
- The attestation binds the exact code/memory candidate trees it inspected; a changed tree stales
  the evidence, and no filename, mtime, or marker substitutes for the typed digest edges.

### Todos

None recorded.

## Docs References

No configured external documentation applies; the schemas are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle schema has no external authority. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The quality attestation validates exact candidate count and uniqueness. | `CuratorQualityAttestation` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:50-74 |
| Immutable record validation enforces exact candidate-to-judgment coverage. | `CuratorCoherenceRecord` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:186-232 |
| The discriminated action request separates read actions from publication CAS input. | `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:256-314 |
| The R03 dependency vocabulary used by this record type. | `EvidenceDependencies`, `dependency`, `require_evidence_dependencies` | mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:99-122; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:216-227; mcp/src/agents_remember/models/lifecycles/evidence_dependencies.py:240-277 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| These are local MCP and lifecycle records only. | — | — |

## MCAR-L03 Acceptance Identity

Both the source memory-quality attestation and immutable curator-coherence record require
`pairIdentity`. Public coherence responses expose the pair and typed pair-refusal field/repair
arguments. Missing pair data is invalid rather than being read through a compatibility path.

## 260831-CCR-R03 Declared Attestation Dependencies

The source attestation now carries `dependencies`; the coherence observer and publication owner
recompute the exact dependency set from the candidate pair, code/memory candidate trees, and
rendered-checklist digest at currentness time, so the memory-quality evidence cannot be rebound to
another candidate or report (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the typed direct-dependency declarations on the memory-quality attestation and coherence record, plus the new attestation dependency builders/currentness guards; prior pair-identity and judgment-set prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: made the exact pair mandatory acceptance evidence across
  attestation, record, and response models. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for MCAR-L02 A005's strict coherence identity, authority,
  snapshot, action, and response contracts. Verification remains closeout-owned.