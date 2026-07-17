# dashboard/src/test/fixtures/busScenarios.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/test/fixtures/busScenarios.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `882fed5806d5698f05c700e39ccae5da53c29176` |
| lastVerifiedCommitDate | 2026-07-18T00:12:18+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

Provides coherent FEUI-L7 pickup and heartbeat fixtures shared by inspector tests, including
sender-address variants and a persisted legacy row that lacks additive owner/redelivery fields.

## Code Commentary

### Logic

- The decision fixture carries a full sender pair, target, owner, gate/artifact, attempts, and age.
- Separate sender-agent-only, sender-role-only, and lifecycle-only rows pin reverse-address rules.
- Escalated and legacy rows cover retry/escalation facts and backward-compatible absence; the
  heartbeat fixture supplies liveness and backlog counts.

### Invariants And Boundaries

- Fixtures use `satisfies` so they remain type-checked without widening away deliberate absences.
- Legacy absence is intentional and must not be filled by test helpers or consumers.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Full decision and sender-address variants. | L7-L67 | [busScenarios.ts](busScenarios.ts) |
| Escalation, legacy absence, combined rows, and heartbeat. | L69-L117 | [busScenarios.ts](busScenarios.ts) |
| Projection types the fixtures satisfy. | L220-L450 | [../../types/projection.ts](../../types/projection.ts) |
| Primary Bus regression consumer. | L1-L338 | [../../panels/session-cockpit/BusPane.test.tsx](../../panels/session-cockpit/BusPane.test.tsx) |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
