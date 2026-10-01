# mcp/src/agents_remember/worktrees/sync_transaction_git.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

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
- **Cancel after a memory conflict restores a tracked cache first (L37).** The memory merge removes a tracked
  `memory.md` from the index, which leaves it on disk as an untracked file; `git merge --abort` then refuses to
  overwrite it. `rollback_side` therefore calls `discard_memory_cache_changes(side)` before the abort: a tracked
  cache is restored from `HEAD`, an untracked one is removed, and the code side is untouched. An abort that still
  does not restore the head raises `_abort_failure`, which names Git's own stderr. Lines that untrack the cache (every
  active line) could already cancel; 48 dormant branches still track it.

### Todos

No new file-local follow-up is identified by this source reconciliation. **One orientation the referential refusal names is deliberately not reachable from here** — *restore the removed row*, where the arriving side deleted a parent the left still references — because the retraction this path can author is bounded to rows the arriving delta *inserted*. That case keeps its refusal and its own `next_action`, and it is recorded as a limitation in the leaf's evidence (`notes/reports/2026-09-21-l40-conflict-diagnosis/EVIDENCE.md`), not as settled behaviour.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Exact refs, worktree identity, and authority-safe cleanup. [1]
- Typed dirty/WIP and restore proof exclude only the memory cache. [2]
- Content-domain conflicts and narrowly scoped cache state handling. [3]
- **The typed merge outcome that replaced the three-tuple, and the adapter's refusal and (since MIK-R24) the crossing report path it carries out of the merge.** [4]
- **The conflict routing: knowledge datasets settle in the transaction, the undecided remainder reaches the agent, and the explanation travels with it.** [5]
- **The authored retry's Git half, which is the same route the automatic pass takes.** [6]
- **The adapter the routing calls, and the one importer that makes this module depend on the application layer rather than on the memory domain.** [7]
- Native merge, exact continuation, and cache-free merge output; both entry points carry the paired code commit to the final memory merge, which first closes any master-line crossing history file the merge adds. [8]
- **The crossing branch of the memory merge (MIK-R24 rule 8): the plan is computed before Git merges, then replaces the merge's knowledge and onboarding paths, and the report path rides the outcome.** [9]
- The crossing helpers this module drives. [10]
- The managed sync crosses an unconverted leaf into a converted line, and leaves overlapping edits to the curator. [11]
- The staged memory tree is validated against both parents before the commit; a refusal raises and leaves the merge staged. [12]
- The managed sync refuses a merge with duplicate IDs, keeps it staged, and syncs after the repair. [13]
- Rollback and created-head proof retain exact operation ownership. [14]
- **Public regression covers cache-only success, true content conflict/continue, preserved WIP, and the structured diagnosis with its authored reconcile.** [15]
- **The real two-sided dataset case that proves the sync completes, both sides survive, and the caller invoked no merge entry point.** [16]
- **The cases that assert the diagnosis reaches the public response, that one authored decision settles it, that the row-less shape is retracted, that the orientation with nothing to retract advertises only a route that works, and that a schema disagreement is reported rather than reconciled.** [17]

- The rollback restores the cache before the merge abort. [18]
- A failed abort names Git's reason. [19]
- Cancel after a memory conflict restores the branch and its tracked cache. [20]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
