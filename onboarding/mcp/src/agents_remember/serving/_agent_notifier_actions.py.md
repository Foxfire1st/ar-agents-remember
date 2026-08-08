# mcp/src/agents_remember/serving/_agent_notifier_actions.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_actions.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-08-08T21:20+02:00                                            |
| lastVerifiedCommitHash | `1c1629fc97dd4daf352cf9b3529d210be167d2af`                                        |
| lastVerifiedCommitDate | 2026-08-08T22:29:45+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

260731-EFA-L7 responsibility split module for `mcp/src/agents_remember/serving/_agent_notifier_actions.py` (renamed from `_supervisor_actions.py` in 260713-TES-L1); owns the behaviours named by its top-level symbols. Since the rename, the file also owns the two event-name constants (`AGENT_NOTIFIER_EVENT_PREFIX` / `LEGACY_SUPERVISOR_EVENT_PREFIX`) and `_log_event`'s dual append that emits every agent-notifier event under both the current and the legacy observer name for the compatibility window; `_find_coalescible` matches legacy and current seat-liveness ask prefixes as one identity via `_seat_liveness_ask_identity`.

## Code Commentary

- `AGENT_NOTIFIER_EVENT_PREFIX` / `LEGACY_SUPERVISOR_EVENT_PREFIX`
- `_log_event` (dual event emission during the rename window)
- `_redeliver`
- `_resolve_ladder_terminal`
- `_escalate_inbox_entry`
- `_nudge_reason`
- `_auto_nudge`
- `_mark_expectation_missed`
- `_find_coalescible` (legacy+current ask-identity match)
- `OwnerSignal`
- `_post_owner_signal`
- `_signal_emit`
- `_rung_entry`
- `_escalate_rung`
- `_respawn_suspect`
- `_signal_dead_upstream`
- `act_on_finding`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/_agent_notifier_actions.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
## Update History

- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the event dual-emission seam (`AGENT_NOTIFIER_EVENT_PREFIX` + `LEGACY_SUPERVISOR_EVENT_PREFIX` in `_log_event`) and the ask-prefix identity in `_find_coalescible`. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
