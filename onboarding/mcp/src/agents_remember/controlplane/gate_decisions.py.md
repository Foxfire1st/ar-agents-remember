# mcp/src/agents_remember/controlplane/gate_decisions.py

## Governing Overview

[overview](overview.md)

## Purpose

Shared mutation service for addressed and lifecycle-scoped gate decisions.

## Code Commentary

### Logic

Module-level surface:

- `GateDecisionContext` (class, lines 30-37) — Stores, policy, and clock that make one gate decision atomic in meaning.
- `_target_gate` (function, lines 40-46)
- `_require_undelegated_cli_decision` (function, lines 49-54)
- `_evidence_refs` (function, lines 57-58)
- `_meet_verdict_expectation` (function, lines 61-71)
- `_reclaim_gate_log` (function, lines 74-80) — Reclaim terminal history only in the process that owns gate compaction.
- `record_gate_decision` (function, lines 83-128) — Apply one decision and return the shared raw gate response payload.
- `record_lifecycle_gate_decision` (function, lines 131-156) — Resolve a lifecycle's latest open gate, then apply the shared decision service.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `GateDecisionContext` (lines 30-37) — Stores, policy, and clock that make one gate decision atomic in meaning.. [1]
- Defines the function `_target_gate` (lines 40-46). [2]
- Defines the function `_require_undelegated_cli_decision` (lines 49-54). [3]
- Defines the function `_evidence_refs` (lines 57-58). [4]
- Defines the function `_meet_verdict_expectation` (lines 61-71). [5]
- Defines the function `_reclaim_gate_log` (lines 74-80) — Reclaim terminal history only in the process that owns gate compaction.. [6]
- Defines the function `record_gate_decision` (lines 83-128) — Apply one decision and return the shared raw gate response payload.. [7]
- Defines the function `record_lifecycle_gate_decision` (lines 131-156) — Resolve a lifecycle's latest open gate, then apply the shared decision service.. [8]
