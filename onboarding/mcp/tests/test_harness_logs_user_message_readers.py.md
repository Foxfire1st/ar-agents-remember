# mcp/tests/test_harness_logs_user_message_readers.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/tests/test_harness_logs_user_message_readers.py`  |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-07-31T15:32+02:00                                 |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`             |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

**Which log records may prove a dispatch was accepted, per harness.**

Acceptance is decided from harness-owned session JSONL, so the reader for each harness has
to say exactly which record is a *developer submission* and which is bookkeeping that
merely quotes one. A delivery id echoed by the assistant, replayed inside a meta record, or
carried by a tool-result envelope is **not** evidence the message was submitted — accepting
any of them would let the seat certify a dispatch it never delivered.

This module pins the **negative** side of each reader, plus the harness table itself.

## Tests

- `test_claude_non_submission_records_never_prove_delivery` — every record in the case
  contains the delivery id verbatim and none is a submission: the assistant quoting it back,
  a meta record replaying it, a `user` record whose payload is not a message object, and a
  tool-result envelope. Only a real developer-typed `user` message counts.
- `test_codex_accepts_the_event_msg_envelope_of_the_same_submission` — the positive control.
  Codex writes one submission twice; the `event_msg` copy alone is enough evidence.
- `test_codex_non_submission_records_never_prove_delivery` — a payload-less record, an
  assistant reply, and a **structured** `user_message`. The last is the shape guard that
  matters: `event_msg`/`user_message` is only read when its `message` **is** the submitted
  string; a structured body is some other event with the same envelope.
- `test_a_harness_without_a_reader_accepts_nothing` — an unregistered harness has no
  truthful reader, so its log proves nothing. The cwd guard still matches (the file really
  is this seat's session log) and the submission text is right there in it. **Acceptance
  still fails closed**, because reading a third vendor's records with a borrowed reader is
  how a false certification happens.

## Invariants And Boundaries

- Presence of the delivery id in a log is never sufficient. The *record kind* decides.
- A harness with no registered reader accepts nothing — fail closed, never fall back to a
  generic reader.
- The positive control exists so the negative cases cannot pass vacuously.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The per-harness log readers and the harness table under test. | [harness_logs.py](agents-remember/mcp/src/agents_remember/serving/harness_logs.py) |
| The reader-level suite this module extends. | [test_harness_logs.py](agents-remember/mcp/tests/test_harness_logs.py) |
| The authority that consumes these acceptance verdicts. | [test_harness_submission_authority.py](agents-remember/mcp/tests/test_harness_submission_authority.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  non-submission-record suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.
