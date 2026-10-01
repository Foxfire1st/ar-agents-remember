# mcp/src/agents_remember/mcp/tools/gates.py

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

This module is the response-adapter boundary for gate application operations. Agent-facing builders
accept structural requests and return document-and-role results. Exact gate/lifecycle correlations
remain available only to trusted application and operator paths.

## Code Commentary

`structural_lifecycle_gate_payload`, `structural_gate_decide_payload`, and
`structural_gate_list_payload` pass typed structural requests into the structural application and
validate the result through `_tool_payload`. The older exact builders use distinct internal
operation names in the response registry; they are not advertised agent tools.

The module does not decide authority. Ambient-seat derivation, topology checks, unique gate
selection, persistence, waiting, and decision attribution live in the application/control-plane
layers. This boundary only chooses the correct operation family and response model.

## Invariants And Boundaries

- Public gate requests never carry lifecycle or gate ids.
- A child decision is addressed by canonical task document and gate kind; zero or multiple matches
  fail closed below this adapter.
- Internal exact builders stay explicitly named and excluded from the public registry.
- All results cross `_tool_payload` once for response validation and envelope decoration.

## Evidence

### Docs References

No external domain source governs this repository-local boundary.

No configured domain documentation was available.

### Repo-Internal References

- Structural gate adapters receive typed document-owned requests. [1]
- Exact-id gate adapters are separate internal composition seams. [2]
- Structural response models omit private correlations. [3]
- The response registry distinguishes advertised structural names from internal compatibility builders. [4]
