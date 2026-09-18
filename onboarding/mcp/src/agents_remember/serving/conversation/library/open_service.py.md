# mcp/src/agents_remember/serving/conversation/library/open_service.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/library/open_service.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T11:05+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
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
| Codex resume-thread-id channel, kind guards, identical-replay absorb, and evicted changed-conversation ownership. | `test_codex_open_passes_resume_thread_id_through_the_channel`; `test_non_codex_open_never_carries_resume_thread_id`; `test_codex_open_with_invalid_resume_target_fails_typed`; `test_codex_kind_target_on_non_codex_record_is_rejected`; `test_identical_replay_after_eviction_absorbs_and_opens`; `test_evicted_changed_conversation_never_retires_foreign_session` | mcp/tests/test_conversation_library_open.py:449-483; mcp/tests/test_conversation_library_open.py:485-512; mcp/tests/test_conversation_library_open.py:514-530; mcp/tests/test_conversation_library_open.py:532-547; mcp/tests/test_conversation_library_open.py:594-636; mcp/tests/test_conversation_library_open.py:638-703; mcp/tests/test_conversation_library_open.py:554-569 |
| Idempotent replay, conflicts, stale digests, retirement, timeout reconcile, ledger bounds, and untouched foreign rows. | `test_open_proves_exact_identity_and_replays_idempotently`; `test_changed_fingerprint_conflicts_without_launching`; `test_stale_expected_digest_fails_before_launch`; `test_identity_mismatch_retires_and_reports`; `test_timeout_unknown_stays_reconcilable_and_opens_later`; `test_ledger_full_of_live_operations_refuses`; `test_ready_without_vendor_identity_stays_reconcilable_not_retired`; `test_existing_catalog_rows_are_never_touched` | mcp/tests/test_conversation_library_open.py:742-792; mcp/tests/test_conversation_library_open.py:794-834; mcp/tests/test_conversation_library_open.py:854-866; mcp/tests/test_conversation_library_open.py:900-934; mcp/tests/test_conversation_library_open.py:936-982; mcp/tests/test_conversation_library_open.py:984-1012; mcp/tests/test_conversation_library_open.py:1051-1078; mcp/tests/test_conversation_library_open.py:1080-1109 |
| The tracked opener absorbs identical replays through the live catalog row and carries `resume_thread_id` codex-only. | `_live_open_result`; `_session_command`; `open_terminal_session` | mcp/src/agents_remember/serving/terminal_opener.py:439-474; mcp/src/agents_remember/serving/terminal_opener.py:564-598; mcp/src/agents_remember/serving/terminal_opener.py:821-879 |
| The declared legacy decision this route makes, and the reason it cannot carry a capsule. | `LIBRARY_REOPEN_LEGACY_REASON`; `legacy_launch_capsule` | mcp/src/agents_remember/serving/conversation/library/open_service.py:113-124; mcp/src/agents_remember/serving/conversation/library/open_service.py:475-478 |
| The refresh plan that makes a capsule-carrying reopen a fresh thread, which is why the exclusion is a real trade rather than a gap. | "def _capsule_refresh_plan"; "class RefreshPlan" | mcp/src/agents_remember/serving/codex_app_server_session.py:435-474; mcp/src/agents_remember/serving/capsule_delivery.py:383-440 |
| The cases pinning the declaration and the launch-point enumeration. | `test_the_declared_legacy_reopen_names_why_it_cannot_carry_a_capsule`; `test_every_production_launch_request_site_is_wired_or_declares_its_legacy_chain` | mcp/tests/test_capsule_launch_wiring.py:803-814; mcp/tests/test_capsule_launch_wiring.py:761-801; mcp/tests/test_capsule_launch_wiring.py:847-856 |


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
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T11:05+02:00 — 260915-CAPS-L15 curator: **this route is the one launch point left on the
  legacy chain, and the body now says so with its reason.** `LIBRARY_REOPEN_LEGACY_REASON` was added and
  the launch passes `legacy_launch_capsule(...)` explicitly rather than defaulting into a capsule-less
  launch. The measured reason is recorded: this route proves the vendor identity it resumed
  (`_settle_observation`), while L5's refresh plan resolves any resume this session did not open to
  `FRESH_THREAD` — so a capsule here would trade the identity proof for the instructions, which is a
  behaviour decision rather than an oversight. Added the matching invariant and four reference rows, and
  **re-anchored the three opener ranges this leaf's insertions shifted** (`_live_open_result`
  431-448 → **459-476**, `_session_command` 534-568 → **564-598**, `open_terminal_session`
  788-841 → **821-879**); the sanctioned per-document `citation_fix` is unreachable in a leaf worktree
  (D14), so the ranges were re-read by hand against the candidate. Verification metadata moves to this
  leaf's base `15fa0e2c`; the candidate is deliberately uncommitted, so the governed closeout stamps the
  real code commit and no hash or fingerprint was invented here.

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: **citation-range-only repair, no content impact.** This card's cross-file row cites three opener constructs, and the L5 candidate's insertion shifted all three (it added the capsule field and its docstring earlier in `terminal_opener.py`). Re-derived against the current tree: `_live_open_result` 386-403 → **431-448**, `_session_command` 489-522 → **534-568**, `open_terminal_session` 742-795 → **788-841**. The claim's wording is unchanged and still holds; the sanctioned per-document `citation_fix` could not be used (no published citation source-index generation for this contract), so the ranges were re-read by hand. Verification metadata unchanged.

- 2026-08-11T19:58+02:00 — Aligned the current conversation-serving card for `open_service.py` with document identity and active-session opening behavior.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: anchored 5 table citations and normalized 5 source paths; no unresolved Tier-3 claims.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 3 cross-file line citations into `test_conversation_library_open.py` (now 1122 lines) by re-anchoring each row on its actual test methods. Pending-retirement arm is L283-L416 (`test_prelaunch_poll_stays_pending_then_real_mismatch_retires_for_real`, `test_absent_row_at_retire_reports_pending_and_reconcile_completes_it`); the codex resume block is L418-L703 (its `-- held-open fix round` section marker through `test_evicted_changed_conversation_never_retires_foreign_session`); the idempotence/conflict/ledger block is L731-L1093 (`test_open_proves_exact_identity_and_replays_idempotently` through `test_existing_catalog_rows_are_never_touched`).
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `LibraryBinding` and `OpenRequest` as the caller-binding and idempotent-open concepts.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: created the idempotent exact open service
  sidecar, recording the review-closed F1 (pre-launch race), F5 (absorbed-lane wrong
  retirement), and O4 (zombie-pending settlement) invariants. Verification is blank until
  closeout commits and stamps the new source.
