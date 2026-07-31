# mcp/src/agents_remember/serving/conversation/library/open_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/open_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`|
| lastVerifiedCommitDate |  2026-07-31T19:28:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Native conversation library overview](overview.md)

## Purpose

The idempotent exact-identity open/status/reconcile service: one stable requestId + immutable
fingerprint drives one launch ever, a NEW tracked AR session is opened through the existing
shared opener, and the operation becomes `opened` only after exact catalog proof of session id,
harness, native identity, and bridge epoch.

## Code Commentary

### Logic

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

### Todos

Review O1 hardening note: the token purpose prefix is not MAC-covered; fold purpose into the
MAC domain if a resume target ever leaves the server.

## Docs References

No Domain Documentation source is configured for this internal open service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The deep open suite covers every arm on doubled launch/proof/retire boundaries; the tracked
opener and retire authority execute the spawn and tombstone; the ASGI suite proves the
outcome→status surface end-to-end.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pre-launch polls stay pending, absent-row retirements report pending, and reconcile completes them for real. | L283-L416 | [test_conversation_library_open.py](agents-remember/mcp/tests/test_conversation_library_open.py) |
| Codex resume-thread-id channel, kind guards, identical-replay absorb, and evicted changed-conversation ownership. | L418-L703 | [test_conversation_library_open.py](agents-remember/mcp/tests/test_conversation_library_open.py) |
| Idempotent replay, conflicts, stale digests, retirement, timeout reconcile, ledger bounds, and untouched foreign rows. | L731-L1093 | [test_conversation_library_open.py](agents-remember/mcp/tests/test_conversation_library_open.py) |
| The tracked opener absorbs identical replays through the live catalog row and carries `resume_thread_id` codex-only. | L170-L257 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |
| Open routes map outcomes to 201/202/409/503 and focus only the proven identity. | L535-L703 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local open service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

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

## Update History

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations into `test_conversation_library_open.py` (now 1122 lines) by re-anchoring each row on its actual test methods. Pending-retirement arm is L283-L416 (`test_prelaunch_poll_stays_pending_then_real_mismatch_retires_for_real`, `test_absent_row_at_retire_reports_pending_and_reconcile_completes_it`); the codex resume block is L418-L703 (its `-- held-open fix round` section marker through `test_evicted_changed_conversation_never_retires_foreign_session`); the idempotence/conflict/ledger block is L731-L1093 (`test_open_proves_exact_identity_and_replays_idempotently` through `test_existing_catalog_rows_are_never_touched`).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `LibraryBinding` and `OpenRequest` as the caller-binding and idempotent-open concepts.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the idempotent exact open service
  sidecar, recording the review-closed F1 (pre-launch race), F5 (absorbed-lane wrong
  retirement), and O4 (zombie-pending settlement) invariants. Verification is blank until
  closeout commits and stamps the new source.
