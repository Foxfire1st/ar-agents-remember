# mcp/tests/test_knowledge_snapshot_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_snapshot_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697`|
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one fixture every case builds on. | `candidate` | mcp/tests/test_knowledge_snapshot_publication.py:46-49 |
| A published snapshot reopens to the records and is a closed database. | "test_a_published_snapshot_reopens_to_the_candidate_records_and_is_closed" | mcp/tests/test_knowledge_snapshot_publication.py:51-79 |
| The load-bearing node: a WAL-resident batch is published whole while a main-file copy is not. | "test_a_wal_resident_batch_is_published_whole_while_a_main_file_copy_is_not" | mcp/tests/test_knowledge_snapshot_publication.py:81-110 |
| The failed replacement that leaves the prior destination byte-identical. | "test_a_failed_replacement_leaves_the_prior_destination_byte_identical" | mcp/tests/test_knowledge_snapshot_publication.py:173-173 |
| The honest durability report when the readback fails. | "test_a_publication_whose_readback_fails_reports_the_destination_it_actually_left" | mcp/tests/test_knowledge_snapshot_publication.py:204-204 |
| The logical no-op that retains the published bytes. | "test_a_logical_no_op_retains_the_published_bytes" | mcp/tests/test_knowledge_snapshot_publication.py:239-239 |
| The byte-level destination-stale assertion. | "test_a_destination_that_moved_since_the_admitted_identity_is_refused_untouched" | mcp/tests/test_knowledge_snapshot_publication.py:265-265 |
| The two candidate-moved refusals across the admission/acquisition window. | "test_a_candidate_that_moved_after_admission_is_refused_rather_than_published_fresher"; "test_a_candidate_that_moves_between_admission_and_acquisition_is_refused" | mcp/tests/test_knowledge_snapshot_publication.py:312-312; mcp/tests/test_knowledge_snapshot_publication.py:332-332 |
| The pinning proof: a write landing during the freeze stays out of the snapshot. | "test_a_write_that_lands_during_the_freeze_stays_out_of_the_published_snapshot" | mcp/tests/test_knowledge_snapshot_publication.py:359-359 |
| The stage-digest re-check that refuses a replaced stage. | "test_a_prepared_stage_that_is_not_the_verified_file_is_not_installed" | mcp/tests/test_knowledge_snapshot_publication.py:391-391 |
| The read-side gate until a publication happens. | "test_a_newer_runtime_candidate_reports_candidate_snapshot_unpublished_until_published" | mcp/tests/test_knowledge_snapshot_publication.py:424-424 |
| The flush failure that is a refusal rather than an escaping error. | "test_a_failed_stage_flush_is_refused_before_the_destination_is_replaced" | mcp/tests/test_knowledge_snapshot_publication.py:464-464 |
| The publication operations these cases protect. | `publish_candidate_snapshot`; `publish_prepared_snapshot` | mcp/src/agents_remember/memory/knowledge/publication.py:66-111; mcp/src/agents_remember/memory/knowledge/publication.py:114-170 |
| The freeze whose closedness the load-bearing node measures. | `freeze_closed_snapshot` | mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109 |
| The read-side gate and its refusal restatement. | `publication_state`; `unpublished_refusal` | mcp/src/agents_remember/memory/knowledge/materialization.py:34-99; mcp/src/agents_remember/memory/knowledge/materialization.py:102-120 |
| The shared harness these cases are built on. | `build_case`; `publish`; `byte_copy`; `journal_peer_names` | mcp/tests/snapshot_lifecycle_test_support.py:177-205; mcp/tests/snapshot_lifecycle_test_support.py:357-380; mcp/tests/snapshot_lifecycle_test_support.py:453-459; mcp/tests/snapshot_lifecycle_test_support.py:410-418 |
| The lane row that keeps this module collectable. | "mcp/tests/test_knowledge_snapshot_publication.py" | mcp/tests/test-evidence-lanes.toml:92-92 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_knowledge_snapshot_publication.py" repointed to mcp/tests/test-evidence-lanes.toml:92-92. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 14 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_knowledge_snapshot_publication.py`, `test_a_candidate_that_moved_after_admission_is_refused_rather_than_published_fresher`, `test_a_candidate_that_moves_between_admission_and_acquisition_is_refused`, `test_a_failed_replacement_leaves_the_prior_destination_byte_identical`, `test_a_publication_whose_readback_fails_reports_the_destination_it_actually_left`, `test_a_logical_no_op_retains_the_published_bytes`, `test_a_destination_that_moved_since_the_admitted_identity_is_refused_untouched`, `test_a_write_that_lands_during_the_freeze_stays_out_of_the_published_snapshot` and 3 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 12 generated projection bullet(s) by hand** — `mcp/tests/test_knowledge_snapshot_publication.py`, `test_a_candidate_that_moved_after_admission_is_refused_rather_than_published_fresher`, `test_a_candidate_that_moves_between_admission_and_acquisition_is_refused`, `test_a_failed_replacement_leaves_the_prior_destination_byte_identical`, `test_a_publication_whose_readback_fails_reports_the_destination_it_actually_left`, `test_a_logical_no_op_retains_the_published_bytes`, `test_a_destination_that_moved_since_the_admitted_identity_is_refused_untouched`, `test_a_write_that_lands_during_the_freeze_stays_out_of_the_published_snapshot` and 3 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_knowledge_snapshot_publication.py"` → `mcp/tests/test-evidence-lanes.toml:87-87`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/tests/test_knowledge_snapshot_publication.py:332 to the row 105 of this card as the citation for `test_a_candidate_that_moves_between_admission_and_acquisition_is_refused`: no cited file carried the construct, and the checker named line(s) [332] in this file as its live location

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_a_candidate_that_moves_between_admission_and_acquisition_is_refused` in the row 105 of this card from mcp/tests/test_knowledge_snapshot_publication.py:312-314 to mcp/tests/test_knowledge_snapshot_publication.py:332-334, the extent of the construct the claim is about (the checker named line(s) [332] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `test_a_candidate_that_moved_after_admission_is_refused_rather_than_published_fresher` in the row 105 of this card from mcp/tests/test_knowledge_snapshot_publication.py:332-334 to mcp/tests/test_knowledge_snapshot_publication.py:312-314, the extent of the construct the claim is about (the checker named line(s) [312] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_knowledge_snapshot_publication.py:312-314 in the row 105 of this card; the repetition added no pooled evidence

- 2026-09-16T09:30:00+00:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new publication suite. It records the twelve nodes one per observable failure or property, and singles out the load-bearing node — a WAL-resident committed batch survives into the published snapshot while a bare main-file copy of the same database does not carry it — because that measurement is what distinguishes a closed snapshot from a `cp`, and it is the evidence node the registry contract declares. Also recorded: refusal cases assert the refusal and the untouched destination together, and `no_change` is asserted to retain the same bytes. Verification metadata remains empty until closeout stamps the code commit.
