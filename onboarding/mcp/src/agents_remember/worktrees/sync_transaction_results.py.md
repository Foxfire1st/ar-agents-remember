# mcp/src/agents_remember/worktrees/sync_transaction_results.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

The body describes the uncommitted CYCLE-02-remainder working candidate. The commit fields identify the base the candidate sits on; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Centralize typed public results for resumable sync, preserving phase, preview, resolution-owner, and terminal replay semantics.

## Code Commentary

### Logic

Result builders cover the memory policy choice, initial preview, retained merge/WIP conflict, staged-resolution and parked-WIP previews, active/cancel/reconcile previews, completed/cancelled replay, and no-authority quarantine replay. Retained conflicts name the agent, the side, the exact worktree/files, and contract-addressed continue/cancel calls.

**The retained-conflict builder now decides what to do next, and that is CYCLE-02's remainder in this module.** `_resolution_guidance` takes precedence in three shapes. When the journaled `knowledgeConflict` admits an authored decision (`decisions` non-empty), the response's `nextOperation` becomes `reconcile_knowledge_resolution` with `nextArgs` built by `_reconcile_args` from the **journaled** diagnosis — the exact `table` and `record_id` the engine refused, and the decision left as a `"<keep-left|keep-right>"` placeholder because choosing it is the agent's act and not this projection's. That replaced a loop: repeating the generic continuation against a retained knowledge conflict returned the same generic conflict forever. A parked candidate reapply keeps the shipped continuation, and a retained conflict that admits *no* decision (a schema disagreement, or the referential orientation whose retraction the merge measured as unavailable) also keeps it, with a summary that says what the caller must do via `_unsettled_instruction`. `resolution_required` publishes the diagnosis at `resolution.knowledge` as well, so the file name is no longer the whole answer.

**The summary of a conflict no decision settles names which unsettled conflict it is, because the two need different work.** `_unsettled_instruction` splits that sentence on the one fact that decides the caller's next act. A referential refusal whose `precondition` is `no_arriving_insertion` is the orientation where the *arriving* side removed a row the retained side still cites: nothing the arriving delta inserted can account for the violation, so no arriving insertion can be retracted, and the caller restores the removed row or retracts the reference in the worktree dataset, stages it and continues — or cancels, which the same response still carries beside that call. Every other unsettled conflict keeps the shipped "resolve it in the worktree, stage it, then continue". This is the half of the CYCLE-02 residue that lives in this module: the first response used to promise that the merge continues while advertising a `keep-left` that provably could not apply, and driving exactly that advertised call returned the identical response forever. What is advertised now is the route that exists — `continue_sync_resolution` with `resolution_action=continue` — and the offer itself is read from the journaled diagnosis, so a conflict the merge measured as unretractable advertises no decision and no reconcile operation at all.

**A crossing sync's resolution names its report (MIK-R24 rule 8).** When the side record journals a
`crossingReport`, `resolution_required` adds `resolution.crossing`, the output of
`knowledge_crossing.crossing_summary`: the report path, the conflicted-item count, the first 100
`(path, item, reason)` entries with a truncation flag, the cards taken from each side, the moved marker
rows, the record-conflict history owner, and `howToResolve`. It also appends one sentence to the summary.
That sentence says this is a crossing sync, names the report, and says that every conflicted JSON item holds
a `crossing-conflict` marker the knowledge validator refuses until it is resolved. For an ordinary sync
`crossingReport` is empty and nothing is added, so the payload is unchanged.

**The `continue` replay of a completed sync recomputes the worklist (MIK-R08 rule 8).**
`terminal_resolution_replay` with `resolution_action='continue'` on a completed generation now returns
`with_recomputed_worklist(completed_sync_result(...), contract)`, so the replay carries the same optional
`knowledgeWorklist` summary as the original finalization (review R1 F2). A worklist failure leaves the
replayed result unchanged.

`reconcile_preview` is the read-only dry run of that operation: it reports the conflict the journal holds, the decisions it admits, and that the decision would be applied and the merge validated afterwards — it does not predict the merge's answer, because whether the decision settles it is the merge's. `resolution_validation_preview` now carries the same `knowledge` projection, so a dry run answers "what is still unresolved" with the row rather than only the path.

Resolution previews read `content_conflicts(side)`: memory-side root memory.md is excluded while code-side files and genuine memory content remain visible. `resolution_validation_preview` delegates the exact staged-content/MERGE_HEAD proof. `parked_wip_validation_preview` reports whether the real reapply conflicts are settled; it does not mutate an index, drop a stash, or create a commit.

### Conventions

All builders return WorktreeCommandResult and reuse shared side/recovery payload owners. A wipRestore marker distinguishes a parked-candidate reapply from the source merge itself. The knowledge diagnosis is projected through one owner (`_conflict_subject`) so every builder names the refused row the same way, and the reconcile arguments are read from the journal rather than re-derived from the databases.

### Invariants And Boundaries

- A preview reports readiness without performing the continuation; `reconcile_preview` asserts no prediction about the outcome.
- Memory cache-only index state cannot become a manual resolution requirement.
- Real conflict guidance keeps both continue and cancel addresses; a reconcile-shaped conflict keeps `cancelArgs` too, so the authored path never removes the way out.
- A completed generation cannot be retroactively cancelled.
- Quarantine replay does not claim branch restoration without authority refs.
- **The advertised reconcile call is built from the journal, never from a fresh read.** A resumed sync therefore advertises the same call the first response did, and the decision placeholder stays a placeholder: this layer never chooses a side.
- **The advertised continuation is one that exists.** Where the journaled diagnosis admits no decision — a schema disagreement, or the referential orientation whose retraction the merge measured as unavailable — the response advertises `continue_sync_resolution` with the manual `resolution_action`, carries `cancelArgs` beside it, and says in its summary which conflict it holds and what the caller must do (`_unsettled_instruction`). It never advertises a reconcile call for a conflict that cannot be reconciled, which is the byte-identical loop this module's guidance exists to replace.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- Conflict ownership and parked-WIP versus merge result shapes, including the journaled knowledge diagnosis. [1]
- A crossing sync's resolution carries the crossing summary and names the report; an ordinary sync's payload is unchanged. [2]
- **The next-move decision: reconcile when the conflict admits a decision, otherwise the continuation that exists — with a summary saying which unsettled conflict this is.** [3]
- **The sentence telling the caller what to do about a conflict no decision settles, split by the merge's measured retraction precondition.** [4]
- **The advertised reconcile call, built from the journal with the decision left to the agent.** [5]
- **The one place the refused row is named in a sentence, shared by every builder.** [6]
- **The read-only preview of authoring a decision, which predicts nothing about the merge.** [7]
- Parked-candidate reapply preview. [8]
- Staged-resolution preview, which now carries the knowledge projection on a dry run. [9]
- Policy choice and non-mutating initial/active/cancel previews. [10]
- Terminal and no-authority replay results remain distinct; the `continue` replay of a completed generation recomputes the worklist. [11]
- Content-domain conflict and staged-resolution proof is delegated to the Git owner. [12]
- **The journaled diagnosis these builders project, and the response fields that carry it.** [13]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
