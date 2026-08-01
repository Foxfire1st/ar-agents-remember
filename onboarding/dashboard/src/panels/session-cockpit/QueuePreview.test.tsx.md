# dashboard/src/panels/session-cockpit/QueuePreview.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/QueuePreview.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T10:30+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fixtures — `identity`, `capabilities`, `page`, `queued`, `seed` — that build interrupt-capability and working-turn evidence. | L25-L92 | [QueuePreview.test.tsx](QueuePreview.test.tsx) |
| The five cases proving visibility gating and the no-withdraw/no-duplicate steer request. | L94-L167 | [QueuePreview.test.tsx](QueuePreview.test.tsx) |
| Implementation under test (`QueuePreview`). | L74-L141 | [QueuePreview.tsx](QueuePreview.tsx) |
| `conversationCapabilities` / `featureCapability` — the full 23-leaf tree these fixtures now override three leaves of. | L69-L153 | [../../test/fixtures/conversationWire.ts](../../test/fixtures/conversationWire.ts) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

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
