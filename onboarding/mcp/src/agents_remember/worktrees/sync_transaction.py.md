# mcp/src/agents_remember/worktrees/sync_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file is the state-machine driver for resumable, contract-addressed mid-task source
synchronization. It replaces abort-and-block merge handling with one durable generation that an
agent can observe, continue after resolving a retained conflict, cancel, or recover.

## Code Commentary

### Logic

`sync_contract_under_authority` validates typed inputs, reads the stable enclosure-root store, and
routes missing/malformed journal recovery, quarantine replay, identity checks, active resume,
terminal replay, or new admission. No integration lock survives the return, so conflict resolution
happens between calls in the reported worktree.

Admission reads the exact official pair, validates its external-memory ledger mapping, plans each
side as already-current/fast-forward/merge/skip, checks non-temporary worktrees before any refs are
pinned, writes the journal, creates temporary `.sync` worktrees for series sides, and starts code
then memory. A genuine merge conflict records the side and conflict files without aborting. Continue
validates the exact staged merge and advances the same generation; cancel delegates exact rollback.
Automatic replay reconciles a side whose operation-owned commit already exists and finalizes only
after both participating sides are proven. `_already_current_result` reports a pair whose recorded
bases and work branches already carry the source on that Git evidence alone: a memory branch that
already descends from its source is current whatever its `memory.md` says, because the ledger is
derived state, its rebuild is its authority, and the rows the rebuild cannot resolve are reported
there rather than refused here.

### Conventions

The driver delegates durable models/store, Git proof, authority, results, and recovery to focused
modules; it owns only phase routing. Input refusals happen before selector, refs, journal, or Git
mutation. State is returned as `WorktreeCommandResult`. The top-level safety boundary translates
unexpected I/O, proof, and value failures into `sync-operation-refused`, names the caught failure
family in the summary, and preserves `str(error)` in the structured `detail` field so a useful Git
or journal refusal is not collapsed into a generic status.

### Invariants And Boundaries

- One active generation is addressed by canonical contract, never a public operation id.
- A current pair is proved from its recorded bases and branch ancestry, never from the rows the
  carried `memory.md` happens to hold.
- Pinned source/base/pre-sync refs plus the stable journal are recovery authority.
- Retained conflicts are agent-owned action, not terminal failure.
- Continue/cancel cannot change the admitted memory-sync choice.
- Normal sync fails closed for malformed, missing-after-admission, or identity-invalid journal state.
- Queue rows and task prose never reconstruct operation lifecycle evidence.

## Parked Worktree Candidate

A closeout-time leaf is dirty by definition, so the transaction parks each dirty moving side's
candidate before it carries the moved source. `_admit_participating_sides` is the single pre-journal
gate: it runs `_preflight_participating_sides`, returns `sync_preview` for `dry_run`, and otherwise
calls `_park_participating_wip`. Only a side this transaction will actually move parks:
`_side_parks_wip` skips a `temporary` side and any side planned `already-current` or `skip`, so an
unchanged side and every temporary series worktree are left exactly as before.

`_park_participating_wip` stashes each dirty side with `park_worktree_wip`
(`git stash push --include-untracked --message "<_wip_stash_message>"`), journals the exact stash
commit, the bounded path sample (`WIP_PATH_SAMPLE_LIMIT = 128`) and the true path count on the side
record, and only then is the admission record written — so the parked identity rides the same
`store.write` that admits the transaction. A park that fails calls `_restore_already_parked` to undo
whatever was already parked and refuses with `sync-side-preflight-failed`; if that restoration also
fails, the refusal names each stranded stash id.

`_preflight_participating_sides` now refuses only a worktree whose index already has unmerged paths
(`_require_parkable_worktree`) or whose checkout cannot be proven (`require_side_checkout`, status
read). A merely dirty moving side is parked, not refused. Restore happens on the completed path
(`_run_side`, `_continue_resolution`), on resume (`_reconcile_completed_sides`), and on cancel
(`sync_transaction_recovery.cancel_sync`); the agent-resolved continuation is
`_continue_parked_wip_restore`. The last safety net is `require_parked_wip_settled` in
`finalize_sync`, which refuses to finalize while any side still parks its candidate. See
[`sync_transaction_authority.py`](sync_transaction_authority.py.md) and
[`sync_transaction_git.py`](sync_transaction_git.py.md) for the restore proof.

### Todos

