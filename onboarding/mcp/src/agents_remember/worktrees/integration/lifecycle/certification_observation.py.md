# mcp/src/agents_remember/worktrees/integration/lifecycle/certification_observation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/certification_observation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:12:42+00:00 |
| lastVerifiedCommitHash | c69d5171187fa1957025e393270db9f5a864ab14 |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing integration overview](overview.md)

## Purpose

Takes the exact current lifecycle journal observation after immutable evidence readback, allowing only concurrent heartbeat fields to differ.

## Code Commentary

### Logic

`observe_certification_publication` reads the current record and compares it with the evidence-verified record after normalizing only `recordRevision`, `heartbeatAt` and `currentCommand` for comparison. A missing record or any other changed field raises a typed certification contract refusal with expected/observed operation key, generation and revision and zero declared gate starts. The actual current record, including its current revision, is returned for the caller’s strict CAS.

### Conventions

The caller verifies evidence first, invokes this read immediately before publication, and uses the returned complete record for one CAS. A lost CAS is a refusal, not an instruction to retry.

### Invariants And Boundaries

- Cancellation, selection, intent, generation and authority changes are not heartbeat differences.
- The helper performs no mutation and does not itself publish a certificate or acquire worker authority.
- Revision/heartbeat write legality remains the journal owner’s responsibility; this comparison does not infer semantic currentness from a revision number alone.

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
| `observe_certification_publication` owns the described selection or observation boundary. | `observe_certification_publication` | mcp/src/agents_remember/worktrees/integration/lifecycle/certification_observation.py:12-51 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | N/A | N/A |

## Update History

- 2026-09-06T15:12:42+00:00 — Created from actual source at c69d5171187fa1957025e393270db9f5a864ab14; documented original evidence, current owner checks and selection/completion boundaries. Source verification does not claim suite execution or CCR acceptance.
