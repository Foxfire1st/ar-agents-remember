# mcp/tests/test_knowledge_guarded_merge.py

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
- `test_both_conflicting_edits_refuse_whole_and_preserve_every_input` — the refusal taxonomy: `_same_field_conflict`, `_shared_revision_shape` (two independent insertions under one identity, with **different** payloads in the shape the case builds) and `_reference_case` (a removed row the other side's new reference depended on) in **both** orientations. Every refusal also names the row it refused — the exact key the engine handed the conflict callback — which is asserted here rather than left to the boundary module, so this node fails if a key is ever read from the wrong side of a change. **The two orientations are also asserted to be two different conflicts to recover from, not one conflict reached two ways.** The precondition the merge measured is `arriving_insertion` where the removal happened on the retained side and `no_arriving_insertion` where the arriving side performed it, and `expressible_decisions` consequently answers `("keep-left",)` in the first orientation and `()` in the second — so a case that found one offer for both would fail here. That is the unit-boundary half of the CYCLE-02 residue: the orientation with nothing to retract admits no decision, while the code, the attribution and the refusal's own next action are unchanged; and the row-less decision stays a nameable input (`AuthoredReconciliation(decision="keep-left")` still validates with no row), so what narrowed is the offer and not the vocabulary. Both orientations stay inside this one collected case because the ceiling the module was written against was exact and an added collected case would have breached it.
  - **Correction, leaf `260915-KS-L47`.** This sentence previously claimed the case was built *"with equal payloads in the shape the case builds"*. That was false: `_shared_revision_shape` gives the two sides different `display_version` and `statement` values, so the case proves the refusal for a *diverging* payload and could not prove the equal-payload property at all. The word "equal" is struck rather than reworded, and the missing property is now measured by a second shape inside this same collected case (below).
  - **The equal-payload insertion is a second, separately asserted variant of the same case** (`_equal_payload_revision_shape`). It inserts one identical complete revision row on both sides — same statement, display version, applicability, conditions, exclusions, state, acceptance_ref, provenance and payload_digest — and asserts the same `duplicate_identity` refusal with every input byte-unchanged, which is the property the developer required be preserved and which no case measured before this leaf. It stays inside this collected case because the guarantee is that exactly one insertion identity is refused, not that a second node exists.
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

None recorded for this slice. The declared ceilings are 2300 unit and 400 integration cases in the root `pyproject.toml`, and both populations stand at them, so this leaf asserted new facts inside already-collected cases rather than adding one — an added collected case would put the lane over its ceiling, where the gate raises and the whole lane then executes zero tests. The owning seat reported the budget position as a standing decision rather than a defect in this module.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The five-case contract, what each case fails on, and the budget statement. [1]
- The structural node and its six classes plus reorder, rename, weakened trigger and `user_version`. [2]
- The registered evidence node of `contract:common-base-merge-cases`. [3]
- The conflict node, including the exact conflict-key assertion and the two orientations' differing retraction precondition. [4]
- The base and input-defect node. [5]
- The partial delta that reproduces a missing `session.attach` and is accepted by SQLite. [6]
- The measured orientation assertion that replaced a constant-true predicate. [7]
- The harness the cases are built on, and its real three-commit Git scenario. [8]
- The boundary module that carries the scenarios needing their own world. [9]
- **The lane manifest row that classifies the unit half — the lane header itself, not one of its member rows.** [10]
- **The lane manifest row that classifies the integration half — the lane header itself.** [11]
- The governed-artifact registration of the support module these cases share. [12]
- The lane manifest rows that classify both modules. [13]
- The governed-artifact registration of the support module these cases share. [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
- The governed-artifact registration of the support module these cases share. [15]
