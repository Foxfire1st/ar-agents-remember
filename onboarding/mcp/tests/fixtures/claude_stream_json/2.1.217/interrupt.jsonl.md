# mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/tests/fixtures/claude_stream_json/2.1.217/interrupt.jsonl` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-31T15:32+02:00                                      |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                  |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

The shape is referenced by the interrupt-settlement arms of
`test_conversation_active_service.py` and `test_conversation_active_projectors.py`
(probe-locked 2.1.217, `terminal_reason: aborted_streaming`), and the same version id
appears in the installed capability evidence (`claude-2.1.217-installed-20260722`) used by
`test_conversation_control_operations.py`.

## Invariants And Boundaries

- Observed vendor evidence for Claude 2.1.217, recorded under its version directory.
  A recording, never a hand-maintained policy file.
- The error-shaped `result` must stay error-shaped: the classification fallback in
  `test_conversation_control_projector_edges.py::ClaudeResultSettlementFallbackTests`
  depends on an unstamped error result **not** being read generously as an interrupt.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The interrupt-settlement arms that assert against this shape. | `ClaudeEngineTests`; `ClaudeMapperTests` | mcp/tests/test_conversation_active_projectors.py:407-710; mcp/tests/test_conversation_active_service.py:553-845 |
| The fallback classification that must not upgrade an unstamped error result. | `ClaudeResultSettlementFallbackTests` | mcp/tests/test_conversation_control_projector_edges.py:75-142 |

## Update History

- 2026-08-02T16:55+02:00 — 260731-EFA-L6 W1-B08 curator: repaired 2 citation rows covering 3 source references and preserved verification metadata.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created the missing sidecar for this
  fixture (a pre-existing 1:1 gap, not introduced by this leaf).
