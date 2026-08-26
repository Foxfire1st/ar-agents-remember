# mcp/tests/test_atomic_series_activation_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_atomic_series_activation_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

This focused suite forces the selecting transaction boundary between atomic-series activation and
resumable sync. It proves ordering and admission semantics that cannot be inferred from selector or
sync tests alone.

## Code Commentary

### Logic

The suite builds typed series contracts and replaces only the adjacent selector/sync/source facts
needed for each transition. It proves invalid input refuses before selection or sync; a
moved-again pass stays reconciling; explicit and no-authority cancellation replay release the exact
selection; only an exact current source pair publishes active; skipping external memory keeps
admission reconciling with merge-memory guidance; a contract race returns the same
contract-addressed retry; store failures translate once at the boundary; and dry-run never publishes
activation.

### Conventions

These are focused orchestration tests, so mocked collaborators return real `WorktreeCommandResult`
and observation-shaped facts while assertions pin call order/arguments. Git/store semantics belong
to the deeper activation and sync suites.

### Invariants And Boundaries

- Input validation precedes fetch, selector, refs, journal, and Git mutation.
- `synced` is insufficient for activation when current external-memory pair proof still fails.
- Cancellation must release the exact selection, including terminal no-authority replay.
- Dry-run is selector-mutation free.
- No Dagger or whole-master acceptance is claimed here.

### Todos

Final states and cases are reconciled to the frozen source; verification remains empty until the
real code commit exists.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selecting transaction under test binds reconciling, sync, cancellation release, and active publication. | `activate_atomic_series_contract`; `reconcile_selected_series_under_authority` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:41-79; mcp/src/agents_remember/worktrees/activation/atomic_series_activation_transaction.py:82-100 |
| Exact selector continuation/cancellation identity comes from the activation authority. | `require_selected_atomic_series`; `require_atomic_series_cancellation_owner` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:252-273; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:276-295 |
| The delegated sync driver owns the retained/recovered generation behind these transition results. | `sync_contract_under_authority` | mcp/src/agents_remember/worktrees/sync_transaction.py:72-100 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of sync-before-exposure,
  pause/reselection, retained conflict, cancellation, and cleanup release forcing.

- 2026-08-26T02:55+02:00 — Drafted selecting-transaction forcing coverage; final test inventory,
  citations, and verification remain post-Dagger work.