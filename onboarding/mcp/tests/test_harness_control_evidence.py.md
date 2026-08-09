# mcp/tests/test_harness_control_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-08-07T22:45:00+02:00               |
| lastVerifiedCommitHash | `fb0296562ceb29929a3675a1b0195700d23bc56a`|
| lastVerifiedCommitDate | 2026-08-09T20:35:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Contract suite for the native evidence and resume substrate (leaf R12 clauses
(i)–(viii)). It proves the per-harness evidence round-trips, the bounded buffer semantics, the
no-leak guarantee, native-page continuation correctness, the submission-provenance batch, the
codex resume launch channel, and zero regression of existing IPC semantics — all through the
production mapper → reserved key → bridge buffer → IPC → validated client seam.

The suite also carries the evidence-truncation settlement coverage (leaf R1–R6):
it proves the clip envelope preserves a clipped frame's terminal-identity enums (frame `type`, pi
`message.stopReason`, codex `turn.id` + `turn.status`) at their original payload paths while no
other content crosses, both at the byte level (`ClipHelperTests`) and end-to-end through the real
bridge clip at the production 32 KiB budget plus the real `read_control_evidence` IPC surface the
settlement consumers read (`EvidenceTruncationSettlementIpcTests`), so oversized-frame interrupt
settlement stays honest.

## Code Commentary

### Logic

`EvidenceBufferTests` drives a fake adapter through the real bridge: reserved-key round-trip with
no leak into `snapshot.raw`, the projected catalog `control_raw`, or subscriber snapshots while the
evidence page carries the frame; unknown-vendor pass-through with raw preserved and semantics never
guessed; count eviction with an honest gap floor at two sizes; the visible bounded byte clip;
byte-budget paging without overlap or gap; and visible bridge failure on non-monotonic sequences or
non-object payloads. `EvidenceIpcTests` runs the real IPC server over a Unix socket: evidence
paging with epoch stamps, typed cross-domain coordinate rejection in both directions, fail-closed
native pages for unsupported adapters, bridge-stamped epochs on native pages, the full provenance
matrix (all three sources, not-found, epoch mismatch, duplicate ids, 65-id overflow) through the
bridge → queue → authority delegation, and the fixture-honesty proof that a canned fixture-shaped
response without a live epoch fails client validation. `CodexEvidenceTests` proves the previously
dropped `item/completed` and `thread/tokenUsage/updated` frames cross with native ids, and that
`thread/read` paging continues with no overlap/gap, is null-terminated, fails closed on absent
cursors and duplicate item identity, and clips an oversized single frame while still progressing.
`PiEvidenceTests` proves `message_end` and unknown frames cross with full payloads and that the
`get_entries(since)` native page carries typed identity with duplicate-id fail-closed.
`ClaudeEvidenceTests` proves assistant blocks and result usage/cost forward as full evidence
without leaking into the adapter's own snapshot raw. `ResumeChannelTests` and `ResumeOpenerTests`
pin the `resumeThreadId` payload round-trip, legacy field-less parse, malformed rejection, codex-only
factory construction with pre-spawn refusal for non-codex harnesses, the opener `bad-kind` refusals
with zero host interactions, and absent-field behavior preservation. `ClipHelperTests` covers the
clip helper's small-payload passthrough, visible marker, and non-serializable rejection, plus the
byte-level terminal-identity preservation: a clipped pi `message_end` keeps exactly `type` +
`message.stopReason` (and no `role`/`content`), a clipped codex `turn/completed` keeps exactly
`turn.id` + `turn.status` and drops the large items body, an absent terminal identity is never
invented (a big blob keeps only the truncation-notice fields; a `message_end` with no `stopReason`
keeps `type` only), and a giant (>256-char) identity scalar in any of the four preserved paths is
dropped WHOLE at the production 32 KiB budget without raising or leaking, with an explicit 256-kept /
257-dropped boundary check. Each proves no content crosses via exact top-level key-sets, an absent
tail-leak sentinel, and a bounded body-char count.

