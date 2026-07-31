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

| Finding | Source Path |
| --- | --- |
| The control surface, interrupt ledger and attachment parser under test. | [serving/](agents-remember/mcp/src/agents_remember/serving/) |
| The per-harness projectors whose unowned/sparse shapes are covered here. | [test_conversation_projector_claude_agents.py](agents-remember/mcp/tests/test_conversation_projector_claude_agents.py), [test_conversation_projector_codex_agents.py](agents-remember/mcp/tests/test_conversation_projector_codex_agents.py) |
| The contract suites whose happy paths these branches complete. | [test_conversation_control_operations.py](agents-remember/mcp/tests/test_conversation_control_operations.py), [test_conversation_control_attachments.py](agents-remember/mcp/tests/test_conversation_control_attachments.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new control /
  projector edge-branch suite. Verification metadata is pinned to the leaf's reformat commit
  until closeout stamps the code commit.
