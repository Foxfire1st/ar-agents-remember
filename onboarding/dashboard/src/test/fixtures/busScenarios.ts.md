# dashboard/src/test/fixtures/busScenarios.ts

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

## Evidence

### Docs References

No Domain Documentation source is configured.

No external domain citation applies.

### Repo-Internal References

- Full decision and sender-address variants. [1]
- Escalation, legacy absence, combined rows, and heartbeat. [2]
- The six pickup fixtures satisfy the generated `AgentPickupNode` projection shape. [3]
- The agent-notifier heartbeat fixture satisfies the generated `AgentNotifierHeartbeat` projection shape. [4]
- The primary Bus regression consumer covers sender-to-owner, redelivery, escalation, heartbeat, and UA-3 limits. [5]

### Cross-Repo References

No meaningful cross-repo boundary is owned here.

No cross-repo evidence applies.
