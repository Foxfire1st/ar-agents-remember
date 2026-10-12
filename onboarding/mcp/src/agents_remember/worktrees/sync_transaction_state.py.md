# mcp/src/agents_remember/worktrees/sync_transaction_state.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Strict enclosure-root durable state for one resumable sync generation.

## Code Commentary

### Logic

Side records pin repositories/worktrees/branches, source/pre-sync/base facts, authority refs, phase progress, file conflicts, structural report and parked stash/path facts. Operation records bind generation and original bases; quarantine preserves damaged evidence without rollback authority.

The narrow _drop_retired_knowledge_keys adapter removes old knowledgeConflict and knowledgeReconciliations on read because a sync already in flight at retirement must resume/cancel. No current row diagnosis/decision is stored; other extras remain forbidden.

The stable store rejects malformed/nonregular normal records and preserves evidence before explicit recovery. Projection distinguishes retained merge from parked reapply, and empty structural report is omitted.


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

`SyncSideRecord.retainedTreeDigests` maps paths to fingerprints of operation-created worktree bytes and full index stages. Each value contains fixed-width SHA-256 digests or explicit absent/unreadable sentinels; the model declares no dictionary-cardinality or total-journal-byte cap. Its empty default keeps older journals readable but supplies no positive attribution for a dirty crash-window tree. The field is recovery evidence, not owner intent or authority to overwrite unknown content. A restored parked side can still carry a live stash until terminal completion; wipState alone does not mean its stash was dropped.

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
frozen and `extra="forbid"`, these fields are part of the durable journal schema, so unsupported extra fields are refused rather than silently misread; the retained-fingerprint field defaults empty for older journals.


**MIK-R24 journals a crossing sync's report path, and only for a crossing sync.**
`SyncSideRecord.crossingReport: str = ""` (at most 4,096 characters) holds the path of the crossing report
that `worktrees/knowledge_crossing.write_crossing_report` wrote into the worktree group's `reports/`. The
resolution payload names that report and summarises it. The wrap serializer `_omit_empty_crossing_report`
drops the key when it is empty. Architect ruling N2 (2026-09-29) historically kept the
crossingReport extension out of ordinary journals; that omission is not a present-tense promise
of the exact pre-MIK-R24 schema. The current serializer does not omit `retainedTreeDigests`,
which defaults to `{}` when an older journal lacks it. These defaults describe old-journal read
tolerance; they do not establish executed forward compatibility with an older runtime.

## Evidence

### Docs References

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- The driver treats this store as the sole current generation and routes recovery from its strict outcomes. [11]

- Recovery archives damaged entries, writes quarantine, or reconstructs cancellation from refs. [12]

- Empty crossingReport is omitted under the historical N2 rule; current retainedTreeDigests remains serialized, and empty defaults admit old-journal reads without claiming old-runtime forward compatibility. [13]
- retainedTreeDigests defaults empty; per-value worktree/index hashes have fixed-width digest or absent/unreadable representations, with no declared dictionary-cardinality or journal-byte cap. [14]

- Current strict side/operation records. [4]

- Optional report serialization. [5]

- Retained phase/parked candidate projection. [6]

- Specific old-key adapter and current file resolution. [7]

### Cross-Repo References

No additional configured cross-repository contract is asserted.
