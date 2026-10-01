# mcp/tests/test_knowledge_snapshot_publication.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

The publication half of the snapshot protection: **replace-or-nothing, closedness, identity comparison and the
read-side publication gate**.

This module carries the increment's one genuinely load-bearing evidence node —
`test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not` (declared as the evidence node of the
`knowledge-snapshot-lifecycle-cases` contract) — because a published snapshot that is not *closed* would reopen to
older records than the candidate it was copied from, and nothing else in the system would notice.

Everything is built by `snapshot_lifecycle_test_support.build_case`. The registered lane row is
`mcp/tests/test-evidence-lanes.toml:75` (unit-regression).

## Code Commentary

### Logic

Twelve nodes, one per observable failure or property of the publication contract:

- `test_a_published_snapshot_reopens_to_the_candidate_records_and_is_closed` — the published file reopens to the
  authored records, declares the `delete` journal mode and has no journal/WAL peer beside it.
- `test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not` — **the load-bearing node.** A
  committed-but-WAL-resident batch survives into the published snapshot, while a plain main-file copy of the same
  database does not carry it. This is the difference between a snapshot and a `cp`, measured on both files.
- `test_a_failed_replacement_leaves_the_prior_destination_byte_identical` — a failing replace refuses and the
  previous destination is unchanged to the byte.
- `test_a_publication_whose_readback_fails_reports_the_destination_it_actually_left` — the honest durability code:
  when the replacement completed but the destination cannot be re-read, the result says so and does **not** claim
  the old file is still there.
- `test_a_logical_no_op_retains_the_published_bytes` — an identical logical dataset (different physical layout)
  returns `no_change` and keeps the existing bytes, so a tree is not dirtied for a change no reader could observe.
- `test_a_destination_that_moved_since_the_admitted_identity_is_refused_untouched` — the admitted
  `expected_destination` is compared exactly, and a destination that is not it is refused without being replaced.
- `test_a_candidate_that_moved_after_admission_is_refused_rather_than_published_fresher` — a fresher candidate is
  never silently published in place of the selected one; the refusal names both digests.
- `test_a_candidate_that_moves_between_admission_and_acquisition_is_refused` — the same rule as observed at the
  other end of the window (the identity re-checked under the candidate lock).
- `test_a_write_that_lands_during_the_freeze_stays_out_of_the_published_snapshot` — the pinning is real: a write
  committed after the freeze does not appear in the published file, which is what makes the frozen identity a
  point in time rather than a moving target.
- `test_a_prepared_stage_that_is_not_the_verified_file_is_not_installed` — the reusable install half re-checks the
  stage's physical digest, so a stage replaced between freezing and installing is refused.
- `test_a_newer_runtime_candidate_reports_candidate_snapshot_unpublished_until_published` — the read-side gate
  reports `candidate_snapshot_unpublished` (and restates it as a refusal) until the publication happens.
- `test_a_failed_stage_flush_is_refused_before_the_destination_is_replaced` — a flush failure in the freeze is a
  `snapshot_incomplete` refusal, not an escaping error, and the destination is untouched.

### Conventions

- Cases assert on the artifacts: byte digests of the destination, the presence/absence of journal peers, the
  journal mode read from the file header, and the logical identity read through a read-only connection.
- The `test_a_…_is_not` half of the load-bearing node is what makes it evidence rather than a restatement: the
  same database copied as a bare main file is shown **not** to carry the batch.
- Refusal cases assert the code and the untouched destination together.

### Invariants And Boundaries

- **A refusal never replaces the destination, and the assertion is byte-level.**
- **Closedness is proven by reopening**, not inferred from the copy having succeeded.
- **`no_change` is asserted to retain the same bytes**, which is what keeps a publication from dirtying a memory
  tree.
- **Boundary.** This module is evidence about the publication contract; it defines no rule the operations do not
  already implement, and it does not test the candidate lifecycle (that is the sibling module).

### Todos

None recorded for this slice.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The one fixture every case builds on. [1]
- A published snapshot reopens to the records and is a closed database. [2]
- The load-bearing node: a WAL-resident batch is published whole while a main-file copy is not. [3]
- The failed replacement that leaves the prior destination byte-identical. [4]
- The honest durability report when the readback fails. [5]
- The logical no-op that retains the published bytes. [6]
- The byte-level destination-stale assertion. [7]
- The two candidate-moved refusals across the admission/acquisition window. [8]
- The pinning proof: a write landing during the freeze stays out of the snapshot. [9]
- The stage-digest re-check that refuses a replaced stage. [10]
- The read-side gate until a publication happens. [11]
- The flush failure that is a refusal rather than an escaping error. [12]
- The publication operations these cases protect. [13]
- The freeze whose closedness the load-bearing node measures. [14]
- The read-side gate and its refusal restatement. [15]
- The shared harness these cases are built on. [16]
- The lane row that keeps this module collectable. [17]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
