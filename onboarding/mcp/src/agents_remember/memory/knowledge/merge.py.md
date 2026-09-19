# mcp/src/agents_remember/memory/knowledge/merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The guarded common-base merge itself.** It takes a resolution that has already proven which dataset is the common base (see `merge_base.py`), two sides derived from it and a private workspace, and it either produces a structurally valid candidate or refuses with a typed code. It is the only caller of this package's preflight, changeset, coverage, integrity, conflict and postcondition steps, so the sequence in its module docstring *is* the contract: each step exists because the step before it cannot see what it prevents.

Its successful state is `structurally_merged` and that is the entire claim. Nothing on this path installs a Git merge driver, configures an attribute, creates a commit, moves a ref, strips a conflicting operation, prefers one side's value, builds a patchset, or attaches a verdict about whether the merged knowledge is correct.

## Code Commentary

### Logic

`merge_knowledge_datasets(request)` runs the sequence inside one owned workspace (`tempfile.mkdtemp`, removed in `finally`), and every failure path returns a typed refusal rather than escaping as a raw `OSError`/`apsw.Error`:

1. `require_session_capability(MERGE_OPERATION)` — the selected binding must be able to produce and apply a changeset at all.
2. `_resolve_databases(request)` — each role's path must be there, or `_unavailable` names the role.
3. `require_distinct_roles` runs **before** the identity comparison, so a self-merge reports `selected_input_unavailable` rather than a downstream stale-identity symptom.
4. `require_admitted_identities(run)` — each dataset's logical identity is re-read and compared with the identity the resolution admitted. Base resolution already checked this once; it is repeated here because the merge reads the files again, and a dataset that moved between the two steps would otherwise be diffed against a base the caller never admitted.
5. `_preflight(databases)` — every input's declared structure is compared against the one supported generation **before a session exists** (see `merge_schema.py`).
6. `_build_covered_deltas(run)` — one delta at a time, each replayed into a fresh copy of the base and recorded (`_coverage_of`); `_coverage_refusal` refuses a table whose rows differ but whose delta carried no operation.
7. `_require_side_integrity(databases)` — each side's sealed revisions must still be the aggregates the base sealed.
8. `_apply_and_validate(run)` — a private target is created from the **left** side, the right delta is applied with `flags=0`, no filter and an always-aborting conflict callback, then `merge_validation`'s postconditions run.
9. `_publish(run, merged_path)` — only when the caller named a destination: `_freeze_merged` freezes the temporary through the closed-snapshot procedure under the temporary's own lock, then `publish_prepared_snapshot` installs it under the destination's lock.

`MergeRun` is the mutable working record: its coverage list grows as each delta is measured, so a refusal late in the sequence still carries the coverage the operation had already proved. `KnowledgeMergeDefect` is reserved for an internal state the sequence itself makes unreachable.

**The candidate's route hierarchy is judged inside step 8's own transaction.** `MergeRun.acyclic_routes` runs `require_acyclic_routes(connection, repository_id, MERGE_OPERATION)` over the merged candidate's repository id, and `_apply_and_validate` hands it to `apply_changeset` as `within_transaction`, so the rule runs on the same connection **after the right delta was applied and before that application is committed**: a candidate that reparents a route into a cycle is rolled back rather than published, and the refusal is returned through `run.refused(applied.refusal)` before the conflict branch. The rule itself stays the one walk in `memory/knowledge/routes.py` — the operation parameter exists so *this* caller's refusal is attributed to `merge_knowledge_datasets` rather than to the authoring operation — and it has to run here because `route` is inside the merge's attached table set and a right-side `route.parent_route_id` change is a real operation the replay performs, so a merge with no guard on this path would publish a cyclic hierarchy. Two other positions are deliberately not used: before the application the rule would judge the delta rather than the result, and after the commit it would leave a committed candidate the caller then rejects.

**The conflict taxonomy** is `_TAXONOMY`, keyed by `(SQLite conflict code, whether the table is a relationship table)`: `DATA` → `conflicting_values`, `NOTFOUND` → `delete_reference_conflict`, `CONFLICT` → `duplicate_identity`, `CONSTRAINT` → `duplicate_relationship` on the two relationship tables (`family_member`, `realization_claim`) and `relationship_constraint` elsewhere, `FOREIGN_KEY` → `delete_reference_conflict`. The table decides between the two constraint meanings because SQLite reports a duplicate relationship tuple under the same code it uses for a constraint violation.

