# mcp/src/agents_remember/serving/conversation/control/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-04T03:03+02:00 |
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

Named bounds are module constants; cit:([`MAX_CHANNELS_PER_APP`, `MAX_SESSION_LOCKS_PER_APP`, `MAX_INTERRUPTS_PER_CHANNEL`, `MAX_WITHDRAWALS_PER_CHANNEL`, `MAX_RECOVERIES_PER_CHANNEL`, `MAX_ATTACHMENT_OPS_PER_CHANNEL`, `MAX_JOURNAL_ENTRIES_PER_CHANNEL`, `MAX_SUBMITS_PER_CHANNEL`, `MAX_QUEUE_ROWS_PER_CHANNEL`], mcp/src/agents_remember/serving/conversation/control/service.py:55-55; mcp/src/agents_remember/serving/conversation/control/service.py:58-58; mcp/src/agents_remember/serving/conversation/control/service.py:63-69) 64 channels/app, **128 session locks/app**, 64 interrupts/64 withdrawals/32 recoveries/32 attachment-ops/
256 journal/256 submits, and — since 260718-CHATS-L5F — **256 queue-rows per channel**. The 900 s
recovery and staged-asset leases are separately owned by cit:([`RECOVERY_TTL_SECONDS`, `STAGED_ASSET_TTL_SECONDS`], mcp/src/agents_remember/serving/conversation/control/service.py:74-74; mcp/src/agents_remember/serving/conversation/control/service.py:77-77). Clock
helpers cit:([`utc_clock`], mcp/src/agents_remember/serving/conversation/control/service.py:81-82), cit:([`iso_seconds_after`], mcp/src/agents_remember/serving/conversation/control/service.py:85-89), and cit:([`iso_expired`], mcp/src/agents_remember/serving/conversation/control/service.py:92-99) do the lease
arithmetic. The typed cit:([`ControlOperationError`, `OperationNotFoundError`, `OperationConflictError`, `CapabilityRefusedError`, `OperationRejectedError`, `ControlUnavailableError`], mcp/src/agents_remember/serving/conversation/control/service.py:102-106; mcp/src/agents_remember/serving/conversation/control/service.py:109-113; mcp/src/agents_remember/serving/conversation/control/service.py:116-120; mcp/src/agents_remember/serving/conversation/control/service.py:123-127; mcp/src/agents_remember/serving/conversation/control/service.py:130-134; mcp/src/agents_remember/serving/conversation/control/service.py:137-141) family — `OperationNotFoundError`,
`OperationConflictError`, `CapabilityRefusedError`, `OperationRejectedError`,
`ControlUnavailableError` — is what routes map to the wire. cit:([`ControlChannel`], mcp/src/agents_remember/serving/conversation/control/service.py:199-219) is the
per-(session, epoch) `OrderedDict`-backed ledger bundle with named eviction; its cit:([`queue_rows`], mcp/src/agents_remember/serving/conversation/control/service.py:209-211) is now a bounded `OrderedDict` (the L5F R5 bound, evicted oldest-first inside
`queue_projection._queue_row`), closing the former unbounded per-channel structure. The service
builds one channel lazily via cit:(["def channel"], mcp/src/agents_remember/serving/conversation/control/service.py:240-240) under the app channel cap; the body looks up or creates the
channel, evicts the oldest entry at `MAX_CHANNELS_PER_APP`, refreshes reuse order, and returns it
cit:([`channel`], mcp/src/agents_remember/serving/conversation/control/service.py:240-250).
cit:([`ConversationControlService`], mcp/src/agents_remember/serving/conversation/control/service.py:222-349) mints a 32-byte control cit:([`secret`], mcp/src/agents_remember/serving/conversation/control/service.py:232-234) and takes an injectable
cit:([`clock`], mcp/src/agents_remember/serving/conversation/control/service.py:236-238) (default `utc_clock`; the fake harness anchors it to `NOW` for time-consistent lease
tests). cit:([`_channels`], mcp/src/agents_remember/serving/conversation/control/service.py:229-229) and cit:([`_locks`], mcp/src/agents_remember/serving/conversation/control/service.py:230-230) are both `OrderedDict`s. cit:([`session_lock`], mcp/src/agents_remember/serving/conversation/control/service.py:252-262) hands
out the per-session `asyncio.Lock` that serializes every same-session interrupt/withdraw above the
L2E replay cache, calling cit:([`_evict_idle_locks`], mcp/src/agents_remember/serving/conversation/control/service.py:264-276) before minting a new lock so `_locks` stays
bounded at `MAX_SESSION_LOCKS_PER_APP` — the oldest UNLOCKED lock is evicted and a currently-held
lock is never dropped (a pathological all-held set is left intact). cit:([`release_session`], mcp/src/agents_remember/serving/conversation/control/service.py:278-289) is the
explicit session-end release (L5F R5): it pops the session's lock and deletes every epoch channel
keyed to that session, closing the prime monotonic `_locks` leak — sync pure-dict ops, safe from
any context. cit:([`resolve_entry`], mcp/src/agents_remember/serving/conversation/control/service.py:291-292), cit:([`verify_epoch`], mcp/src/agents_remember/serving/conversation/control/service.py:294-298) (against the live authority),
cit:([`live_snapshot`], mcp/src/agents_remember/serving/conversation/control/service.py:300-306), cit:([`build_identity`], mcp/src/agents_remember/serving/conversation/control/service.py:308-318) (via the L1 factory seam), cit:([`read_full_timeline`], mcp/src/agents_remember/serving/conversation/control/service.py:320-341)
(pages the L2E operation-timeline to union completeness), and cit:([`spool_assets_root`], mcp/src/agents_remember/serving/conversation/control/service.py:343-349) are
the shared seams. cit:([`conversation_control_service`], mcp/src/agents_remember/serving/conversation/control/service.py:357-364) resolves the one instance through the
`_SERVICES` `WeakKeyDictionary` memo keyed by runtime via cit:([`_SERVICES`, `WeakKeyDictionary`], mcp/src/agents_remember/serving/conversation/control/service.py:352-354), create-on-miss.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this service. | — | — |

