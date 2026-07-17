# dashboard/src/data/setClient.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/setClient.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T08:33+02:00 |
| lastVerifiedCommitHash | `4293c53b9d6ef2bf0fee7aca11c2677322c4e786` |
| lastVerifiedCommitDate | 2026-07-17T10:26:02+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

End-to-end unit contract for the set-control I/O driver and its store-visible honesty semantics.

## Code Commentary

### Logic

Exercises exact wire routes and bodies; all acceptance outcomes; clamp, unknown, unsupported, and
route-error state; superseded responses; focused announcements; snapshot classification and
single-flight; queued/unknown promotion; serialized pair success, refusal, and route termination;
effort cycling; and turn/focus watcher triggers.

### Conventions

Fetch is mocked at the boundary while the real reducers and store are used, so assertions cover
the state that UI consumers actually receive.

### Invariants And Boundaries

Tests distinguish requested, pending, echo-evidenced effective, and readback-confirmed values.
They also prove that pair effort cannot POST before model evidence and that route failures cannot
fabricate effectiveness.

### Todos

The final reviewer PASS retains the production sev-4 observations recorded in `setClient.ts.md`;
they are not release blockers for this leaf.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Set, snapshot, promotion, pair, cycling, and watcher cases. | L63-L694 | [setClient.test.ts](setClient.test.ts) |
| Driver under test. | L1-L433 | [setClient.ts](setClient.ts) |
| Shared deterministic fixtures. | — | [../test/fixtures/capabilityEnvelopes.ts](../test/fixtures/capabilityEnvelopes.ts) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T08:33+02:00 — Created for the 260715-FEUI-L4 R1–R8 regression matrix after
  fix round 3 and final reviewer PASS. Base verification metadata is temporary until code commit.
