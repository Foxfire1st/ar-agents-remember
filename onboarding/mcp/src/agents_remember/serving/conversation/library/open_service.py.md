# mcp/src/agents_remember/serving/conversation/library/open_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/open_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T16:04+02:00 |
| lastVerifiedCommitHash |  `a84add4c9422b18a26f1748dedaed16194994ded`|
| lastVerifiedCommitDate |  2026-08-10T05:11:18+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The deep open suite covers every arm on doubled launch/proof/retire boundaries; the tracked
opener and retire authority execute the spawn and tombstone; the ASGI suite proves the
outcome→status surface end-to-end.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pre-launch polls stay pending, absent-row retirements report pending, and reconcile completes them for real. | `test_prelaunch_poll_stays_pending_then_real_mismatch_retires_for_real`; `test_absent_row_at_retire_reports_pending_and_reconcile_completes_it` | mcp/tests/test_conversation_library_open.py:283-350; mcp/tests/test_conversation_library_open.py:352-416 |
| Codex resume-thread-id channel, kind guards, identical-replay absorb, and evicted changed-conversation ownership. | `test_codex_open_passes_resume_thread_id_through_the_channel`; `test_non_codex_open_never_carries_resume_thread_id`; `test_codex_open_with_invalid_resume_target_fails_typed`; `test_codex_kind_target_on_non_codex_record_is_rejected`; `test_identical_replay_after_eviction_absorbs_and_opens`; `test_evicted_changed_conversation_never_retires_foreign_session` | mcp/tests/test_conversation_library_open.py:449-483; mcp/tests/test_conversation_library_open.py:485-512; mcp/tests/test_conversation_library_open.py:514-530; mcp/tests/test_conversation_library_open.py:532-547; mcp/tests/test_conversation_library_open.py:594-636; mcp/tests/test_conversation_library_open.py:638-703 |
| Idempotent replay, conflicts, stale digests, retirement, timeout reconcile, ledger bounds, and untouched foreign rows. | `test_open_proves_exact_identity_and_replays_idempotently`; `test_changed_fingerprint_conflicts_without_launching`; `test_stale_expected_digest_fails_before_launch`; `test_identity_mismatch_retires_and_reports`; `test_timeout_unknown_stays_reconcilable_and_opens_later`; `test_ledger_full_of_live_operations_refuses`; `test_ready_without_vendor_identity_stays_reconcilable_not_retired`; `test_existing_catalog_rows_are_never_touched` | mcp/tests/test_conversation_library_open.py:731-781; mcp/tests/test_conversation_library_open.py:783-818; mcp/tests/test_conversation_library_open.py:838-850; mcp/tests/test_conversation_library_open.py:884-918; mcp/tests/test_conversation_library_open.py:920-966; mcp/tests/test_conversation_library_open.py:968-996; mcp/tests/test_conversation_library_open.py:1035-1062; mcp/tests/test_conversation_library_open.py:1064-1093 |
| The tracked opener absorbs identical replays through the live catalog row and carries `resume_thread_id` codex-only. | `_live_open_result`; `_session_command`; `open_terminal_session` | mcp/src/agents_remember/serving/terminal_opener.py:373-387; mcp/src/agents_remember/serving/terminal_opener.py:473-506; mcp/src/agents_remember/serving/terminal_opener.py:678-703 |
| Open routes map outcomes to 201/202/409/503 and focus only the proven identity. | `test_open_created_replays_and_focuses_only_proven_identity`; `test_open_maps_stale_digest_unknown_request_and_timeout`; `test_open_launch_failure_and_identity_mismatch_statuses` | mcp/tests/test_conversation_library_api.py:557-592; mcp/tests/test_conversation_library_api.py:594-647; mcp/tests/test_conversation_library_api.py:649-704 |

## Cross-Repo References

No meaningful cross-repo boundary exists for this local open service.

| Finding | Anchor | Source |
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

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 5 table citations and normalized 5 source paths; no unresolved Tier-3 claims.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations into `test_conversation_library_open.py` (now 1122 lines) by re-anchoring each row on its actual test methods. Pending-retirement arm is L283-L416 (`test_prelaunch_poll_stays_pending_then_real_mismatch_retires_for_real`, `test_absent_row_at_retire_reports_pending_and_reconcile_completes_it`); the codex resume block is L418-L703 (its `-- held-open fix round` section marker through `test_evicted_changed_conversation_never_retires_foreign_session`); the idempotence/conflict/ledger block is L731-L1093 (`test_open_proves_exact_identity_and_replays_idempotently` through `test_existing_catalog_rows_are_never_touched`).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `LibraryBinding` and `OpenRequest` as the caller-binding and idempotent-open concepts.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the idempotent exact open service
  sidecar, recording the review-closed F1 (pre-launch race), F5 (absorbed-lane wrong
  retirement), and O4 (zombie-pending settlement) invariants. Verification is blank until
  closeout commits and stamps the new source.
