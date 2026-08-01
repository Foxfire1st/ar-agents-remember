# dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/ChatsStageBody.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T10:55+02:00 |
| lastVerifiedCommitHash |  `e52edaf5b655f495580efd93306afdf922b19b51`|
| lastVerifiedCommitDate |  2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Session cockpit overview](overview.md)

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant domain documentation was found. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Harness setup preserves real stores while replacing network edges (`vi.mock` of the authority + conversation modules, `afterEach` store reset). | L1-L107 | [ChatsStageBody.test.tsx](ChatsStageBody.test.tsx) |
| Boot, pool, epoch/freshness, scroll-restore, and persistent-layer matrices cover the stage seams (six describes). | L109-L968 | [ChatsStageBody.test.tsx](ChatsStageBody.test.tsx) |
| Implementation under test (`ChatsStageBody`). | L146-L454 | [ChatsStageBody.tsx](ChatsStageBody.tsx) |
| The typed page/item/status builders the warm seeds now use. | L170-L245 | [../../test/fixtures/conversationWire.ts](../../test/fixtures/conversationWire.ts) |
| The only two capability-driven cues on the stage — the `live.completeness` reason and the `history.toolCompleteness`/`history.completeness` cue — both of which stay `null` under the new all-`supported` tree exactly as they did under `undefined`. | L278-L287; L319-L322 | [conversation/ConversationSurface.tsx](conversation/ConversationSurface.tsx) |

## Cross-Repo References

No cross-repository boundary is owned here.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repository evidence applies. | — | — |

## Update History

- 2026-08-01T10:55+02:00 — 260731-EFA-L4 curator: recorded the conversation-wire fixture conversion,
  which is the largest data change any of this leaf's session-cockpit suites received, so the Logic
  section now enumerates it instead of leaving a reader to diff it. The described BEHAVIOUR is
  unchanged, and I traced the one path that could have made it otherwise rather than trusting a green
  run: `capabilities` went from a literal `undefined` to a full all-`supported` tree, and the stage's
  only two capability-driven cues are in `ConversationSurface.tsx` — `live.completeness` renders a
  `CapabilityReason` only when the state is defined AND not `"supported"` (L319-L322), and
  `historyCapability` resolves to `null` unless `toolCompleteness` or `completeness` is not
  `"supported"` (L278-L287). Both produced nothing under `undefined` and produce nothing under
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
