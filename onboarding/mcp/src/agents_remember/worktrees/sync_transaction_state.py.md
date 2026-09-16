# mcp/src/agents_remember/worktrees/sync_transaction_state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/sync_transaction_state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash |  `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`|
| lastVerifiedCommitDate |  2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

This file defines and stores the strict stable state for one resumable worktree-sync generation.
The journal lives below the enclosure root so status, continuation, cancellation, and damage
recovery do not depend on a readable task document or queue projection.

## Code Commentary

### Logic

`SyncSideRecord` binds each participating side to exact repositories/worktrees/branches, admitted
source/pre-sync/base commits, three authority refs, plan, progress, result head, conflicts, and the
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

### Todos

Final nonregular handling and public model fields are reconciled to the frozen source;
commit-derived verification remains closeout-owned.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The driver treats this store as the sole current generation and routes recovery from its strict outcomes. | `_read_sync_record`; `_route_sync_record` | mcp/src/agents_remember/worktrees/sync_transaction.py:113-151; mcp/src/agents_remember/worktrees/sync_transaction.py:154-174 |
| Recovery archives damaged entries, writes quarantine, or reconstructs cancellation from refs. | `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:159-190; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:193-263; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:266-283 |
| Public status embeds this journal projection without moving its authority into task/queue state. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:65-152 |
| The strict side record now journals the parked candidate's state, stash identity, bounded path sample, and true path count. | `SyncSideRecord`; `SyncWipState` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:38-38; mcp/src/agents_remember/worktrees/sync_transaction_state.py:41-67 |
| The active projection distinguishes a parked-candidate reapply from a retained merge. | `_active_sync_projection` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:433-509 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the journal move to
  `reports/sync-operation.json` with legacy read tolerance is the frozen change and the card records
  it. Re-checked its ranges: they hold. No wording changed. Verification metadata remains
  closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/sync_transaction_state.py` changed since the recorded
  verification commit. Re-read the card against the frozen on-disk source and re-checked its claims
  and cited ranges: nothing this card asserts is falsified by the change, so no wording changed.
  Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (reopened-claim judgement): the checker reopened
  the `cancel_sync` claim because that construct changed after verification. Re-read the claim
  against `sync_transaction_recovery.py`: `cancel_sync` is at `:159`, `recover_unreadable_journal`
  at `:193` and `recover_missing_journal` at `:266`, and the regenerated ranges cover each; the
  claim that recovery archives, quarantines or reconstructs cancellation still holds. Retained;
  verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved the sync
  journal out of the terminal-evidence root. Corrected the store-path claim to
  `reports/sync-operation.json` with `.lifecycle/sync-operation.json` retained only as
  `legacy_sync_operation_path` read tolerance. Every other cited range was re-read and still holds.
  Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 2 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — Parked-candidate journal fields: recorded `SyncWipState` and the four `SyncSideRecord` fields as durable journal schema, and the active projection's parked-reapply summary. Re-derived the journal/recovery anchors against the current working tree. Verification remains closeout-owned.

- 2026-08-26T08:30+02:00 — Rebounded the public status citation to the frozen status projection
  implementation after final structural consolidation.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of stable journal storage,
  nonregular/raw archive evidence, quarantine, and public phase projection.

- 2026-08-26T02:55+02:00 — Drafted stable journal/store/status onboarding against the pre-Dagger
  candidate; final fields, citations, and verification remain open.