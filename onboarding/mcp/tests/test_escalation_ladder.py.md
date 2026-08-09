# mcp/tests/test_escalation_ladder.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_escalation_ladder.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-09T06:48+02:00                     |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840` |
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

Unit tests for the escalation ladder walker (`controlplane/escalation_ladder.py`, 260707-HFX2-L4
R2/R3) and the orphan-detection hook (`controlplane/orphan_policy.py`, R3) — pure-function coverage
with no supervisor-sweep scaffolding.

## Code Commentary

### 260707-HFX2-L13 Floor Regression

The later-rung test now reproduces the live stale-anchor shape: an hour-old `escalatedAt` plus a
two-minute-old `rungTransitionAt` is not due, and becomes due only when the independent five-minute
floor expires. Existing SLA/configured-dwell tests continue to prove rung-zero and longer settings
authority.

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
  **260713-TES-L4 (R13):** `test_rung_three_lands_on_the_live_architect_seat` now seeds the
  architect with the row's master-scoped `leaf_key` and passes a `leafKey`-carrying entry, so the
  terminal rung resolves through the scoped `derive_architect_owner(catalog, leaf_key=...)`
  (never global first-match).
- **`SeatSuspectTests`** — `seat_is_suspect`'s liveness gate: `None` agent id never suspect; an
  unknown/dead catalog entry ("ghost") is suspect; a `turn_state == "stale"` row past
  `stale_seconds` is suspect, one still inside the grace window is not; a live non-stale seat is
  never suspect.
- **`OrphanPolicyTests`** — `find_orphaned_workers` returns only the RUNNING workers spawned by the
  named manager, excluding a terminated sibling worker and another manager's worker.

`_entry(*, agent_id=..., recipient_role=...)` is a keyword-only inbox-entry builder that calls
`create_operator_inbox_entry` directly through the `InboxMessage`, `InboxRouting`/`InboxAddress`, and
`InboxPoster` parameter objects. It exposes only the two fields the ladder tests vary and leaves every
other variation (`rung`, `state`, timestamps) to `.model_copy(update=...)` at the call site.
`_catalog_entry(session_id, **overrides)` remains the override-layering fixture builder over a base
catalog-entry dict, matching the project's existing `_upsert`/`_entry` fixture convention used across
the terminal-catalog and supervisor test modules.

### Conventions

`unittest.TestCase` per concern, temp-rooted `TerminalCatalog` per test class needing one (`setUp` +
`addCleanup`), `NOW`/`T0` shared fixed-clock constants matching the project's existing
`datetime(..., tzinfo=UTC)` convention.

### Invariants And Boundaries

- No test touches a real coordination root or a real agent-notifier sweep — every catalog is
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No external/domain document defines the ladder/orphan-policy behavior under test; the leaf task doc is authoritative. | `RungDueTests` | mcp/tests/test_escalation_ladder.py:68-110 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test: rung-due dwell logic, per-rung routing, and seat-suspect liveness. | "def next_step(" | mcp/src/agents_remember/controlplane/escalation_ladder.py:123-123 |
| The orphan-detection hook under test. | `find_orphaned_workers` | mcp/src/agents_remember/controlplane/orphan_policy.py:18-30 |
| The catalog entry fixture fields (`spawn_role`/`spawned_by_session`/`turn_state`) this suite seeds. | `TerminalCatalogEntry` | mcp/src/agents_remember/serving/terminal_catalog.py:80-510 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository unit-test suite only. | — | — |

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded the scoped-architect rung-3 fixture
  (master-scoped `leaf_key` seeding; R13 scoped custody, no global first-match). Verification
  metadata pinned until closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.


- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: `_entry` stopped being a `**overrides`
  dict-layering builder and is now keyword-only over `agent_id`/`recipient_role`, calling
  `create_operator_inbox_entry` through the new `InboxMessage`, `InboxRouting`, `InboxAddress`, and
  `InboxPoster` parameter objects. Rewrote the fixture-builder paragraph in Logic to describe that
  shape and to keep `_catalog_entry` documented as the remaining override-layering builder. The rest
  of the diff is `ruff format` rewrapping; the four test classes and their assertions are untouched.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 round 2: added the stale-anchor regression for the
  redundant five-minute later-rung floor. Verification metadata remains pinned until closeout stamps
  the eventual L13 code commit.

- 2026-07-08T23:15+02:00 — Created for 260707-HFX2-L4 (R2/R3/R6): four test classes —
  `RungDueTests` (anchor/threshold/ceiling), `NextStepTests` (per-rung routing including the
  hierarchy-ceiling jump-to-developer fallback), `SeatSuspectTests` (liveness/staleness gating), and
  `OrphanPolicyTests` (running-workers-of-one-manager detection). Verification metadata pinned
  until closeout stamps the 260707-HFX2-L4 commit.
