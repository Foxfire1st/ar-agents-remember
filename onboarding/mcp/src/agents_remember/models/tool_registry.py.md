# mcp/src/agents_remember/models/tool_registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tool_registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-15T09:10+02:00 |
| lastVerifiedCommitHash | `17987fa66a642306eb8d20fa9a4bff2b881550d2` |
| lastVerifiedCommitDate | 2026-08-15T14:36:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

`tool_registry.py` maps every modeled payload operation to its response model and derives the
advertised public subset by excluding internal compatibility and administration operations.

## Code Commentary

L23 registers response envelopes for `citation_fix` and `worktree_operation_cancel`, keeping the public registry aligned with the newly exposed tools.

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
| The advertised subset is derived rather than independently maintained. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:223-227 |
| The choke point validates against this registry before emitting the envelope. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |

## L23 Lifecycle Model Package Review

The public response registry now imports lifecycle turn/block/switch responses from
`models.lifecycles.responses` and finalization responses from `models.lifecycles.finalize`. The
registered model set and strict public response validation remain unchanged; only model ownership
was separated.

## 260815-DAG-L3 Queue Response Contract

The strict response registry maps `closeout_queue` to `CloseoutQueueResponse`, bringing the new
public tool under the same success-payload validation and public/registered parity gates as the
rest of the MCP surface.

## Update History

- 2026-08-15T09:10+02:00 — L3 content update: registered the strict closeout-queue response model;
  verification remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 curator: reviewed the split lifecycle response/finalize imports and
  confirmed registry membership is unchanged; final provenance remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T12:15+02:00 — Reconciled the registry card with structural public responses and the
  expanded exact-id internal exclusion set. Verification remains pinned pending governed closeout.
- 2026-08-01T09:12+02:00 — The registry value type became `ResponseEnvelope`, making shared envelope
  fields reachable before serialization and documenting field/value strictness as separate axes.
- 2026-06-13T16:41+02:00 — Through 2026-08-08, response coverage grew across lifecycle, task, gate, inbox,
  orchestration, terminal, and worktree operations while public coverage remained derived.
