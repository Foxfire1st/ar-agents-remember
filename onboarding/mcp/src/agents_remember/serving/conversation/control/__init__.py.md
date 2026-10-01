# mcp/src/agents_remember/serving/conversation/control/__init__.py

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

Marks the package that owns the implemented structured exact-session control surface (interrupt,
source-aware queue/withdrawal recovery, typed attachments, read-only policy, and evidence-bound
telemetry) landed by 260718-CHATS-L3.

## Code Commentary

### Logic

Contains only the package docstring; the sibling `api.py` owns the seventeen registered control
routes and each capability lives in its own focused module.

### Conventions

Keep the marker behavior-free; no control work executes at import time. The landed submission
authority remains the mutation owner — the control modules compose it, never a second queue.

### Invariants And Boundaries

- The package marker must not execute control work at import time.
- This package is not a third conversation read port or a second operation queue.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured.

No configured domain documentation was available.

### Repo-Internal References

The sibling API module owns the registered control routes; the package overview governs the slice.

- The sibling `api.py` owns the control surface's `APIRouter` instance. [1]
- That router uses the `/api/terminal/{ar_session_id}` prefix and registers exactly seventeen decorated routes, from `conversation_interrupt` through `conversation_telemetry`. [2]
- The governing route-local overview for the implemented control slice. [3]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
