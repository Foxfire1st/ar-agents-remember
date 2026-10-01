# mcp/src/agents_remember/models/application_requests.py

## Governing Overview

[overview](overview.md)

## Purpose

Wire request records consumed by application operations.

## Code Commentary

### Logic

Module-level surface:

- `LifecycleGateRequest` (class, lines 42-53) — The flat public lifecycle-gate request before domain record construction.
- `GateDecisionRequest` (class, lines 57-67) — One addressed gate verdict with its transport-owned attribution.
- `OperatorInboxPostRequest` (class, lines 71-86) — The flat inbox post before application-owned routing and record construction.
- `OrchestrationNudgeRequest` (class, lines 90-100) — The flat manager-nudge request before target/subject construction.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `LifecycleGateRequest` (lines 42-53) — The flat public lifecycle-gate request before domain record construction.. [1]
- Defines the class `GateDecisionRequest` (lines 57-67) — One addressed gate verdict with its transport-owned attribution.. [2]
- Defines the class `OperatorInboxPostRequest` (lines 71-86) — The flat inbox post before application-owned routing and record construction.. [3]
- Defines the class `OrchestrationNudgeRequest` (lines 90-100) — The flat manager-nudge request before target/subject construction.. [4]
