# mcp/src/agents_remember/serving/harness_submission_ledger.py

## Governing Overview

[overview](overview.md)

## Purpose

What one submission authority retains about its operations, and what it can say about them.

## Code Commentary

### Logic

Module-level surface:

- `OperationRecord` (class, lines 58-252) — One ordinary operation's whole life: its state, its evidence, and what it answers with.
- `SubmissionLedger` (class, lines 255-437) — The bounded, epoch-stamped record store one submission authority admits into and reads from.
- `ref_key` (function, lines 440-441)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `OperationRecord` (lines 58-252) — One ordinary operation's whole life: its state, its evidence, and what it answers with.. [1]
- Defines the class `SubmissionLedger` (lines 255-437) — The bounded, epoch-stamped record store one submission authority admits into and reads from.. [2]
- Defines the function `ref_key` (lines 440-441). [3]
