# mcp/src/agents_remember/serving/pi_rpc_submissions.py

## Governing Overview

[overview](overview.md)

## Purpose

The Pi adapter's bounded prompt-correlation ledger.

## Code Commentary

### Logic

Module-level surface:

- `PiSubmissionEvidence` (class, lines 16-25) — What one submitted prompt is known to be, and the entry cursor it was sent after.
- `PiSubmissionLedger` (class, lines 28-64) — Bounded request-id ledger for Pi prompts, from which only a settled row may be evicted.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `PiSubmissionEvidence` (lines 16-25) — What one submitted prompt is known to be, and the entry cursor it was sent after.. [1]
- Defines the class `PiSubmissionLedger` (lines 28-64) — Bounded request-id ledger for Pi prompts, from which only a settled row may be evicted.. [2]
