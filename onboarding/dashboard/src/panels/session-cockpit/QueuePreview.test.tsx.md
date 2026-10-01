# dashboard/src/panels/session-cockpit/QueuePreview.test.tsx

## Governing Overview

[Session cockpit overview](overview.md)

## Purpose

Pins the queue-head steer affordance and its evidence boundaries.

## Code Commentary

### Logic

The fixture seeds active-conversation identity, capability, and turn state. Tests cover absent or
unsupported evidence, supported working-turn visibility, and the direct interrupt request while
asserting that both queue rows remain present in their original order.

Since 260731-EFA-L4 the capability tree is no longer hand-assembled. The local `cap()`/`attachCap()`
helpers are gone; `capabilities(interruptState)` now names only the three control leaves it cares
about — `interrupt` at the requested state, `steer` and `followUp` `unavailable` — as an override on
`conversationCapabilities()` from `test/fixtures/conversationWire.ts`, which fills the other twenty
leaves. Identity, status and page come from `conversationIdentity` / `conversationStatus` /
`conversationPage` the same way. The point is not brevity: the old tree was hand-listed beside the
wire model, so a leaf the server added was invisible here.

### Conventions

The focused request is observed at the fetch boundary so the test checks the exact bridge epoch,
turn id, and generated request id without duplicating client implementation.

### Invariants And Boundaries

Steer is not queue mutation: it may only interrupt a proved working turn and leaves authority-owned
queued entries untouched.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation entries are configured in `system/sources.md`.

No relevant domain documentation was found.

### Repo-Internal References

- The fixtures — `identity`, `capabilities`, `page`, `queued`, `seed` — that build interrupt-capability and working-turn evidence. [1]
- The component gates its interrupt-capability read on a defined session id. [2]
- Implementation under test (`QueuePreview`). [3]
- `conversationCapabilities` / `featureCapability` — the full 23-leaf tree these fixtures now override three leaves of. [4]

### Cross-Repo References

No cross-repository boundary is owned here.

No cross-repository evidence applies.
