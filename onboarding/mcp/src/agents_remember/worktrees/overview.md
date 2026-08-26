# mcp/src/agents_remember/worktrees

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/worktrees` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-26T08:55+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## What This Area Is

This route owns the durable worktree-enclosure and protected-source coordination primitives beneath
the public lifecycle modules. The current architecture adds two related but distinct owners:
source-pair-scoped atomic-series activation decides which live master may expose implementation
work, while a contract-addressed sync transaction reconciles code and external-memory sources
without depending on a readable task document for its in-flight journal.

## Hot Path Summary

`activation/atomic_series_activation.py` is the single disposable selection authority for one
normalized source pair; its release and terminal siblings own exact vacancy. The selecting
transaction publishes `reconciling`, runs exact source sync, and publishes `active` only after both
required bases are current. Root-level `sync_transaction.py` drives the journaled state machine;
focused state, authority, Git, recovery, result, and source-refresh modules own their respective
proof and response boundaries.

## What Belongs Here

| Path | Role |
| --- | --- |
| `activation/` | source-pair selector, selecting transaction, exact release, and terminal bridge |
| `sync_transaction*.py` | resumable source synchronization, journal, Git proof, authority refs, and recovery |
| `worktree_contract.py` and enclosure helpers | canonical worktree/enclosure authority used by child lifecycle routes |
| `modules/` | public lifecycle command composition |
| `queue/` | disposable waiting-candidate scheduling projection |
| `integration/` | protected branch integration and lifecycle journals |

## What Does Not Belong Here

| Nearby Thing | Belongs Instead In |
| --- | --- |
| task-document authoring or publication permission | `tasks/` and `application/task_docs/` |
| closeout claim, commit, certification, integration, or recovery evidence | `worktrees/integration/lifecycle/` and closeout-door owners |
| public MCP schema/transport translation | `mcp/registration/` and `mcp/tools/` |

## Structures Found Here

- `AtomicSeriesSourcePair` and one fingerprint-addressed activation record per protected pair.
- `vacant`, `reconciling`, and `active` selector states; `unreadable` is an observation, not a
  selectable state.
- One stable `.lifecycle/sync-operation.json` record per worktree enclosure plus pinned
  `refs/agents-remember/sync/...` authority on participating repositories.
- Separate code and memory side records with admitted base/source/pre-sync heads, plan, retained
  conflict set, and exact result head.

## Operating Model

1. A selecting public start/attach/dispatch or sync operation identifies one canonical series
   contract and derives its normalized code/memory source pair.
2. Selection atomically replaces the pair's prior snapshot with this master in `reconciling`.
   Other live series remain intact and merely project as paused.
3. The sync transaction pins exact base, pre-sync, and source commits, journals admission below the
   enclosure root, and advances code then memory under repository integration authority.
4. A genuine merge conflict is retained in the operation-owned worktree. The integration lock is
   released while an agent resolves and stages it; a later exact contract-addressed `continue`
   validates and commits it, while `cancel` restores all provably operation-owned heads.
5. Finalization writes the new base pair and terminal journal before removing temporary worktrees
   and authority refs. If the official source moves again, the completed generation reports that
   fact and a new generation may be admitted.
6. Atomic implementation becomes visible only after exact current bases are proven and selection
   advances to `active`.
7. Terminal cleanup attempts to vacate only the exact selected terminal contract. A missing,
   unreadable, vacant, or different selection is preserved and cannot be cleared by the old master.

## Main Flows

### Select And Admit An Atomic Master

1. Refresh remote-tracking evidence outside the integration lock.
2. Re-read the canonical contract under source-pair integration authority.
3. Publish exact selection as `reconciling`.
4. Complete or resume the source-pair sync transaction.
5. Publish `active` only when contract bases equal current admitted source tips.

### Resolve Or Cancel Retained Sync Conflict

1. Read the stable enclosure-root journal and pinned Git authority.
2. Resolve and stage the retained merge in the reported code or memory worktree.
3. Call the same contract-addressed sync with `resolution_action="continue"`, or call it with
   `resolution_action="cancel"` to restore the pinned pre-sync pair.
4. Fail closed for missing/malformed identity; explicit cancellation may recover from complete
   pinned refs and preserves incomplete authority for manual repair.

## Load-Bearing Files

| File | Role | Why It Matters | Onboarding |
| --- | --- | --- | --- |
| `activation/atomic_series_activation.py` | selector store | single source-pair activation authority and strict observation | covered |
| `activation/atomic_series_activation_release.py` | selector transition | exact cancellation and terminal vacancy | covered |
| `activation/atomic_series_activation_transaction.py` | admission state machine | binds selection to exact sync-before-exposure | covered |
| `activation/atomic_series_activation_terminal.py` | terminal bridge | prevents paused cleanup from clearing a newer selection | covered |
| `sync_source_refresh.py` | pre-lock evidence | shared bounded upstream refresh without local authority | covered |
| `sync_transaction.py` | transaction driver | public start/resume/continue/cancel routing | covered |
| `sync_transaction_state.py` | stable journal | state survives task/contract readability failures | covered |
| `sync_transaction_authority.py` | identity/admission | pins sources and validates official code-memory ledger pairing | covered |
| `sync_transaction_git.py` | Git proof | retains conflicts and proves exact operation-created history | covered |
| `sync_transaction_recovery.py` | finalization/recovery | terminal publication, rollback, and malformed/missing journal escape | covered |
| `sync_transaction_results.py` | public evidence | consistent previews, conflict guidance, and terminal replay | covered |

## Local Invariants And Traps

- Task authoring is upstream and wholly unlocked; neither activation nor queue state may veto it.
- The activation snapshot is disposable selection, not a lifecycle journal or retirement record.
- Multiple live series contracts for one source pair are normal. Selection change auto-pauses old
  work without deleting or terminalizing it.
- Sync owns lifecycle evidence in the stable enclosure-root journal and Git refs; the queue owns
  none of it.
- Normal readers never infer selection or sync state from legacy files, task text, queue rows, or
  ambient Git. Missing/corrupt authority fails closed and is repaired only by explicit bounded
  selection/cancellation paths.
- Cleanup may release only an exact selected terminal contract and must do so before deleting the
  canonical contract pointer needed to prove identity.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The activation record is a strict source-pair fingerprinted snapshot with explicit selection states. | `AtomicSeriesSourceRef`; `AtomicSeriesSourcePair`; `AtomicSeriesActivationRecord`; `AtomicSeriesActivationArchiveEvidence` | mcp/src/agents_remember/models/structural/atomic_series_activation.py:16-30; mcp/src/agents_remember/models/structural/atomic_series_activation.py:33-39; mcp/src/agents_remember/models/structural/atomic_series_activation.py:42-54; mcp/src/agents_remember/models/structural/atomic_series_activation.py:57-72 |
| Selection observation treats absence as vacant and validates the exact canonical series/source pair rather than inferring from task or queue state. | `atomic_series_source_pair`; `observe_atomic_series` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:105-127; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187 |
| Selecting admission publishes reconciling, delegates exact sync, and publishes active only after the current source pair is proven. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:41-79; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:82-100 |
| The stable journal lives at `.lifecycle/sync-operation.json` and projects recovery without reading task text. | `SyncOperationStore`; `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:145-295; mcp/src/agents_remember/worktrees/sync_transaction_state.py:298-314 |
| The sync driver retains conflicts for continuation and exposes explicit cancellation. | `sync_contract_under_authority`; `_continue_resolution` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100; mcp/src/agents_remember/worktrees/sync_transaction.py:424-450 |
| Cancellation restores only operation-owned heads; malformed or missing journals recover only through explicit pinned-ref proof. | `cancel_sync`; `recover_unreadable_journal`; `recover_missing_journal` | mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:156-181; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:184-254; mcp/src/agents_remember/worktrees/sync_transaction_recovery.py:257-274 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## File-Level Onboarding Map