`_conflict_record(applied)` returns the **exact key the engine handed the conflict callback**, copied out of the change while the callback still held it, and never a key searched for in the changeset: those are different facts, because the first operation a changeset carries for a table is not necessarily the operation that conflicted. `KEY_NOT_SUPPLIED` is the honest answer for a change whose key columns were not readable — a statement about the changeset, not a placeholder for a row identity.

### Conventions

- Every module-level constant is a named fact rather than a literal at the call site: the private workspace file names (`STAGED_LEFT_NAME`, `REPLAY_LEFT_NAME`, `REPLAY_RIGHT_NAME`, `_FROZEN_STAGE_NAME`), the five SQLite conflict codes, the relationship-table set and the not-supplied key marker. The workspace names are never exposed — the merged candidate only becomes public bytes through the publication contract.
- `_open(path)` is the one read-only connection helper every comparison in this module uses.
- Refusal factories live in `merge_refusals.py`; this module maps a failure onto one and never spells a code out at a raise site.

### Invariants And Boundaries

- **One resource lock at a time, never nested.** The three inputs and the coverage replays take no lock at all; the merged temporary's lock covers the freeze and is released before the destination lock is acquired by the publication operation. `kernel/file_lock.py` forbids nesting, and this module's lock order is why the merge never needs to.
- **The sequence order is the guarantee.** Preflight precedes the session because SQLite's changeset application can silently skip a table it cannot match; coverage replay precedes application because a return code cannot report an omission; postconditions precede publication because publication is the point of no return.
- **A rule over the applied rows runs inside the application's own transaction.** The route-acyclicity walk is the one check this module makes *before* its own postconditions, and it is made on the connection the right delta was applied on, after the application and before its commit — so a refusal leaves the target holding exactly what it held. The policy is the changeset layer's (`apply_changeset`'s `within_transaction`), and this module supplies only the rule and the operation it is attributed to.
- **A refusal publishes nothing and moves no input.** Every refusal path returns before `_publish`, `_publish`'s own failure branch returns the publication's refusal, and the mid-application refusal is coupled to the rollback of the application it judges: `apply_changeset` undoes the right delta before this module returns it, so a candidate refused for a route cycle leaves the staged target exactly as the left side was copied.
- **No verdict is representable.** The outcome carries identities, coverage and publication state; there is no compatibility, acceptance, approval or "harmless" field anywhere in this module or in the models it returns.
- **Nothing here configures Git.** The only Git commands on this path are the two read-only ancestry queries in `merge_base.py`; no driver, attribute or commit exists.
- **The destination is optional.** A caller may merge, inspect the structural outcome and publish nothing.

### Todos

None recorded for this slice. Two reachability facts are stated in their own modules rather than left implicit here: `require_applied_changes` and the merged-candidate `require_immutable_revisions_preserved` call are unreachable by a black-box case under this schema, and `_freeze_merged`'s contribution is invisible to a case for the reason its own docstring gives. Each is recorded as a non-experiment with its policy exercised directly by a boundary node — not as a covered guard.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The eight-step contract, the lock policy and the list of things this operation never does. | `merge_knowledge_datasets` | mcp/src/agents_remember/memory/knowledge/merge.py:1-163; mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The one entry point and its typed-refusal guarantee. | `merge_knowledge_datasets` | mcp/src/agents_remember/memory/knowledge/merge.py:131-163 |
| The working record that keeps coverage already proven when a late step refuses. | `MergeRun` | mcp/src/agents_remember/memory/knowledge/merge.py:167-228 |
| **The candidate's own route hierarchy judged inside the application's uncommitted transaction, with the refusal attributed to the merge operation.** | "def acyclic_routes(self, connection: apsw.Connection)" | mcp/src/agents_remember/memory/knowledge/merge.py:245-261 |
| The private workspace names and the not-supplied key marker. | `STAGED_LEFT_NAME`; `REPLAY_LEFT_NAME`; `REPLAY_RIGHT_NAME`; `KEY_NOT_SUPPLIED` | mcp/src/agents_remember/memory/knowledge/merge.py:106-109; mcp/src/agents_remember/memory/knowledge/merge.py:129-129 |
| The five conflict codes, the relationship-table set and the taxonomy they index. | `_CONFLICT_DATA`; `_CONFLICT_FOREIGN_KEY`; `_RELATIONSHIP_TABLES`; `_TAXONOMY` | mcp/src/agents_remember/memory/knowledge/merge.py:115-115; mcp/src/agents_remember/memory/knowledge/merge.py:119-119; mcp/src/agents_remember/memory/knowledge/merge.py:123-123; mcp/src/agents_remember/memory/knowledge/merge.py:671-676 |
| Identity admission repeated at the merge because the files are read twice. | `require_admitted_identities` | mcp/src/agents_remember/memory/knowledge/merge.py:321-365 |
| The distinct-role check that runs ahead of the identity comparison. | `require_distinct_roles` | mcp/src/agents_remember/memory/knowledge/merge.py:403-430 |
| The declared-manifest comparison that runs before any session exists, and why a pairwise pass would be unreachable. | `_preflight` | mcp/src/agents_remember/memory/knowledge/merge.py:433-467 |
| The one-delta-at-a-time build, the changed-table coverage refusal and the coverage fact. | `_build_covered_deltas`; `_coverage_refusal`; `_changed_tables`; `_coverage_of` | mcp/src/agents_remember/memory/knowledge/merge.py:449-465; mcp/src/agents_remember/memory/knowledge/merge.py:468-488; mcp/src/agents_remember/memory/knowledge/merge.py:491-519; mcp/src/agents_remember/memory/knowledge/merge.py:522-546 |
| The side-integrity pass that refuses a side which rewrote a sealed revision behind its identity. | `_require_side_integrity` | mcp/src/agents_remember/memory/knowledge/merge.py:568-577 |
| The conflict callback's key being the engine's own, and the four code-to-refusal mappings. | `_conflict_record`; `_conflict_facts`; `_recorded_row_refusal`; `_independent_insert_refusal`; `_relationship_constraint_refusal`; `_relationship_duplicate_refusal` | mcp/src/agents_remember/memory/knowledge/merge.py:668-679; mcp/src/agents_remember/memory/knowledge/merge.py:682-715; mcp/src/agents_remember/memory/knowledge/merge.py:599-611; mcp/src/agents_remember/memory/knowledge/merge.py:614-623; mcp/src/agents_remember/memory/knowledge/merge.py:626-633; mcp/src/agents_remember/memory/knowledge/merge.py:636-645 |
| The apply-then-validate step and the publication step that freezes under the temporary's own lock. | `_apply_and_validate`; `_publish`; `_freeze_merged` | mcp/src/agents_remember/memory/knowledge/merge.py:293-334; mcp/src/agents_remember/memory/knowledge/merge.py:739-758; mcp/src/agents_remember/memory/knowledge/merge.py:761-797 |
| The preflight this module runs and the declared manifest it compares against. | `require_supported_structure`; `declared_structure`; `compare_structures` | mcp/src/agents_remember/memory/knowledge/merge_schema.py:226-258; mcp/src/agents_remember/memory/knowledge/merge_schema.py:173-188; mcp/src/agents_remember/memory/knowledge/merge_schema.py:261-305 |
| The delta production, aborting application and coverage replay this module composes. | `build_delta`; `apply_changeset`; `replay_delta`; `require_session_capability` | mcp/src/agents_remember/memory/knowledge/merge_changeset.py:210-254; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:257-319; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:362-401; mcp/src/agents_remember/memory/knowledge/merge_changeset.py:185-207 |
| The postcondition half this module calls before publishing. | `require_structural_validity`; `require_immutable_revisions_preserved`; `require_applied_changes`; `MergeInputs` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:73-101; mcp/src/agents_remember/memory/knowledge/merge_validation.py:104-152; mcp/src/agents_remember/memory/knowledge/merge_validation.py:169-211; mcp/src/agents_remember/memory/knowledge/merge_validation.py:64-70 |
| The refusal factories this module maps every failure onto. | `conflicting_values_refusal`; `duplicate_identity_refusal`; `delete_reference_conflict_refusal`; `duplicate_relationship_refusal`; `changeset_incomplete_refusal`; `changeset_postcondition_failed_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:70-94; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:97-121; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:124-151; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:154-173; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:221-245; mcp/src/agents_remember/memory/knowledge/merge_refusals.py:248-270 |
| The publication contract the frozen stage is installed through, and the freeze procedure reused here. | `publish_prepared_snapshot`; `freeze_closed_snapshot`; `open_existing_knowledge_store` | mcp/src/agents_remember/memory/knowledge/publication.py:114-170; mcp/src/agents_remember/memory/knowledge/closed_snapshot.py:66-109; mcp/src/agents_remember/memory/knowledge/store.py:751-764 |
| The models this operation takes and returns. | `MergeRequest`; `MergeOutcome`; `TableCoverage` | mcp/src/agents_remember/models/knowledge/merge.py:189-215; mcp/src/agents_remember/models/knowledge/merge.py:349-391; mcp/src/agents_remember/models/knowledge/merge.py:218-240 |
| The five unit nodes and the six boundary nodes that hold this contract. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-312 |
| The boundary node for the conflict row identity that this module renders. | "test_a_row_level_conflict_names_the_row_the_engine_refused" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:100-132 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:51:44+00:00: 260915-KS-L23 residue clearance (seat A): four claims in this card re-cited to the constructs they name, after this leaf's module split and pyright repairs moved them. (1) The private workspace names / not-supplied key marker: `KEY_NOT_SUPPLIED` `merge.py:128-128` → `:129-129` (the constant's own line; the other three names stay in `:106-109`). (2) The five conflict codes, relationship-table set and taxonomy: `_CONFLICT_DATA` `:114-114` → `:115-115`, `_CONFLICT_FOREIGN_KEY` `:118-118` → `:119-119`, `_RELATIONSHIP_TABLES` `:122-122` → `:123-123`, `_TAXONOMY` `:650-655` → `:671-676` — each anchor now cited at its own definition, and the taxonomy's six-line definition span restored. (3) The apply-then-validate / publication / freeze row: `_apply_and_validate` `:260-299` → `:293-334`, `_publish` `:720-739` → `:739-758`, `_freeze_merged` `:698-734` → `:761-797` (the split moved the freeze into this module; each range is now that function's current extent). (4) The composed changeset operations: `build_delta` `merge_changeset.py:185-220` → `:210-254`, `apply_changeset` `:223-263` → `:257-319`, `replay_delta` `:292-331` → `:362-401`, `require_session_capability` `:160-182` → `:185-207`. Every anchor was kept, every claim was re-read against the construct it now cites, and no row, citation, range or claim was deleted or reworded. Verification stamp **not** advanced: the code is uncommitted and closeout owns the stamp.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `require_distinct_roles` repointed to mcp/src/agents_remember/memory/knowledge/merge.py:403-430. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_preflight` repointed to mcp/src/agents_remember/memory/knowledge/merge.py:433-467. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_require_side_integrity` repointed to mcp/src/agents_remember/memory/knowledge/merge.py:568-577. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:24+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the one rule this operation gained, and why it had to land with the right-side write fix. `MergeRun.acyclic_routes` (`merge.py:245-261`) runs `require_acyclic_routes(…, MERGE_OPERATION)` over the merged candidate's repository id, and `_apply_and_validate` (`:293-334`, the hand-off at `:300-302`) passes it to `apply_changeset(…, within_transaction=run.acyclic_routes)` and returns `run.refused(applied.refusal)` before the conflict branch — so the walk runs on the connection the right delta was applied on, after the application and **before its commit**, and a candidate that reparents a route into a cycle is rolled back rather than published. The merge's own docstring still states the same eight steps (this is a rule inside step 8, not a ninth), so the card's sequence account is unchanged; what the card now carries is the rule, the operation it is attributed to, the reason it cannot run before the application or after the commit, and the fact that it is a production path only because a right-side `route.parent_route_id` change is a real replayed operation. One row was added for the new method; no existing row, citation or range was rewritten, and no verification stamp advanced (the source is uncommitted and closeout owns the stamp).
- 2026-09-17T20:39:57+00:00: Generated citation repair: `_require_side_integrity` repointed to mcp/src/agents_remember/memory/knowledge/merge.py:547-556. No content impact: mechanical anchor-range projection bound to citation source snapshot b181d6d0b4e4cacc1833ff166c579061a1762313f644c682eec8ffc186d8d42f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the merge's orchestration module. It records the eight-step sequence and *why each step's position is load-bearing* (preflight before the session because changeset application can silently skip an unmatched table; coverage replay before application because a return code cannot report an omission; postconditions before publication because publication is irreversible), the one-lock-at-a-time policy that keeps the temporary's freeze lock and the destination's install lock sequential, the conflict taxonomy including the table-driven split between `duplicate_relationship` and `relationship_constraint`, and the conflict record's engine-supplied key — read from the change the callback held, never reconstructed from the changeset, with `KEY_NOT_SUPPLIED` as the honest answer when a change carries no readable key columns. It also carries this leaf's two stated unreachability facts (the applied-change check and the merged-candidate immutability call are non-experiments whose policies are exercised directly; the freeze's contribution is invisible to a case) so a later reader does not read them as covered guards. Verification metadata remains empty until closeout stamps the code commit.
