# mcp/src/agents_remember/application/knowledge_worklist/unexplained.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R10's unexplained changes, inside the worklist run.** If the closeout gate covered only code that
already has knowledge, new code would never enter the graph (Doc11, D8). This module makes every change the
gate linkage (MIK-R08 definition 8) leaves unlinked an item that needs an authored disposition. It registers
the `unexplained_hunk` and `unexplained_file` item kinds in MIK-R08's registry, owns the **coverage lookup**
(rule 1), raises one item per unlinked hunk or non-text change in every changed file (covered or not), and
binds the uncovered ones to MIK-R30's onboarding trace after the leaf route has computed it.
`compute._Run.document` calls `unexplained_items` as step 7 of every run; `leaf._settled_unexplained` calls
`settle_uncovered` after `worklist_onboarding`. The satisfying rule itself lives in the model module
`models/knowledge_files/unexplained.py`, so the worklist's `satisfiedBy` and the gate's predicate (MIK-R09,
L09) are one function.

## Code Commentary

### Logic

- **Registration (rule 2).** Both kinds are `register_item_kind(ItemKind(...))` at import, owner `MIK-R10`,
  with the one satisfying-row text `_SATISFYING_ROW` naming every answer and the coverage split.
  - `unexplained_hunk`: subject `hunk:<path>@<base lines>..<candidate lines>`, each side `sha256:<hex>` of the
    hunk's changed lines (`range_bytes` then `content_identity`) or `absent` for a side with no changed line.
    Facts: `path`, `hunks`, `changedLines`, `deleteOnly`, `coverage`, `admits`, `row`. Its `row_lookup`
    (`_hunk_row`) finds the leaf's row `hunk:<item id>`.
  - `unexplained_file`: subject `file:<path>@<C-side object>` (`@absent` when C lacks the path), so a second,
    different change to the same path in the same leaf opens a new item. Facts: `path`, `blob`, `baseBlob`,
    `status`, `content`, `modeChange`, `coverage`, `admits`.
  - The package `__init__` imports the module, so the kinds are registered whenever the worklist is.
- **Coverage (rule 1, `RouteCoverage`, `route_coverage`, `_coverage`).** A path is `covered` when K_B holds a
  `RealizationEntry` at it (proofs do not count), or when its governing onboarding route has migration status
  `migrated`. The governing route is MIK-R30's `nearest_governing_route` over K_B's `onboarding/**/overview.md`
  directories (MIK-R21 rule 1); its status is L20's `governing_status` over every census of K_B (the latest
  status entry across all censuses; none means `pending`). The fact records `state`, `realizationEntries`,
  `route`, `routeStatus` and the deciding `census`. Coverage is read **at K_B** (ruling Q4): nothing the leaf
  writes changes which record answers its items. An unreadable census raises `CoverageUnreadable`, and the
  leaf route turns that into an `incomplete` run naming K_B.
- **Raising (`_Collector`, `unexplained_items`).** For each `changes[]` entry: a non-text change whose
  `fileLevel` is not linked gives one file item; each hunk not `linked` gives a hunk item. Hunks of one path
  with identical changed lines on both sides share one subject, and that item lists every occurrence in
  `facts.hunks` (ruling Q4). Coverage is a fact, never part of the ID, so a route that turns `migrated` keeps
  every item ID. A symlink's or submodule's object comes from its C tree entry (`_object`, ruling Q4). A
  blob that cannot be read, and (after review N5) a hunk whose changed lines lie outside its own blob, raise
  `CodeReadError`, so the run is `incomplete` rather than inventing an `absent` side (`_identity`).
- **What each item admits (`_admits`).** Uncovered: `onboarding_trace`. Covered with lines at C: `attach`,
  `author`, `no_invariant`. Covered and delete-only, or a file C no longer holds: only `no_invariant`
  (rule 4). `admits` is a fact only; nothing is suggested or written (Exclusions).
- **Attach and author answer by linkage.** An entry the curator adds over the change links the hunk, so the
  item is simply not raised on the next run; the new entry raises `touched_invariant` (answered by
  `extended`) or, for a new invariant, nothing (MIK-R08 definition 7). A delete-only hunk has no line at C, so
  no new entry can link it (the `hunk.new_count > 0` condition in `compute._Run._change`, ruling Q1/Q2).
- **Answers and unnecessary rows (`_finished`, rulings Q4 and 03:24:28 N2).** `satisfiedBy` is computed with
  `unexplained_satisfied_by` over the leaf's history rows in K_C. The **answering set is built from covered
  items only**: a `no_invariant` row about an uncovered item satisfies nothing (rule 5) and is listed in
  `unexplained.unnecessaryRows`, report-only, like any `no_invariant` row that answers no raised item.
- **Uncovered items take the onboarding trace (`settle_uncovered`, `_settled`).** The run first records the
  trace subject `onboarding:<path>` with no counted change (only that row can answer). After the leaf route
  adds MIK-R30's own items, each uncovered item bound to an `onboarding_trace` item for its file takes that
  item's ID, counted change, unreadable-sidecar flag and answer, so a card changed in the leaf satisfies it.
  The caller recomputes the digest.
- **`answering_trace_subjects` (ruling Q3).** The `onboarding:<path>` subjects that answer uncovered items.
  MIK-R30 raises no card item for a card-less path, so its report would call the leaf's row about that path
  unnecessary; the leaf route and the memory-quality controller drop exactly these subjects from that report.
  An onboarding row that answers an unexplained item is therefore never reported as unnecessary.
