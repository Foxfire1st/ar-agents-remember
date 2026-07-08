# mcp/src/agents_remember/models/ - Response Contract Models Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/models/`          |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-07-08T14:45+02:00 |
| lastVerifiedCommitHash | `45708bbddf1ddb8a2045faa9fad88fe72603b674` |
| lastVerifiedCommitDate | 2026-07-08T05:51:44+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

`models/` owns the Pydantic response contracts for Agents Remember MCP payload
builders. It turns the public tool surface and retained compatibility builders
from loose dictionaries into named, inspectable models that can be validated at
runtime and tested by schema. Model homes follow tool domains: `TaskReopenResponse`
(L11) lives in `task_doc.py` while keeping the `WorktreeCommandResponse` shape, since
the task_reopen payload carries the enclosure contract state.

## Hot Path Summary

Start with `tool_registry.py`: `TOOL_RESPONSE_MODELS` maps every modeled builder
to one response model, while `PUBLIC_TOOL_RESPONSE_MODELS` filters out retained
compatibility builders so it matches `mcp.tools.PUBLIC_TOOLS`. `base.py` defines strict response envelopes, intentionally
flexible detail envelopes, token metadata fields, and the strict `NextStep`
lifecycle-hint model carried by an optional `nextStep` field on BOTH envelope
bases (`ResponseModel` and `FlexibleResponseEnvelope`), so every modeled tool
response can surface the computed next move. Domain modules then own
contract slices: `context_packet.py` for compact `ContextPacketV2`,
`providers.py` for provider summaries and diagnostics, `worktree.py` for
worktree context/status responses including `enclosurePath`, `leafId`, and `kind`, `memory.py` for memory/onboarding tools,
`runtime.py` for runtime and resolver tools, `benchmarks.py` for Codex
benchmark tools, `lifecycle.py` for the `lifecycle_*` signal responses
(with `LifecycleStartResponse` also carrying an optional `frontHalfRundown`
front-half roadmap, and the task-28 `LifecycleTurnEndNotificationResponse`
adding a `summary` for the public NOTIFY-AND-CONTINUE turn-end tool),
`task_doc.py` for the `task_doc` authoring response including the optional Task 21 `masterSync`
leaf-to-master result, `gates.py` for
`LifecycleGateResponse`, the public gate decide/list responses, and retained
compatibility gate responses (L4 adds delegated-decision `decidingRole` and
`evidenceRefs` to the decide response), `operator_inbox.py` for the
three `operator_inbox_*` external-chat response contracts (task 10),
`orchestration.py` for the strict `orchestration_nudge_manager` response,
`lifecycle_finalize.py` for the strict terminal task-finalizer response, `terminal.py` for the strict
`attach_terminal_session_to_leaf` hosted-chat/terminal reassignment response AND the L2
`spawn_agent_session` dispatch response (`SpawnAgentSessionResponse` — spawned-by provenance +
context-delivery outcome (since 260707-HFX-L3 incl. the failure-evidence `deliveryCapture` field) + the server-arbitrated `leaf-taken`/pre-spawn refusal statuses; since HFX-L4 the attach/spawn models also accept
`leaf-ref-not-found` / `leaf-ref-ambiguous` refusals with the original `leafKey` and optional detail; since
260703-L16 also the `effort-invalid`/`model-invalid`/`level-invalid` refusals, the free-form spawn
provenance `launchArgs`/`promptKeywords`/`sessionCommands` + `sessionCommandsDelivered`, and the
level provenance `spawnLevel`/`spawnLevelSource`), and
`tokens.py` for response token accounting. **260707-HFX-L8** adds two more strict models to
`terminal.py`: `SessionRetireResponse` (`retired`/`already-retired`/`unknown-session`/
`unknown-actor`/`retire-refused` statuses, retirement provenance fields, `detail` naming the exact
authority-policy clause on refusal) and `SessionRenameResponse` (`renamed`/`unknown-session`,
`label`/`spawnedLabel` — identity text only, no `spawn_role` field on this response since a rename
never changes it). `lifecycle_finalize.py`'s `LifecycleFinalizeTaskResponse` gains an additive
`autoRetiredSeats: list[str]` field for the master→super finalize edge's auto-retire hook.

## Route Model

- Owned compact contracts should inherit from `StrictResponseModel` or
  `ToolResponse` so unknown fields are rejected.
- Native/detail surfaces that intentionally pass through provider or service
  payloads should inherit from `FlexibleResponseModel` or `FlexibleToolResponse`.
