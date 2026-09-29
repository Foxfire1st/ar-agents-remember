# mcp/src/agents_remember/worktrees/sync_transaction_git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_git.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T07:08:34+02:00 |
| lastVerifiedCommitHash | `8b0254263c6998b1d4814b2e97c1bd231d39350f` |
| lastVerifiedCommitDate | 2026-09-29T15:00:35+02:00|
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

**Since MIK-R22, the memory merge is validated before it is committed.** `start_side_merge` and `continue_side_merge` take an optional keyword `paired_code` (a `worktrees.knowledge_validation.PairedCode`: the code side's settled result commit) and thread it through `_existing_side_merge` and `_continue_memory_merge` to `_finish_staged_memory_merge`. After the cache ignore rule is staged, that function writes the staged index as a tree (`git write-tree`) and calls `memory_commit_refusal` with the tree, both parents (`preSyncHead`, `sourceCommit`) and `paired_code`, before `git commit --no-edit`. A refusal raises `SyncKnowledgeValidationError`, a subclass of `SyncGitProofError`, and the merge stays staged: nothing is committed, and `HEAD` and `MERGE_HEAD` are unchanged. Unconverted memory, where neither the candidate nor a parent holds `knowledge/layout.json`, gets `None` from the helper and commits exactly as before. Code-side merges and memory plans that are not a merge (fast-forward, skip, already-current) are not validated here.

**Since MIK-R24, a memory merge can be a crossing sync (rule 8).** `start_side_merge` takes an optional
keyword `crossing_owner` (`("leaf" | "master", task or leaf ID)`) and asks `_crossing` **before** Git touches
the worktree. `_crossing` returns `None` for a code side or when `knowledge_crossing.crossing_applies` finds
the merge base, the own side (`preSyncHead`) and the incoming side (`sourceCommit`) all alike. For an
unconverted line that is always the case, so an ordinary sync runs exactly as before. When one tree is
converted and another is not, `_crossing` returns `crossing_plan(...)`; a crossing without an owner is
refused at step `markers`. A failing step raises `SyncGitProofError` naming it, with the line untouched.
The merge argv is then the same as ever (`merge --no-commit --no-edit <source>` for memory). For a crossing,
`_apply_crossing_merge` accepts Git exit 0 or 1 with `MERGE_HEAD` at the source, then:

1. replaces every `knowledge/` and `onboarding/` path with the plan (`apply_crossing`: clean paths staged,
   conflicted ones unmerged with stages 1-3);
2. writes the crossing report into the worktree group's `reports/` (`write_crossing_report`);
3. continues through `_continue_memory_merge`, returning the outcome with `crossing_report` set.

`SideMergeOutcome.crossing_report` (default `""`) carries the report path to the driver, which journals it.
`_finish_staged_memory_merge` also calls `close_crossing_history` right after the cache ignore rule is
staged. That call sets `closed: true` on, and stages, each master-line `<task-id>-crossing-<n>.json` the
merge adds. The validator then checks the staged tree, with the unconverted parent replaced by its
conversion (the composition binds `GitBaseConverter`), so rule 8 step 5 is enforced at the commit. Each
conflicted JSON item holds a `crossing-conflict` marker that the validator refuses, and Markdown conflicts
keep Git markers, so `continue` cannot commit an unresolved crossing item.

**`reconcile_side_merge` is the authored retry's Git half, and it is deliberately the same route the automatic pass takes.** It re-materialises the three index stages, calls `settle_knowledge_conflict` with the **sequence** of decisions this side has already accepted — the journaled ones plus the one just authored, so each attempt starts from the conflict the previous attempt actually reached rather than from the first one again — republishes the settled dataset into the worktree and stages it. Nothing about the conflict is interpreted here — which row, which decision and whether the decision is expressible at all are the adapter's answers — and it returns `None` when the path settled or the adapter's *fresh* explanation when it did not, so a decision that settles the first conflict and reveals a second reports that second one exactly as the first was. The caller finishes the merge through the ordinary continuation, so a reconciled sync is a normal sync with one authored input rather than a second route.


The cache is refreshed as a disposable view after applicable memory results. A narrow cache-only stash conflict recovery additionally requires a clean content prestate and the existing restored-WIP proof. Other Git failures remain errors. Rollback and temporary removal retain exact side/ref identity and refuse later substantive work.

### Conventions

All commands use the shared runner. `SyncGitProofError` exposes an unproven Git transition; its subclass `SyncKnowledgeValidationError` is the validator's refusal, which the driver catches first so it is reported as `sync-knowledge-validation-refused`. Cache stripping is domain- and path-specific; it is not an ours/theirs policy for other files.

### Invariants And Boundaries

- Memory cache state cannot block dirty/WIP, native merge, resolution preview, or admitted continuation.
- Real unresolved content is retained with its stash or MERGE_HEAD evidence.
- **A knowledge dataset is settled by the transaction, and only what the adapter will not decide reaches the agent — with the engine's reason.** `settle_knowledge_conflicts` runs before the `resolution-required` return, so the conflict list a caller receives is the post-routing one; a schema disagreement is still the agent's, and the returned owner is still the agent for exactly those paths. What is new is that `SideMergeOutcome.refused` carries the attribution out with them.
- **The routing decides nothing, and neither does the authored retry.** It republishes and stages a structurally merged dataset; it takes no compatibility verdict on the merged knowledge, and the merge adapter's own refusal is what keeps a path conflicted. `reconcile_side_merge` interprets neither the row nor the decision.
- **A retry that reveals the next conflict reports it rather than finishing.** A settled first conflict is not a settled merge, so the fresh explanation is returned and journaled exactly as the first one was.
- **A crossing sync is never merged as plain Git, and never commits a conflict silently (MIK-R24 rule 8).** The plan is computed before Git runs; an unbound crossing port or a missing paired code commit refuses; every conflicted item stays unmerged or marked until the curator resolves it.
- Code-side memory.md keeps normal Git conflict semantics.
- Only the pinned fast-forward or exact admitted two-parent merge is accepted.
- No cache-only commit or cached-row authority is introduced.
- **A converted memory merge is never committed without a passing validator run (MIK-R22 rule 8).** The staged tree is validated against both parents and the paired code commit before `git commit`; a refusal, an unbound validator, an unknown paired code commit, or an unreadable tree leaves the merge staged. There is no parameter that skips the validation.

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
| Exact refs, worktree identity, and authority-safe cleanup. | `read_ref`; `require_side_checkout`; `delete_pinned_ref` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:70-82; mcp/src/agents_remember/worktrees/sync_transaction_git.py:126-132; mcp/src/agents_remember/worktrees/sync_transaction_git.py:97-105 |
| Typed dirty/WIP and restore proof exclude only the memory cache. | `worktree_dirty_paths`; `park_worktree_wip`; `prove_parked_wip_restored` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:160-184; mcp/src/agents_remember/worktrees/sync_transaction_git.py:187-206; mcp/src/agents_remember/worktrees/sync_transaction_git.py:241-259 |
| Content-domain conflicts and narrowly scoped cache state handling. | `content_conflicts` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:328-335 |
| **The typed merge outcome that replaced the three-tuple, and the adapter's refusal and (since MIK-R24) the crossing report path it carries out of the merge.** | `SideMergeOutcome` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:52-67 |
| **The conflict routing: knowledge datasets settle in the transaction, the undecided remainder reaches the agent, and the explanation travels with it.** | `_continue_memory_merge`; `settle_knowledge_conflicts` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:383-415; mcp/src/agents_remember/worktrees/knowledge_conflict.py:241-257 |
| **The authored retry's Git half, which is the same route the automatic pass takes.** | `reconcile_side_merge`; `settle_knowledge_conflict` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:418-444; mcp/src/agents_remember/worktrees/knowledge_conflict.py:201-238 |
| **The adapter the routing calls, and the one importer that makes this module depend on the application layer rather than on the memory domain.** | `merge_conflicted_stages` | mcp/src/agents_remember/application/knowledge_merge.py:113-181 |
| Native merge, exact continuation, and cache-free merge output; both entry points carry the paired code commit to the final memory merge, which first closes any master-line crossing history file the merge adds. | `start_side_merge`; `_finish_staged_memory_merge`; "close_crossing_history"; `continue_side_merge` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:462-512; mcp/src/agents_remember/worktrees/sync_transaction_git.py:570-598; mcp/src/agents_remember/worktrees/sync_transaction_git.py:601-622 |
| **The crossing branch of the memory merge (MIK-R24 rule 8): the plan is computed before Git merges, then replaces the merge's knowledge and onboarding paths, and the report path rides the outcome.** | `_crossing`; `_apply_crossing_merge`; "crossing_report" | mcp/src/agents_remember/worktrees/sync_transaction_git.py:537-567; mcp/src/agents_remember/worktrees/sync_transaction_git.py:515-534; mcp/src/agents_remember/worktrees/sync_transaction_git.py:67-67 |
| The crossing helpers this module drives. | `crossing_plan`; `apply_crossing`; `write_crossing_report`; `close_crossing_history` | mcp/src/agents_remember/worktrees/knowledge_crossing.py:80-112; mcp/src/agents_remember/worktrees/knowledge_crossing.py:150-160; mcp/src/agents_remember/worktrees/knowledge_crossing.py:237-262; mcp/src/agents_remember/worktrees/knowledge_crossing.py:201-222 |
| The managed sync crosses an unconverted leaf into a converted line, and leaves overlapping edits to the curator. | `test_the_managed_sync_crosses_an_unconverted_leaf_into_a_converted_line`; `test_a_crossing_leaves_overlapping_edits_to_the_curator_and_a_failed_step_changes_nothing` | mcp/tests/test_knowledge_crossing.py:403-431; mcp/tests/test_knowledge_crossing.py:434-499 |
| The staged memory tree is validated against both parents before the commit; a refusal raises and leaves the merge staged. | `memory_commit_refusal`; `SyncKnowledgeValidationError` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:581-592; mcp/src/agents_remember/worktrees/sync_transaction_git.py:48-49 |
| The managed sync refuses a merge with duplicate IDs, keeps it staged, and syncs after the repair. | `test_the_managed_sync_refuses_a_merge_with_duplicate_ids_until_it_is_repaired` | mcp/tests/test_knowledge_validator_routes.py:156-188 |
| Rollback and created-head proof retain exact operation ownership. | `rollback_side`; `exact_created_head` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:646-675; mcp/src/agents_remember/worktrees/sync_transaction_git.py:678-686 |
| **Public regression covers cache-only success, true content conflict/continue, preserved WIP, and the structured diagnosis with its authored reconcile.** | `test_memory_merge_settles_content_and_knowledge_conflicts_in_the_transaction`; `_assert_knowledge_conflict_scenarios`; `_assert_memory_content_conflict_scenarios` | mcp/tests/test_worktree_sync.py:698-719; mcp/tests/test_worktree_sync.py:721-761; mcp/tests/test_worktree_sync.py:763-844 |
| **The real two-sided dataset case that proves the sync completes, both sides survive, and the caller invoked no merge entry point.** | `_assert_knowledge_database_conflict_settles` | mcp/tests/test_worktree_sync.py:150-186 |
| **The cases that assert the diagnosis reaches the public response, that one authored decision settles it, that the row-less shape is retracted, that the orientation with nothing to retract advertises only a route that works, and that a schema disagreement is reported rather than reconciled.** | `_assert_knowledge_conflict_is_diagnosed_and_reconciled`; `_assert_delete_reference_conflict_is_retracted`; `_assert_unretractable_delete_reference_advertises_its_real_route`; `_assert_schema_disagreement_is_reported_not_reconciled` | mcp/tests/test_worktree_sync.py:268-354; mcp/tests/test_worktree_sync.py:357-399; mcp/tests/test_worktree_sync.py:402-455; mcp/tests/test_worktree_sync.py:458-490 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Body update: the crossing branch of the memory merge (MIK-R24 rule 8).** Added a Logic paragraph covering `crossing_owner`, `_crossing` (planned before Git runs, inert when all three trees are alike), `_apply_crossing_merge`, `SideMergeOutcome.crossing_report`, and `close_crossing_history` inside `_finish_staged_memory_merge`. Added an invariant: a crossing is never merged as plain Git and never commits a conflict silently. The reopened `_finish_staged_memory_merge` row was reworded to name the history closing and re-cited to the function's own extent (`570-598`). Added three rows: the crossing branch, the helpers, and the managed-sync tests.
- 2026-09-29T12:06:08+00:00: Generated citation repair: `content_conflicts` repointed to mcp/src/agents_remember/worktrees/sync_transaction_git.py:328-335. No content impact: mechanical anchor-range projection bound to citation source snapshot 75677f16e5ed8ed01a37a3496ecf058f05e2f85f804720849cd36afc05309a98; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): documented the MIK-R22 validation of the staged memory merge (`write-tree`, `memory_commit_refusal` against both parents and the paired code commit, before `git commit`), the new `paired_code` keyword on `start_side_merge`/`continue_side_merge`, the `SyncKnowledgeValidationError` subclass, and the new invariant that a converted memory merge is never committed unvalidated. Re-measured the native-merge row (`continue_side_merge` changed) and added rows for the validation call and its route test. The verification stamp is unchanged; closeout owns it.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (uncommitted change set on `ar/260915-ks-l43-ar`, code base `fb719f89`): **the authored retry hands the adapter every decision the side has already accepted.** `reconcile_side_merge(side, path, reconciliations: Sequence[AuthoredReconciliation])` replaces the single `reconciliation` and forwards `tuple(reconciliations)` into `settle_knowledge_conflict`. The reason is the one the whole recovery repair turns on: each attempt must start from the conflict the previous attempt actually reached. Carrying only the newest decision made a two-conflict retained merge alternate between the same two rows forever, re-offering a decision that had already been made and already had its effect. Nothing else on this route changed — the row, the decision and whether the decision is expressible at all are still the adapter's answers, and a second revealed conflict is still reported exactly as the first was. **Stamp accounting:** the recorded working candidate is this leaf's candidate `ar/260915-ks-l43-ar` on base `fb719f89`; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded. No commit was made.
- 2026-09-20T07:30+02:00 — 260915-KS-L42 curator (citation repair in this document; this card's own source file is unchanged): **the three rows naming the integration population were re-cited to those constructs' own extents in the working tree.** This leaf's two new module-level helpers in `mcp/tests/test_worktree_sync.py` pushed the whole `WorktreeSyncTests` class down and grew the two scenario runners, so the ranges this card cited no longer held their anchors: the case and its two runners now read `:698-719`, `:721-761` and `:763-844` (was `:624-646`, `:647-679`, `:680-762`), `_assert_knowledge_database_conflict_settles` reads `:150-186` (was `:150-188`), and the three diagnostic cases read `:268-354`, `:357-399` and `:458-490` (was `:250-338`, `:339-383`, `:384-418`), with the new `_assert_unretractable_delete_reference_advertises_its_real_route` cited at `:402-455`. The Finding text of the third row gained the fact that case asserts — the orientation with nothing to retract advertises only a route that works. No anchor was renamed, no citation dropped and no claim weakened; this card's metadata was not touched and no verification stamp was advanced.

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
