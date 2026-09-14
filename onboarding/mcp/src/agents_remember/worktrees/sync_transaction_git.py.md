# mcp/src/agents_remember/worktrees/sync_transaction_git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_git.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file owns every exact Git mutation and proof for resumable sync. It makes retained conflicts,
agent continuation, exact result attribution, rollback, temporary worktree cleanup, and the
resolution of a divergent memory merge mechanical rather than caller-specific. Every proof here is
about Git state — which head a merge may create, which refs the operation pinned, and whether a
resolution is staged — and deliberately none of them judges what the ledger file says.

## Code Commentary

### Logic

`read_ref` first validates the complete ref name with `git check-ref-format`, then resolves exactly
`<ref>^{commit}` through `git rev-parse --verify --quiet --end-of-options`. Only the latter
command's missing-ref return code becomes `None`; an invalid name or any other inspection failure
raises `SyncGitProofError` with Git's detail. Pinned refs are then created and deleted by
expected-value checks, so malformed authority cannot masquerade as absent authority. Temporary
worktrees are created only for the journaled repository/branch and are removed only when clean.
Checkout proof compares repository identity and branch, while helpers inspect status, MERGE_HEAD,
and unmerged paths.

`start_side_merge` attempts the pinned source merge and leaves a genuine conflict in place. A
divergent memory merge is staged without auto-commit and `_finish_staged_memory_merge` commits
Git's own resolution of the two pinned parents as they stand; the staged `memory.md` is not re-judged
against either parent's row list. `validate_staged_resolution` proves the exact MERGE_HEAD, zero
unmerged/unstaged paths, and index sanity before `continue_side_merge` commits. Completion accepts
only the admitted fast-forward or a two-parent commit with exact pre-sync/source parents.
`rollback_side` restores only an active or completed operation-owned delta and refuses later work.

### Conventions

All Git commands use the shared bounded runner. `SyncGitProofError` means live Git cannot be
attributed exactly to this journal generation; callers return manual-repair/cancel guidance rather
than weakening the proof.

### Invariants And Boundaries

- A conflict is retained only when MERGE_HEAD equals the pinned source and unmerged paths exist.
- Missing exact refs are distinct from invalid ref names and Git inspection failures.
- Continue commits only a fully staged exact retained merge.
- A memory resolution is proved as Git history alone: the admitted fast-forward or the exact
  two-parent commit, with no row list required of the `memory.md` it carries. The ledger is derived
  state and its rebuild is its authority, so a row the rebuild cannot resolve is a reported
  exclusion — `ledger_projection` publishes `sourceRowsExcluded`, `sourceExcludedRows` and
  `sourceExcludedReasons` for it — never a sync refusal.
- Automatic rollback refuses unrelated/later commits or dirty post-sync work.
- Temporary worktree removal and ref deletion are evidence-checked, never best-effort deletion.

## Parked-Candidate Git Primitives

`worktree_dirty_paths` reads every dirty path the worktree holds, untracked included, from
NUL-separated porcelain (`status --porcelain -z -uall`) — the only form that never quotes a path —
and skips the second entry of a rename/copy pair. `park_worktree_wip` stashes the exact candidate
with `--include-untracked` and refuses if the worktree is still dirty or no stash entry appeared.
`apply_parked_wip` reapplies a recorded stash and classifies the result: a nonzero exit with no
conflict is a hard proof error, never a silent skip.

`prove_parked_wip_restored` is the restore proof. A parked path counts as restored when the
worktree reports it dirty again, or when the carried result already holds exactly the parked
content (`<stash>^{tree}:<path>` / `<stash>^3:<path>` equal to `<carried_head>:<path>`) — a clean
reapply the moved source made identical. Anything else fails the proof, the stash is kept, and the
transaction refuses with `sync-git-proof-failed`. `drop_parked_wip` drops exactly the recorded stash
by matching its commit in a bounded `git stash list`, never another entry.
`discard_conflicted_wip_reapply` is cancel-only: it clears a conflicted reapply (refusing if an
active merge sits outside cancel authority) while the candidate itself stays safe in its stash.

### Todos

