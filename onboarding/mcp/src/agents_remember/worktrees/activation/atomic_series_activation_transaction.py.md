# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py

## Governing Overview

[activation overview](overview.md)

## Purpose

This file is the selecting transaction that connects atomic-series activation to resumable source
sync. It prevents start, attach, or dispatch from exposing an atomic master until that master's own
series contract records the exact current code/external-memory source pair. Selection is per contract,
so two masters sharing one protected source pair advance independently: this transaction moves only
the addressed contract's own `reconciling -> active` transition.

## Code Commentary

### Logic

`activate_atomic_series_contract` rejects invalid sync inputs before fetch or selector mutation,
refreshes remote-tracking evidence outside repository integration authority, re-reads the exact
contract under authority, and delegates reconciliation. A changed contract returns a
contract-addressed retry rather than using stale arguments.

For a new operation, `_sync_selected_atomic_series_under_authority` publishes `reconciling`; a
continue or cancel requires this contract's exact selected/last-released record. It delegates the
journaled sync while preserving response evidence. Successful cancellation durably releases this
contract's selection. Any incomplete, failed, moved-again, or memory-skipped pass remains reconciling
with executable `worktree_sync` guidance. Only when reloaded contract bases equal current admitted
source tips does the selector advance this contract to `active`.

`_reconciling_result` reports that state as this operation's own outcome. It attaches the activation
observation, and when the pass itself returned `synced` or `already-current` it rewrites the state to
`atomic-series-reconciling` rather than presenting a finished pass beside a mid-flight record.
`_mid_flight_summary` leads with the selected master's task-document ref and contract path, when the
record was published, its revision, the fact that a source reconciliation did not complete, and both
exits — `worktree_sync(contract_path=..., dry_run=false)` and the `resolution_action='cancel'` form —
with the refused pass's own message kept at the end.

Admission refusals retain the exact contract path and any explicit `memory_sync_choice` and
`resolution_action` in executable `worktree_sync` retry arguments. A successful sync pass whose
source pair moved again still returns blocked implementation admission. These are current source
rules; the deleted transition suite supplies no current execution evidence.

CCR-R25 routes expected activation failures through `_AdmissionRefusalRequest` and the shared
`atomic_series_admission_projection`. The refusal path reuses an error's retained observation when
available, otherwise performs a bounded read-only observation, then emits the exact contract
fingerprint, activation facts, retry precondition, and status action. There is no
"waiting: named blocker owns the source-pair selection" branch and no foreign-blocker summary: every
refusal this path describes is corrective action on the addressed contract, and selection is per
contract, so another master is never reported as this contract's blocker. This changes the public
explanation only; selector publication, source sync, continuation/cancellation ownership, and the
reconciling-to-active transition remain in the same transaction.

cit:([`_admission_refusal`], mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:229-277)
cit:([`_sync_selected_atomic_series_under_authority`], mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:164-226)

### Conventions

Expected store, contract, filesystem, and validation failures are translated once at this boundary
into `WorktreeCommandResult`. Fetch is evidence only; local tips are pinned after authority is held.

### Invariants And Boundaries

- Selector transition and source sync share repository integration authority.
- `reconciling` is fail-closed implementation admission, not a transient success alias.
- A pass that succeeds beside a mid-flight selection is never reported as this call's own success:
  the state is `atomic-series-reconciling`, and the summary leads with the stuck master, its
  contract path, its publication time, its revision, and both exits.
- `skip-memory` cannot activate an external-memory source pair that is still incomplete.
- Dry-run does not publish activation.
- Continue/cancel address only this contract's own selected record; selecting one master never pauses
  or replaces another contract's independent selection.
- Admission output preserves observed evidence and does not infer a live process or repair selector
  bytes while translating a refusal; a foreign master is never named as blocker or retry
  precondition.

### Todos

Exact result states and citations are reconciled to the frozen source; verification remains empty
until the real code commit exists.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Selector publication and this contract's exact continuation/cancellation ownership live in the activation authority. [1]
- The transaction translates expected activation errors through the shared structured admission projection. [2]
- The selecting entry point refuses invalid inputs first, then re-reads the exact contract before reconciliation. [3]
- The internal sync driver publishes reconciling, proves continue/cancel ownership, and advances only this contract to active. [4]
- A mid-flight selection reports the stuck contract and both exits, and a succeeding pass beside it never reports its own success state. [5]
- The sync driver admits, resumes, continues, cancels, or recovers one exact journal generation. [6]

### Cross-Repo References

No cross-repository source is configured for this memory root.

## CCR-L42 current candidate

Atomic-series admission refusals now preserve the full source detail directly in retry arguments and public summary/detail; the former bounded-detail truncation wrapper is gone, while activation ownership and retry routing remain unchanged.
