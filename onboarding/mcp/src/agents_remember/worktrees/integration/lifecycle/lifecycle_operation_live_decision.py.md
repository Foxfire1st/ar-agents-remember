# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_live_decision.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Bounded live-evidence refusals shared by lifecycle controls.

## Code Commentary

### Logic

Live refusal dispatch retains initial-door, direct-landing, and immutable-Git evidence checks. It no longer invokes a ledger-recovery classifier, so malformed or missing computed cache bytes cannot become a developer-decision refusal.

The public surface is `raise_live_evidence_decision`, `immutable_recovery_refusal`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

#### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

No configured external source applies.

### Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

- `raise_live_evidence_decision` dispatches genuine publication and Git contradictions without inspecting ledger bytes. [1]
- `immutable_recovery_refusal` turns immutable-evidence contradictions into bounded recovery refusals. [2]

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `raise_live_evidence_decision`; `immutable_recovery_refusal` as its public seam. [3]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.
