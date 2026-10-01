# mcp/src/agents_remember/worktrees/sync_transaction_state.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file defines and stores the strict stable state for one resumable worktree-sync generation.
The journal lives below the enclosure root so status, continuation, cancellation, and damage
recovery do not depend on a readable task document or queue projection.

## Code Commentary

### Logic

`SyncSideRecord` binds each participating side to exact repositories/worktrees/branches, admitted
source/pre-sync/base commits, three authority refs, plan, progress, result head, conflicts, the
engine's own explanation of a retained knowledge conflict, and the
parked worktree candidate (`wipState`, `wipStash`, `wipPaths`, `wipPathCount`).
`SyncOperationRecord` records one generation, canonical contract/task/kind, original bases, phase,
memory policy, both sides, and timestamps. `SyncQuarantineRecord` is terminal proof that corrupt
evidence was archived without rollback authority. The store path is
`reports/sync-operation.json` (`SYNC_OPERATION_RECORD_NAME`); the pre-move
`.lifecycle/sync-operation.json` survives only as `legacy_sync_operation_path` read tolerance, and
the first write retires the legacy copy. Authority refs derive from a hash of the contract path.

`SyncOperationStore` strictly lstat/opens without following nonregular entries, parses only operation
or quarantine records, writes atomically, preserves raw malformed bytes, and can atomically archive
opaque directory/symlink/other entries with bounded metadata. `observe_sync_operation` projects
malformed, quarantined, identity-mismatched, conflict, cancelling, terminal, or resumable state with
contract-addressed next/cancel arguments and without parsing task truth.

### Conventions

Models are frozen and reject extra fields. The store is single-record; repository integration
authority serializes writers. Observation is total and read-only, while archival happens only in
explicit recovery.

### Invariants And Boundaries

- Stable lifecycle state is at the enclosure root, not in task or queue files.
- Nonregular or malformed journal entries never become normal operation records.
- Raw/opaque evidence is preserved before replacement; quarantine is explicit terminal vocabulary.
- Identity mismatch points cancellation at the locator-proven requested contract and exposes the
  journal path separately.
- The public projection omits private authority refs and commit-detail internals.

## Parked-Candidate Journal Fields

`SyncWipState = Literal["", "parked", "restore-conflict", "restored"]` names the parked-worktree
candidate on `SyncSideRecord`: `""` means nothing parked, `parked` means the candidate is in the
recorded stash, `restore-conflict` means it could not be reapplied onto the carried result and still
needs its resolver, and `restored` means it is back in the worktree. Because `SyncSideRecord` is
frozen and `extra="forbid"`, these fields are part of the durable journal schema, so a record from
another build is refused rather than misread.

`_active_sync_projection` distinguishes the two retained-conflict shapes: for a side whose
`wipState == "restore-conflict"` the summary says "Resolve the parked <side> candidate reapply,
then continue worktree_sync", otherwise it keeps the retained-merge wording. The parked facts are
also projected to callers through `side_payload`'s conditional `wip` block.

**L40 journals the diagnosis, and the reason is that the diagnosis has to survive the response that
carried it.** `SyncSideRecord.knowledgeConflict: SyncKnowledgeConflict | None` holds the merge engine's
own explanation for a conflicted knowledge dataset this side retained — the path, the row-level
`MergeConflict` (table, operation and exact refused key), the typed `KnowledgeRefusal` with the action
it advertises, this seam's `detail` when the engine never answered, and the authored decisions that
conflict admits. It is **journaled rather than only returned** because the agent reads it again on
every later call: `_active_sync_projection` re-projects this side's state from the journal, so without
the field a resumed sync could say only which file is unresolved while the first response had said
exactly which row to reconcile. The projection carries it through `knowledgeConflict`, and the field
is cleared with `conflictFiles` when the retained merge is finally settled, so a completed sync cannot
re-advertise a reconcile call for a conflict that no longer exists. Because `SyncSideRecord` is frozen
with `extra="forbid"`, the field is part of the durable journal schema: a record from another build is
refused rather than misread.

**L43 journals the accepted decisions beside the conflict they answer, and that is what makes the
recovery terminate.** `SyncSideRecord.knowledgeReconciliations: tuple[AuthoredReconciliation, ...] = ()`
holds every authored decision this side's retained knowledge merge has already accepted, in the order
they were accepted. They travel **together** into the next attempt, because a decision that settled one
conflict has to still hold when the merge goes on to the next one: with only the newest decision
carried, a two-conflict merge alternates between the same two rows forever and re-offers a decision
that has already been made and already had its effect. The field is cleared with `knowledgeConflict`
when the retained merge is finally settled, so a completed sync carries no stale decisions; and, like
`knowledgeConflict`, it is part of the durable journal schema under `extra="forbid"`, so a record from
another build is refused rather than misread.

**MIK-R24 journals a crossing sync's report path, and only for a crossing sync.**
`SyncSideRecord.crossingReport: str = ""` (at most 4,096 characters) holds the path of the crossing report
that `worktrees/knowledge_crossing.write_crossing_report` wrote into the worktree group's `reports/`. The
resolution payload names that report and summarises it. The wrap serializer `_omit_empty_crossing_report`
drops the key when it is empty, so an ordinary sync's journal keeps exactly the shape the installed,
pre-MIK-R24 runtime reads (architect ruling N2, 2026-09-29). Journals written by older builds still load,
because the field defaults to `""`.

### Todos

Final nonregular handling and public model fields are reconciled to the frozen source;
commit-derived verification remains closeout-owned.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- The driver treats this store as the sole current generation and routes recovery from its strict outcomes. [1]
- Recovery archives damaged entries, writes quarantine, or reconstructs cancellation from refs. [2]
- Public status embeds this journal projection without moving its authority into task/queue state. [3]
- The strict side record now journals the parked candidate's state, stash identity, bounded path sample, true path count, the engine's explanation of a retained knowledge conflict, and every authored decision this side has already accepted for it. [4]
- The crossing report path is journaled for a crossing sync only; an empty one is omitted, so ordinary journals stay readable by the installed runtime. [5]
- The active projection distinguishes a parked-candidate reapply from a retained merge, and re-projects the journaled knowledge diagnosis. [6]
- **The journaled diagnosis's own vocabulary: the row the engine refused, the action it advertised, and the decisions that conflict admits.** [7]

### Cross-Repo References

No cross-repository source is configured for this memory root.
