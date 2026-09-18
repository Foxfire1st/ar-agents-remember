# mcp/src/agents_remember/models/tools/tool_registry.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/tools/tool_registry.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T20:19:44+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[models overview](../overview.md)

## Purpose

`tool_registry.py` maps every modeled payload operation to its response model and derives the
advertised public subset by excluding internal compatibility and administration operations.

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

## Docs References

No external domain source governs this repository-local registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exclusion set names trusted compatibility and administration operations. | `INTERNAL_COMPAT_TOOL_NAMES` | mcp/src/agents_remember/models/tools/tool_registry.py:126-147 |
| The complete registry includes structural agent and gate responses alongside internal exact models. | "\"dispatch_agent\": DispatchAgentResponse,"; "\"gate_decide\": GateDecideResponse," | mcp/src/agents_remember/models/tools/tool_registry.py:155-238 |
| The advertised subset is derived rather than independently maintained. | `PUBLIC_TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tools/tool_registry.py:241-244 |
| The checkpoint-landing tool's response model is registered between its integrate and record-landing siblings, matching the advertised order. | `worktree_checkpoint_landing` | mcp/src/agents_remember/models/tools/tool_registry.py:198-198 |
| The stop tool's response model is registered immediately after its sync sibling, matching the advertised order. | `worktree_pause` | mcp/src/agents_remember/models/tools/tool_registry.py:194-194 |
| The record-landing tool's response model is registered immediately after its checkpoint sibling, matching the advertised order. | `worktree_record_landing` | mcp/src/agents_remember/models/tools/tool_registry.py:199-199 |
| The three rows the capsule-and-skill registrar needs, at the mapping's tail to match their appended roster position. | `role_capsule_compile`; `skill_catalog_list`; `skill_catalog_read` | mcp/src/agents_remember/models/tools/tool_registry.py:238-240 |
| The choke point validates against this registry before emitting the envelope. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| The three strict contracts the new rows map to, including the shared success/refusal capsule envelope. | `RoleCapsuleResponse`; `SkillCatalogListResponse`; `SkillCatalogReadResponse` | mcp/src/agents_remember/models/role_capsule_resources.py:86-115; mcp/src/agents_remember/models/role_capsule_resources.py:137-150; mcp/src/agents_remember/models/role_capsule_resources.py:153-167 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes the module-level vocabulary at this ownership boundary. | "INTERNAL_COMPAT_TOOL_NAMES = frozenset("; "PUBLIC_TOOL_RESPONSE_MODELS: dict[str, type[ResponseEnvelope]] = {" | mcp/src/agents_remember/models/tools/tool_registry.py:121-148; mcp/src/agents_remember/models/tools/tool_registry.py:233-237; mcp/src/agents_remember/models/tools/tool_registry.py:243-243 |

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

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_checkpoint_landing` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:198-198. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_pause` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `worktree_record_landing` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:199-199. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `role_capsule_compile`; `skill_catalog_list`; `skill_catalog_read` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:238-238; mcp/src/agents_remember/models/tools/tool_registry.py:239-239; mcp/src/agents_remember/models/tools/tool_registry.py:240-240. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator (uncommitted change set on `ar/260915-caps-l4`, base
  `b00a4ac2`): registered the three response-model rows the new capsule-and-skill-serving registrar
  needs — `role_capsule_compile` → `RoleCapsuleResponse`, `skill_catalog_list` →
  `SkillCatalogListResponse`, `skill_catalog_read` → `SkillCatalogReadResponse`, imported from
  `models.role_capsule_resources` and placed at the mapping's tail (`:236-238`) to match the appended
  tail position of the three names in `PUBLIC_TOOLS`. Recorded that the roster rows, the registrar
  declaration and these registry rows all landed in one change, and that the new capsule envelope
  carries its refusal as the same envelope rather than a second model. Re-derived this card's registry
  ranges against the current source: `INTERNAL_COMPAT_TOOL_NAMES` 120-141 → **126-147**,
  `TOOL_RESPONSE_MODELS` 150-231 → **155-238** and `PUBLIC_TOOL_RESPONSE_MODELS` 233-237 → **241-244**;
  the removal of the `closeout_door` row and this leaf's three additions both moved them. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T17:20:55+00:00: Generated citation repair: `worktree_checkpoint_landing` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:191-191. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: `worktree_record_landing` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:192-192. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37 citation review (curator-authored, not a mechanical
  projection): re-read the two `TOOL_RESPONSE_MODELS` claims and the module-level vocabulary row against
  the current source and re-cited them to the extents those constructs now occupy —
  `INTERNAL_COMPAT_TOOL_NAMES` `121-148`, `TOOL_RESPONSE_MODELS` `150-231`,
  `PUBLIC_TOOL_RESPONSE_MODELS` `233-237`. The ranges cover the constructs the claims name and the
  wording holds unchanged. The previous ranges had arrived from generated anchor-range projections,
  which are not evidence that a claim still holds; these are curator-confirmed.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: registered `worktree_pause` →
  `WorktreePauseResponse` between the sync and closeout-preview rows, recorded the by-name registry
  lookup as the reason the row is mandatory, and re-derived this card's reference ranges
  (`TOOL_RESPONSE_MODELS` 150-231, `PUBLIC_TOOL_RESPONSE_MODELS` 233-237, checkpoint row 190,
  record-landing row 191). Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:22-24. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: registered
  `worktree_checkpoint_landing` → `WorktreeCheckpointLandingResponse` between the integrate and
  record-landing rows, recorded the by-name registry lookup as the reason the row is mandatory, and
  re-derived this card's reference ranges. Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: registered
  `worktree_record_landing` → `WorktreeRecordLandingResponse` immediately after `worktree_integrate`,
  recorded the by-name registry lookup as the reason an advertised-but-unregistered tool cannot
  answer, and added its reference row. Verification metadata remains closeout-owned; no acceptance
  claim.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `INTERNAL_COMPAT_TOOL_NAMES`, `PUBLIC_TOOL_RESPONSE_MODELS`, `TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:118-139, mcp/src/agents_remember/models/tools/tool_registry.py:147-225, mcp/src/agents_remember/models/tools/tool_registry.py:227-231. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `INTERNAL_COMPAT_TOOL_NAMES` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:118-139. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:147-225. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `PUBLIC_TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:227-231. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:75-77. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `PUBLIC_TOOL_RESPONSE_MODELS` repointed to mcp/src/agents_remember/models/tools/tool_registry.py:235-239. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:79-81. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded the `worktree_status_wait` response-model registry row.
- 2026-08-29T08:52+02:00 — Registered strict response conformance for the one curator-coherence
  tool. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: registered the strict closeout-door response model. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/models/tools/tool_registry.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-20T09:35+02:00 — 260815-DAG-L16: registers `direct_landing` → `DirectLandingResponse` in
  `TOOL_RESPONSE_MODELS`. Verified at code commit a9d50e08.


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
