# mcp/src/agents_remember/worktrees/sync_transaction_state.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Strict enclosure-root durable state for one resumable sync generation.

## Code Commentary

### Logic

Side records pin repositories/worktrees/branches, source/pre-sync/base facts, authority refs, phase progress, file conflicts, structural report and parked stash/path facts. Operation records bind generation and original bases; quarantine preserves damaged evidence without rollback authority.

_retain_nonempty_knowledge_keys preserves opaque nonempty legacy conflicts/decisions to block continuation, with cancel available; only empty values are dropped. because a sync already in flight at retirement must resume/cancel. No current row diagnosis/decision is stored; other extras remain forbidden.

The stable store rejects malformed/nonregular normal records and preserves evidence before explicit recovery. Projection distinguishes retained merge from parked reapply, and empty structural report is omitted.


`SyncOperationRecord` records one generation, canonical contract/task/kind, original bases, phase,
memory policy, both sides, and timestamps. `SyncQuarantineRecord` is terminal proof that corrupt
evidence was archived without rollback authority. The store path is
`reports/sync-operation.json` (`SYNC_OPERATION_RECORD_NAME`); the pre-move
`.lifecycle/sync-operation.json` survives only as `legacy_sync_operation_path` read tolerance, and
after canonical publication the writer attempts to retire the legacy copy. Authority refs derive from a hash of the contract path.

`SyncOperationStore` strictly lstat/opens without following nonregular entries, parses only operation
or quarantine records, writes atomically, preserves raw malformed bytes, and can atomically archive
opaque directory/symlink/other entries with bounded metadata. `observe_sync_operation` projects
malformed, quarantined, identity-mismatched, conflict, cancelling, terminal, or resumable state with
contract-addressed next/cancel arguments and without parsing task truth.

`SyncSideRecord.retainedTreeDigests` maps paths to fingerprints of operation-created worktree bytes and full index stages. Each value contains fixed-width SHA-256 digests or explicit absent/unreadable sentinels; the model declares no dictionary-cardinality or total-journal-byte cap. Its empty default keeps older journals readable but supplies no positive attribution for a dirty crash-window tree. The field is recovery evidence, not owner intent or authority to overwrite unknown content. A restored parked side can still carry a live stash until terminal completion; wipState alone does not mean its stash was dropped.

### Conventions

Models are frozen and reject extra fields. The store publishes one canonical record atomically;
that local publication does not establish whole-call repository serialization. Observation is total and read-only, while archival happens only in
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


**`crossingReport` carries a structural memory-merge diagnostic report, not only a converting crossing.**
`SyncSideRecord.crossingReport: str = ""` (at most 4,096 characters) names the report written by
`worktrees/knowledge_crossing.write_crossing_report` into the worktree group's `reports/`. The
producer writes a report for conflict versions, converted sides or nonzero reference-alignment
diagnostics (renumbered references, kept evidence lines or skipped cards), including all-converted
merges. The resolution payload names and summarises it; a nonempty `converted` report field selects
crossing wording, otherwise it describes a structural knowledge merge. The wrap serializer
`_omit_empty_optional_state` omits an empty `crossingReport` and empty retired database keys,
but preserves nonempty values. Architect ruling N2 (2026-09-29) historically kept the extension
out of ordinary journals; it is not a current crossing-only restriction or an exact pre-MIK-R24
schema promise. `retainedTreeDigests` remains serialized and defaults to `{}` for older journals.
These defaults describe old-journal read tolerance, not executed compatibility with an older runtime.

## Evidence

### Docs References

No external Domain Documentation entries are configured. Source and test assertions are distinguished from execution and acceptance evidence.

### Repo-Internal References

- The driver treats this store as the sole current generation and routes recovery from its strict outcomes. [11]

- Recovery archives damaged entries, writes quarantine, or reconstructs cancellation from refs. [12]

- A nonempty crossingReport may name crossing or all-converted structural diagnostics; the serializer omits the empty value. N2 is historical; current retainedTreeDigests remains serialized, and old-journal defaults do not prove old-runtime forward compatibility. [13]
- retainedTreeDigests defaults empty; per-value worktree/index hashes have fixed-width digest or absent/unreadable representations, with no declared dictionary-cardinality or journal-byte cap. [14]

- Current strict side/operation records. [4]

- Optional report serialization. [5]

- Retained phase/parked candidate projection. [6]

- Specific old-key adapter and current file resolution. [7]

### Cross-Repo References

No additional configured cross-repository contract is asserted.
