# mcp/src/agents_remember/serving/_app_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_common.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`                                        |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_app_common.py`; owns the behaviours named by its top-level symbols.

## Code Commentary

- `_encode`
- `_ProjectionBodyCache`
- `_if_none_match_matches`
- `_looks_like_image`
- `_apply_terminal_input`
- `TerminalOpenRequest`
- `TerminalAttachLeafRequest`
- `TerminalRetireRequest`
- `TerminalLandedCleanupRequest`
- `TerminalRenameRequest`
- `TerminalPasteRequest`
- `OperatorInboxPostRequest`
- `_catalog_payload`
- `_resolve_request_leaf_key`
- `_leaf_ref_response`
- `_attach_terminal_session`
- `_ResolvedLiveInputs`
- `LiveProjectionInputs`
- `ServingCollaborators`
- `_ServingRuntime`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_app_common.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round 2 (curator): No content impact: the supervisor -> agent-notifier rename does not change the behavior this sidecar documents; reviewed current against the changed source. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
