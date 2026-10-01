# claude_stream_state.py

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

## Evidence

### Repo-Internal References

The protocol supplies canonical replay text, and the submission record stores both evidence phases.

- Protocol parsing derives the canonical native-command replay body and keeps identity-changing commands blocked. [1]
- Submission records retain wire/replay text, acceptance and terminal futures, and abandoned/completed state. [2]
- The adapter waits for terminal evidence and maps absent/refused/exact results without a paste fallback. [3]



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
