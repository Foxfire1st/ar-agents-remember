# mcp/src/agents_remember/serving/_agent_notifier_actions.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_actions.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T10:33+02:00 |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`                                        |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

Applies one evaluated agent-notifier finding through durable inbox transitions, structural owner
rebinding, shared delivery, and observer evidence.

## Code Commentary

L23 batches independent inbox expiry transitions through one durable `transition_many` write while preserving per-finding order, event emission, readdressing, and skip results.

### Logic

`_rebind_due` rewrites a pending row's structural address/owner to the current qualified occupant
before delivery. Expiry and unresolved paths write explicit terminal snapshots. State-signal,
compound-idle, and non-reaction actions use the same structural routing and shared whole-message
delivery; boundary drain records adapter acknowledgement.

### Conventions

Actions re-check the current fold before mutation so a stale sweep snapshot cannot reverse a newer
terminal outcome.

### Invariants And Boundaries

- Ordinary pending rows can follow replacement; dispatch briefs never rebind.
- Rebinding and owner stamps change together.
- Persistence precedes delivery.
- No action treats model consume or completion as acknowledgement.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Due rebinding updates and redelivers the current structural owner. | `_rebind_due` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:177-221 |
| State-signal action uses the durable structural message path. | `_emit_state_signal` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:452-515 |
| Dispatch maps each current finding to one action. | `act_on_finding` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:689-702 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_agent_notifier_actions.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: recorded action-time revalidation, fresh routing
  metadata, fail-closed mutation handling, and role-neutral subordinate relays. Verification
  metadata remains pinned until closeout stamps the code commit.

- 2026-08-09T21:10+02:00 — No content impact: master integration gate repair corrected the source's stale
  `_signal_dead_upstream` self-citation to the declaration's current line. Runtime behavior
  and the action surface are unchanged. Verification metadata stays pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the judgment-action demolition --
  respawn/ladder/auto-nudge/mark-missed action functions deleted, `_FINDING_ACTIONS` reduced to
  the fact-relay surface, nudge store + escalation knobs removed from the context, and the
  stale "ladder owns later climb" docstring claim corrected (reviewer F1). Verification
  metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the rebind/expiry/unresolved
  action family (`_rebind_due`, `_rebind_expired`, `_expire_pending`, `_mark_unresolved`),
  the attempt-ceiling terminal in `_redeliver` (N3), the architect-mailbox readdress on grace
  expiry (N2/N3), the removal of the `escalation-due` action mapping (ladder dormant), and the
  latest-fold transition call sites (F1). Verification metadata pinned until closeout stamps
  the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded `_emit_compound_idle` (action-time
  episode signature in ask + marker, master-scoped member read, one-hop orchestrator owner,
  no-owner skip, no coverage exemption, boundary-gated post) and the manager branch in
  `_emit_non_reaction` (manager residue → orchestrator; worker residue unchanged). Verification
  metadata pinned until closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay actions and the
  owner-signals extraction (posting primitives moved to `owner_signals.py`; retired
  `turn-report-stale` action; boundary admission on redeliver/escalate). Verification metadata
  pinned until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded the event dual-emission seam (`AGENT_NOTIFIER_EVENT_PREFIX` + `LEGACY_SUPERVISOR_EVENT_PREFIX` in `_log_event`) and the ask-prefix identity in `_find_coalescible`. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
