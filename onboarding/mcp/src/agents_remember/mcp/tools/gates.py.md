# mcp/src/agents_remember/mcp/tools/gates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/mcp/tools/gates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
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
| Structural response models omit private correlations. | `StructuralGateResponse`; `LifecycleGateResponse`; `GateDecideResponse`; `GateListResponse` | mcp/src/agents_remember/models/structural/gates.py:108-160 |
| The response registry distinguishes advertised structural names from internal compatibility builders. | `INTERNAL_COMPAT_TOOL_NAMES`; `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:121-148; mcp/src/agents_remember/models/tools/tool_registry.py:233-237 |

## Update History
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `INTERNAL_COMPAT_TOOL_NAMES`, `PUBLIC_TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:118-139, mcp/src/agents_remember/models/tools/tool_registry.py:227-231. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: re-anchored citation range(s) to current source after the L16 line movement (cited files changed, card source unchanged); verification metadata unchanged.

- 2026-08-11T12:15+02:00 — Reconciled the card with the structural public boundary: document-and-role
  gate operations are current; exact ids are internal correlations. Verification remains pinned
  pending governed closeout.
- 2026-08-08T17:18+02:00 — References were refreshed after the model-extraction wave.
- 2026-07-31T15:31+02:00 — Parameter objects separated raise/wait/inbox-watch concerns at the
  application seam without changing durable gate semantics.
- 2026-06-18T01:05+02:00 — Through 2026-07-08, the route gained durable gate create/decide/wait/list behavior,
  blocking lifecycle-gate orchestration, decision policy, evidence, and expectation-row tracking.
