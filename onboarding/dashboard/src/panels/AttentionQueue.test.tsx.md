# dashboard/src/panels/AttentionQueue.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Attention bell/layer assertions cover provider-down, actionable-drift, failed-setup and blocked-start. Every served row posts itemId/kind; lifecycle/gate joins stay retired, and dismissibility is no longer a page gate — the action fixtures carry the v1 `dismissible: false` flag precisely so the suite proves the page ignores it.

## Code Commentary

### Logic

Explicit served queues drive blocked-start cause/severity without joins or opener. Dismissal is optimistic on every kind and Clear all takes the whole queue: an action row posts its own id/kind and hides at once, an all-action queue is cleared, and a locally suppressed action leaves both the layer and the bell. Failed writes restore affected rows with an alert; successful retry clears it. Empty/count/urgency, the served order as issued, Dialog and non-dismissing Escape/outside close remain. Cleanup resets DOM/store/mocks.

### Invariants And Boundaries

Seeded render and mocked writes do not prove server persistence. Severity rendering remains generic; dismissal does not read the served `dismissible` flag at all, so an entry the earlier producer marked non-dismissible is dismissed here too, and dismissibility stays server-owned. Layer close is not dismissal.

## Evidence

### Repo-Internal References


- The panel under test (generic severity-keyed rendering). [1]

- The reducer source of the `blocked-start` item (§9). [2]

- The store `applySnapshot` path used by this fixture's projection seed. [3]


- The seeded queue includes operational rows, a taskless permission action, a stalled-task action and a landed notice. Mocked component cases exercise exact dismissal payloads, optimistic hide and failed-write retry, mixed and all-action clearing, suppression of a served non-dismissible action, and exact task or taskless-agent opening controls; these are source-level component assertions, not backend or live acceptance. [4]


- Clear all optimistically removes every listed provider-down, actionable-drift, failed-setup and blocked-start item, and sends each exact itemId/kind pair. The mixed-result case restores only the failed provider-down row and reports that dismissal did not hold; worktree-lane setup/start failures are included, not skipped. [5]
