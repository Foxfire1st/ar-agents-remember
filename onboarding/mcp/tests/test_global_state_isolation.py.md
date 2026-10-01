# mcp/tests/test_global_state_isolation.py

## Governing Overview

[overview](overview.md)

## Purpose

The suite identifies the test that leaks an explicitly-owned mutable global.
The expected owner is the kernel checkout-execution declaration, whose normal pytest baseline is
`{"mode": "test"}`; a leaked dashboard/MCP role is restored to that explicit mode before failure.

## Code Commentary

### Logic

Module-level surface:

- `GlobalStateLeakDetectionTests` (class, lines 14-38)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `GlobalStateLeakDetectionTests` (lines 14-38). [1]

## 260824-PDLS Route Impact

The production owner moved from `mcp/tests/_global_state.py` to
`agents_remember_test_support.testing.global_state`. This suite still expects root certifying bootstrap to have
declared the normal `test` mode, deliberately leaks dashboard mode, and proves restoration happens
before failure. It is therefore a Dagger-suite contract, not a valid standalone raw-host test.
