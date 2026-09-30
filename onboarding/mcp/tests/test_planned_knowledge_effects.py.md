# mcp/tests/test_planned_knowledge_effects.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_planned_knowledge_effects.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T22:35:02+02:00 |
| lastVerifiedCommitHash | `3dc2ab0cf59cdc87ec478f6563d4ac6696871076`|
| lastVerifiedCommitDate | 2026-09-30T23:11:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R11@v2 cases (5 collected): a leaf's declared knowledge effects, reconciled against its history
rows.** The worklist cases reuse MIK-R08's real Git code and converted memory repositories
(`test_knowledge_worklist.World`), commit the leaf's rows into K_C, and compute the worklist over the four
named sides exactly as the leaf route does. The file runs in the unit lane (`test-evidence-lanes.toml`) and,
through that world, transitively consumes `fixtures/repository_profiles/node/package-lock.json`, which is why
`evidence-lifecycle.toml` lists it (the Thirty-eighth re-pin).

## Code Commentary

### Logic

- **The field (rule 1).** `test_the_field_is_optional_normative_intent_settable_and_refuses_malformed_declarations`:
  absent by default and absent from the intent projection (existing digests hold); classified
  `NORMATIVE_INTENT`; settable through `task_doc` `set_field` (`_apply`), which changes the intent digest,
  and clearing restores it; rendered in the header; and refused when malformed (a repeat, a bad subject form
  or ID, a label outside the vocabulary, a prose `requirementRef`, an empty list, an extra key, a master).
- **Matching and marks (rules 3, 4 and 6).** `test_declarations_match_only_the_rows_that_deliver_them_and_mark_every_item`:
  a matched `changed`/`strengthen`; a label mismatch; a `no_impact` row not clearing a strengthening; `retire`
  via a retiring `deleted` row; `new:e1` matched and `new:e2` unmatched; `INV-ZZZZZZ` as `subject_unknown`;
  the `planned`/`unplanned` marks; the undeclared run (every item `unplanned`, no `planned_untouched`); and
  reversed declarations giving identical items and digest. A second fixture commit adds the four branches of
  review R1 F3 (ruling F3): the positive family match (`FAM-F00002` by `ROW-FFFFF2`), `new:e3` (another
  leaf's invariant) and `new:e4` (already in K_B) staying unmatched, the `planned` mark on a
  `stale_invariant` and a `reached_family`, and a plain `deleted` row not matching `retire`.
- **The answer (rule 5).** `test_a_planned_row_answers_its_item_and_the_stored_predicate_agrees`: a
  `deferred` planned row sets `satisfiedBy`, the item ID is unchanged, and `planned_item_open` equals
  `satisfiedBy is None` on every item.
- **The writer and the task owner.** `test_the_writer_writes_planned_rows_and_refuses_what_they_cannot_name`
  writes planned rows through `write_knowledge` and refuses: an unresolved decision, no task owner, a wrong
  ref for the disposition, an unknown `ref.invariant` or `ref.row`, a missing `ref`, an `effect`, two refs,
  a disposition outside the three and a label outside the vocabulary. It also checks the task owner's own
  answers (`leaf_decision_refusal`) and, after ruling F1, the strict lookup: two readable documents
  (ambiguous), a claiming document with an unknown field, an unparseable `<LEAF>.json`, and an unrelated
  `preview.json` (ignored).
- **The leaf route and visibility (rule 7).** `test_a_leaf_reads_its_declaration_and_the_checklist_and_tool_show_the_marks`
  reads the declaration from the leaf's task document through its series contract, shows the checklist's
  "Planned effects" block and **Plan** column and the `knowledge_integrity_check` rows, and (ruling F2) makes
  the task document unreadable: the run is `incomplete` with input `leaf task document`, naming
  `99_leaf.json`, with no items and no `plannedEffects`.

### Conventions

- The F3 assertions extend the existing matching case through a second fixture commit, so the collected
  count stays at 5 within the unit budget.

### Invariants And Boundaries

- **The cases pin the rulings** of 2026-09-29T21:56:18+02:00 (Q4: `new:` matches writer-authored invariants
  only; Q5: the detail choices) and 22:35:34 (F1 strict lookup; F2 fail closed; F3 the four assertions).
- The reviewer-UI half of rule 7 has no case here: it is carried to L31 (ruling Q1).

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R11@v2` of task
`260928_maintained-invariant-knowledge`; it lives outside the code and memory repositories, so it is named
here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: the reused worklist world. | "reconciled against its history rows" | mcp/tests/test_planned_knowledge_effects.py:1-7 |
| The field, its class, `set_field`, the intent digest, render and the refusals. | `test_the_field_is_optional_normative_intent_settable_and_refuses_malformed_declarations` | mcp/tests/test_planned_knowledge_effects.py:119-184 |
| The declarations the matching case uses. | `DECLARED` | mcp/tests/test_planned_knowledge_effects.py:195-211 |
| Matching, marks, the undeclared run, the reordering and the F3 branches. | `test_declarations_match_only_the_rows_that_deliver_them_and_mark_every_item` | mcp/tests/test_planned_knowledge_effects.py:246-360 |
| A planned row answers its item; the predicate agrees. | `test_a_planned_row_answers_its_item_and_the_stored_predicate_agrees` | mcp/tests/test_planned_knowledge_effects.py:363-398 |
| The writer's planned rows, its refusals and the strict lookup. | `test_the_writer_writes_planned_rows_and_refuses_what_they_cannot_name` | mcp/tests/test_planned_knowledge_effects.py:419-501 |
| The leaf route, the checklist, the tool rows and the fail-closed run. | `test_a_leaf_reads_its_declaration_and_the_checklist_and_tool_show_the_marks` | mcp/tests/test_planned_knowledge_effects.py:530-587 |
| The unit-lane row. | "mcp/tests/test_planned_knowledge_effects.py" | mcp/tests/test-evidence-lanes.toml:124-124 |
| The census-derived consumer row. | "mcp/tests/test_planned_knowledge_effects.py" | mcp/tests/evidence-lifecycle.toml:835-835 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are temporary Git repositories and a temporary
task root.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T22:35:02+02:00 — 260928-MIK-L33 curator (staged change set on `ar/260928-mik-l33`, code base `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`; review R1 changes-required, R2 and R3 pass-with-notes, each followed by a fix round, with the merge round after MIK-L34): No content impact: citation repair only; this document's own source is unchanged by MIK-L33. Rows citing MIK-L33's changed sources (`test-evidence-lanes.toml`) moved with the leaf's inserted lines: 2 row(s) re-pointed by the installed fixer (its generated bullets kept). The fixer's normalisation also re-measured ranges into files this leaf did not change (`evidence-lifecycle.toml`). No claim wording changed, and no verification stamp was advanced.
- 2026-09-30T20:30:58+00:00: Generated citation repair: "mcp/tests/test_planned_knowledge_effects.py" repointed to mcp/tests/test-evidence-lanes.toml:124-124. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T20:30:58+00:00: Generated citation repair: "mcp/tests/test_planned_knowledge_effects.py" repointed to mcp/tests/evidence-lifecycle.toml:835-835. No content impact: mechanical anchor-range projection bound to citation source snapshot 8b6fd4477f4e6588d3a971c6b77ff9a95df2a0849774b3a5c948b24cd8c436b5; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): created this card for the new test file MIK-R11 adds, recording the architect rulings of 21:56:18 (Q1, Q4, Q5) and 22:35:34 (F1, F2, F3). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
