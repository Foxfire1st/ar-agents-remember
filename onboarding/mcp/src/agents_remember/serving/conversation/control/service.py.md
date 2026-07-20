# mcp/src/agents_remember/serving/conversation/control/service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

The per-app control service authority: one `ConversationControlService` per installed
`ConversationRuntime`, holding the control secret, the bounded per-(session, epoch) operation
ledgers (interrupt, withdrawal, recovery, attachment), the cockpit submit journal, the revision
counters, and the per-session serialization locks. It owns the shared seams every control operation
composes — session resolution, live epoch verify, native identity, full-timeline paging, and the
spool anchor — and consumes the L2E control-plane client reads rather than reimplementing them.

## Code Commentary

### Logic

Named bounds are module constants (L55-L68): 64 channels/app, 64 interrupts/64 withdrawals/32
recoveries/32 attachment-ops/256 journal/256 submits per channel, and the 900 s recovery + 900 s
staged-asset TTLs. Clock helpers `utc_clock` (L72), `iso_seconds_after` (L76), and `iso_expired`
(L83) do the lease arithmetic. The typed `ControlOperationError` family (L93-L132) —
`OperationNotFoundError`, `OperationConflictError`, `CapabilityRefusedError`,
`OperationRejectedError`, `ControlUnavailableError` — is what routes map to the wire. `ControlChannel`
(L148) is the per-(session, epoch) `OrderedDict`-backed ledger bundle with named eviction; the
service builds one lazily via `channel` (L186) under the app channel cap. `ConversationControlService`
(L168) mints a 32-byte control `secret` (L179) and takes an injectable `clock` (L171 — default
`utc_clock`; the fake harness anchors it to `NOW` for time-consistent lease tests). `session_lock`
(L198) hands out the per-session `asyncio.Lock` that serializes every same-session interrupt/withdraw
above the L2E replay cache. `resolve_entry` (L207), `verify_epoch` (L210 — against the live authority),
`live_snapshot` (L216), `build_identity` (L224 — via the L1 factory seam), `read_full_timeline` (L236
— pages the L2E operation-timeline to union completeness), and `spool_assets_root` (L259) are the
shared seams. `conversation_control_service` (L273) resolves the one instance through the
`_SERVICES` `WeakKeyDictionary` memo keyed by runtime (L268), create-on-miss.

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
- The control secret is never persisted; a restart is a loud not-found, not a silent forgery window.

### Todos

- Reviewer precision note 1: `channel.queue_rows` is the one unbounded per-channel structure (per-row
  revision memory, keys never removed) — soft-bounded by session/epoch lifetime and the 256-record
  ledger; a named bound would match the sibling stores' D2 discipline. Non-blocking.

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
| The L1 running-session factory and native-identity proof `build_identity` reuses. | L1-L120 | [active/factories.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/factories.py) |
| The L2E validated interrupt/timeline/submit/recovery reads this service consumes. | L270-L360 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The catalog row `resolve_entry` returns. | L1-L120 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the per-app control
  service — control secret, bounded per-(session, epoch) ledgers with named eviction, per-session
  serialization locks, the injectable clock seam, and the `_SERVICES` weak-key memo, plus the shared
  session/epoch/identity/timeline/spool seams. Verification is blank because the new source file is
  uncommitted; closeout owns its first source stamp.
