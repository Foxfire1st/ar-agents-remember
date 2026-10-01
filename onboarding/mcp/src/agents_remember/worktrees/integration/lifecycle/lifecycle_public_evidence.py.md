# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_public_evidence.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Bound private lifecycle identity before developer-facing serialization.

## Code Commentary

### Logic

The bounded migrated-output payload reports proven code and memory-content commits. It carries no `ledgerCommitProven` field: public recovery describes real Git outputs, while downstream ledger-cache availability supplies no lifecycle proof.

The public surface is `PublicEvidencePair`, `MigratedLifecycleClassification`, `public_lifecycle_evidence_pair`, `public_lifecycle_evidence`, `public_failure_evidence`, `classify_migrated_lifecycle`. This file bounds public refusal evidence and next actions. Missing, unreadable, mismatched, or ambiguous artifacts remain typed decisions with expected/observed facts; they are never downgraded to absence and private operation keys never cross the public boundary.

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

- `MigratedLifecycleClassification` reports proven code and memory output without a ledger-proof field. [1]
- `classify_migrated_lifecycle` classifies the retained migration proof without inventing new outputs. [2]

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `PublicEvidencePair`; `MigratedLifecycleClassification`; `public_lifecycle_evidence_pair` as its public seam. [3]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No additional cross-repository evidence applies.