| Source File | Onboarding File | Status | Reason |
| --- | --- | --- | --- |
| `sync_source_refresh.py` | [`sync_source_refresh.py.md`](sync_source_refresh.py.md) | covered | shared pre-lock fetch evidence |
| `sync_transaction.py` | [`sync_transaction.py.md`](sync_transaction.py.md) | covered | transaction driver |
| `sync_transaction_authority.py` | [`sync_transaction_authority.py.md`](sync_transaction_authority.py.md) | covered | source/contract authority |
| `sync_transaction_git.py` | [`sync_transaction_git.py.md`](sync_transaction_git.py.md) | covered | exact Git mutation/proof |
| `sync_transaction_recovery.py` | [`sync_transaction_recovery.py.md`](sync_transaction_recovery.py.md) | covered | finalization and recovery |
| `sync_transaction_results.py` | [`sync_transaction_results.py.md`](sync_transaction_results.py.md) | covered | result and guidance construction |
| `sync_transaction_state.py` | [`sync_transaction_state.py.md`](sync_transaction_state.py.md) | covered | stable journal model/store |

## Child Overviews

| Route | Why It Has Its Own Overview |
| --- | --- |
| [`activation/overview.md`](activation/overview.md) | source-pair selector, reconciliation-bound admission, and exact vacancy |
| [`integration/overview.md`](integration/overview.md) | protected-source integration and lifecycle journals |
| [`modules/overview.md`](modules/overview.md) | public worktree command composition |
| [`queue/overview.md`](queue/overview.md) | disposable closeout scheduling projection |

## How To Use This Area

When changing worktree coordination:

1. Read this overview for selector/sync ownership.
2. Read the nearest child overview when editing `integration`, `modules`, or `queue`.
3. Read the exact file-level onboarding and the focused tests.
4. Keep task truth, disposable scheduling, selection, and lifecycle evidence in their separate
   authority planes.

## Needs Verification

- [CLOSEOUT] Verification hashes and entity fingerprints require the real code commit; exact names,
  states, citations, and changed-file membership are reconciled to the frozen candidate.
- [CURATOR] Generated route indexes are refreshed from explicit frozen code/onboarding roots in
  this final pass; they are never hand-edited.

## Update History

- 2026-08-26T08:55+02:00 — Promoted the activation and sync units from provisional to frozen
  covered status after pass 13.

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of 5 activation package units, 7 root
  sync units, and their queue/module/integration boundaries; commit-derived stamps remain
  closeout-owned.

- 2026-08-26T06:25+02:00 — Reconciled current coverage after the consolidation: five activation
  package units and seven root sync units have strict provisional sidecars; final citations and
  verification remain post-Dagger owned.

- 2026-08-26T06:05+02:00 — Reconciled the structural-limit move: activation is now one focused
  child route with five strict sidecars, while resumable sync remains at the worktrees root. No
  compatibility readers or old-path cards remain.

- 2026-08-26T02:55+02:00 — Created for the direct IAS source-pair coordination repair. Recorded
  approved activation, resumable-sync, task-authoring, queue-ownership, cleanup, and no-fallback
  boundaries against the moving candidate; verification remains frozen-candidate owned.