# mcp/src/agents_remember/serving/codex_app_server_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad` |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Adapts one native Codex app-server session and JSON-RPC transport to the normalized hosted adapter
contract, including cached model/effort advertisement, transient token-free catalog discovery,
settings-resolved initial configuration, and ordered same-thread model/effort switching.
The adapter no longer drops native frames: full notification/item/usage params now
ride the reserved `arEvidence` key into the bridge's evidence buffer, and the dedicated,
runtime-probed native-history reader exposes persisted threads through bounded items/turns when
accepted or an explicit legacy whole-thread path after two exact method-unavailable responses. It
implements the structural
`InterruptCapableAdapter`/`AssetSubmitCapable` seams: a native `turn/interrupt` write against the
exact active turn with replay-once, and verified `localImage` asset construction on `turn/start`.
It additionally carries each notification's native method under the reserved
`AR_EVIDENCE_METHOD_KEY` so the codex projector recognizes the 0.144.5 startup burst instead of
re-guessing it from params shape and flooding one unknown-vendor row per MCP server.
Harness sub-agents are first-class on the multiplexed app-server connection: a
bounded per-thread demux registry (`_ThreadState`) replaces the single-thread `_validate_thread`
gate, collab identity learning binds agent labels into `snapshot.raw.agentRegistry`, server-request
approvals multiplex into per-thread pending-interaction MAPS keyed by rpc id (a concurrent second
request on one thread is normal vendor traffic, never an error) projected through
`AdapterSnapshot.pending_interactions`, an unknown/experimental request METHOD is declined and
degraded on ANY thread while a known method's malformed shape keeps the agent-degrade/parent-fail
split, malformed sub-agent frames degrade to preserved raw evidence instead of failing the bridge,
the bounded event queue sheds oldest delta-method events under load (every shed counted, one
`ar/load-shed` notice on catch-up) instead of raising queue-full, and `read_native_page` gains an
optional `thread_id` selector so native history can be paged per thread.

## Code Commentary

### Logic

The adapter delegates initialize/model discovery/thread ownership to `CodexAppServerSession`.
Setters mutate only the session's desired selection: an already-effective value is `immediate`,
while a real pending change is `queued` for the next fresh `turn/start` on the existing thread.
Each submitted prompt captures its model/effort selection when reserved, so later setters cannot
rewrite earlier accepted queue work. A pending switch disables steer and queues behind an active
turn. `turn/start` promotes only `inProgress` or `completed`; `failed`/`interrupted` reject the
prompt and retain the prior effective selection plus pending fresh-turn blocker. Matching
`thread/settings/updated` is supplementary evidence, while unrelated drift fails loudly.
Launch-knob ownership, token-free discovery, interactions, events, and bounded reconciliation remain
on their existing native paths.

