# mcp/tests/test_knowledge_candidate_workspace.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_candidate_workspace.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T11:30+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec`|
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The candidate-lifecycle half of the snapshot protection: **creation, resumption, cloning and disposal
authority**, plus the two durability facts the whole increment rests on — a live reader must not let a closing
writer lose a committed batch, and a real crash must preserve the committed batch while dropping the abandoned
one.

Everything is built by `snapshot_lifecycle_test_support.build_case`, so each case reads as one admitted candidate
plus the operation under test. The registered lane row is
`mcp/tests/test-evidence-lanes.toml:69` (unit-regression); its shared harness carries the registered contract
`knowledge-snapshot-lifecycle-cases`.

## Code Commentary

### Logic

Eleven nodes, each protecting a distinct operation or consequential failure:

- `test_a_created_candidate_reopens_with_its_receipt_and_the_declared_schema` — creation is only `created` if a
  later reopen sees the same identity, the sealed receipt and the declared schema, which is what makes the
  readback-through-the-resume-path ordering meaningful.
- `test_two_candidates_cloned_from_one_baseline_diverge_and_share_no_file_or_row` — two clones of one baseline are
  independent: an authored record in one is absent from the other, and they share no file or row. This is the
  property a copy-based clone would violate.
- `test_an_existing_destination_is_a_resume_attempt_not_an_initialization_target` — a second creation against an
  occupied destination is refused and **writes nothing**, so unpublished authored work cannot be overwritten by a
  routine re-run.
- `test_a_candidate_the_admission_cannot_verify_is_refused_with_its_bytes_intact` — a receipt that is not this
  admission's (or a database bound elsewhere) is refused, and the rows are still there afterwards.
- `test_a_missing_database_or_receipt_is_an_input_error_that_creates_nothing` — an absent input is
  `selected_input_unavailable` naming the path, never an empty dataset, and no destination appears.
- `test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit` — **the upstream L1 durability
  correction's own protection.** A reader holds a read transaction while a writer commits and closes; the
  committed batch must still be readable afterwards. This is the state the removed unconditional peer unlink
  destroyed.
- `test_a_crash_restart_keeps_the_committed_batch_and_drops_the_abandoned_one` — a real child interpreter exits
  with an uncommitted write transaction open; after the restart the committed batch is present and the abandoned
  one is not.
- `test_a_discard_disposition_must_name_the_current_candidate_identity` — an authorization written for an earlier
  state is refused against newer unpublished work.
- `test_a_published_disposition_requires_a_publication_of_that_exact_dataset` — a publication that holds a
  *different* logical dataset does not establish that the candidate's authored work is retained.
- `test_a_failed_candidate_flush_is_refused_before_the_directory_is_exposed` — a durability failure in the expose
  step returns `snapshot_incomplete` and the admitted destination does not exist afterwards, which is the fix for
  the round-1 finding that creation could report `created` after a failed flush.

### Conventions

- The one fixture (`candidate`) returns a `SnapshotCase`; cases call the harness rather than assembling paths, so
  the layout stays declared in one place.
- Assertions are made on **artifacts**: row counts, logical identities, file existence and which peer files are
  present — not on internal call order.
- Two cases deliberately keep a connection open across a boundary (`test_a_live_reader_…`,
  `test_a_crash_restart_…`) because the failure they protect is only reachable in that shape.

### Invariants And Boundaries

- **A refusal must leave the world as it was.** Every refusal case asserts both the refusal code and the absence of
  the side effect (no destination, unchanged rows, unchanged bytes).
- **Durability claims are made against files, not against return values.**
- **The crash case uses a real process.** A simulated crash would prove nothing about SQLite's own recovery.
- **Boundary.** This module is evidence about the lifecycle contract; it defines no rule the operations do not
  already implement, and it does not test publication (that is the sibling module).

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
| The one fixture every case builds on. | `candidate` | mcp/tests/test_knowledge_candidate_workspace.py:56-58 |
| Creation is `created` only if a reopen sees the same identity and sealed receipt. | "test_a_created_candidate_reopens_with_its_receipt_and_the_declared_schema" | mcp/tests/test_knowledge_candidate_workspace.py:57-79 |
| Two clones of one baseline share no file and no row. | "test_two_candidates_cloned_from_one_baseline_diverge_and_share_no_file_or_row" | mcp/tests/test_knowledge_candidate_workspace.py:119-149 |
| An occupied destination is a resume attempt and is refused without writing. | "test_an_existing_destination_is_a_resume_attempt_not_an_initialization_target" | mcp/tests/test_knowledge_candidate_workspace.py:152-172 |
| A candidate the admission cannot verify is refused with its bytes intact. | "test_a_candidate_the_admission_cannot_verify_is_refused_with_its_bytes_intact" | mcp/tests/test_knowledge_candidate_workspace.py:175-198 |
| A missing database or receipt is an input error that creates nothing. | "test_a_missing_database_or_receipt_is_an_input_error_that_creates_nothing" | mcp/tests/test_knowledge_candidate_workspace.py:163-204 |
| The live-reader protection for the removed peer unlink. | "test_a_live_reader_does_not_let_the_write_boundarys_close_lose_the_commit" | mcp/tests/test_knowledge_candidate_workspace.py:206-246 |
| The real-crash restart protection. | "test_a_crash_restart_keeps_the_committed_batch_and_drops_the_abandoned_one" | mcp/tests/test_knowledge_candidate_workspace.py:286-316 |
| The two narrow disposal grounds, each refused against a stale or wrong publication. | "test_a_discard_disposition_must_name_the_current_candidate_identity"; "test_a_published_disposition_requires_a_publication_of_that_exact_dataset" | mcp/tests/test_knowledge_candidate_workspace.py:319-347; mcp/tests/test_knowledge_candidate_workspace.py:350-400 |
| The failed-flush refusal that keeps `created` honest. | "test_a_failed_candidate_flush_is_refused_before_the_directory_is_exposed" | mcp/tests/test_knowledge_candidate_workspace.py:403-425 |
| The shared harness this module exercises the lifecycle through. | `build_case`; `crash_and_abandon` | mcp/tests/snapshot_lifecycle_test_support.py:177-205; mcp/tests/snapshot_lifecycle_test_support.py:477-533 |
| The lifecycle operations these cases protect. | `create_candidate`; `clone_candidate`; `open_candidate`; `authorize_candidate_disposal` | mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:85-98; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:100-126; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:129-138; mcp/src/agents_remember/memory/knowledge/candidate_workspace.py:141-173 |
| The lane row that keeps this module collectable. | "mcp/tests/test_knowledge_candidate_workspace.py" | mcp/tests/test-evidence-lanes.toml:84-84 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_candidate_workspace.py" repointed to mcp/tests/test-evidence-lanes.toml:84-84. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_knowledge_candidate_workspace.py" repointed to mcp/tests/test-evidence-lanes.toml:83-83. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/test_knowledge_candidate_workspace.py" repointed to mcp/tests/test-evidence-lanes.toml:70-70. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): created this one-to-one card for the new candidate-lifecycle suite. It records the eleven distinct operations/failures the nodes protect, with the two durability nodes called out as the protection for the upstream L1 peer-unlink correction (`test_a_live_reader_…` reaches exactly the state an unconditional unlink destroyed, and `test_a_crash_restart_…` uses a real child interpreter), and the convention that refusal cases assert both the refusal and the absence of the side effect. Verification metadata remains empty until closeout stamps the code commit.
