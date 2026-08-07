# mcp/src/agents_remember/serving/conversation/_models_status.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/conversation/_models_status.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[Structured conversation contract overview](overview.md)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/conversation/_models_status.py`; owns the behaviours named by its top-level symbols.

## Code Commentary

- `StatusFreshness`
- `ConversationProcessStatus`
- `ConversationTurnWaiting`
- `ConversationTurnOutcome`
- `ConversationTurnStatus`
- `ConversationStatusEvidence`
- `ConversationStatus`
- `AppendItemMutation`
- `AppendBlockDeltaMutation`
- `UpsertItemMutation`
- `ReplacePageMutation`
- `StatusMutation`
- `GapMutation`
- `ConversationEventEnvelope`
- `CapabilityEvidence`
- `FeatureCapability`
- `AttachmentCapability`
- `LiveCapabilities`
- `HistoryCapabilities`
- `AttachmentCapabilities`
- `ControlCapabilities`
- `TelemetryCapabilities`
- `ConversationCapabilities`
- `ConversationPageWindow`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/conversation/_models_status.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
