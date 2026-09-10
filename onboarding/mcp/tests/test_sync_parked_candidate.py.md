# mcp/tests/test_sync_parked_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_parked_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T15:06+02:00 |
| lastVerifiedCommitHash | `4bbe2c37b0fa70b07af4ddbc247aeee1f58343b0` |
| lastVerifiedCommitDate | 2026-09-10T08:03:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

The transaction-level proof for the parked worktree candidate inside the existing sync
transaction. A closeout-time leaf is dirty by definition, so `worktree_sync` parks its WIP, carries
the moved source, and must return the candidate. These cases pin that contract against the real
sync transaction; the closeout boundary's own surface is pinned in
`test_source_lineage.py::CloseoutSourceLineageHealTests`.

## Code Commentary

### Logic

The suite reuses `SyncFixture` and its `commit_file` / `git` / `section` helpers from
`test_worktree_sync.py`, so the fixture Git flows under real repositories and canonical contracts.
Each case builds the dirty candidate, moves the official source, and asserts the exact transaction
outcome:

1. `test_parked_candidate_is_carried_and_returned` — untracked plus modified code WIP with a moved
   source: one sync reports `synced`, the code side's `wip.state` is `restored`, the candidate content
   is byte-identical, `git stash list` is empty, the work branch is at the source tip, and the
   recorded base advanced.
2. `test_parked_memory_candidate_is_carried_and_returned` — the same contract on the external-memory
   side.
3. `test_parked_candidate_reapply_conflict_is_retained_and_cancel_returns_it` — the moved source
   edits the file the parked WIP edits: `sync-resolution-required` with `resolution.wipRestore`,
   `README.md` in `resolution.files`, and the stash still holding the candidate; then
   `resolution_action=cancel` returns the candidate, restores the pre-sync head, and empties the
   stash.
4. `test_resume_returns_the_candidate_a_crash_left_parked` — a simulated crash before the restore
   (patching `restore_parked_wip` to raise once) leaves the candidate parked and absent from the
   worktree; the next call resumes, restores it, drops the stash, and finalizes.
5. `test_resolving_a_retained_merge_returns_the_parked_candidate` — a retained source merge conflict
   (no `wipRestore` flag) resolved and staged, then `resolution_action=continue`: the merge commits,
   the parked candidate comes back, the stash is empty, and the base advanced.
6. `test_unmerged_index_entries_still_refuse_the_sync` — a real pre-existing conflict refuses with
   `sync-side-preflight-failed` and names the unmerged paths, leaving no stash behind.

`git_unchecked` runs the one Git command whose nonzero exit is the expected outcome (creating the
real conflict), distinct from the fixture's fail-loud `git` helper.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts. Cases assert
exact payload states, byte-identical candidate content, stash emptiness, and the recorded base; a
focused green result here is not end-to-end closeout evidence.

### Invariants And Boundaries

- A parked candidate must come back byte-identical, and the stash must be empty on the clean path.
- A reapply conflict is retained, never silently dropped; `cancel` returns the candidate.
- Resume repairs a crash that left the candidate parked; it does not re-run the carried merge.
- The kept refusals (unmerged index entries) still refuse and leave no stash.
- Coverage percentages are diagnostic; these cases exist to protect distinct transaction outcomes,
  not to raise a floor.

### Todos

The unit-regression lane budget is untouched (this module was added to the existing
`unit-regression` lane rather than raising any case budget).

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite classifies its six retained parked-candidate transaction outcomes. | `ParkedCandidateTests` | mcp/tests/test_sync_parked_candidate.py:26-27 |
| The clean carry returns the candidate and advances the base. | `test_parked_candidate_is_carried_and_returned` | mcp/tests/test_sync_parked_candidate.py:29-53 |
| The same contract holds on the external-memory side. | `test_parked_memory_candidate_is_carried_and_returned` | mcp/tests/test_sync_parked_candidate.py:55-72 |
| A reapply conflict is retained and `cancel` returns the candidate. | `test_parked_candidate_reapply_conflict_is_retained_and_cancel_returns_it` | mcp/tests/test_sync_parked_candidate.py:74-99 |
| Resume returns a candidate a crash left parked. | `test_resume_returns_the_candidate_a_crash_left_parked` | mcp/tests/test_sync_parked_candidate.py:101-128 |
| Resolving a retained source merge still returns the parked candidate. | `test_resolving_a_retained_merge_returns_the_parked_candidate` | mcp/tests/test_sync_parked_candidate.py:130-155 |
| Unmerged index entries still refuse the sync and leave no stash. | `test_unmerged_index_entries_still_refuse_the_sync` | mcp/tests/test_sync_parked_candidate.py:157-172 |
| The suite reuses the shared real-Git sync fixture and helpers. | `SyncFixture`; `section`; `commit_file`; `git` | mcp/tests/test_worktree_sync.py:38-113; mcp/tests/test_worktree_sync.py:198-201; mcp/tests/test_worktree_sync.py:216-221; mcp/tests/test_worktree_sync.py:224-232 |
| The transaction behaviour under test is owned by the sync driver's park/restore boundary. | `_park_participating_wip`; `restore_parked_wip`; `_continue_parked_wip_restore`; `_reconcile_completed_sides` | mcp/src/agents_remember/worktrees/sync_transaction.py:264-301; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:356-395; mcp/src/agents_remember/worktrees/sync_transaction.py:573-594; mcp/src/agents_remember/worktrees/sync_transaction.py:597-629 |
| The lane manifest classifies this module. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-105 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-10T15:06+02:00 — Created for the parked-candidate change: the six transaction-level cases proving a dirty closeout candidate is parked, carried, and returned (with restore on completion, resume, and cancel, and the kept unmerged-index refusal). The new module has no committed identity yet, so verification remains closeout-owned.
