# mcp/tests/test_sync_parked_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_parked_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
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
| The suite classifies its six retained parked-candidate transaction outcomes. | `ParkedCandidateTests` | mcp/tests/test_sync_parked_candidate.py:27-183 |
| The clean carry returns the candidate and advances the base. | `test_parked_candidate_is_carried_and_returned` | mcp/tests/test_sync_parked_candidate.py:30-54 |
| The same contract holds on the external-memory side. | `test_parked_memory_candidate_is_carried_and_returned` | mcp/tests/test_sync_parked_candidate.py:56-73 |
| A reapply conflict is retained and `cancel` returns the candidate. | `test_parked_candidate_reapply_conflict_is_retained_and_cancel_returns_it` | mcp/tests/test_sync_parked_candidate.py:75-110 |
| Resume returns a candidate a crash left parked. | `test_resume_returns_the_candidate_a_crash_left_parked` | mcp/tests/test_sync_parked_candidate.py:112-139 |
| Resolving a retained source merge still returns the parked candidate. | `test_resolving_a_retained_merge_returns_the_parked_candidate` | mcp/tests/test_sync_parked_candidate.py:141-166 |
| Unmerged index entries still refuse the sync and leave no stash. | `test_unmerged_index_entries_still_refuse_the_sync` | mcp/tests/test_sync_parked_candidate.py:168-183 |
| The suite reuses the shared real-Git sync fixture and helpers. | `SyncFixture`; `section`; `commit_file`; `git` | mcp/tests/test_worktree_sync.py:38-113; mcp/tests/test_worktree_sync.py:267-270; mcp/tests/test_worktree_sync.py:285-290; mcp/tests/test_worktree_sync.py:293-297 |
| The transaction behaviour under test is owned by the sync driver's park/restore boundary. | "def _park_participating_wip("; "def restore_parked_wip("; "def _continue_parked_wip_restore("; "def _reconcile_completed_sides(" | mcp/src/agents_remember/worktrees/sync_transaction.py:263-302; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:356-397; mcp/src/agents_remember/worktrees/sync_transaction.py:574-597; mcp/src/agents_remember/worktrees/sync_transaction.py:598-628 |
| The lane manifest classifies this module. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-105 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the shared sync fixture
  and park/restore owners are the frozen ones. Re-checked every case and helper range: they hold. No
  wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 7 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 1 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — Created for the parked-candidate change: the six transaction-level cases proving a dirty closeout candidate is parked, carried, and returned (with restore on completion, resume, and cancel, and the kept unmerged-index refusal). The new module has no committed identity yet, so verification remains closeout-owned.
