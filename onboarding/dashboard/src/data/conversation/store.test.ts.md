# dashboard/src/data/conversation/store.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation/store.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash | `38c3fd81bdf851dce96e9b2b14e2bff741e7b383` |
| lastVerifiedCommitDate | 2026-07-21T11:31:07+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The store-orchestration proof added in fix round 1 to close finding F4 — the round-1 report had
claimed keep-alive/LRU were "covered by store tests" when no such test existed, so this file makes the
claim true. Four vitest cases drive `connectConversation`/`disconnectConversation`/`applyPage`
through an injected no-op `EventSource` and fake `fetch`, proving keep-alive, bounded LRU, typed
error threading, and (260718-CHATS-L5F R10) the transient boot-race retry — all without a real
network. The R10 case pins the honesty boundary that kills the codex-launch cried-wolf red strip: a
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
| The store orchestration under test (connect/disconnect/enforceLru/failStream). | — | [store.ts](store.ts) |
| The stream ctor injected as a no-op. | — | [stream.ts](stream.ts) |
| The typed error shape threaded to the banner. | — | [types.ts](types.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

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
