# mcp/src/agents_remember/observer/reducer_impl/_attention.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/reducer_impl/_attention.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                                        |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[overview](../../overview.md)

## Purpose

Attention queue: rank what needs the human from the reduced surfaces. Pure and deterministic: every source contributes one small builder and the queue sorts by (severity, wait, id). Dismissals suppress lifecycle-bound items until a newer triggering signal re-surfaces them.

## Code Commentary

- `_ask_text`
- `build_attention_queue`
- `_is_dismissed`
- `_signal_after`
- `_await_summary`
- `_lifecycle_attention`
- `_gate_node`
- `_attach_gates`
- `_gate_attention`
- `_provider_attention`
- `_drift_attention`
- `_drift_attention_detail`
- `_setup_attention`
- `_start_attention`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/observer/reducer_impl/_attention.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |

## Update History

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
