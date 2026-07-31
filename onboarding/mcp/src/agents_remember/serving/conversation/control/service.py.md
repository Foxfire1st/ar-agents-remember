# mcp/src/agents_remember/serving/conversation/control/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T11:30+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

The per-app control service authority: one `ConversationControlService` per installed
`ConversationRuntime`, holding the control secret, the bounded per-(session, epoch) operation
ledgers (interrupt, withdrawal, recovery, attachment), the cockpit submit journal, the revision
counters, and the per-session serialization locks — the locks and queue-rows now bounded-by-
construction and releasable on session end (260718-CHATS-L5F R5). It owns the shared seams every control operation
composes — session resolution, live epoch verify, native identity, full-timeline paging, and the
spool anchor — and consumes the L2E control-plane client reads rather than reimplementing them.

## Code Commentary

### Logic

Named bounds are module constants (L55-L77): 64 channels/app, **128 session locks/app
(`MAX_SESSION_LOCKS_PER_APP`, L58)**, 64 interrupts/64 withdrawals/32 recoveries/32 attachment-ops/
256 journal/256 submits, and — since 260718-CHATS-L5F — **256 queue-rows per channel
(`MAX_QUEUE_ROWS_PER_CHANNEL`, L69)**, plus the 900 s recovery + 900 s staged-asset TTLs. Clock
helpers `utc_clock` (L81), `iso_seconds_after` (L85), and `iso_expired` (L92) do the lease
arithmetic. The typed `ControlOperationError` family (L102-L137) — `OperationNotFoundError`,
`OperationConflictError`, `CapabilityRefusedError`, `OperationRejectedError`,
`ControlUnavailableError` — is what routes map to the wire. `ControlChannel` (L199-L219) is the
per-(session, epoch) `OrderedDict`-backed ledger bundle with named eviction; its `queue_rows`
(L209-L211) is now a bounded `OrderedDict` (the L5F R5 bound, evicted oldest-first inside
`queue_projection._queue_row`), closing the former unbounded per-channel structure. The service
builds one channel lazily via `channel` (L240) under the app channel cap.
`ConversationControlService` (L222) mints a 32-byte control `secret` (L228) and takes an injectable
`clock` (L225 — default `utc_clock`; the fake harness anchors it to `NOW` for time-consistent lease
tests). `_channels` (L229) and `_locks` (L230) are both `OrderedDict`s. `session_lock` (L252) hands
out the per-session `asyncio.Lock` that serializes every same-session interrupt/withdraw above the
L2E replay cache, calling `_evict_idle_locks` (L264) before minting a new lock so `_locks` stays
bounded at `MAX_SESSION_LOCKS_PER_APP` — the oldest UNLOCKED lock is evicted and a currently-held
lock is never dropped (a pathological all-held set is left intact). `release_session` (L278) is the
explicit session-end release (L5F R5): it pops the session's lock and deletes every epoch channel
keyed to that session, closing the prime monotonic `_locks` leak — sync pure-dict ops, safe from
any context. `resolve_entry` (L291), `verify_epoch` (L294 — against the live authority),
`live_snapshot` (L300-L306), `build_identity` (L308-L318 — via the L1 factory seam), `read_full_timeline`
(L320 — pages the L2E operation-timeline to union completeness), and `spool_assets_root` (L343) are
the shared seams. `conversation_control_service` (L357) resolves the one instance through the
`_SERVICES` `WeakKeyDictionary` memo keyed by runtime (L352), create-on-miss.

### Conventions

Ledgers are bounded, reconstructable, and daemon-scoped: records are semantic-revisioned per
channel, terminal/expired records are reclaimed on write sweeps, and a daemon restart invalidates
every reference loudly (the L1 app-scoped cursor-secret posture). The `clock` is a public
constructor seam — the only substitution tests make (the reviewer ruled the fake-harness
`_SERVICES` seed a legitimate fixture technique, not a production bypass).

### Invariants And Boundaries

- One service per runtime; the memo is a `WeakKeyDictionary` so each entry evicts with its runtime.
- Every wire verifies `expectedBridgeEpoch` against the LIVE submission authority; ambient server
  context is never a substitute.
- The per-session lock is above the L2E replay cache (L2E precision note 4: the pair cache is not a
  concurrency lock).
- Every channel store is capped with named eviction (terminal/expired first, oldest last); recovery
  pressure expires the oldest lease with full disposal rather than failing a completed withdrawal.
- `_locks` and `queue_rows` are bounded-by-construction with named caps (128 locks/app via
  `MAX_SESSION_LOCKS_PER_APP`; 256 queue-rows/channel via `MAX_QUEUE_ROWS_PER_CHANNEL`); the lock
  evictor drops the oldest UNLOCKED lock and never a currently-held serializer.
