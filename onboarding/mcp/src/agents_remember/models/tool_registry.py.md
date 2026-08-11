# mcp/src/agents_remember/models/tool_registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tool_registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-11T12:15+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

`tool_registry.py` maps every modeled payload operation to its response model and derives the
advertised public subset by excluding internal compatibility and administration operations.

## Code Commentary

`TOOL_RESPONSE_MODELS` is typed as `dict[str, type[ResponseEnvelope]]`, preserving the strict versus
provider-flexible response convention while allowing `_tool_payload` to set shared envelope fields
before one model dump. `PUBLIC_TOOL_RESPONSE_MODELS` filters the complete registry through
`INTERNAL_COMPAT_TOOL_NAMES`.

The public set now includes structural dispatch, message, child lifecycle, and gate responses.
Exact terminal session operations, operator inbox administration, legacy gate composition, and
orchestration nudge builders remain modeled for trusted callers but are deliberately not public.

## Invariants And Boundaries

- Every advertised MCP tool has a registered response model.
- Internal exact-id operations can be validated without becoming agent-visible tools.
- Agent-facing structural response models do not expose runtime session, lifecycle, inbox, or gate ids.
- Field-set strictness and producer-owned value vocabularies are separate contract axes.

## Docs References

No external domain source governs this repository-local registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exclusion set names trusted compatibility and administration operations. | `INTERNAL_COMPAT_TOOL_NAMES` | mcp/src/agents_remember/models/tool_registry.py:113-134 |
| The complete registry includes structural agent and gate responses alongside internal exact models. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:142-215 |
| The advertised subset is derived rather than independently maintained. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:217-221 |
| The choke point validates against this registry before emitting the envelope. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:70-72 |

## Update History

- 2026-08-11T12:15+02:00 — Reconciled the registry card with structural public responses and the
  expanded exact-id internal exclusion set. Verification remains pinned pending governed closeout.
- 2026-08-01T09:12+02:00 — The registry value type became `ResponseEnvelope`, making shared envelope
  fields reachable before serialization and documenting field/value strictness as separate axes.
- 2026-06-13T16:41+02:00 — Through 2026-08-08, response coverage grew across lifecycle, task, gate, inbox,
  orchestration, terminal, and worktree operations while public coverage remained derived.
