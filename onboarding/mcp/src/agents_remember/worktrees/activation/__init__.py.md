# mcp/src/agents_remember/worktrees/activation/__init__.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/activation/__init__.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-26T08:20+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[activation overview](overview.md)

## Purpose

Package marker for the focused atomic-series selection and source-reconciliation authority.

## Code Commentary

### Logic

The module intentionally contains only its package docstring. It establishes the canonical import
home for the selector store, selecting transaction, exact release owner, and terminal bridge; it
does not re-export the old flat paths or introduce a second public API.

### Conventions

Consumers import the focused owner they need. Keep this marker free of compatibility aliases and
side effects.

### Invariants And Boundaries

- Package placement is structural; lifecycle ownership remains in the four focused modules.
- No old-path forwarding module or aggregate state owner is created here.

### Todos

The package boundary is reconciled to the frozen source; verification metadata awaits the real
code commit.

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package docstring names selection and source reconciliation as the route authority. | "Atomic-series selection and source-reconciliation authority." | mcp/src/agents_remember/worktrees/activation/__init__.py:1-1 |
| The route overview maps the four concrete owners. | `## File-Level Onboarding Map` | onboarding/mcp/src/agents_remember/worktrees/activation/overview.md:55-64 |

## Cross-Repo References

No cross-repository source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-26T08:20+02:00 — Reconciled the focused package marker to the frozen route; no
  compatibility export was introduced.

- 2026-08-26T06:05+02:00 — Created with the new focused activation package; no compatibility
  export or behavior is claimed.
