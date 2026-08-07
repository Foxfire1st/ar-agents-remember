# claude_stream_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_state.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-19T09:15+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce` |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose

Reduces Claude frames into normalized snapshots, transcripts, interactions, receipts, and terminal
outcomes while retaining the exact two-stage evidence needed by native session setters.
260718-CHATS-L0E forwards full native frames (assistant blocks, result usage/cost, unhandled
shapes) under the reserved `arEvidence` key while keeping the adapter's own snapshot merge free of
that key.

## Code Commentary

### Logic

`submit` records both wire text and the canonical replay text. A native command is accepted only
after a replay agrees on vendor session, retained UUID, and exact replay body; `wait_terminal` then
waits separately for its ordered result. Cancellation or timeout marks the record abandoned and
removes live lookup entries without discarding the tombstone. A matching late replay/result can
finish only that abandoned command, and a duplicate replay after completion is ignored rather than
requeued. Ordinary prompt correlation, permissions/questions, transcripts, reconciliation, and
API-429 failure metadata remain bounded in the same state machine.

L0E full-frame forwarding places the complete native frame under the reserved `arEvidence` raw key
at three emit sites: assistant frames (every content block — thinking, tool_use, tool_result,
image, text), result frames (usage, modelUsage, total_cost_usd, duration_ms), and the
unhandled-frame fallback (unknown shapes cross with payload preserved and semantics never guessed).
The status-quo keys (`claudeEventType`, `claudeEventSubtype`, `terminalOutcome`) keep their exact
shape. `_emit` excludes the reserved key from the adapter's own snapshot raw merge — the second,
adapter-side merge point — so bridge-side redaction has the final say over what any projection can
see and `snapshot.raw`/`control_raw`/SSE stay byte-identical. Interaction and replay correlation
behavior is unchanged.

### Conventions

Replay acceptance and terminal completion use separate futures. Result frames do not carry the
request UUID, so accepted commands are paired to results in retained order. `unknown` is preserved
when bounded evidence cannot prove effect.

### Invariants And Boundaries

- Same-session UUID and exact canonical body are all required; text-only or pane evidence is never
  enough.
- A later command is not sent while an earlier abandoned command still lacks a terminal frame.
- Completed abandoned tombstones become evictable and duplicate replays cannot steal the next
  command's result.
- Disconnected sessions are reconciliation-only: no resend or sensitive diagnostic retention.
- The reserved `arEvidence` key rides the event only; the adapter's own snapshot merge must stay
  byte-identical for every pre-existing key, so evidence payloads can never reach a projection
  through this reducer.

### Todos

None known for the L3 correlation state.

## Repo-Internal References

The protocol supplies canonical replay text, and the submission record stores both evidence phases.

| Finding | Anchor | Source |
| --- | --- | --- |
| Protocol parsing derives the canonical native-command replay body and keeps identity-changing commands blocked. | `session_command_replay_text`; `command_unsupported_detail` | mcp/src/agents_remember/serving/claude_stream_protocol.py:330-349; mcp/src/agents_remember/serving/claude_stream_protocol.py:352-360 |
| Submission records retain wire/replay text, acceptance and terminal futures, and abandoned/completed state. | `ClaudeSubmission` | mcp/src/agents_remember/serving/claude_stream_submission.py:18-30 |
| The adapter waits for terminal evidence and maps absent/refused/exact results without a paste fallback. | `_submit_set_command`; `_wait_set_terminal`; `_terminal_set_result`; `_completed_set_result` | mcp/src/agents_remember/serving/harness_control_claude.py:402-442; mcp/src/agents_remember/serving/harness_control_claude.py:589-607; mcp/src/agents_remember/serving/harness_control_claude.py:627-646; mcp/src/agents_remember/serving/harness_control_claude.py:649-674 |
| Contract tests pin full-frame forwarding and the no-leak guarantee at both merge points. | `test_assistant_blocks_and_unknown_frames_forward_full_payload_without_leak`; `test_result_usage_and_cost_forward_as_evidence` | mcp/tests/test_harness_control_evidence_other.py:157-205; mcp/tests/test_harness_control_evidence_other.py:208-279 |
| The Claude native page remains fail-closed when the adapter reports it unsupported. | `test_native_page_unsupported_fails_closed_with_adapter_name` | mcp/tests/test_harness_control_evidence_ipc.py:141-153 |

## 260715-FEUI-L5 Submission Authority Delta

Claude now accepts at most one authority operation, runs sole-operation preflight, records the full
ref before guarded write, and correlates exact terminal result/replay evidence back to it. Prompt,
interaction response, model, and effort writes share the transport lock. Prepared/correlation state
is not a FIFO and cannot admit a hidden second prompt; late/cancelled frames complete only their exact
operation.

## 260718-CHATS-L5I Current Delta

Claude stream state retains accepted native-interrupt correlation through settlement and preserves unmatched or malformed frames as evidence. That prevents a late or unrelated error from being rewritten into a user interruption while still allowing an accepted abort to settle honestly.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260731-EFA-L2 Current Delta

Two named concepts replaced loose constructor/threading arguments:

- **`ClaudeStreamSession`** (`identity`, `snapshot`, `transport`, `supported_commands`) — WHICH
  Claude stream this state reduces. The four are settled together at handshake and never
  independently: the supported command set is what THIS transport advertised for THIS identity, and
  the snapshot is the state that pairing starts from.
- **`TranscriptCorrelation`** (`request_id`, `vendor_correlation_id`, `created_at`) — what ties one
  transcript entry back to the submission that produced it, and when. The AR request id and the
  vendor's correlation id name the same submission from the two sides of the bridge; the timestamp
  is the moment they were observed together. An entry stamped with one submission's ids and
  another's time is unusable as evidence.

The replay-user-message path was extracted into `_handle_abandoned_replay` (the late/abandoned
correlation case) and `_require_faithful_replay` (the identity + body checks). Both refusals are
unchanged — the session-identity change and the body-changed-for-its-retained-correlation errors
still raise `HarnessControlError`; they now live in one helper each instead of being written twice.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: removed source-clear domain/cross-repo placeholders and bound replay, submission, adapter, and evidence claims to exact anchors.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the `ClaudeStreamSession` / `TranscriptCorrelation` concepts and the `_handle_abandoned_replay` / `_require_faithful_replay` extraction (replay refusals byte-preserved).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented full-frame `arEvidence`
  forwarding at the assistant/result/unhandled emit sites and the `_emit` reserved-key exclusion
  from the adapter's own snapshot merge (the implementation-found second leak point); the Claude
  native page stays honestly fail-closed because the adapter class lives outside this leaf's
  ownership. Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: replaced multi-queued implications with sole-operation
  preflight, guarded writes, full-ref correlation, and exact terminal completion.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented exact session/UUID/body command
  correlation, separate terminal evidence, abandoned-command tombstones, duplicate-replay
  suppression, ordered result pairing, and bounded eviction.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
