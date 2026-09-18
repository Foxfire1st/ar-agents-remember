# mcp/src/agents_remember/worktrees/sync_transaction_git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_git.py` |
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

Own exact Git mutation and proof for resumable code and memory-content sync, including parked WIP, retained conflicts, continuation, rollback, and temporary worktree cleanup.

## Code Commentary

### Logic

Ref reads distinguish invalid names, absent refs, and inspection errors. Pinned refs use expected-value creation/deletion, and worktree identity includes the recorded repository and branch. A completed side must be the admitted fast-forward or an exact two-parent merge in pre-sync/source order.

Dirty-path and WIP helpers take the typed side record. Only the memory domain excludes root memory.md. Before a native operation, only that disposable path is restored/cleaned so its local edits cannot obstruct Git or enter a stash; substantive WIP is still parked with untracked files and later restored and proved.

An admitted divergent memory merge runs without auto-commit. A cache-only conflict removes only memory.md from the merge index. Real content conflicts remain unresolved; when content is ready, the cache ignore rule is added to the same ordinary memory merge and the exact parents are checked. No standalone cache commit is created. Continue previews inspect content without mutation. Both fresh and resumed staged memory merges re-prove HEAD/MERGE_HEAD, remaining content conflicts, tracked unstaged changes, and cached diff validity before committing. The code side treats a file named memory.md as ordinary content.

The cache is refreshed as a disposable view after applicable memory results. A narrow cache-only stash conflict recovery additionally requires a clean content prestate and the existing restored-WIP proof. Other Git failures remain errors. Rollback and temporary removal retain exact side/ref identity and refuse later substantive work.

### Conventions

All commands use the shared runner. `SyncGitProofError` exposes an unproven Git transition. Cache stripping is domain- and path-specific; it is not an ours/theirs policy for other files.

### Invariants And Boundaries

- Memory cache state cannot block dirty/WIP, native merge, resolution preview, or admitted continuation.
- Real unresolved content is retained with its stash or MERGE_HEAD evidence.
- Code-side memory.md keeps normal Git conflict semantics.
- Only the pinned fast-forward or exact admitted two-parent merge is accepted.
- No cache-only commit or cached-row authority is introduced.

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
| Exact refs, worktree identity, and authority-safe cleanup. | `read_ref`; `require_side_checkout`; `delete_pinned_ref` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:27-39; mcp/src/agents_remember/worktrees/sync_transaction_git.py:54-62; mcp/src/agents_remember/worktrees/sync_transaction_git.py:83-89 |
| Typed dirty/WIP and restore proof exclude only the memory cache. | `worktree_dirty_paths`; `park_worktree_wip`; `prove_parked_wip_restored` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:117-141; mcp/src/agents_remember/worktrees/sync_transaction_git.py:144-163; mcp/src/agents_remember/worktrees/sync_transaction_git.py:198-216 |
| Content-domain conflicts and narrowly scoped cache state handling. | `content_conflicts` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:285-292 |
| Native merge, exact continuation, and cache-free merge output. | `start_side_merge`; `_finish_staged_memory_merge`; `continue_side_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:363-396; mcp/src/agents_remember/worktrees/sync_transaction_git.py:399-411; mcp/src/agents_remember/worktrees/sync_transaction_git.py:414-435 |
| Rollback and created-head proof retain exact operation ownership. | `exact_created_head` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:491-499 |
| Public regression covers cache-only success, true content conflict/continue, and preserved WIP. | `test_memory_merge_discards_only_cache_conflicts_and_preserves_content_conflicts` | mcp/tests/test_worktree_sync.py:330-411 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Fixed native legacy-memory.md conflicts and surrounding WIP/status/continuation boundaries; cache-only conflicts now progress while real content conflicts and code-domain memory.md remain ordinary Git facts. The existing public regression also interrupts before publication, proves an unstaged real edit refuses with refs unchanged, and completes after the intended edit is staged. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

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
