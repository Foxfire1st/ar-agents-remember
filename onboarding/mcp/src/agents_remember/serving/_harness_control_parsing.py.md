# mcp/src/agents_remember/serving/_harness_control_parsing.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_harness_control_parsing.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                        |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

Wire-response parsing for the hosted harness control client. The blocking client keeps its protocol boundary explicit: every response is validated because the peer is a long-lived subprocess, not trusted in-process state. This module owns the raw-response parsers and shape checks; the client operations (request/read/submit/interrupt) live in :mod:`agents_remember.serving.harness_control_client`...

## Code Commentary

- `_decode_control_response`
- `_unknown_set_result`
- `_submission_receipt`
- `_submission_status_batch`
- `_submission_lookup`
- `_withdrawal_result`
- `_withdrawal_recovery`
- `_asset_reference`
- `_interrupt_result`
- `_operation_timeline`
- `_operation_timeline_items`
- `_operation_timeline_item`
- `_evidence_page`
- `_native_evidence_page`
- `_native_evidence_frames`
- `_native_evidence_frame`
- `_submission_provenance_batch`
- `_submission_provenance_item`
- `_evidence_bridge_epoch`
- `_require_coordinate`
- `_require_page_limit`
- `_required_non_negative_int`
- `_submission_state`
- `_submission_state`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_harness_control_parsing.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
