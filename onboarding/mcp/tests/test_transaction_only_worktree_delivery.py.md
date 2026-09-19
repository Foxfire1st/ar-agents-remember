# mcp/tests/test_transaction_only_worktree_delivery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| lastUpdated | 2026-09-19T19:52+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| path | `mcp/tests/test_transaction_only_worktree_delivery.py` |
| doc_type | `file-level-onboarding` |
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Protect public transaction-only closeout/integration and recovery with two accepted outputs and a disposable memory cache.

## Code Commentary

### Logic

The seven existing scenario definitions forbid the named quality, certification, curator, and review-related acceptance entry points while exercising the real transaction paths. Public closeout begins with malformed cache text and must create exactly one code commit and one memory commit; recovery begins with a missing cache, interrupts after code publication, rejects a wrong recovery code identity, and resumes without another code commit.

Configured failing pre-commit hooks are probed to prove they work, then the transaction scenarios assert no hook log. `_assert_memory_attribution` checks the exact memory message and both native trailer readers, and verifies memory.md is absent from the memory-content commit. The resulting cache is present and untracked; retired ledger result fields are absent. Integration still publishes exact refs and refuses a moved source before pair publication.

The sync/recloseout case passes the accepted code commit to _commit_memory_content and proves an unchanged memory candidate reuses the actual merged head. The final two cache tests derive canonical data from Git, keep an already-correct cache unchanged, recreate a missing cache, and repair malformed, forged, reordered, or header-inconsistent text. They compare refs and all commit objects in both repositories and preserve real file bytes and clean content state.

### Conventions

Existing mocks forbid acceptance-tool calls or inject the deliberate interruption; they do not mask production failures. The cache test fixture creates no ledger-only commit and never treats its observed cache as canonical input. Scenario definitions and their execution receipts are separate evidence.

### Invariants And Boundaries

- Normal transaction delivery does not acquire the forbidden acceptance tools.
- Recovery retains exact code identity and one real memory output.
- Both Git trailer readers see the attribution, while the committed tree contains no memory cache.
- Cache rebuilds change no refs, commit objects, or substantive content.
- Hook non-invocation applies to the installed scenario hooks, not arbitrary unrelated commands.

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
| Named acceptance-tool prohibition and real failing-hook probes. | `_forbid_acceptance_tools`; `_install_failing_pre_commit_hooks` | mcp/tests/test_transaction_only_worktree_delivery.py:120-146; mcp/tests/test_transaction_only_worktree_delivery.py:149-173 |
| One code/memory commit, cache absence from the committed tree, and both trailer readers. | `_assert_memory_attribution`; `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |
| Interrupted public closeout resumes only its exact accepted code identity. | `test_closeout_recovery_attributes_the_memory_commit_it_still_owed`; `test_public_closeout_commits_code_and_memory_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:321-448; mcp/tests/test_transaction_only_worktree_delivery.py:211-318 |
| Integration publishes accepted refs or refuses source movement before publication. | `test_public_integration_merges_prepared_pair_without_acceptance_tools`; `test_public_integration_ref_movement_refuses_before_pair_merge` | mcp/tests/test_transaction_only_worktree_delivery.py:451-504; mcp/tests/test_transaction_only_worktree_delivery.py:507-560 |
| A recloseout after sync records the actual memory head. | `test_recloseout_after_a_sync_records_the_memory_head_as_content_commit` | mcp/tests/test_transaction_only_worktree_delivery.py:574-607 |
| Cache materialization preserves both repositories' refs/commit objects and real content. | `assert_content_unchanged`; `git_state`; `test_cache_refresh_preserves_current_bytes_and_materializes_a_missing_cache`; `test_cache_refresh_repairs_malformed_forged_and_reordered_data_from_git` | mcp/tests/test_transaction_only_worktree_delivery.py:610-679; mcp/tests/test_transaction_only_worktree_delivery.py:682-702; mcp/tests/test_transaction_only_worktree_delivery.py:705-743 |
| None | `git_state`; `assert_content_unchanged`; `test_cache_refresh_preserves_current_bytes_and_materializes_a_missing_cache`; `test_cache_refresh_repairs_malformed_forged_and_reordered_data_from_git` | mcp/tests/test_transaction_only_worktree_delivery.py:648-672; mcp/tests/test_transaction_only_worktree_delivery.py:683-688; mcp/tests/test_transaction_only_worktree_delivery.py:682-702; mcp/tests/test_transaction_only_worktree_delivery.py:705-743 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## 260918-TSIP-L6 The Closed Payload's Own Address, Driven End To End

