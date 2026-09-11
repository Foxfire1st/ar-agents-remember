# mcp/tests/test_source_lineage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_source_lineage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T15:06+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Builds real Git repositories and canonical sprint/master/leaf contracts to check transitive code and memory lineage. Parent movement blocks the leaf; start and attach recheck exact source tips; sibling worktrees of the same repository remain legitimate. The lineage chain comes from task authority rather than caller-invented identifiers. `CloseoutSourceLineageHealTests` extends the same fixture to the closeout boundary, where a settleable stale break is now carried, an unprovable one escalates, a `dry_run` mutates nothing, and a retained sync conflict hands back both worktrees with their duties.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The closeout-boundary class covers both halves of the change: the plain fast-forward, the leaf that
owns its own commit, the unprovable-escalation and retained-conflict paths, the read-only preview,
and the parked-candidate cases (uncommitted carry and retained reapply conflict) whose transaction
detail is pinned in `test_sync_parked_candidate.py`.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Leaf identity proves code and memory transitively | `test_leaf_identity_proves_code_and_memory_transitively` | mcp/tests/test_source_lineage.py:57-74 |
| Organizational super move blocks the leaf boundary | `test_organizational_super_move_blocks_the_leaf_boundary` | mcp/tests/test_source_lineage.py:76-90 |
| Start rechecks exact source tips before start effects | `test_start_rechecks_exact_source_tips_before_start_effects` | mcp/tests/test_source_lineage.py:92-125 |
| Attach refuses before stale task context is resumed | `test_attach_refuses_before_stale_task_context_is_resumed` | mcp/tests/test_source_lineage.py:126-139 |
| Parent and leaf paths may be sibling worktrees of one repository | `test_parent_and_leaf_paths_may_be_sibling_worktrees_of_one_repository` | mcp/tests/test_source_lineage.py:190-210 |
| Lifecycle boundary requires the full transitive chain | `test_lifecycle_boundary_requires_the_full_transitive_chain` | mcp/tests/test_source_lineage.py:212-224 |
| The closeout-boundary class proves the self-healing source-lineage guard. | `CloseoutSourceLineageHealTests` | mcp/tests/test_source_lineage.py:227-432 |
| A plain fast-forward break is carried by the closeout boundary. | `test_closeout_boundary_heals_a_plain_fast_forward_break` | mcp/tests/test_source_lineage.py:235-251 |
| A `dry_run` closeout refuses with the preview duty and moves nothing. | `test_closeout_preview_refuses_without_moving_the_break` | mcp/tests/test_source_lineage.py:253-269 |
| A leaf that owns its own commit is carried (merge, not refusal). | `test_closeout_boundary_carries_a_leaf_that_owns_its_own_commit` | mcp/tests/test_source_lineage.py:271-292 |
| An unprovable break escalates to the human developer. | `test_unprovable_lineage_escalates_to_the_human_developer` | mcp/tests/test_source_lineage.py:294-312 |
| A retained sync conflict hands back both worktrees and their duties. | `test_retained_sync_conflict_hands_back_both_worktrees_and_their_duties` | mcp/tests/test_source_lineage.py:314-348 |
| A dirty (uncommitted) candidate is parked, carried, and returned by the closeout boundary. | `test_closeout_boundary_carries_an_uncommitted_candidate` | mcp/tests/test_source_lineage.py:350-370 |
| A parked-candidate reapply conflict surfaces as `source-lineage-sync-conflict` with the candidate recoverable. | `test_closeout_boundary_retains_a_parked_candidate_conflict` | mcp/tests/test_source_lineage.py:372-399 |
| The moved-source integration guidance routes through the sync. | `test_source_moved_integration_guidance_routes_through_the_sync` | mcp/tests/test_source_lineage.py:401-432 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_parent_and_leaf_paths_may_be_sibling_worktrees_of_one_repository` repointed to mcp/tests/test_source_lineage.py:190-210. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_lifecycle_boundary_requires_the_full_transitive_chain` repointed to mcp/tests/test_source_lineage.py:212-224. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `CloseoutSourceLineageHealTests` repointed to mcp/tests/test_source_lineage.py:227-432. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_closeout_boundary_heals_a_plain_fast_forward_break` repointed to mcp/tests/test_source_lineage.py:235-251. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_closeout_preview_refuses_without_moving_the_break` repointed to mcp/tests/test_source_lineage.py:253-269. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_closeout_boundary_carries_a_leaf_that_owns_its_own_commit` repointed to mcp/tests/test_source_lineage.py:271-292. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_unprovable_lineage_escalates_to_the_human_developer` repointed to mcp/tests/test_source_lineage.py:294-312. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_retained_sync_conflict_hands_back_both_worktrees_and_their_duties` repointed to mcp/tests/test_source_lineage.py:314-348. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_closeout_boundary_carries_an_uncommitted_candidate` repointed to mcp/tests/test_source_lineage.py:350-370. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_closeout_boundary_retains_a_parked_candidate_conflict` repointed to mcp/tests/test_source_lineage.py:372-399. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_source_moved_integration_guidance_routes_through_the_sync` repointed to mcp/tests/test_source_lineage.py:401-432. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T15:06+02:00 — Closeout-heal curation: recorded the `CloseoutSourceLineageHealTests` class and its eight cases (fast-forward carry, read-only preview, leaf-owns-its-commit carry, unprovable escalation, retained-conflict handback, uncommitted-candidate carry, retained parked-candidate conflict, moved-source integration guidance) and re-derived every retained method range against the current working tree. Verification remains closeout-owned.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-26T08:45+02:00 — Restored the canonical commentary and Docs/Cross-Repo reference section
  shape for this changed lineage suite card.

- 2026-08-26T03:37+02:00 — Strengthened stale attach forcing: the exact parent series is selected
  and active before the later lineage refusal, proving implementation admission does not get
  skipped merely because exposure ultimately blocks on ancestry. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: reconciled this test card to current source while preserving prior history and verification provenance.

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-16T05:27+02:00 — L4 exact-review forcing: added real-Git organizational and atomic
  code-forward/external-memory-rewind cases plus an under-lock race for exact pre-start source
  snapshots; refusals assert no code/memory worktree or contract mutation.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
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
