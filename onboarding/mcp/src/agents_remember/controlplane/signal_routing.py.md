# mcp/src/agents_remember/controlplane/signal_routing.py

| Field                  | Value                                                             |
| ---------------------- | ------------------------------------------------------------------ |
| repository             | agents-remember                                                    |
| path                   | `mcp/src/agents_remember/controlplane/signal_routing.py`           |
| doc_type               | `file-level-onboarding`                                            |
| lastUpdated            | 2026-07-10T01:14+02:00                                             |
| lastVerifiedCommitHash | `5b49fa85a51d527a5a216a88c361c08246c759d0`|
| lastVerifiedCommitDate | 2026-07-10T05:00:02+02:00|
| governingOverview      | `overview.md`                                                      |

## Governing Overview

[overview.md](overview.md)

## Purpose

R4 (260707-HFX2-L1): derive a signal's routed owner address from catalog spawn provenance — one
hop up the spawn edge (worker -> its manager, manager -> its orchestrator), never further (a
developer ruling: no layer is addressed its grandchildren's noise). 260707-HFX2-L4 (R2/R4) adds a
second, deliberately separate two-hop derivation — `derive_skip_level_owner` — for the escalation
ladder's rung-2 skip-level target and the dead-upstream grandparent signal, plus `is_seat_dead`, the
liveness check both the ladder and that two-hop walk use to skip past a confirmed-dead node.

## Code Commentary

### 260707-HFX2-L13 Manager-First Routing And Chain Progress

Worker, reviewer, and curator signals now resolve the live direct manager first, then a manager
proven on the same qualified leaf/master, and otherwise the role-only manager mailbox. Address-time
routing never guesses a manager from another master and never jumps directly to orchestrator or
architect. The older spawn-provenance walk remains separate and is used only by later ladder
skip-level derivation.

`leaf_chain_has_progress` suppresses stale expectations, inactivity signals, redelivery, and rung
escalation when another exact-leaf seat, the current manager, or an unbound reviewer/curator spawned
by that manager in the subject worktree has progressed. Current code deliberately excludes unbound
workers from that active-phase credit. The round-2 reviewer accepted the resulting bounded
false-inactivity refire risk as non-blocking because manager addressing, cooldowns, the five-minute
floor, and completion wake bound it; HFX2-L14 S7 owns extending same-worktree/current-manager credit
to the unbound worker without cross-leaf suppression. Do not document or infer that S1 is fixed here.

### Logic

`_OWNER_ROLE_BY_SENDER_SPAWN_ROLE` maps the SENDER's own spawned-as role to its owner's role:
`worker -> manager`, `manager -> orchestrator`. Any other spawn role (orchestrator, strategist,
reviewer, designer, ...) has no entry, so `derive_signal_owner` returns an empty `RoutedOwner()` —
"no route derived, keep the caller's explicit `recipient_role`" — this module never fabricates an
address.

`derive_signal_owner(catalog, sender_agent_id=, message_kind=)`: a `message_kind ==
"decision-item"` always routes to the reserved `architect` role regardless of provenance (the
routing TARGET is reserved here; the decision-item QUEUE itself is a different leaf's job, AQR
Q3). Otherwise it looks up `sender_agent_id` in the catalog and reads the address straight off the
SENDER's own row: `spawned_by_session` / `spawned_by_lifecycle`
(`serving/terminal_catalog.py:48-59`) — no second catalog lookup is needed to resolve "the
manager's own session id" because that field IS it.

`RoutedOwner` is a frozen dataclass, not a Pydantic model — this module is pure derivation logic
with no wire/persistence concern of its own; the caller (`mcp/tools/operator_inbox.py::
operator_inbox_post_payload`) stamps the result onto the durable `OperatorInboxEntry`'s
`ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields at post time.

**260707-HFX2-L4 (R2/R4).** `is_seat_dead(catalog, agent_id)` — `True` for `None`, an unknown
catalog id, or any non-`running` status; "no evidence of life" reads the same as "confirmed dead"
here, since there is nothing live to route TO. `derive_skip_level_owner(catalog, *,
sender_agent_id, message_kind)` walks the SENDER's provenance TWO hops (hop 1 =
`derive_signal_owner(sender)`, the ordinary one-hop owner; hop 2 =
`derive_signal_owner(hop-1's owner)`, the owner's owner) — but unlike `derive_signal_owner`, it
walks PAST any dead node it lands on: if hop 1 is dead, the walk continues from hop 1's own owner as
if hop 1 had answered; if the eventual hop-2 landing is dead, the walk continues once more rather
than stopping there. A cycle or an exhausted chain (no further owner-role mapping — the top of the
hierarchy, the orchestrator, has none) returns whatever the walk last resolved, or `RoutedOwner()`
if nothing did. This is deliberately a SECOND function, not a parameter on `derive_signal_owner` —
see Invariants.

### Conventions

Every "no route" case returns the same empty `RoutedOwner()` sentinel (all fields `None`) rather
than raising — routing derivation is best-effort surfacing, never a hard requirement a caller must
satisfy before posting.

### Invariants And Boundaries

- **`derive_signal_owner` remains one hop only**, unchanged by this leaf: a worker's signal never
  chases the chain past its manager to the orchestrator, even though the manager's OWN
  `spawned_by_session` is the orchestrator — routing reads only the SENDER's provenance, never
  recurses. A locked existing test (`test_no_layer_is_addressed_its_grandchildren_noise`) pins this
  invariant for THIS function specifically.
- **`derive_skip_level_owner` is why that invariant stays locked as a SEPARATE function rather than
  a parameter.** The one-hop rule is about who ADDRESSES whom (an existing caller's routing
  contract); the two-hop walk is a different question — how many hops THIS walker takes to find a
  live address for the SAME sender, for the ladder's rung-2/R4-grandparent use case. Folding them
  together would either break the locked test or silently change routing for every existing
  `derive_signal_owner` caller (the L2 supervisor's nudge/signal-emit actions).
- Pure and catalog-read-only: neither function ever mutates the catalog or posts an inbox entry.
- `decision-item` routing to `architect` is unconditional — it does not consult the catalog at all
  (unchanged, `derive_signal_owner` only).
- `derive_skip_level_owner`'s walk is bounded (a 64-node pathological-chain guard) so a corrupt or
  cyclic catalog can never hang it.

### Todos

None.

## Docs References

No meaningful external design-doc references found yet (created this leaf); the "no layer is
addressed its grandchildren's noise" rule is a developer ruling recorded in the leaf spec, not an
existing design doc.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The owner address is read straight off the sender's own `spawned_by_session`/`spawned_by_lifecycle` catalog fields. | L48-L59 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| The two callers of the two-hop walk: rung 2's skip-level target and the dead-upstream grandparent signal. | `derive_skip_level_owner` | [../serving/supervisor.py](../serving/supervisor.py.md) |
| `next_step`'s rung-2 branch calls this walker directly and detects the hierarchy-ceiling empty-owner case. | `derive_skip_level_owner` | [escalation_ladder.py](escalation_ladder.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: replaced stale one-hop leaf addressing with
  current-manager resolution, separated historical skip-level provenance, and added chain-progress
  suppression. Recorded the accepted S1 truth that unbound workers remain excluded until HFX2-L14.
  Verification metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (R2/R4, escalation ladder + dead-upstream detection):
  added `is_seat_dead` (liveness check — unknown or non-`running` reads as dead) and
  `derive_skip_level_owner` (a second, separate two-hop owner's-owner walk that skips PAST dead
  intermediates, feeding the ladder's rung-2 skip-level target and the dead-upstream grandparent
  signal). `derive_signal_owner`'s existing one-hop behavior is UNCHANGED — the locked
  `test_no_layer_is_addressed_its_grandchildren_noise` still asserts it. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T14:25+02:00 — 260707-HFX2-L1: created for R4 hierarchical routing derivation (worker
  -> manager, manager -> orchestrator, decision-item -> architect). Verification metadata pinned
  until closeout stamps the 260707-HFX2-L1 commit.
