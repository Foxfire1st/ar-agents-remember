# mcp/src/agents_remember/models/tools/tool_registry.py

## Governing Overview

[models overview](../overview.md)

## Purpose

`tool_registry.py` maps every modeled payload operation to its response model and derives the
advertised public subset by excluding internal compatibility and administration operations.

Maps public tool operation names to their declared response contracts.

## Code Commentary

L23 registers response envelopes for `citation_fix` and `worktree_operation_cancel`, keeping the public registry aligned with the newly exposed tools.

`TOOL_RESPONSE_MODELS` is typed as `dict[str, type[ResponseEnvelope]]`, preserving the strict versus
provider-flexible response convention while allowing `_tool_payload` to set shared envelope fields
before one model dump. `PUBLIC_TOOL_RESPONSE_MODELS` filters the complete registry through
`INTERNAL_COMPAT_TOOL_NAMES`.

The public set now includes structural dispatch, message, child lifecycle, and gate responses;
260815-DAG-L16 registers `direct_landing` → `DirectLandingResponse` for the direct-execution
landing operation.
Exact terminal session operations, operator inbox administration, legacy gate composition, and
orchestration nudge builders remain modeled for trusted callers but are deliberately not public.

### Role Runtime and Scope

TOOL_RESPONSE_MODELS adds role_start=RoleStartResponse and role_message=RoleMessageResponse. This retains the strict owned-field response contract and common _tool_payload validation/token path; provider-native flexible response policy is unchanged.

## Invariants And Boundaries

- Every advertised MCP tool has a registered response model.
- **Registration is what makes an advertised tool answerable.** `finalize_tool_response` indexes
  `TOOL_RESPONSE_MODELS` by tool name (`models/tools/tool_response.py`), so a name that FastMCP
  publishes but this registry omits raises `KeyError` inside the tool handler rather than returning
  a payload. A registered row must also sit in the same relative order as its
  `mcp.tools.PUBLIC_TOOLS` entry.
- Internal exact-id operations can be validated without becoming agent-visible tools.
- Agent-facing structural response models do not expose runtime session, lifecycle, inbox, or gate ids.
- Field-set strictness and producer-owned value vocabularies are separate contract axes.

## Evidence

### Docs References

No external domain source governs this repository-local registry.

No configured domain documentation was available.

### Repo-Internal References

- The exclusion set names trusted compatibility and administration operations. [1]
- The complete registry includes structural agent and gate responses alongside internal exact models. [2]
- The advertised subset is derived rather than independently maintained. [3]
- The checkpoint-landing tool's response model is registered between its integrate and record-landing siblings, matching the advertised order. [4]
- The stop tool's response model is registered immediately after its sync sibling, matching the advertised order. [5]
- The record-landing tool's response model is registered immediately after its checkpoint sibling, matching the advertised order. [6]
- The three rows the capsule-and-skill registrar needs, at the mapping's tail to match their appended roster position. [7]
- The choke point validates against this registry before emitting the envelope. [8]
- The five rows the knowledge registrar needs, at the mapping's tail to match their appended roster position. [9]
- The five strict response contracts those rows map to, in the module that declares them and exports exactly those five names. [10]
- The three strict contracts the capsule rows map to, including the shared success/refusal capsule envelope. [11]

### Runtime Source References

- Frozen implementation of TOOL_RESPONSE_MODELS supporting the stated file behavior. [13]

## L23 Lifecycle Model Package Review

The public response registry now imports lifecycle turn/block/switch responses from
`models.lifecycles.responses` and finalization responses from `models.lifecycles.finalize`. The
registered model set and strict public response validation remain unchanged; only model ownership
was separated.

## 260815-DAG-L3 Queue Response Contract

The strict response registry maps `closeout_queue` to `CloseoutQueueResponse`, bringing the new
public tool under the same success-payload validation and public/registered parity gates as the
rest of the MCP surface.

## 260821-CLIVE-L2 Current Contract

The current source seams include the module-level vocabulary. The model change keeps public vocabulary closed and validates nonblank identity/evidence fields. Models describe state but do not locate journals, authorize mutation, or supply compatibility fallbacks.

### Reconciled Source Evidence

- The current module exposes the module-level vocabulary at this ownership boundary. [12]

## 260821-CLIVE Strict Door Response

The public registry maps `closeout_door` to the strict `CloseoutDoorResponse`. This validates the
canonical generation, refusal shape, operation result, and downstream projection effects at the
same single response-model boundary as other AR-owned tools. It remains distinct from the
`closeout_queue` projection response.

## MCAR-L02 Response Registry

The strict response registry maps `curator_coherence` to `CuratorCoherenceResponse`, so every
success and typed refusal from all four actions passes the same no-extra-fields public boundary.

## 260831-CCR-L15 Status-Wait Response Model

`TOOL_RESPONSE_MODELS` now maps `worktree_status_wait` to
`WorktreeStatusWaitResponse` (imported from `models.worktree`), so the read-only
wait tool shares the strict typed response registry with the other worktree tools.

## 260831-LOCR-L29 Record-Landing Registration Row

`TOOL_RESPONSE_MODELS` now maps `worktree_record_landing` to `WorktreeRecordLandingResponse`
(imported from `models.worktree`), placed immediately after `worktree_integrate` — its position at
that leaf; since 260831-LOCR-L30 the checkpoint-landing row sits between them — so the registry
order matches that tool's position in `mcp.tools.PUBLIC_TOOLS`.

