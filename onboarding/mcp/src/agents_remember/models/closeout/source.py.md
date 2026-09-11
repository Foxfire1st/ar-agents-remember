# mcp/src/agents_remember/models/closeout/source.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/closeout/source.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Define neutral typed inputs and evidence for closeout-door source publication.

## Code Commentary

### Logic

The module models candidate admission facts, scheduling grade input/output, evidence facts, and route-review facts with strict validation and bounded text.

### Invariants And Boundaries

- False admission facts require explanatory reasons.
- Scheduling priority is typed and separate from lifecycle state.
- Source evidence is input to door/projection derivation, never queue-owned history.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate and scheduling inputs validate readiness and priority explicitly. | `CandidateAdmissionFacts`; `SchedulingGradeInput`; `SchedulingGrade` | mcp/src/agents_remember/models/closeout/source.py:16-56 |
| Evidence and route-review facts are strict bounded source models. | `EvidenceFact`; `RouteReviewFact` | mcp/src/agents_remember/models/closeout/source.py:57-72 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
