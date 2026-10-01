# mcp/tests/test_task_reopen.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks reopen resets the exact contract, leaf document and parent row to planning while preserving the leaf identity and recording the decision. An injected contract-publication failure rolls back document and landing changes. The same module also carries the **series** half: one gathered case drives the terminal atomic-series reopen and, through two plain helper methods, the two other arrivals at the same publication — the series that is already live at a collected address, and the reset that was interrupted before its successor generation was published. Deleted guard/start/abandon companion suites are not claimed as current tests here. Since 260928-MIK-L38 the leaf half also pins how reopen finds a leaf's master (MIK-R38's one rule) and that it refuses a leaf or master the store would write to another file.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

`SeriesReopenTests` is deliberately **one collected subject told from all of its arrivals**. The
collected case drives the terminal series: the reset of the contract cells, the master document and
the enclosure generation, with the fixture asserting up front that the cleanup really did retire the
integration branch, because a re-cut of a branch that still exists would be measuring the wrong
thing. Its two helper methods are plain (not `test_*`) on purpose: both pytest lanes sit at exactly
their case budget, and one added collected case makes the lane run **zero** tests rather than one
more. They are called from inside the collected case, so they still execute — a plain method is a
budget fact here, not a claim that the scenario is unverified.

The three facts the gathered subject pins are the three ways a series reaches the publication:

- **`advance`** — a series that is in flight (neither closeout nor integration completed) may stand
  strictly ahead of its source *on the same line*. That branch is the series' own landed work, so it
  is reported as `advance` and never moved; a diverged or lagging branch keeps its refusal.
- **`publish`** — a series already live at an address whose generation is `terminal-archived`, with
  closeout and integration untouched, is re-addressed rather than refused: the successor generation
  is published and the branch is left exactly where the series put it.
- **the counter** — the completion's spent review rounds (`round: 3` in the fixture) are cleared to
  `0`, not pending, no baseline or residual, no developer approval and no additional rounds, so the
  next round reads as the first instead of the fourth.

**The MIK-R38 cases in `ReopenResetTests`** (integration lane, ruling 2026-09-30T12:33:07 Q1):
- an unnamed `subTask` leaf still finds its folder master through the shared helper: `reopen_task` returns
  `masterIndex: reset` and the row goes back to `planning` (ruling Q2; passes on base, which is the preservation);
- a `light` document that is itself the folder's `task.json` is not its own master: `_plan_master_index_reset`
  returns `(None, "no-master")`. It calls the planner directly because `reopen_task`'s integration-branch preflight
  refuses a leaf contract whose folder has no master before the planner runs (it fails on base, which resolved the
  document to itself and refused it as not a master);
- a hand-made `light` leaf `01_demo-leaf.json` listed by the master, which the store would write as `task.json`, is
  refused `blocked` with "would be rewritten to" and the contract, leaf, `task.json` and `task.md` bytes unchanged
  (review R1 finding 1; base crashed with `duplicate task document write target`);
- a leaf naming a hand-made master `other.json` is refused the same way, with the series master unchanged (ruling
  13:35:32; base overwrote the series `task.json`).

These four are collected cases in the integration lane; the case-budget reason the series helpers above give for
being plain methods is of its own time (review R1 found the integration budget has room for them).

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.
The series methods reuse the shared `task_reopen_test_support` fixtures rather than building their
own contract, and each scenario gets its own temporary workspace so the locator state of one cannot
leak into another.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

A branch is only ever read, never moved, by any of these scenarios: the fixture records the landed
commit before the call and asserts the same commit after it. Adding a collected subject to this
module is a cross-lane budget decision, not a local one.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Resets contract doc and master index [1]
- Contract publish failure rolls back docs and landing [2]
- A leaf naming no master resets the row its folder master lists (MIK-R38). [3]
- A light leaf that is the folder's `task.json` is not its own master. [4]
- A leaf the store would write elsewhere is refused before any write. [5]
- A named master the store would write elsewhere is refused before any write. [6]
- The terminal series reopen, gathered as one collected subject across all three of its arrivals. [7]
- The reset that is durable while the locator is still the collected generation is resumed, not refused. [8]
- A series that is already live and unaddressed is re-addressed: the successor is published citing the archived predecessor, the branch is unmoved, and the spent review counter is cleared. [9]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
