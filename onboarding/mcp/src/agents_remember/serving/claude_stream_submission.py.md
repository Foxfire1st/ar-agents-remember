# claude_stream_submission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_submission.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The state machine owns tombstone lifecycle and exact replay/result correlation.

| Finding | Anchor | Source |
| --- | --- | --- |
| State creates these records, correlates exact replays, and completes the terminal future in ordered result handling. | `ClaudeStreamState` | mcp/src/agents_remember/serving/claude_stream_state.py:112-1030 |

## Cross-Repo References

No external repository boundary is implemented by this record type.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Claude submission state retains the full operation reference rather than a queued boolean or bare
request id. That ref is the only key allowed to complete/release the shared authority operation.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T16:56+02:00 — 260731-EFA-L6 curator W1-B06: anchored 1 citation claim
  (Repo-Internal reference row); scoped result 0 findings.

- 2026-07-17T21:39+02:00 — FEUI-L5: documented full-ref Claude submission correlation and removed
  implicit queued authority.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented canonical replay text, separate
  acceptance/terminal futures, abandonment tombstones, and late-future error consumption.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
