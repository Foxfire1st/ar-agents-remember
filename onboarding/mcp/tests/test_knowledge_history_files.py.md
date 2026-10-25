# mcp/tests/test_knowledge_history_files.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R07: per-leaf history files (`ar-history/v1`), their models and the Writer/validator item-token boundary.** The cases pin each
disposition and row shape, the revision binding, the freeze predicate, and that two leaves' history
files merge without conflict. Other writer tests belong to MIK-R12 and the broader validator freeze cases to MIK-R22; this module now also exercises their token-admission boundary. Registered in the `unit-regression` lane. The earlier 9-test/29-collected-case snapshot is historical; this read-only review did not collect or run tests.

## Code Commentary

### Logic

- `test_conforming_example_parses_at_its_owner_path_and_formats_canonically`: the packet's
  conforming example (a no-impact invariant row plus a family row) formats canonically, parses at
  `knowledge/history/260928-MIK-L07.json`, and is refused at any other path; a no-impact judgment
  placed inside an invariant record is refused as an extra input.
- `test_file_shape_owner_and_row_uniqueness_are_enforced`: exactly one of `leaf`/`wave`/`crossing`,
  the crossing pattern, strict `closed`, unique row IDs and subjects, and `mint_id("history_row")`.
- `test_row_kind_registry_owns_disjoint_subject_forms`: eight kinds (`invariant`, `family`,
  `onboarding_trace`, `planned`, `unexplained`, `reconsideration`, and MIK-R53 `membership`/`record`),
  compared as a set, not registration order (review F9). Subject disjointness remains asserted
  (review N4). MIK-R10 cases remain in `test_unexplained_change_disposition.py`, MIK-R14
  in `test_reconsideration_surfacing.py`. The case dispatches onboarding to `onboarding_trace`
  and `DEC-7K3F9Q` to `record`; unclaimed subjects are `hunk:abc` and legacy `INV-0143`. Both
  invariant/family disposition tuples remain asserted.
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
- `test_short_items_are_judged_only_in_the_files_the_reanchor_check_reads` (renamed from
  `test_validator_refuses_short_items_without_closed_comparison_base`; five parametrised
  `(closed, base_state, publication, judged)` cases): an open file is judged, also when a comparison
  base holds it open; the leaf's own closed file is judged at its publication; a closed file at a
  master checkpoint, a master-level landing or a sync is **not** judged (MIK-R180; MIK-R52 rule 5
  covers it there); and a file closed by an earlier frozen closeout of the same leaf is not judged.
  The former `(closed, "open")` case is not among the five: it asserted a refusal for a closed
  candidate file whose base holds it open at a route with no publication operand, where that file is
  no longer selected; at a leaf publication the same shape is selected and judged.
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

Newly authored history item tokens must be full `sha256:` plus64hex digits, accepting either hex case; malformed values refuse without changing memory. Stored closed comparison-base history with old short labels parses, validates and round-trips byte-exact. The item check shares the re-anchor check's population (MIK-R180). At a route that is not a leaf publication — a master's checkpoint, a master-level landing or a sync — a closed file is outside that population whether or not a comparison base holds it closed; at a leaf publication the leaf's own file stays inside it even when the comparison base is absent or holds the file open, and only a file closed in a comparison base or in a frozen commit of the same leaf is historical. A separately frozen publication tree is therefore outside both checks rather than granted the old closed-base reading exception. The duplicate-item shape control now uses valid full hashes so it still tests duplication rather than malformed tokens.

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

- The registry set includes eight kinds, with MIK-R53 membership/record; decision dispatch and unclaimed hunk/legacy invariant subjects are explicit. [3]
- Current source delta inspected statically: Repair six-kind registry and unclaimed-decision prose/caption against exact current assertions; retain set semantics, model/revision/freeze facets and historical execution limits. [12]

- Writer and validator token tests distinguish new full-hash admission. [13]
- Stored closed comparison-base legacy items parse, validate and round-trip unchanged. \ [14]
- Item tokens are judged only in the files the re-anchor check reads: five file/base/route shapes. \ [15]
