# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

This file owns the only durable vacancy transitions for atomic-series activation. It separates
strict explicit cancellation release from terminal cleanup release so neither call path can clear a
different selected master.

## Code Commentary

### Logic

`release_atomic_series_selection` derives the exact source-pair path, reads beneath the selector
store lock, rejects unreadable or absent authority, proves selected master plus canonical contract
path, and replaces a non-vacant record with a revision-incremented vacant record. Replaying an
already-vacant exact record is idempotent.

`release_terminal_atomic_series_selection_if_exact` uses the same identity proof but deliberately
preserves unreadable, absent, or different selection state. `_release_record` retains the last
selected master/contract in the durable vacant record so later exact cancellation replay and audit
do not require a surviving task contract.

### Conventions

All writes use the selector owner and per-path exclusive access declared by the activation module.
Release time defaults to a second-granularity UTC timestamp and may be injected by forcing tests.

### Invariants And Boundaries

- Explicit cancellation must prove an existing exact owner or fail closed.
- Terminal cleanup never clears another selected master.
- Vacancy is a durable selector transition, not task completion or queue mutation.
- Release carries no commit or lifecycle evidence.

### Todos

Exact release claims and citations are reconciled to the frozen source; verification remains empty
while the file is uncommitted.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The selector authority supplies exact pair, master, observation, and locked-store identity. | `atomic_series_source_pair`; `observe_atomic_series`; `require_selected_atomic_series`; `require_atomic_series_cancellation_owner` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:105-127; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:252-273; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:276-295 |
| The terminal bridge translates exact, absent, unreadable, and different-selection outcomes. | `with_terminal_atomic_series_release` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py:17-65 |
| Tests prove durable vacancy and refusal to clear another selected master. | `AtomicSeriesActivationTests` | mcp/tests/test_atomic_series_activation.py:110-362 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of exact cancellation/terminal vacancy;
  verification awaits the real code commit.

- 2026-08-26T06:05+02:00 — Moved with exact release ownership into
  `worktrees/activation/`; no forwarding or compatibility module remains.

- 2026-08-26T02:55+02:00 — Drafted exact-release ownership for the pre-Dagger frozen partition;
  final ranges and verification remain open.