Reconcile line ranges after Dagger fixes; verification remains empty for the uncommitted source.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Side records carry the exact repository, worktree, commits, refs, plan, and conflict set proven here. | `SyncSideRecord` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67 |
| The driver records retained conflicts and delegates continue through these proof functions. | "def _continue_resolution("; "def continue_side_merge("; "def validate_staged_resolution(" | mcp/src/agents_remember/worktrees/sync_transaction.py:540-571; mcp/src/agents_remember/worktrees/sync_transaction_git.py:329-350; mcp/src/agents_remember/worktrees/sync_transaction_git.py:353-372 |
| Recovery uses exact-created-head and rollback proof before restoring or finalizing. | "def _recover_from_refs("; "def exact_created_head("; "def rollback_side(" | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:315-373; mcp/src/agents_remember/worktrees/sync_transaction_git.py:406-414; mcp/src/agents_remember/worktrees/sync_transaction_git.py:375-403 |
| The parked-candidate Git primitives read exact dirty paths, park with untracked files, reapply with conflict classification, prove restoration, drop exactly the recorded stash, and clear a cancel-only conflicted reapply. | `worktree_dirty_paths`; `park_worktree_wip`; `apply_parked_wip`; `prove_parked_wip_restored`; `drop_parked_wip`; `discard_conflicted_wip_reapply` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:126-148; mcp/src/agents_remember/worktrees/sync_transaction_git.py:151-164; mcp/src/agents_remember/worktrees/sync_transaction_git.py:167-180; mcp/src/agents_remember/worktrees/sync_transaction_git.py:183-199; mcp/src/agents_remember/worktrees/sync_transaction_git.py:216-232; mcp/src/agents_remember/worktrees/sync_transaction_git.py:202-213 |
| The automatic memory merge commits Git's own resolution and proves only its pinned parents; the module's docstring records the ledger ruling. | `_finish_staged_memory_merge`; "Developer ruling on the 260913 ledger line" | mcp/src/agents_remember/worktrees/sync_transaction_git.py:304-326; mcp/src/agents_remember/worktrees/sync_transaction_git.py:7-15 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the ledger-ruling changes
  this card records are the frozen ones. Re-checked the cited ranges and the prose: they hold. No
  wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit (the deleted ledger validators and the parked-WIP primitives).
  Re-read the card against the current source: all twelve cited ranges hold and the history already
  names every deletion. No wording changed; verification metadata remains closeout-owned.
- 2026-09-14T13:20+02:00 — The ledger ruling reaches the sync: removed the sync-side row-preservation
  rule (`validate_current_memory_side`, `validate_completed_side`, `_validate_parent_ledgers`,
  `_validate_required_ledger_rows`, `_ledger_rows` and their call sites), so this module proves Git
  state only — `_finish_staged_memory_merge` commits the pinned memory merge without re-judging
  either parent's row list, and `validate_staged_resolution` proves the staged resolution alone. The
  ledger is derived state and its rebuild is its authority, so a row the rebuild cannot resolve is
  reported by `ledger_projection` rather than refused here. Rewrote the Purpose, the merge/continue
  Logic, and the parent-row invariant, and re-derived every reference anchor against the current
  source (the module docstring grew and the parked-candidate primitives moved with it). Verification
  remains closeout-owned.

- 2026-09-10T15:06+02:00 — Parked-candidate Git primitives: recorded `worktree_dirty_paths`, `park_worktree_wip`, `apply_parked_wip`, `prove_parked_wip_restored`, `drop_parked_wip`, and the cancel-only `discard_conflicted_wip_reapply`, including the restore proof's exact-content branch. Re-derived the retained proof anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T14:32+02:00 — Removed the unrequested per-code uniqueness rule from staged
  memory-merge validation. Exact parent-row preservation remains mandatory and same-code history is
  retained. Verification remains closeout-owned.

- 2026-08-26T06:20+02:00 — Reconciled exact authority-ref lookup: validate the ref name first,
  return absence only for quiet exact verification's missing-ref result, and preserve every other
  Git failure as `SyncGitProofError`. No test-execution claim is made.

- 2026-08-26T02:55+02:00 — Drafted exact Git-proof onboarding for the resumable sync partition;
  final citations and verification remain open.