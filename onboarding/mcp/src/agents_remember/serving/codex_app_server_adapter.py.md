# mcp/src/agents_remember/serving/codex_app_server_adapter.py

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

Parent-turn completion carries both correlation domains in one terminal transcript entry:
`requestId` is the exact `ControlOperationRef.operation_id` owned by the durable submission, while
`vendorCorrelationId` is the Codex turn id cit:([`_handle_turn_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:780-836). This lets a prompt whose initial
receipt was honestly `queued` converge onto its exact inbox row when the turn completes; completion
does not depend on text matching or retroactive vendor-id guessing. Foreign/sub-agent completions
remain operation-free and therefore do not acquire a durable inbox request identity.

Evidence forwarding places the full `params` of each previously trimmed emit under the reserved
`arEvidence` raw key — consolidated through the `_emit_notification` helper cit:([`_emit_notification`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:762-778),
with the parent-thread `thread/status/changed`/`thread/settings/updated` state emits keeping their
direct path — while every pre-existing raw key (`codexMethod`, `turnId`) keeps its exact shape; the
bridge diverts the payload so no projection changes. It additionally sets
`AR_EVIDENCE_METHOD_KEY: method` inside `_emit_notification` cit:([`_emit_notification`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:762-778), which also serves
the item/completed evidence path cit:([`_handle_item_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:838-867), so the notification's native method reaches the
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
error. Every notification handler demuxes first (`_handle_message` cit:([`_handle_message`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:675-694)): parent-thread
traffic keeps the pre-multiplexing snapshot/activity contract byte-identical, while sub-agent
`thread/status/changed`, `turn/started`, `thread/settings/updated`, and `turn/completed` update
only registry state plus raw evidence and never move the parent-scoped activity or settlement (D4).
Turn writes stay parent-only, so agent turn completions record `None` as the operation and never
touch `_active_operation` or the submission ledger. `learn_collab_identity` cit:([`learn_collab_identity`], mcp/src/agents_remember/serving/codex_app_server_threads.py:231-245) (now a
dispatcher over `_learn_sub_agent_activity` + `_learn_collab_tool_call`) binds
agent identity from parent-thread `collabAgentToolCall` (`receiverThreadIds`/`agentsStates`) and
`subAgentActivity` (`agentThreadId`/`agentPath`) items, and `_publish_agent_registry` cit:([`_publish_agent_registry`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:1126-1134)
mirrors the bounded registry into `snapshot.raw.agentRegistry` for the serving projector.

Server requests demux per thread and MULTIPLEX within a thread. `_handle_server_request` cit:([`_handle_server_request`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:869-941)
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
owns). `_handle_server_request_resolved` cit:([`_handle_server_request_resolved`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:943-959) pops the pending by rpc id.
`_sync_pending_snapshot` cit:([`_sync_pending_snapshot`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:961-973) rebuilds `AdapterSnapshot.pending_interactions` from EVERY
thread's full map (agent entries carry `raw.threadId` plus the bound `agentLabel`; concurrent
parent entries beyond the oldest ride the tuple plainly), keeping the singular slot on the parent's
OLDEST pending for back-compat. `respond` cit:([`respond`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:376-403) routes by interaction id via
`interaction_thread` cit:([`interaction_thread`], mcp/src/agents_remember/serving/codex_app_server_threads.py:166-173), which returns the owning (thread, rpc id) pair — the
active-operation match is enforced only for parent-thread responses (the parent-only operation
guard). `read_native_page` cit:([`read_native_page`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:445-471)
gains an additive `thread_id` selector: `None` reads the parent thread exactly as
before, an explicit id pages that sub-agent thread through the same `thread/read` echo check.
`_handle_item_completed` cit:([`_handle_item_completed`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:838-867) stamps agent transcripts with `raw.threadId` (parent entries
deliberately carry none, keeping the pre-multiplexing parent transcript shape byte-identical — fix-round
review finding 12), while `learn_item_thread` cit:([`learn_item_thread`, `route_delta_params`], mcp/src/agents_remember/serving/codex_app_server_threads.py:200-213; mcp/src/agents_remember/serving/codex_app_server_threads.py:215-229) + `route_delta_params`
bind thread-less delta frames (`item/.../delta`, `patchUpdated`) to their item's learned thread
without ever inventing one. `_degrade_agent_frame` cit:([`_degrade_agent_frame`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:638-673) decides every `CodexAppServerError`
the message loop catches (`_run_messages` cit:([`_run_messages`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:620-636)): only a well-formed FOREIGN threadId degrades to preserved raw evidence
with the failure noted; a missing or parent threadId re-raises and still fails the bridge — unless
`force=True` (the unknown-request-METHOD path above), which degrades on any thread. The four
white-box parent views (`_active_turn_id`, `_turn_operations`, `_unbound_completions`,
`_completed_turns` cit:([`_completed_turns`], mcp/src/agents_remember/serving/codex_app_server_adapter.py:1122-1124)) keep the original correlation-test surface as live mappings over the
parent `_ThreadState`.

The event queue is a bounded LOAD-SHED queue, not a kill seam. `CodexEventQueue` cit:([`CodexEventQueue`], mcp/src/agents_remember/serving/codex_app_server_events.py:26-120) uses `offer` cit:([`offer`], mcp/src/agents_remember/serving/codex_app_server_events.py:61-74) and never
raises at saturation: `_evict_for_space` cit:([`_evict_for_space`], mcp/src/agents_remember/serving/codex_app_server_events.py:96-111) evicts the oldest HIGH-VOLUME delta event
first (the `_LOAD_SHED_DELTA_METHODS` set — `item/agentMessage/delta`, `item/plan/delta`,
reasoning deltas, `item/commandExecution/outputDelta`, `item/fileChange/patchUpdated`), structural
events (turns, completions, interactions, failures, the close sentinel) shed only when nothing else
remains, and every shed is counted in `_dropped_events`. `_flush_notice` cit:([`_flush_notice`], mcp/src/agents_remember/serving/codex_app_server_events.py:113-120)
mints exactly one `codex-notification` carrying `ar/load-shed` with the shed count
once the queue has room again — producer-side after an enqueue that leaves space, consumer-side in
`stream` cit:([`stream`], mcp/src/agents_remember/serving/codex_app_server_events.py:76-86) after each drained yield (a silent producer must not strand the
accounting), and always BEFORE the close sentinel (the enqueue path for `None` first makes room for
notice + sentinel, so the subscriber sees the loss account before termination). The queue limit
rose 256 → `ADAPTER_EVENT_QUEUE_LIMIT = 1024` cit:([`ADAPTER_EVENT_QUEUE_LIMIT`], mcp/src/agents_remember/serving/codex_app_server_events.py:12-12). The shed notice rides the same monotonic
sequence path as every other event, and a zero count makes the emit a no-op, so the notice itself
never recurses.

Structurally spawned role sessions now cross one additional startup gate after the native thread is
opened and before the adapter handshake becomes ready: `_role_mcp_readiness` asks the canonical
`codex_mcp_readiness` API for a connected configured server advertising exact `dispatch_agent`.
Roleless sessions retain their existing path. A refusal stops the half-open session; if cleanup also
fails, that secondary failure is attached as a note and cannot mask the original readiness error.

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

- A role session is never advertised ready until its native app-server MCP inventory contains one
  connected `dispatch_agent`; there is no name fallback or alternate discovery path, and startup
  cleanup never hides the refusal that caused it.

### Todos

None known for the same-thread mutation seam.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

No configured domain documentation could be checked.

### Repo-Internal References

Session ownership and strict model-page parsing remain dedicated modules rather than adapter-local
policy. The multiplexing grammar lives in the control models, and a dedicated
thread-demux regression suite pins the anti-death behavior (before the demux, the first
foreign-thread notification failed the whole bridge — the 2026-07-24 production seat death) plus
the follow-on concurrency and queue-shed remediation.

- Session keeps desired and effective settings separate, validates dynamic model-local choices, and promotes only accepted selection evidence. [1]
- Submission evidence captures the exact model/effort pair accepted at reservation time. [2]
- The stable server-request grammar (`STABLE_SERVER_REQUESTS`) the method-first degrade split keys on: methods outside it parse as experimental/unsupported traffic, never protocol violations. [3]
- The transport removes cancelled requests and ignores their syntactically valid late responses without retaining tombstones. [4]
- The launch boundary refuses duplicate adapter-owned argv/config selectors before discovery. [5]
- Model pages preserve display/description metadata and model-local reasoning effort options. [6]
- The thread flatten helper enforces unique typed item identity for native paging. [7]
- The multiplexing grammar this adapter fills: `AdapterSnapshot.pending_interactions` (parent slot back-compat, agent entries carry `raw.threadId`/`agentLabel`) and `EvidenceFrame.thread_id` as the demux key. [8]
- The bridge extracts `threadId` from diverted evidence into `EvidenceFrame.thread_id` and forwards the additive `thread_id` native-page selector. [9]


| The structural sub-protocols this adapter implements; the caller's identity guards ride the write. | `InterruptCapableAdapter`, `AssetSubmitCapable` | mcp/src/agents_remember/serving/harness_control_adapter.py:91-106; mcp/src/agents_remember/serving/harness_control_adapter.py:109-113 |
| The control-plane contract suite pins the interrupt write/replay/turnId guard/no-active typed refusal and the "blocks.append({\"type\": \"localImage\", \"path\": verified_asset_path(asset)})" construction with zero-write rejection. | "blocks.append({\"type\": \"localImage\", \"path\": verified_asset_path(asset)})" | mcp/src/agents_remember/serving/codex_app_server_turns.py:62-62 |
| Historical evidence (retired with the d3610903 suite reduction): The installed-runtime suite captures the live 0.144.5 interrupt, timeline, asset, and withdrawal-recovery evidence behind the fixture rows. These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |
| Historical evidence (retired with the d3610903 suite reduction): The fixture recorded the redacted `control-plane/*` observed rows this adapter produced through the production seam. These removed artifacts provide no current execution or capability-enablement proof. | N/A | N/A |

### Cross-Repo References

No external repository boundary is implemented by this adapter; prior task-review artifacts are not
runtime boundary contracts.

No meaningful cross-repo references found.

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
