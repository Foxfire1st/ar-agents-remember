# mcp/tests/test_harness_control_claude_stream_1.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Claude structured launch, discovery, prompt and interaction contracts.

## Code Commentary

### Logic

Token-free bootstrap and list_models discover capabilities without query cost. Launch preserves arguments/environment and requires structured init; absent capabilities or model mismatch close loudly. Prompt acceptance, activity, settling and terminal completion are distinct. Permission and user-question responses use the exact durable interaction identity.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A fixture version is evidence, not authority to invent unsupported flags. Authentication data must not leak into handshake evidence and ordinary launch keeps its supplied MCP configuration.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Discover uses only token free bootstrap and list models. [1]
- Launch preserves arguments environment and requires structured init. [2]
- Missing protocol capability fails loudly. [3]
- Expected launch model mismatch closes and propagates as failure. [4]
- Correlated acceptance retry activity and terminal result are distinct. [5]
- Permissions and ask user question use durable interaction response. [6]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
