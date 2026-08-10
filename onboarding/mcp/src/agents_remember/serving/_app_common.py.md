# mcp/src/agents_remember/serving/_app_common.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_app_common.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                        |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
