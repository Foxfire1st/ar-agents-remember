# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

This file is the selecting transaction that connects atomic-series activation to resumable source
sync. It prevents start, attach, or dispatch from exposing an atomic master until the selected
contract records the exact current code/external-memory source pair.

## Code Commentary

### Logic

`activate_atomic_series_contract` rejects invalid sync inputs before fetch or selector mutation,
refreshes remote-tracking evidence outside repository integration authority, re-reads the exact
contract under authority, and delegates reconciliation. A changed contract returns a
contract-addressed retry rather than using stale arguments.

For a new operation, `_sync_selected_atomic_series_under_authority` publishes `reconciling`; a
continue or cancel requires the exact selected/last-released contract. It delegates the journaled
sync while preserving response evidence. Successful cancellation durably releases selection. Any
incomplete, failed, moved-again, or memory-skipped pass remains reconciling with executable
`worktree_sync` guidance. Only when reloaded contract bases equal current admitted source tips does
the selector advance to `active`.

Admission refusals retain the exact contract path and any explicit `memory_sync_choice` and
`resolution_action` in executable `worktree_sync` retry arguments. A successful sync pass whose
source pair moved again still returns blocked implementation admission. These are current source
rules; the deleted transition suite supplies no current execution evidence.

cit:([`_admission_refusal`], mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:204-234)
cit:([`_sync_selected_atomic_series_under_authority`], mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:139-201)

### Conventions

Expected store, contract, filesystem, and validation failures are translated once at this boundary
into `WorktreeCommandResult`. Fetch is evidence only; local tips are pinned after authority is held.

### Invariants And Boundaries

- Selector transition and source sync share repository integration authority.
- `reconciling` is fail-closed implementation admission, not a transient success alias.
- `skip-memory` cannot activate an external-memory source pair that is still incomplete.
- Dry-run does not publish activation.
- Continue/cancel cannot address another selected master.

### Todos

Exact result states and citations are reconciled to the frozen source; verification remains empty
until the real code commit exists.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selector publication and exact continuation/cancellation ownership live in the activation authority. | `publish_atomic_series_selection`; `require_selected_atomic_series`; `require_atomic_series_cancellation_owner` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:190-249; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:252-273; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:276-295 |
| The sync driver admits, resumes, continues, cancels, or recovers one exact journal generation. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of reconciling, selected sync,
  continue/cancel, and active exposure states.

- 2026-08-26T06:05+02:00 — Moved the admission transaction into `worktrees/activation/` with its
  behavior and history intact; import rewrites are mechanical consumers of the new canonical path.

- 2026-08-26T02:55+02:00 — Drafted selecting-transaction onboarding against the pre-Dagger
  candidate; final behavior inventory and verification remain open.
