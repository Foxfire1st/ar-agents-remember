# mcp/tests/test_knowledge_guarded_merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_guarded_merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

**The merge's whole contract in five cases**, in the unit-regression lane. The unit population is at its declared `unit_case_budget` ceiling, so this module carries the contract in five named nodes rather than one per scenario, and each node is the node a specific guard is mutation-checked against.

Every case asserts the **whole** outcome — the state, the identity, the refusal code, and that every input is byte-identical to what it was — rather than one field of it. That is the property the module exists to protect: a merge that refuses for the right reason while moving an input, or a merge that succeeds while dropping a side's work, fails here rather than in a downstream consumer.

## Code Commentary

### Logic

- `test_every_structural_violation_is_refused_before_a_session_exists` — compares each input against the declared manifest. `_structural_violations` builds six distinct classes (the set of canonical tables, an added column, a weakened NOT NULL, a wrong foreign key, a dropped trigger, changed table options) plus a reorder and a rename (`_reorder_invariant_columns`, `_rewrite_schema`), a weakened trigger body, a changed `user_version`, and an absent or unreadable input. Every edit is applied through `_edited`/`_mutate`. Fails if any comparison stops refusing.
- `test_an_incomplete_delta_applies_silently_and_is_caught_by_coverage_and_replay` — the **silent-omission class**, and the module's named unit-side guard. `_partial_delta` builds one delta whose session was told about only a subset of the canonical tables — the shape a missing `session.attach` produces in production, where the connection still holds every table and SQLite reports no error. The case asserts that SQLite accepts it and that the coverage comparison and the replay each refuse it. Fails if either comparison stops measuring, or if the not-supplied marker is conflated with a stored SQL `NULL`.
- `test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate` — the conforming case: both sides' own work is retained, the published file is closed, the coverage record is complete, and the outcome carries no verdict field. Fails if either side's work is dropped, if the published file is not closed, or if a publication that changed nothing is reported as a change. **This is the registered evidence node of `contract:common-base-merge-cases`.**
- `test_both_conflicting_edits_refuse_whole_and_preserve_every_input` — the refusal taxonomy: `_same_field_conflict`, `_shared_revision_shape` (two independent insertions under one identity, with equal payloads in the shape the case builds) and `_reference_case` (a removed row the other side's new reference depended on) in **both** orientations. Every refusal also names the row it refused — the exact key the engine handed the conflict callback — which is asserted here rather than left to the boundary module, so this node fails if a key is ever read from the wrong side of a change.
- `test_every_base_and_every_input_defect_refuses_without_moving_a_dataset` — base resolution and input integrity: the ancestry-proven and supplied claims, a history with no common base, a criss-cross history with two (built by `_merge_commit`), a relative repository root, an input that moved after admission, one file named as two roles, `_tamper` (a side that rewrote a sealed revision in place and restored the trigger that refused the write), and an input moved after resolution. Fails if a base is chosen rather than proven, or if an input defect is carried into a merge.

Shared helpers: `assert_refused_without_moving_any_input` (a refused outcome that published nothing and left all three inputs untouched), `assert_removal_orientation` (measures 0/0 anchors and claims on the removing side against 1/1 on the citing side, so the orientation is a measurement rather than a restatement of the parameter), and `assert_input_defects_refuse` (every input defect in one case refuses, and no refusal moves a dataset).

### Conventions

- The two committed artificial states are built through the real store operations or through explicit catalog edits, and every Git object is created by `_commit_on_top`/`_merge_commit` in a temporary repository this module's harness owns. `_git` runs the one scenario Git command through the package's own runner and refuses a failure.
- `_insert_revision` inserts a whole revision row directly, as two independent authors would, because the case is about the collision and not about the store's own path.
- `resolve`/`run`/`base_request` are per-case convenience readers over `merge_case_test_support`, so a case reads as its scenario rather than as its plumbing.

### Invariants And Boundaries

- **Five cases is a budget decision, not a coverage claim.** The module docstring says so, and the boundary scenarios that need their own world live in `test_knowledge_guarded_merge_boundaries.py` (integration lane) instead of being packed in here.
- **Each case asserts the whole outcome.** A node that checked one field would leave the input-preservation property unmeasured, which is the failure mode this leaf's review sealed twice.
- **Boundary.** This module holds the unit-side contract; it does not own the base-resolution or schema modules' internals, and it publishes only into private temporary destinations the harness creates.

### Todos

None recorded for this slice. The unit-population budget is exactly full (1000/1000 collected) after this leaf, which the owning seat reported as a standing decision rather than a defect in this module.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The five-case contract, what each case fails on, and the budget statement. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:1-33 |
| The structural node and its six classes plus reorder, rename, weakened trigger and `user_version`. | "test_every_structural_violation_is_refused_before_a_session_exists" | mcp/tests/test_knowledge_guarded_merge.py:111-180 |
| The registered evidence node of `contract:common-base-merge-cases`. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-312 |
| The conflict node, including the exact conflict-key assertion. | "test_both_conflicting_edits_refuse_whole_and_preserve_every_input" | mcp/tests/test_knowledge_guarded_merge.py:318-386 |
| The base and input-defect node. | "test_every_base_and_every_input_defect_refuses_without_moving_a_dataset" | mcp/tests/test_knowledge_guarded_merge.py:392-486 |
| The partial delta that reproduces a missing `session.attach` and is accepted by SQLite. | `_partial_delta` | mcp/tests/test_knowledge_guarded_merge.py:747-777 |
| The measured orientation assertion that replaced a constant-true predicate. | `assert_removal_orientation` | mcp/tests/test_knowledge_guarded_merge.py:645-660 |
| The harness the cases are built on, and its real three-commit Git scenario. | `build_case`; `GitBranchWorld` | mcp/tests/merge_case_test_support.py:511-571; mcp/tests/merge_case_test_support.py:72-78 |
| The boundary module that carries the scenarios needing their own world. | "Boundary cases for the guarded merge: the conflict row identity and the final-integrity checks." | mcp/tests/test_knowledge_guarded_merge_boundaries.py:1-22 |
| The lane manifest rows that classify both modules. | `unit-regression`; `integration` | mcp/tests/test-evidence-lanes.toml:154; mcp/tests/test-evidence-lanes.toml:138-139 |
|  The governed-artifact registration of the support module these cases share. | "contract:common-base-merge-cases" | mcp/tests/evidence-lifecycle.toml:1132-1152  |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `integration` in the row 72 of this card from mcp/tests/test-evidence-lanes.toml:5-73 to mcp/tests/test-evidence-lanes.toml:154, the extent of the construct the claim is about (the checker named line(s) [154] as its live location)
- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new unit suite. It records the five-case contract, each case's named guard and what it fails on, the whole-outcome assertion rule that makes input preservation measured rather than assumed, and — the fact a successor most needs — that the register-time failure this leaf's review found twice was a *text claim outrunning its bytes*: the module docstring now names the nodes that exist, and `assert_removal_orientation` measures both orientations (0/0 against 1/1) instead of returning a constant-true predicate. It also records that the fifth case holds the conflict key to the engine's own operation, which is the regression guard for the corrected contract. Verification metadata remains empty until closeout stamps the code commit.
