# mcp/src/agents_remember/serving/conversation/library/open_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/open_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `67cad9bcdc736de70168ea9c153a0f12319a7263`|
| lastVerifiedCommitDate |  2026-07-19T17:19:21+02:00|
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
| Pre-launch polls stay pending, absent-row retirements report pending, and reconcile completes them for real. | L274-L437 | [test_conversation_library_open.py](agents-remember/mcp/tests/test_conversation_library_open.py) |
| Codex resume-thread-id channel, kind guards, identical-replay absorb, and evicted changed-conversation ownership. | L438-L707 | [test_conversation_library_open.py](agents-remember/mcp/tests/test_conversation_library_open.py) |
| Idempotent replay, conflicts, stale digests, retirement, timeout reconcile, ledger bounds, and untouched foreign rows. | L708-L1067 | [test_conversation_library_open.py](agents-remember/mcp/tests/test_conversation_library_open.py) |
| The tracked opener absorbs identical replays through the live catalog row and carries `resume_thread_id` codex-only. | L170-L257 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) |
| Open routes map outcomes to 201/202/409/503 and focus only the proven identity. | L535-L703 | [test_conversation_library_api.py](agents-remember/mcp/tests/test_conversation_library_api.py) |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local open service.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the idempotent exact open service
  sidecar, recording the review-closed F1 (pre-launch race), F5 (absorbed-lane wrong
  retirement), and O4 (zombie-pending settlement) invariants. Verification is blank until
  closeout commits and stamps the new source.
