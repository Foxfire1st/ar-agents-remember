# mcp/tests/test_unexplained_change_disposition.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R10@v2 cases (historical collection: 10): every unexplained change needs an authored disposition.** The worklist
cases reuse MIK-R08's real Git code and converted memory repositories (`test_knowledge_worklist.World`):
`pkg/review.py` carries four realization entries in K_B, so it is *covered*; a new file is covered only when
its governing onboarding route is `migrated`. The curator's answers go through the real writer, and every run
checks that `application/knowledge_gate/predicates.unexplained_row_open` over a parsed history and
`GateContext` agrees with the worklist's stored `satisfiedBy`. This card describes current source
assertions; no collection or test execution was performed for this inspection.

## Code Commentary

The added updated-card/no-separate-trace-item case writes an actual card change and an updated source-bound row through the ordinary fixture writer, settles an uncovered hunk with item=None, then requires both the worklist's satisfiedBy and the gate predicate to accept that same row with countedChange=True. It is the discrepancy regression, not permission to relabel updated as no_impact or satisfy a hunk by a bare counted edit.


### Logic

- **Helpers.** `world` builds MIK-R08's fixture; `unexplained` returns items by subject **after**
  parsing `HistoryFile` from the captured K_C location and building `GateContext` to compare
  `unexplained_row_open` with each stored answer. `_rows` remains a pure row-ID map helper for cases
  that need it, not the currency-owning gate. `written`/`write` use the writer as leaf
  `260928-MIK-L99`; `no_invariant` builds a
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
  - covered-hunk currentness (rule 6): an edit elsewhere keeps that hunk's ID and `no_invariant`
    answer; editing the lines themselves gives a new open ID and lists the old row as unnecessary.
    This is not permanent currentness for source-bound onboarding rows after another source edit;
  - review N6: a symlink's subject is `file:pkg/link@<C tree object>`, covered through the migrated route; a
    deleted binary is `file:pkg/extra.bin@absent`, admitting only `no_invariant`; an uncovered delete-only hunk
    admits `onboarding_trace`. The directly committed history supplies explicit onboarding
    `sources` using the candidate blob; a sourceless row in an open file answers nothing. With
    the right rows, the source asserts all three items are answered;
  - an uncovered new file (rule 5, boundary example): the initial `onboardingTrace` includes
    `sourceBlobs`; a `no_invariant` row leaves it open and is listed unnecessary. Writing the card
    still leaves `satisfiedBy` null. The fixture then authors a source-bound onboarding row and
    asserts that its `row.id`, not `counted-change`, settles the unchanged item ID. This is a
    source assertion, not instructions to create a changed-card no_impact/backfill row for L53;
  - the writer's refusals: an attach to an absent invariant, an attach to a **retired** invariant, a blank
    reason, `covers` on the row, and a disposition other than `no_invariant`;
  - ruling Q3: an `onboarding:` row that answers a card-less uncovered file is not reported unnecessary (the
    persisted `unnecessaryRows` and `_needed_rows_dropped` keep only the stray row; the response count drops
    from 2 to 1). The direct trace-result call now forwards
    `code_blobs=worktree_code_blobs(world.code, [FRESH])` instead of relying on row presence.

- The new uncovered-file regression writes an actual updated row over a changed card in the Git fixture, settles an item without a separate trace item, and asserts both the worklist row ID and the gate acceptance read countedChange=true. A card edit alone still supplies no authored answer; this is source-level test intent, not execution by this Curator.

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
  current source-bound gate predicate agrees with `satisfiedBy`, not merely the low-level row-ID
  lookup. A counted edit alone is no ordinary candidate answer; unchanged-contract judgments and
  real card updates follow their distinct current-row eligibility rules.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R10@v2` of task `260928_maintained-invariant-knowledge`, outside the code and memory repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The module docstring: the reused worklist world and the predicate check. [1]

- Registration and the row model's refusals. [3]
- Coverage by entries or the latest census status. [4]
- The three answers of a covered hunk; never onboarding. [5]
- Delete-only: only no_invariant. [6]
- Non-text changes bound to the C blob. [7]
- The writer's refusals, including a retired invariant. [11]




> Retained earlier citation wording: - The unit-lane row. Source caption: "mcp/tests/test_unexplained_change_disposition.py"






> Retained earlier citation wording: - The catalog consumer row.



### Cross-Repo References

No meaningful cross-repo references found: the cases build their own temporary code and memory repositories.

No cross-repo boundary is crossed by this file.

- The items are checked against `predicates.unexplained_row_open` using parsed HistoryFile/GateContext, not just `unexplained_item_open` row-ID lookup. [2]
- An edit elsewhere preserves the covered hunk's no_invariant answer, not the currency of every source-bound onboarding judgment. [8]
- Symlink, deleted binary and uncovered deletion (review N6): the direct onboarding row explicitly binds candidate source blobs. [9]
- The uncovered-file source assertions keep the item open after card creation and settle it only with the authored source-bound row ID; no counted-change-only answer remains. [10]
- An answering onboarding row is not unnecessary (Q3); the trace-result call supplies the candidate code_blobs map before filtering and adjusted-count assertions. [12]
- Current source delta inspected statically: Replace counted-edit settlement and helper owner, show explicit blobs, narrow hunk stability and fix captions; prior blocked advice is superseded. [15]

## Current counted-change evidence


- The changed-card regression asserts worklist/gate agreement for an authored updated row without a separately bound trace item; source assertions are not fresh execution acceptance. [16]












- The unit-lane row. Source caption: "mcp/tests/test_unexplained_change_disposition.py" [13]


- The catalog consumer row.

Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:1920-1920 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted [14]

## Retirements

- Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:1920-1920 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.