- **`open_count`** counts unexplained items with no `satisfiedBy`; the summary (`itemsByKind`, `openCount`,
  `unnecessaryRows`) is the document's `unexplained` key.

### Conventions

- Producer facts and curator decisions stay separate (Preservation Boundary): every fact is mechanical, and
  every answer is an authored row or entry.
- MIK-R30's items are read, never changed (Preservation Boundary: the onboarding trace for uncovered files).
- Complexity: every function scores at most 10 (radon; the standing bar, ruling 03:24:28 N1).

### Invariants And Boundaries

- **Every changed hunk in range is either explained by a knowledge change or answered by an explicit
  disposition; an unexplained hunk keeps its worklist item open.** Candidate invariant; realized by
  `unexplained_items` over the run's `changes[]` linkage and `unexplained_satisfied_by`; proved by
  `test_a_covered_hunk_is_answered_by_no_invariant_attach_or_author_and_never_by_onboarding` and the
  real-data run on ICR L47 (160 items; `openCount` 0 only after the attach and 22 rows). Enforcement is
  MIK-R09's (L09).
- **A delete-only hunk can be answered only by a disposition, never by attach or author.** Candidate
  invariant; realized by the `new_count > 0` linkage condition in `compute._Run._change` and `_admits`;
  proved by `test_a_delete_only_hunk_admits_only_no_invariant` (a line-range attach around the deletion
  point leaves the same item open) and the reviewer's real `changeSetBar.tsx` comparison.
- **`no_invariant` answers only covered items; a row about an uncovered item is reported unnecessary and
  closes nothing.** Candidate invariant; realized by the covered-only answering set in `unexplained_items`
  and the coverage split in `unexplained_satisfied_by`; proved by
  `test_an_uncovered_new_file_is_satisfied_by_its_onboarding_trace` and the reviewer's R2 real probe
  (`ROW-RSSPD7` listed, `openCount` unchanged).
- **An onboarding row that answers an uncovered item is never reported as unnecessary.** Realized by
  `answering_trace_subjects`; proved by
  `test_an_onboarding_row_that_answers_an_uncovered_item_is_not_reported_unnecessary`.
- **Item IDs depend only on the changed lines** (rule 6): an edit elsewhere never reopens an answered item,
  and a coverage flip keeps every ID. Proved by `test_an_edit_elsewhere_in_the_file_never_reopens_an_answered_item`
  and the real w1 to w4 runs.
- **Unconverted memory reads are unchanged.** An unconverted leaf gets no worklist (MIK-R08 applicability:
  `leaf._sides` returns `None` before any coverage read), so no unexplained item exists on today's production
  leaves; the base and worktree builds both return `None` on the real unconverted pair.

### Todos

- **L09:** the gate applies `unexplained_item_open(item, rows_by_subject)` to the stored item. Carried note
  (ruling 03:24:28 N3): an insertion-only hunk can still be linked by a K_B range through `hits_old`'s
  "strictly inside" rule; the symmetric strict reading was not applied here.
- **Resolved by MIK-L31 and MIK-L32:** item volume is by design (160 on ICR L47). L31 groups the unexplained items
  in the reviewer's panel by file and coverage state (`dashboard/src/panels/review/worklistGroups.ts`,
  `UnexplainedGroups`), and L32's unexplained-changes lane shows an opened file's groups beside its own
  classification (`LaneFileFocus.tsx`), for display only (ruling Q4).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R10@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings of 2026-09-30T01:56:39 and 03:24:28 in
the task's leaf document `10_unexplained-change-disposition.json`) and the coordination-root note Doc14;
they live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: registration, what is raised, coverage and satisfaction. [1]
- The one satisfying-row text over both kinds and the coverage split. [2]
- A hunk item's row is found by its item ID. [3]
- Both kinds registered on import with their facts and owner. [4]
- An unreadable census makes coverage undecidable. [5]
- The governing route and its latest census status. [6]
- The route half of coverage over one memory tree. [7]
- Covered by a realization entry in K_B or a migrated route. [8]
- The summary under the document's `unexplained` key. [9]
- A side's identity; an out-of-range read is a named problem. [10]
- What an item admits. [11]
- Unlinked hunks and non-text changes collected; identical lines share a subject. [12]
- A symlink's or submodule's object from its tree entry. [13]
- The file item bound to its C-side object. [14]
- The ID, row subject, trace fact and `satisfiedBy`. [15]
- The answering set from covered items only; stray `no_invariant` rows are unnecessary. [16]
- Uncovered items bound to MIK-R30's item for their file. [17]
- The onboarding subjects an uncovered item needs. [18]
- Open unexplained items. [19]
- Step 7 of the run: the items join the one sorted list. [20]
- A delete-only hunk is linked only by a K_B range; since MIK-R09 an insertion-only hunk is linked only by a K_C range (the symmetric correction L10's N3 carried to L09), which can only add `unexplained_hunk` items. [21]
- The leaf route settles uncovered items after the onboarding trace. [22]
- Covered hunk: no_invariant, attach or author; never onboarding. [23]
- Delete-only hunk: only no_invariant. [24]
- An uncovered file: its onboarding trace; its no_invariant row is unnecessary. [25]

### Cross-Repo References

No meaningful cross-repo references found: the module reads the run's linkage, the parsed memory sides and
one code repository's trees, handed to it by the worklist run.

No cross-repo boundary is crossed by this file.
