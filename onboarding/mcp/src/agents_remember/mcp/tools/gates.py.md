# mcp/src/agents_remember/mcp/tools/gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T12:15+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external domain source governs this repository-local boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Structural gate adapters receive typed document-owned requests. | `structural_lifecycle_gate_payload`; `structural_gate_decide_payload`; `structural_gate_list_payload` | mcp/src/agents_remember/mcp/tools/gates.py:77-90; mcp/src/agents_remember/mcp/tools/gates.py:123-136; mcp/src/agents_remember/mcp/tools/gates.py:199-203 |
| Exact-id gate adapters are separate internal composition seams. | `gate_create_payload`; `gate_decide_payload`; `gate_list_payload` | mcp/src/agents_remember/mcp/tools/gates.py:44-55; mcp/src/agents_remember/mcp/tools/gates.py:92-110; mcp/src/agents_remember/mcp/tools/gates.py:191-196 |
| Structural response models omit private correlations. | `StructuralGateResponse`; `LifecycleGateResponse`; `GateDecideResponse`; `GateListResponse` | mcp/src/agents_remember/models/structural/gates.py:108-151 |
| The response registry distinguishes advertised structural names from internal compatibility builders. | `INTERNAL_COMPAT_TOOL_NAMES`; `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-137; mcp/src/agents_remember/models/tool_registry.py:223-227 |

## Update History

- 2026-08-11T12:15+02:00 — Reconciled the card with the structural public boundary: document-and-role
  gate operations are current; exact ids are internal correlations. Verification remains pinned
  pending governed closeout.
- 2026-08-08T17:18+02:00 — References were refreshed after the model-extraction wave.
- 2026-07-31T15:31+02:00 — Parameter objects separated raise/wait/inbox-watch concerns at the
  application seam without changing durable gate semantics.
- 2026-06-18T01:05+02:00 — Through 2026-07-08, the route gained durable gate create/decide/wait/list behavior,
  blocking lifecycle-gate orchestration, decision policy, evidence, and expectation-row tracking.
