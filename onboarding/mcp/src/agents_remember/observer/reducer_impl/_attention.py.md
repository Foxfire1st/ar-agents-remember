# mcp/src/agents_remember/observer/reducer_impl/_attention.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/observer/reducer_impl/_attention.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-07T22:45:00+02:00                                            |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56`                                        |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview      | `../overview.md`                                          |

## Governing Overview

[overview](../overview.md)

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

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **dead governing-overview body link repaired, and the field brought into agreement with it.** The field named `overview.md` — which resolves, but only under the onboarding root rather than against this card's own route — while the body link named `../../overview.md` and resolved card-relative to nothing, so a reader clicking it landed nowhere and the two declarations disagreed. Both now name `../overview.md`, the route-local overview of this card's own directory, so the field and the link agree by construction. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
