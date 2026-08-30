# mcp/src/agents_remember/models/lifecycles/curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[lifecycle models overview](overview.md)

## Purpose

Defines the strict structured contracts for curator source candidates, agent-owned judgments,
immutable coherence generations, the sole live authority manifest, optional attempt snapshots, and
the four-action public request/response API.

## Code Commentary

### Logic

`CuratorQualityAttestation` accepts only the exact `ar-curator-memory-quality/v1` schema and checks
candidate count and uniqueness. `CuratorCoherenceRecord` keeps semantic requirement revision,
delivery attempt, and content identities in separate fields and requires the recorded judgment set
to exactly equal the source-candidate set. `CuratorCoherenceRequest` makes publication a strict
compare-and-swap shape while forbidding publication-only fields on status, prepare, and validate.

### Conventions

All authority models are frozen and reject extra fields. Caller judgments omit lifecycle-owned
evidence digests; publication creates the recorded judgment form after reading the cited bytes.

### Invariants And Boundaries

- A requirement revision is not a delivery attempt or an evidence digest.
- Exactly one judgment exists for each `(sourceFile, onboardingFile, classification)` tuple.
- Markdown is not represented as an input model; it is projection output only.
- The stable manifest points to one content-addressed generation.
- Publication requires every expected identity and an authorized declared caller.

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
| Immutable record validation enforces exact candidate-to-judgment coverage. | `CuratorCoherenceRecord` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:106-140 |
| The discriminated action request separates read actions from publication CAS input. | `CuratorCoherenceRequest` | mcp/src/agents_remember/models/lifecycles/curator_coherence.py:166-220 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| These are local MCP and lifecycle records only. | — | — |

## MCAR-L03 Acceptance Identity

Both the source memory-quality attestation and immutable curator-coherence record require
`pairIdentity`. Public coherence responses expose the pair and typed pair-refusal field/repair
arguments. Missing pair data is invalid rather than being read through a compatibility path.

## Update History

- 2026-08-29T21:46+02:00 — MCAR-L03: made the exact pair mandatory acceptance evidence across
  attestation, record, and response models. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for MCAR-L02 A005's strict coherence identity, authority,
  snapshot, action, and response contracts. Verification remains closeout-owned.
