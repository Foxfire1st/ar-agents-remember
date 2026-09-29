# mcp/src/agents_remember/application/knowledge_writer/authoring.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_writer/authoring.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T10:05:46+02:00 |
| lastVerifiedCommitHash | `cd3e943d740b490d391722389af0a6bca0ccf93e`|
| lastVerifiedCommitDate | 2026-09-29T10:38:08+02:00|
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
- **Cited tests** (`_cited_test`): each `path::name` in evidence is reported `proof_written`, `needs_facet`
  (it resolves at C; a draft facet from the statement is offered) or `unresolvable`. Evidence never becomes
  a proof without the curator's facet (ruling 4; MIK-R28 builds on this).
- **History rows** (`_write_rows`, `_row`): one row per subject in `knowledge/history/<owner>.json`; the row
  ID is reused by subject; a closed file is refused (MIK-R07 rule 7). Invariant rows get the invariant's
  revision and `covers` with `before` (the base anchor, or `absent`) and `after`; re-anchoring writes the new
  anchor into the entry in the same operation (MIK-R07 rule 4), and `{remove: true}` removes it with
  `after: absent`. Family rows need `examined` and record each member's revision. Only invariant and family
  subjects have a registered row kind; any other subject is refused.

### Conventions

- Every problem is appended through `problem(where, message)`; the writer decides after the whole run.

### Invariants And Boundaries

- A rerun of the same list writes the same files with the same IDs (idempotence).
- An updating leaf never merges evidence into another leaf's origin (ruling F4 / R2-1).
- No database writes; no automatic authoring of meaning (packet exclusions).

### Todos

- The report `note` path of the first fix round is no longer used for foreign evidence; `notes` stays in
  the report shape (`report.py`) and is currently never appended to by this module.

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
| Fields that carry no meaning; a change elsewhere is a new revision. | `NON_MEANING_FIELDS` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:77-77 |
| The operation: entries, records, rows, then unstored foreign evidence refuses. | `run` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:118-146 |
| ID assignment and rerun reuse. | `_assign_ids` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:161-184 |
| Origin: own records gain evidence, another owner's origin is kept exactly. | `_origin` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:219-254 |
| Revision once per leaf against the base. | `_place_record` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:256-285 |
| Records of any kind, with defaults and resolved links. | `_write_record` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:348-376 |
| Realization and proof entries upserted in the sidecar. | `_upsert_entry` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:400-443 |
| A rerun removes only this owner's unnamed entries. | `_remove_unnamed_entries` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:445-469 |
| What became of a test the evidence names. | `_cited_test` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:513-527 |
| History rows into the owner's file; a closed file is frozen. | `_write_rows` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:531-554 |
| Foreign evidence stored in this owner's row reason. | `_reason_with_evidence` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:580-589 |
| A cover's before and after, re-anchored at C when asked. | `_cover` | mcp/src/agents_remember/application/knowledge_writer/authoring.py:642-662 |
| The conforming example: decision, realization and proof, validated. | `test_a_decision_a_realization_and_a_tested_evidence_produce_validated_files` | mcp/tests/test_knowledge_writer.py:133-159 |
| Rerun idempotence. | `test_a_rerun_of_the_same_list_writes_the_same_files_with_the_same_ids` | mcp/tests/test_knowledge_writer.py:285-295 |
| Revision increments once; foreign evidence goes to this leaf's row. | `test_a_meaning_change_increments_the_revision_once_against_the_base` | mcp/tests/test_knowledge_writer.py:369-402 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
