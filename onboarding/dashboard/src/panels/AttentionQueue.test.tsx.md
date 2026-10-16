# dashboard/src/panels/AttentionQueue.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Attention bell/layer assertions cover provider-down, actionable-drift, failed-setup and blocked-start. All dismiss by itemId/kind; lifecycle/gate joins and restricted dismissibility are retired.

## Code Commentary

### Logic

Explicit served queues drive blocked-start cause/severity without joins or opener. Every kind dismisses optimistically; Clear all includes all. Failed writes restore affected rows with an alert; successful retry clears it. Empty/count/urgency, server order, Dialog and non-dismissing Escape/outside close remain. Cleanup resets DOM/store/mocks.

### Invariants And Boundaries

Seeded render and mocked writes do not prove server persistence. Severity rendering remains generic; every remaining kind is dismissible regardless of absent lifecycleId. Layer close is not dismissal.

## Evidence

### Repo-Internal References


- The panel under test (generic severity-keyed rendering). [1]

- The reducer source of the `blocked-start` item (§9). [2]

- The store `applySnapshot` path used by this fixture's projection seed. [3]


- The four-kind fixture covers provider-down, actionable-drift, failed-setup and blocked-start. Parameterized dismissal asserts immediate optimistic hiding and a request containing exactly itemId/kind for each kind; the actionable-drift failure case restores the row, reports that dismissal did not hold and clears the alert on a successful retry. No nullable lifecycle target is posted. [4]


- Clear all optimistically removes every listed provider-down, actionable-drift, failed-setup and blocked-start item, and sends each exact itemId/kind pair. The mixed-result case restores only the failed provider-down row and reports that dismissal did not hold; worktree-lane setup/start failures are included, not skipped. [5]
