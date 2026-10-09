# mcp/src/agents_remember/application/knowledge_writer/authoring.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The edits: a read hand-off document applied to the memory tree with every mechanical field filled
(MIK-R12 rules 1-3).** The curator authors meaning (statements, scope, admission, facets, links,
dispositions, reasons); `Authoring` fills IDs, anchors, revisions, origin and history-row fields. Nothing
here judges meaning, and nothing is written to disk. History-row mechanics are implemented by the inherited `HistoryRowAuthoring` in `authoring_rows.py`; this implementation move changes neither authored dispositions nor worklist obligations.

## Code Commentary

### Logic

- **IDs** (`_assign_ids`, `mint`): an entry with `invariant_id` updates that invariant; otherwise the ID
  is the one this owner already wrote from the same hand-off entry (`record_by_origin`) or a freshly minted
  one unique against `known_ids`. Records do the same by `(kind, handoff entry)`; two records of one kind
  from one hand-off entry are refused.
- **Revisions** (`_place_record`): against the base record, `revision` is the base revision plus one when
  `meaning` differs, else unchanged; `NON_MEANING_FIELDS` are `id`, `schema`, `origin`, `revision`,
  `admission` and `status`, so a status change does not increment it (architect ruling 6). With no Git
  base, the pre-operation file is the reference.
- **Origin and evidence** (`_origin`): a new record's origin names the task, the leaf or wave, the hand-off
  path and entry, and the entry's evidence. A record this owner authored gains this run's evidence. A record
  **another** leaf or wave authored keeps its origin exactly; the evidence is queued and must be stored in
  this owner's history row about that record (`_reason_with_evidence` appends `Evidence (<entry>): …` to the
  row's `reason`); without such a row the run is refused (ruling R2-1). Evidence is never only reported.
- **Records of any kind** (`_write_record`): `fields` are merged over the stored record; `handoff:` handles
  are resolved; a link whose target is `{path, locator}` gets its anchor resolved at C (`_link`). A new
  record's `status` defaults to `proposed` (`active` for a decision).
- **Entries** (`_upsert_entry`): a realization per target and a proof per curator `proofs[]` item go into
  the source file's sidecar (`realizes` / `proves`), matched on invariant, owner, hand-off entry and
  locator; entry origin is `{leaf, handoffEntry}`. `_remove_unnamed_entries` removes, and reports
  `removed`, only this owner's earlier entries from the same hand-off entry that this run no longer names
  (ruling F3); another leaf's entries never match.
- **Cited tests** (`_cited_test`): each test the evidence names, as `path::name` or `path -k name`
  (`handoff.tests_named_in`), is reported `proof_written`, `needs_facet` (it resolves at C; a draft facet
  from the statement is offered) or `unresolvable`. A test module named without a test in it is reported
  `unresolvable` with the remedy (write `path::<name>` or `path -k <name>`). Evidence never becomes a proof
  without the curator's facet (ruling 4; MIK-R28 rule 2).
- **History rows** (`_write_rows`, `_row`): one row per subject in `knowledge/history/<owner>.json`; the row
  ID is reused by subject; a closed file is refused (MIK-R07 rule 7). Invariant rows get the invariant's
  revision and `covers` with `before` (the base anchor, or `absent`) and `after`; re-anchoring writes the new
  anchor into the entry in the same operation (MIK-R07 rule 4), and `{remove: true}` removes it with
  `after: absent`. Since MIK-R06 (L06 ruling Q6) a `moved` row's cover may name another `path`: the entry
  is relocated into that file's sidecar and re-anchored there (`_relocate`). Family rows need `examined` and record each member's revision. Since MIK-R30 an
  `onboarding:` subject is an onboarding row (`_onboarding_row`), and since MIK-R11 a `planned:` subject is
  a planned row (`_planned_row`), and since MIK-R10 a `hunk:<item id>` or `file:<path>@<blob>` subject is a
  `no_invariant` row (`_unexplained_row`); `_row` dispatches these three through one table of (row model,
  builder) pairs. Any subject that is not an invariant, a family, an onboarding card or route, a planned key
  or an unexplained change is refused.

