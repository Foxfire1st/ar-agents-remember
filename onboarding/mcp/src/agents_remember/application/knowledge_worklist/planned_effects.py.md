# mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:18:54+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R11@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`11_planned-invariant-effects-reconciliation.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: matching, classification and the satisfying row. | "Planned invariant effects reconciliation (MIK-R11@v2)" | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:1-27 |
| The marked kinds and the unmatched reason. | `_MARKED_KINDS`; `UNMATCHED` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:62-62; mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:65-65 |
| The kind registered on import, with its satisfying row. | `PLANNED_UNTOUCHED_KIND`; `register_item_kind` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:67-81 |
| One declaration, its planned key and its record ID. | `Declaration` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:84-108 |
| The task document's declarations read as `Declaration`s. | `declarations_from` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:111-126 |
| The marks and the per-declaration summary. | `PlannedReconciliation` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:129-151 |
| The reconciliation; no declaration gives `declared=False`. | `reconcile_planned_effects` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:154-181 |
| Matching by subject form, and `subject_unknown`. | `_match` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:184-200 |
| Which rows deliver an effect. | `_delivers` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:203-210 |
| `new:` matches a writer-authored invariant of this leaf only. | `_new_invariant` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:213-221 |
| The item, its facts, its stable ID and `satisfiedBy`. | `_untouched_item` | mcp/src/agents_remember/application/knowledge_worklist/planned_effects.py:224-245 |
| Step 5 of the run: marks, items and the summary. | `reconcile_planned_effects`; `plannedEffects` | mcp/src/agents_remember/application/knowledge_worklist/compute.py:249-251; mcp/src/agents_remember/application/knowledge_worklist/compute.py:270-271; mcp/src/agents_remember/application/knowledge_worklist/compute.py:286-286 |
| Matching, marks, `subject_unknown`, the reordering and the four R1-F3 branches. | `test_declarations_match_only_the_rows_that_deliver_them_and_mark_every_item` | mcp/tests/test_planned_knowledge_effects.py:246-360 |
| A planned row answers its item; the stored predicate agrees. | `test_a_planned_row_answers_its_item_and_the_stored_predicate_agrees` | mcp/tests/test_planned_knowledge_effects.py:363-398 |

## Cross-Repo References

The declaration is read from the leaf's task document in the coordination root, through the task plane
(`tasks/leaf_decisions.py`); this module receives it as data and crosses no repository boundary itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:18:54+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `mcp/src/agents_remember/application/knowledge_worklist/compute.py`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. No verification stamp was advanced.
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): No content impact: this card's source is unchanged. `compute.py` moved under it (MIK-R14 bound the run's classifier to a local and added step 8). The "Step 5 of the run" row could not be shifted (its first line changed) and was already partly stale at base (`plannedEffects` lay outside `228-244`), so it was re-measured by hand to the call, the marked items and the summary key (`247-249; 268-269; 284-284`).
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): No content impact: citation-only repair. This card's source is unchanged; the step-5 row into `compute.py` moved when L06 split `_Run.document` into helpers and added step 6 (`243-272` → `228-244`, re-measured by hand: the fixer declined it as a multi-anchor row). Claim wording unchanged. No verification stamp was advanced.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): created this card for the new file MIK-R11 adds, recording the architect rulings of 21:56:18 (Q1, Q2, Q4, Q5) and 22:35:34 (F3). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
