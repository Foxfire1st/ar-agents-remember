# dashboard/src/data/conversation/store.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/store.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-01T09:56+02:00 |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The store-orchestration proof added in fix round 1 to close finding F4 — the round-1 report had
claimed keep-alive/LRU were "covered by store tests" when no such test existed, so this file makes the
claim true. It started as four cases and has grown with each round: today it is seventeen `it` cases
plus a three-row `it.each` (twenty runs) across five describes, all driving
`connectConversation`/`disconnectConversation`/`applyPage` through an injected no-op `EventSource`
and fake `fetch` without a real network. The four founding cases prove keep-alive, bounded LRU, typed
error threading, and (260718-CHATS-L5F R10) the transient boot-race retry. The R10 case pins the honesty boundary that kills the codex-launch cried-wolf red strip: a
hard 4xx fails loud immediately while a transient boot-race (503 / connection-refused) retries
quietly on the `connecting` phase and never flashes the fail-loud alarm.

## Code Commentary

### Logic — what each case proves and why it is required

- **Keep-alive across disconnect** — after connect, `disconnectConversation` stops the stream but the
  `bySession` projection SURVIVES; a later reconnect (new epoch) rehydrates it (§11.1 keep-alive — an
  unfocused session's transcript is not destroyed).
- **Bounded LRU eviction with rehydrate** — seeding 7 hydrated-but-runtime-less sessions then
  connecting an 8th enforces `LRU_LIMIT=6`, evicting the oldest (`s1`); the evicted session simply
  rehydrates on the next `connect`. Only runtime-less (unfocused/disconnected) projections are evicted
  — a live session is never dropped.
- **Typed error threading on first-connect failure (F15)** — a 409 `cursor-reset-required` page read
  lands the exact `{status, detail, httpStatus}` in `errorBySession` and fabricates NO projection
  (`bySession` stays undefined), so the reconnect banner can render the server's real reason.
- **Transient boot-race retry, never fail-loud (260718-CHATS-L5F R10)** — a `fetch` that answers
  transiently (a 503 `bridge composing`, i.e. `httpStatus === 0` or `>= 500`) MUST NOT set
  `errorBySession` on the first attempt: right after the first 503 there is no fail-loud error
  (contrast the 409 case above, which sets it immediately) and the surface stays on the quiet
  `connecting` phase, then keeps retrying rather than giving up after one attempt. This is the
  `hydrateAndStream` initial-hydrate bounded-window retry that stops a just-booting codex bridge from
  flashing the cried-wolf "structured surface unavailable" strip; a hard 4xx still fails loud
  immediately (proven by the 409 case) so a real failure is never masked.

### Invariants And Boundaries

- The injected `FakeEventSource`/`okFetch`/`errorFetch` exercise the real store orchestration
  (generation guards, `enforceLru`, `failStream`) — only transport is faked.
- `afterEach` disconnects every session and `reset()`s the store so cases do not leak runtime.
- The page every fake `fetch` answers with is built by
  `test/fixtures/conversationWire.ts::conversationPage` (identity and status through
  `conversationIdentity`/`conversationStatus`). It replaced a local literal whose `capabilities` was
  `{} as unknown as ConversationCapabilities` — an empty tree where the wire model declares
  twenty-three filled `FeatureCapability` leaves — and whose `status` was a lone `turn` object cast
  past its five sibling fields. The suite never asserts on either, but the fixture is now a page the
  server could actually send rather than one it could not.

### 2026-07-24 Curator Delta

The orchestration suite now covers the exact six-warm-chat LRU bound, slow boot recovery, rejected
resume escalation, and the preservation of warm conversations across refocus without an eager
disconnect.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The store orchestration under test (connect/disconnect/enforceLru/failStream). | `connectConversation`; `enforceLru`; `failStream` | [store.ts](store.ts.md) |
| The stream ctor injected as a no-op. | `EventSourceCtor` | [stream.ts](stream.ts.md) |
| The typed error shape threaded to the banner. | `ConversationPage`; `ConversationCapabilities` | [types.ts](types.ts.md) |
| The shared page/status/identity builders the fake `fetch` answers with. | `conversationPage`; `conversationStatus`; `conversationIdentity` | [../../test/fixtures/conversationWire.ts](../../test/fixtures/conversationWire.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## 260727-CHATS-IM-L2 Child-Hydration Regression Delta

The suite now proves selected-child-only POST routing and encoded identity (L59-L92), concurrent
same-child singleflight (L94-L124), and the exact 64-request/64-state capacity bound — written as the
exported `AGENT_HISTORY_CHILD_LIMIT`, not as a repeated literal — with visible local-resource refusal
(L126-L173). Its three-row `it.each` (L175-L242) preserves non-2xx, network, and timeout reasons as
child-local state while the parent stream stays `live` and `errorBySession` stays clear, and each row
then proves a retry recovers without changing the parent stream.

## Update History

- 2026-08-01T09:56+02:00 — 260731-EFA-L4 curator: corrected two body claims and re-anchored the
  IM-L2 delta's citations. (1) "Four vitest cases" was stale by four rounds of growth — the source is
  seventeen `it` cases plus a three-row `it.each` across five describes. (2) The delta section listed
  four table-driven error reasons ("non-2xx, invalid payload, network, and timeout"); the `it.each`
  table (L175-L202) carries three, and there is no invalid-payload case anywhere in the file. The
  64-request/64-state bound in the same sentence checks out and is kept — `AGENT_HISTORY_CHILD_LIMIT`
  is 64 (`store.ts` L45) and the case asserts through the constant.
  The diff against `abc7cbc` removed seven lines from the fixture block, so L66-L99 / L101-L131 /
  L133-L180 had all slid off their cases — re-anchored to L59-L92 / L94-L124 / L126-L173. Recorded
  in Invariants what the fixture swap actually replaced: `capabilities: {} as unknown as
  ConversationCapabilities` (an empty tree against a model declaring twenty-three filled leaves) and
  a `status` cast past five of its six fields. Left every behavioral bullet untouched after checking
  the consumers — `data/conversation/store.ts` never mentions `capabilities`, `reducer.ts` never
  mentions `capabilities` or `totalItems`, and the only `.status` this suite asserts on is
  `errorBySession.s1.status` at L309 (the F15 `cursor-reset-required` case), which comes from the
  error body and not from the page fixture at all.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: recorded selected-child routing,
  singleflight, capacity, visible failure, and recovery coverage. Verification metadata remains
  pinned while uncommitted.

- 2026-07-24T13:17:50Z — Added current recovery and warm-LRU regression coverage. Verification
  hash/date remain pinned to the pre-commit source stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the fourth vitest case — the R10
  transient boot-race retry. The suite now pins the cried-wolf honesty boundary: a hard 4xx (409
  epoch-rolled) fails loud immediately, a transient 503 retries quietly on the `connecting` phase and
  never flashes the fail-loud alarm. Verification stays pinned; the L5F change is uncommitted and
  closeout re-stamps.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the store-orchestration
  proof (F4/F15) — keep-alive across disconnect, bounded LRU with rehydrate (runtime-less only), and
  typed first-connect error threading with no fabricated projection. Verification is pinned to the
  leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its first source
  stamp.
