# mcp/tests/test_conversation_control_and_library_helpers.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/tests/test_conversation_control_and_library_helpers.py` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-07-31T15:32+02:00                                      |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                  |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                               |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Behavioural cover for the small mappers and decoders the conversation surfaces lean on —
the private helpers the bigger contract suites reach only through their happy paths.

## What Is Covered

| Class | Helper |
| --- | --- |
| `AttachmentEvictionTests` | `_evict_attachment_operation` frees **exactly one** terminal slot, or refuses. |
| `AttachmentOperationByteDeletionTests` | `_delete_operation_bytes` removes staged bytes **and** the emptied request directory. |
| `WithdrawalFailureMappingTests` | `_failure_for_result` maps every non-withdrawn substrate outcome exactly. |
| `CodexCommandBlocksTests` | `_command_blocks` renders a command item **without guessing missing evidence**. |
| `HelperHostExchangeTests` | `_exchange` writes the JSON-lines request pair and bounds every failure. |
| `HelperLineDecodingTests` | `_decode_lines` proves the response count before anything is interpreted. |
| `HelperFailureMappingTests` | `_raise_helper_failure` types the helper's error and bounds its detail. |
| `PiLibraryRowTests` | `PiConversationLibrary._row` binds one native session row to a signed key. |
| `ActiveProjectorPollLoopTests` | `ActiveSessionProjector._run` releases, gaps, or stops — and **never spins on**. |

## Method

Every test asserts a returned value, an on-disk side effect, or the exact typed refusal.

- `_FakeHelperProcess` is the subprocess boundary as an in-memory pipe pair; **nothing is
  ever spawned**. `_DoubledHost` is the real `ConversationLibraryHelperHost` with only the
  spawn boundary replaced, so the locked wire protocol under test is the production one.
- `_ScriptedBridge` is the substrate reads a projector performs, scripted in memory;
  `_ControlledEntry` drives one entry through it.

## Invariants And Boundaries

- The helper-host wire protocol is *locked*: request/response pairing, line count and
  failure typing are all asserted before any content is interpreted.
- The projector poll loop must reach a terminal decision — release, gap, or stop. A loop
  that keeps polling is the failure this class exists to prevent.
- Attachment eviction frees one slot, never zero and never more; byte deletion removes the
  directory it emptied.
- A Codex command block never invents evidence it was not given.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The conversation control and library surfaces these helpers belong to. | `install_conversation_runtime`; `ActiveConversationService`; `ConversationLibraryPort` | mcp/src/agents_remember/serving/conversation/active/service.py:68-275; mcp/src/agents_remember/serving/conversation/runtime.py:85-91; mcp/src/agents_remember/serving/ports.py:93-118 |
| The contract suites whose happy paths these edge arms complete. | `CodexInterruptTests`; `AttachmentStageTests`; `OpenServiceTests` | mcp/tests/test_conversation_control_attachments.py:72-155; mcp/tests/test_conversation_control_operations.py:40-192; mcp/tests/test_conversation_library_open.py:217-1093 |
| Sibling edge-arm suite for the same surfaces. | `ClaudeResultSettlementFallbackTests` | mcp/tests/test_conversation_control_projector_edges.py:75-142 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T21:13:21+02:00 — W2-B07 curator: repaired 3 repository-reference citations after bounded source reads; the scoped citation check is clean.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  conversation control/library helper suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
