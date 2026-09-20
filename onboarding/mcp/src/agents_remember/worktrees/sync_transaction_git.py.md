# mcp/src/agents_remember/worktrees/sync_transaction_git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_git.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T06:05+02:00 |
| reviewedWorkingCandidate | candidate `ar/260915-ks-l40-ar`, uncommitted; base `f79f4db745ad00b908d6ce4871d0b4ab2320207c` |
| lastVerifiedCommitHash | `74c6c693b8c5a5863ce15f016793192931f4adc1` |
| lastVerifiedCommitDate | 2026-09-20T06:22:08+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted CYCLE-02-remainder working candidate. The commit fields name the base the candidate sits on; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Own exact Git mutation and proof for resumable code and memory-content sync, including parked WIP, retained conflicts, continuation, rollback, and temporary worktree cleanup.

## Code Commentary

### Logic

Ref reads distinguish invalid names, absent refs, and inspection errors. Pinned refs use expected-value creation/deletion, and worktree identity includes the recorded repository and branch. A completed side must be the admitted fast-forward or an exact two-parent merge in pre-sync/source order.

Dirty-path and WIP helpers take the typed side record. Only the memory domain excludes root memory.md. Before a native operation, only that disposable path is restored/cleaned so its local edits cannot obstruct Git or enter a stash; substantive WIP is still parked with untracked files and later restored and proved.

An admitted divergent memory merge runs without auto-commit. A cache-only conflict removes only memory.md from the merge index. A content conflict is first offered to the knowledge merge adapter: `_continue_memory_merge` hands the conflicted paths, the work branch tip it started from and the arriving source commit to `settle_knowledge_conflicts`, which settles every path that is a knowledge dataset — republishing the union into the worktree and staging it — and returns a `KnowledgeConflictSettlement` naming the ones it would not decide *and why*. Only those remaining paths are real content conflicts that stay unresolved for the agent, so the routing narrows the agent's work rather than hiding any of it. **The merge's answer is now a typed `SideMergeOutcome` rather than a three-tuple**: `state`, the still-unmerged `conflicts`, Git's own `message`, and `refused` — the adapter's `RefusedKnowledgeStage` for a conflicted knowledge dataset, carrying the engine's row-level conflict and the action it advertised. That is what the driver journals and publishes, and it is the reason a resumed sync re-projects the diagnosis instead of only the file name. When content is ready, the cache ignore rule is added to the same ordinary memory merge and the exact parents are checked. No standalone cache commit is created. A settled dataset is structurally valid and nothing more: no compatibility verdict is taken on either side of the call. Continue previews inspect content without mutation. Both fresh and resumed staged memory merges re-prove HEAD/MERGE_HEAD, remaining content conflicts, tracked unstaged changes, and cached diff validity before committing. The code side treats a file named memory.md as ordinary content.

**`reconcile_side_merge` is the authored retry's Git half, and it is deliberately the same route the automatic pass takes.** It re-materialises the three index stages, calls `settle_knowledge_conflict` (singular) with the caller's `reconciliation` for that one conflict, republishes the settled dataset into the worktree and stages it. Nothing about the conflict is interpreted here — which row, which decision and whether the decision is expressible at all are the adapter's answers — and it returns `None` when the path settled or the adapter's *fresh* explanation when it did not, so a decision that settles the first conflict and reveals a second reports that second one exactly as the first was. The caller finishes the merge through the ordinary continuation, so a reconciled sync is a normal sync with one authored input rather than a second route.


The cache is refreshed as a disposable view after applicable memory results. A narrow cache-only stash conflict recovery additionally requires a clean content prestate and the existing restored-WIP proof. Other Git failures remain errors. Rollback and temporary removal retain exact side/ref identity and refuse later substantive work.

### Conventions

All commands use the shared runner. `SyncGitProofError` exposes an unproven Git transition. Cache stripping is domain- and path-specific; it is not an ours/theirs policy for other files.

