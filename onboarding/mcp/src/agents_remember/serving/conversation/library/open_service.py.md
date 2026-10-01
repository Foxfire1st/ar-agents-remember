# mcp/src/agents_remember/serving/conversation/library/open_service.py

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The idempotent exact-identity open/status/reconcile service: one stable requestId + immutable
fingerprint drives one launch ever, a NEW tracked AR session is opened through the existing
shared opener, and the operation becomes `opened` only after exact catalog proof of session id,
harness, native identity, and bridge epoch.

## Code Commentary

### Logic

**The one launch point left on the legacy chain — by declared decision (260915-CAPS-L15).**
`LIBRARY_REOPEN_LEGACY_REASON` is a named module constant and the launch passes
`legacy_launch_capsule(env.get("AR_SPAWN_ROLE"), LIBRARY_REOPEN_LEGACY_REASON)` explicitly, so a reader
meets a decision with a reason instead of an absent field. The reason is **measured, not stylistic**:
this route exists to reopen one exact native conversation and to prove the identity it resumed
(`_settle_observation` compares `vendor == record.ref.vendor_conversation_id`), while L5's
`_capsule_refresh_plan` resolves *any* resume this session did not itself open to `FRESH_THREAD`
(dropping `threadId`). Delivering a capsule here would therefore convert the reopen into a fresh thread
and destroy the identity proof the route exists for — trading one documented behaviour for another
rather than adding one. The other two production launch points are wired; the enumeration case
(`test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain`) fails if a site has
neither disposition, and a dedicated case pins that this declaration names why. Owner of any future
capsule-carrying reopen: the final-verification leaf, with the harness delivery leaves that own the
thread lifecycle.

`OpenOperationLedger` is a bounded (256) in-memory idempotence ledger keyed by (principal,
requestId) with LRU terminal eviction and a hard refusal when full of live work. `open`
re-authorizes the conversation key through the library service, compares the caller's expected
identity digest, narrows an optional cwd against the conversation's canonical scope, and
fingerprints the immutable request; identical replay returns the retained operation, changed
fingerprint conflicts without launching, and any escaping drive fault settles terminal
`launch-failed` rather than stranding a live pending slot (review O4). `_drive` gates resume
support, resolves and verifies the server-private resume target (kind `argv`, or codex-only
`codex-thread-resume` with a whitespace-rejecting thread-id guard through the landed L0E
channel), launches via the tracked opener with the deterministic `ar-open-<digest>` session id,
then waits bounded for exact catalog proof. `_settle_observation` opens on exact vendor
identity, retires record-spawned mismatches, keeps `ready`-without-identity and expired waits
reconcilable, and — via the `absorbed_existing` spawn-ownership discriminator recorded before
the opener call — fails absorbed foreign sessions honest `launch-failed` without ever retiring
them (review F5). `status`/`reconcile` re-authorize and re-observe; reconcile retries owed
retirements (`retire-failed`/`retire-pending`).

### Conventions

The `_OpenRecord` dataclass is server-private; the wire operation is a strict projection that
publishes session id, bridge epoch, and catalog generation only beside an exact proven
identity. Pre-identity launch failures keep wire `rollback: "not-needed"` while the server
tombstones the row idempotently; a published identity beside an owed-but-uncompletable
retirement rests at visible `retire-pending` and never fabricates a tombstone (review F1b).

### Invariants And Boundaries

- The deterministic session id is replay keying, never launch evidence: only `launched` (set
  after the opener commits the catalog row) authorizes proof observation and retirement
  (review F1/O5).
- Absorbed pre-existing sessions are never retired, whatever they prove; the caller is told to
  retry with a fresh requestId.
- Timeout stays `timeout-unknown` and reconcilable — never a relaunch; the previous
  conversation, draft, focus, and scroll are never touched (there is no browser or Toad state
  in this service at all).
- No durable conversation index and no in-place `switch_session` identity mutation (leaf R6).
- **This route runs the legacy chain by declared decision, and the declaration is load-bearing.** The
  reopen exists to prove the vendor identity it resumed; a capsule applied to a thread this session did
  not open resolves through the installed protocol as a bounded fresh thread, which would destroy that
  proof. `LIBRARY_REOPEN_LEGACY_REASON` is the record, and it is passed explicitly — never defaulted
  into, and never silently omitted.

### Todos

Review O1 hardening note: the token purpose prefix is not MAC-covered; fold purpose into the
MAC domain if a resume target ever leaves the server.

## Evidence

### Docs References

No Domain Documentation source is configured for this internal open service.

No configured domain documentation was available.

### Repo-Internal References

The deep open suite covers every arm on doubled launch/proof/retire boundaries; the tracked
opener and retire authority execute the spawn and tombstone; the ASGI suite proves the
outcome→status surface end-to-end.

- Pre-launch polls stay pending, absent-row retirements report pending, and reconcile completes them for real. [1]
- Codex resume-thread-id channel, kind guards, identical-replay absorb, and evicted changed-conversation ownership. [2]
- Idempotent replay, conflicts, stale digests, retirement, timeout reconcile, ledger bounds, and untouched foreign rows. [3]
- The tracked opener absorbs identical replays through the live catalog row and carries `resume_thread_id` codex-only. [4]
- The declared legacy decision this route makes, and the reason it cannot carry a capsule. [5]
- The refresh plan that makes a capsule-carrying reopen a fresh thread, which is why the exclusion is a real trade rather than a gap. [6]
- The cases pinning the declaration and the launch-point enumeration. [7]


### Cross-Repo References

No meaningful cross-repo boundary exists for this local open service.

No meaningful cross-repo references found.

## 260731-EFA-L2 Current Delta

Two named concepts replaced the open service's parameter lists:

- **`LibraryBinding`** (`runtime`, `shared`, `authorization`) — the app-scoped library authorities
  bound to ONE caller. The runtime and shared library state are per-app; the authorization is
  per-caller. Every operation fingerprint, ledger key and minted session id is derived from that
  pairing, so binding them once is what stops one caller's request from being keyed under
  another's identity.
- **`OpenRequest`** (`request_id`, `expected_identity_digest`, `cwd`, `launch_context`) — one
  idempotent open, in the caller's own words. The request id keys the ledger, the identity digest is
  the exact row the caller believes it is opening, and cwd/launch context narrow where and how.
  Replaying the id with any of the others changed is a **conflict, not a second open** — which is
  only checkable because they form one fingerprinted value.

Idempotency, conflict detection and the minted session identity are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
