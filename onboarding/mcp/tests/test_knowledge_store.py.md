# mcp/tests/test_knowledge_store.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_store.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

The focused behavioural suite for the immutable knowledge identity store. Each case protects one consequential
operation or failure — a divergent-successor read, an identity reuse, a lineage violation, or a database-level
immutability guarantee. Constructor validation is not re-tested here; the failure each case protects is a
stored-state failure.

## Code Commentary

### Logic

Support in this module: a `fixture` pytest fixture that builds the shared branching fixture under
`tmp_path / "candidate"`; `ExtensionOptions` (optional invariant id, predecessors, statement and provenance for one
extension case); `_extension_request` (builds a `RevisionRequest` around `fixture_revision_draft`, allowing the
invariant id and provenance to be overridden); `_disable_immutability_triggers` and `_write_raw_cycle` /
`_write_raw_edge` (write cyclic state **outside** the operation, with a docstring stating why the triggers are
dropped); and a `_revision_and_edge_counts` helper used by the refusal-invariance assertions.

23 collected nodes, all in the unit lane and with no integration marker. The `KS-R03` increment added the one node marked below:

| Node | Protects |
| --- | --- |
| `test_two_same_label_successors_reopen_as_separate_revisions` | two `v2` successors stay independently addressable with their exact statements after a close/reopen cycle |
| `test_reopening_the_same_path_keeps_identity_and_schema` | reopen validates the same generation instead of creating or repairing |
| `test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses` | **added by `KS-R03`**: the single-record identity operation confirms an identical repeat (`no_change`) and refuses a different label under one id (`duplicate_identity`) — the two-caller contract the batch refactor nearly unified away |
| `test_created_revision_stores_the_digest_the_store_recomputed` | the stored seal is the store's recomputation, not caller input |
| `test_identical_aggregate_is_no_change` | re-submitting the same aggregate is `no_change` rather than a duplicate refusal |
| `test_reused_revision_identity_with_other_content_refuses` | an identity reuse with different content refuses and leaves the stored row unchanged |
| `test_accepted_origin_data_requires_an_acceptance_reference` | proposal is distinct from acceptance at the vocabulary boundary |
| `test_cross_invariant_predecessor_refuses_with_the_named_endpoint` | a cross-invariant predecessor refuses as `invalid_reference` naming both invariants |
| `test_dangling_predecessor_refuses_without_leaving_a_row` | a nonexistent predecessor refuses with unchanged row counts |
| `test_self_predecessor_is_refused_at_the_vocabulary_boundary` | a self-referencing payload is refused before storage |
| `test_cycle_membership_reports_the_edges_of_an_on_cycle_revision` | the membership query reports both edges of a cycle, and an unrelated successor is admitted |
| `test_lineage_guard_refuses_a_candidate_descending_from_a_stored_cycle` | the write-path guard refuses a candidate below a stored cycle, naming the cycle, with no row written and wording that does not claim self-reachability |
| `test_lineage_cycle_refusal_describes_each_branch_honestly` | both branches of the rule are worded for the branch they describe |
| `test_lineage_guard_fires_before_the_candidate_insert` | the guard is evaluated before the candidate's own INSERT (disabling it fails this node) |
| `test_unknown_invariant_refuses_the_revision` | a revision for an unrecorded invariant refuses as `unknown_invariant` |
| `test_other_repository_namespace_is_refused` | a foreign namespace refuses as `unauthorized_scope` on every write operation |
| `test_stored_revision_rows_refuse_update_and_delete` | direct `UPDATE`/`DELETE` raises `immutable_revision` at the database level |
| `test_payload_digest_seals_more_than_the_statement` | the seal covers the predecessor set, so a re-pointed edge fails the read-time check |
| `test_schema_carries_the_declared_manifest_and_generation` | the live schema matches the declared tables, columns and `user_version` |
| `test_partial_schema_is_refused_instead_of_written_through` | a missing canonical table refuses at open |
| `test_dropped_immutability_trigger_is_refused` | a dropped trigger refuses at open |
| `test_application_seam_initializes_and_extends_one_namespace` | the composition seam initializes and extends one namespace end to end |
| `test_lower_ranked_owners_do_not_import_the_memory_domain` | the layer direction holds: no owner below `memory` imports the storage package |

### Conventions

The module imports the fixture through the bare module name `knowledge_fixture_test_support`, which is how
`mcp/tests/conftest.py` puts this directory on `sys.path`. Assertions name the observable outcome (state, refusal
code, offending record, row counts) rather than internal call order.

### Invariants And Boundaries

- The suite is the executable counterpart of the requirement's failure list. Two nodes are load-bearing for
  enforcement rather than for reading: disabling the write-path lineage guard makes
  `test_lineage_guard_refuses_a_candidate_descending_from_a_stored_cycle` and
  `test_lineage_guard_fires_before_the_candidate_insert` fail; reintroducing the superseded refusal wording fails
  the descending node and the branch node.
- **`test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses` is not a duplicate of the
  aggregate node.** `test_identical_aggregate_is_no_change` covers revision reuse; this one covers the *identity*
  operation, and it exists because the `KS-R03` refactor moved the invariant insert into a shared helper and
  silently dropped the `no_change` branch — the base tree returned `no_change` for an identical repeat while the
  candidate refused `duplicate_identity` (sealed finding `260915-KS-L3-RV-2`). The repair restored the branch via
  `confirm_repeat` and this node would fail if it were removed again. The suite passed 54/54 while the behaviour
  was wrong, which is why the node had to be added rather than a passing suite trusted.
