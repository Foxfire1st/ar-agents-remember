# mcp/tests/test_conversation_control_projector_edges.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                          |
| path                   | `mcp/tests/test_conversation_control_projector_edges.py` |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-31T15:32+02:00                                   |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`               |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                            |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Decisions the conversation control and projector suites only ever reach **on the happy
path**. Each test names one branch the production code takes and asserts the value it
produces.

## Classes

| Class | Branch |
| --- | --- |
| `ClaudeResultSettlementFallbackTests` | A Claude result frame the adapter never classified, read from its **native shape**. The stamp is the accepted-interrupt correlation, so a frame without one may only be read from what the native fields themselves prove — an error-shaped result with no proven cancellation keeps its **failed** meaning rather than being generously called an interrupt. |
| `InterruptStatusTupleGuardTests` | The interrupt-status tuple guard. |
| `PiUncertifiedOperationSettlementTests` | A pi interrupt read while the operation's delivery is still **uncertified**. |
| `AttachmentFormParsingTests` | The four typed refusals of the attachment multipart parser. The body is refused **before any byte is spooled**, and says which part was wrong. |
| `ActiveIdentityProofTests` | The active-identity proof gate. |
| `CodexItemScopedNotificationTests` | An item-scoped Codex note. |
| `CodexThreadItemRoutingTests` | Codex thread-item routing: a patch update, a content-indexed delta, a plan item, an unowned item type. |
| `ClaudeSparseTaskNotificationTests` | A description-less roster notification. |
| `PiAssistantStopReasonTests` | An errored pi turn. |

The mapper shapes covered here are ones **no existing frame in the suite carries** — they
were unreachable through the fixtures the contract suites use.

## Invariants And Boundaries

- Generosity is the bug. An unclassified error result must not be upgraded to "interrupted"
  without the correlation stamp that proves cancellation.
- The multipart parser refuses before spooling, and names the offending part — a parser that
  spooled first would let an oversized or malformed body consume disk before refusing.
- A settlement read against an uncertified delivery must not certify it.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The control interrupt ledger under test. | `_claude_result_settlement`; `interrupt`; `interrupt_status` | mcp/src/agents_remember/serving/conversation/control/operations.py:95-156; mcp/src/agents_remember/serving/conversation/control/operations.py:159-201; mcp/src/agents_remember/serving/conversation/control/operations.py:417-449 |
| The attachment multipart parser under test. | `_parse_uploads` | mcp/src/agents_remember/serving/conversation/control/api.py:737-748 |
| The active-identity proof gate under test. | `build_identity` | mcp/src/agents_remember/serving/conversation/active/factories.py:79-105 |
| The Claude projector whose sparse task shape is covered here. | `map_evidence_frame`; `_map_result` | mcp/src/agents_remember/serving/conversation/projectors/claude.py:210-239; mcp/src/agents_remember/serving/conversation/projectors/claude.py:1021-1074 |
| The Codex projector whose unowned and item-scoped shapes are covered here. | `map_evidence_frame`; `_map_item_scoped_notification` | mcp/src/agents_remember/serving/conversation/projectors/codex.py:148-201; mcp/src/agents_remember/serving/conversation/projectors/codex.py:282-309 |
| The Pi projector whose errored assistant shape is covered here. | `map_evidence_frame`; `_map_assistant_message` | mcp/src/agents_remember/serving/conversation/projectors/pi.py:112-167; mcp/src/agents_remember/serving/conversation/projectors/pi.py:259-331 |
| The interrupt contract suites whose happy paths these branches complete. | `CodexInterruptTests`; `PiInterruptTests`; `ClaudeInterruptTests` | mcp/tests/test_conversation_control_operations.py:40-192; mcp/tests/test_conversation_control_operations.py:195-410; mcp/tests/test_conversation_control_operations.py:413-509 |
| The attachment contract suites whose happy paths these branches complete. | `AttachmentStageTests`; `AttachmentSubmitTests`; `AttachmentRebindTests`; `AttachmentReconcileTransitionTests` | mcp/tests/test_conversation_control_attachments.py:72-155; mcp/tests/test_conversation_control_attachments.py:158-233; mcp/tests/test_conversation_control_attachments.py:236-402; mcp/tests/test_conversation_control_attachments.py:405-569 |

## Update History
- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 8 table citations for control operations, attachment parsing, identity, per-harness projectors, and contract suites; fixer-generated ranges verified.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new control /
  projector edge-branch suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.
