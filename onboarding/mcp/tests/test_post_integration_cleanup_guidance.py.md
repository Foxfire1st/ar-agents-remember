# mcp/tests/test_post_integration_cleanup_guidance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_post_integration_cleanup_guidance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Pin finalization guidance for a landed task, the still-working checkpoint phase, and cache-independent external-memory completion.

## Code Commentary

### Logic

The minimal internal-memory contract tests phase, operation, tool, contract args, required args, and explanatory summary. A landed but unfinalized task must offer lifecycle_finalize_task rather than a cleanup decision/retry. The vocabulary case keeps the retired cleanup choices absent and finalize present. A checkpointed series stays worktree-started and continues work.

The external-memory case creates real temporary code and memory repositories. Missing, malformed, or stale cache text leaves carryover completion and finalization guidance valid when the accepted outputs are landed. An unlanded memory commit, nonexistent accepted code commit, or missing memory repository must still make the completion proof false.

### Conventions

Module-level tests use the small constructed contract where only projection is at issue and real Git where ancestry is the subject. The external-memory case is no longer accurately described as repository-free.

### Invariants And Boundaries

- Assert structured phase/tool/args, not summary text alone.
- Finalization owns reclamation and a checkpoint remains open.
- Cache contents cannot decide carryover completion.
- Actual missing or unlanded output identities still refuse completion.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| None | `test_a_pending_cleanup_offers_finalization_and_never_a_cleanup_decision`; `test_the_cleanup_decision_is_no_longer_in_the_next_operation_vocabulary` | mcp/tests/test_post_integration_cleanup_guidance.py:49-65; mcp/tests/test_post_integration_cleanup_guidance.py:68-81 |
| External completion depends on landed commits, never cache text. | `test_external_completion_proves_landed_commits_without_reading_the_cache` | mcp/tests/test_post_integration_cleanup_guidance.py:84-119 |
| Checkpoint guidance remains still-working. | `test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate` | mcp/tests/test_post_integration_cleanup_guidance.py:122-148 |
| Production completion and post-integration guidance owner. | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:245-328 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Added real Git completion coverage for absent/malformed/stale cache states and unlanded/missing outputs; retained the three existing finalization/vocabulary/checkpoint scenarios. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.
- 2026-09-13T17:20:55+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:862-893. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T19:50+02:00 — 260831-LOCR-L31: the first case was renamed with its subject —
  `test_a_pending_cleanup_offers_a_retry_and_never_a_cleanup_decision` →
  `test_a_pending_cleanup_offers_finalization_and_never_a_cleanup_decision` — because the
  `cleanup-pending` phase now routes `finalize` / `lifecycle_finalize_task` with
  `nextRequiredArgs == ["contract_path"]` instead of a `retry_cleanup` / `worktree_cleanup` move;
  recorded the new assertion set (including that `"worktree_cleanup"` is absent from the summary) and
  the **inverted** second case (`retry_cleanup not in NextOperation`, `finalize in`), which is a
  removal rather than an addition because the branch the first case covers was that member's only
  writer. Added `nextRequiredArgs` to the asserted-projection invariant and re-pointed the guidance
  and model reference ranges after this leaf's line movement. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T04:10+02:00 — Created by the 260831-LOCR-L30 follow-up curator pass. Documents the
  three cases, the one-cell-per-case fixture convention, and the checkpoint projection the new case
  pins (which is the exact set of assertions that failed before the `checkpointed` branch existed).
  Verification metadata is pinned to the leaf base commit and remains closeout-owned.

- 2026-09-12T01:26:36+00:00: Generated citation repair: `_post_integration_phase`; `retry_cleanup` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:255-329; mcp/src/agents_remember/worktrees/modules/guidance.py:302-302. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b5cbe38ab438de766feb0fc3860228f5125b623ebbee641f90211d51326d68e; claim bytes unchanged; generated by ccr-r10@v1.
