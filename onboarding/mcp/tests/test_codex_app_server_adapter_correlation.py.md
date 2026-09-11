# mcp/tests/test_codex_app_server_adapter_correlation.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_codex_app_server_adapter_correlation.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-31T10:13+02:00                                            |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`                                        |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_codex_app_server_adapter_correlation.py`'s
source module. It pins early-completion, retained-turn, successor, and bounded-correlation behavior;
the early-completion case also requires the emitted terminal transcript to carry the exact durable
request id from its `ControlOperationRef`.

## Code Commentary



## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_codex_app_server_adapter_correlation.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-31T10:13+02:00 — 260821-ARSPAWN-L5 closeout repair: the early-completion forcing case now
  requires exact request-id projection on the terminal transcript. Verification remains
  closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
