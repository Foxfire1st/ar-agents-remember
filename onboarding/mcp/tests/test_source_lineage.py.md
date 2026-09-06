# mcp/tests/test_source_lineage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_source_lineage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Builds real Git repositories and canonical sprint/master/leaf contracts to check transitive code and memory lineage. Parent movement blocks the leaf; start and attach recheck exact source tips; sibling worktrees of the same repository remain legitimate. The lineage chain comes from task authority rather than caller-invented identifiers.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

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
| Leaf identity proves code and memory transitively | `test_leaf_identity_proves_code_and_memory_transitively` | mcp/tests/test_source_lineage.py:48-65 |
| Organizational super move blocks the leaf boundary | `test_organizational_super_move_blocks_the_leaf_boundary` | mcp/tests/test_source_lineage.py:67-81 |
| Start rechecks exact source tips before start effects | `test_start_rechecks_exact_source_tips_before_start_effects` | mcp/tests/test_source_lineage.py:83-114 |
| Attach refuses before stale task context is resumed | `test_attach_refuses_before_stale_task_context_is_resumed` | mcp/tests/test_source_lineage.py:117-130 |
| Parent and leaf paths may be sibling worktrees of one repository | `test_parent_and_leaf_paths_may_be_sibling_worktrees_of_one_repository` | mcp/tests/test_source_lineage.py:132-152 |
| Lifecycle boundary requires the full transitive chain | `test_lifecycle_boundary_requires_the_full_transitive_chain` | mcp/tests/test_source_lineage.py:154-166 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

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
