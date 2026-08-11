# mcp/src/agents_remember/serving/_agent_notifier_evaluation.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/_agent_notifier_evaluation.py`                                        |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T20:28+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                                        |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

[None](None)

## Purpose

Evaluates mechanical agent-notifier findings from current catalog, topology, inbox, deadline, and
pane evidence without performing mutations.

## Code Commentary

### Logic

Rebind evaluation detects pending rows whose private occupant correlation is dead and derives the
current owner from task-document containment. Pending expiry, liveness, dead-upstream, inbox, and
pane predicates remain evidence-only. The combined evaluator passes one topology authority through
the structural finding families.

### Conventions

Evaluation returns typed findings; actions, persistence, and delivery are separate. Predicate
helpers accept the `TaskHierarchy` protocol, while the production composition constructs
`TaskDocumentTopology`; tests and other callers can supply an existing hierarchy authority without
requiring the concrete filesystem topology type.

### Invariants And Boundaries

- Owner rebinding never uses spawn ancestry or global role fallback.
- Ambiguous structural owners fail instead of first-match routing.
- Model output/artifact judgment is not a notifier predicate.
- Evaluation itself performs no durable write.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rebind findings use structural owner derivation and dead correlations. | `evaluate_rebind_findings` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:130-177 |
| The combined evaluator threads task hierarchy through all relevant predicates. | `evaluate_predicates` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:349-403 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: recorded the protocol-typed
  hierarchy seam accepted by notifier predicates; production behavior remains the same concrete
  `TaskDocumentTopology` composition.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `_agent_notifier_evaluation.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: No content impact: re-read the current staged agent-notifier evaluation body after the supervisor rename and predicate removal; the sidecar remains accurate. Verification metadata remains pinned until closeout.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the predicate demolition
  (expectation/escalation/ladder-terminal predicates deleted) and the `escalationBudget`
  load-shed wiring in `evaluate_predicates` (owner-signal findings capped per sweep, twin of
  `redeliverBudget`). Superseded the L2/L4 expectation-kind and dormant-ladder prose.
  Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the N14 rebind predicates
  (`_row_target_dead`, `_row_dead_since`, `evaluate_rebind_findings`,
  `REBIND_GRACE_SECONDS=300.0`, dispatch-brief exclusion), the §9 pending-expiry predicate
  (`evaluate_pending_expiry_findings`, `inbox-ttl-expired`), the `ack-by` retirement in
  `_INACTIVE_EXPECTATION_KINDS`, and the removal of ladder/escalation predicate composition
  from `evaluate_predicates` (dormant ladder, N3) plus the dead-target redeliverable-budget
  exclusion. Verification metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: recorded the compound-idle predicate
  composition in `evaluate_predicates` (state-signal → compound-idle → non-reaction →
  boundary-drain). Verification metadata pinned until closeout stamps the 260713-TES-L3
  commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the relay predicate composition,
  `_INACTIVE_EXPECTATION_KINDS = {verdict-by, ack-by}`, the retired turn-report predicates, and
  the held/landed state-signal exclusions. Verification metadata pinned until closeout stamps
  the 260713-TES-L2 commit.
- 2026-08-08T21:20+02:00 — 260713-TES-L1 curator: moved this card to the renamed module path; recorded `SEAT_LIVENESS_ASK_PREFIXES` + `_seat_liveness_ask_identity` (fix round 1, reviewer F1) and the legacy+current createdBy/prefix acceptance in the chain-progress predicate. Verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
