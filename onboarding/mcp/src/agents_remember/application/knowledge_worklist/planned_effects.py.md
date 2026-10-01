# mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**MIK-R11's planned invariant effects reconciliation, inside the worklist run.** A leaf's task document may
declare, before implementation, the invariant and family effects it expects (`expectedKnowledgeEffects`).
This module registers the `planned_untouched` item kind in MIK-R08's registry, reconciles each declaration
against the rows of the leaf's own history file in K_C (MIK-R07), marks every invariant and family item
`planned` or `unplanned`, and raises one `planned_untouched` item for every declaration no row delivers as
declared. `compute._Run.document` calls it as step 5; the declaration itself comes from
`leaf.leaf_expected_effects`.

## Code Commentary

### Logic

- **Registration (rule 4).** `PLANNED_UNTOUCHED_KIND` is `register_item_kind(ItemKind(...))` at import:
  name `planned_untouched`, subject pattern `^planned:`, facts `declared`, `unmatched` and `rows`, owner
  `MIK-R11`, and `row_lookup=subject_row("planned")`. The package `__init__` imports the module, so the kind
  is registered whenever the worklist is.
- **Declarations.** `Declaration` holds one entry (`subject`, `effect`, `requirement_ref`). Its `key` is the
  planned subject key `planned:<declared subject>#<effect>` (`models/knowledge_files/planned.planned_subject`),
  and its `record_id` is the declared `INV-`/`FAM-` ID, or `None` for `new:<label>`. `declarations_from`
  reads the task document's `ExpectedKnowledgeEffect` models or their JSON documents; `None` stays `None`
  (no declaration).
- **Matching (rule 3, `_match` and `_delivers`).**
  - `invariant:<ID>` with effect E: only a `changed` row about the invariant whose `effect` is E; for
    E = `retire`, also a `deleted` row whose `effect` is `retire`. A plain `deleted` row does not match.
  - `family:<ID>`: any `changed` family row, whatever the declared effect, because family rows carry no
    effect (ruling Q5).
  - `new:<label>` (`_new_invariant`): an invariant present in K_C, absent from K_B, whose
    `origin.handoffEntry` equals the label and whose `origin.leaf` is this leaf when the owner is known.
    Legacy-converted records carry no `handoffEntry`, so `new:` matches writer-authored invariants only
    (ruling Q4).
  - Any other row (`no_impact`, `moved`, a `changed` row with another effect) leaves the declaration
    unmatched (`no_matching_row`). An `invariant:` or `family:` ID that K_C does not hold is unmatched with
    the fact `subject_unknown`.
- **Reconciliation (`reconcile_planned_effects`).** With no declaration it returns
  `PlannedReconciliation(declared=False)`: every mark is `unplanned`, there are no items, and the summary is
  `{declared: false}` (rule 6). Otherwise each declaration becomes a summary entry (`key`, `subject`,
  `effect`, `requirementRef`, and `matched`/`matchedBy`, or `unmatched` plus the item ID) and each unmatched
  one becomes a `planned_untouched` item.
- **Marks (`PlannedReconciliation.mark`).** Items of kind `touched_invariant`, `stale_invariant` and
  `reached_family` get `planning: planned` when their subject is a declared record ID (with any effect), else
  `unplanned`. Other kinds (`onboarding_trace`, `planned_untouched`) carry no mark. A stale invariant counts as
  touched (ruling Q5).
- **The item (`_untouched_item`).** Subject is the planned key; facts are the declaration, the unmatched
  reason and every row of the leaf's history about the declared record (ID, disposition and effect); its ID
  is `item_id(planned_untouched, key, [requirementRef, reason])`, so it is stable across reorderings of the
  list and across a row answering it. `satisfiedBy` is the leaf's row whose subject is the planned key, if
  any.

### Conventions

- Nothing reads requirement prose (Exclusions): the declaration is the only plan.
- The module never writes: `compute.py` merges the marked items with the new items and sorts the union by
  `(kind, subject)` before the digest.

### Invariants And Boundaries

- **With no declaration, every item is `unplanned` and no `planned_untouched` item exists** (rule 6).
  Candidate invariant; realized by the `declarations is None` branch of `reconcile_planned_effects`; proved
  by the undeclared block of `test_declarations_match_only_the_rows_that_deliver_them_and_mark_every_item`
  and the real L44 run of the worker's evidence.
- **A `planned_untouched` item is answered only by a planned row that resolves its ref.** Candidate
  invariant; realized here by `satisfiedBy` (the planned-key row only; a `no_impact` row about the declared
  invariant is listed in `rows` and never answers it), and by the writer, which refuses a planned row whose
  ref does not resolve (`knowledge_writer/authoring.py`); proved by
  `test_a_planned_row_answers_its_item_and_the_stored_predicate_agrees` and
  `test_the_writer_writes_planned_rows_and_refuses_what_they_cannot_name`.
- **The subject key is built from the declared subject and effect, never from list position** (rule 5).
  Candidate invariant; realized by `Declaration.key` and the item ID; proved by the reordering assertion in
  the matching case (reversed declarations give identical items and digest).
- **The worklist's `satisfiedBy` and the gate's `planned_item_open` apply the same rule**, so the stored
  predicate for MIK-R09 never disagrees with the run.

### Todos

- Rendering the marks in the reviewer UI is carried to L31 (ruling Q1, 2026-09-29T21:56:18+02:00); this
  module keeps them in the persisted worklist and the curator checklist.
- No real task document may declare `expectedKnowledgeEffects` before the L37 install (ruling Q2): the
  installed runtime's `TaskDocument` is `extra=forbid`.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R11@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`11_planned-invariant-effects-reconciliation.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: matching, classification and the satisfying row. [1]
- The marked kinds and the unmatched reason. [2]
- The kind registered on import, with its satisfying row. [3]
- One declaration, its planned key and its record ID. [4]
- The task document's declarations read as `Declaration`s. [5]
- The marks and the per-declaration summary. [6]
- The reconciliation; no declaration gives `declared=False`. [7]
- Matching by subject form, and `subject_unknown`. [8]
- Which rows deliver an effect. [9]
- `new:` matches a writer-authored invariant of this leaf only. [10]
- The item, its facts, its stable ID and `satisfiedBy`. [11]
- Step 5 of the run: marks, items and the summary. [12]
- Matching, marks, `subject_unknown`, the reordering and the four R1-F3 branches. [13]
- A planned row answers its item; the stored predicate agrees. [14]

### Cross-Repo References

The declaration is read from the leaf's task document in the coordination root, through the task plane
(`tasks/leaf_decisions.py`); this module receives it as data and crosses no repository boundary itself.

No cross-repo boundary is crossed by this file.
