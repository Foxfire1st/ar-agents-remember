# mcp/tests/test_transaction_only_worktree_delivery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_transaction_only_worktree_delivery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T07:05+02:00 |
| lastVerifiedCommitHash | `4214d7a103dcc120481c6fe0059b322396ec9be6` |
| lastVerifiedCommitDate | 2026-09-14T07:21:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Protects the CCR-R12@v5 transaction-only closeout and integration boundary at the public worktree
tool surface.

## Code Commentary

The focused tests patch strict code quality, memory quality, selected certification, and curator
coherence entry points to fail if normal closeout or integration calls them. They then exercise the
real public closeout and paired integration routes: closeout must produce the code, external-memory,
and ledger commits with the exact ledger mapping; integration must publish the prepared pair; and a
source-ref movement must refuse before protected pair publication.

Each scenario installs a real failing `pre-commit` hook in both repositories and probes it once to
prove the hook itself is active, then asserts that the normal code and memory transaction commits
leave no hook log. This captures the bounded commit contract: closeout stages and uses
`commit_verified_staged` with `--no-verify`, while integration moves existing refs/tree state and
creates no merge commit or merge-hook path.

`_assert_memory_attribution` (`:183-227`) is the shared attribution reader the closeout scenarios call
with the real commit shas the public routes returned. It reads the memory-content commit back out of the
object and asserts `%B` equals `MESSAGES.memory` plus `\n\nCode-Commit: <code commit>`, that the literal
`Code-Commit:` appears exactly once, that `git interpret-trailers --parse` returns
`Code-Commit: <code commit>`, and that `git log --format=%(trailers:key=Code-Commit)` returns the same
trailer. The mandatory `memory.md`-only ledger commit is asserted to return `""` from that same reader:
it has no code counterpart to name, so it is deliberately left unattributed.

**Since 260913-LCA-L4 the reader serves two routes, and the recovery route is the second one.**
`test_closeout_recovery_attributes_the_memory_commit_it_still_owed` (`:328-452`) interrupts a real public
closeout *after* its code commit by making `closeout_external._refresh_external_memory` raise, asserts the
contract holds a code commit but no memory-content commit, then resumes exactly as the recovery route does
— a `WorktreeArgs` carrying `LifecycleOperationRecoveryCommits(codeCommit=..., memoryContentCommit="",
ledgerCommit="")` through `git_worktree_manager.closeout_result`. The recovery cell is load-bearing rather
than decoration: the same call with a cell naming another code commit refuses first with `does not match
task HEAD`, which is what makes the resume the recovery route rather than a fresh closeout that happens to
agree with it. The case then reads both documented git readers against the resumed shas. That module has
no memory-content commit site of its own, so this case is the behavioural half of the census in
`mcp/tests/test_memory_attribution_producers.py`: it proves the resumed path reaches the producer the
first attempt uses.

## Invariants And Boundaries

- Normal public closeout/integration does not acquire a quality or certification acceptance tool.
- Closeout preserves the code-to-memory ledger mapping and sequential recovery evidence.
- The memory-content commit object carries exactly one `Code-Commit:` trailer naming the code commit
  that same closeout landed, and it reads as trailer data to both documented git readers; the
  `memory.md`-only ledger commit carries none. Since 260913-LCA-L4 this holds for **both** the first
  attempt and the resumed recovery route, and the file gained the recovery case that proves it; the
  assertions themselves were introduced by L1.
- The recovery resume is a real public route: the journal cell is supplied as data, a wrong cell refuses
  before any mutation, and the case asserts the contract's code commit is unchanged by the resume.
- The task documents these scenarios build carry both derived fields, exactly as `task_doc` stamps
  them against a leaf contract. Since 260913-LCA-L5 a leaf document with an exact enclosure address
  but no `seriesContractPath` refuses closeout by name
  (`task-enclosure-binding-master-link-missing`), so a fixture that withheld the field would model the
  damage state a later start repairs, not the document a start produces.
- Integration refuses source movement before changing the protected pair.
- Hook non-invocation is tested only for the configured repository hooks installed by the scenario;
  it does not imply that arbitrary external commands cannot run outside these commit paths.
- This file records focused behavior protection, not full-suite certification or independent review.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public closeout delivers code, memory, and ledger while acceptance helpers are forbidden. | `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:230-325 |
| The memory-content commit carries exactly one `Code-Commit` trailer naming the landed code commit, read back by `%B`, by `git interpret-trailers --parse`, and by `%(trailers:key=Code-Commit)`; the ledger commit returns `""` from the same reader. | `_assert_memory_attribution` | mcp/tests/test_transaction_only_worktree_delivery.py:183-227 |
| The recovery route's behavioural case: a real public closeout interrupted after its code commit, resumed from the journalled cell, with a wrong cell refused first and the same two git readers asserted on the resumed shas. | `test_closeout_recovery_attributes_the_memory_commit_it_still_owed` | mcp/tests/test_transaction_only_worktree_delivery.py:328-452 |
| Public integration publishes the prepared pair without acceptance helpers and without configured hooks. | `test_public_integration_merges_prepared_pair_without_acceptance_tools` | mcp/tests/test_transaction_only_worktree_delivery.py:455-508 |
| Source movement refuses before protected pair publication. | `test_public_integration_ref_movement_refuses_before_pair_merge` | mcp/tests/test_transaction_only_worktree_delivery.py:511-564 |
| The task-binding helper now binds both derived fields, because a leaf document with an exact enclosure address but no `seriesContractPath` refuses closeout instead of passing silently. | `_bind_task_without_review` | mcp/tests/test_transaction_only_worktree_delivery.py:93-116 |

## Update History
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
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_closeout_commits_code_memory_and_ledger_without_acceptance_tools` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:172-257. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_integration_merges_prepared_pair_without_acceptance_tools` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:260-313. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `test_public_integration_ref_movement_refuses_before_pair_merge` repointed to mcp/tests/test_transaction_only_worktree_delivery.py:316-369. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-10T07:24:09+02:00 — Added with CCR-R12@v5 source commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`. The hook-aware focused run passed 3 tests in 5.95s (measured wall 6.213346s); this is targeted behavior evidence and not a full-suite or certification claim.
