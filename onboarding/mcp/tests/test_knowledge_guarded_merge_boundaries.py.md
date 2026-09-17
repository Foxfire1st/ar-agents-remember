# mcp/tests/test_knowledge_guarded_merge_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_guarded_merge_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The merge's boundary cases — the conflict row identity and the final-integrity checks — in the integration lane.** They live here rather than as more assertions inside an existing unit case because each needs its own scenario, and the unit population is at its declared ceiling so a new case cannot be added there.

Two subjects, and the second one is a recorded *non-experiment* rather than a claim of coverage:

1. **The row identity a conflict reports.** A changeset supplies only the columns an operation changes, so the new side of an `UPDATE` carries the not-supplied marker where its key columns are, and a key read from there names no row. The engine does hand the conflict callback the operation it refused, and its *old* values carry the key. These cases hold that to the two shapes where the earlier version of the code was wrong: a conflict on a row that is **not the first one in the table**, and a table carrying an insert alongside a conflicting update.
2. **The final-integrity checks and which of them a case can reach.** The merge validates its candidate three ways. `require_structural_validity` is reachable and has a failing case here: a candidate carrying a foreign-key violation, built from inputs that *all* carry it so no delta would otherwise mention it and the candidate is the first place it can be seen. `require_applied_changes` and the merged-candidate `require_immutable_revisions_preserved` cannot be reached by a black-box case at all — the merged candidate is a copy of the left side with the right delta applied, the left side has already passed the immutability comparison, and SQLite's application cannot drop an operation under this schema. Their docstrings say so and the cases below exercise their **policies directly**, so the refusals they produce are demonstrated rather than assumed.

## Code Commentary

### Logic

- `test_a_row_level_conflict_names_the_row_the_engine_refused` — both sides edit the label of an invariant the base already has, and each side also authors its own extra invariant, so a key taken from the *first* operation the changeset carries for `invariant` would name the authored row while the engine's own change names the edited one.
- `test_a_table_carrying_an_insert_and_a_conflicting_update_names_the_conflicting_row` — one table, two operations, one conflict: the record names the operation that conflicted. The case does not depend on which operation the changeset materialises first.
- `test_the_conflict_record_prefers_the_old_side_and_reports_a_missing_key_as_such` — the key renderer's two facts: an `INSERT` is the one operation with no old side, so the new side is the whole row; and an operation whose change carries no primary-key columns names no row and is reported as naming none rather than as some nearby row.
- `test_a_candidate_carrying_a_foreign_key_violation_is_refused_by_the_structural_check` — the reachable final-integrity guard. `_add_dangling_claim` inserts a realization claim whose anchor does not exist with FK enforcement off. Identity admission reads rows, the preflight reads the catalog, and the coverage replay compares logical bodies — **none of which inspects foreign keys**, which is exactly why the candidate's own check is the first place the violation can be seen.
- `test_a_candidate_that_dropped_an_intended_change_is_refused` — the applied-change policy exercised directly: the candidate is a copy of the left side, structurally valid, preserving the base's sealed aggregates, and missing the change the right delta carried.
- `test_a_candidate_missing_a_sealed_aggregate_is_refused` — the merged-candidate immutability policy exercised directly. `_remove_sealed_revision` deletes one sealed revision row the way only a damaged file could lose it and **restores the trigger afterwards**, so what is under test is the comparison and not the schema.

`resolve`/`run`/`case` are the per-case convenience readers over `merge_case_test_support`; every case resolves its base by ancestry and merges without publishing anything.

### Conventions

- The three direct-policy cases construct their candidate by copying the left side and damaging it in one specific way, so each is a statement about one comparison rather than about the application step.
- The two conflict-identity cases deliberately construct a table with more than one operation, because a single-operation table could not distinguish "the engine's operation" from "the first operation".

### Invariants And Boundaries

- **A survivor here is documented as a non-experiment, not as coverage.** The module's docstring, `merge_validation.py`'s docstrings and `merge.py`'s `_freeze_merged` docstring all state the same fact, and the mutation matrix records `M16`, `M20`, `M21` and `M22` as non-experiments with their causes named. Presenting any of them as a killed guard is the defect this leaf's review round 3 corrected.
- **Every case asserts the refusal it names.** A direct-policy case proves the *policy*, not the call site; the call site's unreachability is a fact about the code, stated where the code is.
- **No case writes outside its private temporary world.** Every database, commit and destination is created by the harness under a per-case temporary root.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's two subjects, including why two of the final-integrity checks are policy cases rather than black-box cases. | "Boundary cases for the guarded merge: the conflict row identity and the final-integrity checks." | mcp/tests/test_knowledge_guarded_merge_boundaries.py:1-22 |
| The conflict row identity on a row that is not the table's first, and the insert-plus-update shape. | "test_a_row_level_conflict_names_the_row_the_engine_refused" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:100-132 |
| The insert-plus-conflicting-update node. | "test_a_table_carrying_an_insert_and_a_conflicting_update_names_the_conflicting_row" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:135-162 |
| The old-side preference and the honest missing-key report. | "test_the_conflict_record_prefers_the_old_side_and_reports_a_missing_key_as_such" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:165-184 |
| The reachable structural guard and the dangling claim that reaches it. | "test_a_candidate_carrying_a_foreign_key_violation_is_refused_by_the_structural_check" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:187-226 |
| The two direct-policy nodes for the unreachable call sites, and the trigger-restoring damage they build. | "test_a_candidate_that_dropped_an_intended_change_is_refused"; "test_a_candidate_missing_a_sealed_aggregate_is_refused"; `_remove_sealed_revision` | mcp/tests/test_knowledge_guarded_merge_boundaries.py:229-249; mcp/tests/test_knowledge_guarded_merge_boundaries.py:252-272; mcp/tests/test_knowledge_guarded_merge_boundaries.py:298-314 |
| The unreachability statements the two policy nodes correspond to. | `require_applied_changes`; `require_immutable_revisions_preserved` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:169-211; mcp/src/agents_remember/memory/knowledge/merge_validation.py:104-152 |
| The conflict key the first two nodes hold to the engine's own operation. | `_conflicting_key`; `AppliedChangeset` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:266-289; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:133-157 |
| The harness these cases are built on. | `build_case`; `copy_closed`; `materialize_commit` | mcp/tests/merge_case_test_support.py:511-571; mcp/tests/merge_case_test_support.py:219-239; mcp/tests/merge_case_test_support.py:474-484 |
| The integration-lane row that classifies this module outside the unit budget. | `integration` | mcp/tests/test-evidence-lanes.toml:154-154 |
| The unit module that carries the rest of the contract. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:1-33 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T06:49:47+00:00: Generated citation repair: `integration` repointed to mcp/tests/test-evidence-lanes.toml:154-154. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new boundary module. It records the two subjects and, as the fact a successor most needs, that the module **declares its own non-experiments**: the applied-change check and the merged-candidate immutability check are unreachable by a black-box case under this schema, so their policies are exercised directly and their call-site unreachability is stated where the code is — this is the correction review round 3 made after a *broken* mutant (`NameError`) was wrongly scored as a killed guard. It also records why the two conflict-identity cases construct a table with more than one operation, and that the first two nodes are the regression guard for the corrected old-side key contract. Verification metadata remains empty until closeout stamps the code commit.
