# mcp/tests/test_source_lineage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_source_lineage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T14:32+02:00 |
| lastVerifiedCommitHash | `100b40d6be4a7d03eedbb1164ce54e2e8a314038` |
| lastVerifiedCommitDate | 2026-08-14T08:23:37+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Provides real-Git acceptance coverage for task-derived source-lineage policy.
The fixture builds canonical sprint, master, and leaf documents plus matching
series/leaf contracts and repositories, so the tests exercise ancestry from the
same durable identities used by structural dispatch rather than caller-supplied
ids.

## Test Coverage

`SourceLineageTests` proves sprint/no-edge behavior and the full
code/external-memory edge order for a leaf, then moves actual branch tips to
cover blocked super-to-master, master-to-leaf, and diverged ancestry. The start case explicitly supplies
`stale_base_choice="proceed-stale"` and still expects a lineage refusal, proving
that the human stale-base option cannot bypass this structural gate. Attach is
also refused before stale task context resumes.

The missing-contract tests pin relation attribution: a missing leaf contract is
reported as an unavailable `master-to-leaf` edge, while a missing master series
contract is `super-to-master`. This keeps dashboard/recovery evidence useful
even when no branch comparison can be performed. Additional cases cover
malformed/missing parent contracts, non-task contracts, mismatched parent
branches, absent repositories/branch names/refs, and an unavailable Git
comparison. Unavailable projections deliberately expose no sync command because
there is not yet a safe branch movement to perform.

The sibling-worktree regression creates a real detached linked checkout for the parent contract
while leaving the leaf contract on the repository's original checkout. The full leaf projection
must stay current, proving repository identity follows Git's shared common directory rather than
literal checkout path. Complementary cases prove repository identity is unavailable for a missing
path and for an existing non-Git directory, while `require_current_source_lineage` accepts a fully
current transitive chain and raises operation-specific sync guidance after the super moves.

## Invariants And Boundaries

- Repositories are initialized and advanced with Git commands; ancestry tests do
  not mock the fact source.
- Task identity is resolved from canonical JSON documents and enclosure paths.
- The fixture can enable external memory to prove both code and memory edges.
- Refusal tests assert both the blocked state and the exact recovery contract.
- The lifecycle-boundary helper accepts a current full chain, then refuses after the real super
  branch moves and names the parent-first `worktree_sync` recovery.
- Parent and leaf contracts may name sibling worktrees of one repository without producing a false
  unavailable lineage edge.
- The suite is collected by pytest only. It has no `__main__`/`unittest.main()` script launcher;
  removing that pytest-inert footer changes no test semantics and prevents dead launcher lines
  from appearing as uncovered acceptance delta.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Sprint roles have no single master edge; leaf identity proves the ordered transitive code and external-memory edges. | `test_sprint_roles_have_no_single_master_lineage_edge`; `test_leaf_identity_proves_code_and_memory_transitively` | mcp/tests/test_source_lineage.py:42-70 |
| Super movement blocks start despite a stale-base override and points to the master contract. | `test_super_move_blocks_before_leaf_start_even_with_stale_override` | mcp/tests/test_source_lineage.py:72-94 |
| Master movement blocks leaf dispatch and points to the leaf contract. | `test_master_move_blocks_leaf_dispatch_with_leaf_sync_recovery` | mcp/tests/test_source_lineage.py:96-112 |
| Missing/malformed task or parent contracts fail closed with relation-specific evidence. | `test_missing_leaf_contract_fails_closed`; `test_missing_master_contract_names_the_super_to_master_edge`; `test_parent_only_preflight_fails_closed_for_every_missing_parent_shape` | mcp/tests/test_source_lineage.py:128-202 |
| Unavailable repositories/branches/Git comparisons carry no fabricated sync recovery. | `test_unavailable_lineage_has_no_sync_recovery_command`; `test_contract_branch_mismatch_and_git_failures_are_unavailable` | mcp/tests/test_source_lineage.py:204-244 |
| Sibling linked worktree paths resolve as the same repository and keep the leaf chain current. | `test_parent_and_leaf_paths_may_be_sibling_worktrees_of_one_repository` | mcp/tests/test_source_lineage.py:247-267 |
| Diverged master ancestry reports both ahead and behind counts. | `test_diverged_master_reports_divergence` | mcp/tests/test_source_lineage.py:269-280 |
| The shared fixture writes task topology, contracts, and real Git branches. | `_fixture`; `_write_task_tree`; `_repo` | mcp/tests/test_source_lineage.py:276-367 |

## L23 Final Candidate Disposition

Lineage regressions compare Git common-directory identity across sibling worktrees and require
current super-to-master-to-leaf ancestry for both code and external memory. Missing, behind,
diverged, or foreign-repository evidence fails closed with task-addressed recovery.

## Update History
- 2026-08-14T06:38+02:00 — L23 final candidate review: lineage tests compare Git common-directory
  identity across sibling worktrees and fail closed on stale code or external-memory ancestry.

- 2026-08-13T14:32+02:00 — No content impact: removed the pytest-inert
  `__main__`/`unittest.main()` footer. Pytest collection and every lineage assertion are unchanged;
  the deletion only clears dead script-launcher lines from changed-coverage accounting. Final
  provenance remains closeout-owned.
- 2026-08-13T12:53+02:00 — L23 Dagger-rail coverage: added absent/non-Git repository-identity
  cases and direct lifecycle-boundary proof that the full transitive chain is required and a moved
  super raises sync guidance. Verification provenance remains closeout-owned.


- 2026-08-13T09:27+02:00 — L23 curator: documented the real linked-worktree fixture proving that a
  parent contract may name a sibling checkout without falsely blocking lineage, and repaired the
  shifted divergence citation. Verification metadata remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: added direct coverage for the reusable lifecycle-boundary guard over a real transitive chain and its parent-first recovery. Verification metadata remains closeout-owned.

- 2026-08-12T20:18+02:00 — 260731-EFA-L23 curator: expanded for the final 100% statement/branch coverage wave, including sprint/no-edge, malformed parent evidence, mismatched branch linkage, unavailable Git facts, and no-recovery unavailable payloads. Verification remains closeout-owned.
- 2026-08-12T20:10+02:00 — 260731-EFA-L23 curator: created for real-Git transitive source-lineage admission and exact missing-contract relation coverage. Verification remains pinned to the leaf base until closeout assigns the dirty test source a real commit identity.
