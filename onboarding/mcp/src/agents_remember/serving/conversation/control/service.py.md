# mcp/src/agents_remember/serving/conversation/control/service.py

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

Named bounds are module constants; cit:([`MAX_CHANNELS_PER_APP`, `MAX_SESSION_LOCKS_PER_APP`, `MAX_INTERRUPTS_PER_CHANNEL`, `MAX_WITHDRAWALS_PER_CHANNEL`, `MAX_RECOVERIES_PER_CHANNEL`, `MAX_ATTACHMENT_OPS_PER_CHANNEL`, `MAX_JOURNAL_ENTRIES_PER_CHANNEL`, `MAX_SUBMITS_PER_CHANNEL`, `MAX_QUEUE_ROWS_PER_CHANNEL`], mcp/src/agents_remember/serving/conversation/control/service.py:57-57; mcp/src/agents_remember/serving/conversation/control/service.py:60-60; mcp/src/agents_remember/serving/conversation/control/service.py:65-71) 64 channels/app, **128 session locks/app**, 64 interrupts/64 withdrawals/32 recoveries/32 attachment-ops/
256 journal/256 submits, and — since 260718-CHATS-L5F — **256 queue-rows per channel**. The 900 s
recovery and staged-asset leases are separately owned by cit:([`RECOVERY_TTL_SECONDS`, `STAGED_ASSET_TTL_SECONDS`], mcp/src/agents_remember/serving/conversation/control/service.py:76-76; mcp/src/agents_remember/serving/conversation/control/service.py:79-79). Clock
helpers cit:([`utc_clock`], mcp/src/agents_remember/serving/conversation/control/service.py:83-84), cit:([`iso_seconds_after`], mcp/src/agents_remember/serving/conversation/control/service.py:85-89), and cit:([`iso_expired`], mcp/src/agents_remember/serving/conversation/control/service.py:92-99) do the lease
arithmetic. The typed cit:([`ControlOperationError`, `OperationNotFoundError`, `OperationConflictError`, `CapabilityRefusedError`, `OperationRejectedError`, `ControlUnavailableError`], mcp/src/agents_remember/serving/conversation/control/service.py:102-106; mcp/src/agents_remember/serving/conversation/control/service.py:109-113; mcp/src/agents_remember/serving/conversation/control/service.py:116-120; mcp/src/agents_remember/serving/conversation/control/service.py:123-127; mcp/src/agents_remember/serving/conversation/control/service.py:130-134; mcp/src/agents_remember/serving/conversation/control/service.py:137-141) family — `OperationNotFoundError`,
`OperationConflictError`, `CapabilityRefusedError`, `OperationRejectedError`,
`ControlUnavailableError` — is what routes map to the wire. cit:([`ControlChannel`], mcp/src/agents_remember/serving/conversation/control/service.py:199-219) is the
per-(session, epoch) `OrderedDict`-backed ledger bundle with named eviction; its cit:([`queue_rows`], mcp/src/agents_remember/serving/conversation/control/service.py:209-211) is now a bounded `OrderedDict` (the L5F R5 bound, evicted oldest-first inside
`queue_projection._queue_row`), closing the former unbounded per-channel structure. The service
builds one channel lazily via cit:(["def channel"], mcp/src/agents_remember/serving/conversation/control/service.py:246-246) under the app channel cap; the body looks up or creates the
channel, evicts the oldest entry at `MAX_CHANNELS_PER_APP`, refreshes reuse order, and returns it
cit:(["def channel"], mcp/src/agents_remember/serving/conversation/control/service.py:240-250).
cit:([`ConversationControlService`], mcp/src/agents_remember/serving/conversation/control/service.py:222-356) mints a 32-byte control cit:([`secret`], mcp/src/agents_remember/serving/conversation/control/service.py:234-236) and takes an injectable
cit:([`clock`], mcp/src/agents_remember/serving/conversation/control/service.py:238-240) (default `utc_clock`; the fake harness anchors it to `NOW` for time-consistent lease
tests). cit:(["_channels: OrderedDict"], mcp/src/agents_remember/serving/conversation/control/service.py:231-231) and cit:(["_locks: OrderedDict"], mcp/src/agents_remember/serving/conversation/control/service.py:232-232) are both `OrderedDict`s. cit:([`session_lock`], mcp/src/agents_remember/serving/conversation/control/service.py:252-262) hands
out the per-session `asyncio.Lock` that serializes every same-session interrupt/withdraw above the
L2E replay cache, calling cit:([`_evict_idle_locks`], mcp/src/agents_remember/serving/conversation/control/service.py:264-276) before minting a new lock so `_locks` stays
bounded at `MAX_SESSION_LOCKS_PER_APP` — the oldest UNLOCKED lock is evicted and a currently-held
lock is never dropped (a pathological all-held set is left intact). cit:([`release_session`], mcp/src/agents_remember/serving/conversation/control/service.py:278-289) is the
explicit session-end release (L5F R5): it pops the session's lock and deletes every epoch channel
keyed to that session, closing the prime monotonic `_locks` leak — sync pure-dict ops, safe from
any context. cit:([`resolve_entry`], mcp/src/agents_remember/serving/conversation/control/service.py:291-299), cit:([`verify_epoch`], mcp/src/agents_remember/serving/conversation/control/service.py:307-311) (against the live authority),
cit:([`live_snapshot`], mcp/src/agents_remember/serving/conversation/control/service.py:307-313), cit:([`build_identity`], mcp/src/agents_remember/serving/conversation/control/service.py:315-325) (via the L1 factory seam), cit:([`read_full_timeline`], mcp/src/agents_remember/serving/conversation/control/service.py:327-348)
(pages the L2E operation-timeline to union completeness), and cit:([`spool_assets_root`], mcp/src/agents_remember/serving/conversation/control/service.py:350-356) are
the shared seams. `resolve_entry` is async since 260731-EFA-L16: like `verify_epoch`, `live_snapshot`, and
`read_full_timeline` it offloads its blocking read through `asyncio.to_thread`, because
`resolve_running_entry` takes the `TerminalCatalog` RLock and every caller here runs on the uvicorn
event loop, where a catalog lock wait parks the whole server (measured live in the 2026-08-05 ABBA
incident); sync callers needing resolution use `factories.resolve_running_entry` directly, off the
loop. cit:([`conversation_control_service`], mcp/src/agents_remember/serving/conversation/control/service.py:364-371) resolves the one instance through the
`_SERVICES` `WeakKeyDictionary` memo keyed by runtime via cit:([`_SERVICES`, `WeakKeyDictionary`], mcp/src/agents_remember/serving/conversation/control/service.py:365-367), create-on-miss.

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

## Evidence

### Docs References

No Domain Documentation source is configured; the composition is repository-owned.

No configured domain documentation was available for this service.

### Repo-Internal References

The immutable app-scoped runtime is the authority this service keys on; the L1 factory proves native
identity; the L2E validated client reads are the substrate this service consumes.

- The immutable app-scoped `ConversationRuntime` one service instance binds. [1]
- The L1 running-session factory and native-identity proof `build_identity` reuses. [2]
- The L2E validated interrupt/timeline/submit/recovery reads this service consumes. [3]
- The catalog row `resolve_entry` returns (async; offloaded via `asyncio.to_thread` since 260731-EFA-L16). [4]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.

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
