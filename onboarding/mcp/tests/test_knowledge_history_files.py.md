# mcp/tests/test_knowledge_history_files.py

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
- `test_row_kind_registry_owns_disjoint_subject_forms`: the six registered kinds (`invariant`,
  `family`, since MIK-R24 MIK-R30's `onboarding_trace`, since MIK-R11 `planned`, since MIK-R10
  `unexplained`, and since MIK-R14 `reconsideration`), **compared as a set since MIK-R14**: leaves register in
  landing order, so the order is not asserted (review F9); the duplicate-name check the ordered list gave is gone,
  while subject disjointness is still asserted below it (review N4, accepted as a note). MIK-R10's own row cases
  are in `test_unexplained_change_disposition.py` and MIK-R14's in `test_reconsideration_surfacing.py`. The case also asserts the subject dispatch (an
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
- **L37 (INV-XN0FG8).** `test_revision_binding_for_invariant_and_family_rows` also pins the three rule functions:
  a `changed` row at an unchanged revision is accepted only when `restated_revision` equals that revision;
  `changed_record_row_violation` refuses a `no_impact` or `moved` row while the base and candidate revisions
  differ, and accepts `changed` and `deleted`; `changed_family_row_violation` accepts only `changed` and `retired`
  for a family whose guarantee changed, and anything for one whose guarantee is as it was.

### Conventions

Documents are built from small dict helpers (`_anchor`, `_cover`, `_invariant_row`, `_family_row`,
`_history`) and refused through `_refused`, matching the idiom of `test_knowledge_file_formats.py`.

### Invariants And Boundaries

- A closed history file must be byte-identical on every later side; a reformat counts as an edit.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R07@v2` of task
`260928_maintained-invariant-knowledge`, which lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases cover `models/knowledge_files/history.py` and its registration in `documents.py`.

- The conforming example and the owner path. [1]
- File shape, owner and uniqueness. [2]
- The row-kind registry, with the six kinds as a set (MIK-R10 adds `unexplained`, MIK-R14 `reconsideration`). [3]
- Invariant dispositions, covers and effects. [4]
- Family rows. [5]
- Re-anchoring against the candidate. [6]

- The revision binding. [7]

- The freeze predicate. [8]
- The parallel merge in a real repository. [9]
- Lane registration. [10]

- The governing-row rules for a changed invariant and a family with a changed guarantee. [11]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is crossed by this file.