This row is the registry half of the public-surface repair, and the reason the hole was invisible.
`mcp/registration/closeout.py` registered the tool and FastMCP advertised it, while this registry
had no entry for the name. `finalize_tool_response` indexes this mapping by tool name, so the tool
was published and could not return a payload — the `KeyError` surfaced where no caller sees the
model contract that was violated. `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` now drives
one `finalize_tool_response` call for this name as well as comparing registered names to the
advertised tuple, so a missing row fails in the suite instead of at a caller.

## 260831-LOCR-L30 Checkpoint-Landing Registration Row

`TOOL_RESPONSE_MODELS` now maps `worktree_checkpoint_landing` to
`WorktreeCheckpointLandingResponse` (imported from `models.worktree`), inserted between
`worktree_integrate` and `worktree_record_landing` so the registry order matches that name's position
in `mcp.tools.PUBLIC_TOOLS`.

This is the second tool to exercise the L29 rule by construction rather than by repair: a name that
`mcp/registration/closeout.py` registers and FastMCP advertises but this mapping omits raises
`KeyError` inside the tool handler, because `finalize_tool_response` indexes this registry by tool
name. The two landing tools are also why a *set* comparison is not enough — they sit adjacent in the
registry and their payloads differ only in the operation literal, so
`mcp/tests/test_tools.py::PublicSurfaceInventoryTests` drives one `finalize_tool_response` call per
name as well as comparing registered names to the advertised tuple.

## 260831-LOCR-L37 Pause Registration Row

`TOOL_RESPONSE_MODELS` now maps `worktree_pause` to `WorktreePauseResponse` (imported from
`models.worktree`), inserted between `worktree_sync` and `worktree_closeout_preview` so the registry
order matches that name's position in `mcp.tools.PUBLIC_TOOLS`.

The row is mandatory for the same reason the checkpoint's is: `mcp/registration/worktrees.py`
registers and FastMCP advertises the name, and `finalize_tool_response` indexes this registry by tool
name, so a missing row raises `KeyError` inside the handler instead of returning a payload. The
envelope it maps to is the one whose only own field is `paused`, which the stop's route claims and a
publication's envelope cannot express.

## 260915-CAPS-L4 Capsule And Skill Registration Rows

`TOOL_RESPONSE_MODELS` now maps the three names the new `mcp/registration/capsule_serving.py` family
publishes, each to a strict model imported from `models.role_capsule_resources`:

| Name | Response model |
| --- | --- |
| `role_capsule_compile` | `RoleCapsuleResponse` |
| `skill_catalog_list` | `SkillCatalogListResponse` |
| `skill_catalog_read` | `SkillCatalogReadResponse` |

All three rows and all three advertised names were added in one change, together with the registrar
that declares them, so the roster, the registrar and this registry never disagreed — the L29 rule
applied by construction for the third time. The rows are mandatory for the reason this card already
records: `finalize_tool_response` indexes this mapping by tool name, so a name FastMCP advertises but
this registry omits raises `KeyError` inside the handler instead of returning a payload. The three new
names sit at the tail of the mapping (`:236-238`), matching their appended position at the tail of
`PUBLIC_TOOLS`.

`RoleCapsuleResponse` is also the first strict response on this registry whose **refusal** is the same
envelope as its success (`ok` false plus a typed `refusalStatus`), so the row covers both shapes without
a second model.

## 260915-KS-L20 Knowledge Registration Rows

`TOOL_RESPONSE_MODELS` now maps the five names the new `mcp/registration/knowledge.py` family
publishes, each to a strict model imported from `models.tools.knowledge_responses`:

| Name | Response model |
| --- | --- |
| `knowledge_read` | `KnowledgeReadResponse` |
| `knowledge_change` | `KnowledgeChangeResponse` |
| `knowledge_diff` | `KnowledgeDiffResponse` |
| `knowledge_integrity_check` | `KnowledgeIntegrityCheckResponse` |
| `knowledge_project` | `KnowledgeProjectResponse` |

All five rows and all five advertised names were added in one change, together with the registrar that
declares them and the roster tail that advertises them, so the roster, the registrar and this registry
never disagreed — the L29 rule applied by construction for the fourth time, and the **second**
append-only membership change in this master. The rows are mandatory for the reason this card already
records: `finalize_tool_response` indexes this mapping by tool name, so a name FastMCP advertises but
this registry omits raises `KeyError` inside the handler instead of returning a payload. The five new
names sit at the tail of the mapping (`:248-252`), matching their appended position at the tail of
`PUBLIC_TOOLS`.

**One shape, not five** is the property these five envelopes share. Each is a strict `ToolResponse`
whose own fields are the wire contract, and each carries the same two-state discriminator — the
operation's own payload state or `refused` — with refusal fields that name the offending input, so a
handler cannot translate a refusal into an empty result or a default. `knowledge_read`'s payload is the
**view payload itself**, which is why the classification rule has exactly one implementation: a tool
that re-rendered a view in its own format would create a second renderer and therefore a second place
for that rule to be violated. `KnowledgeIntegrityCheckResponse` carries `compatible: null` beside an
explicit `unresolved` list rather than manufacturing a verdict from a passing test.
