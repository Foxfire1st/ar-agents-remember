# mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl

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

## Evidence

### Repo-Internal References

- The assistant frame records interrupted streaming. [1]
- The terminal error result records the abort reason; it is not a successful completion. [2]
