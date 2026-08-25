# mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-25T08:16+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Pure exact-state classifier for an ordinary closeout ledger mutation intent.

## Code Commentary

### Logic

The public surface is `CloseoutLedgerRecoveryClassification`, `CloseoutLedgerRecoveryDecision`, `classify_closeout_ledger_recovery`. The classifier derives ledger recovery only from the journaled mutation intent plus exact repository state. Ambiguity stays attached to the same generation and yields a typed recovery decision; it never fabricates a commit or overwrites accepted input.

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
| The module defines `CloseoutLedgerRecoveryClassification`; `CloseoutLedgerRecoveryDecision`; `classify_closeout_ledger_recovery` as its public seam. | `CloseoutLedgerRecoveryClassification`; `CloseoutLedgerRecoveryDecision`; `classify_closeout_ledger_recovery` | mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py:37-60; mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py:63-74; mcp/src/agents_remember/worktrees/integration/closeout/ledger_recovery.py:90-156 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