### Conventions

- Every problem is appended through `problem(where, message)`; the writer decides after the whole run.

### Invariants And Boundaries

- A rerun of the same list writes the same files with the same IDs (idempotence).
- An updating leaf never merges evidence into another leaf's origin (ruling F4 / R2-1).
- No database writes; no automatic authoring of meaning (packet exclusions).
- **Only a `moved` row may relocate an entry** (L06 ruling Q6). A cover naming a path on any other
  disposition is refused; a rerun that finds the entry already at the path is a plain re-anchor.
- **A record both sides of a merge changed is resolved at one more than the higher side's revision (L37, MIK-R24
  rule 8 step 4).** `_place_record` takes the revision from `_revision`: when `state.merged_sides_revision` finds
  the record's path unmerged (a crossing sync leaves it so), the result is that maximum plus one; a
  `MergeStageError` is a named problem and no revision is guessed. Every other record keeps the earlier rule: the
  base's revision, plus one when the meaning changed, and 1 for a record new to the base. The rule keys on the
  unmerged path, not on the owner kind.
- **Rows go to the owner's writable history file (L37 reopen ruling).** `_write_rows` and the evidence note of
  `_reason_with_evidence` take the path from `state.history_target(owner)`. A new attempt file carries `attempt: n`
  (n >= 2); a first file carries no `attempt`, so existing files keep their bytes.

### Todos

- The report `note` path of the first fix round is no longer used for foreign evidence; `notes` stays in
  the report shape (`report.py`) and is currently never appended to by this module.

## 260928-MIK-L28 A Test File Named Without A Test Is Reported (MIK-R28 Rule 2)

`_cited_test` now also takes a `TestFileMention`: evidence that names a test module but no test in it.
It is reported `unresolvable` with the remedy text, never silently skipped, so rule 2's "evidence that
names no resolvable test is reported" holds for the bare-file case too. The evidence text itself is still
stored in `origin.handoff`, as the MIK-R12 writer already did. A proof is still written only from a `proofs[]` item that carries the
curator's facet; the report offers the statement only as a draft.

- Both forms become proofs once faceted; an absent test and a bare test file are reported. [1]
- No sidecar until the facet is authored; a blank facet is refused and writes nothing. [2]

## 260928-MIK-L30 The Onboarding Row Through The Writer (MIK-R30)

`_row` sends a subject matching `OnboardingTraceRow.subject_pattern` (`onboarding:<path>` or
`onboarding:<route>/overview`) to `_onboarding_row`, so the curator can author the `no_impact` row that
satisfies an onboarding trace on a converted tree through `knowledge-ingest`:

- it refuses `covers`, `effect`, `because` and `examined`;
- it reuses an existing row's ID for the same subject, and keeps the `markers` a crossing sync moved into
  that row (MIK-R24 rule 8 step 1);
- it validates the row as `OnboardingTraceRow`, so `no_impact` is the only disposition accepted.

The file is outside MIK-R30's Scope list; the architect accepted it as necessary wiring (ruling
2026-09-29T18:49:50 (6)), since rows are authored only through the writer.

- An `onboarding:` subject goes to its own row builder. [3]
- The onboarding row: no extra members, the ID and moved markers kept, validated. [4]
- A moved marker row satisfies its item and survives a rewrite through the writer. [5]

## 260928-MIK-L11 The Planned Row Through The Writer (MIK-R11 Rule 5)

`_row` sends a subject matching `PlannedEffectRow.subject_pattern` (`planned:<declared subject>#<effect>`)
to `_planned_row`, so the curator answers a `planned_untouched` worklist item through `knowledge-ingest`:

- it refuses `covers`, `effect`, `because` and `examined`, and requires `ref`;
- it reuses an existing row's ID for the same subject, and validates the row as `PlannedEffectRow`
  (disposition `realized_elsewhere`, `deferred` or `dropped`, with the ref key that disposition takes);