Evidence forwarding places the full `params` of each previously trimmed emit under the reserved
`arEvidence` raw key — consolidated through the `_emit_notification` helper cit:([`_emit_notification`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:712-728),
with the parent-thread `thread/status/changed`/`thread/settings/updated` state emits keeping their
direct path — while every pre-existing raw key (`codexMethod`, `turnId`) keeps its exact shape; the
bridge diverts the payload so no projection changes. It additionally sets
`AR_EVIDENCE_METHOD_KEY: method` inside `_emit_notification` cit:([`_emit_notification`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:712-728), which also serves
the item/completed evidence path cit:([`_handle_item_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:787-816), so the notification's native method reaches the
projector as typed evidence rather than being stripped with the trimmed event; the bridge preserves
it onto `EvidenceFrame.native_method` and strips the reserved key, keeping the redacted snapshot
byte-identical. `codexMethod` still rides for diagnostics; the method-carry key is the discriminator
the projector reads. `read_native_page` implements the
structural native-page protocol over `thread/read` with `includeTurns`: it reconnects a disconnected
session, requires the echoed thread id to match the requested one, flattens items through
`native_evidence_frames_from_thread`, and windows them with an opaque cursor; native window errors
raise as typed `CodexAppServerError`, and ephemeral threads' native `includeTurns` refusal crosses
typed with the native reason rather than a guessed page. Reconcile, submission, and interaction
behavior is byte-preserved.

`interrupt` writes one native `turn/interrupt(threadId, turnId)` against the exact active
turn: a missing active turn or a caller `turn_id` mismatching it fails typed before any write
(`expected_operation_id` is result evidence, never a guard input — the codex guard is the native
turn identity), and the write parameters use the captured active id so a completion interleaving
can never redirect the write into a successor turn. The acknowledgement is replayed once per
(turn_id-or-active, active) pair with no second native write, and an RPC failure crosses as a
`rejected` acknowledgement; the bridge stamps the epoch. `submit_with_assets` pre-verifies every
staged asset before any native write — a verification failure returns a clean `rejected` receipt
with zero `turn/start` requests — and `_turn_input` appends verified `localImage{path}` blocks
after the text block, with sha256/size re-verified at construction (`_verified_asset_path`).
Receipt raw gains additive `assetIds` only when assets ride.

The single-thread correlation maps are replaced by a per-thread demux. `CodexThreadState`
holds one thread's active turn, turn→operation bindings, unbound completions, bounded cit:([`CodexThreadState`], mcp/src/agents_remember/serving/codex_app_server_threads.py:31-66)
terminal window, and a per-thread pending-interaction MAP (`pending_interactions`, an insertion-ordered
dict keyed by rpc id, bounded at `PENDING_INTERACTIONS_PER_THREAD = 16` cit:([`PENDING_INTERACTIONS_PER_THREAD`], mcp/src/agents_remember/serving/codex_app_server_threads.py:28-28); its
`pending_interaction` property is the thread's OLDEST pending — the pre-multiplex singular
view. `self._threads` (bounded at `THREAD_REGISTRY_LIMIT = 64` cit:([`THREAD_REGISTRY_LIMIT`], mcp/src/agents_remember/serving/codex_app_server_threads.py:26-26)) is keyed by native thread id with the parent/session state registered on first use via
`CodexThreadRegistry` cit:([`CodexThreadRegistry`], mcp/src/agents_remember/serving/codex_app_server_threads.py:69-300). The old `_validate_thread` fail-on-foreign-thread gate is replaced by
`resolve` cit:([`resolve`], mcp/src/agents_remember/serving/codex_app_server_threads.py:104-140), which still fails closed on a missing or non-text `threadId` exactly as
before, but a well-formed foreign id auto-registers as an `unresolved` agent thread and is never an
error. Every notification handler demuxes first (`_handle_message` cit:([`_handle_message`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:625-644)): parent-thread
traffic keeps the pre-multiplexing snapshot/activity contract byte-identical, while sub-agent
`thread/status/changed`, `turn/started`, `thread/settings/updated`, and `turn/completed` update
only registry state plus raw evidence and never move the parent-scoped activity or settlement (D4).
Turn writes stay parent-only, so agent turn completions record `None` as the operation and never
touch `_active_operation` or the submission ledger. `learn_collab_identity` cit:([`learn_collab_identity`], mcp/src/agents_remember/serving/codex_app_server_threads.py:231-245) (now a
dispatcher over `_learn_sub_agent_activity` + `_learn_collab_tool_call`) binds
agent identity from parent-thread `collabAgentToolCall` (`receiverThreadIds`/`agentsStates`) and
`subAgentActivity` (`agentThreadId`/`agentPath`) items, and `_publish_agent_registry` cit:([`_publish_agent_registry`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:1075-1083)
mirrors the bounded registry into `snapshot.raw.agentRegistry` for the serving projector.

Server requests demux per thread and MULTIPLEX within a thread. `_handle_server_request` cit:([`_handle_server_request`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:818-890)
decides by METHOD first: an unknown/experimental request method (anything outside the
stable grammar `STABLE_SERVER_REQUESTS`) is vendor traffic, never a bridge failure — it is answered
with decline semantics (`respond_error` -32601 when the rpc id is answerable; the vendor maps an
error response to decline) and crossed as degraded preserved evidence via
`_degrade_agent_frame(..., force=True)` on ANY thread, parent included. A KNOWN stable method's
malformed shape (rpc-id type, non-object params) is a protocol violation, not traffic: it re-raises
into the message loop's agent-degrade/parent-fail split unchanged. Malformed thread identity on a
parsed request is declined when answerable, then the same split applies. The old "multiple
unresolved server requests on one thread" raise is deleted — the vendor keeps one app-global
pending map keyed by approval id, so concurrent pendings on one thread are normal traffic and
register, never raise; a full per-thread map (16) declines + degrades the NEW request, never a
bridge failure and never a silent loss of an older unanswered one; a vendor rpc-id REUSE overwrites
the older pending, which then becomes honestly unanswerable later (a JSON-RPC violation the vendor
owns). `_handle_server_request_resolved` cit:([`_handle_server_request_resolved`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:892-908) pops the pending by rpc id.
`_sync_pending_snapshot` cit:([`_sync_pending_snapshot`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:910-922) rebuilds `AdapterSnapshot.pending_interactions` from EVERY
thread's full map (agent entries carry `raw.threadId` plus the bound `agentLabel`; concurrent
parent entries beyond the oldest ride the tuple plainly), keeping the singular slot on the parent's
OLDEST pending for back-compat. `respond` cit:([`respond`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:330-353) routes by interaction id via
`interaction_thread` cit:([`interaction_thread`], mcp/src/agents_remember/serving/codex_app_server_threads.py:166-173), which returns the owning (thread, rpc id) pair — the
active-operation match is enforced only for parent-thread responses (the parent-only operation
guard). `read_native_page` cit:([`read_native_page`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:395-421)
gains an additive `thread_id` selector: `None` reads the parent thread exactly as
before, an explicit id pages that sub-agent thread through the same `thread/read` echo check.
`_handle_item_completed` cit:([`_handle_item_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:787-816) stamps agent transcripts with `raw.threadId` (parent entries
deliberately carry none, keeping the pre-multiplexing parent transcript shape byte-identical — fix-round
review finding 12), while `learn_item_thread` cit:([`learn_item_thread`, `route_delta_params`], mcp/src/agents_remember/serving/codex_app_server_threads.py:200-213; mcp/src/agents_remember/serving/codex_app_server_threads.py:215-229) + `route_delta_params`
bind thread-less delta frames (`item/.../delta`, `patchUpdated`) to their item's learned thread
without ever inventing one. `_degrade_agent_frame` cit:([`_degrade_agent_frame`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:588-623) decides every `CodexAppServerError`
the message loop catches (`_run_messages` cit:([`_run_messages`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:570-586)): only a well-formed FOREIGN threadId degrades to preserved raw evidence
with the failure noted; a missing or parent threadId re-raises and still fails the bridge — unless
`force=True` (the unknown-request-METHOD path above), which degrades on any thread. The four
white-box parent views (`_active_turn_id`, `_turn_operations`, `_unbound_completions`,
`_completed_turns` cit:([`_completed_turns`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:1079-1081)) keep the original correlation-test surface as live mappings over the
parent `_ThreadState`.

The event queue is a bounded LOAD-SHED queue, not a kill seam. `CodexEventQueue` cit:([`CodexEventQueue`], mcp/src/agents_remember/serving/codex_app_server_events.py:24-118) uses `offer` cit:([`offer`], mcp/src/agents_remember/serving/codex_app_server_events.py:59-72) and never
raises at saturation: `_evict_for_space` cit:([`_evict_for_space`], mcp/src/agents_remember/serving/codex_app_server_events.py:94-109) evicts the oldest HIGH-VOLUME delta event
first (the `_LOAD_SHED_DELTA_METHODS` set — `item/agentMessage/delta`, `item/plan/delta`,
reasoning deltas, `item/commandExecution/outputDelta`, `item/fileChange/patchUpdated`), structural
events (turns, completions, interactions, failures, the close sentinel) shed only when nothing else
remains, and every shed is counted in `_dropped_events`. `_flush_notice` cit:([`_flush_notice`], mcp/src/agents_remember/serving/codex_app_server_events.py:111-118)
mints exactly one `codex-notification` carrying `ar/load-shed` with the shed count
once the queue has room again — producer-side after an enqueue that leaves space, consumer-side in
`stream` cit:([`stream`], mcp/src/agents_remember/serving/codex_app_server_events.py:74-84) after each drained yield (a silent producer must not strand the
accounting), and always BEFORE the close sentinel (the enqueue path for `None` first makes room for
notice + sentinel, so the subscriber sees the loss account before termination). The queue limit
rose 256 → `ADAPTER_EVENT_QUEUE_LIMIT = 1024` cit:([`ADAPTER_EVENT_QUEUE_LIMIT`], mcp/src/agents_remember/serving/codex_app_server_events.py:12-12). The shed notice rides the same monotonic
sequence path as every other event, and a zero count makes the emit a no-op, so the notice itself
never recurses.

### Conventions

Acceptance is proven by correlated `turn/start`/`turn/steer` responses. A setter's `queued` result
does not claim an effective value; the fresh turn is the effect boundary. Running advertise is a
synchronous no-RPC read. Initial model/effort belongs to `thread/start`/`thread/resume` config; this
native adapter never uses the codex-acp-only `CODEX_CONFIG` environment path. Adapter identity
reports `codex-app-server:<opaque negotiated version>`. Per-thread demux state lives in one
`_ThreadState` dataclass rather than parallel adapter-level dicts; the four parent-view properties
exist only so the white-box correlation tests keep reading the original attribute names. The
singular `pending_interaction` property is a back-compat OLDEST view over the per-thread map, never
the only live pending. Sheddable queue pressure is identified by `codexMethod` membership in
`_LOAD_SHED_DELTA_METHODS`; everything else is structural and outlives deltas.

### Invariants And Boundaries

- Cold discovery performs initialize plus paginated `model/list` only: no thread and no turn.
- Running advertise uses the catalog fetched for that same connected session; it does not refetch,
  hardcode, or silently filter the selected model's effort choices.
- Adapter-owned `--model`/`-m` and `model`/`model_reasoning_effort` config selectors cannot compete
  with the normalized launch selection; the runner preflights all accepted spellings.
- The effort used for later turns and settings-update validation is the exact effort resolved while
  opening the thread, including a model-local dynamic default for a roleless session.
- Model changes rebase an unavailable desired effort to the target row's dynamic default; effort
  remains gated by the desired model's own menu.
- Prompt-before-set and set-before-prompt preserve their captured selection order. No setter
  reconnects or changes the thread id.
- Failed/interrupted fresh turns cannot promote desired settings; reversing desired back to the
  effective pair clears pending/fresh state and returns `immediate`.
- Protocol readiness and acceptance are authoritative; pane, terminal, log, ACP transport, and Toad
  hosting are not used.
- No blind resend follows an ambiguous send; retention remains bounded.
- Completion metadata does not consume durable inbox state, and queued state requires an actual
  replacement.
- Evidence payloads ride only the reserved `arEvidence` key; the adapter never merges that key into
  any projection itself and never mints `bridgeEpoch`.
- The native notification method rides the reserved `AR_EVIDENCE_METHOD_KEY` beside the `arEvidence`
  payload; the adapter only emits it and never reads or merges it — the bridge alone diverts it
  onto the frame and strips it from the republished event.
- Native pages are for persisted threads: a native refusal (e.g. ephemeral `includeTurns`) crosses
  typed with its reason instead of being retried into a less truthful shape.
- The interrupt write targets only the exact active turn (native `turnId` guard, no-active typed)
  and replays once per (expected, active) pair; it never settles the operation — settlement stays
  with the landed completion path, and a post-settlement interrupt fails typed.
- Asset bytes are re-verified (sha256/size) at construction before the native process sees a
  `localImage` path; a verification failure is a clean `rejected` receipt with zero native writes,
  and unknown/unverified native shapes are never guessed.
- The thread demux fails closed exactly like the former `_validate_thread` on a missing or non-text
  `threadId`; a well-formed foreign threadId auto-registers as `unresolved` and is never an error.
- Malformed sub-agent frames degrade to preserved raw evidence with the failure noted (the bridge
  stays ready); parent-thread shape errors still fail the bridge — `_degrade_agent_frame` is keyed
  on a well-formed FOREIGN threadId, never a blanket catch, with one explicit exception:
  `force=True` degrades an unknown/experimental server-request METHOD on ANY thread (a new vendor
  request type is traffic, not a protocol violation), while a KNOWN stable method's malformed shape
  keeps the agent-degrade/parent-fail split with no decline-and-degrade.
- Turn writes, settlement, and the submission ledger stay parent-only: agent turns carry no
  `ControlOperationRef`, record `None` as the operation, and never move the parent-scoped
  activity/acceptance (D4); a sub-agent approval likewise never moves parent activity.
- The singular `pending_interaction` slot stays the parent's OLDEST pending for back-compat; every
  thread keeps a bounded per-thread pending map (≤ `PENDING_INTERACTIONS_PER_THREAD`, keyed by rpc
  id) mirrored into `pending_interactions` (agent entries carry `threadId`/`agentLabel`; concurrent
  parent entries beyond the oldest ride the tuple plainly). Concurrent pendings on one thread are
  normal vendor traffic and never raise; a full map declines + degrades the NEWEST request without
  dropping older ones; `respond`'s active-operation guard applies to parent-thread responses only.
- The adapter event queue never raises at saturation: the oldest high-volume delta event sheds
  first, structural events (turns, completions, interactions, failures, the close sentinel) shed
  only when nothing else remains, every shed is counted, and one `ar/load-shed` notice with the
  count crosses when the consumer catches up — after a drained put, off the consumer drain, and
  always BEFORE the close sentinel.
- The thread registry (`THREAD_REGISTRY_LIMIT = 64`) and item→thread index
  (`ITEM_THREAD_INDEX_LIMIT = 1024`) are bounded; eviction never removes the parent, an
  actively-turning agent, or one holding a pending approval, and a full registry raises so the
  message loop degrades that frame to raw evidence instead of failing the bridge.
- Delta routing never invents a thread: a thread-less delta for an unknown item crosses unmodified
  on the parent/None path, and agent transcript entries carry `raw.threadId` while parent
  transcript entries stay byte-identical to the pre-multiplexing shape.

### Todos

None known for the same-thread mutation seam.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Session ownership and strict model-page parsing remain dedicated modules rather than adapter-local
policy. The multiplexing grammar lives in the control models, and a dedicated
thread-demux regression suite pins the anti-death behavior (before the demux, the first
foreign-thread notification failed the whole bridge — the 2026-07-24 production seat death) plus
the follow-on concurrency and queue-shed remediation.

| Finding | Anchor | Source |
| --- | --- | --- |
| Session keeps desired and effective settings separate, validates dynamic model-local choices, and promotes only accepted selection evidence. | `CodexAppServerSession` | mcp/src/agents_remember/serving/codex_app_server_session.py:102-458 |
| Submission evidence captures the exact model/effort pair accepted at reservation time. | `SubmissionEvidence` | mcp/src/agents_remember/serving/codex_app_server_state.py:74-80 |
| The stable server-request grammar (`STABLE_SERVER_REQUESTS`) the method-first degrade split keys on: methods outside it parse as experimental/unsupported traffic, never protocol violations. | `STABLE_SERVER_REQUESTS` | mcp/src/agents_remember/serving/codex_app_server_state.py:27-34 |
| The transport removes cancelled requests and ignores their syntactically valid late responses without retaining tombstones. | `CodexStdioTransport` | mcp/src/agents_remember/serving/codex_app_server_protocol.py:60-305 |
| The launch boundary refuses duplicate adapter-owned argv/config selectors before discovery. | `apply_launch_knobs` | mcp/src/agents_remember/serving/harness_launch.py:173-206 |
| Model pages preserve display/description metadata and model-local reasoning effort options. | `parse_model_page` | mcp/src/agents_remember/serving/codex_app_server_state.py:156-227 |
| The thread flatten helper enforces unique typed item identity for native paging. | `native_evidence_frames_from_thread` | mcp/src/agents_remember/serving/codex_app_server_state.py:378-413 |
| The multiplexing grammar this adapter fills: `AdapterSnapshot.pending_interactions` (parent slot back-compat, agent entries carry `raw.threadId`/`agentLabel`) and `EvidenceFrame.thread_id` as the demux key. | `AdapterSnapshot`, `EvidenceFrame` | mcp/src/agents_remember/models/conversations/control_wire.py:126-151; mcp/src/agents_remember/models/conversations/evidence.py:79-102 |
| The bridge extracts `threadId` from diverted evidence into `EvidenceFrame.thread_id` and forwards the additive `thread_id` native-page selector. | `native_page`, `_evidence_thread_id` | mcp/src/agents_remember/serving/harness_control_bridge.py:226-271; mcp/src/agents_remember/serving/harness_control_bridge.py:491-503 |
| Thread-demux regression tests pin the anti-death behavior (foreign-thread auto-registration, collab identity binding into `agentRegistry`, multiplexed pending interactions, parent-only settlement, degraded-never-fatal malformed agent frames) plus the remediation pins: concurrent parent pendings answered per id, the method-first degrade split, the bounded pending map, and the load-shed queue with its honest notice. | `test_spawned_subagent_traffic_never_fails_the_bridge`, `test_subagent_approval_is_multiplexed_and_answered_by_request_id`, `test_experimental_server_request_on_parent_degrades`, `test_pending_map_overflow_declines_the_newest_request`, `test_delta_flood_sheds_oldest_deltas_with_an_honest_notice` | mcp/tests/test_codex_adapter_thread_demux.py:117-180; mcp/tests/test_codex_adapter_thread_demux.py:183-221; mcp/tests/test_codex_adapter_thread_demux.py:533-568; mcp/tests/test_codex_adapter_thread_demux.py:662-697; mcp/tests/test_codex_adapter_thread_demux.py:700-761 |
| Contract tests pin the evidence round-trip, unknown-vendor pass-through, thread/read paging, and the installed 0.144.5 production-seam capture. | `test_reserved_key_round_trip_and_no_leak`, `test_unknown_vendor_pass_through_preserves_raw_without_guessing`, `test_native_page_thread_id_is_additive_over_ipc`, `test_dropped_item_and_token_usage_frames_reach_evidence_with_native_ids` | mcp/tests/test_harness_control_evidence.py:361-409; mcp/tests/test_harness_control_evidence.py:411-427; mcp/tests/test_harness_control_evidence_ipc.py:200-226; mcp/tests/test_harness_control_evidence_ipc.py:341-391 |
| The structural sub-protocols this adapter implements; the caller's identity guards ride the write. | `InterruptCapableAdapter`, `AssetSubmitCapable` | mcp/src/agents_remember/serving/harness_control_adapter.py:91-106; mcp/src/agents_remember/serving/harness_control_adapter.py:109-113 |
| The control-plane contract suite pins the interrupt write/replay/turnId guard/no-active typed refusal and the "blocks.append({\"type\": \"localImage\", \"path\": verified_asset_path(asset)})" construction with zero-write rejection. | "blocks.append({\"type\": \"localImage\", \"path\": verified_asset_path(asset)})" | mcp/src/agents_remember/serving/codex_app_server_turns.py:62-62 |
| The installed-runtime suite captures the live 0.144.5 interrupt, timeline, asset, and withdrawal-recovery evidence behind the fixture rows. | `test_live_interrupt_timeline_assets_and_recovery` | mcp/tests/test_harness_control_plane_installed.py:142-266 |
| The fixture records the redacted `control-plane/*` observed rows this adapter produced through the production seam. | "control-plane/interrupt-write-ack", "control-plane/asset-local-image-submit", "control-plane/withdrawal-recovery" | mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:95-95; mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:119-119; mcp/tests/fixtures/conversation_runtime/codex-0.144.5.json:129-129 |

## Cross-Repo References

No external repository boundary is implemented by this adapter; prior task-review artifacts are not
runtime boundary contracts.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Submission Authority Delta

Codex is now dispatch-now under the shared authority: it does not queue or steer an active turn.
Prompt/setter writes are guarded and carry the exact operation ref; native turn ids bind to that ref.
Synchronous or asynchronous terminal events share one once-only completion latch. Live correlations
and terminal dedupe are bounded, removed on completion, and keyed strongly enough that stale events
or turn-id reuse cannot release a successor.

## 260727-CHATS-IM-L2 Native-History Acquisition Delta

`read_native_page` now delegates source acquisition, opaque continuation, and response bounds to
one connection-local `CodexNativeHistoryReader` (L133-L146; L470-L496). The adapter no longer
materializes `thread/read` itself. Reconnect resets the capability probe cit:([`reset_probe`], mcp/src/agents_remember/serving/codex_app_server_history.py:126-131), so a new
process proves items/turns/legacy support independently. The selected thread id remains exact and
parent-by-default; history-method fallback is owned by the reader and requires exact `-32601`.

This section supersedes older direct-`thread/read` descriptions in this sidecar. The dormant
`conversation/library/codex.py` full-read path is outside this adapter change and remains a
separate follow-up.

## 260731-EFA-L2 Current Delta

**`StartedTurn`** (`turn_id`, `status`, `operation`, `buffered`) names what `turn/start` answered:
which turn began, in what state, for which operation — and the buffered first frame belongs with
them, because it is the notification that arrived before the response and is only interpretable
against this turn id. The four settle one submission together. The submit path is now
`_turn_start_params` → `_bind_started_turn` → (`_rejected_turn_receipt` | `_accept_started_turn`).

The single notification dispatcher was split by method into `_handle_status_changed`,
`_handle_turn_started`, `_handle_settings_notification` and `_handle_foreign_notification`, and the
item-learning branches into `_learn_sub_agent_activity` and `_learn_collab_tool_call`. Routing and
outcomes are unchanged; what changed is that each notification class is now named.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T20:49:28+02:00 — 260731-EFA-L6 curator W2-B11: repaired 54 citation findings in this card (13 citation_anchor_missing, 28 citation_prose_not_in_cit_form, 13 citation_source_malformed) with exact current anchors and source paths; scoped memory-citations recheck PASS with 0 findings.

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived 3 stale self-citations left behind by
  the same leaf's `StartedTurn` submit split and per-method handler split, which grew the file to
  1503 lines. `_learn_collab_identity` is L1385-L1450 (the dispatcher plus the two extracted
  learners the sentence describes), `_publish_agent_registry` is L1452-L1468, and
  `_degrade_agent_frame` cit:([`_degrade_agent_frame`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:588-623) — the catch itself lives in `_run_messages` cit:([`_run_messages`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:570-586), so
  that sentence now names the caller instead of implying the helper holds the `except`.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `StartedTurn` and the per-method notification handler / item-learning split.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: replaced the direct whole-thread history
  description with the connection-local, runtime-probed history reader; recorded reconnect probe
  reset, exact thread selection, opaque continuation ownership, explicit legacy fallback, and the
  separate dormant library exposure. Verification metadata stays pinned because the change is
  uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: documented the two closed kill seams and the
  degrade rework. (1) Concurrent server requests: `_ThreadState.pending_interactions` is now a
  bounded per-thread MAP keyed by rpc id (≤16; the `pending_interaction` property is the
  oldest/back-compat view) and the "multiple unresolved server requests" raise is deleted —
  concurrency is normal vendor traffic; `_handle_server_request` decides by METHOD first
  (unknown/experimental methods declined -32601 + degraded on ANY thread via
  `_degrade_agent_frame(force=True)`; KNOWN stable methods' malformed shapes keep the
  agent-degrade/parent-fail split; a full map declines + degrades the newest request);
  `serverRequest/resolved` pops by rpc id; `respond`/`_interaction_thread` route by (thread, rpc
  id); `_sync_pending_snapshot` projects ALL pendings with the singular slot on the parent's
  oldest. (2) The event queue no longer raises queue-full: `_enqueue`/`_evict_for_space` shed the
  oldest delta-method events first (structural events survive until nothing else remains), count
  every shed, and mint one `ar/load-shed` notice with the count on catch-up (producer-side, off the
  consumer drain in `_event_stream`, and before the close sentinel); the limit rose 256 → 1024.
  Re-anchored every stale line citation against the post-remediation source (the file grew to 1376
  lines) and extended the demux-suite row cit:([`test_spawned_subagent_traffic_never_fails_the_bridge`], mcp/tests/test_codex_adapter_thread_demux.py:117-180). Verification metadata stays pinned — the
  change is uncommitted, so no commit hash can attest it.
- 2026-07-26T15:35 — 260718-CHATS-L7 curator: documented the per-thread demux — `_ThreadState` +
  bounded thread registry replacing the deleted `_validate_thread` gate (foreign ids auto-register,
  missing/non-text ids still fail closed), collab identity learning into `snapshot.raw.agentRegistry`,
  multiplexed `pending_interactions` with the parent-only operation guard on `respond`, per-thread
  `read_native_page(thread_id=...)`, agent-transcript `threadId` stamping with byte-identical parent
  entries, item→thread delta routing, bounded eviction, and degrade-not-fatal malformed agent frames.
  Fixed stale emit-site citations (`_emit_notification` cit:([`_emit_notification`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:712-728) +
  `_handle_item_completed` cit:([`_handle_item_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:787-816), refreshed the protocol-cancellation (`CodexStdioTransport` cit:([`CodexStdioTransport`], mcp/src/agents_remember/serving/codex_app_server_protocol.py:60-305)) and
  launch-refusal (`apply_launch_knobs` cit:([`apply_launch_knobs`], mcp/src/agents_remember/serving/harness_launch.py:173-206)) citations, and added rows for the models grammar and the
  `test_codex_adapter_thread_demux.py` regression suite. Verification metadata stays pinned: the L7
  change is uncommitted, so no commit hash can attest it.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: R1 — documented the native-method carry: the
  `codex-notification`/`item/completed` emits cit:([`_emit_notification`, `_handle_item_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:712-728; mcp/src/agents_remember/serving/codex_app_server_adapter.py:787-816) now set
  `AR_EVIDENCE_METHOD_KEY: method` so the codex projector recognizes the 0.144.5 startup burst by
  method instead of re-guessing from params shape; added the emit-only invariant. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the `InterruptCapableAdapter`
  implementation (native `turn/interrupt` on the exact active turn, no-active/mismatch typed,
  replay-once per pair, RPC failure → `rejected` acknowledgement) and the `AssetSubmitCapable`
  implementation (pre-verified `localImage{path}` blocks on `turn/start`, construction-time
  sha256 re-verification, additive receipt `assetIds`, zero native writes on verification
  failure). Verification metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented stop-dropping `arEvidence`
  forwarding at the six emit sites and the `thread/read`-backed `read_native_page` with thread-id
  echo check, duplicate-id fail-closed, and typed ephemeral `includeTurns` refusal. Verification
  metadata stays pinned until closeout stamps the candidate commit.
- 2026-07-17T21:39+02:00 — FEUI-L5: replaced adapter-queue/steer semantics with guarded fresh-turn
  dispatch, exact turn-operation binding, once-only completion, and bounded correlation maps.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented desired/pending/effective settings,
  next-fresh-turn application, captured prompt selection epochs, failed-turn non-promotion,
  model-local effort rebasing, reversal collapse, and same-thread/no-reconnect switching.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented native thread config launch knobs,
  adapter-owned selector refusal, roleless model-local defaults, and reuse of the resolved effort
  for subsequent turns and settings-update evidence.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented harness-id validation,
  initialize/list-only discovery, and cached same-session advertise while preserving correlated
  delivery, boundedness, and inbox-consumption boundaries.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented null-requestId/vendor-correlation completion,
  loud correlation validation, terminal idle/immediate projection, and replacement-only queued state.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented structured Codex identity and negotiated adapter
  reporting; exact versions remain fixture/smoke baselines only.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for normalized Codex
  lifecycle, correlated acceptance, busy policy, approvals, reconnect, and no-cutover boundary.
  Verification remains unset until closeout stamps the code commit.