State-machine claims and citations are reconciled to the frozen source; commit-derived verification
remains closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Strict journal records and read-only status projection live at the enclosure root. | `SyncSideRecord`; `SyncOperationRecord`; `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67; mcp/src/agents_remember/worktrees/sync_transaction_state.py:70-87; mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366; mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385 |
| Admission and pinned identity validate contract/source/ledger authority. | `preflight_official_pair`; `pin_authority`; `require_pinned_authority` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:126-158; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:161-166; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:169-183 |
| Git operations retain conflicts and prove exact staged, completed, or rolled-back heads. | `start_side_merge`; `continue_side_merge`; `validate_staged_resolution`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:264-301; mcp/src/agents_remember/worktrees/sync_transaction_git.py:329-350; mcp/src/agents_remember/worktrees/sync_transaction_git.py:353-372; mcp/src/agents_remember/worktrees/sync_transaction_git.py:375-403 |
| Finalization, cancellation, quarantine, and damaged-journal escape are separate recovery ownership. | `finalize_sync`; `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:56-92; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:159-190; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:193-263; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:266-283 |
| Public result constructors keep recovery guidance consistent across phases. | `memory_choice_required`; `resolution_required`; `active_preview`; `cancel_preview`; `terminal_resolution_replay`; `quarantine_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:28-50; mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-113; mcp/src/agents_remember/worktrees/sync_transaction_results.py:173-187; mcp/src/agents_remember/worktrees/sync_transaction_results.py:190-207; mcp/src/agents_remember/worktrees/sync_transaction_results.py:210-245; mcp/src/agents_remember/worktrees/sync_transaction_results.py:248-261 |
| The parkability preflight, the park-and-journal admission, and the stash message are the driver's new pre-journal boundary. | `_admit_participating_sides`; `_park_participating_wip`; `_side_parks_wip`; `_wip_stash_message`; `_restore_already_parked` | mcp/src/agents_remember/worktrees/sync_transaction.py:240-254; mcp/src/agents_remember/worktrees/sync_transaction.py:263-300; mcp/src/agents_remember/worktrees/sync_transaction.py:257-260; mcp/src/agents_remember/worktrees/sync_transaction.py:303-309; mcp/src/agents_remember/worktrees/sync_transaction.py:312-333 |
| A dirty moving side is parked; only an unmerged index or an unprovable checkout refuses. | `_preflight_participating_sides`; `_require_parkable_worktree` | mcp/src/agents_remember/worktrees/sync_transaction.py:390-405; mcp/src/agents_remember/worktrees/sync_transaction.py:408-416 |
| Restore runs on the completed path, on resume, and through the agent-resolved parked continuation. | `_run_side`; `_continue_resolution`; `_continue_parked_wip_restore`; `_reconcile_completed_sides` | mcp/src/agents_remember/worktrees/sync_transaction.py:509-537; mcp/src/agents_remember/worktrees/sync_transaction.py:540-571; mcp/src/agents_remember/worktrees/sync_transaction.py:574-595; mcp/src/agents_remember/worktrees/sync_transaction.py:598-630 |
| The parked-candidate path sample is bounded and the true count is journaled beside it. | `WIP_PATH_SAMPLE_LIMIT` | mcp/src/agents_remember/worktrees/sync_transaction.py:79-79 |
| An already-current pair is decided by recorded bases and branch ancestry, not by the rows the carried ledger holds. | `_already_current_result` | mcp/src/agents_remember/worktrees/sync_transaction.py:336-362 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the already-current
  branch no longer validates the parent memory side, as the earlier entry records. Re-checked all
  fourteen cited ranges against the frozen source: they hold. No wording changed. Verification
  metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/sync_transaction.py` changed since the recorded verification
  commit. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the already-current branch no longer validates the parent memory
  side). Re-read the card: it already records that removal and all fourteen cited ranges still hold.
  No wording changed; verification metadata remains closeout-owned.
- 2026-09-14T13:20+02:00 — The ledger ruling reaches the driver: `_already_current_result` reports an
  already-descendant pair as `already-current` on its recorded bases and branch ancestry alone, and
  the `validate_current_memory_side` call that used to refuse it with `sync-work-branch-invalid` is
  gone. Recorded that boundary in Logic and as a local invariant, and re-derived every reference
  anchor (the Git, recovery, park-boundary, and driver ranges all moved). Verification remains
  closeout-owned.

- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `SyncOperationRecord`, `SyncOperationStore`, `SyncSideRecord`, `observe_sync_operation` repointed to mcp/src/agents_remember/worktrees/sync_transaction_state.py:172-366, mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385, mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67, mcp/src/agents_remember/worktrees/sync_transaction_state.py:70-87. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-09-10T15:06+02:00 — Parked-candidate curation: recorded the new pre-journal admission (`_admit_participating_sides`, `_park_participating_wip`, `_side_parks_wip`, `_wip_stash_message`, `_restore_already_parked`), the narrowed parkability preflight (`_require_parkable_worktree`), the completed/resume/agent-resolved restore paths, and the bounded `WIP_PATH_SAMPLE_LIMIT`. A dirty moving side is now parked rather than refused; unmerged index entries and unprovable checkouts still refuse. Re-derived every cited range against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the resumable state machine and its
  detail-preserving controlled refusal boundary.

- 2026-08-26T06:20+02:00 — Recorded that the public refusal boundary preserves the lower-level
  proof failure's exact detail while keeping the result controlled. No test-execution claim is
  made.

- 2026-08-26T02:55+02:00 — Drafted resumable-sync driver onboarding against the pre-Dagger
  partition; final state vocabulary, citations, and verification remain open.