# dashboard/src/panels/AttentionQueue.test.tsx

## Governing Overview

[panels/ overview](overview.md)

## Purpose

Attention bell/layer assertions cover the two operational kinds the server still publishes — `actionable-drift` and `blocked-start` — together with the live native causes (a permission wait, a stalled task) and a landed notice. A separate case seeds a payload from an older server that still carries both retired kinds (`provider-down`, `failed-setup`) beside one live item, and asserts that the bell count and the rendered list carry only the live items and that no dismissal request ever names a retired kind. Every served row posts itemId/kind; lifecycle/gate joins stay retired, and dismissibility is no longer a page gate — the action fixtures carry the v1 `dismissible: false` flag precisely so the suite proves the page ignores it.

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



- The seeded queue includes operational rows, a taskless permission action, a stalled-task action and a landed notice. Mocked component cases exercise exact dismissal payloads, optimistic hide, a failed write that restores the row and a retry that clears it, mixed and all-action clearing, the x on a row served with the old non-dismissible flag, and the exact task or taskless-agent opening controls; these are source-level component assertions, not backend or live acceptance. [4]


- Clear all optimistically removes both listed live items and sends exactly two itemId/kind requests. The mixed-result case restores only the failed `blocked-start` row and reports that dismissal did not hold. [5]
