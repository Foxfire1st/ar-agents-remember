# mcp/src/agents_remember/models/tool_registry.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/tool_registry.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-03T00:30+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tool_registry.py` maps modeled MCP payload-builder names to response model
classes and exposes the advertised public subset separately. L11 maps
`task_reopen` → `TaskReopenResponse` (imported from `models.task_doc`).

## Code Commentary

`TOOL_RESPONSE_MODELS` is the enforcement registry consumed by
`mcp.tools._tool_payload()`. It covers all modeled core, runtime, memory, skill
install, provider, worktree (including `worktree_sync` → `WorktreeSyncResponse`,
GitHub #54 sub-task D), benchmark, slice-2b lifecycle, the slice-3c
`task_doc` → `TaskDocResponse`, `lifecycle_gate` → `LifecycleGateResponse`, the
control-plane gate payload builders (`gate_create`/`gate_decide`/`gate_wait`/
`gate_response_wait`/`gate_list` → the strict `models/gates.py` responses), plus the
task-10 external-chat inbox tools (`operator_inbox_post` / `operator_inbox_poll`
/ `operator_inbox_consume` → the strict `models/operator_inbox.py` responses),
plus dashboard task 14 `lifecycle_finalize_task` → `LifecycleFinalizeTaskResponse`,
plus the task-28 `lifecycle_turn_end_notification` → `LifecycleTurnEndNotificationResponse`
(the public NOTIFY-AND-CONTINUE turn-end response), plus L9
`attach_terminal_session_to_leaf` → `AttachTerminalSessionToLeafResponse`
(`models/terminal.py`) — 56 entries. `INTERNAL_COMPAT_TOOL_NAMES` identifies the four lower-level split
builders that remain modeled but are not advertised MCP tools:
`lifecycle_block`, `gate_create`, `gate_wait`, and `gate_response_wait`
(`lifecycle_turn_end_notification` is deliberately NOT among them — it is a real
public tool). `PUBLIC_TOOL_RESPONSE_MODELS` is derived by filtering those names
out and matches the 52-entry `PUBLIC_TOOLS` tuple/server tool list. The lifecycle
rows map to STRICT `ToolResponse` subclasses in
`models/lifecycle.py` (`LifecycleStartResponse`, `LifecycleBlockResponse`,
`LifecycleResumeResponse`, `LifecycleTurnEndNotificationResponse`,
`LifecycleEndResponse`, `SwitchLifecycleResponse`,
`LifecyclePhaseResponse`).

The module docstring fixes a deliberate two-tier response-model convention.
Tools whose response shape is fully AR-owned register a STRICT model
(`StrictResponseModel` / `ResponseModel` / `ToolResponse`, `extra="forbid"`) so
the field set is a drift-proof contract; `context_packet` (`ContextPacketV2`),
`ping`, and `server_info` are the exemplars. Tools that surface provider-native
or raw diagnostic detail (CodeGraphContext, GrepAI, Docker, watcher output)
register a FLEXIBLE model (`FlexibleResponseModel` / `FlexibleToolResponse`,
`extra="allow"`) on purpose: the upstream provider owns that payload, so extra
fields are tolerated rather than rejected. This is tolerated drift, not
un-validated input -- the envelope (`ok`/`operation`/`tokens`) is still typed.
Pick STRICT unless the payload genuinely embeds provider-native detail.

## Invariants And Boundaries

- `PUBLIC_TOOL_RESPONSE_MODELS` keys must equal `mcp.tools.PUBLIC_TOOLS`.
- Adding or removing an advertised public tool requires updating this registry and the
  schema coverage tests.
- Lower-level compatibility builders stay in `TOOL_RESPONSE_MODELS` so their
  responses are still validated even though they are not registered as public MCP tools.
- The registry is response-only; it does not own request validation.
- A FLEXIBLE (`extra="allow"`) entry is a tolerated-drift surface for
  provider-native payloads, not a license to skip validation; the typed
  envelope still applies. AR-owned shapes must register a STRICT model.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Payload builders validate through `TOOL_RESPONSE_MODELS`. | [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| Tests assert exact coverage between `PUBLIC_TOOLS` and the public subset, and conformance across all modeled builders. | [test_tool_response_conformance.py](agents-remember/mcp/tests/test_tool_response_conformance.py) |
| Inbox responses registered here are strict AR-owned tool responses. | [operator_inbox.py](agents-remember/mcp/src/agents_remember/models/operator_inbox.py) |
| Gate responses, including the combined wait helper, are strict AR-owned tool responses. | [gates.py](agents-remember/mcp/src/agents_remember/models/gates.py) |
| Lifecycle finalizer response registered here is a strict AR-owned tool response. | [lifecycle_finalize.py](agents-remember/mcp/src/agents_remember/models/lifecycle_finalize.py) |
| Terminal leaf reassignment response registered here is a strict AR-owned tool response. | L78-L82; L105-L111 | [terminal.py](terminal.py) |

## Update History

- 2026-07-03T00:30+02:00 — L11 registers task_reopen → TaskReopenResponse.
- 2026-07-02T17:04+02:00 — L9: registered `attach_terminal_session_to_leaf` →
  `AttachTerminalSessionToLeafResponse`, keeping the new agent-facing reassignment tool in the strict
  AR-owned response-contract path. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): registered `lifecycle_turn_end_notification` → strict `LifecycleTurnEndNotificationResponse` (`models/lifecycle.py`). It is a real public tool — deliberately NOT in `INTERNAL_COMPAT_TOOL_NAMES` — so `TOOL_RESPONSE_MODELS` is now 55 entries and `PUBLIC_TOOL_RESPONSE_MODELS` is 51, still exactly matching `PUBLIC_TOOLS`. The parked `lifecycle_gate` → `LifecycleGateResponse` row is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T14:16+02:00 — Task 25: split the registry into all modeled builders (`TOOL_RESPONSE_MODELS`, 54 entries) and the advertised public subset (`PUBLIC_TOOL_RESPONSE_MODELS`, 50 entries), excluding `lifecycle_block`, `gate_create`, `gate_wait`, and `gate_response_wait` from the public MCP surface while keeping their response validation.
- 2026-06-25T07:17+02:00 — Task 19: registered `gate_response_wait` to strict `GateResponseWaitResponse`; the registry is now 52 entries and still exactly matches `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: registered `lifecycle_finalize_task` to strict `LifecycleFinalizeTaskResponse`; the registry is now 51 entries and still exactly matches `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: registered `operator_inbox_post` / `operator_inbox_poll` / `operator_inbox_consume` to strict `models/operator_inbox.py` responses; the registry is now 50 entries and still exactly matches `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: registered the four `gate_*` → strict `models/gates.py` responses (`GateCreateResponse`/`GateDecideResponse`/`GateWaitResponse`/`GateListResponse`); the registry is now 47 entries and still exactly matches `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: registered `task_doc` → `TaskDocResponse` (a STRICT `ToolResponse`); the registry is now 43 entries and still exactly matches `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: registered the six `lifecycle_*` STRICT response models (`models/lifecycle.py`); the registry is now 42 entries and still exactly matches `PUBLIC_TOOLS`. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — Removed the `direct_closeout_preview`/`direct_closeout_apply` rows and their model imports (issue #62 worktree-only closeout); the conformance tests enforce that the registry still exactly matches `PUBLIC_TOOLS`.
- 2026-06-10T09:56+02:00: Registered `worktree_sync` → `WorktreeSyncResponse` (GitHub #54 sub-task D).
- 2026-06-06T12:28+02:00: Corrected the payload-validation reference after the former `mcp/tools.py` module became the `mcp/tools/` package; source behavior unchanged.
- 2026-06-01T20:45+02:00 — Registered `worktree_abandon` → `WorktreeAbandonResponse` in `PUBLIC_TOOL_RESPONSE_MODELS`.
- 2026-05-31T12:30+02:00 — Documented the deliberate STRICT vs FLEXIBLE response-model two-tier convention now fixed in the module docstring (1.0.0 review remediation).
- 2026-05-28T19:52+02:00: Created for the public tool response model coverage registry.