`EvidenceTruncationSettlementIpcTests` (leaf R6/R8) drives oversized (>32 KiB)
production terminal-frame shapes end-to-end through the REAL evidence path — the real bridge clip at
the production budget plus the real `read_control_evidence` IPC surface interrupt settlement
consumes — and asserts the frame is actually `arEvidenceTruncated` yet the tiny identity/status
enums survive to the exact reads the settlement code performs: an oversized pi content-ful
`message_end` settles `stop` and `aborted` (facet a — no permanent `pending`), a small mid-turn
frame (crosses whole, unclipped) followed by an oversized final abort settles `aborted` under the
latest-wins scan (facet b — never mis-settling `already-settled`), and an oversized codex
`turn/completed` with a large items body keeps `turn.id` + `turn.status`. Its
`_pi_latest_stop_reason` / `_codex_terminal_status` scan helpers mirror
`control.operations._pi_stop_reason` / `_codex_terminal_outcome` verbatim, so a green run is the
in-leaf acceptance proxy for the settlement reads (the definitive check remains the unmodified
`probe_l3_delta.py` after base sync). Two new `_EvidenceAdapter` helpers mirror the production
mappers exactly so the regressions drive real frame shapes: `emit_pi_content_ful_message_end`
mirrors `pi_rpc_events._message_event` (a `transcript` event + minted `TranscriptEntry` + the full
frame under `AR_EVIDENCE_KEY`, with `filler_chars` inflating the content past the clip budget) and
`complete_with_codex_turn` mirrors `codex_app_server_adapter._handle_turn_completed` (a `completed`
event bound to the exact operation ref, native turn params under `AR_EVIDENCE_KEY`).

The reserved-method addition,
`test_native_method_is_carried_onto_the_frame_and_stripped_from_snapshot`, pins the notification-identity
fix end to end: an adapter emit carrying the reserved `AR_EVIDENCE_METHOD_KEY` surfaces the native
method on the typed `EvidenceFrame.native_method` across the bridge divert and the IPC round trip,
while the reserved key is stripped from the republished event so `snapshot.raw` stays byte-identical —
so the codex projector can classify by method instead of shape-guessing, and no method name leaks
into a public snapshot.

`test_native_page_thread_id_is_additive_over_ipc` pins the multiplexed per-thread selector on the
`evidence-native-page` action end-to-end over a real socket: a set `threadId` reaches the
thread-aware adapter as the trailing `thread_id` argument, an unset selector keeps the exact
single-thread adapter call (the bridge passes `None`), and an empty-string selector fails typed
before any adapter call. The `_ThreadAwareNativePageAdapter` fake records the exact call shape so
the test proves forwarding only happens when the wire carries the field.

cit:([`test_evidence_thread_id_round_trips_over_ipc`], mcp/tests/test_harness_control_evidence_ipc.py:91-117) pins the multiplexed demux key on the
evidence wire end-to-end over a real socket: an adapter emit whose `arEvidence` payload carries a
`threadId` surfaces on the typed `EvidenceFrame.thread_id` across the bridge divert, the
`evidence_frame_json` serialization, and the validated client parse, while a frame without the key
reads `None` — the parent thread — so the pre-multiplex wire shape stays identical. The root cause
it guards: before the demux key crossed the evidence wire, a dashboard-side projector received
every evidence frame as thread-less and bound all agent content to the parent conversation.

### Conventions

Tests are `unittest.IsolatedAsyncioTestCase` classes over in-process fakes and real Unix-socket
IPC endpoints under `tmp_path`; assertions are exact-value, never vacuous shape checks. The suite
imports only the production seam it pins — no fixture-only production authority.

### Invariants And Boundaries

- Every evidence assertion proves both sides: the frame reaches the evidence page AND no projection
  (`snapshot.raw`, `control_raw`, SSE subscriber) carries `arEvidence` or payload bytes.
- Coordinate domains stay disjoint: native cursors fail typed in the deque domain and adapter
  sequences fail typed in the native domain, client-side and server-side.
- Continuation must be exact: no overlap, no gap, null-terminated, and an epoch flip mid-paging
  raises `HarnessBridgeEpochMismatchError`.
- The resume channel refuses non-codex harnesses and malformed values before any spawn.
- The native method carried under the reserved `AR_EVIDENCE_METHOD_KEY` reaches
  `EvidenceFrame.native_method` and the IPC round trip, and is stripped from `snapshot.raw` so the
  redacted snapshot stays byte-identical (leaf R1).
