# mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[queue overview](overview.md)

## Purpose

This file is the read-only adapter from source-pair activation authority into disposable closeout
projection source facts. It gives the queue waiting reasons without granting it selector mutation or
lifecycle ownership.

## Code Commentary

### Logic

`project_series_activation` strictly observes the series contract's source-pair snapshot. A valid
observation returns its source fact plus zero or one waiting reason: not selected, paused by another
master, or reconciling. A derivation/read failure becomes a bounded `ProjectionSourceProblem` with
the contract or selector address and an explicit repair through a selecting manager/start/attach
operation. It never chooses a winner itself.

### Conventions

`SeriesActivationProjection` is a frozen local carrier for source fact, waiting tuple, and optional
problem. Repair guidance names the selecting transaction rather than an internal store edit.

### Invariants And Boundaries

- The queue observes activation; it cannot publish, release, or archive it.
- Multiple live series are valid and nonselected ones are waiting, not invalid contracts.
- Malformed authority fails loud as a source problem; no stale row or census-order fallback exists.
- No claim, commit, certification, integration, or terminal evidence is projected here.

### Todos

Repair wording and claims are reconciled to the frozen selector observer; verification metadata
awaits the real code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Selector observation and waiting-reason derivation are owned outside the queue. | `observe_atomic_series`; `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:170-187; mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:298-311 |
| The queue route is a disposable rebuild projection with task truth and lifecycle state outside it. | `## 260821-CLIVE Final Disposable Projection Route` | onboarding/mcp/src/agents_remember/worktrees/queue/overview.md:59-86 |
| Focused tests force source-alias failure into a typed projection problem. | `AtomicSeriesActivationTests` | mcp/tests/test_atomic_series_activation.py:110-362 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Final frozen reconciliation of selector observation and scoped
  invalid-empty projection behavior.

- 2026-08-26T02:55+02:00 — Drafted the activation-observer sidecar; final source freeze and
  verification remain open.