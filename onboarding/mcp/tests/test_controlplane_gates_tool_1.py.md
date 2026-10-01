# mcp/tests/test_controlplane_gates_tool_1.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Gate decision attribution and lifecycle admission tests.

## Code Commentary

### Logic

The public tool records deciding actor and surface, refuses owner self-approval and missing required reviewer verdicts, and expires an older open lifecycle gate. Default lifecycle waiting returns the developer decision and note; a mismatched explicit lifecycle refuses before creating a gate.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Refused decisions leave the durable gate open. Tests use injected stores and timing rather than creating real user approvals.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Create then decide records attribution. [1]
- Orchestration decision rejects owner self approval. [2]
- Orchestration decision requires verdict when policy requires it. [3]
- Create expires previous open lifecycle gate. [4]
- Lifecycle gate default returns after developer decision. [5]
- Lifecycle gate rejects explicit lifecycle mismatch. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
