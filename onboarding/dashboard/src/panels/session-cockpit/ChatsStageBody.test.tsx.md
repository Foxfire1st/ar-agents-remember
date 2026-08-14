# dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T10:55+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Session cockpit overview](overview.md)

## 260731-EFA-L8 Change

The suite gained the keep-alive assertions (B1: harness↔terminal keeps the PTY
stack alive through focus handoff) as part of the e2e-driven repair; existing
assertions are unchanged.

## Purpose

Exercises the structured-stage orchestration seams: bridge readiness, per-session mounted surfaces,
epoch attribution, freshness, and the interaction between view switches and scroll geometry.

## Code Commentary

### Logic

The suite mocks only the authority and conversation network edges while retaining the real stores.
It seeds warm projection pages, drives focused-session changes, and proves transient boot retries,
fail-loud bounds, LRU pool eviction, stale-epoch isolation, and view-switch restoration behavior.

The warm pages it seeds are now built by `conversationIdentity` / `conversationItem` /
`conversationStatus` / `conversationPage` (`test/fixtures/conversationWire.ts`) rather than cast
literals — 260731-EFA-L4. The seeded page is therefore materially more complete than it used to be,
and it is worth knowing which parts: the status previously carried only `revision` / `process.state` /
`turn` and now carries `identity`, `observedAt`, `freshness`, `evidence` and `process.generation`;
`capabilities` was an explicit `undefined` on a required field and is now the full 23-leaf tree;
`page.totalItems` is set; and each item carries a `turnId`. Note that "freshness" here and the M9
**authority** freshness case are unrelated facts — M9 is about the submission-authority cache having
no TTL, not about `ConversationStatus.freshness`.

### Conventions

Tests use explicit fake-timer windows and mock projection data rather than a live bridge. The PTY and
ambient telemetry are substituted only where their rendering is irrelevant to the stage contract.

### Invariants And Boundaries

A warm surface must remain mounted but hidden; a cold or evicted surface must not be reused. A slow
boot gets bounded transient retries, while terminal answers fail loud rather than being masked.

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
| Harness setup preserves real stores while replacing the authority and conversation network edges at their module boundaries. | "mocked at their module boundary" | dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:32-48 |
| Teardown unmounts while timers are fake, discards the virtualizer's orphaned debounce, and only then restores real time. | "TanStack Virtualizer owns a 150 ms scroll-observer debounce" | dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:99-112 |
| Boot, pool, epoch/freshness, scroll-restore, and persistent-layer matrices cover the stage seams (six describes). | "ChatsStageBody fresh-chat boot (260721 D1/D2)"; "ChatsStageBody keep-alive pool (F-j)"; "ChatsStageBody epoch attribution (M3)"; "ChatsStageBody authority freshness (M9)"; "ChatsStageBody view-switch scroll restore (F-ac)"; "ChatsStageBody B1: persistent conversation + PTY layers" | dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:111-234; dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:282-404; dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:411-514; dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:516-565; dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:590-756; dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx:767-976 |
| Implementation under test (`ChatsStageBody`). | `ChatsStageBody` | dashboard/src/panels/session-cockpit/ChatsStageBody.tsx:147-489 |
| The typed page/item/status builders the warm seeds now use. | `conversationIdentity`; `conversationStatus`; `conversationItem`; `conversationPage` | dashboard/src/test/fixtures/conversationWire.ts:172-185; dashboard/src/test/fixtures/conversationWire.ts:187-207; dashboard/src/test/fixtures/conversationWire.ts:209-226; dashboard/src/test/fixtures/conversationWire.ts:228-243 |
| The `live.completeness` reason stays `null` under the all-`supported` tree. | `CapabilityReason` | dashboard/src/panels/session-cockpit/conversation/primitives.tsx:140-158 |
| The `history.toolCompleteness`/`history.completeness` cue stays `null` under the all-`supported` tree. | `historyCapability` | dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:313-315 |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History
- 2026-08-14T06:30+02:00 — No production impact: L23 drains TanStack Virtualizer's fake-timer
  callback before restoring real time, preserving the existing scroll-restore proof without jsdom
  teardown leakage. Verification remains closeout-owned.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the keep-alive assertions added with the e2e repair. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T13:42:02+02:00 — 260731-EFA-L6 S18-B08 curator: regenerated the six describe bodies, restored builder owner order, and split the two capability cues so each whole claim retains its operative surface branch.

- 2026-08-01T10:55+02:00 — 260731-EFA-L4 curator: recorded the conversation-wire fixture conversion,
  which is the largest data change any of this leaf's session-cockpit suites received, so the Logic
  section now enumerates it instead of leaving a reader to diff it. The described BEHAVIOUR is
  unchanged, and I traced the one path that could have made it otherwise rather than trusting a green
  run: `capabilities` went from a literal `undefined` to a full all-`supported` tree, and the stage's
  only two capability-driven cues are in `ConversationSurface.tsx` — `live.completeness` renders a
  `CapabilityReason` only when the state is defined AND not `"supported"` (cit:([`CapabilityReason`], dashboard/src/panels/session-cockpit/conversation/primitives.tsx:140-158)), and
  `historyCapability` resolves to `null` unless `toolCompleteness` or `completeness` is not
  `"supported"` (cit:([`historyCapability`], dashboard/src/panels/session-cockpit/conversation/ConversationSurface.tsx:313-315)). Both produced nothing under `undefined` and produce nothing under
  all-`supported`, so no cue appeared or disappeared; `grep` also finds no capability/interrupt/stop
  reference anywhere in this suite. The status gained `identity`/`observedAt`/`freshness`/`evidence`/
  `process.generation`, which is unrelated to the M9 "authority freshness" case (that one is about the
  submission-authority cache having no TTL) — the card now says so, because the shared word is a real
  trap. Suite re-run: all cases pass. Citation repairs: the file is 968 lines, so `L106-L981` was out
  of bounds → `L109-L968` (opening on the first describe); harness setup `L1-L105` → `L1-L107` (the
  `afterEach` closes at 107); implementation `L151-L454` → `L146-L454`, where `ChatsStageBody` actually
  opens. Two rows added.

- 2026-07-24T13:17:17Z — Curator: created the structured-stage regression-suite sidecar. It is
  uncommitted, so verification fields are intentionally blank until closeout stamps the code commit.
