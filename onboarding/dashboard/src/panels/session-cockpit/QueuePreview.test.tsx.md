# dashboard/src/panels/session-cockpit/QueuePreview.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/QueuePreview.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T10:30+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in `system/sources.md`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixtures — `identity`, `capabilities`, `page`, `queued`, `seed` — that build interrupt-capability and working-turn evidence. | `conversationIdentity`, `conversationCapabilities`, `conversationPage`, `queued`, `seed` | dashboard/src/panels/session-cockpit/QueuePreview.test.tsx:28-28; dashboard/src/panels/session-cockpit/QueuePreview.test.tsx:39-39; dashboard/src/panels/session-cockpit/QueuePreview.test.tsx:61-61; dashboard/src/panels/session-cockpit/QueuePreview.test.tsx:68-77; dashboard/src/panels/session-cockpit/QueuePreview.test.tsx:81-83 |
| The component gates its interrupt-capability read on a defined session id. | `interruptCapability` | dashboard/src/panels/session-cockpit/QueuePreview.tsx:100-104 |
| Implementation under test (`QueuePreview`). | `QueuePreview` | dashboard/src/panels/session-cockpit/QueuePreview.tsx:91-146 |
| `conversationCapabilities` / `featureCapability` — the full 23-leaf tree these fixtures now override three leaves of. | `conversationCapabilities`, `featureCapability` | dashboard/src/test/fixtures/conversationWire.ts:69-74; dashboard/src/test/fixtures/conversationWire.ts:103-146 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer residual correction: bound the interrupt-capability selector,
  read, and gate to the complete component expression through the scoped fixer.

- 2026-08-01T10:30+02:00 — 260731-EFA-L4 curator: recorded that the capability/identity/status/page
  fixtures moved to `test/fixtures/conversationWire.ts` and that `capabilities()` is now a three-leaf
  override rather than a hand-listed tree. The described BEHAVIOUR is unchanged, and I checked that
  rather than assuming: the builder bases differ from the deleted local helpers in three visible ways —
  every leaf's `reason` is now `""` instead of `"fixture-probed"`/`"not yet probed"`, `evidenceTier` is
  `"adapter"` instead of `"runtime-fixture"`, and `attachments` carry `["image/png"]`/1024/1 instead of
  `[]`/0/0 — and `grep` over both `QueuePreview.test.tsx` and `QueuePreview.tsx` finds no reader of
  `reason`, `evidenceTier` or any attachment field, so all five cases still gate on
  `controls.interrupt.state`, which every case still sets explicitly. `page.totalItems` and a
  `hydrationId` of `"hy-1"` are likewise unread here. Suite re-run: 5 cases pass. Citation repairs: the
  file shrank to 167 lines, so `L144-L217` was out of bounds → `L94-L167` (the describe), and the
  fixture row `L21-L143` → `L25-L92`, which is where `identity`/`capabilities`/`page`/`queued`/`seed`
  actually end. One row added for the builder module.

- 2026-07-24T13:17:17Z — Curator: created the queue-steer regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