- `_unresolved_ref` then checks what the ref names: a `realized_elsewhere` `ref.invariant` must be a stored
  invariant and a `ref.row` a known history-row ID; a `dropped` row's `ref.decision` (the `at` of a
  decision entry) goes to `Authoring.decisions`, the injected `DecisionResolver`, and any answer but
  "resolved" refuses the row; with no task owner (`decisions` is `None`, as in a wave) a `dropped` row is
  refused. A `deferred` ref is shape-checked only (ruling Q5).

The resolver is the task owner's (`tasks/leaf_decisions.leaf_decision_refusal`, bound by the CLI), which
resolves through the strict leaf lookup: an unreadable or duplicated leaf document is a named refusal
(ruling F1, 2026-09-29T22:35:34+02:00). The writer never imports the task plane.

- **A `planned_untouched` item is answered only by a planned row that resolves its ref.** Candidate
  invariant; realized by `_planned_row` and `_unresolved_ref` (with the worklist's `satisfiedBy`); proved by
  `test_the_writer_writes_planned_rows_and_refuses_what_they_cannot_name`.

- The task owner's answer about a decision, injected into the writer. [6]
- The resolver field; `None` has no task owner. [7]
- A `planned:` subject goes to its own row builder. [8]
- The planned row: no extra members, `ref` required, the ID kept, validated. [9]
- What the ref names must exist or resolve. [10]
- The writer's planned rows and every refusal. [11]

## 260928-MIK-L06 A Moved Row Relocates Its Entry To Another File (MIK-R06, Ruling Q6)

The real-data directory move of MIK-R06's expected evidence needs `moved` invariant rows whose `after` names
the moved file. Before this change the writer could only re-anchor an entry at its own source path, so a
moved file's entries had to be re-created and the row could only be `extended`. The architect ruled that a
conformance gap of landed L12 against MIK-R12 rule 2 and MIK-R07 rule 4, to be fixed minimally here (ruling
Q6, 2026-09-29T21:49:19+02:00):

- `_invariant_row` passes `moving` (disposition `moved`) to `_covers`, which refuses a cover naming a `path`
  on any other disposition: "a cover names another source path only on a moved row".
- `_cover_after` calls `_relocate` when the cover's path differs from the entry's current file. `_relocate`
  removes the entry from its sidecar and appends it, with its ID, invariant and authored fields, to the new
  file's sidecar (created when needed); the entry is then re-anchored at the new path as before, so its
  `blob` and `content` are C's.
- The row's `before` keeps the base anchor at the old path and its `after` names the new path, which is
  MIK-R07 rule 4 (`after` equals the entry's anchor in K_C). A rerun finds the entry already at the path.
- **Known limit, unchanged:** the old file's sidecar stays with an empty `realizes`. Moving or removing the
  onboarding cards and sidecars of moved files is c-05 onboarding work, not the writer's row path (review
  N3); each new sidecar raises a report-only `R22.3-sidecar-without-markdown` until a card exists.
- The malformed-path and remove-plus-path refusals are the hand-off reader's (`handoff._cover_path`, review
  F1 and N7).

- An invariant row tells its covers whether it is a moved row. [12]
- A path on any other disposition is refused. [13]
- The entry's `after`: relocated when the path differs, then re-anchored at C. [14]
- The relocation: the entry keeps its ID and fields and moves sidecar. [15]
- A moved row relocates the entry; before and after name the old and new paths; a rerun is byte-identical. [16]

## 260928-MIK-L10 The No-Invariant Row And The Retired-Attach Refusal (MIK-R10)

- **Dispatch table.** `_row` now tries `OnboardingTraceRow`, `PlannedEffectRow` and `UnexplainedChangeRow` in
  one loop over `(model, builder)` pairs, matching each model's `subject_pattern`, which keeps `_row` within
  PLR0911. The behaviour for the first two is unchanged. (L14 adds `ReconsiderationRow` as a fourth pair.)
