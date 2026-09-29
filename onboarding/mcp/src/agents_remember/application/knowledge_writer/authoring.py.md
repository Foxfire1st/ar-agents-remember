# mcp/src/agents_remember/application/knowledge_writer/authoring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/authoring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T01:22:26+02:00 |
| lastVerifiedCommitHash | `7127756cd132d1103cd0a24bc7dc6884ddb663ee`|
| lastVerifiedCommitDate | 2026-09-30T01:41:06+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The edits: a read hand-off document applied to the memory tree with every mechanical field filled
(MIK-R12 rules 1-3).** The curator authors meaning (statements, scope, admission, facets, links,
dispositions, reasons); `Authoring` fills IDs, anchors, revisions, origin and history-row fields. Nothing
here judges meaning, and nothing is written to disk.

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
  a planned row (`_planned_row`); any subject that is not an invariant, a family, an onboarding card or
  route, or a planned key is refused.

### Conventions

- Every problem is appended through `problem(where, message)`; the writer decides after the whole run.

### Invariants And Boundaries

- A rerun of the same list writes the same files with the same IDs (idempotence).
- An updating leaf never merges evidence into another leaf's origin (ruling F4 / R2-1).
- No database writes; no automatic authoring of meaning (packet exclusions).
- **Only a `moved` row may relocate an entry** (L06 ruling Q6). A cover naming a path on any other
  disposition is refused; a rerun that finds the entry already at the path is a plain re-anchor.

### Todos

- The report `note` path of the first fix round is no longer used for foreign evidence; `notes` stays in
  the report shape (`report.py`) and is currently never appended to by this module.

## 260928-MIK-L28 A Test File Named Without A Test Is Reported (MIK-R28 Rule 2)

`_cited_test` now also takes a `TestFileMention`: evidence that names a test module but no test in it.
It is reported `unresolvable` with the remedy text, never silently skipped, so rule 2's "evidence that
names no resolvable test is reported" holds for the bare-file case too. The evidence text itself is still
stored in `origin.handoff`, as the MIK-R12 writer already did. A proof is still written only from a `proofs[]` item that carries the
curator's facet; the report offers the statement only as a draft.

