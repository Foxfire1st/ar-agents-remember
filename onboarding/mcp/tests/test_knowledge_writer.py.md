# mcp/tests/test_knowledge_writer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_writer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T01:22:26+02:00 |
| lastVerifiedCommitHash | `7127756cd132d1103cd0a24bc7dc6884ddb663ee`|
| lastVerifiedCommitDate | 2026-09-30T01:41:06+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R12: the curator writer creates and updates every knowledge kind as validated files.** Registered
in the `unit-regression` lane; 18 collected cases, each over real Git repositories.

## Code Commentary

### Logic

- Conforming example: a decision, a realization with blob and content (blob equals `git rev-parse`, content
  the sha256 of the symbol's lines) and a proof from tested evidence, all validated.
- `knowledge-ingest --commit` round-trips every kind: all ten record kinds, a realization, a proof, a
  `moved` invariant row and a `no_impact` family row; a second run exits 0.
- Idempotence: a rerun is byte-identical with every action `unchanged`.
- Evidence naming no resolvable test is reported and kept; four problems refuse in one report; a colliding
  ID is refused by `R22.2-identity` with the tree unchanged.
- A meaning change increments the revision once against the base; evidence on another leaf's record goes to
  this leaf's row reason (`storedIn` names the row), and without the row the run is refused. The base
  record's kept origin now includes its `legacyId` (`legacy-invariant-landing-pair`), because the base
  records are genuine exports since MIK-R27 (leaf 260928-MIK-L27).
- `incidental` is written as `support`; a closed history file is frozen.
- Planning writes nothing; unconverted memory is not this route; the bootstrap writes as a wave, and the
  `knowledge-bootstrap` command dispatches converted memory to the file writer.
- A contradicted history row refuses until named again; an entry naming no record is refused; a rerun that
  changes a locator removes only this leaf's old entry; a blank authorization is refused.
- The MIK-R04 route rules are reports in the writer and refusals at `require_valid_commit`.
- **MIK-R27 inside the writer** (leaf 260928-MIK-L27): a new invariant claiming `guarded_by_test` with no
  proof is refused (`[R27.2-new-record]`, naming the criterion) and the memory tree is byte-identical;
  the same entry with a `proofs` item is written. The admission rules set no `writer_reports`, so the
  writer refuses as every commit route does.
- **A moved row relocates its entry** (leaf 260928-MIK-L06, ruling Q6):
  `test_a_moved_row_whose_after_names_another_path_relocates_the_entry` moves a file with `git mv`. An
  `extended` row whose cover names a `path` is refused ("only on a moved row"); a cover path `../outside.py`,
  `/abs/landing.py` or `""`, and a cover with both `remove` and `path`, are each refused as a named problem
  with the memory tree byte-identical (review F1 and N7). A `moved` row relocates `RLZ-BASE01` into
  `onboarding/pkg/moved/landing.py.json` with its role kept, its `blob` the moved file's blob at C and its
  content unchanged; the row's `before` and `after` name the old and new paths and validate as `moved`; a
  rerun is byte-identical.

### Conventions

- Helpers `_write`, `_decision`, `_conforming` and `_every_kind` build requests and documents.

### Invariants And Boundaries

- The family-route test fails if the writer split is disabled (verified by the reviewer's mutation check).

### Todos

None recorded.

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

The cases.

| Finding | Anchor | Source |
| --- | --- | --- |
| The conforming example. | `test_a_decision_a_realization_and_a_tested_evidence_produce_validated_files` | mcp/tests/test_knowledge_writer.py:133-159 |
| Every kind through the command line. | `test_the_command_line_round_trips_every_kind` | mcp/tests/test_knowledge_writer.py:244-282 |
| Unresolvable evidence reported and kept. | `test_evidence_that_names_no_resolvable_test_is_reported_and_kept` | mcp/tests/test_knowledge_writer.py:298-323 |
| A bootstrap of converted memory writes as a wave. | `test_a_bootstrap_of_converted_memory_writes_as_a_wave` | mcp/tests/test_knowledge_writer.py:464-492 |
| A rerun that changes a locator removes this leaf's old entry only. | `test_a_rerun_that_changes_a_locator_removes_this_leafs_old_entry` | mcp/tests/test_knowledge_writer.py:560-580 |
| The bootstrap command dispatch. | `test_the_bootstrap_command_dispatches_converted_memory_to_the_file_writer` | mcp/tests/test_knowledge_writer.py:583-602 |
| MIK-R27: the writer refuses an unsupported admission claim and writes nothing, and writes once the proof is added. | `test_the_writer_refuses_a_new_invariant_whose_claim_the_tree_does_not_support` | mcp/tests/test_knowledge_writer.py:659-675 |
| Route rules: report in the writer, refusal at commit. | `test_family_route_rules_are_reports_in_the_writer_and_refusals_at_a_commit_route` | mcp/tests/test_knowledge_writer.py:618-656 |
| MIK-R06 (ruling Q6): a moved row relocates its entry; malformed paths and remove-plus-path are refused. | `test_a_moved_row_whose_after_names_another_path_relocates_the_entry` | mcp/tests/test_knowledge_writer.py:678-749 |

## Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T01:22:26+02:00 — 260928-MIK-L06 curator (uncommitted change set on `ar/260928-mik-l06`, code base `c493b55731545a090d6b81f504bf02e1e427ec74` plus the staged delta): **body updated for MIK-R06.** Purpose now counts 18 cases; a Logic bullet and one row record the moved-row relocation test and its four refusals (ruling Q6; review F1 and N7). The test was appended after L27's (the sync kept both), so no existing row moved. No verification stamp was advanced.
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — one MIK-R27 case (17 collected) and the meaning-change case's origin now carries the base record's `legacyId`.** Purpose, two Logic bullets and one row; the later rows re-pointed by the exact +4 shift. No verification stamp was advanced.
- 2026-09-29T10:05:46+02:00 — 260928-MIK-L12 curator (uncommitted change set on `ar/260928-mik-l12`, code base `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695` plus the staged delta): created this card for the new file MIK-R12 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