This module gained one assertion (`:275-284`) inside
`test_public_closeout_commits_code_and_memory_without_acceptance_tools`: the applied closeout
payload's `contractPath` must equal `contract.contract_path.as_posix()`. It is the **producer
half** of `260918-TSIP` `T54` — `status_payload` emits the snake_case `contract_path`, while the
guidance guard a seat's next move depends on reads `contractPath`/`enclosurePath`, so a closed
closeout declaring neither made the guard withhold the guidance **entirely** and the seat silently
lost "integrate the task branches". This is the only case that drives the real producer end to
end; the guard's own four cases are in `mcp/tests/test_response_address_binding.py`.

## Update History
- 2026-09-19T19:52+02:00 — 260918-TSIP-L6 curator (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): one assertion added (`:275-284`) — the applied closeout payload must declare its own `contractPath` — which is the producer half of `T54`, driven end to end. Every citation range re-derived against the candidate. Closeout owns the real commit stamp.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Kept seven collected scenarios while removing retired ledger imports/outputs and third commits; public malformed/missing-cache delivery and cache-only materialization now prove two-output, hook, ref, trailer, and zero-Git-mutation behavior. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.
- 2026-09-14T07:05+02:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): recorded that `_bind_task_without_review` now binds `seriesContractPath` alongside its
  canonical enclosure binding, and why — the helper had been modelling the damage state, and a leaf
  document with an exact enclosure address but no master link now refuses closeout by name
  (`task-enclosure-binding-master-link-missing`) instead of passing silently. Added that rule as an
  invariant and a reference row. Re-derived every range and both inline citations against the current
  source with AST: the change's one import plus seven lines in `_bind_task_without_review` shifted every
  later definition by seven (`_assert_memory_attribution` 176-221 → 183-227, closeout 223-318 → 230-325,
  recovery 321-445 → 328-452, integration 448-501 → 455-508, ref-movement 504-558 → 511-564).
  Verification metadata remains closeout-owned; no execution or acceptance claim.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): the file gained the recovery route's behavioural case,
  `test_closeout_recovery_attributes_the_memory_commit_it_still_owed` (`:321-445`) — a real public
  closeout interrupted after its code commit, resumed through `git_worktree_manager.closeout_result`
  with a `LifecycleOperationRecoveryCommits` cell that leaves the memory commit owed, plus a wrong-cell
  refusal asserted first so the resume is provably the recovery route. This is the behavioural half of
  the L4 producer census: the recovery module has no memory-content commit site of its own and reaches
  `closeout_external.py`'s producer transitively. Corrected the invariant that said the file gained no
  new test function (it did, at L4), recorded that the reader now serves two routes, and rebound every
  row shifted by the new imports and case (`_assert_memory_attribution` 172-215 → 176-221, closeout
  219-315 → 223-318, integration 317-370 → 448-501, ref-movement 373-427 → 504-558). Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T21:42+02:00 — 260913-LCA-L1 (uncommitted change set on `ar/260913-lca-l1-ar`): assertion-only extension. Added the shared `_assert_memory_attribution` reader and called it from `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools`, so the public closeout path is now checked for exactly one `Code-Commit: <code sha>` trailer inside the memory-content commit object (by `%B`, `git interpret-trailers --parse`, and `%(trailers:key=Code-Commit)`) and for no trailer at all on the `memory.md`-only ledger commit. The re-closeout test's direct call into `_commit_memory_content` now passes `code_commit=`. No new test function and no new parametrized case. Rebound every stale row (`test_public_closeout...` 219-315, `_assert_memory_attribution` 172-215, `test_public_integration_merges...` 317-370, `test_public_integration_ref_movement...` 373-427). Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_integration_ref_movement_refuses_before_pair_merge` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:316-369. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_integration_merges_prepared_pair_without_acceptance_tools` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:260-313. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:172-257. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T07:24:09+02:00 — Added with CCR-R12@v5 source commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`. The hook-aware focused run passed 3 tests in 5.95s (measured wall 6.213346s); this is targeted behavior evidence and not a full-suite or certification claim.
