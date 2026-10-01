# mcp/tests/test_unexplained_change_disposition.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R10@v2 cases (10 collected): every unexplained change needs an authored disposition.** The worklist
cases reuse MIK-R08's real Git code and converted memory repositories (`test_knowledge_worklist.World`):
`pkg/review.py` carries four realization entries in K_B, so it is *covered*; a new file is covered only when
its governing onboarding route is `migrated`. The curator's answers go through the real writer, and every run
checks that the stored-item predicate the gate uses (`unexplained_item_open`) agrees with the worklist's own
`satisfiedBy`.

## Code Commentary

### Logic

- **Helpers.** `world` builds MIK-R08's fixture; `unexplained` returns the run's items by subject **after**
  asserting the predicate agreement on each; `_rows` reads the leaf's history file from the K_C working tree
  the run captured; `written`/`write` run the real writer as leaf `260928-MIK-L99`; `no_invariant` builds a
  row whose default reason is literally "logging-only helper" (the packet's conforming example); `attach`
  builds an entry on a stored invariant; `_census` writes a census with one route status.
- **Cases, by rule:**
  - registration and the row (rule 2, rule 3, the blank-reason failure): both kinds registered with owner
    `MIK-R10`; `no_invariant` is the only row disposition; a blank reason, `covers` and a malformed subject
    are refused by the model;
  - coverage, both conditions (rule 1): realization entries in K_B; then a route `pending`, `migrated` in
    `wave-1`, a later `in_progress` in `wave-2` (uncovered again: the latest status wins), and an unreadable
    census (the run is `incomplete`, naming K_B);
  - a covered hunk: answered by a `no_invariant` row, by an attach (then `touched_invariant` with `added`), or
    by an authored invariant (no item at all), and **never** by an `onboarding:` row (the non-conforming
    example);
  - a delete-only hunk (rule 4, ruling Q1): `admits` is only `no_invariant`; a line-range attach around the
    deletion point leaves the same item open and the hunk unlinked; a `no_invariant` row answers it;
  - a non-text change: a mode change and a new binary open `file:` items bound to the C blob; a second,
    different binary change opens a new subject;
  - currentness (rule 6): an edit elsewhere keeps the ID and the answer; editing the lines themselves gives a
    new, open ID, and the old row is listed as unnecessary;
  - review N6: a symlink's subject is `file:pkg/link@<C tree object>`, covered through the migrated route; a
    deleted binary is `file:pkg/extra.bin@absent`, admitting only `no_invariant`; an uncovered delete-only hunk
    admits `onboarding_trace`. A committed history file answers all three;
  - an uncovered new file (rule 5, boundary example): open, then a `no_invariant` row does not answer it and is
    listed in `unexplained.unnecessaryRows` (ruling 03:24:28 N2), then writing its card gives `counted-change`;
  - the writer's refusals: an attach to an absent invariant, an attach to a **retired** invariant, a blank
    reason, `covers` on the row, and a disposition other than `no_invariant`;
  - ruling Q3: an `onboarding:` row that answers a card-less uncovered file is not reported unnecessary (the
    persisted `unnecessaryRows` and `_needed_rows_dropped` keep only the stray row; the response count drops
    from 2 to 1).

### Conventions

- The module is in the `unit-regression` lane (`test-evidence-lanes.toml:124`); the evidence catalog derives it
  as a consumer of `fixtures/repository_profiles/node/package-lock.json` (the Fortieth re-pin, `449b69ef`).
- Reviewer R2-1 (low, non-blocking): the N6 case commits its rows directly, so the writer's
  `file_subject_mismatch` has no unit assertion for a symlink object or an `@absent` subject; the reviewer
  verified both by a probe.

### Invariants And Boundaries

- Proves the four candidate invariants recorded on
  `application/knowledge_worklist/unexplained.py.md`: every unlinked hunk keeps an item open until answered; a
  delete-only hunk takes only a disposition; `no_invariant` answers only covered items; and the stored
  predicate agrees with `satisfiedBy`.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R10@v2` of task `260928_maintained-invariant-knowledge`, outside the code and memory repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: the reused worklist world and the predicate check. [1]
- The items, checked against the gate's predicate. [2]
- Registration and the row model's refusals. [3]
- Coverage by entries or the latest census status. [4]
- The three answers of a covered hunk; never onboarding. [5]
- Delete-only: only no_invariant. [6]
- Non-text changes bound to the C blob. [7]
- An edit elsewhere never reopens. [8]
- Symlink, deleted binary and uncovered deletion (review N6). [9]
- An uncovered new file and its onboarding trace. [10]
- The writer's refusals, including a retired invariant. [11]
- An answering onboarding row is not unnecessary (Q3). [12]
- The unit-lane row. [13]
- The catalog consumer row. [14]

### Cross-Repo References

No meaningful cross-repo references found: the cases build their own temporary code and memory repositories.

No cross-repo boundary is crossed by this file.
