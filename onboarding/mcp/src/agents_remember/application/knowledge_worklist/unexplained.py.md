# mcp/src/agents_remember/application/knowledge_worklist/unexplained.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R10's unexplained changes, inside the worklist run.** If the closeout gate covered only code that
already has knowledge, new code would never enter the graph (Doc11, D8). This module makes every change the
gate linkage (MIK-R08 definition 8) leaves unlinked an item that needs an authored disposition. It registers
the `unexplained_hunk` and `unexplained_file` item kinds in MIK-R08's registry, owns the **coverage lookup**
(rule 1), raises unlinked hunk/non-text items after exact generated-copy filtering and equal-change grouping, and
binds the uncovered ones to MIK-R30's onboarding trace after the leaf route has computed it.
`compute._Run.document` calls `unexplained_items` as step 7 of every run; `leaf_completion._settled_unexplained` calls
`settle_uncovered` after `worklist_onboarding`. The satisfying rule itself lives in the model module
`models/knowledge_files/unexplained.py`, so the worklist's `satisfiedBy` and the gate's predicate (MIK-R09,
L09) are one function.

## Code Commentary

### Logic

- **Registration (rule 2).** Both kinds are `register_item_kind(ItemKind(...))` at import, owner `MIK-R10`,
  with the one satisfying-row text `_SATISFYING_ROW` naming every answer and the coverage split.
  - `unexplained_hunk`: subject `hunk:<path>@<base lines>..<candidate lines>`, each side `sha256:<hex>` of the
    hunk's changed lines (`range_bytes` then `content_identity`) or `absent` for a side with no changed line.
    Facts: `path`, `candidateBlob` (the blob at C or `absent`), `hunks`, `changedLines`,
    `deleteOnly`, `coverage`, `admits`, `row`. Its `row_lookup`
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
- **Raising and grouping.** The collector still makes source-content-bound hunk/file identities and deduplicates equal range occurrences. Before the generated-copy filter and before grouping, the changed paths that a dependent record represents are removed from the change list: `dependent_document_paths` over both sides names every document a dependent holds, so a dependent-backed document raises no hunk or file item here, and taking the classification from both sides keeps that through the record's removal and through a document rename. That suppression is not `changed_document` itself: that item is produced separately, from the base dependents whose document this task changes or whose document survives a rename, and a record-only change, a new record or a deleted document raises none. Exact declared generated copies matching their canonical source are omitted; remaining uncovered equal base/candidate changes are grouped under a deterministic representative, preferring an existing card. Group facts retain every member source/base blob and any generated-copy classification. A differing copy remains a real change rather than inheriting equality. Unreadable content still refuses as an incomplete source read; coverage is read at K_B.
- **What each item admits (`_admits`).** Uncovered: `onboarding_trace`. Covered with lines at C: `attach`,
  `author`, `no_invariant`. Covered and delete-only, or a file C no longer holds: only `no_invariant`
  (rule 4). `admits` is a fact only; nothing is suggested or written (Exclusions).
- **Attach and author answer by linkage.** An entry the curator adds over the change links the hunk, so the
  item is simply not raised on the next run; the new entry raises `touched_invariant` (answered by
  `extended`) or, for a new invariant, nothing (MIK-R08 definition 7). A delete-only hunk has no line at C, so
  no new entry can link it (the `hunk.new_count > 0` condition in `linkage._linked`, called by `linkage._Linkage._change`, ruling Q1/Q2).
- **Answers and unnecessary rows (`_finished`, rulings Q4 and 03:24:28 N2).** `satisfiedBy` is computed with
  `unexplained_satisfied_by` over the leaf's history rows in K_C. The **answering set is built from covered
  items only**: a `no_invariant` row about an uncovered item satisfies nothing (rule 5) and is listed in
  `unexplained.unnecessaryRows`, report-only, like any `no_invariant` row that answers no raised item.
- **Uncovered items take the current onboarding trace (`settle_uncovered`, `_settled`, MIK-R53).**
  The initial run records `onboarding:<path>`, `item: None`, the actual counted Markdown/reference
  change from K_B to K_C, and `sourceBlobs` for the path or every member of its equal-change group. `_finished` computes the
  counted change once, stores it through `_trace`, and passes that same stored fact to current-row
  selection, including when no separate onboarding item is raised. Worklist satisfaction and gate
  currency must not disagree. It names only an eligible onboarding row whose `sources` equal that
  blob: `updated` also requires that counted change, while `no_impact` answers the unchanged-contract
  case. A counted edit alone does not answer the ordinary candidate. This initial run lacks closed-file
  provenance and never credits sourceless rows. Once the leaf adds the file's own `onboarding_trace`
  item, settlement copies its ID, counted-change flag, unreadable-sidecar flag, `sourceBlobs` and
  answer (retaining initial source blobs when the trace lacks them); the caller recomputes the digest.
  Frozen sourceless rows are handled by the gate with their own closed-file provenance, not guessed here.
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
- The old L10 Radon-at-most-10 sentence is historical evidence, not a current complexity certification for the extended grouping implementation.