- Cyclic state has no reachable creation path through `create_revision` — admission accepts only existing
  predecessors and the vocabulary refuses a self-referencing payload — so the cycle cases write the raw edges
  outside the operation and say so. That construction is labelled, not a workaround: the finding it once carried
  was about what a node asserted, not about how the state was built.
- The module is registered in exactly one lane, `unit-regression`, in `mcp/tests/test-evidence-lanes.toml`.
  Without that row `load_lane_manifest` refuses the repository and the certifying collection path cannot start, so
  the registration is a load-bearing part of this change set rather than bookkeeping.
- The 23 nodes all live inside the unit collected-case budget; no integration marker is used and no case spawns a
  repository or a subprocess.

### Todos

None recorded. Later leaves (KS-R02 … KS-R08) extend the fixture and add their own modules rather than growing this
one.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The divergent-successor read, the node registered as the shared fixture's evidence node. | `test_two_same_label_successors_reopen_as_separate_revisions` | mcp/tests/test_knowledge_store.py:87-113 |
| The two-caller identity contract the `KS-R03` repair restored, added to this suite in that same change. | `test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses` | mcp/tests/test_knowledge_store.py:180-217 |
| The identity reuse refusal and its unchanged stored row. | `test_reused_revision_identity_with_other_content_refuses` | mcp/tests/test_knowledge_store.py:257-282 |
| The write-path guard's descending branch, including the wording assertions. | `test_lineage_guard_refuses_a_candidate_descending_from_a_stored_cycle` | mcp/tests/test_knowledge_store.py:453-502 |
| The before-the-insert evaluation a disabled guard fails. | `test_lineage_guard_fires_before_the_candidate_insert` | mcp/tests/test_knowledge_store.py:590-623 |
| The database-level immutability proof against the stored revision rows. | `test_stored_revision_rows_refuse_update_and_delete` | mcp/tests/test_knowledge_store.py:680-706 |
| The seal covering more than the statement. | `test_payload_digest_seals_more_than_the_statement` | mcp/tests/test_knowledge_store.py:709-727 |
| The seam case that drives the production composition path, including the batch entry points this leaf added to that module. | `test_application_seam_initializes_and_extends_one_namespace` | mcp/tests/test_knowledge_store.py:736-788 |
| The layer-direction case. | `test_lower_ranked_owners_do_not_import_the_memory_domain` | mcp/tests/test_knowledge_store.py:838-856 |
| The shared fixture every case builds from. | `build_branching_knowledge_fixture` | mcp/tests/knowledge_fixture_test_support.py:203-261 |
|  The lane registration that makes the repository's manifest load (this module's row inside the lane, after the `KS-R03` insertions). | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5  |
|  The fixture's registered stable contract and evidence node. | "contract:knowledge-identity-branching-fixture" | mcp/tests/evidence-lifecycle.toml:1183-1183  |
| The store contract the added node pins, including the two-caller distinction. | `insert_invariant`; `_insert_invariant` | mcp/src/agents_remember/memory/knowledge/store.py:536-572; mcp/src/agents_remember/memory/knowledge/store.py:360-368 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "contract:knowledge-identity-branching-fixture" repointed to mcp/tests/evidence-lifecycle.toml:1183-1183. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:11+00:00 — 260915-KS-L10 curator (uncommitted change set on `ar/260915-ks-l10`, base `420669c4`): citation ranges re-derived against the working tree after this leaf enlarged the modules this card cites (`schema.py` gained the relocated `PRIMARY_KEYS`/`JSON_COLUMNS`, and the knowledge modules and their test modules grew), so ranges that were exact at the base commit no longer held the constructs their rows name. Every re-derived range was verified to contain the construct its own row names; no row, citation or claim was deleted or weakened, and the claim wording was retained where it still holds. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `build_branching_knowledge_fixture` repointed to mcp/tests/knowledge_fixture_test_support.py:203-261. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **extended this card for the node the review forced.** The suite is now 23 nodes: `test_a_repeated_identical_invariant_is_no_change_and_a_relabel_refuses` was added because the candidate-batch refactor moved the invariant insert into a shared helper and silently dropped its `no_change` branch, so a repeated identical `create_invariant` refused `duplicate_identity` where the base commit confirmed it (sealed finding `260915-KS-L3-RV-2`). The fix restored the branch behind `confirm_repeat` and this node pins it. The card records why the node is not a duplicate of `test_identical_aggregate_is_no_change` (identity versus aggregate) and that the 54 upstream cases passed while the behaviour was wrong — a passing suite is not a preservation proof. Citation ranges were re-derived against the grown file and the lane row re-cited. Verification metadata remains closeout-owned.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new focused suite. It records the 22-node census with what each node protects, the two mutation-proved enforcement nodes (sealed findings `RV-1`/`RV-2`/`RV-4`), the labelled outside-the-operation construction of cyclic state, and the load-bearing `unit-regression` registration. Verification metadata remains empty until closeout stamps the code commit.