| Finding | Anchor | Source |
| --- | --- | --- |
| Both forms become proofs once faceted; an absent test and a bare test file are reported. | `test_both_forms_become_proofs_once_faceted_and_unresolvable_evidence_is_reported` | mcp/tests/test_knowledge_proofs.py:155-200 |
| No sidecar until the facet is authored; a blank facet is refused and writes nothing. | `test_a_proof_waits_for_the_curator_facet_and_is_offered_the_statement_as_a_draft` | mcp/tests/test_knowledge_proofs.py:203-224 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| An `onboarding:` subject goes to its own row builder. | `_row`; `OnboardingTraceRow` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:578-604 |
| The onboarding row: no extra members, the ID and moved markers kept, validated. | `_onboarding_row` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:606-640 |
| A moved marker row satisfies its item and survives a rewrite through the writer. | `test_a_moved_marker_row_satisfies_its_item_and_survives_a_rewrite` | mcp/tests/test_onboarding_trace_gate.py:401-435 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The task owner's answer about a decision, injected into the writer. | `DecisionResolver` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:81-81 |
| The resolver field; `None` has no task owner. | "decisions: DecisionResolver" | mcp/src/agents_remember/application/knowledge_writer/authoring.py:124-124 |
| A `planned:` subject goes to its own row builder. | `_row`; `PlannedEffectRow` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:578-604 |
| The planned row: no extra members, `ref` required, the ID kept, validated. | `_planned_row` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:642-688 |
| What the ref names must exist or resolve. | `_unresolved_ref` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:690-708 |
| The writer's planned rows and every refusal. | `test_the_writer_writes_planned_rows_and_refuses_what_they_cannot_name` | mcp/tests/test_planned_knowledge_effects.py:419-501 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| An invariant row tells its covers whether it is a moved row. | `_invariant_row`; `moving` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:721-744 |
| A path on any other disposition is refused. | `_covers`; "only on a moved row" | mcp/src/agents_remember/application/knowledge_writer/authoring.py:763-776 |
| The entry's `after`: relocated when the path differs, then re-anchored at C. | `_cover_after`; `_relocate` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:810-834; mcp/src/agents_remember/application/knowledge_writer/authoring.py:836-847 |
| The relocation: the entry keeps its ID and fields and moves sidecar. | `_relocate` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:836-847 |
| A moved row relocates the entry; before and after name the old and new paths; a rerun is byte-identical. | `test_a_moved_row_whose_after_names_another_path_relocates_the_entry` | mcp/tests/test_knowledge_writer.py:678-749 |

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The mechanical fields, by concern.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fields that carry no meaning; a change elsewhere is a new revision. | `NON_MEANING_FIELDS` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:85-85 |
| The operation: entries, records, rows, then unstored foreign evidence refuses. | `run` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:128-156 |
| ID assignment and rerun reuse. | `_assign_ids` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:171-194 |
| Origin: own records gain evidence, another owner's origin is kept exactly. | `_origin` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:229-264 |
| Revision once per leaf against the base. | `_place_record` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:266-295 |
| Records of any kind, with defaults and resolved links. | `_write_record` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:358-386 |
| Realization and proof entries upserted in the sidecar. | `_upsert_entry` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:410-453 |
| A rerun removes only this owner's unnamed entries. | `_remove_unnamed_entries` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:455-479 |
| What became of a test the evidence names, and a test file named without a test is `unresolvable`. | `_cited_test`; `TestFileMention` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:516-542 |
| History rows into the owner's file; a closed file is frozen. | `_write_rows` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:553-576 |
| Foreign evidence stored in this owner's row reason. | `_reason_with_evidence` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:710-719 |
| A cover's before and after, re-anchored at C when asked. | `_cover` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:778-798 |
| The conforming example: decision, realization and proof, validated. | `test_a_decision_a_realization_and_a_tested_evidence_produce_validated_files` | mcp/tests/test_knowledge_writer.py:133-159 |
| Rerun idempotence. | `test_a_rerun_of_the_same_list_writes_the_same_files_with_the_same_ids` | mcp/tests/test_knowledge_writer.py:285-295 |
| Revision increments once; foreign evidence goes to this leaf's row. | `test_a_meaning_change_increments_the_revision_once_against_the_base` | mcp/tests/test_knowledge_writer.py:369-406 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **body updated for MIK-R06.** Added the section "260928-MIK-L06 A Moved Row Relocates Its Entry To Another File" (`moving`, `_covers`'s refusal, `_relocate`), with ruling Q6 (21:49:19) and the review's N3 known limit, extended the Logic bullet on history rows, and added the moved-row invariant. Five rows added; the existing `_cover` row still holds at `778-798`. No verification stamp was advanced.
- 2026-09-29T21:48:07+00:00: Generated citation repair: `NON_MEANING_FIELDS` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:85-85. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:48:07+00:00: Generated citation repair: `_reason_with_evidence` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:710-719. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:48:07+00:00: Generated citation repair: `_cover` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:772-792. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added the section "260928-MIK-L11 The Planned Row Through The Writer" (`DecisionResolver`, `_planned_row`, `_unresolved_ref`) and reworded the Logic bullet on history rows to admit the planned key. Records architect rulings 2026-09-29T21:56:18 (Q5) and 22:35:34 (F1). Rows below the inserted methods were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T18:58:58+00:00: Generated citation repair: `NON_MEANING_FIELDS` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:80-80. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:58:58+00:00: Generated citation repair: `_reason_with_evidence` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:633-642. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T18:58:58+00:00: Generated citation repair: `_cover` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:695-715. No content impact: mechanical anchor-range projection bound to citation source snapshot f243d6cd7f6b1214330608a0b5e372fb521b8035680e9d41a0f33ceb9d8057ab; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 The Onboarding Row Through The Writer" (`_onboarding_row`) and reworded the Logic bullet on history rows, which said that only invariant and family subjects have a row kind. Records architect ruling 2026-09-29T18:49:50 (6). Rows below the inserted method were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T15:26:13+02:00 — 260928-MIK-L28 curator (uncommitted change set on `ar/260928-mik-l28`, code base `8b0254263c6998b1d4814b2e97c1bd231d39350f` plus the working-tree delta and untracked files): Added the section "260928-MIK-L28 A Test File Named Without A Test Is Reported": `_cited_test` reports a `TestFileMention` as `unresolvable` with its remedy. The "Cited tests" Logic bullet now names both evidence forms and the bare-file case, and the `_cited_test` row says so. Two test rows. The other ranges were re-pointed by the installed `memory-citations --fix`. No verification stamp was advanced.
- 2026-09-29T13:25:18+00:00: Generated citation repair: `NON_MEANING_FIELDS` repointed to mcp/src/agents_remember/application/knowledge_writer/authoring.py:79-79. No content impact: mechanical anchor-range projection bound to citation source snapshot 669685dd91608eb0296af5d8546b06d1035099d9a0ff44914baa1ead631123fe; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
