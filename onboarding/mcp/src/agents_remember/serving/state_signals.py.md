# mcp/src/agents_remember/serving/state_signals.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/serving/state_signals.py`        |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated | 2026-08-11T10:20+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                                    |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Derives terminal-outcome, compound-idle, and non-reaction findings from catalog truth using real
task-document containment for manager ownership.

## Code Commentary

### Logic

`compound_idle_sets` groups a manager with running leaf-role occupants whose documents are direct
children of that manager's master. State-signal and non-reaction evaluation resolve the current
manager structurally, including singular replacement handling. Inbox delivery/landing remains owned
by the shared durable message path.

### Conventions

Task hierarchy determines ownership; runtime ids only correlate observed episodes.

### Invariants And Boundaries

- Spawn ancestry does not establish manager/subordinate membership.
- Missing or ambiguous current managers fail closed.
- Findings arise from terminal/turn evidence, not model artifact judgment.
- State-signal delivery still obeys the target turn boundary.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Compound-idle membership follows direct task containment. | `compound_idle_sets` | mcp/src/agents_remember/serving/state_signals.py:93-117 |
| Terminal outcome findings resolve manager ownership structurally. | `evaluate_state_signal_findings` | mcp/src/agents_remember/serving/state_signals.py:135-186 |
| Non-reaction evaluation uses topology and durable landed rows. | `evaluate_non_reaction_findings` | mcp/src/agents_remember/serving/state_signals.py:211-273 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `state_signals.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented structural all-subordinate membership,
  shared relay evaluation, action-time revalidation, and timezone-aware non-reaction evidence.
  Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the ladder-vocabulary removal in
  `state_signal_held_on_boundary` (boundary-held rows wait for the next boundary; no ladder
  climb exists). Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: updated the landing vocabulary to the formal
  `state="landed"` (non-reaction scan now filters on the terminal state; the by-rule pending
  predicate is gone), and recorded the dead-seat skip in `evaluate_boundary_drain_findings`
  (N2/N14 — rebind machinery owns dead-target rows). Verification metadata pinned until
  closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: added the compound-idle predicate family
  (`_compound_worker_index`, `compound_idle_sets`, `compound_idle_signature`,
  `evaluate_compound_idle_findings`, `compound_idle_response`,
  `COMPOUND_IDLE_SWEEP_LATENCY_SECONDS=10.0`), master-scoped membership on every arm,
  zero-worker no-signal, action-time-signature semantics, and widened the non-reaction
  predicate from worker-only to worker+manager scope. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  state-signal predicate module (NON_REACTION_WINDOW_SECONDS=300, three finding families,
  held-on-boundary exclusion, self-contained payloads, R1/F7 accepted notes). Verification
  metadata pinned to the leaf base `1c1629fc` until closeout stamps the 260713-TES-L2 commit.
