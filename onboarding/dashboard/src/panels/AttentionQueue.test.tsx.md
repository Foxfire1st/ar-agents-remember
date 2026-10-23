# dashboard/src/panels/AttentionQueue.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Attention bell/layer assertions cover provider-down, actionable-drift, failed-setup and blocked-start. Dismissible rows post itemId/kind; lifecycle/gate joins stay retired, and dismissibility is a served field again — the three action kinds carry none.

## Code Commentary

### Logic

Explicit served queues drive blocked-start cause/severity without joins or opener. A dismissible kind dismisses optimistically, and Clear all includes only dismissible rows: an action row sends nothing and stays visible whatever was sent for its id. Failed writes restore affected rows with an alert; successful retry clears it. Empty/count/urgency, server order, Dialog and non-dismissing Escape/outside close remain. Cleanup resets DOM/store/mocks.

### Invariants And Boundaries

Seeded render and mocked writes do not prove server persistence. Severity rendering remains generic; dismissal follows the served `dismissible` flag rather than an absent lifecycleId, so a live cause is not dismissible. Layer close is not dismissal.

## Evidence

### Repo-Internal References


- The panel under test (generic severity-keyed rendering). [1]

- The reducer source of the `blocked-start` item (§9). [2]

- The store `applySnapshot` path used by this fixture's projection seed. [3]


- The seeded queue includes operational rows, a taskless permission action, a stalled-task action and a landed notice. Mocked component cases exercise exact dismissal payloads, optimistic hide and failed-write retry, mixed and all-action clearing, non-dismissible suppression exclusion, and exact task or taskless-agent opening controls; these are source-level component assertions, not backend or live acceptance. [4]


- Clear all optimistically removes every listed provider-down, actionable-drift, failed-setup and blocked-start item, and sends each exact itemId/kind pair. The mixed-result case restores only the failed provider-down row and reports that dismissal did not hold; worktree-lane setup/start failures are included, not skipped. [5]
