# claude_stream_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_state.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose

Reduces Claude frames into normalized snapshots, transcripts, interactions, receipts, and terminal
outcomes while retaining the exact two-stage evidence needed by native session setters.

## Code Commentary

### Logic

`submit` records both wire text and the canonical replay text. A native command is accepted only
after a replay agrees on vendor session, retained UUID, and exact replay body; `wait_terminal` then
waits separately for its ordered result. Cancellation or timeout marks the record abandoned and
removes live lookup entries without discarding the tombstone. A matching late replay/result can
finish only that abandoned command, and a duplicate replay after completion is ignored rather than
requeued. Ordinary prompt correlation, permissions/questions, transcripts, reconciliation, and
API-429 failure metadata remain bounded in the same state machine.

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

### Todos

None known for the L3 correlation state.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The protocol supplies canonical replay text, and the submission record stores both evidence phases.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Protocol parsing derives the canonical native-command replay body and keeps identity-changing commands blocked. | L190-L227 | [claude_stream_protocol.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) |
| Submission records retain wire/replay text, acceptance and terminal futures, and abandoned/completed state. | L18-L35 | [claude_stream_submission.py](agents-remember/mcp/src/agents_remember/serving/claude_stream_submission.py) |
| The adapter waits for terminal evidence and maps absent/refused/exact results without a paste fallback. | L404-L508 | [harness_control_claude.py](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) |

## Cross-Repo References

No external repository boundary is implemented by this state reducer.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented exact session/UUID/body command
  correlation, separate terminal evidence, abandoned-command tombstones, duplicate-replay
  suppression, ordered result pairing, and bounded eviction.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