- **`_unexplained_row`.** A `no_invariant` row answers an unexplained change in a covered file (rule 3). It
  refuses `covers`, `effect`, `because`, `examined` and `ref` ("a no_invariant row carries no [...]"), reuses
  the row ID by subject, validates against `UnexplainedChangeRow` (only `no_invariant`; a blank `reason` is
  refused by the model), and for a `file:<path>@<blob>` subject asks `CodeSnapshot.file_subject_mismatch`
  whether the object names the path's tree entry at C (or `absent`): a row about another change of the path
  answers no item and is refused. A `hunk:` row cannot be checked against item IDs without the worklist; a
  row that answers no raised item is reported by the worklist as unnecessary (ruling Q4).
- **Attach to a retired invariant is refused (`_attaches_to_retired`).** In `_write_entry`, an entry that
  names an `invariant_id` and carries targets is refused when the stored invariant's status is `retired`,
  naming the invariant and the two alternatives (author a new invariant, or record `no_invariant`). An
  attach to an absent invariant hits the existing "no stored record" refusal. The guard is its own method
  (the L06 sync); `_write_entry` rose from 8 to 9 (radon), within the standing bar of 10 (ruling 03:24:28 N1).
- **Attach or author for a delete-only hunk is not refused here (ruling 01:56:39 Q1).** A hand-off entry names
  no worklist item, and a new entry may legitimately cover other hunks. The refusal is structural: such an
  entry cannot link a delete-only hunk, so the item stays open and the closeout gate refuses the leaf.
- **Unconverted memory is unchanged.** The installed runtime writes no history files before MIK-R37.

- The retired-attach guard, called before the record is placed. [17]
- The refusal names the invariant and the alternatives. [18]
- The special row kinds (L10's three, and MIK-R14's reconsideration row since L14), dispatched through one table. [19]
- The no_invariant row: no extra members, the ID kept, validated, and a `file:` subject checked at C. [20]
- The writer's refusals: absent and retired invariants, a blank reason, covers, another disposition. [21]

## 260928-MIK-L14 The Reconsideration Rows Through The Writer (MIK-R14 Rule 4)

