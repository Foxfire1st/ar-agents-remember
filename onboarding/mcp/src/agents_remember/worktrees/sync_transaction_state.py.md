# mcp/src/agents_remember/worktrees/sync_transaction_state.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Strict enclosure-root durable state for one resumable sync generation.

## Code Commentary

### Logic

Side records pin repositories/worktrees/branches, source/pre-sync/base facts, authority refs, phase progress, file conflicts, structural report and parked stash/path facts. Operation records bind generation and original bases; quarantine preserves damaged evidence without rollback authority. [4]

The narrow _drop_retired_knowledge_keys adapter removes old knowledgeConflict and knowledgeReconciliations on read because a sync already in flight at retirement must resume/cancel. No current row diagnosis/decision is stored; other extras remain forbidden. [7]

The stable store rejects malformed/nonregular normal records and preserves evidence before explicit recovery. Projection distinguishes retained merge from parked reapply, and empty structural report is omitted. [5] [6]


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

- Observation grants no mutation authority.
- Old keys are read tolerance, never a current reconcile route.

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


**MIK-R24 journals a crossing sync's report path, and only for a crossing sync.**
`SyncSideRecord.crossingReport: str = ""` (at most 4,096 characters) holds the path of the crossing report
that `worktrees/knowledge_crossing.write_crossing_report` wrote into the worktree group's `reports/`. The
resolution payload names that report and summarises it. The wrap serializer `_omit_empty_crossing_report`
drops the key when it is empty, so an ordinary sync's journal keeps exactly the shape the installed,
pre-MIK-R24 runtime reads (architect ruling N2, 2026-09-29). Journals written by older builds still load,
because the field defaults to `""`.


## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.


### Repo-Internal References


- Current strict side/operation records. [4]


- Optional report serialization. [5]


- Retained phase/parked candidate projection. [6]


- Specific old-key adapter and current file resolution. [7]



- The driver treats this store as the sole current generation and routes recovery from its strict outcomes. [11]
- Recovery archives damaged entries, writes quarantine, or reconstructs cancellation from refs. [12]
- The crossing report path is journaled for a crossing sync only; an empty one is omitted, so ordinary journals stay readable by the installed runtime. [13]


### Cross-Repo References

No cross-repository source is configured for this memory root.


No cross-repository contract is established by this file.
