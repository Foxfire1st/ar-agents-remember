# mcp/src/agents_remember/worktrees/sync_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-10T15:06+02:00 |
| lastVerifiedCommitHash |  `7833df0b219bba560f67f6e1158c3f4f155e1ce6`|
| lastVerifiedCommitDate |  2026-08-26T15:02:28+02:00|
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
after both participating sides are proven.

### Conventions

The driver delegates durable models/store, Git proof, authority, results, and recovery to focused
modules; it owns only phase routing. Input refusals happen before selector, refs, journal, or Git
mutation. State is returned as `WorktreeCommandResult`. The top-level safety boundary translates
unexpected I/O, proof, and value failures into `sync-operation-refused`, names the caught failure
family in the summary, and preserves `str(error)` in the structured `detail` field so a useful Git
or journal refusal is not collapsed into a generic status.

### Invariants And Boundaries

- One active generation is addressed by canonical contract, never a public operation id.
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
| Strict journal records and read-only status projection live at the enclosure root. | `SyncSideRecord`; `SyncOperationRecord`; `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67; mcp/src/agents_remember/worktrees/sync_transaction_state.py:70-87; mcp/src/agents_remember/worktrees/sync_transaction_state.py:155-305; mcp/src/agents_remember/worktrees/sync_transaction_state.py:308-324 |
| Admission and pinned identity validate contract/source/ledger authority. | `preflight_official_pair`; `pin_authority`; `require_pinned_authority` | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:126-158; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:161-166; mcp/src/agents_remember/worktrees/sync_transaction_authority.py:169-183 |
| Git operations retain conflicts and prove exact staged, completed, or rolled-back heads. | `start_side_merge`; `continue_side_merge`; `validate_staged_resolution`; `rollback_side` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:253-293; mcp/src/agents_remember/worktrees/sync_transaction_git.py:318-344; mcp/src/agents_remember/worktrees/sync_transaction_git.py:345-368; mcp/src/agents_remember/worktrees/sync_transaction_git.py:369-399 |
| Finalization, cancellation, quarantine, and damaged-journal escape are separate recovery ownership. | `finalize_sync`; `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:57-93; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:160-191; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:194-264; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:267-284 |
| Public result constructors keep recovery guidance consistent across phases. | `memory_choice_required`; `resolution_required`; `active_preview`; `cancel_preview`; `terminal_resolution_replay`; `quarantine_replay` | mcp/src/agents_remember/worktrees/sync_transaction_results.py:28-50; mcp/src/agents_remember/worktrees/sync_transaction_results.py:71-113; mcp/src/agents_remember/worktrees/sync_transaction_results.py:173-187; mcp/src/agents_remember/worktrees/sync_transaction_results.py:190-207; mcp/src/agents_remember/worktrees/sync_transaction_results.py:210-245; mcp/src/agents_remember/worktrees/sync_transaction_results.py:248-261 |
| The parkability preflight, the park-and-journal admission, and the stash message are the driver's new pre-journal boundary. | `_admit_participating_sides`; `_park_participating_wip`; `_side_parks_wip`; `_wip_stash_message`; `_restore_already_parked` | mcp/src/agents_remember/worktrees/sync_transaction.py:241-255; mcp/src/agents_remember/worktrees/sync_transaction.py:264-301; mcp/src/agents_remember/worktrees/sync_transaction.py:258-261; mcp/src/agents_remember/worktrees/sync_transaction.py:304-310; mcp/src/agents_remember/worktrees/sync_transaction.py:313-334 |
| A dirty moving side is parked; only an unmerged index or an unprovable checkout refuses. | `_preflight_participating_sides`; `_require_parkable_worktree` | mcp/src/agents_remember/worktrees/sync_transaction.py:389-404; mcp/src/agents_remember/worktrees/sync_transaction.py:407-415 |
| Restore runs on the completed path, on resume, and through the agent-resolved parked continuation. | `_run_side`; `_continue_resolution`; `_continue_parked_wip_restore`; `_reconcile_completed_sides` | mcp/src/agents_remember/worktrees/sync_transaction.py:508-536; mcp/src/agents_remember/worktrees/sync_transaction.py:539-570; mcp/src/agents_remember/worktrees/sync_transaction.py:573-594; mcp/src/agents_remember/worktrees/sync_transaction.py:597-629 |
| The parked-candidate path sample is bounded and the true count is journaled beside it. | `WIP_PATH_SAMPLE_LIMIT` | mcp/src/agents_remember/worktrees/sync_transaction.py:80-80 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-10T15:06+02:00 — Parked-candidate curation: recorded the new pre-journal admission (`_admit_participating_sides`, `_park_participating_wip`, `_side_parks_wip`, `_wip_stash_message`, `_restore_already_parked`), the narrowed parkability preflight (`_require_parkable_worktree`), the completed/resume/agent-resolved restore paths, and the bounded `WIP_PATH_SAMPLE_LIMIT`. A dirty moving side is now parked rather than refused; unmerged index entries and unprovable checkouts still refuse. Re-derived every cited range against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of the resumable state machine and its
  detail-preserving controlled refusal boundary.

- 2026-08-26T06:20+02:00 — Recorded that the public refusal boundary preserves the lower-level
  proof failure's exact detail while keeping the result controlled. No test-execution claim is
  made.

- 2026-08-26T02:55+02:00 — Drafted resumable-sync driver onboarding against the pre-Dagger
  partition; final state vocabulary, citations, and verification remain open.