# mcp/src/agents_remember/controlplane/escalation_ladder.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/escalation_ladder.py`        |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `b252c42cca200933d5c9c36e26de47a526a569ce`                           |
| lastVerifiedCommitDate | 2026-08-07T23:58:52+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

P-15 tier 3 (260707-HFX2-L4): the pure escalation-ladder walker. "No signal dies with a silent
seat" — an unacked `OperatorInboxEntry` climbs the spawn edges deterministically: rung 1 (renudge
the original addressee) -> rung 2 (skip-level, re-address to the owner's owner via
`signal_routing.derive_skip_level_owner`, which walks past any dead intermediate) -> rung 3 (the
developer attention queue, terminal). This module decides WHAT should happen and WHO the next
addressee is; `serving/supervisor.py` (the only caller) reads the stores, calls this, and performs
the delivery + durable row update.

## Code Commentary

### 260707-HFX2-L17 Architect Binding Identity

The never-suspect architect exemption now checks current `binding_role`, making a hand-opened seat
attached as architect visible even when it has no spawn provenance. Ladder parent walking remains
provenance-based elsewhere because it reconstructs historical ownership.

### 260707-HFX2-L13 Rung-Dwell Safety Floor

Later-rung eligibility now requires both the configured rung dwell and a hard five-minute minimum
since the newest valid `escalatedAt`/`rungTransitionAt` anchor. Rung zero still follows its per-kind
SLA. Malformed timestamps fail closed. The redundant transition anchor is necessary because the live
HFX3 incident showed stale escalation metadata collapsing several rungs into seconds; generic row
`ts` is unsuitable because delivery and renewal also mutate it. Configured dwell values above five
minutes remain authoritative.

### Logic

`rung_due(entry, *, now, sla_seconds, rung_seconds)` — whether a still-`pending` entry is due for
its NEXT rung. Rung 0 -> 1 uses the per-`message_kind` ack SLA; every later transition uses that
rung's own dwell time, anchored at `entry.escalatedAt` (re-stamped on every transition by
`OperatorInboxStore.advance_rung`) or `entry.createdAt` if never escalated. A row already at
`MAX_RUNG` (3, developer attention) never reports due again — rung 3 is terminal by construction
(R5: no auto-action past the developer), so re-surfacing happens via the row's own rung-3 dwell SLA
firing the SAME signal again, never a further rung bump.

`next_step(catalog, entry)` — the `LadderStep` (rung + action + `RoutedOwner`) for the row's next
transition. Rung 1 = `renudge`, addressed back to the row's own mailbox key (`recipientRole`/
`agentId`/`lifecycleId` — the seat that has not acked). Rung 2 = `skip-level`, calling
`signal_routing.derive_skip_level_owner(catalog, sender_agent_id=entry.agentId,
message_kind=entry.messageKind)`. If that walk hits the hierarchy ceiling (a manager-addressed row
has only one level above it — the orchestrator — so "the owner's owner" resolves to nothing),
`next_step` jumps straight to rung 3/developer rather than stalling an unaddressable rung 2. Rung 3
= `developer-attention`, always `RoutedOwner(role="developer")`, terminal.

`seat_is_suspect(catalog, agent_id, *, now, stale_seconds)` — R3: a seat is "suspect" (respawn
candidate) only when this module can actually OBSERVE it as dead (`signal_routing.is_seat_dead`) or
stalled (an L8-classified `turn_state == "stale"` past `stale_seconds`, the same cutoff the L2
seat-liveness predicate uses). A `None` agent id, or a row this module has no catalog trace for at
all, is never inferred suspect from silence alone — only from an actual dead/stalled catalog
observation.

### Conventions

Pure, no I/O — every function takes `catalog`/`entry` in and returns a frozen value
(`LadderStep`) or a bool; `serving/supervisor.py` is the sole caller and the only place a store
write or delivery happens.

### Invariants And Boundaries