### Invariants And Boundaries

- Memory cache state cannot block dirty/WIP, native merge, resolution preview, or admitted continuation.
- Real unresolved content is retained with its stash or MERGE_HEAD evidence.
- **A knowledge dataset is settled by the transaction, and only what the adapter will not decide reaches the agent — with the engine's reason.** `settle_knowledge_conflicts` runs before the `resolution-required` return, so the conflict list a caller receives is the post-routing one; a schema disagreement is still the agent's, and the returned owner is still the agent for exactly those paths. What is new is that `SideMergeOutcome.refused` carries the attribution out with them.
- **The routing decides nothing, and neither does the authored retry.** It republishes and stages a structurally merged dataset; it takes no compatibility verdict on the merged knowledge, and the merge adapter's own refusal is what keeps a path conflicted. `reconcile_side_merge` interprets neither the row nor the decision.
- **A retry that reveals the next conflict reports it rather than finishing.** A settled first conflict is not a settled merge, so the fresh explanation is returned and journaled exactly as the first one was.
- Code-side memory.md keeps normal Git conflict semantics.
- Only the pinned fast-forward or exact admitted two-parent merge is accepted.
- No cache-only commit or cached-row authority is introduced.

### Todos

No new file-local follow-up is identified by this source reconciliation. **One orientation the referential refusal names is deliberately not reachable from here** — *restore the removed row*, where the arriving side deleted a parent the left still references — because the retraction this path can author is bounded to rows the arriving delta *inserted*. That case keeps its refusal and its own `next_action`, and it is recorded as a limitation in the leaf's evidence (`notes/reports/2026-09-21-l40-conflict-diagnosis/EVIDENCE.md`), not as settled behaviour.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact refs, worktree identity, and authority-safe cleanup. | `read_ref`; `require_side_checkout`; `delete_pinned_ref` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:51-65; mcp/src/agents_remember/worktrees/sync_transaction_git.py:107-115; mcp/src/agents_remember/worktrees/sync_transaction_git.py:78-88 |
| Typed dirty/WIP and restore proof exclude only the memory cache. | `worktree_dirty_paths`; `park_worktree_wip`; `prove_parked_wip_restored` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:141-167; mcp/src/agents_remember/worktrees/sync_transaction_git.py:168-189; mcp/src/agents_remember/worktrees/sync_transaction_git.py:222-242 |
| Content-domain conflicts and narrowly scoped cache state handling. | `content_conflicts` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:309-318 |
| **The typed merge outcome that replaced the three-tuple, and the adapter's refusal it carries out of the merge.** | `SideMergeOutcome` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:35-50 |
| **The conflict routing: knowledge datasets settle in the transaction, the undecided remainder reaches the agent, and the explanation travels with it.** | `_continue_memory_merge`; `settle_knowledge_conflicts` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:364-396; mcp/src/agents_remember/worktrees/knowledge_conflict.py:240-256 |
| **The authored retry's Git half, which is the same route the automatic pass takes.** | `reconcile_side_merge`; `settle_knowledge_conflict` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:397-425; mcp/src/agents_remember/worktrees/knowledge_conflict.py:200-237 |
| **The adapter the routing calls, and the one importer that makes this module depend on the application layer rather than on the memory domain.** | `merge_conflicted_stages` | mcp/src/agents_remember/application/knowledge_merge.py:113-181 |
| Native merge, exact continuation, and cache-free merge output. | `start_side_merge`; `_finish_staged_memory_merge`; `continue_side_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:439-478; mcp/src/agents_remember/worktrees/sync_transaction_git.py:479-493; mcp/src/agents_remember/worktrees/sync_transaction_git.py:494-517 |
| Rollback and created-head proof retain exact operation ownership. | `rollback_side`; `exact_created_head` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:539-570; mcp/src/agents_remember/worktrees/sync_transaction_git.py:571-581 |
| **Public regression covers cache-only success, true content conflict/continue, preserved WIP, and the structured diagnosis with its authored reconcile.** | `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction`; `_assert_knowledge_conflict_scenarios`; `_assert_memory_content_conflict_scenarios` | mcp/tests/test_worktree_sync.py:624-646; mcp/tests/test_worktree_sync.py:647-679; mcp/tests/test_worktree_sync.py:680-762 |
| **The real two-sided dataset case that proves the sync completes, both sides survive, and the caller invoked no merge entry point.** | `_assert_knowledge_database_conflict_settles` | mcp/tests/test_worktree_sync.py:150-188 |
| **The cases that assert the diagnosis reaches the public response, that one authored decision settles it, that the row-less shape is retracted, and that a schema disagreement is reported rather than reconciled.** | `_assert_knowledge_conflict_is_diagnosed_and_reconciled`; `_assert_delete_reference_conflict_is_retracted`; `_assert_schema_disagreement_is_reported_not_reconciled` | mcp/tests/test_worktree_sync.py:250-338; mcp/tests/test_worktree_sync.py:339-383; mcp/tests/test_worktree_sync.py:384-418 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-20T06:05+02:00 — 260915-KS-L40 curator (uncommitted CYCLE-02-remainder change set on `ar/260915-ks-l40-ar`, code base `f79f4db7`): **the merge's answer stopped being a three-tuple, and this card gains the authored retry.** Recorded: `SideMergeOutcome` (`state`, `conflicts`, Git's `message`, and `refused` — the adapter's `RefusedKnowledgeStage`) replacing the tuple at `start_side_merge`, `_continue_memory_merge` and `_existing_side_merge`, and `reconcile_side_merge` as the authored retry's Git half. The reason the card needed a rewrite rather than an append is stated in it: the routing paragraph said the transaction receives "the ones it would not decide", and the whole point of this change set is that it now receives them *with the engine's reason*, which is what the driver journals so a resumed sync re-projects the diagnosis. Two invariants are added (the authored retry interprets neither the row nor the decision; a retry that reveals the next conflict reports it rather than finishing), and the Todos line records the one deliberately unreachable orientation — restore-the-removed-row — as an open limitation rather than settled behaviour. Verification metadata is **advanced to the candidate's base `f79f4db7`** with the working candidate named beside it; closeout owns the committed stamp.

- 2026-09-19T23:20+00:00 — 260915-KS-L31 curator (uncommitted CYCLE-02 change set on `ar/260915-ks-l31-ar`, code base `7dcec036`): **the memory merge now routes what Git cannot decide.** `_continue_memory_merge` gained a docstring and one call: the conflicted paths go to `settle_knowledge_conflicts` with the work branch tip it started from as `left` and the arriving source commit as `right` — exactly the left/right pair the adapter's request names — so a knowledge database, which is binary to Git and cannot be resolved by staging, is republished and staged inside the transaction, and only the paths the adapter declined are returned as `resolution-required`. The Logic paragraph that said real content conflicts remain unresolved is corrected rather than deleted: the remainder still does, and it is now the post-routing remainder. Two invariants were added (the routing decides nothing; the conflict list a caller receives is post-routing) and the reference table was repaired as well as extended — the renamed regression is re-cited by its current name and the shipped scenarios by their new helper, and the `start_side_merge` / `_finish_staged_memory_merge` / `continue_side_merge` ranges were re-read after the insertion moved them. Verification metadata is **not** advanced: the candidate is uncommitted and closeout owns the stamp.

- 2026-09-19T22:49:08+00:00: Generated citation repair: `rollback_side`; `exact_created_head` repointed to mcp/src/agents_remember/worktrees/sync_transaction_git.py:477-506; mcp/src/agents_remember/worktrees/sync_transaction_git.py:509-517. No content impact: mechanical anchor-range projection bound to citation source snapshot e67b35357c3610162648ff9c1506b2bd840c93c142fe18de408cd68cfbaf5daa; claim bytes unchanged; generated by ccr-r10@v1.
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