- The strict `NextStep` model (task 27) mirrors the worktree guidance dict shape
  (`summary` plus optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`),
  so an operational hint and a gate-raise share one vocabulary (a gate junction
  is just `nextTool="lifecycle_gate"`). Both envelope bases
  ([base.py](agents-remember/mcp/src/agents_remember/models/base.py)) declare an
  optional `nextStep: NextStep | None` field, populated for in-lifecycle calls at
  the [mcp/tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py)`::_tool_payload`
  choke point and excluded when None, so lifecycle-less calls stay unchanged.
- `ContextPacketV2` keeps startup context compact and points detailed provider
  troubleshooting to `provider_diagnostics`.
- Token metadata fields exist on every modeled response; the final S6 wiring
  fills them from the serialized JSON payload.

## Invariants And Boundaries

- Every public MCP tool must have exactly one declared response model in
  `PUBLIC_TOOL_RESPONSE_MODELS`; every retained compatibility builder that still
  returns through `_tool_payload` must have one in `TOOL_RESPONSE_MODELS`.
- Do not rely on Pydantic to silently coerce nested raw dictionaries for owned
  contract objects. Construct nested models explicitly, or call
  `NestedModel.model_validate(...)` only at a narrow raw-adapter boundary.
- Keep `context_packet` free of `rawStatus` and duplicate top-level
  `pathRules`; detailed provider state belongs in `provider_diagnostics`.
- Nullable response fields that can be omitted after `exclude_none=True` must
  declare optional defaults (`= None`); otherwise a later public payload
  validation pass treats the missing key as a required-field error.
- Flexible models are for intentionally raw/detail payloads, not a shortcut for
  avoiding a stable public contract.
- Tools whose bulk moved to `temp/tool-reports/` (2.5.1: runtime install,
  provider diagnostics/watchers; 2.5.2: carryover plan/apply) document the
  compact wire fields as optional declared fields on their flexible models —
  `reportPath` everywhere, plus the per-tool digests (rebind `phases`,
  carryover `decisions`/`carriedPaths`) — so the compact shape is discoverable
  from the model even though the envelope stays flexible.

L14: the task-doc node model exposes the optional `orchestrates` list and the sessions wire model carries the optional `spawnRole` — both additive, absent on old payloads.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Public MCP payload builders validate through the response model registry. | [mcp/tools/](agents-remember/mcp/src/agents_remember/mcp/tools/) |
| The registry maps every modeled builder and the advertised public subset to response models. | [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| Contract tests prove public tool coverage and schema generation. | [test_models.py](agents-remember/mcp/tests/test_models.py) |
| Operator inbox response models cover post, poll, consume, and hosted-delivery metadata. | [operator_inbox.py](agents-remember/mcp/src/agents_remember/models/operator_inbox.py) |
| Orchestration response models cover the public manager-nudge helper. | [orchestration.py](agents-remember/mcp/src/agents_remember/models/orchestration.py) |
| Lifecycle finalizer response model covers the terminal task finalization payload. | [lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/models/lifecycle_finalize.py) |
| Terminal response models cover hosted session leaf reassignment and the L2 agent-facing session spawn. | [terminal.py](agents-remember/mcp/src/agents_remember/models/terminal.py) |
| The next-step engine that fills `nextStep` from the active lifecycle. | [next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py) |

## Update History

- 2026-07-08T14:45+02:00 — No route impact: 260707-HFX2-L1 adds `ownerRole`/`ownerAgentId`/`ownerLifecycleId` to `OperatorInboxPostResponse` (`models/operator_inbox.py.md` documents the field addition); the response-contract pattern and module layout are unchanged.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issues #12/#4): `models/terminal.py` adds `SessionRetireResponse`/`SessionRenameResponse`
  (strict `ToolResponse`), `tool_registry.py` registers `session_retire`/`session_rename` → those
  models; `models/lifecycle_finalize.py`'s `LifecycleFinalizeTaskResponse` gains additive
  `autoRetiredSeats: list[str]`. Follows the existing STRICT `ToolResponse` pattern, so the
  strict/flexible split this overview describes is unchanged. Verification metadata pinned until
  closeout stamps the HFX-L8 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4 route impact: `models/terminal.py` accepts
  `leaf-ref-not-found` / `leaf-ref-ambiguous` statuses on terminal attach and spawn responses, with
  optional detail for attach refusals. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 route impact (additive field): `terminal.py`'s
  `SpawnAgentSessionResponse` gained `deliveryCapture` — the pane-capture evidence attached whenever
  context delivery or submit fails (never a bare false-success boolean); the response model shape is
  otherwise unchanged.
- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 1 declares the additive optional
  `removedSubtask`/`deletedFiles`/`wouldDeleteFiles` fields on `TaskDocResponse` so a `remove_subtask`
  success validates against `extra="forbid"`; it stays a STRICT `ToolResponse`, so the strict/flexible
  split this overview describes is unchanged (detail in the file sidecar).
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application) route impact: `terminal.py`'s
  `SpawnAgentSessionResponse` gained three refusal statuses (`effort-invalid`/`model-invalid`/
  `level-invalid`) and the free-form + level provenance fields (all additive, `None`-omitted). No
  other model changed. Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:59:58+02:00 — L14 route impact (body): optional orchestrates + spawnRole on the response models. Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T23:59:42+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: `terminal.py`'s `SpawnAgentSessionResponse` gained the optional `spawnRole` field mirroring the new catalog column (additive, `None`-omitted). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: `models/gates.py` extends
  `GateDecideResponse` with delegated-decision attribution and evidence refs.
  It remains a strict `ToolResponse`, so the strict/flexible route model is
  unchanged. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: added the strict orchestration
  nudge response model and expanded inbox response fields for delivery metadata.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2 route impact: `models/terminal.py` adds the strict
  `SpawnAgentSessionResponse` (+ `SpawnAgentSessionStatus`) for the agent-facing `spawn_agent_session`
  dispatch tool, and `tool_registry.py` registers `spawn_agent_session` → that model in the strict public
  response-contract path. It follows the existing STRICT `ToolResponse` pattern, so the strict/flexible
  split this overview describes is unchanged. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-03T00:35+02:00 — L11 route impact: TaskReopenResponse added in task_doc.py; tool_registry maps task_reopen to it.
- 2026-07-02T17:04+02:00 — L9 route impact: added `models/terminal.py` with the strict
  `AttachTerminalSessionToLeafResponse` and registered it in `tool_registry.py` for the new public
  reassignment tool. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 route impact: `models/lifecycle.py` adds `LifecycleTurnEndNotificationResponse(LifecycleResponse)` (adds a required `summary`) and `tool_registry.py` registers `lifecycle_turn_end_notification` → that strict response as a real public tool (not in `INTERNAL_COMPAT_TOOL_NAMES`; `TOOL_RESPONSE_MODELS` → 55, `PUBLIC_TOOL_RESPONSE_MODELS` → 51, still matching `PUBLIC_TOOLS`). It follows the existing STRICT `ToolResponse` pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27 route impact: `base.py` adds the strict `NextStep`
  lifecycle-hint model (`summary` + optional `nextOperation`/`nextTool`/`nextArgs`/`nextRequiredArgs`,
  mirroring the worktree guidance dict so a gate-raise is `nextTool="lifecycle_gate"`) and an optional
  `nextStep: NextStep | None` field on both envelope bases (`ResponseModel`, `FlexibleResponseEnvelope`),
  populated at `mcp/tools/base.py::_tool_payload` and excluded when None; `lifecycle.py::LifecycleStartResponse`
  gains an optional `frontHalfRundown: list[str] | None`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: `models/task_doc.py` adds the optional
  `TaskDocMasterSync` nested response so `task_doc` leaf writes can report same-root master-row changes.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — Task 25: response-model route now distinguishes all modeled builders (`TOOL_RESPONSE_MODELS`) from the advertised public subset and includes `LifecycleGateResponse` for the unified gate junction.
- 2026-06-25T07:26+02:00 — Task 19: `models/gates.py` now models gate wait decision metadata and the
  strict `GateResponseWaitResponse`, with `tool_registry.py` mapping `gate_response_wait` into the public
  response-contract surface. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree response models now declare leaf enclosure identity (`enclosurePath`, `leafId`, `kind`) and finalizer responses declare `taskArchive` for completed root-task archival. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: added `models/lifecycle_finalize.py`, a strict `ToolResponse` for `lifecycle_finalize_task`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: added `models/operator_inbox.py` and its three strict `ToolResponse` registry rows. The strict/flexible route model is unchanged. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T07:23 — No route impact: slice 3c R5 adds the additive optional `dryRun`/`rendered`/`diff`/`wouldLose` fields to `TaskDocResponse` (set only on a dry-run preview); it stays a STRICT `ToolResponse`, so the strict/flexible split this overview describes is unchanged (detail in the file sidecar). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: added `models/gates.py` (the four `gate_*` strict `ToolResponse` subclasses) to the route and their `tool_registry` rows; they follow the existing STRICT pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: added `models/task_doc.py` (`TaskDocResponse`, a STRICT `ToolResponse`) to the route and its `tool_registry` row; it follows the existing STRICT pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c declares one optional `lifecycleId` field on the flexible `WorktreeCommandResponse`; the strict/flexible response-contract route model this overview describes is unchanged (detail in the file sidecar).
- 2026-06-13T16:41+02:00 — Slice 2b: added `models/lifecycle.py` (the six `lifecycle_*` STRICT response models) to the route; they follow the existing STRICT `ToolResponse` pattern, so the strict/flexible split this overview describes is unchanged. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed `DirectCloseoutPreviewResponse`/`DirectCloseoutApplyResponse`, their registry rows, and their package exports; the strict/flexible route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T09:56+02:00 — No route impact: sub-task D adds `WorktreeSyncResponse` (one more flexible `WorktreeCommandResponse` subclass) and its registry row (GitHub #54); the strict/flexible route model this overview describes is unchanged (detail in the file sidecars).
- 2026-06-10T07:40+02:00 — No route impact: `models/worktree.py` only documented the existing flexible `providers` field's async setup states (GitHub #53).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.1/2.5.2 compact-response field documentation pattern (`reportPath` + per-tool digests declared on flexible models); previous closeouts had only stamped the verification header. Developer-flagged gap.
- 2026-06-08T09:57+02:00: Re-verified response model guidance after compact provider `ok` fields became optional-null defaults for skipped-provider payload re-validation.
- 2026-06-06T12:15: Re-verified against the current response model package; corrected the payload-builder reference from the deleted `mcp/tools.py` file to the `mcp/tools/` package.
- 2026-05-28T19:52+02:00: Created for the Pydantic public response-contract model package while S2/S4 source changes are still uncommitted in the checkout.