### Invariants And Boundaries

- **Every changed hunk in range is either explained by a knowledge change or answered by an explicit
  disposition; an unexplained hunk keeps its worklist item open.** Candidate invariant; realized by
  `unexplained_items` over the run's `changes[]` linkage and `unexplained_satisfied_by`; proved by
  `test_a_covered_hunk_is_answered_by_no_invariant_attach_or_author_and_never_by_onboarding` and the
  real-data run on ICR L47 (160 items; `openCount` 0 only after the attach and 22 rows). Enforcement is
  MIK-R09's (L09).
- **A delete-only hunk can be answered only by a disposition, never by attach or author.** Candidate
  invariant; realized by the `new_count > 0` condition in `linkage._linked`, called by `linkage._Linkage._change`, and `_admits`;
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
- **Within a selected source/group representative, hunk item content identities depend on the changed lines** (rule 6); coverage is not part of the ID. Equal-copy grouping additionally binds the representative and its full source set.
  An elsewhere edit preserves the hunk ID and covered `no_invariant` answers, as the historical
  `test_an_edit_elsewhere_in_the_file_never_reopens_an_answered_item` and w1–w4 witnesses described.
  It can nevertheless reopen an uncovered item: its onboarding row binds the whole source blob,
  so a later source edit makes that answer stale even when the changed-line identity survives.
- **Both-unconverted applicability is a conditional boundary.** The leaf chooser returns no converted worklist when both sides lack the layout marker; historical pre-cutover runs are not a statement that every current production leaf is unconverted.

### Todos

- **Current gate:** covered items retain the `no_invariant` predicate; `unexplained_row_open` checks
  uncovered items with the file's onboarding-row currency, including source blobs and counted change.
  Historical L09 helper names are not a row-map-only currency check. The former insertion-only K_B-coverage claim (L10 N3) is explicitly retired: `linkage._linked` requires `old_count > 0` for B coverage and `new_count > 0` for C coverage. An insertion-only hunk can link only through K_C; a delete-only hunk can link only through K_B.
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


- Unexplained items retain groups and expose open counts with unnecessary covered rows [9]


- A side's identity; an out-of-range read is a named problem. [10]
- What an item admits. [11]
- Unlinked hunks and non-text changes collected; identical lines share a subject. [12]
- A symlink's or submodule's object from its tree entry. [13]
- The file item bound to its C-side object. [14]
- The answering set from covered items only; stray `no_invariant` rows are unnecessary. [16]
- The onboarding subjects an uncovered item needs. [18]
- Open unexplained items. [19]
- Step 7 of the run: the items join the one sorted list. [20]
- Per-change linkage belongs to linkage._Linkage._change; linkage._linked symmetrically requires changed lines on the side supplying coverage: delete-only B, insertion-only C. [21]

- leaf_completion settles uncovered items after worklist_onboarding and recomputes their digest and unnecessary-row projection. [22]
- Covered hunk: no_invariant, attach or author; never onboarding. [23]
- Delete-only hunk: only no_invariant. [24]
- An uncovered file: its onboarding trace; its no_invariant row is unnecessary. [25]

### Cross-Repo References

No meaningful cross-repo references found: the module reads the run's linkage, the parsed memory sides and
one code repository's trees, handed to it by the worklist run.

No cross-repo boundary is crossed by this file.



- The representative item binds its complete source map, actual counted change and eligible current onboarding row [15]




- Settlement retains complete source maps and the trace item currency without inventing an answer [17]




- Current source-bound trace construction and row admission use the complete blob map [26]



## Current counted-change evidence

- The initial uncovered-item fact and its answer use one actual counted card change; settlement may still replace both from the trace item. A counted edit alone does not answer the item. [27]


## Current generated-copy and grouped-source contract

The generated-copy declaration is an equality test against the candidate, not a waiver based on a folder name. Only proven matching projections disappear before collection. Equal uncovered changes share their chosen representative and complete base/candidate source maps; a source-current onboarding row must bind that map. Card edits alone remain insufficient, and covered hunks retain their no-invariant/attach/author domain. No group or copy card is edited by this trace judgment.

- Exact generated-copy filtering, representative collection and complete source/base maps precede item settlement. [28]
- Current onboarding row selection consumes the complete source blob map, never a counted edit alone. [29]
