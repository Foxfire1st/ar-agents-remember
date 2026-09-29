# mcp/tests/test_knowledge_history_files.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_history_files.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T06:00:00+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f`|
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R07: per-leaf history files (`ar-history/v1`) at model level.** The cases pin each
disposition and row shape, the revision binding, the freeze predicate, and that two leaves' history
files merge without conflict. The writer's own tests belong to MIK-R12 and the validator's freeze
test to MIK-R22. Registered in the `unit-regression` lane; 9 tests, 29 collected cases.

## Code Commentary

### Logic

- `test_conforming_example_parses_at_its_owner_path_and_formats_canonically`: the packet's
  conforming example (a no-impact invariant row plus a family row) formats canonically, parses at
  `knowledge/history/260928-MIK-L07.json`, and is refused at any other path; a no-impact judgment
  placed inside an invariant record is refused as an extra input.
- `test_file_shape_owner_and_row_uniqueness_are_enforced`: exactly one of `leaf`/`wave`/`crossing`,
  the crossing pattern, strict `closed`, unique row IDs and subjects, and `mint_id("history_row")`.
- `test_row_kind_registry_owns_disjoint_subject_forms`: the three registered kinds (`invariant`,
  `family` and, since MIK-R24, MIK-R30's `onboarding_trace`), their subject dispatch (an
  `onboarding:<path>` subject now dispatches to `onboarding_trace`), the refusal of an unclaimed subject
  (`DEC-…`, a legacy `INV-0143`), and both disposition tuples.
- `test_invariant_row_dispositions_and_shape` (parametrized): every invariant disposition with
  accepted and refused covers and effects, including `moved` refusing an added or removed entry and
  a blob-only change counting as re-anchoring; each accepted row round-trips.
- `test_family_row_dispositions_and_examined_members`: family dispositions and unique members.
- `test_after_anchor_must_equal_the_entry_anchor_in_the_candidate`: `reanchor_mismatches` against
  a real `FileSidecar`, plus `unknown_subjects`.
- `test_revision_binding_for_invariant_and_family_rows`: `changed` is exactly K_B + 1 (no repeat,
  no jump), other dispositions keep the revision, `deleted` is free, and `stale_examined_members`.
- `test_closed_in_base_implies_byte_identical_in_candidate`: `closed_copy`, `is_closed_history`
  (including the schema check), and `frozen_history_violation` for edits, reformatting, deletion
  and a merge parent; `empty_history(..., closed=True)`.
- `test_two_parallel_leaves_merge_their_history_files_without_conflict`: in a real git repository,
  two leaf branches each add their closed history file; both merge cleanly and each merged file is
  byte-identical and parses.

### Conventions

Documents are built from small dict helpers (`_anchor`, `_cover`, `_invariant_row`, `_family_row`,
`_history`) and refused through `_refused`, matching the idiom of `test_knowledge_file_formats.py`.

### Invariants And Boundaries

- A closed history file must be byte-identical on every later side; a reformat counts as an edit.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R07@v2` of task
`260928_maintained-invariant-knowledge`, which lives outside the code and memory repositories, so it
is named here and not cited as a row.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases cover `models/knowledge_files/history.py` and its registration in `documents.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The conforming example and the owner path. | `test_conforming_example_parses_at_its_owner_path_and_formats_canonically` | mcp/tests/test_knowledge_history_files.py:111-144 |
| File shape, owner and uniqueness. | `test_file_shape_owner_and_row_uniqueness_are_enforced` | mcp/tests/test_knowledge_history_files.py:147-165 |
| The row-kind registry, with the three kinds. | `test_row_kind_registry_owns_disjoint_subject_forms` | mcp/tests/test_knowledge_history_files.py:168-183 |
| Invariant dispositions, covers and effects. | `test_invariant_row_dispositions_and_shape` | mcp/tests/test_knowledge_history_files.py:200-240 |
| Family rows. | `test_family_row_dispositions_and_examined_members` | mcp/tests/test_knowledge_history_files.py:243-251 |
| Re-anchoring against the candidate. | `test_after_anchor_must_equal_the_entry_anchor_in_the_candidate` | mcp/tests/test_knowledge_history_files.py:259-283 |
| The revision binding. | `test_revision_binding_for_invariant_and_family_rows` | mcp/tests/test_knowledge_history_files.py:286-308 |
| The freeze predicate. | `test_closed_in_base_implies_byte_identical_in_candidate` | mcp/tests/test_knowledge_history_files.py:320-348 |
| The parallel merge in a real repository. | `test_two_parallel_leaves_merge_their_history_files_without_conflict` | mcp/tests/test_knowledge_history_files.py:361-385 |
| Lane registration. | "mcp/tests/test_knowledge_history_files.py" | mcp/tests/test-evidence-lanes.toml:98-98 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): The registry case now asserts three kinds, including MIK-R30's `onboarding_trace`, which MIK-R24 registers; an `onboarding:` subject now dispatches to it. Reworded the bullet and the row, and re-measured the row (`168-183`).
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta, after worker fix round 1): created this card for the new test file MIK-R07 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
