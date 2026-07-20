# mcp/tests/test_harness_control_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:10+02:00 |
| lastVerifiedCommitHash | `c07121fbab43672329bc3b86f9189d4d73ce5f1b`|
| lastVerifiedCommitDate | 2026-07-20T14:14:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Contract suite for the 260718-CHATS-L0E native evidence and resume substrate (leaf R12 clauses
(i)–(viii)). It proves the per-harness evidence round-trips, the bounded buffer semantics, the
no-leak guarantee, native-page continuation correctness, the submission-provenance batch, the
codex resume launch channel, and zero regression of existing IPC semantics — all through the
production mapper → reserved key → bridge buffer → IPC → validated client seam.

260718-CHATS-L3E extends this suite with the evidence-truncation settlement coverage (leaf R1–R6):
it proves the clip envelope preserves a clipped frame's terminal-identity enums (frame `type`, pi
`message.stopReason`, codex `turn.id` + `turn.status`) at their original payload paths while no
other content crosses, both at the byte level (`ClipHelperTests`) and end-to-end through the real
bridge clip at the production 32 KiB budget plus the real `read_control_evidence` IPC surface the L3
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
L3E byte-level terminal-identity preservation: a clipped pi `message_end` keeps exactly `type` +
`message.stopReason` (and no `role`/`content`), a clipped codex `turn/completed` keeps exactly
`turn.id` + `turn.status` and drops the large items body, an absent terminal identity is never
invented (a big blob keeps only the truncation-notice fields; a `message_end` with no `stopReason`
keeps `type` only), and a giant (>256-char) identity scalar in any of the four preserved paths is
dropped WHOLE at the production 32 KiB budget without raising or leaking, with an explicit 256-kept /
257-dropped boundary check. Each proves no content crosses via exact top-level key-sets, an absent
tail-leak sentinel, and a bounded body-char count.

`EvidenceTruncationSettlementIpcTests` (260718-CHATS-L3E R6/R8) drives oversized (>32 KiB)
production terminal-frame shapes end-to-end through the REAL evidence path — the real bridge clip at
the production budget plus the real `read_control_evidence` IPC surface interrupt settlement
consumes — and asserts the frame is actually `arEvidenceTruncated` yet the tiny identity/status
enums survive to the exact reads the L3 settlement code performs: an oversized pi content-ful
`message_end` settles `stop` and `aborted` (facet a — no permanent `pending`), a small mid-turn
frame (crosses whole, unclipped) followed by an oversized final abort settles `aborted` under the
latest-wins scan (facet b — never mis-settling `already-settled`), and an oversized codex
`turn/completed` with a large items body keeps `turn.id` + `turn.status`. Its
`_pi_latest_stop_reason` / `_codex_terminal_status` scan helpers mirror
`control.operations._pi_stop_reason` / `_codex_terminal_outcome` verbatim, so a green run is the
in-leaf acceptance proxy for L3's settlement reads (the definitive check remains L3's unmodified
`probe_l3_delta.py` after base sync). Two new `_EvidenceAdapter` helpers mirror the production
mappers exactly so the regressions drive real frame shapes: `emit_pi_content_ful_message_end`
mirrors `pi_rpc_events._message_event` (a `transcript` event + minted `TranscriptEntry` + the full
frame under `AR_EVIDENCE_KEY`, with `filler_chars` inflating the content past the clip budget) and
`complete_with_codex_turn` mirrors `codex_app_server_adapter._handle_turn_completed` (a `completed`
event bound to the exact operation ref, native turn params under `AR_EVIDENCE_KEY`).

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
- Existing IPC semantics stay green unmodified; this suite adds coverage without editing prior
  suites.
- The L3E settlement regressions replicate each L3 consumer's read expression verbatim against the
  real `read_control_evidence` surface; a green run proves the preserved paths satisfy
  `_pi_stop_reason` / `_codex_terminal_outcome` unchanged (the codex helper matches `turn.id` before
  reading `turn.status`, so a status-only envelope would fail the correlation).
- The L3E no-content proof is structural, not zero-bytes: exact top-level key-sets, a tail-leak
  sentinel absent from the serialized envelope, and a bounded body-char count — the pre-existing
  bounded `preview` prefix is the L0E truncation-notice field and is expected to carry a capped
  content head.
- A giant identity scalar in a preserved path drops whole and never collapses the clip into a
  raise; the boundary is exact (256 kept, 257 dropped), driven at the production 32 KiB budget.

### Todos

Delta-heavy codex streams at realistic sizes and large-thread `thread/read` latency remain
unmeasured by design (worker confidence register entries 3/9); bounds are additive tunables.

## Docs References

No Domain Documentation source is configured. The production seam under test is the direct
evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The bounded evidence deque, reserved-key diversion, and epoch-stamped page reads under test. | L85-L88; L168-L232; L440-L471 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The three additive IPC actions exercised over a real socket. | L198-L203; L286-L313 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The strict client validators for pages, native pages, and provenance. | L286-L358; L576-L730 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The authority's provenance batch read exercised through the queue delegation. | L375-L412 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The codex stop-dropping forwards and `thread/read` native page under test. | L334-L361; L503-L600 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The resume payload/parse/factory/opener channel under test. | L46-L105 | [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py) |

## Cross-Repo References

No neighboring repository participates in this contract suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

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
