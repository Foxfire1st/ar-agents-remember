# claude_stream_submission.py

## Governing Overview
[serving overview](overview.md)

## Purpose

Stores compact per-request Claude correlation, acceptance, terminal, and abandonment evidence.

## Code Commentary

### Logic

`ClaudeSubmission` retains the original request, vendor correlation UUID, submitted wire text,
expected canonical replay text, queue position, separate acceptance/terminal futures, and the
accepted/completed/abandoned lifecycle bits. `consume_future_exception` safely retrieves a late
error after a bounded waiter has already returned.

### Conventions

The record is mutable internal state, not a serving DTO. Acceptance and terminal completion remain
separate because Claude replay and result frames are separate protocol events.

### Invariants And Boundaries

- Records preserve evidence and never authorize resend.
- `abandoned` does not mean completed; the retained record is a late-frame tombstone until its
  ordered terminal result arrives.
- Wire text and canonical replay text are both retained because Claude transforms native slash
  commands during replay.

### Todos

None known for the L3 submission record.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

The state machine owns tombstone lifecycle and exact replay/result correlation.

- State creates these records, correlates exact replays, and completes the terminal future in ordered result handling. [1]

### Cross-Repo References

No external repository boundary is implemented by this record type.

No meaningful cross-repo references found.

## 260715-FEUI-L5 Submission Authority Delta

Claude submission state retains the full operation reference rather than a queued boolean or bare
request id. That ref is the only key allowed to complete/release the shared authority operation.