- **Dispatch.** `_row`'s `(model, builder)` table gains `(ReconsiderationRow, self._reconsideration_row)`, the
  fourth special kind (L10's table form kept at the sync, review F9), so a `reconsider:<DEC-ID>#<i>` subject is
  routed by the model's `subject_pattern`.
- **The common row (`_common_row`).** A reconsideration row carries the common fields only: `covers`, `effect`,
  `because`, `examined` and `ref` are refused ("a reconsideration row carries no [...]"); the row ID is reused by
  subject or minted; the row is validated against `ReconsiderationRow` (only `still_rejected` and `raise`, a
  non-blank `reason`).
- **What the subject names (`_reconsideration_row`).** The decision is read from the memory tree
  (`state.record`) and checked by `reconsidered_alternative`: a decision record, a `rejected` or `deferred`
  alternative at the index, and a `reconsider_on` link to it; otherwise the row is refused with the reason.
- **`raise` (`_raise`).** The question is composed by `raise_question` and checked through the `questions` port
  (a dry run of the task-document edit); with no port the row is refused ("a raise appends a question to the leaf's
  task document, and this write has no task owner"), and a check refusal refuses it too ("the raise is refused, so
  the item stays open: …"). Otherwise the decision's `status` becomes `under_reconsideration` through `state.put`
  (status is in `NON_MEANING_FIELDS`, so the revision stays), the `(key, question)` pair is queued in `raised` for
  `writer.py` to append before any file is written, and the note names the question. A `raise` leaves the links
  as they are.
- **`still_rejected` (`_refresh`, rulings 04:37:56 Q2/Q3, 05:31:11 F1–F4 and reviews R3–R5).** `_answered_item`
  finds the leaf worklist's item for the subject (`reconsiderations`, filled from `WriteRequest.worklist`): with no
  item the row is written and a note says no link was refreshed (review N3); a row whose `items` names another ID
  is refused ("recompute the worklist and answer that item"). The `Answer` carries the item's `facts.changed`, the
  decision as memory `HEAD` records it (`state.base_record`), the item ID and whether the row names it; `CodeAtC`
  carries C's trees and blobs. `refreshed_links` returns the links and any problems: each problem refuses the row
  ("the still_rejected refresh is refused: links.<i>: …"). Unchanged links write nothing; a newly judged link places
  the decision through `_place_record`, so its revision goes up once in the leaf and it is reported in `records`
  (F2: links are meaning); a link only carried to the current C is written with `state.put` and a note, with no
  further bump (R4-1).
- **Fields.** `questions` (the `OpenQuestions` port, `None` without a task owner), `raised` (the queued questions)
  and `reconsiderations` (the worklist's reconsideration items by subject).
- **Size and complexity.** The module is 1,094 lines (under the 1,200 limit). Radon reports no new C: the C blocks
  (`run`, `_invariant_document`, `_write_record`, `_upsert_entry`) exist at base (reviews R1–R6).

- The port, the queued questions and the worklist's items. [22]
- The fourth special row kind in the dispatch table. [23]
- The row: common fields, the named alternative, then `raise` or the refresh. [24]
- `still_rejected`: the answered item, the refresh, one bump when judged, carried in place otherwise. [25]
- `raise`: the checked question, the status, and the queued append. [26]
- The refusals of a wrong subject or an extra field. [27]
- A `raise` refused without a task owner, on a check refusal and on an append refusal writes nothing. [28]

## 260928-MIK-L37 The Writer Fills A Row's Items, And A Cover Revises A Rationale In Place

- **`items` (MIK-R07 rule 1).** `_write_rows` collects the rows it wrote and calls `_fill_items`. A row whose
  hand-off names no item gets the IDs of the worklist items it answers: `_answered_items` asks each item kind's own
  satisfying-row rule (`registry.satisfying_row`) over the file as written, for every `(kind, subject, id)` in
  `Authoring.worklist_items`. Items the hand-off names are kept. Without a worklist, or with a file that does not
  parse as a history file, nothing is filled in and nothing is refused: the field is informational, and the gate
  matches rows by subject.
- **A cover's `rationale`.** `_cover` calls `_revise_rationale` after the cover's `after` anchor is settled. When the
  cover carries a rationale, the realization entry's `rationale` is replaced in its sidecar and the entry keeps its
  ID, role, invariant and anchor. A rationale on a proof entry is a named problem ("a proof has a facet"). The entry
  is looked up again first, because the cover may have moved it.

- A row whose hand-off names no item lists the worklist items it answers. [47]
- The items a row answers, by each kind's satisfying-row rule. [48]
- A cover's rationale replaces the realization entry's rationale in place. [49]

- The writer fills row items from the worklist after the unchanged case moved to governing-row tests. [50]

- A cover revises a realization entry's rationale in place. [51]

## History Rows Carry The Family's Own Revision (MIK-R48)

The module docstring states that a history row gets the invariant's or the
family's own revision beside each examined member's revision. Nothing here judges
meaning: the revision fill for family rows happens in `HistoryRowAuthoring`, and
this module only records what the row construction resolved.

- Row mechanics record the invariant's or family's own revision. [52]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The mechanical fields, by concern.

- Fields that carry no meaning; a change elsewhere is a new revision. [29]
- The operation: entries, records, rows, then unstored foreign evidence refuses. [30]
- ID assignment and rerun reuse. [31]
- Origin: own records gain evidence, another owner's origin is kept exactly. [32]
- Revision once per leaf against the base. [33]
- Records of any kind, with defaults and resolved links. [34]
- Realization and proof entries upserted in the sidecar. [35]
- A rerun removes only this owner's unnamed entries. [36]
- What became of a test the evidence names, and a test file named without a test is `unresolvable`. [37]

- History rows into the owner's file; a closed file is frozen. [38]

- Foreign evidence stored in this owner's row reason. [39]

- A cover's before and after, re-anchored at C when asked. [40]

- The conforming example: decision, realization and proof, validated. [41]
- Rerun idempotence. [42]
- Revision increments once; foreign evidence goes to this leaf's row. [43]

- The record's revision after this operation: an unmerged record at the higher side's plus one. [44]

- Rows are written to the history target, with its attempt when above 1. [45]

- A record both sides changed is resolved at one more than the higher side. [46]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
