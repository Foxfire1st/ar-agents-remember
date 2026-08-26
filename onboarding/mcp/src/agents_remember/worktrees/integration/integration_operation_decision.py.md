# mcp/src/agents_remember/worktrees/integration/integration_operation_decision.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_operation_decision.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

One read-only live decision observation for an integration generation.

## Code Commentary

### Logic

The public surface is `IntegrationOperationObservation`, `classify_integration_operation`, `require_integration_operation_convergent`, `raise_integration_decision`. Protected-ref and door state are classified from exact live and journal evidence. A moved, missing, unreadable, or contradictory ref is never discarded: the same landing generation must reconcile or complete, with an executable task-addressed handoff for any later repair or revert planning.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `IntegrationOperationObservation`; `classify_integration_operation`; `require_integration_operation_convergent` as its public seam. | `IntegrationOperationObservation`; `classify_integration_operation`; `require_integration_operation_convergent` | mcp/src/agents_remember/worktrees/integration/integration_operation_decision.py:33-42; mcp/src/agents_remember/worktrees/integration/integration_operation_decision.py:45-91; mcp/src/agents_remember/worktrees/integration/integration_operation_decision.py:94-100 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

