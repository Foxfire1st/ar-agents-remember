# mcp/src/agents_remember/models/tool_registry.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/models/tool_registry.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-09T06:48+02:00                     |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`tool_registry.py` maps modeled MCP payload-builder names to response model
classes and exposes the advertised public subset separately. L11 maps
`task_reopen` -> `TaskReopenResponse` (imported from `models.task_doc`). L2 maps
`spawn_agent_session` -> `SpawnAgentSessionResponse` (imported from `models.terminal`).
L3 maps `orchestration_nudge_manager` -> `OrchestrationNudgeManagerResponse`
(imported from `models.orchestration`). 260713-TES-L4 maps
`operator_inbox_supersede` -> `OperatorInboxSupersedeResponse` (imported from
`models.operator_inbox`).

## Code Commentary

cit:([`TOOL_RESPONSE_MODELS`], mcp/src/agents_remember/models/tool_registry.py:116-179) is the enforcement registry consumed by
`mcp.tools._tool_payload()`. Its value type is
**`type[ResponseEnvelope]`** (`models.base`, the union
`ResponseModel | FlexibleResponseEnvelope`), not `type[BaseModel]`.
cit:([`PUBLIC_TOOL_RESPONSE_MODELS`], mcp/src/agents_remember/models/tool_registry.py:181-185) carries the same annotation. That is not
cosmetic: `BaseModel` made the envelope's two choke-point fields — `nextStep`
and `agentNotifierBanner` — unreachable by type from `_tool_payload`, which is how
`agentNotifierBanner` came to be written into the already-dumped dict instead of
declared at all. With `ResponseEnvelope` the choke point sets both on the
validated response *before* the single `model_dump`, so the emitted object stays
inside its own contract and inside its own token count. It covers all modeled core, runtime, memory, skill
install, provider, worktree (including `worktree_sync` → `WorktreeSyncResponse`,
GitHub #54 sub-task D), benchmark, slice-2b lifecycle, the slice-3c
`task_doc` → `TaskDocResponse`, `lifecycle_gate` → `LifecycleGateResponse`, the
control-plane gate payload builders (`gate_create`/`gate_decide`/`gate_wait`/
`gate_response_wait`/`gate_list` → the strict `models/gates.py` responses), plus the
task-10/L3 inbox tools (`operator_inbox_post` / `operator_inbox_poll`
/ `operator_inbox_consume`, plus 260713-TES-L4 `operator_inbox_supersede` -> the strict
`models/operator_inbox.py` responses),
the L3 orchestration nudge tool (`orchestration_nudge_manager` ->
`models/orchestration.py`),
plus dashboard task 14 `lifecycle_finalize_task` → `LifecycleFinalizeTaskResponse`,
plus the task-28 `lifecycle_turn_end_notification` → `LifecycleTurnEndNotificationResponse`
(the public NOTIFY-AND-CONTINUE turn-end response), plus L9
`attach_terminal_session_to_leaf` → `AttachTerminalSessionToLeafResponse` and L2
`spawn_agent_session` → `SpawnAgentSessionResponse`
(both `models/terminal.py`), plus 260707-HFX-L8 `session_retire` → `SessionRetireResponse` and
`session_rename` → `SessionRenameResponse` (both `models/terminal.py`, right after the
`spawn_agent_session` row). `INTERNAL_COMPAT_TOOL_NAMES` identifies the four lower-level split
builders that remain modeled but are not advertised MCP tools:
`lifecycle_block`, `gate_create`, `gate_wait`, and `gate_response_wait`
(`lifecycle_turn_end_notification` is deliberately NOT among them — it is a real
public tool). `PUBLIC_TOOL_RESPONSE_MODELS` is derived by filtering those names
out and matches the `PUBLIC_TOOLS` tuple/server tool list. The lifecycle
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

**The tier posture has two axes, and until 260731-EFA-L4 only one of them was
guarded.** `extra="forbid"` guards the **field set**: which keys may appear. The
`Literal` type aliases on those fields guard the **value set**: which tokens each
key may carry. Nothing enforced the second axis, and STRICT is precisely where
that hurts — a strict model is the one that *raises* on an unknown value, and it
raises with a `ValidationError` inside an `@server.tool()` handler that has no
`except` for one. Measured: 165 of the 213 `series-contract.md` files on disk
(77.5%) made `context_packet` raise, across seven independent gaps, every one of
them a hand-written `Literal` at a wire boundary over a vocabulary owned by some
other module. So the convention now has a third clause beside STRICT-vs-FLEXIBLE:
**a wire model never retypes a vocabulary it does not produce — it imports the
producer's alias.** `models/gates.py`, `lifecycle.py`, `operator_inbox.py` and
`orchestration.py` were already doing this; `models/worktree.py`,
`context_packet.py`, `drift.py`, `memory.py`, `read_files.py` and
`models/terminal.py` now do too. The set difference then cannot exist, because
there is no second set. `test_wire_vocabulary_exhaustiveness.py` is the suite
that pins it, in three deliberately different kinds (a behavioural walk of the
guidance state machine, an AST scan of every literal written at a vocabulary
field, and `produced == declared` equality against the `VALID_*` frozensets).

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
- **Both registries are `dict[str, type[ResponseEnvelope]]`.** Every registered
  model must be a `ResponseModel` or a `FlexibleResponseEnvelope`, because
  `_tool_payload` assigns the envelope's `nextStep` / `agentNotifierBanner` on the
  instance it validated. Widening this back to `type[BaseModel]` would silently
  put those two fields out of the type checker's reach again.
- **A registered model does not retype a vocabulary another module produces.**
  `extra="forbid"` is the field-set guard; the imported producer alias is the
  value-set guard. A hand-copied `Literal` at a wire boundary is a drift
  generator, and on a STRICT model it fails as an uncaught `ValidationError`
  inside the MCP handler.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Payload builders validate through `TOOL_RESPONSE_MODELS` at `_tool_payload`. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:73-75 |
| Tests assert exact coverage between `PUBLIC_TOOLS` and the public subset, and conformance across all modeled builders. | `PUBLIC_TOOLS` | mcp/src/agents_remember/mcp/tools/base.py:10-69 |
| Inbox responses registered here are strict AR-owned tool responses: `OperatorInboxPostResponse`, `OperatorInboxPollResponse`, and `OperatorInboxConsumeResponse`. | `OperatorInboxPostResponse`; `OperatorInboxPollResponse`; `OperatorInboxConsumeResponse` | mcp/src/agents_remember/models/operator_inbox.py:17-42; mcp/src/agents_remember/models/operator_inbox.py:45-52; mcp/src/agents_remember/models/operator_inbox.py:55-61 |
| Gate responses, including the combined wait helper, are strict AR-owned tool responses: `GateCreateResponse`, `LifecycleGateResponse`, `GateDecideResponse`, `GateWaitResponse`, `GateResponseWaitResponse`, and `GateListResponse`. | `GateCreateResponse`; `LifecycleGateResponse`; `GateDecideResponse`; `GateWaitResponse`; `GateResponseWaitResponse`; `GateListResponse` | mcp/src/agents_remember/models/gates.py:18-24; mcp/src/agents_remember/models/gates.py:27-33; mcp/src/agents_remember/models/gates.py:36-44; mcp/src/agents_remember/models/gates.py:47-55; mcp/src/agents_remember/models/gates.py:58-68; mcp/src/agents_remember/models/gates.py:71-75 |
| Lifecycle finalizer response registered here is a strict AR-owned tool response, `LifecycleFinalizeTaskResponse`. | `LifecycleFinalizeTaskResponse` | mcp/src/agents_remember/models/lifecycle_finalize.py:12-32 |
| Terminal responses registered here — `AttachTerminalSessionToLeafResponse`, `SpawnAgentSessionResponse`, `SessionRetireResponse`, and `SessionRenameResponse` — are strict AR-owned tool responses. | `AttachTerminalSessionToLeafResponse`; `SpawnAgentSessionResponse`; `SessionRetireResponse`; `SessionRenameResponse` | mcp/src/agents_remember/models/terminal.py:30-42; mcp/src/agents_remember/models/terminal.py:80-122; mcp/src/agents_remember/models/terminal.py:162-178; mcp/src/agents_remember/models/terminal.py:188-199 |
| `ResponseEnvelope` — the union both registries are annotated with, and the two envelope bases carrying `nextStep`/`agentNotifierBanner`. | `ResponseEnvelope` | mcp/src/agents_remember/models/base.py:98-98 |
| The suite that pins the value-set axis: `produced == declared` for each `VALID_*` frozenset, the AST scan of every literal written at a contract cell, and the guidance state-machine walk. | "class GuidanceWalkTests(unittest.TestCase):"; "class ProducedLiteralTests(unittest.TestCase):"; "class AdvertisedVocabularyTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness.py:230-294; mcp/tests/test_wire_vocabulary_exhaustiveness.py:632-817; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:45-45; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:450-450 |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

## Update History

- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: recorded `operator_inbox_supersede` →
  `OperatorInboxSupersedeResponse` in `TOOL_RESPONSE_MODELS`. Verification metadata pinned until
  closeout stamps the 260713-TES-L4 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

"- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 8 table citations and 2 prose citations for registry payloads, gate responses, terminal responses, envelopes, and test vocabulary; fixer-generated ranges verified.
- 2026-08-01T09:12+02:00 — 260731-EFA-L4 curator: body corrected on both counts an earlier review
  flagged. (1) The registry's declared value type changed from `dict[str, type[BaseModel]]` to
  `dict[str, type[ResponseEnvelope]]` (L116 and L181; `ResponseEnvelope` is the new
  `models.base` union at that file's L93-L101). The card described neither annotation. This is
  what made `ResponseModel.nextStep` and `ResponseModel.supervisorBanner` reachable by type from
  `_tool_payload` — under `BaseModel` they were not, which is how `supervisorBanner` ended up
  written into an already-dumped dict rather than declared on the envelope. (2) The two-tier
  paragraph framed the posture as one axis. `extra="forbid"` guards the FIELD set; the `Literal`
  aliases on those fields guard the VALUE set, and nothing had guarded the second — 165 of the 213
  `series-contract.md` files on disk (77.5%) made `context_packet` raise a `ValidationError`
  inside a handler with no `except` for one, across seven independent gaps, each a hand-written
  `Literal` over a vocabulary owned elsewhere. Added the third clause of the convention (a wire
  model imports the producer's alias, never retypes it), named the four models that already did
  this and the six that now do, and added the two matching invariants. Citations: the terminal
  reference row's model names gained their registry line numbers (L121/L122/L124/L125), and rows
  were added for `models/base.py` L93-L101 and for
  `test_wire_vocabulary_exhaustiveness.py`. Verification metadata pinned until closeout stamps
  the L4 commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state):
  registered `session_retire` → `SessionRetireResponse` and `session_rename` →
  `SessionRenameResponse` (both `models/terminal.py`), right after the `spawn_agent_session` row;
  `PUBLIC_TOOL_RESPONSE_MODELS` still exactly matches `PUBLIC_TOOLS` (both new tools are public).
  Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-04T12:31+02:00 - L3: registered
  `orchestration_nudge_manager` to the strict orchestration response model while
  the inbox response rows gained delivery metadata. Verification metadata pinned
  until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: registered `spawn_agent_session` → `SpawnAgentSessionResponse`
  (`models/terminal.py`), keeping the new agent-facing dispatch tool in the strict AR-owned
  response-contract path; `PUBLIC_TOOL_RESPONSE_MODELS` still exactly matches `PUBLIC_TOOLS`.
  Verification metadata pinned until closeout stamps the L2 commit.
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
