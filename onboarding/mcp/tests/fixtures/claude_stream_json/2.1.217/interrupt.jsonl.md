# mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-31T15:32+02:00                                      |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                  |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `../../../overview.md`                                      |

## Governing Overview

[mcp/tests overview](../../../overview.md)

## Purpose

The recorded Claude 2.1.217 wire sequence for **one interrupted turn**, in order:

1. a `control_response` acknowledging `ar-claude-interrupt-1` with `still_queued: []`;
2. a truncated `assistant` message carrying `aborted: true` and `stop_reason: null`;
3. the synthetic `user` turn Claude writes, `[Request interrupted by user]`;
4. a `result` frame with `subtype: "error_during_execution"` and `is_error: true`.

That fourth frame is why the recording matters: an interrupted turn settles as an
**error-shaped result**, so the interrupt correlation — not the result's own shape — is what
proves cancellation.

## Consumers

This file retains a versioned wire example with `terminal_reason: aborted_streaming`. The former interrupt-settlement test families no longer provide a direct reference to this file in the retained source; the recording alone establishes its payload, not current executable coverage.

## Invariants And Boundaries

- Observed vendor evidence for Claude 2.1.217, recorded under its version directory.
  A recording, never a hand-maintained policy file.
- The error-shaped `result` must stay error-shaped: its abort marker and error fields are distinct data. This fixture does not establish that an arbitrary unstamped error result should be classified as cancellation.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The assistant frame records interrupted streaming. | "aborted" | mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl:2-2 |
| The terminal error result records the abort reason; it is not a successful completion. | "aborted_streaming" | mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl:4-4 |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 2 citation rows covering 3 source references and preserved verification metadata.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created the missing sidecar for this
  fixture (a pre-existing 1:1 gap, not introduced by this leaf).
