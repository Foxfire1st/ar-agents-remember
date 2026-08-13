# mcp/tests/test_judgment_demolition.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_judgment_demolition.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T12:53+02:00 |
| lastVerifiedCommitHash | `a09b906bbf2855c3479b4d3199607ff8689b7d93` |
| lastVerifiedCommitDate | 2026-08-13T13:51:44+02:00|
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
| No external/domain document defines the demolished machinery; the leaf decisions and forcing-suite provenance are authoritative. | `SuspectRespawnDemolitionTests` | mcp/tests/test_judgment_demolition.py:256-299 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The post-demolition actions surface (fact-relay `_FINDING_ACTIONS` only). | `_FINDING_ACTIONS` | mcp/src/agents_remember/serving/_agent_notifier_actions.py:675-686 |
| The post-demolition predicate composition, including the `escalationBudget` load-shed slice. | `evaluate_predicates` | mcp/src/agents_remember/serving/_agent_notifier_evaluation.py:330-380 |
| The fact-only finding/action vocabulary. | `FindingKind`; `ActionKind` | mcp/src/agents_remember/serving/agent_notifier_models.py:26-50 |
| The retired-kind settings surface (fail-loud unknown keys). | `KNOWN_EXPECTATION_KINDS` | mcp/src/agents_remember/kernel/_agentic_settings_core.py:125-125 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository unit-test suite only. | — | — |

## Update History

- 2026-08-13T12:53+02:00 — No content impact: the stabilized package-source scan reads
  `sys.modules["agents_remember"].__file__` after existing submodule imports have loaded the
  package. No bare/direct package import or Ruff configuration exception remains; demolition
  behavior is unchanged. This supersedes the 12:26 import-shape note; provenance stays closeout-owned.

- 2026-08-13T12:26+02:00 — No content impact: the final Ruff-safe form imports
  `agents_remember.__file__` directly as `agents_remember_file` for the unchanged package-source
  scan. Demolition scenarios, constants, fixtures, and assertions are unchanged; verification
  provenance remains closeout-owned.

- 2026-08-13T11:57+02:00 — No content impact: Ruff I001 moved the `agents_remember` import below
  the control-plane, serving, task, and test-support imports. Constants, fixtures, demolition
  scenarios, and assertions are unchanged; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the regression card for `test_judgment_demolition.py` with the source's current task-document, seat-routing, inbox, or lifecycle assertions.
- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: created this sidecar for the new forcing
  suite (26 tests): suspect-respawn, ladder-policy, inferred-nudge, ack-by/turn-report-by
  retirement, landed-never-escalates, and live-chain-shape proofs. Verification metadata
  pinned until closeout stamps the 260713-TES-L5 commit.