- **Doctrine (R4, HFX-L6 capture hardening):** this module never reassigns a role — it only ever
  finds the next LIVE address to hand a signal to. A spawned seat NEVER absorbs its dead owner's
  role.
- **Rung 3 is a hard ceiling.** `rung_due` refuses to advance a row already at `MAX_RUNG`; the only
  path back through this module for such a row is a repeated rung-3 dwell-SLA re-surface, never a
  state change.
- **The rung-2 hierarchy-ceiling jump is not an error path** — a manager-addressed row legitimately
  has no further owner's-owner to skip to, so `next_step` treats an empty `derive_skip_level_owner`
  result as "go straight to the developer," not as a failure.

### Todos

None.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for the
escalation-ladder's specific rung semantics; the leaf task doc (R1-R6) and the P-15 pilot-observer
log (tier 3, dead-man ladder) are the source of truth.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines this walker; the leaf task doc and P-15 pilot log are authoritative. | `rung_due` | mcp/src/agents_remember/controlplane/escalation_ladder.py:94-120 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two-hop, dead-node-skipping owner derivation `next_step`'s rung-2 branch calls, and the liveness check `seat_is_suspect` calls. | `is_seat_dead`; `derive_skip_level_owner` | mcp/src/agents_remember/controlplane/signal_routing.py:307-315; mcp/src/agents_remember/controlplane/signal_routing.py:335-375 |
| The `OperatorInboxEntry.rung`/`escalatedAt` fields this walker reads, and the `advance_rung` transition its caller stamps. | "rungTransitionAt: str"; `advance_rung` | mcp/src/agents_remember/controlplane/operator_inbox_records.py:207-207; mcp/src/agents_remember/controlplane/operator_inbox_records.py:209-209; mcp/src/agents_remember/controlplane/operator_inbox_transitions.py:255-285 |
| The sole caller: evaluates `rung_due` as a predicate, calls `next_step` for the action, and calls `seat_is_suspect` past the respawn threshold. | "def evaluate_escalation_findings("; "def _escalate_rung(  # pragma: no cover"; "def _respawn_suspect(  # pragma: no cover" | mcp/src/agents_remember/serving/_supervisor_evaluation.py:313-313; mcp/src/agents_remember/serving/_supervisor_actions.py:504-504; mcp/src/agents_remember/serving/_supervisor_actions.py:592-592 |
| Unit tests: rung-due dwell/anchor/ceiling cases, next-step routing per rung including the hierarchy-ceiling jump, and seat-suspect liveness/staleness cases. | `RungDueTests`; `NextStepTests`; `SeatSuspectTests` | mcp/tests/test_escalation_ladder.py:68-110; mcp/tests/test_escalation_ladder.py:113-182; mcp/tests/test_escalation_ladder.py:185-228 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository control-plane logic only. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: removed duplicated Source ranges;
  exact non-fixing check returns zero findings.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 5 repository-reference citations (5/5 anchored and sourced; scoped citation check clean).

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: made the architect never-suspect rule honor current
  seat binding rather than origin provenance.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: enforced the developer-ruled five-minute
  later-rung floor with an independent transition anchor while retaining configured longer dwells and
  rung-zero SLAs. Verification metadata remains pinned until closeout stamps the eventual L13 code
  commit.

- 2026-07-08T23:15+02:00 — Created for 260707-HFX2-L4 (P-15 tier 3, R2/R3): the pure ladder walker
  — `rung_due` (per-kind SLA at rung 0, re-anchored per-rung dwell thereafter, `MAX_RUNG` ceiling),
  `next_step` (rung 1 renudge / rung 2 skip-level via the new two-hop `derive_skip_level_owner` /
  rung 3 developer-attention, with the hierarchy-ceiling jump-to-rung-3 fallback for
  manager-addressed rows), and `seat_is_suspect` (R3, respawn candidate only on an actually
  observed dead/stalled seat). `serving/supervisor.py` is the sole caller. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L4 commit.