- `release_session` drops the session's lock and every epoch channel on session end. Honesty
  (reviewer F1, master accepted-bounding disposition): it is unit-tested but currently UNWIRED from
  the terminate/retire endpoints — the monotonic `_locks` leak is closed by bounding-by-construction
  plus the active-side tombstone idle-release, NOT yet by an explicit session-end hook. Wiring locus:
  expose the `ConversationRuntime` and call `release_session` after `catalog.mark_terminated` in the
  app.py terminate/retire routes.
- The control secret is never persisted; a restart is a loud not-found, not a silent forgery window.

### Todos

- The former precision note — `channel.queue_rows` the one unbounded per-channel structure — is
  CLOSED by 260718-CHATS-L5F: `queue_rows` now carries the named `MAX_QUEUE_ROWS_PER_CHANNEL=256`
  bound with oldest-first eviction, matching the sibling stores' D2 discipline.
- Reviewer F1 (L5F, non-blocking): `release_session` is not yet called from the terminate/retire
  endpoints — the `_locks` leak is closed by bounding + active-side idle-release; wiring the explicit
  end-hook is the recorded follow-on (locus in Invariants).

## Docs References

No Domain Documentation source is configured; the composition is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this service. | — | — |

## Repo-Internal References

The immutable app-scoped runtime is the authority this service keys on; the L1 factory proves native
identity; the L2E validated client reads are the substrate this service consumes.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The immutable app-scoped `ConversationRuntime` one service instance binds. | L47-L101 | [runtime.py](agents-remember/mcp/src/agents_remember/serving/conversation/runtime.py) |
| The L1 running-session factory and native-identity proof `build_identity` reuses. | L1-L114 | [active/factories.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/factories.py) |
| The L2E validated interrupt/timeline/submit/recovery reads this service consumes. | L270-L360 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The catalog row `resolve_entry` returns. | L1-L120 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260731-EFA-L2 Current Delta

Two concepts now carry request scope through this package, and the distinction between them is the
point:

- **`ControlRequest`** (`service`, `authorization`, `ar_session_id`, `expected_bridge_epoch`) — one
  authorized control request's scope: who is asking, of which session, at which epoch **the caller
  believes**. Nothing in this package may act on a session without all four: the service owns the
  per-(session, epoch) channel, the authorization binding is what every operation fingerprint is
  computed against, and the session id plus expected epoch are what the epoch check verifies. An
  operation carrying one caller's authorization against another session's epoch is exactly the
  confusion that check exists to prevent.
- **`ControlScope`** (`service`, `authorization`, `ar_session_id`, `epoch`) — the same request
  narrowed to the **VERIFIED** epoch, produced by `ControlRequest.resolved(epoch)`. Refs are minted
  and decoded against the verified epoch; carrying the caller's *claimed* epoch past the check would
  let a stale client mint refs for an epoch that no longer exists.

Do not collapse the two types. `ControlRequest` before the check, `ControlScope` after it, is the
invariant they encode.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived the self-citations the `ControlRequest`/
  `ControlScope` insertion invalidated. `ControlChannel` L157→L199-L219 (L157 is now `ControlRequest`
  itself) and `live_snapshot` L343→L300-L306 (L343 had been copied from `spool_assets_root`); the
  same-sentence neighbours that drifted with them were re-derived too — `queue_rows` L252→L209-L211,
  the injectable `clock` L184→L225, `build_identity` L265→L308-L318. `secret` (L228), `_channels`
  (L229), `_locks` (L230) and the `_SERVICES` `WeakKeyDictionary` (L352) were checked and left
  unchanged: they already point at their exact `__init__`/module declaration lines. No behavioral
  claim changed.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `ControlRequest` (claimed epoch) vs `ControlScope` (verified epoch, via `.resolved()`) as the pre/post-check scope types.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R5 per-session release/bounds. `_locks` is now
  a bounded `OrderedDict` (`MAX_SESSION_LOCKS_PER_APP=128`, oldest-UNLOCKED evicted via
  `_evict_idle_locks`, a held lock never dropped) with an explicit `release_session` that pops the
  lock and every epoch channel on session end; `queue_rows` gained the named
  `MAX_QUEUE_ROWS_PER_CHANNEL=256` bound, closing the prior unbounded-queue_rows precision-note Todo.
  Honesty recorded: `release_session` is unit-tested but unwired from terminate/retire (reviewer F1,
  master accepted-bounding disposition — leak closed by bounding + active-side idle-release; wiring
  locus recorded in Invariants). Change uncommitted; closeout re-stamps verification.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the per-app control
  service — control secret, bounded per-(session, epoch) ledgers with named eviction, per-session
  serialization locks, the injectable clock seam, and the `_SERVICES` weak-key memo, plus the shared
  session/epoch/identity/timeline/spool seams. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
