# mcp/tests/test_escalation_ladder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_escalation_ladder.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T23:15+02:00                     |
| lastVerifiedCommitHash | `69314ba144d9461a0daec43f1d1aa5ce1ab18946` |
| lastVerifiedCommitDate | 2026-07-08T09:40:32+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Unit tests for the escalation ladder walker (`controlplane/escalation_ladder.py`, 260707-HFX2-L4
R2/R3) and the orphan-detection hook (`controlplane/orphan_policy.py`, R3) — pure-function coverage
with no supervisor-sweep scaffolding.

## Code Commentary

### Logic

Four test classes:

- **`RungDueTests`** — `rung_due`'s anchor/threshold logic: rung 0 anchors at `createdAt` and uses
  `sla_seconds`; a later rung anchors at `escalatedAt` and uses `rung_seconds`; a `consumed` row
  never fires regardless of how far past any threshold; a row already at `MAX_RUNG` never advances
  further even with a trivially-small threshold.
- **`NextStepTests`** — `next_step`'s per-rung routing: rung 1 renudges the row's own mailbox
  address; rung 2 skip-levels to the owner's owner via a seeded three-tier catalog chain
  (orchestrator/manager/worker); `test_rung_two_with_no_further_owner_jumps_straight_to_developer`
  is the hierarchy-ceiling case — a manager-addressed row's "owner's owner" resolves to nothing (the
  orchestrator has no further owner), so the walker jumps straight to rung 3 rather than stalling;
  rung 3 and any rung at/past `MAX_RUNG` both resolve to the terminal `developer-attention` action.
- **`SeatSuspectTests`** — `seat_is_suspect`'s liveness gate: `None` agent id never suspect; an
  unknown/dead catalog entry ("ghost") is suspect; a `turn_state == "stale"` row past
  `stale_seconds` is suspect, one still inside the grace window is not; a live non-stale seat is
  never suspect.
- **`OrphanPolicyTests`** — `find_orphaned_workers` returns only the RUNNING workers spawned by the
  named manager, excluding a terminated sibling worker and another manager's worker.

`_entry(**overrides)` and `_catalog_entry(session_id, **overrides)` are the shared fixture builders
layering overrides onto a base inbox-entry / catalog-entry dict, matching the project's existing
`_upsert`/`_entry` fixture convention used across the terminal-catalog and supervisor test modules.

### Conventions

`unittest.TestCase` per concern, temp-rooted `TerminalCatalog` per test class needing one (`setUp` +
`addCleanup`), `NOW`/`T0` shared fixed-clock constants matching the project's existing
`datetime(..., tzinfo=UTC)` convention.

### Invariants And Boundaries

- No test touches a real coordination root or a real supervisor sweep — every catalog is
  temp-rooted and every entry is a fixture-built `OperatorInboxEntry`/`TerminalCatalogEntry`.
- The hierarchy-ceiling jump (`test_rung_two_with_no_further_owner_jumps_straight_to_developer`) is
  the regression a naive "always walk exactly 2 hops" rung-2 implementation would fail — any future
  change to `next_step`'s rung-2 branch must preserve this fallback.
- `OrphanPolicyTests` is deliberately narrow (detection only) — it does not and should not assert
  any re-parent side effect, since none exists in this module.

### Todos

None.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation; this is a
same-repository unit-test suite for internal control-plane plumbing with no external spec — the
leaf task doc (R2/R3/R6) is the source of truth this suite pins.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines the ladder/orphan-policy behavior under test; the leaf task doc is authoritative. | L1-L207 | [test_escalation_ladder.py](test_escalation_ladder.py) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module under test: rung-due dwell logic, per-rung routing, and seat-suspect liveness. | whole module | [../src/agents_remember/controlplane/escalation_ladder.py](../src/agents_remember/controlplane/escalation_ladder.py.md) |
| The orphan-detection hook under test. | `find_orphaned_workers` | [../src/agents_remember/controlplane/orphan_policy.py](../src/agents_remember/controlplane/orphan_policy.py.md) |
| The catalog entry fixture fields (`spawn_role`/`spawned_by_session`/`turn_state`) this suite seeds. | `TerminalCatalogEntry` | [../src/agents_remember/serving/terminal_catalog.py](../src/agents_remember/serving/terminal_catalog.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository unit-test suite only. | — | — |

## Update History

- 2026-07-08T23:15+02:00 — Created for 260707-HFX2-L4 (R2/R3/R6): four test classes —
  `RungDueTests` (anchor/threshold/ceiling), `NextStepTests` (per-rung routing including the
  hierarchy-ceiling jump-to-developer fallback), `SeatSuspectTests` (liveness/staleness gating), and
  `OrphanPolicyTests` (running-workers-of-one-manager detection). Verification metadata pinned
  until closeout stamps the 260707-HFX2-L4 commit.
