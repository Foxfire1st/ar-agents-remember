# mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/atomic_series_activation_terminal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

This file bridges a successful terminal series operation to the source-pair selector after lifecycle
locks are gone. It makes cleanup release visible without turning cleanup or the queue into selector
owners.

## Code Commentary

### Logic

`with_terminal_atomic_series_release` is inert for leaves, previews, and failed terminal operations.
For a successful series result it calls the exact terminal release owner, adds activation source
facts, and classifies the outcome as vacant, already vacant, different selection preserved, or
unreadable preserved. An actual release exception converts the otherwise successful result into a
retryable failure before the caller deletes the canonical contract pointer.

### Conventions

The bridge wraps and enriches `WorktreeCommandResult`; it does not write task documents or queue
projections. Classification distinguishes a different selected contract from a missing record.

### Invariants And Boundaries

- Release runs after lifecycle/store locks, before destructive contract deletion.
- A paused terminal series cannot clear the newer selected series.
- Corrupt selector evidence stays preserved for the next exact selecting repair.
- Terminal scheduling state is not inferred from cleanup success alone.

### Todos

Final call sites and citations are reconciled to the frozen source; do not stamp an uncommitted file.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact terminal release preserves absent, unreadable, or different selection and vacates only a matching owner. | `release_terminal_atomic_series_selection_if_exact` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:58-79 |
| Focused tests cover release-before-contract-deletion and paused-series preservation. | `AtomicSeriesActivationTests` | mcp/tests/test_atomic_series_activation.py:110-362 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of terminal exact-release composition;
  newer selections remain protected.

- 2026-08-26T06:05+02:00 — Moved the terminal selector bridge into the focused activation route;
  its exact-release boundary and history are unchanged.

- 2026-08-26T02:55+02:00 — Drafted terminal exact-release bridge onboarding; final source freeze
  and verification remain open.