## Repo-Internal References

The immutable app-scoped runtime is the authority this service keys on; the L1 factory proves native
identity; the L2E validated client reads are the substrate this service consumes.

| Finding | Anchor | Source |
| --- | --- | --- |
| The immutable app-scoped `ConversationRuntime` one service instance binds. | `ConversationRuntime` | mcp/src/agents_remember/serving/conversation/runtime.py:55-78 |
| The L1 running-session factory and native-identity proof `build_identity` reuses. | `build_identity` | mcp/src/agents_remember/serving/conversation/active/factories.py:79-105 |
| The L2E validated interrupt/timeline/submit/recovery reads this service consumes. | `read_control_snapshot`; `interrupt_control`; `read_operation_timeline`; `submit_control_prompt` | mcp/src/agents_remember/serving/harness_control_client.py:119-131; mcp/src/agents_remember/serving/harness_control_client.py:214-252; mcp/src/agents_remember/serving/harness_control_client.py:425-445; mcp/src/agents_remember/serving/harness_control_client.py:448-472 |
| The catalog row `resolve_entry` returns. | `resolve_entry` | mcp/src/agents_remember/serving/conversation/control/service.py:291-292 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
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

- 2026-08-04T03:26:26+02:00 — 260731-EFA-L6 S18-SR3-B06 curator: source-read the ambiguous `channel` candidates, applied one provisional declaration-line disambiguator, and generated the whole channel-body range (0 repairs, 1 final normalisation, 1 first-pass decline); the locked rerun recheck was clean with frozen zero source/tokenize/parse/build telemetry.
- 2026-08-04T03:03:23+02:00 — 260731-EFA-L6 S18-SR3-B06 worker: replaced the
  underbound channel-state/loop/move fragments with the complete `channel` owner, binding lookup,
  lazy creation, cap eviction, reuse refresh, and return together. The changed binding is a
  provisional `:1-1` input for the fresh Luna curator; no citation mechanics ran.
- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: preserved the generated
  named-bound and `channel` definition ranges, then source-first bound the two TTL constants and
  the channel body's lazy creation/cap eviction/reuse behavior with honest `:1-1` citations. No
  citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired and normalized the scoped control-service citations; final exact frozen-snapshot check is clean.
- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived the self-citations the `ControlRequest`/
  `ControlScope` insertion invalidated. cit:(["class ControlChannel"], mcp/src/agents_remember/serving/conversation/control/service.py:200-200); cit:(["async def live_snapshot"], mcp/src/agents_remember/serving/conversation/control/service.py:300-300); cit:(["queue_rows: OrderedDict"], mcp/src/agents_remember/serving/conversation/control/service.py:209-209); cit:(["clock: Clock"], mcp/src/agents_remember/serving/conversation/control/service.py:225-225); cit:(["def build_identity"], mcp/src/agents_remember/serving/conversation/control/service.py:308-308); cit:(["self._secret = os.urandom"], mcp/src/agents_remember/serving/conversation/control/service.py:228-228); cit:(["self._channels: OrderedDict"], mcp/src/agents_remember/serving/conversation/control/service.py:229-229); cit:(["self._locks: OrderedDict"], mcp/src/agents_remember/serving/conversation/control/service.py:230-230); cit:(["_SERVICES: weakref.WeakKeyDictionary"], mcp/src/agents_remember/serving/conversation/control/service.py:352-352) were checked against the current definitions and left behaviorally unchanged.
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