- The demux key round-trips verbatim: an agent `threadId` reaches the client
  `EvidenceFrame.thread_id` through the real IPC surface, and parent frames carry no key (the
  pre-multiplex wire stays byte-identical).
- Existing IPC semantics stay green unmodified; this suite adds coverage without editing prior
  suites.
- The settlement regressions replicate each consumer's read expression verbatim against the
  real `read_control_evidence` surface; a green run proves the preserved paths satisfy
  `_pi_stop_reason` / `_codex_terminal_outcome` unchanged (the codex helper matches `turn.id` before
  reading `turn.status`, so a status-only envelope would fail the correlation).
- The no-content proof is structural, not zero-bytes: exact top-level key-sets, a tail-leak
  sentinel absent from the serialized envelope, and a bounded body-char count — the pre-existing
  bounded `preview` prefix is the original truncation-notice field and is expected to carry a capped
  content head.
- A giant identity scalar in a preserved path drops whole and never collapses the clip into a
  raise; the boundary is exact (256 kept, 257 dropped), driven at the production 32 KiB budget.

### Todos

Delta-heavy codex streams at realistic sizes and large-thread `thread/read` latency remain
unmeasured by design (worker confidence register entries 3/9); bounds are additive tunables.

## Docs References

No Domain Documentation source is configured. The production seam under test is the direct
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The bounded evidence deque, reserved-key diversion, and epoch-stamped page reads under test. | `HarnessControlBridge` | mcp/src/agents_remember/serving/harness_control_bridge.py:77-543 |
| The three additive IPC actions exercised over a real socket. | `HarnessControlServer` | mcp/src/agents_remember/serving/harness_control_ipc.py:99-412 |
| The strict client validators for pages (including the `threadId` frame parse), native pages, and provenance. | `read_control_evidence`, `read_control_native_page`, `read_submission_provenance` | mcp/src/agents_remember/serving/harness_control_client.py:346-366; mcp/src/agents_remember/serving/harness_control_client.py:369-401; mcp/src/agents_remember/serving/harness_control_client.py:404-422 |
| The authority's provenance batch read exercised through the queue delegation. | `HarnessSubmissionAuthority` | mcp/src/agents_remember/serving/harness_submission_authority.py:116-1023 |
| The codex stop-dropping forwards (a transcript-less `item/completed` and any foreign notification cross as raw `codex-notification` evidence instead of being dropped) and the `read_native_page` contract under test. | `read_native_page` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:395-421 |
| The resume payload/parse/factory/opener channel under test. | `parse_runner_config` | mcp/src/agents_remember/serving/harness_control_runner.py:72-97 |

## Cross-Repo References

No neighboring repository participates in this contract suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Current Delta

Evidence tests now cover the extended normalized control evidence used for structured interaction and interrupt correlation, preserving redaction and byte-boundary guarantees.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## 260727-CHATS-IM-L2 Opaque History/IPC Regression Delta

Codex native-page cases now drive items-list source cursors through the adapter and private socket,
assert the `ar-cnh1` continuation is opaque, and prove every item is emitted once across pages.
Repeated source ids/cursors and an oversized projected source response produce typed local
failures. The IPC cases additionally prove `NativeHistoryUnavailable` and
`NativeHistoryLimitExceeded` preserve stable code and byte evidence in both control-client
directions.

## 260731-EFA-L2 Delta — present but unusable

`test_a_present_but_unusable_native_method_fails_the_bridge_visibly`: a native method that exists
but cannot be used must fail the bridge **visibly**. Degrading quietly would leave the cockpit
believing an evidence channel it does not have.

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 5 repository-internal reference rows for the bounded evidence bridge, IPC server, strict client validators, submission authority, and runner payload parser; scoped citation verification follows.

