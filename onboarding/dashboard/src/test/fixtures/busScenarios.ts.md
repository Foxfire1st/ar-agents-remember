# dashboard/src/test/fixtures/busScenarios.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/test/fixtures/busScenarios.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T23:54+02:00 |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af` |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain citation applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Full decision and sender-address variants. | `L7_DECISION_PICKUP`; `L7_SENDER_AGENT_ONLY_PICKUP`; `L7_SENDER_ROLE_ONLY_PICKUP`; `L7_LIFECYCLE_ONLY_PICKUP` | dashboard/src/test/fixtures/busScenarios.ts:8-30; dashboard/src/test/fixtures/busScenarios.ts:32-46; dashboard/src/test/fixtures/busScenarios.ts:48-59; dashboard/src/test/fixtures/busScenarios.ts:61-71 |
| Escalation, legacy absence, combined rows, and heartbeat. | `L7_ESCALATED_PICKUP`; `L7_LEGACY_PICKUP`; `L7_PICKUPS`; `L7_AGENT_NOTIFIER_HEARTBEAT` | dashboard/src/test/fixtures/busScenarios.ts:73-92; dashboard/src/test/fixtures/busScenarios.ts:95-106; dashboard/src/test/fixtures/busScenarios.ts:108-112; dashboard/src/test/fixtures/busScenarios.ts:114-122 |
| The six pickup fixtures satisfy the generated `AgentPickupNode` projection shape. | `L7_DECISION_PICKUP`; `L7_SENDER_AGENT_ONLY_PICKUP`; `L7_SENDER_ROLE_ONLY_PICKUP`; `L7_LIFECYCLE_ONLY_PICKUP`; `L7_ESCALATED_PICKUP`; `L7_LEGACY_PICKUP` | dashboard/src/test/fixtures/busScenarios.ts:8-30; dashboard/src/test/fixtures/busScenarios.ts:32-46; dashboard/src/test/fixtures/busScenarios.ts:48-59; dashboard/src/test/fixtures/busScenarios.ts:61-71; dashboard/src/test/fixtures/busScenarios.ts:73-92; dashboard/src/test/fixtures/busScenarios.ts:95-106 |
| The agent-notifier heartbeat fixture satisfies the generated `AgentNotifierHeartbeat` projection shape. | `L7_AGENT_NOTIFIER_HEARTBEAT` | dashboard/src/test/fixtures/busScenarios.ts:114-122 |
| The primary Bus regression consumer covers sender-to-owner, redelivery, escalation, heartbeat, and UA-3 limits. | "defaults fleet-global and renders sender-to-owner, redelivery, escalation, heartbeat, and UA-3 limits" | dashboard/src/panels/session-cockpit/BusPane.test.tsx:50-77 |

## Cross-Repo References

No meaningful cross-repo boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo evidence applies. | — | — |

## Update History
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: bound each fixture-shape claim to its concrete satisfies expression under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-07-17T23:54+02:00 — Created for 260715-FEUI-L7 after Round 3 reviewer PASS. Verification
  metadata remains pinned to the leaf base until closeout.
