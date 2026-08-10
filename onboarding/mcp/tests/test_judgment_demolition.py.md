# mcp/tests/test_judgment_demolition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_judgment_demolition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T12:08+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The 260713-TES-L5 forcing suite (26 test methods) that pins the judgment demolition: written
RED before the demolition (19 failed / 7 passed against the pre-demolition base), then green
after it (26 passed). It proves the relay has NO suspect-respawn path, NO escalation-ladder
interpretation, NO inferred nudges, NO ack-by/turn-report-by writers, NO expectation
evaluation, and a fact-only live-loop chain shape (worker-done state-signal -> manager,
compound-idle state-signal -> orchestrator, re-sweeps re-emit nothing).

## Code Commentary

### Logic

- `_DemolitionCase` — shared sweep harness: temp-rooted `TerminalCatalog`, inbox store,
  expectation store, event store, heartbeat store, and a landing paster; builds an
  `AgentNotifierContext` with the post-demolition surface (no `nudge_store`, no escalation
  knobs).
- `SuspectRespawnDemolitionTests` — no `_respawn_suspect` on the actions module, no
  `seat_is_suspect` importable, no `escalation_ladder` module, no suspect-retire reason in
  actions source, no `respawnAfterRung` settings surface, and a stale seat stays `running`
  through sweeps (never retired/respawned).
- `LadderPolicyDemolitionTests` — no `rung_due`/`next_step` importable, no `escalation-due`
  finding kind, no `escalate-rung` action kind, no ladder actions registered, no ladder
  transitions, no `orchestration.escalation` settings family, and the sweep never emits an
  `orchestration.escalation.rung` event.
- `InferredNudgeDemolitionTests` — no `_auto_nudge`/`_mark_expectation_missed` functions, no
  `auto-nudge` action kind, and overdue expectation rows produce zero findings/events.
- `AckByRetirementTests` — `ack-by` absent from `KNOWN_EXPECTATION_KINDS` and
  `DEFAULT_EXPECTATION_SLA_SECONDS`, a settings override for it is refused, no source writes
  ack-by rows, and a legacy ack-by row parses and stays silent.
- `TurnReportByRetirementTests` — no source writes turn-report-by rows; a legacy
  turn-report-by row parses and stays silent.
- `LandedRowNeverEscalatesTests` — a landed row stays terminal across sweeps with zero
  findings/actions.
- `LiveChainShapeTests` — worker-done produces one durable state-signal to the manager;
  compound-idle produces one to the orchestrator; re-sweeps re-emit nothing; the event
  vocabulary is facts only (no rung/escalate/respawn/nudge/ladder-resolved events). This is
  the simulation shape of the exit-bar chain; the live proof script
  (`notes/reports/260713-TES-L5-live-chain-proof.py`) remains deployment-blocked.

### Conventions

`unittest.TestCase` per concern, `unittest.mock` patches for the paster, temp-rooted stores,
and the same fixed-clock constants as the sibling notifier suites.

### Invariants And Boundaries

- The suite is the demolition pin: do not re-add any respawn, ladder, or expectation
  evaluation surface without turning these tests red first.
- It proves code-shape and simulation-shape only; the live multi-seat chain proof is the
  separate exit-bar script.

### Todos

None.

## Docs References

No relevant external documentation found after checking the resolved source registry; the
leaf spec, `notes/260713-TES-L5-decisions.md`, and the worker/reviewer reports are the
authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines the demolished machinery; the leaf decisions and forcing-suite provenance are authoritative. | `SuspectRespawnDemolitionTests` | mcp/tests/test_judgment_demolition.py:195-239 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The post-demolition actions surface (fact-relay `_FINDING_ACTIONS` only). | `_FINDING_ACTIONS` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:616-630 |
| The post-demolition predicate composition, including the `escalationBudget` load-shed slice. | `evaluate_predicates` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:330-380 |
| The fact-only finding/action vocabulary. | `FindingKind`; `ActionKind` | mcp/src/agents_remember/serving/agent_notifier_models.py:26-50 |
| The retired-kind settings surface (fail-loud unknown keys). | `KNOWN_EXPECTATION_KINDS` | mcp/src/agents_remember/kernel/_agentic_settings_core.py:128-128 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository unit-test suite only. | — | — |

## Update History

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: created this sidecar for the new forcing
  suite (26 tests): suspect-respawn, ladder-policy, inferred-nudge, ack-by/turn-report-by
  retirement, landed-never-escalates, and live-chain-shape proofs. Verification metadata
  pinned until closeout stamps the 260713-TES-L5 commit.