- 2026-07-31T19:30+02:00 — 260731-EFA-L2 curator: re-derived 1 stale self-citation.
  `test_evidence_thread_id_round_trips_over_ipc` is L679-L705; the cited L683-L707 started inside
  the test's docstring and ran one line into `test_cross_domain_coordinates_fail_typed`. The claim
  (a `threadId` in the `arEvidence` payload surfaces on `EvidenceFrame.thread_id`, a frame without
  the key reads `None`) re-verified against the assertions at L700/L702 and unchanged.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. In the 1503-line `codex_app_server_adapter.py` the stop-dropping forwards are `_handle_foreign_notification` + `_emit_notification` (cit:([`_handle_foreign_notification`, `_emit_notification`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:703-714; mcp/src/agents_remember/serving/codex_app_server_adapter.py:716-732)) and the transcript-less completion branch (cit:(["        await self._emit_notification(\"item/completed\", params)"], mcp/src/agents_remember/serving/codex_app_server_adapter.py:807-807)); the native page the suite drives is `read_native_page` (cit:([`read_native_page`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:399-425)). Reworded the claim, which said "`thread/read` native page" — the adapter's `thread/read` call is in `reconcile` (cit:([`reconcile`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:359-397)), not on the native-page path.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: recorded the arms this leaf added; the rest of this card was re-read against the file and remains true. Call sites in this module now build parameter objects (see the route overview) — what the suite proves is unchanged. Verification metadata pinned until closeout stamps the code commit.

- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: documented opaque Codex continuation,
  once-only paging, duplicate/cycle/limit refusal, and typed history error round-trip coverage.
  Verification metadata remains pinned while uncommitted.

- 2026-07-27T00:02+02:00 — 260718-CHATS-L7R curator: recorded the evidence `threadId` IPC
  round-trip test (cit:([`test_evidence_thread_id_round_trips_over_ipc`], mcp/tests/test_harness_control_evidence_ipc.py:91-117)): an agent `threadId`
  crosses the bridge divert + serializer + real socket + client parse into
  `EvidenceFrame.thread_id`, while parent frames carry none (the pre-multiplex wire stays
  identical); re-anchored the stale client-validators citation to the current parser block
  (cit:(["def _evidence_page(result: object, *, expected_bridge_epoch", "def _native_evidence_page(  # pragma: no cover", "def _submission_provenance_batch(  # pragma: no cover"], mcp/src/agents_remember/serving/_harness_control_parsing.py:348-348; mcp/src/agents_remember/serving/_harness_control_parsing.py:399-399; mcp/src/agents_remember/serving/_harness_control_parsing.py:459-459)), and scrubbed the pre-existing task-id references out of the body (bodies carry
  behavioral prose only; the tags remain in this history). Verification metadata stays pinned
  (uncommitted); closeout re-stamps the candidate
  commit.

- 2026-07-26T18:30+02:00 — 260718-CHATS-L7 curator: recorded the multiplexed native-page selector
  coverage — `test_native_page_thread_id_is_additive_over_ipc` plus the `_ThreadAwareNativePageAdapter`
  fake: an optional `threadId` crosses the real IPC socket end-to-end to the adapter, an unset
  selector keeps the exact single-thread call shape, and an empty selector fails typed before any
  adapter call. One Logic paragraph added; verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the R1 notification-identity round-trip
  test (`test_native_method_is_carried_onto_the_frame_and_stripped_from_snapshot`) — the native method
  reaches `EvidenceFrame.native_method` across the bridge divert + IPC while the reserved key is
  stripped so `snapshot.raw` stays byte-identical. Verification metadata stays pinned (uncommitted);
  closeout re-stamps the candidate commit.
- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: added the evidence-truncation settlement
  coverage — three byte-level clip terminal-identity preservation tests plus one giant-scalar
  drop-whole regression (256/257 boundary) in `ClipHelperTests`, and the new
  `EvidenceTruncationSettlementIpcTests` (four end-to-end oversized-frame regressions through the
  real bridge clip + `read_control_evidence`, mirroring the L3 `_pi_stop_reason` /
  `_codex_terminal_outcome` reads) plus the two production-mapper-mirroring `_EvidenceAdapter`
  helpers (`emit_pi_content_ful_message_end`, `complete_with_codex_turn`). Verification metadata
  stays pinned to the last committed source until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: created the evidence contract suite sidecar
  (32 tests + 6 subtests covering R12 (i)–(viii)). Verification is blank because the new source
  file is uncommitted; closeout owns its first source stamp.
