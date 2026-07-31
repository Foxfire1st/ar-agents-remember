# mcp/src/agents_remember/serving/ — Dashboard Serving Layer Overview

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| sourceRoute            | `mcp/src/agents_remember/serving/`               |
| doc_type               | `route-local-overview`                           |
| lastUpdated            | 2026-07-31T04:28+02:00 |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7`|
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../../overview.md`                         |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

### Current Runtime-Truth Repair

The serving boundary exposes a packaged dashboard fingerprint without fabricating one when the
artifact is absent. Since 260731-EFA-L1 that absence is **routine rather than exceptional**: the
cockpit bundle and its `dashboard.fingerprint` sidecar are generated at release time and are not in
version control, so a source checkout serves no cockpit and reports no `dashboardBuild`. Both
absences are answered honestly — a 503 naming the build command at `/`, and an omitted key on the
wire — never with a placeholder page or a fabricated identity. The boundary also sends revalidation
policy only on successful HTML, and keeps pre-session harness
discovery to `id`/`name`/`detected`. Raw event cursors realign to server-owned record boundaries and
advance past malformed, undecodable, blank, heartbeat, and non-object records; accepted top-level
objects are parsed once and reused by SSE. Dashboard-owned tmux clients strip inherited tmux
identity and force the browser PTY grammar while preserving unrelated environment settings.

### Current Folded-State Stream Repair

The state SSE channel now has one projector-owned activation and publication contract.
`Projector.subscribe()` registers a queue before capturing current authority, so a concurrent
projection is either in that snapshot or in the registered queue. `_publish_projection()` computes
the event batch, commits stable/current state, then notifies subscribers; the first successful tick
after failed `prime()` emits one full snapshot, an identical recovered state emits nothing, and
later changes use ordinary named deltas. `app.stream_events()` only decorates/serializes that stream
and explicitly closes the subscription on disconnect or cancellation.

### Current Structured-Conversation Contract

`serving/conversation/` is the protocol-neutral contract roof for the future
Chats interface. Strict Pydantic wire models normalize harness identity, active transcript/event
pages, independent active/library cursor scopes, evidence-backed status and capabilities,
operation queue/withdrawal recovery, attachments, and telemetry without claiming that native
history/control implementations or a renderer already exist. Exactly two read ports define the
active and library seams. Three behavior-empty owned child routers (`active`, `library`, `control`)
compose under one root router, registered exactly once by `harness_control_api.py`, so later leaves
can add behavior without restructuring the serving route.

The missing production composition boundary under that roof is repaired: the same
single registration now constructs and installs one immutable app-scoped `ConversationRuntime`
(scope, terminal catalog/host, effective harness registry, liveness clock/config, capability
evidence, and a server-resolved local-operator authorization resolver) on `app.state` exactly
once. Child leaves consume it through two narrow request dependencies and never edit
`conversation/router.py`, `harness_control_api.py`, or `app.py` again. Authorization is the
server-resolved local single-user ruling: loopback-only at request time, no browser-supplied
principal/tenant channel, fail closed otherwise.

The active child is implemented inside its owned seam as
`serving/conversation/active/` plus the per-harness mapper grammars in
`serving/conversation/projectors/`: three registered production wires (authorized native-hydrated
page, selected-child history, and resumable SSE events) behind the shared composition,
HMAC-signed purpose-branded
page/event cursors re-bound against the authorized identity on every wire, a per-app service
holding a bounded reconstructable-projector LRU, per-session engines that hydrate from native
authority (codex persisted-thread pages, pi durable entries, the bounded live evidence window —
never the flattened transcript deque) and mint totally ordered envelopes with one typed gap per
established-stream failure class, an idempotent projection store whose tool-call upserts union
blocks by `block_id`, the canonical `ConversationStatusService` whose one evidence
classification both Chats and orchestration consume (`hosted_control_projection.snapshot_turn_state`
now delegates to it), and fixture-gated per-session capabilities (claude honestly `unverified`
for a never-probed contract reason — THE CONTRACT IS THE ONLY GATE and
no version-string comparison demotes any capability, so the prior "installed 2.1.214 vs locked
2.1.211" version demotion is removed; codex historical tool loss visible). The shared
composition, router, wire grammar, and library/control shells are untouched; the slices are
governed by `conversation/active/overview.md` and `conversation/projectors/overview.md`.

The library child is implemented inside its owned seam as
`serving/conversation/library/`: authorized dormant native list/read routes over each normalized
harness's catalog/history (Codex direct app-server, Claude/Pi through the repository-locked Node
helpers), live production-path capability gates cached per installed-executable fingerprint, a
per-app HMAC-signed cursor/key authority with content-derived catalog generations, narrow-only
canonical project scope, and an idempotent exact open/status/reconcile service that launches a
NEW tracked session through the existing opener (codex through the additive
`resume_thread_id` channel), proves exact catalog identity, and retires record-spawned failures
honestly. The shared composition, router, and wire grammar are untouched; the slice is governed
by `conversation/library/overview.md`.

The control child is implemented inside its owned seam as
`serving/conversation/control/`, filling the last behavior-empty conversation router: seventeen
registered routes for exact-turn interrupt (idempotent request/status/reconcile, acknowledgement
never equal to settlement), the complete source-aware never-bodies operation queue with cockpit-only
withdrawal and a bounded authorization-bound 900 s recovery lease, typed attachment stage/rebind/
submit through the control-plane asset channel into a confined 0700/0600 spool, read-only effective policy with
no mutation surface, and evidence-bound telemetry (codex cumulative token usage). Opaque control
references are HMAC-signed, purpose-branded, and re-bound per wire; a per-app control service holds
bounded per-(session, epoch) ledgers with per-session serialization above the control-plane replay cache; the
pi settlement reads the clip-preserved evidence terminal identity. It consumes the closed
control-plane substrate (native interrupt write, paged never-bodies operation timeline, asset
channel, pre-tombstone recovery payload) read-only and touches neither the shared composition, the
router, nor the wire grammar; the slice is governed by `conversation/control/overview.md`.

### Current Hosted-Session Contract

The current hosted-session serving contract is protocol-backed: exact adapter snapshots govern
readiness, liveness/activity, delivery evidence, interactions, and terminal projection. Durable
operator-inbox rows are the only inter-agent message roots; the adapter is only their delivery wire,
and explicit recipient `consume` is the sole acknowledgement. Pane text, terminal logs, copy mode,
paste echoes, and timing windows are diagnostic-only and cannot authorize readiness, delivery,
completion, or supervisor action. The older pane/log/paste descriptions retained below are historical
route history, not current authority.

**`HarnessSubmissionAuthority` is the sole epoch-bound prompt/setter
timeline.** It owns prompt FIFO, immutable id/source/payload admission, atomic queued-withdraw versus
dispatch claim, exact full-operation-ref completion, early-terminal dominance, response bypass,
raw-free cockpit status, and bounded privacy-aware retention. `HarnessControlQueue` is now only a
compatibility facade. Codex, Claude, and Pi are dispatch-now adapters with guarded first-byte seams;
none may create a native/adapter queue or release work by FIFO/id alone.

**The additive, read-only native evidence and resume substrate.** Mappers
place full native frames under the single reserved `arEvidence` raw key on events they already emit;
the bridge diverts each payload at its one `_run_events` consumption point into a bounded
per-session evidence deque (2,000 frames, 32 KiB clip with a visible marker, monotonic adapter-event
sequence, honest eviction floor) and reduces/publishes the redacted event, so `snapshot.raw`,
catalog `control_raw`, SSE projections, and every existing consumer stay byte-identical. Three
additive IPC reads cross only the user-private socket: `evidence` (deque-domain page),
`evidence-native-page` (native-domain page with typed identity and an opaque `nextCursor`, codex
`thread/read` and pi `get_entries(since)`; claude fails closed typed), and `submission-provenance`
(epoch-checked batch over all three sources through the sole bridge → queue → authority delegation).
Every evidence response carries `bridgeEpoch`, the two coordinate domains are disjoint and rejected
cross-typed, and the validated client enforces monotonicity, continuation coherence, and exact
counts. The codex-only `resume_thread_id` channel rides opener → `RunnerConfig` payload → factory
kwarg → the sole `CodexAppServerSettings` site, refusing non-codex or malformed values before any
spawn. No existing action, DTO, consumer, deque, or snapshot reduction changed shape; unknown
native shapes cross as unknown-vendor evidence with raw preserved and semantics never guessed.

**The additive native control-plane substrate lands inside the same family.** A
native interrupt write rides a runtime-checkable structural `InterruptCapableAdapter` sub-protocol
(base protocol byte-compatible): the bridge dispatch is epoch-guarded and bridge-stamped
(adapter-mint epochs refused), codex writes `turn/interrupt` against the exact active turn with
its native `turnId` guard, pi writes RPC `abort` guarded pre-write by the caller's expected
active-operation identity, both replay the first acknowledgement once per (expected, active) pair,
claude/unsupported fail closed typed naming the adapter, and settlement stays with the landed
completion path (a pi aborted turn's content-less `message_end` now crosses evidence-only instead
of killing the bridge). The operation timeline is a paged never-bodies enumeration of the
authority's retained ledger — all three prompt sources plus set-model/set-effort identity under a
page count cap and the shared 48 KiB-class budget, every page carrying `latestSequence`,
`evictedBeforeSequence` (tracked at the sole pop site), `truncated`, and `bridgeEpoch`, with
completeness as the union of pages and an epoch flip failing typed at the validated client; the
delegation runs authority → queue → bridge → IPC → validated client exactly like the evidence provenance reads.
The asset channel rides submit with references only: schema validation, resolve-and-verify
confinement under the request-independent `<endpoint-root>/assets` anchor (lexical
separator/dot-segment ban, ≤255-byte components, NUL translated to a typed refusal), size/sha256
verification at admission and re-verification at native construction (codex `localImage{path}`,
pi base64 `images[]`), an asset-conditional idempotence digest extension (asset-free digests
byte-identical), an `unsupported` terminal receipt on non-capable adapters, and additive receipt
`assetIds`. Withdrawal recovery captures the exact pre-tombstone body once inside the already
`cockpit_only` response at the true transition; replays carry none and the tombstone timing/class
is byte-preserved. Two additive IPC actions (`interrupt`, `operation-timeline`) keep the protocol
at `ar-harness-control/v1` (now 20 actions); daemon-side bounded recovery retention stays the control
child's obligation.

`serving/` is the **local dashboard serving layer** (slice 04 of the 3.0
browser-dashboard series): a FastAPI app over the observer projection read side. It
is **transport only** — it adds no interpretation (the reducer owns that) and reads
coordination state exclusively through `McpRuntimeConfig` + `observer.paths`
(North-Star #5), never raw host paths. It serves `project_and_write`'s
`WorkspaceProjection` live over SSE, tails the raw observer event log, ships the static
cockpit bundle, opens the POST action return-channel (targeted gate decisions are
developer-attributed and binding), and hosts the Mode B2 terminal backend
(`terminal.py` — tmux-wrapped PTY sessions, slice 6d-1) bridged to the browser over the
`@app.websocket("/api/terminal/{session}")` WebSocket (slice 6d-2); a `POST /api/terminal/{session}`
opener + `GET /api/harnesses` let the dashboard spawn + own a shell or a detected harness (slices
6e-2a/6e-2b, the `harnesses.py` registry). `POST /api/operator-inbox` is the trusted
developer/dashboard write side for durable inbox messages; a queued row can be pushed immediately into a
matching hosted session through the shared terminal paster while keeping the row pollable.
`POST /api/operator-inbox/{entry_id}/dismiss` is the delete path
for stale task-row pickup warnings. `terminal_catalog.py` provides the durable terminal-session
surface: opener rows persist under `logs/dashboard/terminal-sessions.json`, `/api/terminal/sessions`
hydrates the UI after refresh, the opener creates detached tmux sessions, each WebSocket gets its own
tmux client only after a tmux probe, and explicit terminate kills tmux and hides the row from normal
lists. `terminal_leaf_assignment.py` is the shared catalog move policy used by both
`POST /api/terminal/{session}/attach-leaf` and the agent-facing MCP tool so hosted chats can move between
durable leaves without respawn. `leaf_ref_validation.py` is the serving adapter that normalizes
terminal opener/attach leaf keys to canonical qualified task-doc ids before catalog mutation. `terminal_opener.py` is the shared
hosted-session **opener** (leaf claim + env-seeded tmux ensure + catalog upsert) that both the
`POST /api/terminal/{session}` route and the agent-facing `spawn_agent_session` MCP tool compose over so
there is **no parallel spawn path** — and `terminal_paste.py`, the server-side capture-verified stdin
paste (success only after the pane provably shows the paste; one origin baseline per
delivery makes duplicate stacking impossible; failures ship the pane capture) that backs the
`POST /api/terminal/{session}/paste` endpoint and the tool's context delivery. `terminal.py`
gains an `env` knob-injection seam (`tmux new-session -e KEY=VALUE`) and `terminal_catalog.py` gains
spawned-by provenance columns for the orchestration tree (`spawn_role` beside them —
written only when AR_SPAWN_ROLE is set, preserved on re-open, riding the sessions wire for the
chats command tree). Run via
`agents-remember dashboard` (the `cli/` umbrella); `--sim` replays a recorded fixture
through the byte-identical path. The seat-lifecycle surface (issues #12/#4):
`POST /api/terminal/{session}/retire` and `POST /api/terminal/{session}/rename` — server-authoritative
retirement (kill tmux + a retirement-provenance mark layered on the existing `terminated` status,
authority enforced via `retire_policy.check_retire_authority`: owner-never-self-retires, a manager
retires only worker/reviewer seats of its own master, the orchestrator retires anything) and
post-spawn identity rename (`spawned_label` freezes the original label on first rename, identity
text only, `spawn_role` never changes). Live turn-state (`working`/`turn-ended`/`awaiting-input`/
`stale`) rides the EXISTING `terminal_liveness.py` alive-probe sweep — no new hot loop — classifying
harness rows from the same `terminal_paste.capture_pane` history-inclusive pane view paste
verification already uses, and firing `seat_events.py` observer events (`seat.retired`/
`seat.renamed`/`seat.turn-state-changed`) only on an actual transition. Landed/archive classification
replaces normal completion cleanup: successful integrate/finalize marks
matching seats `status:"landed"` via `landing.py` + `seat.landed`, keeps them visible/inspectable in
the dashboard, and leaves manual retire as the explicit terminating path for stuck/abandoned/duplicate
or harmful seats; `POST /api/terminal/landed-cleanup` closes only rows still marked landed and reports
closed/skipped counts. The
**deterministic supervisor sweep** (P-15 tiers 1+2, "the model is never the polling layer"): a
third decoupled-cadence lifespan task (`supervisor.py::run_supervisor_sweep`, default ~10s,
settings-controlled) that reads `TerminalCatalog`/`OperatorInboxStore`/`ExpectationRowStore`/the
nudge store DIRECTLY (never the projection), evaluates five mechanical predicates — pane-state
(new `pane_signals.py`), expectation-deadline expiry, turn-report staleness (`missing_artifact()`
gets its first caller), unacked-row redelivery, and seat-liveness (the liveness/turn-state join with graceful
degradation) — and acts: redeliver via the shared injector, auto-nudge, owner-addressed signal-emit, or
hand off to the escalation ladder's reserved stub, logging every action as an
`orchestration.supervisor.*` observer event. New `supervisor_heartbeat.py` gives the sweep its own
self-liveness tick row (issue #15, "the watcher must be code AND watched"), surfaced as a fail-loud
MCP-tool banner (`mcp/tools/base.py`) and a dashboard header badge (`/api/state`/SSE).
The escalation ladder fills that reserved stub: `supervisor.py` gains two more predicates
(`evaluate_escalation_findings`/`evaluate_dead_upstream_findings`) and two more actions
(`_escalate_rung`/`_signal_dead_upstream`), calling through the new
`controlplane/escalation_ladder.py` walker (governed by the `controlplane/` overview) for rung
decisions and `controlplane/signal_routing.py`'s new two-hop `derive_skip_level_owner`/`is_seat_dead`
for skip-level/grandparent addressing. Past the respawn threshold, `_escalate_rung` calls new
`_respawn_suspect`: retires the suspect seat's husk via `serving/retire.py::retire_entry`,
re-delivers its pending inbox queue to the successor via the signal payload, and — when the retired
seat was a manager — surfaces its still-running workers (new `controlplane/orphan_policy.py::
find_orphaned_workers`) as orphans in the same respawn event, never auto re-parenting them or
absorbing the dead manager's role. No new hot loop, no new `InboxMessageKind` values — rung 1 reuses
`nudge`, rung 2/3/respawn/dead-upstream reuse `escalation`, distinguishable via the dedicated
`orchestration.escalation.rung`/`.respawn`/`.dead-upstream` events.
The supervisor keeps its observation cadence independent from its delivery/escalation
cadence: `supervisor.py` passes the redelivery floor into hosted delivery, checks the new
`controlplane/supervisor_signals.py` cooldown store before repeated pane/seat-liveness owner signals,
and skips `pane-signal: mid-turn` as busy-state noise. `app.py` wires the new store plus
`settings.supervisor.signal_cooldown_seconds` into `SupervisorContext`; `inbox_delivery.py` threads
the redelivery floor into every stored delivery snapshot.
The supervisor is chain-aware and manager-first: stale expectation/report/
seat/inbox/escalation predicates defer when the same leaf chain has progressed; nudge, signal, and
dead-upstream actions resolve the current responsible manager; one row can transition at most once per
sweep; and completion/artifact posts are readdressed and hosted-delivered to the current manager.
Unbound reviewer/curator progress is credited in the subject worktree; unbound worker active-phase
credit remains an accepted follow-up.

Release-tail hardening covers the same supervisor path: delivery-failure inbox rows whose
delivery state is `"no-hosted-session"` or `"unconfirmed"` stay in the redelivery domain until
`PERSISTENT_FAILURE_ATTEMPTS` or `escalatedAt`; the generic unacked escalation ladder skips them
until then, so hosted-delivery failures do not escalate before the persistent redelivery threshold.

## Hot Path Summary

For the active conversation serving, start at
`conversation/active/api.py` (page/events plus selected-child history and the O4 error ladder), then
`conversation/active/service.py` (epoch/cursor checks, atomic page+cursor),
`conversation/active/projector.py` (hydration, polls, echo zipper, gap mechanics),
`conversation/active/store.py` (idempotence, tool block union),
`conversation/active/cursor.py` (signed cursor authority), and
`conversation/active/status.py` (the canonical classification orchestration shares). The
per-harness grammars live in `conversation/projectors/{codex,claude,pi}.py`; the four focused
suites pin the slice, the API suite over a real socket.

For the native conversation library, start at
`conversation/library/api.py` (five routes plus the O4 error-status ladder), then
`conversation/library/service.py` (per-call re-authorization),
`conversation/library/open_service.py` (idempotent exact open and bounded ledger),
`conversation/library/cursor.py` (signed token authority), `conversation/library/gates.py`
(live capability gates), and the three dormant ports `conversation/library/codex.py`,
`claude.py`, `pi.py` with `helper_host.py` for the locked Node helpers. The six focused suites
plus the installed-runtime suite pin the slice.

For the native evidence and resume substrate, start at
`harness_control_bridge.py::_run_events` (the single diversion point) and
`harness_control_models.py` (evidence DTOs, reserved key, clip/window helpers), then the three IPC
actions in `harness_control_ipc.py` and the validated reads in `harness_control_client.py`.
Per-harness forwarding lives in `codex_app_server_adapter.py`, `claude_stream_state.py`, and
`pi_rpc_events.py`; native pages in the codex/pi adapters; provenance in
`harness_submission_authority.py`; the resume channel runs `terminal_opener.py` →
`harness_control_runner.py` → `harness_control_factories.py`. `test_harness_control_evidence.py`
pins the whole seam.

For the native control-plane substrate, start at
`harness_control_bridge.py::interrupt` (epoch guard, structural dispatch, bridge-stamped epoch),
then the adapter writes `codex_app_server_adapter.py::interrupt` (exact active turn) and
`pi_rpc_adapter.py::interrupt` (expected-operation guard), the authority read
`harness_submission_authority.py::operation_timeline` (paged never-bodies, eviction floor), the
IPC admission `harness_control_ipc.py::_submit_assets`/`_confined_asset_path` (schema +
resolve-and-verify), the native asset constructors `_turn_input`/`_image_content`, the recovery
capture in `harness_submission_authority.py::withdraw`, and the validated reads
`harness_control_client.py::interrupt_control`/`read_operation_timeline`.
`test_harness_control_plane.py` pins the whole seam; `test_harness_control_plane_installed.py`
captures it live.

For folded-state stream convergence, start at `projector.py::_publish_projection` and
`Projector.subscribe`, then follow `app.py::stream_events` into
`test_serving.py::StreamEventsTests`. Publication commits before notification, subscription
registers before snapshot capture, failed-prime recovery emits one full snapshot, and iterator
closure owns subscriber cleanup.

The structured-conversation contract establishes structure rather than a live endpoint path: consumers validate hostile
normalized products through `conversation/models.py`; future active and library implementations
must satisfy their separate read ports and cursor purposes; future mutations stay on the control
router. The root composition is mounted once beside existing harness-control routes. The locked
repository helper and redacted installed-runtime fixtures are compatibility evidence only and may
not promote a capability by being present.

Reliable submission enters one bridge-generation authority. Async native preflight is
followed by a lifecycle-lock claim and final adapter write guard; a queued withdrawal and dispatch
compete at that exact point. Each prompt/model/effort operation is identified by epoch + monotonic
sequence + id + kind. Direct adapter completion reaches authority before coalesced publication and
can dominate a later unknown receipt when the ref is exact. Cockpit status/withdraw are raw-free,
epoch-gated, and batched to 64 ids. Timeline/duplicate retention is bounded (64/256 defaults) without
evicting live, active, or unknown rows; terminal prompt text is discarded while digest/correlation
remain. Only a certified pre-dispatch busy failure is retry-safe. Codex uses fresh-turn guarded
writes and bounded turn correlation, Claude accepts one guarded operation under the shared transport
lock, and Pi requires fresh state plus generation/activity/event tokens and settled+fresh-idle
completion. The older setter/daemon queue descriptions below are historical provenance superseded by this
authority model.

The live native-capability gate is closed and Claude catalog discovery hardened. Only
the ephemeral discovery launch removes every Claude 2.1.210-supported pre-`--` MCP selector
(`--mcp-config` separate/variadic/repeated or equals-attached, plus the exact strict flag), preserves
unrelated argv and the complete positional suffix, and inserts one strict empty MCP set. Normal
session startup remains byte-for-byte caller-owned and continues to load the installed MCP
configuration. This prevents a token-free catalog refresh from launching unrelated configured MCP
children while preserving the same dynamic model/model-local-effort rows. The final live matrix
keeps Claude Fable switching native-result-driven, Codex selection queued until an accepted fresh
turn on the same thread, and Pi requested/effective thinking readback distinct. Captured catalog
counts and resource measurements are installation evidence, never maintained enums or capacity
policy. A startup-failed bridge may still surface `control command queue is stopped` during graceful
stop; terminate/retire retain that detail, reap the host, and reach terminal catalog state.

The normalized port is exposed through the daemon without introducing ACP transport.
`HarnessCapabilityCatalog` performs token-free native discovery, caches one successful snapshot per
built-in harness under an executable/argv fingerprint, single-flights concurrent misses, and treats
explicit refresh as the auth/account boundary: failure conditionally quarantines only the entry it
observed. `harness_control_api` accepts an optional complete native launch pair and addresses exact
live sessions for advertise, honest set, whole-message submit, and same-id reconcile. Public
serializers omit private raw adapter evidence. The IPC client distinguishes pre-write failure from
first-byte ambiguity, never blindly resends, and the queue makes duplicate request ids idempotent and
reconciles retained known outcomes locally. The shared opener fences one read/probe/ensure/upsert
transaction, so live reopens return immutable process truth or conflict and dead replacement starts
a clean generation. Liveness precedes 404/409 support classification. Role spawn and the durable
inbox/brief bus remain on their existing paths; no UI, settings authoring, paste fallback, Toad, or
ACP transport rides this boundary.

`set_model` and `set_effort` are first-class operations on the normalized
own-adapter port, serialized with prompt submission through `HarnessControlQueue`.
`SetResult` accepts exactly `echo-verified`, `immediate`, `queued`, `unknown`, or `unsupported`,
with requested and effective values kept separate and contradictory combinations rejected. Claude
sends ordinary structured `/model` and `/effort` user frames, then requires the same vendor
session, retained UUID, canonical replay body, and native terminal result; the exact dynamic
`claude-fable-5[1m]` row is a current successful path, while any real
`noninteractive_set_blocked` result remains an honest generic refusal rather than an AR model
policy. Codex keeps desired, pending, captured-prompt, and effective selections distinct, forces a
fresh `turn/start` for pending settings on the same thread, and promotes only a successful turn.
Pi serializes mutation response, bounded `get_state`, and refreshed catalog validation before one
atomic model/thinking snapshot commit, preserving model-error versus thinking-clamp asymmetry.
Cancelled and late responses are reclaimed without reader or queue failure. None of these setter
delegates reaches composer paste, tmux input, session commands, terminal surfaces, or injectors;
role-based spawn and the durable inbox/brief bus retain their separate ownership.

One settings-resolved `ResolvedLaunch{harness, model, effort, workspace}`
is carried through the shared opener into the exact-session runner. Before a configured vendor session starts,
the runner applies adapter-owned selector conflict preflight, performs token-free dynamic discovery,
validates model plus model-local launch effort, then starts Claude with native `--model/--effort`,
Codex with `thread/start` model/config effort, or Pi with provider-qualified
`--model/--thinking`. Effective startup evidence is honest: Pi echoes both, Codex echoes thread
model/effort, and Claude echoes model while its effort remains catalog-validated native-flag
evidence because stream-json has no effort echo. Failures remain addressable as
failed/rejected/exact `bridgeError`; normalized native model/effort is never composer-pasted.

A normalized, own-adapter capability layer sits beneath the port without ACP transport. Claude
`list_models`, Codex paginated `model/list`, and Pi `get_available_models` dynamically advertise
the installed/authenticated model catalog without submitting a model turn. Effort is nested under
each model; running adapters serve their retained startup catalog while transient discovery starts
only the native protocol handshake/catalog path. The ACP Sense 1 projection uses the `model` and
`thought_level` category shape; unknown current values are omitted rather than fabricated.

Claude, Codex, and Pi built-ins negotiate the structured fields their adapters
consume; exact package versions are fixture/smoke evidence only. Rolling inbox compatibility is
limited to optional `adapterDeliveryState` and `adapterDeliveryDetail`, and cutover reloads the
daemon, every MCP-owning client, per-session runners/adapters, and browser tabs. Resource
performance work remains queued.

Codex terminal completion with a null protocol `requestId` is resolved only through its text vendor
correlation on exactly one accepted inbox row for the same hosted session. Missing, non-text,
unmatched, or ambiguous correlation fails loudly. Completion projects onto that same row as adapter
delivery metadata while explicit inbox state remains `pending` and unconsumed. With no actual queued
replacement the adapter reports `idle` / `immediate`; `settling` / `queued` means a replacement is
actually queued. This is protocol-owned structured behavior, not a fixture-version, parser, pane,
fallback, or resource performance behavior.

The exact-session Unix IPC response lifecycle contains peer-loss `BrokenPipeError` and
`ConnectionResetError` only after accepted dispatch, across response write/drain and close/
`wait_closed`. Request dispatch, identity/protocol validation, malformed input, serialization,
cancellation, and unrelated failures remain loud. A delayed-reply disconnect leaves the accepted
submission ambiguous but bridge-reconcilable, with no retry or fallback; bridge reconciliation
returns the preserved vendor correlation.

The projector's waking is change-driven: `change_watcher.py` derives watch
roots from the projection's actual input surfaces (watchfiles/inotify, nothing under `worktrees/`
— container data is unreadable + high-churn, 30s watch-set re-derivation), filters non-input churn, and paces wakes through `ChangePacer`
(debounce 0.1s, max-delay = `--interval` so a busy world keeps the former 1s cadence, idle
heartbeat default 15s via the new `--heartbeat` flag). The tick body is untouched; `/api/state`
staleness and time-derived fields (ages, stale/overdue flips) are bounded by the heartbeat;
watcher absence/failure degrades LOUDLY to legacy fixed-interval ticking; `--sim` stays
time-driven; a running daemon picks the new pacing up only via explicit stop + spawn (ensure
adopts healthy daemons).

Confirmed-gone inbox reconciliation runs at the front of the deterministic
supervisor sweep. The bounded policy resolves only eligible supervisor nudge/escalation rows:
catalog termination is direct proof, compacted tombstones require one successful exact-name tmux
snapshot, and command failure fails closed. Resolve-plus-compact runs under the inbox lock before
redelivery; the body-free aggregate event is silent on no-op sweeps. The existing TTL/cap fallback
and active/landed/exited retention remain unchanged.

Seat normalization is centralized in `seat_binding.py`: `spawnRole` is immutable
provenance, `seatRole` is current binding, and uniqueness is one live owner per canonical
leaf-role pair. `terminal_catalog.py` migrates old rows; opener/assignment liveness-check the
same-role holder; attach requires identity for an untyped hand-opened harness; retire/supervisor/
landing paths consume binding identity. The supervisor also preserves role in findings, rows,
cooldowns, coalescing, and events, and uses one injected sweep timestamp for delivery writes.

Harness JSONL is the only submitted-delivery authority across spawn, inbox,
supervisor redelivery, and REST paste. `harness_logs.py` discovers/binds a recent cwd-matching
Claude/Codex log; `injector.py` separates message and command evidence with calibrated 40.3 s/29.0
s windows; `terminal_paste.py` owns one Enter re-press and one verified-absence clear/replace
re-paste, with pane capture restricted to duplicate prevention and failure diagnostics. The catalog
persists resolved knobs, log id/path, and `replacementForLeaf`; safe binding re-reads the latest row.
Codex knobs ride explicit argv, and the supervisor's synchronous redelivery budget defaults to one.

A live sixty-second workspace-river compactor runs over virtual locked cursors, full task bodies are
served only through `GET /api/task-document`, and the supervisor is current-manager-first,
chain-progress-aware, and one-rung-per-row-per-sweep. The always-on state/SSE projection remains
body-free for task documents.

`agents-remember dashboard --config <settings.json>` → `cli/dashboard.py` →
`serving.app.create_app(config)`. The app's lifespan starts one `Projector` that ticks
`project_and_write` — on change-or-heartbeat wakes when the live change
watcher is healthy (`--interval` is the fast-path cadence floor a busy world still ticks at;
`--heartbeat`, default 15s, is the quiet-world refresh) and on the legacy fixed `--interval`
under `--sim` or a degraded watcher — refreshing provider current-state first in live mode, then
hands each successful projection to one publication boundary. That boundary derives either a
first-recovery snapshot or `serving.delta.diff_projection` events, commits stable/current
authority, and only then fans events out to every registered SSE client. Beside the projector task,
the same lifespan runs the **provider containment
metrics sampler**: every 30s
(`DEFAULT_SAMPLE_INTERVAL_SECONDS`, deliberately decoupled from the projection tick)
it snapshots labeled provider containers read-only
(`providers/metrics.sample_provider_containers`) into the `ProviderMetricsStore` under
`logs/observer/providers/` — exception-tolerant (a failed docker probe logs and retries
next interval), dockerless-safe, cancelled at shutdown; `provider_status` and the
degradation protocol read that store. The same sampling-loop
iteration, in the same exception-tolerant `try` block, also calls
`await asyncio.to_thread(evaluate_provider_degradation, config)` immediately after the metrics
record — no separate task, no separate cadence; the degradation detector's durable
events/state/inbox-alerts/critical-failsafe live entirely in `providers/degradation.py` (governed
by the `mcp/` package overview), this route's `app.py` only wires the one extra call into the
loop it already owns. `GET /api/stream` consumes one atomic projector subscription: it emits the
captured current `event:snapshot`, or waits for one full first-recovery snapshot when prime failed,
then per-entity `lifecycle`/`enclosure`/`provider`/`metrics`/`analytics` (and `*.removed`) events;
`GET /api/state` returns the
projection once; `GET /api/events` tails the raw `ar-observer-event/v1` log with physical byte-offset
resume for lifecycle sources and lock-consistent virtual byte offsets for the live-compacted workspace
source (`serving.events`), doing one retained-backlog scan per connect,
streaming that bounded backlog in chunks (no whole-history materialization), filtering
`lifecycle.heartbeat` out of the river, and pruning expired logs on a slow cadence; `POST /api/actions/{action}`
validates lifecycle transitions against `ActionAvailability` (no mutation) and records
targeted gate-decision verbs as developer-attributed gate decisions, including `gateId` staleness
checks and rejection notes (`serving.actions` + `gate_decide_for_lifecycle`). `POST /api/operator-inbox` writes developer/dashboard-attributed
external-chat responses through `mcp/tools/operator_inbox.py` so non-hosted agents can poll/consume
them; `/api/actions/dismiss` also persists targetless actionable-drift acknowledgements
and the raw `/api/events` stream sends a one-shot `ready` marker after retained backlog replay, so the
frontend can avoid painting an empty feed before history has arrived. `POST /api/operator-inbox/{entry_id}/dismiss` deletes stale pending entries after the pickup TTL
warning is shown. `--sim` swaps a replay clock + fixture feeder onto the projector's
`now`/`before_tick` seams (`serving.sim`). `GET /api/task-document?path=...` is the separate
task-reader body edge: it requires a ready projection and delegates path confinement/schema
validation to `observer.snapshots`; `/api/state` and `/api/stream` carry summaries only. Gate-id-only
`cancel` requests are the explicit legacy
cleanup path for workspace-shaped stale gates; approve/reject/revision stay lifecycle-targeted. The static bundle (`package_data/dashboard/`)
mounts at `/` when one was built, and a 503 diagnostic mounts there when one was not. The Mode B2 terminal bridge `@app.websocket("/api/terminal/{session}")` (6d-2)
attaches one concrete `TerminalHost.attach` tmux client per browser WebSocket — binary PTY bytes out,
JSON `stdin`/`resize` in (the `websockets` dep is uvicorn's WS impl). The bridge can rehydrate catalog
rows after a dashboard restart, but only after `TerminalHost.has_session` proves the tmux name still
exists; normal browser disconnect closes only that websocket's PTY client while leaving the tmux/catalog
row running so refreshes and second browser tabs get fresh independent attaches; stale running rows
become `exited` only through the **catalog liveness hysteresis** path
(`terminal_liveness.py`: evidence-scaled thresholds, ≤1 probe sweep per 10s regardless of the
dashboard's 1s polling, self-healing false exits), and `POST /api/terminal/{session}/terminate` is
the only destructive terminal action.

### Projection/Observation Split

The serving layer starts one lifecycle-managed landing refresher for live projection, passes its latest immutable snapshot into the network-free projector tick, and cancels it during shutdown. Simulation disables remote observation; interactive status remains the fresh-probe path. A failed refresher is logged without preventing host shutdown.

## Route Model

- `harness_submission_authority.py` — the sole prompt/setter timeline: epoch/idempotency
  admission, lock-linearized dispatch/withdraw, full operation refs, response bypass, early exact
  completion, raw-free status/withdraw projection, and bounded live-safe retention.
- `harness_control_queue.py` — compatibility facade over `HarnessSubmissionAuthority`; it owns no
  independent command queue or receipt ledger.

- `harness_capabilities.py` and `harness_control_adapter.py` — the normalized capability contract:
  `CapabilitySnapshot` contains dynamic `ModelCapability` rows with model-local `EffortOption`
  menus; ACP Sense 1 projects category-keyed select options; `LaunchKnobs` includes adapter-owned
  selectors and `SetResult` establishes the setter evidence boundary. The combined launchable adapter
  seam joins synchronous cached advertise, transient native discovery, and native launch knobs. No
  ACP transport, global effort enum, or composer-paste fallback belongs in this port.

- `harness_capability_catalog.py` — the pre-session discovery authority. It resolves only the
  built-in native registry rows, fingerprints effective argv plus the canonical executable/stat
  identity, passes the current environment into the own-adapter `discover()` port, and retains at
  most one successful entry and lock per built-in harness. Ordinary misses are single-flight;
  explicit refresh re-enumerates auth/account state, and a failed refresh conditionally evicts only
  the exact observed entry so stale data cannot reappear as a healthy hit or erase a later success.

- `harness_control_client.py`, `harness_control_api.py`, and `harness_control_models.py` — the
  exact-session serving boundary. The client strictly parses normalized advertise/set results and
  records whether a Unix-socket failure happened before or after the first accepted byte; only the
  latter becomes honest unknown evidence under the same request id/value. The API exposes
  pre-session/live capabilities, setter results, whole-message submit, and reconcile after
  liveness-first session resolution. Public receipt/reconciliation serializers preserve normalized
  acceptance, timestamps, detail, and correlation while omitting adapter-private `raw`.

- `harness_launch.py`, `harness_control_factories.py`, and `harness_control_runner.py` — carry the
  complete typed settings selection across tmux, reject adapter-owned selector conflicts before
  discovery, validate against the live model/model-local effort catalog, construct a fresh
  configured adapter, and preserve exact failure evidence over IPC. The daemon request can now
  supply an optional complete pair through this same launch path; a selectionless request still
  lets the native authenticated catalog choose its default without creating a second authority.

- `claude_stream_capabilities.py`, `claude_stream_protocol.py`, `claude_stream_startup.py`, and
  `harness_control_claude.py` — correlate `control_request/list_models` before the steady-state
  stdout reader starts, validate the live catalog/current-model relationship, map only each model's
  advertised effort tokens, and retain the normalized catalog for running advertise. Cold discovery
  performs initialization plus catalog enumeration and sends no bootstrap prompt. Initial model and
  effort use native `--model`/`--effort`; model echo is verified, while absent effort echo is
  recorded honestly rather than fabricated.

- `codex_app_server_state.py`, `codex_app_server_session.py`, and
  `codex_app_server_adapter.py` — preserve descriptions and model-local reasoning efforts from every
  `model/list` page (including hidden rows), retain the catalog at connect, and expose a cold
  initialize/list-only discovery path that starts neither a thread nor a turn. Initial model and
  model-local effort travel through `thread/start`/`thread/resume` config and are echoed before
  readiness; later turns reuse the resolved effort.

- `pi_rpc_protocol.py`, `pi_rpc_process.py`, `pi_rpc_events.py`, and
  `pi_rpc_adapter.py` — the Pi protocol/process/event/adapter chain: strict LF JSONL, bounded child
  transport, normalized retry/compaction/settlement and extension UI events, `get_state` readiness,
  exact-session reconnect, and post-cursor reconciliation without resend. The Pi adapter also consumes
  `get_available_models`, preserves provider-qualified model identity, derives model-gated thinking
  menus using Pi's own map rules, strips provider headers from retained state, and makes transient
  discovery fail-clean and prompt-free. Configured startup uses exact provider-qualified
  `--model` plus native `--thinking` and requires both effective values to echo, exposing Pi's
  silent-clamp asymmetry rather than trusting it.

- `cadence.py` — `ProjectionCadence(interval, heartbeat)` + `DEFAULT_PROJECTION_CADENCE`. The one
  pacing decision every dashboard process shares, kept **stdlib-only** so the import-light daemon
  supervisor can name a spawned child's cadence without importing the projector (and, through it,
  the serving stack).

- `hosted_session_runtime.py` — `HostedSessionRuntime(catalog, host)`. The pair of authorities that
  jointly decide which hosted sessions exist: a durable catalog row and a live tmux process. Neither
  answers "does this session exist, and what is it?" alone, and a row read against the wrong host is
  a silent correctness bug, so the opener takes them bound together.

- `app.py` — `create_app(config, *, cadence, replay, live_inputs, collaborators)` builds
  the FastAPI app
  (`ProjectionCadence` paces it; `ProjectionReplay` is the sim seam; `LiveProjectionInputs` resolves
  the three live world-input toggles together against that seam — each `None` = infer, so live
  serving injects a `ProjectionInputWatcher` for change-driven pacing while `--sim` stays
  time-driven, and `cadence.heartbeat` bounds quiet-world staleness; `ServingCollaborators` are the
  four injectable long-lived objects). Since 260731-EFA-L2 the handlers, background loops and route
  registrars are module-level functions taking one frozen `_ServingRuntime` rather than nested
  closures. It wires: a
  lifespan that primes + runs one shared `Projector` plus the 30s provider containment
  metrics loop (`sample_provider_containers` → `ProviderMetricsStore.record`
  via `asyncio.to_thread`, exception-tolerant, both tasks cancelled + awaited at shutdown),
  `GET /api/state` (one-shot; **change-gated**
  — weak `ETag: W/"<projector.revision(seq)>"` + `Cache-Control: no-cache`,
  `If-None-Match` weak-matches → `304` empty-body via `_if_none_match_matches`, and the body
  carries the boot-time `servingBuild` stamp),
  `GET /api/stream` (the `state` SSE endpoint, delegating to the testable
  `stream_events(projector, build=…)` — it consumes one atomic projector subscription, decorates
  both initial and first-recovery snapshots with `servingBuild`/supervisor identity, preserves
  delta framing, and explicitly closes the iterator on disconnect/cancellation),
  `GET /api/events` (the raw channel, delegating to `stream_raw_events`; fresh
  connections start from lifecycle-aware retained offsets while valid
  `Last-Event-ID` cursors still resume exactly and emit a backend `ready` event after retained replay),
  `POST /api/actions/{action}` (delegating to `evaluate_action`; gate verbs carry targeted
  `gateId`/`note`, require a reason for reject, and distinguish stale gates from no-open-gate), the
  `@app.websocket("/api/terminal/{session}")` Mode B2 terminal bridge (6d-2 — catalog-backed
  per-websocket `TerminalHost.attach`, binary PTY bytes out / JSON `stdin`+`resize` in, via the
  module-level `_bridge_terminal`/`_apply_terminal_session_input` helpers), `POST /api/operator-inbox` (call
  `operator_inbox_post_payload` with developer/dashboard attribution for durable inbox messages,
  accepting lifecycle/agent/recipient role plus role/message/artifact metadata and passing catalog/host/paster
  seams for optional hosted push; bad lifecycle/agent/role addressing returns `400 bad-address`),
  `POST /api/operator-inbox/{entry_id}/dismiss` (physically delete a pending inbox entry
  for dismissible `check chat` warnings), the
  `POST /api/terminal/{session}` **opener**
  (6e-2a/6e-2b; the leaf-claim + `host.ensure` + catalog-upsert composition delegates to the
  shared `terminal_opener.open_terminal_session` — `resolve_terminal_launch` / `_terminal_label` / the
  role-scoped conflict check all left `app.py` for that module — so this route and the `spawn_agent_session`
  MCP tool spawn through ONE opener; it accepts optional `model`/`effort`, requires a complete pair for
  built-in native harnesses, and maps `bad-kind`→400 / `leaf-taken`→409 /
  `launch-conflict`→409 / `opened`→200. Successful and conflicting responses report the actual
  retained row's launch/control facts rather than echoing the attempted request. Server-resolved
  harness id, never argv on the wire; the opener passes `suspend_unsafe=(kind=="harness")` so
  later host writes strip Ctrl-Z for bare-pane harnesses, slice 6f, and persists a `TerminalCatalogEntry`
  carrying label/lifecycle/cwd/tmux/command/status/leafKey + spawned-by provenance + `spawnRole` without opening a
  starter PTY client; uniqueness is per (leaf, role) so a terminal never collides with the
  leaf's chat, and the `leafKey` is normalized through `leaf_ref_validation.resolve_catalog_leaf_key`
  before persistence (preserving an existing binding when none is sent) and echoed),
  `POST /api/terminal/{session}/paste` (server-side capture-verified
  context-packet delivery to a hosted session with no attached browser client, over
  `terminal_paste.TerminalPaster`; delivery is confirmed against the pre-delivery origin capture —
  a new chip in either harness vocabulary or the payload head, not mere pane output; 404 on
  unknown/gone session, else `{delivered, submitted}` plus the pane `capture` on an unconfirmed
  outcome),
  `POST /api/terminal/{session}/attach-leaf` (normalize the requested leaf ref,
  then claim or move a leaf for an existing session, enclosure-free / no respawn; delegates to
  `terminal_leaf_assignment.assign_terminal_session_to_leaf`, returning `400 leaf-ref-not-found` /
  `400 leaf-ref-ambiguous`, `404 unknown-session`, `409 leaf-taken` without mutation, or `200 attached`), `GET
  /api/terminal/sessions` (return non-terminated sessions via
  `terminal_liveness.TerminalCatalogLivenessSweeper.refresh()`: ≤1 probe sweep per 10s,
  non-overlapping, rate-limited callers get the persisted catalog; WebSocket attach + the paste
  endpoint run direct `observe_terminal_liveness` observations on the app's ONE injected clock,
  replacing the deleted `_refresh_catalog_entries` immediate exit-marks),
  `POST /api/terminal/{session}/terminate` (kill tmux and mark the catalog row terminated),
  `GET /api/harnesses` (6e-2b — `detect_harnesses()` per `shutil.which`), the native control
  routes (`GET /api/harnesses/{harness}/capabilities`, live `GET .../capabilities`, `POST
  .../set-model`, `POST .../set-effort`, `POST .../submit`, `POST .../reconcile`,
  authority/status, and authoritative withdraw) registered
  before the static mount, `POST /api/terminal/{session}/image`
  (6f — save a validated screenshot under `<cwd>/.dashboard-pastes/<uuid>.<ext>` using either a live host
  session cwd or a catalog-restored cwd so the composer can inject its path; the terminal channel is
  text-only), `POST /api/terminal/{session}/retire` (issue #12 — the
  server-authoritative retire surface: 404 unknown-session/unknown-actor, 200 `already-retired`
  idempotent fast-path on an already-terminated target BEFORE any authority check, 403
  `retire-refused` naming the exact policy clause via `retire_policy.check_retire_authority`, else
  `retire.retire_entry` kills tmux + marks the catalog row + `seat_events.log_retire_event`),
  `POST /api/terminal/{session}/rename` (issue #4 — 404 unknown-session on a
  missing/terminated target, else `catalog.set_label` + `seat_events.log_rename_event`; identity
  text only, never `spawn_role`), and the static mount.
  SSE uses built-in `fastapi.sse` (`EventSourceResponse`/`ServerSentEvent`).
- `daemon.py` — the dashboard daemon supervisor: `ensure()` adopts a healthy detached
  daemon, spawns a missing one, and restarts on version/host/port mismatch, behind one
  non-blocking flock (`ensure.lock`) so concurrent MCP boots never double-spawn. State lives under
  `<coordinationRoot>/logs/dashboard/` — an atomic `daemon.json` (pid/host/port/version/paths,
  written immediately after spawn) and a per-spawn-rotated `dashboard.log` (the child serves with
  `--no-access-log` so the log stays bounded). Liveness is kill-probe **plus** `/proc/<pid>/cmdline`
  identity (pid reuse and zombies read as stale); stop is TERM → bounded wait → KILL.
  `ensure`/`spawn` plumb an optional `heartbeat` onto the child argv
  (`--heartbeat`, spawn/restart only — ensure ADOPTS a healthy daemon without cadence comparison,
  so adaptive pacing reaches a live daemon only via explicit stop + spawn). The child is
  the plain foreground CLI addressed by module string — the module stays import-light (stdlib +
  config types, never uvicorn/FastAPI), so `mcp/server.py`'s boot hook
  (`maybe_autostart_dashboard`, threaded/total/stderr-only, gated by the `dashboard.autoStart`
  settings key) never pulls the serving stack into MCP startup.
- `projector.py` — `Projector`: owns the atomically-published `(seq, projection)` tuple, the
  previous tick's stable form, a boot nonce, and the subscriber fan-out. `prime()`, `run()`
  (tick: re-project → compute snapshot/delta batch → commit stable/current authority → notify),
  `_publish_projection()`, `current()`,
  `revision(seq)` (the `"{boot}-{seq}"` content fingerprint behind the `/api/state` ETag — seq
  only advances on stable-content change), `subscribe()` (register queue and capture the
  current snapshot without an await, then drain that queue with `finally` cleanup). A failed
  `prime()` recovers by sending one full snapshot to already-connected subscribers; identical
  recovery does not duplicate and later changes return to ordinary deltas. The `now`/`before_tick`
  seams + `_tick_sync(moment)` keep one loop generic across live and sim. Live projectors can
  pass a provider refresher into the observer store; sim projectors keep fixture state
  deterministic by omitting it. One re-projection per tick regardless of client count.
  With an injected `change_watcher` the pacemaker is `ChangePacer.wait()`
  (change-or-heartbeat waking) instead of the unconditional `sleep(interval)`; the watch task's
  lifecycle mirrors the landing refresher's, a dead watcher degrades loudly to fixed-interval
  ticking (`_on_watch_task_done`), and `projection_count`/`last_wake_reason` instrument the loop.
  Without a watcher (sim, injected-`now()` tests) the legacy pacing is byte-identical.
- `change_watcher.py` — the **change-driven pacing module**:
  `projection_input_roots` (watch roots derived reader-by-reader from `project_and_write`'s input
  surfaces — tasks/, observer lifecycles/workspace/drift, provider status/setup, temp
  worktree-start/tool-reports; nothing under `worktrees/` — container data is unreadable to the
  daemon user and high-churn; the derivation
  table lives in its docstring), `is_projection_input_event` (drops `*.tmp`, dotfiles, the
  projection's own outputs, and workspace non-input churn incl. `operator-inbox.lock`),
  `ChangePacer` (debounce 0.1s, max-delay = interval — a busy world keeps the former cadence —
  heartbeat default 15s, degraded ⇒ fixed interval, starts degraded at boot), and
  `ProjectionInputWatcher` on `watchfiles` (30s watch-set re-derivation; ANY failure — missing
  wheel, derivation error, crashed watch — degrades LOUDLY to fixed-interval ticking and retries
  every 30s). Heartbeat = the staleness bound for `/api/state` and time-derived fields
  (volatile ages already advance client-side via `servedAges.ts`).
- `delta.py` — the **pure** `diff_projection(previous, current, *, previous_state=None,
  current_state=None) -> list[DeltaEvent]`: the per-entity diff over the flat id-keyed
  collections (upserts in projection order, removals sorted for determinism). A transport concern
  kept out of the reducer. It also emits an `activeWorktreeGroups` whole-value delta
  (a bare list wrapped as `{"activeWorktreeGroups": [...]}`) when that set changes, alongside the
  `metrics`/`analytics` whole-block events. **The change gate:** comparison runs
  over *stable forms* — `VOLATILE_AGE_FIELDS` (`staleSeconds`/`snapshotStaleSeconds`/`ageSeconds`/
  `waitSeconds`/`heartbeatAgeSeconds`, mirrored client-side in `dashboard/src/data/servedAges.ts`)
  stripped recursively — so a tick where only ages advanced emits NOTHING (live measurement:
  ~780 KB/tick → 0; the dashboard-tab OOM driver). `StableProjectionState` +
  `stable_projection_state` are the projector's per-tick cache.
- `build_info.py` — the boot-time **serving build stamp** (the July-4
  ghost-process lesson): `ServingBuild` (version / best-effort git short-hash / boot time) +
  `resolve_serving_build`, resolved ONCE in `create_app` and injected on `/api/state` + the SSE
  snapshot as `servingBuild` so a stale serving process is visible in the cockpit top bar. A
  failed hash resolve serves version-only (`commit` omitted), never a fake.
  Both probes — `_git_short_head` (`rev-parse --short HEAD`) and `_git_worktree_dirty`
  (`status --porcelain`) — go through the package's one git runner, `run_git` in
  `kernel/git_command.py`, since 260731-EFA-L3; they previously built their own `subprocess.run`
  calls here. The runner strips the `GIT_DIR`-family repository selectors, which is what makes the
  stamp name **the checkout the server was actually booted from**: with `GIT_DIR` exported, the
  identity meant to expose a ghost process would have described whatever repository that variable
  pointed at. It also keeps the `stdin=DEVNULL` guard the local calls carried by hand (never touch
  the MCP stdio protocol pipes). The 2-second bound survives as the named
  `_PROBE_TIMEOUT_SECONDS = 2`, passed explicitly against the runner's general-purpose
  `GIT_LOCAL_TIMEOUT_SECONDS = 300` — a best-effort stamp must never delay app creation, so a git
  that does not answer in two seconds is "unstampable" like any other failure.
- `events.py` — the raw `event` channel: the **pure** byte-offset tail `read_new_events` (a
  composite per-source offset cursor, `encode_cursor`/`decode_cursor`) + the `stream_raw_events`
  async tailer. Fresh connections use `observer.event_retention.initial_event_offsets` so expired
  (inactivity-pruned) lifecycle logs are skipped, workspace/lifecycle-less rows are bounded by age, and
  active lifecycle histories remain uncapped; malformed/empty cursors fall back to those retained offsets,
  while valid `Last-Event-ID` cursors keep exact byte-offset resume. Separate from `/api/stream`
  (byte-offset resume vs. snapshot resume). The stream emits `event: ready` once after the retained
  backlog is sent on each connection, giving the browser a reliable hydration boundary. The
  connect path is cheap and quiet: it does **one** retained-backlog scan per connect (no repeated
  whole-history reads), streams that bounded backlog to the client in **chunks** rather than
  materializing the whole history, filters `lifecycle.heartbeat` events out of the river, and prunes
  expired logs on a slow background cadence instead of on every tail.
- `sim.py` — sim mode: `build_sim` + `ReplayClock` + progressive `ReplayFeeder` +
  `parse_sim_speed`, replaying a fixture's recorded events through the projector's
  `now`/`before_tick` seams over a throwaway temp root (the fixture is never mutated). `build_sim`
  also **materializes the fixture's structural surfaces** (`_materialize_surfaces` — contracts / task
  docs / provider state / ledgers / drift) into the sim root, so a rich fixture exercises the whole
  projection, not only the replayed event logs.
- `actions.py` — the POST action layer: `ActionRequest` + the **pure** `evaluate_action`.
  Lifecycle transitions map against the node's `ActionAvailability` to 202/409/404 with
  attribution (no mutation); gate-decision verbs carry a targeted `GateDecisionIntent` with optional
  `gate_id` and `note`, reject requires a non-empty reason, target omission is allowed for `cancel`
  with `gateId` and for actionable-drift `dismiss`, and the router records the result as a
  developer/dashboard-attributed gate decision via `gate_decide_for_lifecycle` or a workspace-gate
  `gate_decide_payload` cancel. Targetless actionable-drift dismissals are persisted as attention
  acknowledgements instead of gate decisions.
- `static.py` — `dashboard_static_dir()` resolves `package_data/dashboard` via
  `importlib.resources` (the `install.assets` idiom), returning `None` when nothing was built there;
  `mount_static(app)` always mounts something at `/`. With a bundle it mounts
  `DashboardStaticFiles` (HTML revalidates, hashed assets keep default caching). Without one it
  mounts `MissingDashboardBundle`: **503** on `GET`/`HEAD` with the expected location and the build
  command in a `no-store` plain-text body, and **405** on every other method — exactly what
  `StaticFiles` raises — so the greedy mount cannot turn an `/api` method error into an outage.
  Since 260731-EFA-L1 the bundle is a release build product that is not in version control, so
  "absent" is a normal state for a source checkout, not a broken install. There is no placeholder
  and no fallback UI.
- `files.py` — the **read-only files API**: `register_files_routes(app, config)`
  registers `GET /api/files/{repos,list,read,onboarding}` **before** `mount_static` (the greedy `/` mount
  must stay last). It is the first serving module to resolve a kernel `CoordinationContext`: a
  `{repo, mainline|enclosure}` scope maps to `(codeRoot, onboardingRoot)` to enumerate repos/enclosures,
  list one directory level (code + paired onboarding), read a file (content + drift metadata), and resolve
  the 1:1 code↔onboarding sidecar pairing both ways via the shared `kernel/sidecar_pairing.py`. Allow-listed
  roots only, realpath-confined (Task-6 posture); a memory-less repo degrades to code-only browsing and a
  missing sidecar is a normal `missing` result, never an error. Feeds the dashboard File Viewer and
  Change-Set Viewer.
- `scope.py` — the **shared browse-scope layer** (extracted from `files.py`):
  `FileScope`, `resolve_scope` (`{repo, mainline|enclosure}` → roots), the `run_scoped` error map (404
  unknown-repo/unknown-scope/not-found, 400 bad-path), `language_for`, and the active leaf-enclosure
  enumeration. `files.py` and `changeset.py` both import it (files.py re-exports `FileScope` +
  `_resolve_within` for callers/tests). Behaviour matches the original files resolver — one resolver, shared.
- `changeset.py` — the **read-only change-set API**: `register_changeset_routes`
  mounts `GET /api/changeset/{task,file-diff,master}` **before** the static mount. Computes a task's
  `base → current` code + memory change-set with insertion/deletion counts + status + `hasSidecar`
  (`task`), BEFORE/AFTER file content for the CodeMirror MergeView (`file-diff`, with an optional `master` param for the series net file-diff), and the master's **NET**
  change-set (`master`) — `git diff <master-base> <resolved-series-tip>` for code + memory (one
  coherent, per-file-inspectable range) with a per-leaf counter breakdown alongside. For an in-flight
  series the resolved tip is the contract work-branch tip; after landing, when that work branch is gone,
  it falls back to the source-branch tip. The master file-diff view uses the same resolved tip so
  counters and BEFORE/AFTER content cannot drift. The doc-reader
  **leaf views**: the `task` + `file-diff` routes take a `leaf` + `mode` selector (precedence
  `leaf > master > scope`), resolving one leaf's `committed` (`base → code_commit`) or `working`
  (`HEAD → worktree`, uncommitted only) change-set straight off the persisted enclosure contract
  (`_load_leaf_contract`, by leaf-id — works with no live worktree, for a completed leaf), with the
  selector validated (`leaf` needs `master` + a valid `mode` → `400`, no-live-worktree `working` → `404`).
  Master and leaf contract discovery is confined to the requested repo/master enclosure and
  canonicalizes both requested and persisted leaf ids; `/api/changeset/master?includeLeaves=false`
  skips the optional per-leaf breakdown while preserving the coherent net range.
  Reuses `scope.py` + the same confinement posture; the change-detection primitive is
  `worktrees/modules/git.changed_files_with_counts`. Feeds the dashboard Change-Set Viewer.
- `notes.py` — the **read-only coordination-notes API** (its status mapper, like `scope.py`'s files-API mapper, answers `400 bad-path` for `ValueError` input such as null bytes — a review fix applied to both):
  `register_notes_routes` mounts `GET /api/notes/{list,read}` **before** the static mount. Lists +
  reads one series master's `tasks/<repo>/<master>/notes/` tree under the coordination root — the
  design records / friction ledger / worker reports / adversarial verdicts that previously had no
  dashboard surface. Confinement: `require_repo` allow-list, single-segment `master`, `confine_rel`
  realpath reads, per-child realpath checks on the depth-capped (`truncated`-honest) listing walk;
  a missing notes folder is an empty list, a binary file reads as `language: "binary"` with empty
  content. Feeds the task reader's notes view (`dashboard/src/panels/TaskNotes.tsx`).
- `terminal.py` — the **Mode B2 terminal host** (slice 6d-1): `TerminalHost`, a registry of
  tmux-wrapped PTY sessions correlated to a lifecycle/worktree. `open`/`write`/
  `read_nonblocking`/`resize`/`close` over a stdlib-`pty` master fd; the spawn (`tmux
  new-session -A … -- <harness>` on `pty.openpty`) is injectable so tests drive a real kernel
  PTY without tmux. The spawn gives the child a **controlling terminal** (`os.login_tty` in a
  `preexec_fn`) + a seeded winsize, so tmux has a `/dev/tty` to size against and honors resize (slice
  6e-4). `write` strips the Ctrl-Z byte `0x1a` for **suspend-unsafe** (bare-pane harness) sessions only,
  so a harness can't be soft-locked into a suspend while a plain shell keeps its job control (slice 6f).
  Injectable tmux probe/create/kill hooks, `has_session`, `ensure`, `terminate`, and
  unregistered per-connection `attach` clients so the durable catalog can create a detached tmux
  session, prove it still exists before attach, kill one explicitly, and serve multiple browser tabs
  without sharing one PTY fd. The probe is evidence-bearing:
  `TmuxProbeResult(exists, evidence)` / `probe_session` beside the boolean `has_session`, with
  stderr-aware classification — only explicit missing-session stderr is definitive `pane-gone`;
  every other failure (subprocess error, timeout, non-missing nonzero exit) is the transient
  `tmux-command-failed` that feeds catalog hysteresis instead of an immediate exit mark. An optional `env: Mapping[str, str]` threads through
  `ensure`/`open`/`_build_tmux_command` (`_tmux_create_detached` emits `tmux new-session -e KEY=VALUE`
  via the pure `_env_flags`), seeded only at creation and inert on re-attach — the minimal
  env-passthrough seam the agent-facing spawn tool injects role knobs through (empty-safe: an empty
  mapping keeps the byte-identical legacy argv). The injectable `TmuxConfigurer` seam
  (default: per-session `tmux set-option mouse on`, failures suppressed) is asserted by `ensure` and
  every `attach`, so browser wheel input reaches tmux as mouse reports — tmux scrolls pane history for
  normal-buffer TUIs and passes wheel through to mouse-aware ones (pane text selection becomes
  Shift+drag). Its copy-mode escape companion: `write_session` arms a per-connection flag on
  mouse-report-only stdin and cancels copy-mode (injectable `TmuxModeCanceller`, `send-keys -X cancel`
  default) on the first typed input after scrolling, so typing anywhere in the scrollback snaps to the
  live bottom and reaches the pane app. Fixed-argv (no shell injection), OS-user creds, localhost. The live
  WebSocket bridge (`@app.websocket("/api/terminal/{session}")`, in `app.py`) + the `websockets`
  dep landed in 6d-2; the xterm.js viewport is 6e.
- `terminal_catalog.py` — the durable dashboard terminal-session catalog: immutable
  `TerminalCatalogEntry` rows plus a JSON store under `logs/dashboard/terminal-sessions.json`. It
  persists id, label, kind, optional harness/lifecycle, cwd, tmux name, command, timestamps, status,
  an optional `leaf_key`, and optional spawned-by provenance
  (`spawned_by_session` / `spawned_by_lifecycle`, written migration-safe only when set; the copiers now
  use `dataclasses.replace` so a new column survives a re-attach); normal `list()` keeps exited rows visible and filters terminated
  rows, while `include_terminated=True`
  is available for audits. Explicit termination wins over later passive exit bookkeeping so an `End`
  action cannot reappear after refresh as an `exited` row. The catalog is the
  **leaf→chat registry**: `to_json` writes `leafKey` only when set (migration-safe), `with_leaf_key` is
  the attach write point, and a leaf-uniqueness **role** (`TerminalSessionRole`,
  `role_for_kind` / `entry.role` — a shell is a terminal, a harness is a chat) scopes
  `active_for_leaf(leaf_key, role="chat")` so it returns the single **running** owner *of that role* — the
  per-(leaf, role) single-owner probe the opener + attach-leaf routes call before an upsert, letting one
  leaf hold a running chat AND a running terminal at once. The catalog also carries persisted liveness
  state (`livenessFailures`/`livenessFirstFailedAt`/`livenessLastFailedAt`/`livenessEvidence` +
  `exitEvidence` on exited rows, all migration-safe write-when-set) and the locked
  `record_liveness_probe` write point with the `with_liveness_success`/`with_liveness_failure`
  transition copiers — hysteresis survives a daemon restart and a false exit self-heals on the next
  alive probe. `batch()` serves as the complete session-open transaction fence: its file lock
  plus process `RLock` spans read, live probe, host ensure, and upsert, so concurrent callers cannot
  share one newly created process and then publish different attempted launch provenance. Other
  processes see the coherent last committed atomic-file snapshot until the batch commits.
- `terminal_liveness.py` — the **catalog liveness hysteresis** module:
  `TerminalCatalogLivenessSweeper` (rate-limited — 10s default interval — and non-overlapping via a
  non-blocking lock; a rate-limited or concurrent `refresh()` serves the persisted catalog without
  probing, so the dashboard's 1s cadence never implies 1s tmux probing) +
  `observe_terminal_liveness`, the shared single-row observation path (in-process `is_alive` →
  evidence-bearing `probe_session` → legacy boolean `has_session`) that persists transitions
  through `TerminalCatalog.record_liveness_probe`. Evidence-scaled hysteresis: transient
  `tmux-command-failed` probes need 3 consecutive failures across ≥5s before an exit mark (a
  command-failure storm cannot mass-exit a live fleet), definitive `pane-gone` marks fast, and a
  falsely exited row self-heals to `running` within one sweep (exited rows are probed too;
  `terminated` is never revived). Constants are code defaults, not settings knobs. Replaces
  `app.py`'s deleted `_refresh_catalog_entries`. Live turn-state
  classification is folded into the SAME alive-probe call (`_observe_alive`, no new hot loop, no new tmux
  round-trip cadence): `kind == "harness"` rows only get `terminal_paste.capture_pane` +
  `turn_state.classify_turn_state` on every ALIVE observation, persisted via
  `catalog.record_turn_state`; `TerminalLivenessObservation.turn_state_changed` is true only on an
  actual transition, and `TerminalCatalogLivenessSweeper` gained an `on_turn_state_change` callback
  (wired in `app.py`'s `create_app` to `seat_events.log_turn_state_change_event`) fired only for
  those transitioning rows, never per sweep tick. The `on_control_snapshot` observer (the
  hosted-interaction synchronizer wired in `create_app`) is quarantined as a
  per-entry side effect: `_observe_alive` routes it through `_observe_control_snapshot`, which
  records any failure fail-loud on that ONE row's `control_raw["interactionSyncError"]` and lets the
  sweep continue. Before this, a single orphan-`vendorCorrelationId` completion raised
  `HarnessControlError` out of the per-entry comprehension inside `catalog.batch()`, aborting the
  whole sweep and 500-ing `GET /api/terminal/sessions` for EVERY row (the stuck-loading
  rail). Load-bearing fact: an orphan `vendorCorrelationId` is the NORMAL steady state of every
  cockpit-driven hosted (`+ Chat`) codex chat, so this quarantine path is HOT, not exceptional; the
  warning is bounded to state changes (first occurrence / heal) while the per-sweep marker keeps the
  wire honestly degraded. Availability hardening only — the completion-correlation contract in
  `hosted_interactions.py` is untouched (the
  phantom-transition re-warn on non-observer `control_raw` rebuilds is a known Low residual). Detail in the
  file sidecar.
- `retire_policy.py` — the server-side retire authority policy: `SeatRef`,
  `master_of(leaf_key)` (the qualified leaf key's 2nd path segment — uniform for a leaf-level or
  master-level `leaf_key`), `check_retire_authority(actor, target)` (owner-never-self-retires
  checked FIRST unconditionally; a manager may retire only worker/reviewer seats of its own master;
  only the orchestrator has portfolio-wide authority; every refusal names the exact clause via
  `RetirePolicyError`).
- `retire.py` — the shared manual retire mechanics: `retire_entry` kills the tmux
  session best-effort/idempotent, then `catalog.mark_retired`. This path backs explicit retire/tool and
  landed-cleanup closure, not normal successful completion.
- `landing.py` — the shared landing mechanics: `land_seats_for_leaf` marks matching
  non-terminated catalog rows `status:"landed"` with reason/edge provenance, without constructing a
  `TerminalHost` and without killing tmux. `controllers/worktree_tools.py` calls it from successful
  `worktree_integrate`/`lifecycle_finalize_task` completion edges.
- `turn_state.py` — the live turn-state classifier: `classify_turn_state(pane_text,
  harness=)` is marker-regex-based (precedence working > awaiting-input > turn-ended > stale; blank/
  unreadable pane ⇒ `stale`), with empty per-harness override dicts ready for future tuning. Rides
  the EXISTING `terminal_liveness.py` sweep cadence via `terminal_paste.capture_pane` — no new
  tmux round-trip. Patterns are a first-cut, not verified against live harness panes (the classifier
  is fed the full history-inclusive capture rather than just the pane tail).
- `seat_events.py` — the observer-event emitters for the seat surface:
  `log_retire_event`/`log_rename_event`/`log_turn_state_change_event` write `ar-observer-event/v1`
  records (`seat.retired`/`seat.renamed`/`seat.turn-state-changed`) mirroring the existing
  `orchestration_nudge_manager` event-logging pattern, feeding the watcher/architect
  NEEDS-ATTENTION feed.
- `terminal_leaf_assignment.py` — the shared catalog reassignment helper: moves an existing catalog row
  to a new durable `leafKey`, returns `leaf-taken` without mutation when another running same-role session
  owns the target leaf, and is reused by the dashboard route and MCP tool.
- `leaf_ref_validation.py` — the serving adapter for terminal catalog write surfaces: resolves
  qualified ids, doc ids, and unambiguous legacy stems/slugs through `worktrees.leaf_refs`, returning the
  canonical qualified leaf key that opener/attach routes persist.
- `terminal_opener.py` — the shared hosted-session opener: `open_terminal_session(...)` resolves a
  harness **id** to settings-owned base argv, carries an optional typed
  `ResolvedLaunch{harness,model,effort,workspace}` into the exact-session runner, claims `leaf_key`
  under role-scoped per-(leaf, role) uniqueness before spawn, seeds namespaced provenance env at
  `TerminalHost.ensure`, and upserts the durable catalog row with write-once role/lineage/free-form/
  resolved-selection provenance. Static knob mapping is retained only for explicitly declared
  settings-defined non-native harnesses; native Claude/Codex/Pi selection is dynamically validated
  and applied by their adapters. Dashboard `POST /api/terminal/{session}` and
  `spawn_agent_session` compose this same opener—no parallel spawn path. A live catalog
  row is treated as immutable process truth: a selectionless or exact-pair reopen returns it unchanged; a
  changed kind, harness, cwd, or explicit pair returns `launch-conflict` without a second ensure or
  catalog mutation. A dead row starts a fresh generation and drops process-specific control/log/raw
  evidence. The full operation runs under the catalog batch fence so cross-thread/process races
  create one process and one durable launch truth.
- `terminal_paste.py` — the **capture-verified server-side paste**:
  `TerminalPaster.paste(tmux_name, text, submit=…)` mirrors the frontend
  `pasteAndConfirm`/`submitAndConfirm` over tmux primitives — the payload rides STDIN into
  `load-buffer` (never argv/ARG_MAX) then `paste-buffer -p -d`, and `capture-pane` verification
  against ONE pre-delivery origin baseline held for the whole delivery: a NEW paste chip in either
  harness vocabulary (`[Pasted text #N]` claude, `[Pasted Content N chars]` codex) or the payload's
  own head confirms; before any re-paste across the boot window the pane is re-captured first, so a
  landed paste is never re-sent (duplicate stacking impossible — per-attempt re-baselining
  is what allowed repeats to stack). `PasteResult.capture` attaches the final pane snapshot so a failed
  delivery is loud evidence, never a bare boolean; Escape is refused by
  construction — only Enter is ever sent. Every tmux op + the clock are injectable so the loop is
  fake-driven and sleepless in tests. Never submits an unconfirmed paste; never raises on a gone
  session. Backs the `spawn_agent_session` context delivery, the
  `POST /api/terminal/{session}/paste` endpoint, and the inbox hosted push (whose durable failure
  detail embeds a bounded capture tail). The public `capture_pane(tmux_name)`
  wrapper wraps the existing private `_tmux_capture_pane`, so turn-state classification
  (`terminal_liveness.py`) reads the identical history-inclusive pane view paste verification
  already uses — one capture-command shape in the codebase, not two.
- `harnesses.py` — the harness id/base-command registry and injectable executable detection behind
  `GET /api/harnesses` and opener resolution. Built-in Claude/Codex/Pi rows intentionally contain no
  static native model/effort vocabulary or mapping; the dynamic capability port and adapter-owned
  launch channels are authoritative. The older mapping helpers remain only for explicit
  settings-defined non-native harnesses. A harness id is on the wire, fixed argv stays in registry
  or validated settings, and normalized native model/effort never becomes a generated session
  command or paste.
- `supervisor.py` — the deterministic supervisor sweep, also the
  P-15 tier-3 ladder + dead-man-respawn host and the
  bounded dead-seat-storm terminator: `SupervisorContext` (the
  one seam every predicate/action reads through — stores + catalog/host/paster, injected directly,
  never the projection, plus the `escalation_sla_seconds`/`escalation_rung_seconds`/
  `respawn_after_rung` plain-primitive knobs and `redeliver_budget`), the eight predicate functions
  (`evaluate_pane_findings`/`evaluate_expectation_findings`/`evaluate_turn_report_findings`/
  `evaluate_inbox_findings`/`evaluate_seat_liveness_findings`/`evaluate_escalation_findings`/
  `evaluate_dead_upstream_findings`/`evaluate_ladder_terminal_findings`), the action dispatcher (`act_on_finding` →
  `_redeliver`/`_auto_nudge`/`_signal_emit`/`_escalate_rung`/`_signal_dead_upstream`/
  `_resolve_ladder_terminal`, each logging an
  `orchestration.supervisor.*` or `orchestration.escalation.rung` event), and `run_supervisor_sweep`
  (one in-sweep inbox snapshot/index → evaluate → bounded act → tick the heartbeat unconditionally,
  now including inbox backlog counts and last sweep duration). Gives `missing_artifact()` its first
  caller; `mark_missed` stays the sweep's own reserved transition, while `mark_escalated` and the
  ladder's own `advance_rung`/respawn/orphan-surfacing (via `escalation_ladder.py`/
  `orphan_policy.py`, governed by the `controlplane/` overview) are now genuinely landed here. Still
  touches no `terminal_paste.py` internals. `_delivery_failure_still_retrying`, a
  guard inside `evaluate_escalation_findings`, lets delivery-failure rows exhaust the redelivery
  threshold before the generic unacked ladder advances them.
- `pane_signals.py` — the pane-state classifier: `classify_pane_signal`
  answers which of the four P-15 intervention triggers (`never-briefed`/`delivery-stalled`/
  `mid-turn`/`blocked`) a captured pane shows, reusing `terminal_paste.count_paste_chips` for the
  chip-count trigger. Distinct from `turn_state.py`'s `classify_turn_state` (a different question
  over the same captured text — deliberately not merged).
  `_HARNESS_BLOCKED_PATTERNS["codex"]` carries the issue #20 quota/rate-limit modal markers, and
  `blocked_reason_label` + `composer_state` are the two signatures `harness_adapters.py` composes.
- `supervisor_heartbeat.py` — the self-liveness primitive (issue #15): an
  atomic-overwrite single-row `SupervisorHeartbeatStore` (`logs/observer/workspace/
  supervisor-heartbeat.json`), `heartbeat_age_seconds`, and `supervisor_staleness_banner` (silent
  when never-ticked, a fail-loud one-liner past the staleness cutoff) — consumed by the MCP tool
  choke point and the dashboard header payload. The heartbeat row also carries volatile
  `pendingInboxCount`, `redeliverableInboxCount`, and `lastSweepDurationSeconds`.
- `harness_adapters.py` — the per-harness delivery adapter: `HarnessAdapter`
  (`boot_ready`/`composer_state`/`mid_turn`/`mid_turn_behavior`/`blocked_reason`/`turn_started`), a
  thin composition over `pane_signals.py`/`turn_state.py` with NO new pattern table of its own, plus
  `get_adapter` (named `CLAUDE_CODE_ADAPTER`/`CODEX_ADAPTER`, generic fallback for any other id) and
  the NEW-HARNESS CHECKLIST (a future harness is one adapter registration, never a new delivery
  path).
- `injector.py` — the ONE delivery path: `deliver(row) -> {acked,
  landed-unacked, blocked(reason), failed(reason)}` — the four-way `DeliveryOutcome` contract every
  payload class (spawn briefs, inbox dispatch/nudge/redelivery/signal rows) now funnels through
  instead of two independent `TerminalPaster.paste` call sites. Wraps `TerminalPaster.paste`
  unchanged, reads `harness_adapters.get_adapter` for the blocked-check (against the FINAL capture)
  and the turn-started corroboration, and never retries itself — retries stay the caller's (the
  supervisor's) decision. `DeliveryRow`'s `envelope=False` on both current callers keeps the exact
  pre-existing wire format for the spawn-brief path and avoids double-heading the inbox path's own
  `_push_text` header.
- `__init__.py` — package docstring only; `delta`/`projector` stay importable without FastAPI.

## Invariants And Boundaries

### Current Authority Boundary

- The conversation products are strict normalized contracts, not proof of a live projector,
  historical store, control service, or renderer.
- Active-transcript and conversation-library cursors are purpose-bound and non-interchangeable;
  status, capability, operation, attachment, and metric claims require their modeled evidence.
- The route owns exactly two read ports and three owned child routers — all now implemented (active,
  library, control), none behavior-empty. Production behavior lands in the owning child
  without creating a second root registration seam.
- Runtime observations and the locked native helper are evidence boundaries. Their versions and
  observed counts do not become feature flags or maintained capability declarations.
- Protocol adapter snapshots, bridge receipts, reconciliation, and normalized transcript entries
  are authoritative for hosted sessions.
- Panes, logs, copy mode, paste echoes, and timing observations are diagnostic-only.
- Hosted delivery starts from a durable inbox row and records adapter evidence without consuming it;
  explicit recipient `consume` remains the sole acknowledgement.
- Legacy raw-TUI and unsupported custom sessions remain explicitly unsupported, with no compatibility
  raw-paste or timing fallback.
- `settings.json`/role resolution supplies the complete typed native initial selection; dynamic
  adapter advertise validates it before the configured vendor session starts.
- Native Claude/Codex/Pi model and effort are applied only through their owned launch channels.
  Free-form duplicate selectors refuse before discovery, and normalized selection is never pasted.
- Startup acceptance remains protocol-honest: Codex/Pi echo effective values; Claude has no effort
  echo and reports exactly that narrower evidence.
- Pre-session daemon advertise uses only dynamic own-adapter discovery. Cache identity includes the
  installed executable/effective argv; explicit refresh owns auth/account invalidation, and failure
  quarantines the observed entry rather than serving it as a current hit.
- A live session's persisted process launch is immutable. Reopen returns that actual row or a
  conflict; only observed-dead replacement may publish a new model/effort/control generation.
- Exact-session set and submit never retry after request bytes may have been sent. Same request ids
  are idempotent, retained known outcomes reconcile locally, and only genuinely unknown outcomes
  invoke native reconciliation without resubmission.
- Public daemon responses are normalized and raw-free; adapter-private `raw` remains inside the
  IPC/diagnostic boundary. Unknown/stopped/dead sessions are 404 before live unsupported sessions
  are classified 409.

The older route bullets below preserve historical implementation context and must not be read as
current hosted-session authority.

- **Control authority is protocol-backed.** Adapter state, bridge receipts, reconciliation, and
  normalized transcript entries are authoritative; tmux panes and terminal logs are diagnostics.
- **Codex app-server compatibility is structured.** The consumed initialize/model/thread messages
  and fields decide compatibility; package-version text is fixture/smoke evidence only. No
  terminal/pane/log fallback is permitted.
- **One epoch-bound submission authority.** Prompt/model/effort work shares the authority timeline;
  adapters dispatch now and may not retain a second queue. Browser drafts are local revisioned state,
  while server status/withdrawal owns delivery and pop-back truth.
- **Exact operation completion.** Only the full epoch/sequence/id/kind ref can release active work;
  early exact terminal evidence may dominate unknown, but stale/id-only/FIFO evidence cannot.
- **Retention and privacy are load-bearing.** Timeline and duplicate ledgers are bounded without
  evicting live/active/unknown work; terminal prompt text is dropped; public status/withdraw is
  cockpit-only and raw-free.

- **Transport only.** No interpretation here — the reducer produces full projections; this
  layer serves them, diffs consecutive snapshots, tails the raw log, and reads precomputed
  action availability. The observer stays a pure fold.
- **Client-agnostic (NS #2).** The served shapes are the existing `WorkspaceProjection`
  nodes verbatim; no dashboard-bespoke endpoints in the reducer. Named per-entity SSE events let any
  client (browser, TUI, agent) merge by id. The operator-inbox POST is a dashboard serving write into
  the shared control-plane inbox, not a projection shape.
- **One read abstraction (NS #5).** Every read flows through `config` + `observer.paths` +
  `project_and_write`; sim mode swaps the root + clock at that one seam.
- **Local-first.** Bind `127.0.0.1` only, no auth in v1 (documented in `app.py`). The UI is
  never the gate *enforcement* (the mutating MCP tools bind it server-side); a gate-decision POST
  does record a developer-attributed gate *decision* (slice 6b).
- **Terminal host = render-not-scrape, fixed argv (slice 6d).** `terminal.py` launches the
  harness on a PTY whose raw bytes xterm.js renders verbatim; the spawn is a `Sequence[str]`
  (never a shell string — no injection surface), runs as the dashboard's own OS user, and
  persists via tmux. PTY attach, detached creation, and termination are injectable for tests. Rehydrate
  probes tmux before using `tmux new-session -A`, and detach remains non-destructive; termination is
  explicit.
- **Two resume models, two streams.** The `state` channel re-snapshots on (re)connect; the
  raw `event` channel resumes by exact byte offset (`Last-Event-ID`) when the client presents a
  valid cursor, while fresh connections do one retained-backlog scan, stream that bounded backlog in
  chunks (heartbeats filtered, no whole-history materialization) instead of replaying every
  historical raw row, and then emit a `ready` marker. They stay separate.
- **One atomic activation/publication owner for folded state.** The projector registers each
  subscriber before capturing its current snapshot, computes each successful tick's event batch
  before mutation, commits `_latest_stable`/`_published` before notification, and removes the exact
  queue on close/cancellation. A failed-prime `None → success` transition emits one full snapshot;
  an identical recovered state emits nothing; later content changes use the normal delta grammar.
  The app decorates this authority but never performs a second current-state handoff.
- **Sim is a seam, not a fork.** Only `now` + `coordination_root` differ from live, so the
  SSE output is byte-identical and replay is deterministic.
- **Containment metrics are observation, not control.** The lifespan's
  sampler is read-only + dockerless-safe, discovers stacks by ownership label (no settings
  needed, leftover stacks stay visible), runs on its own 30s cadence — never the projection
  tick — and never gates or launches providers; a failed pass logs and retries.
- **Change-driven pacing changes when the projector wakes, never what a tick does.**
  The tick body, prime, diff/broadcast, and ETag revision are untouched; a
  busy world keeps the former `--interval` cadence (max-delay = interval + floor); a quiet
  world's `/api/state` staleness and time-derived fields advance at heartbeat resolution
  (default 15s); watcher absence or failure degrades LOUDLY to legacy fixed-interval ticking —
  fail-open, never fail-silent, never a crash. `--sim` replay is always time-driven, and an
  already-running daemon adopts the new pacing only through explicit stop + spawn.
- **The supervisor sweep is stores-not-projections, code-not-model.**
  `supervisor.py` imports nothing from `projector.py`/`observer/reducer.py`; every predicate reads
  its store directly. Own decoupled cadence (settings-controlled, default 10s), zero model calls
  anywhere in the loop, level-triggered (a missed action is caught by the next sweep). The
  heartbeat's staleness is a volatile age (same posture as `servingBuild`): never gates the
  `/api/state` ETag revision.
- **Dead-seat storm termination is narrower than escalation.** A pending row only
  becomes `ladder-resolved` when it is both at the terminal rung and addressed to a provably dead/no-
  hosted-session seat. Live seats and rows still climbing stay pending; redelivery is merely bounded by
  budget/rate limit, not dropped.
- **The escalation ladder never absorbs a dead owner's role.** A spawned seat with a dead owner continues its own brief and escalates to its
  grandparent — `_signal_dead_upstream` only ever signals, never reassigns. Rung 3 (developer
  attention) is a hard ceiling: `escalation_ladder.rung_due` refuses to advance a row past it, so
  re-surfacing happens via the row's own rung-3 dwell SLA firing the same signal again, never a
  state change past the developer. Orphaned workers of a respawned manager are surfaced, never
  auto re-parented.
- **Manual retirement is terminal; landed completion is inspectable archive.**
  A retire rides the EXISTING `status == "terminated"` catalog state plus provenance, so it composes
  for free with the liveness hysteresis (never resurrected) and the "never a zombie row" `list()`
  filter — no new interplay logic. Normal successful completion instead sets `status == "landed"` with
  landing provenance, keeps the row visible for dashboard/WebSocket inspection, and releases leaf
  ownership because active lookup is running-only. Retire authority is enforced server-side, never
  trusted from the caller; refusals are loud and name the exact policy clause. Rename is identity text only — `spawn_role`
  (role-seat immutability) never changes on a rename. Turn-state classification is best-effort and
  fail-safe (an unreadable/blank pane classifies `stale`, never raises) — it rides the existing
  sweep cadence and classifies `kind == "harness"` rows only, never plain terminals.

## Docs References

The resolved Domain Documentation registry has no configured entries for this route. The
structured-conversation contract is grounded in repository code, tests, and redacted observations.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation governed the structured-conversation contract update. | — | — |

## Cross-Repo References

The structured-conversation contract, helper package, fixtures, and tests are all owned by `agents-remember`; no
neighboring repository governs this route.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repository reference was found. | — | — |

## Repo-Internal References

### Current Evidence Substrate

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reserved `arEvidence` key, evidence DTOs, clip/window helpers, and structural native-page protocol define the substrate; the DTOs also carry the multiplexing grammar (`AdapterSnapshot.pending_interactions`, `EvidenceFrame.thread_id`). | L57-L72; L217-L234; L456-L477; L770-L815 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The bounded evidence deque diverts the reserved key at the one consumption point and stamps epochs on every page; `_evidence_thread_id` also stamps the per-thread demux key on every diverted frame. | L167-L234; L548-L610 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| Three additive read actions cross only the private socket under the unchanged v1 protocol. | L213-L218; L380-L401 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| Strict client validation enforces disjoint coordinate domains, continuation coherence, and epoch continuity; `read_control_native_page` takes the additive `threadId` selector and snapshots parse the plural `pendingInteractions`. | L342-L395; L863-L874; L1100-L1152 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| The provenance batch reads the authority's existing records epoch-checked through the sole queue delegation. | L452-L489 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The codex resume channel threads opener → runner payload → factory → the sole settings site with pre-spawn refusals. | L611-L621; L88-L105; L41-L58 | [terminal_opener.py](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py); [harness_control_runner.py](agents-remember/mcp/src/agents_remember/serving/harness_control_runner.py); [harness_control_factories.py](agents-remember/mcp/src/agents_remember/serving/harness_control_factories.py) |
| Contract and installed-runtime suites pin the whole seam including no-leak, continuation, provenance, and resume. | L268-L1470 | [test_harness_control_evidence.py](agents-remember/mcp/tests/test_harness_control_evidence.py); [test_harness_control_evidence_installed.py](agents-remember/mcp/tests/test_harness_control_evidence_installed.py) |

### Current Control-Plane Substrate

| Finding | Citations | Source Path |
| --- | --- | --- |
| The control-plane DTOs/constants and serializers: `InterruptResult`, `OperationTimeline{,Item}`, `AssetReference`, `WithdrawalRecovery`, the additive optionals, and the typed spool reader. | L255-L263; L385-L443; L1046-L1064 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The structural sub-protocols adapters opt into without a base-contract member. | L92-L115 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The bridge's epoch-guarded interrupt dispatch (structural refusal, adapter-mint refusal, bridge-stamped epoch) and timeline delegation. | L291-L355 | [harness_control_bridge.py](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py) |
| The authority's paged never-bodies enumeration, eviction floor, pre-tombstone recovery capture, capability gate, and asset-conditional digest; `respond` matches a response against the singular parent pending OR the plural tuple with the active-operation guard kept parent-only BY ENTRY THREAD (a parent-thread tuple entry is guarded like the singular slot). | L276-L334; L502-L542; L549-L601; L1141-L1162 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The two additive IPC actions and the submit-asset schema/confinement/verification admission under the endpoint's own assets root. | L219-L225; L259-L325 | [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py) |
| The validated client helpers: `interrupt_control`, `read_operation_timeline` coherence/monotonicity/epoch validation, recovery parsing, additive submit assets. | L421-L444; L733-L760 | [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |
| Codex exact-active-turn `turn/interrupt` with replay-once and verified `localImage` construction; the adapter also owns the per-thread demux/registry, collab identity learning, per-thread pending-interaction MAPS (concurrent requests normal traffic, unknown METHODS declined + degraded on any thread), and the load-shed event queue (detail in the file sidecar). | L99-L135; L375-L422; L950-L1071; L1160-L1247; L1309-L1346; L1385-L1469 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| Pi expected-operation-guarded `abort` with replay-once and verified base64 image content. | L393-L477 | [pi_rpc_adapter.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_adapter.py) |
| The content-less `message_end` evidence-only mapping (the abort's own shape) with preserved role strictness. | L226-L244 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |
| Contract and installed-runtime suites pin the whole seam; the fixtures record redacted `control-plane/*` rows without enabling anything. | L252-L1575; L126-L384 | [test_harness_control_plane.py](agents-remember/mcp/tests/test_harness_control_plane.py); [test_harness_control_plane_installed.py](agents-remember/mcp/tests/test_harness_control_plane_installed.py) |

### Current Structured-Conversation Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Strict normalized conversation products encode identity, cursor, provenance, status, capability, operation, attachment, and telemetry authority. | L1-L1282 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |
| Exactly two protocol read ports separate active transcript reads from conversation-library reads. | L1-L87 | [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py) |
| Three owned child routers compose beneath one stable root and one explicit registration function. | L1-L24 | [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The existing harness-control application factory mounts the conversation root once. | L166-L201 | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) |

### Current Folded-State Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| Projector publication computes events, commits authority, and then notifies; subscription activation registers before snapshot capture and cleans up in `finally`. | L207-L269 | [projector.py](agents-remember/mcp/src/agents_remember/serving/projector.py) |
| App streaming consumes one iterator, decorates every snapshot, preserves event/id/retry framing, and owns explicit closure. | L181-L203 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| Deterministic regressions force handoff publication, failed-prime recovery, identical-state silence, later delta, and cancellation cleanup. | L416-L492 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |

### Legacy route map

| Finding | Source Path |
| --- | --- |
| The tick entry the projector drives (read → fold → atomic write; the `now` seam + fixture loader). | [observer/projection_store.py](agents-remember/mcp/src/agents_remember/observer/projection_store.py) |
| The served shapes (`WorkspaceProjection`, `ActionAvailability`). | [observer/projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py) |
| The raw event envelope + log layout tailed by `events.py`/`sim.py`. | [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| The one read/path abstraction (NS #5). | [observer/paths.py](agents-remember/mcp/src/agents_remember/observer/paths.py) |
| The `--config` → `McpRuntimeConfig` contract the CLI mirrors. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The umbrella CLI entry that launches the server (and wires `--sim`). | [cli/__main__.py](agents-remember/mcp/src/agents_remember/cli/__main__.py) |
| The transport design (SSE, snapshot-then-deltas, raw channel, sim, placement). | [docs/design/observable-lifecycle.md](agents-remember/docs/design/observable-lifecycle.md) |
| The containment metrics sampler + store the lifespan loop drives. | [providers/metrics.py](agents-remember/mcp/src/agents_remember/providers/metrics.py) |
| The provider degradation detector the sampling loop also calls once per tick; governed by the `mcp/` package overview. | [providers/degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py) |
| The stores the supervisor sweep's predicates read directly: expectation rows, operator inbox, orchestration nudges, supervisor signal cooldowns, and the observer event log the sweep appends `orchestration.supervisor.*` events to. | [controlplane/expectation_rows.py](agents-remember/mcp/src/agents_remember/controlplane/expectation_rows.py); [controlplane/operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py); [controlplane/orchestration_nudges.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_nudges.py); [controlplane/supervisor_signals.py](agents-remember/mcp/src/agents_remember/controlplane/supervisor_signals.py); [observer/store.py](agents-remember/mcp/src/agents_remember/observer/store.py) |
| The `orchestration.supervisor` settings family (interval/enable/staleness cutoff/redeliver rate limit/signal cooldown/redeliver budget) `app.py`'s supervisor loop re-reads per-use. | [kernel/agentic_settings.py](agents-remember/mcp/src/agents_remember/kernel/agentic_settings.py) |
| The MCP tool choke point that surfaces the supervisor staleness banner on every tool call. | [mcp/tools/base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py) |
| The sole epoch-bound prompt/setter timeline and its authoritative status/withdrawal model. | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |
| The daemon/IPC/client boundary for raw-free lifecycle operations and first-byte classification. | [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py); [harness_control_ipc.py](agents-remember/mcp/src/agents_remember/serving/harness_control_ipc.py); [harness_control_client.py](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) |

## Historical Route Impact (superseded hosted authority)

Serving implements exact-session readiness, copy-mode rechecks, calibrated settling beyond the shipped 120 ms suppression window, harness-log proof, and pending-without-respawn recovery. Catalog writers serialize the complete one-read/one-write batch across processes while atomic readers remain lock-free.


### Current Capability Contract

Claude, Codex, and Pi production adapters launch the installed/current harness and validate the
structured capabilities, messages, and fields they consume. Missing, malformed, or contradictory
required evidence fails loudly; exact 2.1.207, 0.144.3, and 0.80.6 values are fixture/smoke
evidence only. Rolling inbox compatibility remains limited to optional `adapterDeliveryState`
and `adapterDeliveryDetail`; unrelated extras remain rejected. Resource performance work is queued
and not implemented or current behavior.

### Codex Completion Correlation

The Codex adapter owns the null-requestId/vendor-correlation mapping and terminal projection. It
must consume structured protocol messages and fields and fail loudly on missing, non-text,
unmatched, or ambiguous correlation evidence; exact 2.1.207, 0.144.3, and 0.80.6 values remain
fixture/smoke evidence only. The matched row receives adapter completion metadata without explicit
inbox consumption, and only an actual replacement permits `settling` / `queued`; otherwise the
terminal snapshot is `idle` / `immediate`. Inbox compatibility remains limited to optional
`adapterDeliveryState` and `adapterDeliveryDetail`, with unrelated extras rejected. Resource performance remains queued and unimplemented.

### Hosted Protocol Cutover

Claude, Codex, and Pi hosted sessions now launch through the shared bridge. Exact adapter snapshots
govern readiness, delivery, liveness, interactions, and terminal projection. Durable inbox rows are
the only inter-agent message roots: adapter receipts record delivery evidence, while explicit consume
acknowledges receipt. Custom and already-running raw-TUI sessions are explicitly unsupported, and
pane/turn/log classifiers remain diagnostics-only. Dashboard and packaged assets stay additive and
must remain synchronized.

## Hot-Path Performance And Diagnostics Route Impact

The serving hot path is both cheaper and more explicit: one published projection supplies the `/api/state` and snapshot body memo, per-response volatile fields are injected outside that memo, ordinary JSON is gzip-compressed while SSE stays streaming, and repository discovery is single-pass/TTL-cached. The route also adds bounded dashboard shutdown, opt-in heap diagnostics/allocator trimming, honest dirty-build marking, structured interaction responses, native Claude interrupt support, and capability-aware terminal frame synchronization.

Route indexes are intentionally not regenerated during a partitioned documentation pass; a single aggregate refresh runs after all ownership is complete. Existing verification metadata remains pre-commit.

## Sub-Agent Multiplexing Route Impact

Harness sub-agents became first-class across the control substrate: the bridge extracts
`threadId` into every evidence frame (`_evidence_thread_id`; missing/malformed degrades to the
parent thread, never guessed), snapshots carry the multiplexed `pending_interactions` tuple
end-to-end (catalog column `control_pending_interactions` → hosted projection → API
`pendingInteractions`; the singular slot stays the parent-thread entry), the authority's
`respond` matches a response against the singular parent pending OR the plural sub-agent tuple
with the active-operation guard explicitly parent-only, the codex adapter owns the per-thread
demux/registry with collab identity learning and degrade-never-fatal agent frames, and claude
launches with the floor-gated `--forward-subagent-text` (floor 2.1.220) only after `system/init`
proves the floor. Every change is additive; single-thread sessions stay byte-identical.

That floor gate makes the Claude subprocess transport a RESTARTABLE resource rather than a one-shot:
the adapter stops and re-launches the same transport object to add the flag, so
`claude_stream_transport.py` releases its process and stderr-task ownership as the final step of a
completed stop, while a start against a live process still refuses. The refusal and the release are
one contract — a transport that kept its terminated process turned every at-or-above-floor install
into an `unsupported` handshake, which is what removed control readiness and the dashboard's
model/effort selection before 260727-CHATS-IM-L4.

The remediation pass closed the two multiplexed-production kill seams. Concurrent server requests
are now normal traffic: the adapter keeps a bounded per-thread pending-interaction MAP keyed by
rpc id (the "multiple unresolved server requests" raise is deleted; the vendor keeps a global
pending map), the singular slot carries the parent's OLDEST pending, an unknown/experimental
request METHOD is declined (`respond_error` -32601) and degraded on ANY thread while a known
method's malformed shape keeps the agent-degrade/parent-fail split, the projector projects ALL
pendings (concurrent parent ones plainly) with singular-rotation resolution semantics, and the
authority's parent guard follows the entry's own thread (a parent-thread tuple entry is guarded
like the singular slot). And the adapter event queue no longer raises queue-full: it sheds the
oldest high-volume delta events first (structural events survive), counts every shed, and emits
one `ar/load-shed` notice with the count when the consumer catches up (queue 256→1024).

Route indexes are intentionally not regenerated during a partitioned documentation pass; a single aggregate refresh runs after all ownership is complete. Existing verification metadata remains pre-commit.

## Codex Native-History And Selected-Child Route Impact

Codex history now has separate compatibility/resource layers: the 128 MiB JSON payload fuse in
`codex_app_server_protocol.py`; runtime-probed items/turns/explicit-legacy acquisition plus the
16 MiB complete source-response ceiling and 64 MiB/64-walk continuation LRU in
`codex_app_server_history.py`; typed preservation over control IPC; and selected-child-only active
projection. The fuse is shared-fatal above its boundary and is never history paging.

The active serving child now owns three routes. Parent paging discovers children from metadata/live
events without hydrating all of them; the selected-child POST performs native I/O outside the
projector apply lock, singleflights same-child work, caps concurrent reads at 64, and converts only
typed native-history outcomes into child-local unavailable/recovered state. The separate dormant
`conversation/library/codex.py` full-read path remains a follow-up exposure.

## 260731-EFA-L2 Route Impact — named concepts replaced parameter lists

Enforcing `PLR0913` (Ruff's default max-args of 5) and the complexity codes at full strength, with
no per-file ignore or `noqa` anywhere in this route, turned this route's long parameter lists into
named values. The rule for reading the rest of this overview: **wherever a description below names
a keyword that no longer exists, the concept it belonged to is one of the values listed here.**

Three modules are new:

| Module | Concept |
| --- | --- |
| `cadence.py` | `ProjectionCadence(interval, heartbeat)` — one pacing decision; stdlib-only so `daemon.py` can name it without importing the projector. |
| `hosted_session_runtime.py` | `HostedSessionRuntime(catalog, host)` — the durable row and the tmux process that jointly decide which hosted sessions exist. |
| `conversation/active/projector/wiring.py` | `SessionProjectionSpine` + `BridgeReaders` — one projection, one session, one epoch, made structural. |

The concepts introduced across the existing modules, grouped by what they name:

- **Composition / substitution seams.** `ServingCollaborators` + `LiveProjectionInputs` +
  `_ServingRuntime` (`app.py`), `ProjectionReplay` + `ProjectionRefreshers` (`projector.py`),
  `TerminalHostSeams` (`terminal.py`), `TerminalPasterSeams` (`terminal_paste.py`), `LivenessProbe`
  (`terminal_liveness.py`), `AppServerSeams` (`conversation/library/codex.py`), `GateProbes`
  (`conversation/library/gates.py`), `ConfigurationPorts` (`pi_rpc_configuration.py`),
  `BridgeSnapshotPort` (`harness_submission_authority.py`), `BridgeReaders` (projector `wiring.py`).
  Every one of them exists because **partial substitution observes a world that does not exist**.
- **Bounds chosen as one budget.** `BridgeLimits` (`harness_control_bridge.py`), `SubmissionLimits`
  (`harness_submission_authority.py`), `PiAdapterLimits` (`pi_rpc_adapter.py`),
  `TerminalCatalogLivenessConfig` (now in `terminal_catalog.py`), `AcceptanceWindow` +
  `PasteRecoveryLadder` (`terminal_paste.py`), `EscalationSchedule` (`supervisor.py`),
  `ReadinessWait` (`hosted_readiness.py`), `BoundedPageRequest` (`codex_app_server_history.py`).
- **Identity / scope that must travel together.** `TerminalLaunchRequest` + `SpawnProvenance` +
  `SpawnKnobs` + `ControlRunnerRequest` (`terminal_opener.py`), `TerminalSessionSpec`
  (`terminal.py`), `DaemonEndpoint` (`daemon.py`), `ControlRequest` → `ControlScope`
  (`conversation/control/service.py`), `RefBinding` + `RefTarget` (`conversation/control/refs.py`),
  `ControlSubmission` (`harness_control_client.py`), `ProjectedSession` (projector `facade.py`),
  `LibraryBinding` + `OpenRequest` (`conversation/library/open_service.py`), `ChangesetFileRef`
  (`changeset.py`), `ClaudeStreamSession` (`claude_stream_state.py`).
- **One attempt / one observation.** `WithdrawalTicket` (`conversation/control/withdrawals.py`),
  `InterruptTicket` (`conversation/control/operations.py`), `TurnTransition`
  (`conversation/active/status.py`), `SubmittedContent` (`conversation/control/attachments.py`),
  `StartedTurn` (`codex_app_server_adapter.py`), `TranscriptCorrelation`
  (`claude_stream_state.py`), `SeatClosure` (`retire.py`, also written by `landing.py`),
  `OwnerSignal` (`supervisor.py`), `_DeliveryOutcome` + `InboxDeliveryLog` + `RedeliveryFloor` +
  `DeliveryAdmission` (`inbox_delivery.py`), `ExpectedEcho` (`harness_control_claude.py`),
  `StagedAssetClaim` (`harness_control_ipc.py`), `ItemPlacement` + `_LiveItemContext` +
  `_CollabCall` (`conversation/projectors/codex.py`), `_TaskIdentity`
  (`conversation/projectors/claude.py`), `IngestionComponents` (projector
  `rebuild_coordinator.py`), `StageAttachmentsForm` (`conversation/control/api.py`),
  `ActionEvaluationContext` (`actions.py`, now built by the caller).

**Deletions in this route, at the cause rather than covered by a test:**

- `terminal_opener.py` lost its legacy pre-bridge argv path. `_live_open_result` is now the single
  place a live row is handled; everything past it is a spawn, so `_reopen_state` no longer probes
  the host and `_control_metadata` mints control columns instead of inheriting them.
- `app.py` lost two duplicated request-shape guards (the `missing-gate-id` re-check and the
  dismissal scope re-check). Request validation lives once, in `actions.py`, which already refuses
  both shapes with 400 `missing-target` / `missing-lifecycle`.
- `harness_submission_authority.py` reduced its dispatch-time asset-capability guard to an assert;
  `_unsupported_prompt_locked` is the single capability decision point, deciding under the same lock
  that enrols the record.
- `terminal_paste.py` lost its "dispatch paste requires a harness-log acceptance probe" `ValueError`:
  `paste_dispatch` requires the probe in its signature, and `paste()` no longer accepts a dispatch
  policy at all.
- `harness_control_client.py` lost its "operation timeline item requires lifecycle state" re-check:
  `_submission_state` now raises for anything outside the seven states unless `optional=True`.
- `harness_control_ipc.py` collapsed two `if action == …` chains into one `_CONTROL_ACTIONS` table
  with one unknown-action refusal.

**One relocation:** `TerminalCatalogLivenessConfig`, `DEFAULT_LIVENESS_HYSTERESIS` and the four
`DEFAULT_LIVENESS_*` constants moved from `terminal_liveness.py` to `terminal_catalog.py`.

This entry supersedes any earlier description in this overview that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

## Update History

- 2026-07-31T21:02+02:00 — 260731-EFA-L3 curator: corrected the `build_info.py` Route Model bullet,
  which described the build stamp's honesty rules without saying which repository the stamp reads.
  `_git_short_head` and `_git_worktree_dirty` no longer own local `subprocess.run` calls; both now
  call `run_git` (`kernel/git_command.py`), whose `GIT_DIR`-family scrub is what guarantees the
  stamp identifies the checkout the server booted from rather than an inherited one — the property
  the whole ghost-process surface depends on. The 2s bound is now the named `_PROBE_TIMEOUT_SECONDS`
  passed explicitly against the runner's `GIT_LOCAL_TIMEOUT_SECONDS = 300`. `ServingBuild`'s fields,
  the tri-state `dirty` fail-open rule and the version-only fallback are unchanged, as is every
  other serving surface. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 4 cross-file line citations. The codex
  adapter row now cites each thing it names: `_ThreadState` L99-L135 (per-thread demux), `interrupt`
  L375-L422 (exact-active-turn `turn/interrupt` with the `_last_interrupt` replay-once pair),
  `_handle_server_request` → `_sync_pending_snapshot` L950-L1071 (per-thread pending-interaction
  maps, the `PENDING_INTERACTIONS_PER_THREAD` cap, unknown-method declines), `_enqueue` →
  `_verified_asset_path` L1160-L1247 (load-shed queue and verified `localImage` construction),
  `_thread_for` L1309-L1346 (registry with `THREAD_REGISTRY_LIMIT` eviction) and
  `_learn_collab_identity` → `_publish_agent_registry` L1385-L1469. `models.py` is 1282 lines, so
  the whole-module row is L1-L1282. The harness-control factory row is
  `register_harness_control_routes` L166-L201, whose L179 is the single
  `register_conversation_routes(app, runtime)` call. The regression row is `StreamEventsTests`
  L416-L492 — later delta, interleaved-projection handoff, failed-prime recovery (whose L473-L478
  is the identical-state silence), and cancellation cleanup. All ranges read back; no claim text
  changed.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: added the route-impact section naming every parameter object introduced in this route, the three new modules (`cadence.py`, `hosted_session_runtime.py`, `conversation/active/projector/wiring.py`), the six deletions made at the cause, and the liveness-config relocation; corrected the `create_app` signature in the Route Model. Verification metadata stays pinned until closeout.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: the cockpit bundle and its fingerprint sidecar
  left version control and are now built at release, so a source checkout legitimately serves no
  cockpit. Recorded `static.py`'s new missing-bundle surface (503 with expected location and build
  command under `no-store`, GET/HEAD only with 405 elsewhere so the greedy `/` mount cannot change
  `/api` method semantics, no placeholder or fallback UI) and the shift in `dashboardBuild` from
  "absent means legacy bundle" to "absent means no build happened here". Verification metadata
  remains pre-commit.

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: gave the Claude subprocess transport's restart contract
  a route-level home — a completed stop releases process and stderr-task ownership so the floor-gated
  re-launch can reuse the object, while a live start still refuses — and named the control-readiness
  and model/effort loss that a retained process caused.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: recorded the transport/source/cache/output
  boundary split, runtime-probed history reader, typed IPC, selected-child active route, necessary
  capacity bounds, parent/sibling continuity, and dormant library follow-up. Refreshed the active
  hot-path route count. Verification metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the multiplexing remediation in the
  route-impact section — per-thread pending-interaction maps (concurrency is normal traffic; the
  multi-request raise deleted), the method-first degrade split (unknown/experimental request
  METHODS decline + degrade on any thread; known-method malformed shapes keep the old split), the
  entry-thread parent guard in the authority's `respond`, the projector's all-pendings projection
  with singular rotation, and the load-shed adapter event queue (256→1024, shed-oldest-deltas,
  counted, one `ar/load-shed` notice on catch-up). Re-anchored the authority (L276-L334;
  L502-L542; L549-L601; L1141-L1162) and codex-adapter (L356-L403; L681-L847; L1056-L1122)
  reference rows against the post-remediation source. Aggregate route-index generation remains
  manager-owned; verification metadata stays pinned (remediation uncommitted).
- 2026-07-26T15:52 — 260718-CHATS-L7 curator: recorded the sub-agent control-substrate changes
  (evidence `thread_id` demux, plural pendings end-to-end, parent-only authority respond guard,
  codex per-thread registry, claude floor-gated sub-agent text flag) and re-anchored the L0E/L2E
  substrate citation ranges the L7 insertions shifted (verified against the current worktree
  source). Aggregate route-index generation remains manager-owned; verification metadata stays
  pinned (L7 uncommitted).
- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: recorded the half-time functional fixes across
  the conversation slice (detail in the `conversation/` sub-overviews). R4 version-gate REMOVAL
  (developer ruling 2026-07-21): THE CONTRACT IS THE ONLY GATE — no version-string comparison gates or
  demotes any capability at any of the seven former sites (grep-proven); observed runtime/helper
  versions are informational metadata only; corrected the L1 capability line's now-false "installed
  2.1.214 vs locked 2.1.211" version-demotion wording to the never-probed contract reason. Also landed
  in this leaf: R1 codex notification identity (`EvidenceFrame.native_method` carried; the codex
  projector drops the known 0.144.5 startup burst by method, names truly-unknown methods), R2 claude
  acceptance (requested-alias-wins-on-resolved-model), R3 claude 2.1.216 frame contracts
  (`command_lifecycle`/`rate_limit_event`), R5 per-session bounds/release (`_locks`/`queue_rows`
  bounded; dormant projector idle-release; `release_session` unwired — F1 accepted-bounding), R6 the
  honest control-socket exit note + the bounded `providers/metrics.py` docker-ps timeout, and the
  durable `dashboard/e2e-chats/` opt-in suite (R7). Verification stays pinned until L5F closeout.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: extended the `terminal_liveness.py` bullet with
  the H1/F2 hosted-interaction synchronizer quarantine — `_observe_control_snapshot` contains a
  poisoned `on_control_snapshot` failure fail-loud on its own row instead of aborting the whole
  catalog sweep + 500-ing `/api/terminal/sessions`, with the load-bearing fact that an orphan
  `vendorCorrelationId` is the normal steady state of cockpit-driven hosted chats (so this path is
  hot) and F2's log-on-state-change bound; the completion-correlation contract is unchanged (F3
  master-exit, F8 residual). The twin-projection + input-authority-pin fixes land inside the active
  conversation slice, whose detail is routed to `conversation/overview.md` and its child governors,
  leaving this route's conversation paragraph accurate. Verification metadata stays pinned until L5
  closeout stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: added the "260718-CHATS-L3 implements the control
  child" paragraph to the structured-conversation contract section — the seventeen control routes
  (interrupt, source-aware queue with cockpit-only withdrawal recovery, typed attachments, read-only
  policy, evidence-bound telemetry) over the closed L2E/L3E substrate, routed to
  `conversation/control/overview.md` — and corrected the L5-authority-boundary invariant from "three
  behavior-empty child routers" to the now-implemented reality (active L1, library L2, control L3).
  The substrate contracts, hot paths, and route model are unchanged. Verification metadata stays
  pinned until L3 closeout stamps the candidate commit.
- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: No route impact: the L3E clip-envelope
  terminal-identity preservation is a file-level additive refinement of `clip_evidence_payload`
  (documented in the `harness_control_models.py` sidecar); the route overview's L0E "32 KiB clip
  with a visible marker" description and the L2E content-less `message_end` note both remain
  accurate and complete for the clip semantics this route describes. Verification metadata remains
  pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the additive native control-plane
  substrate — the structural-sub-protocol interrupt write (bridge epoch guard, codex exact-turn,
  pi expected-operation guard, replay-once, claude fail-closed, settlement untouched), the paged
  never-bodies operation-timeline enumeration with eviction-floor honesty, the digest-verified
  asset channel with resolve-and-verify spool confinement and native codex/pi construction, and
  the once-only withdrawal-recovery payload — plus a hot-path entry and a Current-L2E reference
  section. Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  library paragraph/hot-path/history with the L1 active-serving content after the master memory
  branch advanced; both implemented slices are documented under the L9/L0 contract section with
  detail routed to `conversation/overview.md` and the `conversation/active/`,
  `conversation/projectors/`, `conversation/library/` governors. Verification metadata remains
  pinned until L1 closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: documented the implemented active
  conversation serving under `serving/conversation/active/` and the per-harness mappers under
  `serving/conversation/projectors/` — the two authorized production routes, signed cursor
  authority, the bounded per-app service and projector engines, the idempotent store with the
  review-F1 tool block union, the canonical status service now also backing orchestration's
  seat projection, and fixture-gated capabilities — consumed from the untouched L0 composition
  and L9 contract; detail routed to `conversation/overview.md` and the new
  `conversation/active/overview.md` + `conversation/projectors/overview.md`. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the implemented native
  conversation library under `serving/conversation/library/` — authorized list/read routes,
  live capability gates, the per-app signed cursor/key authority, narrow-only scope, the
  locked-helper and direct app-server ports, and the idempotent exact open/status/reconcile
  service with honest retirement — consumed from the untouched L0 composition and L9 contract;
  detail routed to `conversation/overview.md` and the new `conversation/library/overview.md`.
  Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive native evidence and
  resume substrate — reserved-key diversion into the bounded bridge evidence deque with byte-
  identical projections, the three epoch-scoped additive IPC reads across two disjoint coordinate
  domains, per-harness stop-dropping forwarding and codex/pi native pages (claude honestly
  fail-closed), the sole-path submission-provenance batch, and the codex-only resume launch
  channel. Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the conversation runtime
  composition repair — one immutable app-scoped `ConversationRuntime` installed once through the
  existing harness-control registration, the server-resolved local-operator authorization ruling,
  and the two request dependencies that keep child leaves out of the shared composition files.
  Verification metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: refreshed the serving route for one atomic
  projector subscription/publication owner, publish-before-notify ordering, one full failed-prime
  recovery snapshot with identical-state silence, ordinary later deltas, and explicit iterator/
  subscriber cleanup. Root and `mcp/` ancestors were inspected and remain accurate at their
  public-surface granularity. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: added packaged-client identity, HTML revalidation, narrow
  pre-session discovery, record-safe raw cursor semantics, and owned tmux-client environment.
  Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the strict normalized
  structured-conversation roof, separate active/library read ports and cursor purposes, three
  behavior-empty owned child routers, single harness-control registration seam, and the rule that
  helper/fixture observations cannot promote capabilities. Verification remains pinned to the
  last committed source until closeout stamps the candidate.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: established the sole
  `HarnessSubmissionAuthority` current contract; documented epoch/full-ref identity, atomic
  withdrawal-vs-dispatch, event-before-publication completion, early-terminal dominance, response
  bypass, safe-retry certificate, raw-free status, bounded retention, and dispatch-now native
  adapters. Marked the former queue facade and ACPUI queue semantics historical.
- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: recorded discovery-only Claude MCP-selector
  replacement across the accepted argv grammar, byte-preserved normal startup, the live three-harness
  acceptance asymmetries, dynamic evidence boundary, and the visible non-leaking startup-failed stop
  residual. Verification metadata remains pinned until closeout stamps the L5 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: documented the daemon advertise/launch/set/
  submit/reconcile boundary, bounded install/auth cache and failed-refresh quarantine, exact-session
  first-byte ambiguity and request-id idempotency, raw-free public serialization, liveness-first
  status ordering, and cross-process live-reopen truth with fresh dead replacement. Preserved
  settings-owned role spawn and the durable inbox/brief bus. Verification metadata remains pinned
  until closeout stamps the L4 code commit.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: documented the normalized same-session set
  graph, exact `SetResult` truth table, shared queue ordering and cancellation reclamation, Claude
  exact correlated replay-plus-terminal evidence with the live Fable correction, Codex ordered
  desired/pending/effective fresh-turn behavior, Pi bounded coherent error/clamp readback, and the
  transitive no-paste boundary. Preserved role-based spawn and durable-bus ownership. Verification
  metadata remains pinned until closeout stamps the L3 code commit.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented the typed settings-resolved launch
  path, pre-discovery owned-selector refusal, token-free dynamic validation, Claude/Codex/Pi native
  launch channels and asymmetric acceptance evidence, persistent exact launch failures, roleless
  Codex temporal default, and retirement of static/paste native knob mapping. Final audit removed
  a duplicate capability/adapter route inventory so the current contract has one governing home.
- 2026-07-15T20:04+02:00 — 260714-ACPUI-L1 curator: documented the normalized own-adapter
  capability port, dynamic token-free Claude/Codex/Pi catalog paths, model-gated effort, cached
  running advertise, and transient prompt-free discovery. Verification metadata remains pinned
  until closeout stamps the L1 code commit.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented the narrow IPC peer-disconnect reply/close
  boundary and delayed-reply bridge reconciliation result.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: documented protocol-owned Codex null-requestId
  correlation, same-row pending completion, loud failures, and replacement-only queued state.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: historicized obsolete exact-version
  language in the serving route model and made structured consumed capabilities normative.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the serving route for structured capability
  negotiation and the complete reload boundary; recorded R10 as deferred.
- 2026-07-14T15:00:00+02:00 — PHA-ME-FL2: reconciled the serving route's normative hosted authority to protocol
  snapshots, inbox-rooted delivery, explicit consume acknowledgement, and diagnostic-only panes/logs.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: refreshed hosted cutover, bridge semantics, legacy unsupported,
  dashboard/package parity, R13 inbox-rooting, R14 explicit consume, and diagnostic-only pane signals.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: documented the unregistered, exact Claude Code
  2.1.207 stream-json adapter. Readiness is structured initialize/system-init only; replay acceptance
  is distinct from terminal completion; and disconnect reconciliation never resends. The pinned live
  smoke uses the local `/cost` command. API-429 terminal frames remain failed and retain only safe
  status metadata, never result text or credentials. Verification remains pinned until closeout.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator: added the stable Codex app-server route model,
  exact `0.144.3` protocol pin, protocol-only reasoning effort, structured interaction and
  reconnect boundaries, and explicit no-registration/no-cutover scope. Verification remains pinned
  until closeout stamps the leaf commit.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: documented the unregistered pinned Pi RPC
  protocol/process/event/adapter chain, strict framing, settlement, UI, and cursor-reconciliation
  boundaries. Verification metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator refresh: added the normalized control contract,
  one-adapter bridge, bounded shared queue, private IPC, transcript/draft surface, unsupported
  adapter boundary, and deliberate no-production-cutover scope to the serving route.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3 route impact (change-driven projection pacing): route
  gains `change_watcher.py` (derived watch roots + input-event filter + `ChangePacer` +
  `ProjectionInputWatcher` on the new `watchfiles>=1.1,<2` core dep); `projector.py`'s
  unconditional `sleep(interval)` became change-or-heartbeat waking when a watcher is injected
  (tick body untouched; loud fixed-interval fallback; `projection_count`/`last_wake_reason`);
  `app.py` gained `heartbeat=`/`watch_changes=` (watcher iff `before_tick is None`);
  `cli/dashboard.py` + `daemon.py` gained `--heartbeat` (default 15s) with `--interval`
  re-documented as the fast-path cadence floor. Why: the projector re-projected the whole world
  every 1s regardless of change — py-spy 2026-07-12 showed `_tick_sync` at 11.1s of a 15s sample.
  Change-driven delta latency ≈ debounce + projection time (measured ~0.2s); adaptive pacing
  reaches a live daemon only via explicit stop + spawn. Adversarial review INTEGRATE with two
  adopted hardenings (inbox-lock filter, retryable root derivation). Updated the Hot Path Summary,
  the `app.py`/`daemon.py`/`projector.py` Route Model bullets, and added the `change_watcher.py`
  bullet + pacing invariant. Verification metadata pinned until closeout stamps the PTS-L3 commit.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: refreshed the serving route for the new
  inbox-reclamation policy, one-catalog-read/one-snapshot boundedness, same-sweep compaction before
  redelivery, body-free aggregate telemetry, no-op silence, 5-second lock-hold characteristics,
  and F3-F6 non-blocking reviewer residuals. Verification metadata remains pinned until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: serving lifecycle wiring starts and cancels the landing refresher outside the projection tick and preserves host shutdown after refresher failure.
+## 260712-TRH-L4 Route Impact

Serving implements exact-session readiness, copy-mode rechecks, calibrated settling beyond the shipped 120 ms suppression window, harness-log proof, and pending-without-respawn recovery. Catalog writers serialize the complete one-read/one-write batch across processes while atomic readers remain lock-free.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-12T12:55+02:00 — 260712-TRH-L2 route impact: `changeset.py` now scopes contract discovery to the requested master enclosure, canonicalizes persisted/requested leaf ids, and exposes an opt-out for expensive master leaf summaries while retaining the net range semantics. Verification metadata pinned until closeout stamps the L2 code commit.

- 2026-07-10T18:30+02:00 — No route impact: 260707-HFX2-L18 replaced repeated terminal-catalog
  optional-field parsing/projection branches with typed helpers and added a complete round-trip
  regression. Required/optional/legacy JSON semantics and the serving route's ownership are
  unchanged; the work is a strict-CRAP quality decomposition within the existing catalog module.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 serving route impact: added the seat-binding module,
  pair catalog/open/attach/retire semantics, binding-first supervisor/landing behavior, explicit
  role-required attach, and sweep-clock delivery persistence. Verification metadata remains pinned
  until closeout stamps L17.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 serving route impact: replaced pane-rendering acceptance
  with bound harness-log evidence, added calibrated duplicate-safe recovery and catalog provenance,
  explicit Codex argv, replacement-leaf support, and one-row supervisor redelivery. Verification
  metadata remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 route impact: added live virtual-cursor river
  compaction, the on-demand task-body endpoint, chain-aware/current-manager supervisor behavior, and
  one-rung-per-row-per-sweep enforcement; recorded the unbound-worker S1 follow-up. Verification
  metadata remains pinned until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: reviewed route impact for the CS-6 store/projection/process scaling sweep and updated the route summary for changed files. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T13:07+02:00 — 260707-HFX2-L11 (landed chat archive): route gained `landing.py`,
  `TerminalCatalog.status == "landed"` + landing provenance, `seat_events.log_landed_event`, and
  `POST /api/terminal/landed-cleanup`. Successful integrate/finalize paths now auto-land seats for
  archive inspection instead of auto-retiring/killing them; manual retire remains the terminating path.
  Verification metadata remains pinned until closeout stamps the HFX2-L11 commit; route index was not
  refreshed in this worker seat because the brief forbids route-index tools.

- 2026-07-09T11:19+02:00 — 260707-HFX2-L9 route impact: supervisor redelivery now passes the
  configured/shared 900-second floor through delivery snapshots; pane/seat-liveness signal emission
  checks persisted cooldown state before posting repeated owner inbox rows; `pane-signal: mid-turn`
  is skipped as busy-state noise; and `app.py` wires the new cooldown store/settings into
  `SupervisorContext`. Verification metadata pinned until closeout stamps the 260707-HFX2-L9
  commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 route impact (dead-seat storm, R1-R6): `supervisor.py`
  now builds one in-sweep inbox snapshot/index, resolves terminal-rung dead/no-hosted-session rows
  to durable `ladder-resolved`, limits redelivery actions by `redeliver_budget`, and ticks heartbeat
  metrics with pending/redeliverable backlog counts and last sweep duration. `supervisor_heartbeat.py`
  carries the new volatile fields; `app.py` forwards the budget from settings and surfaces the
  metrics on `/api/state`/SSE; `inbox_delivery.py` accepts the shared current snapshot. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 route impact (P-15 tier 3 escalation ladder + dead-man
  respawn, R1-R6): `supervisor.py` gains two predicates (`evaluate_escalation_findings`/
  `evaluate_dead_upstream_findings`) and two actions (`_escalate_rung`/`_signal_dead_upstream`),
  calling through NEW `controlplane/escalation_ladder.py` (the pure rung walker) and
  `controlplane/signal_routing.py`'s NEW two-hop `derive_skip_level_owner`/`is_seat_dead` (a
  SEPARATE function from L1's one-hop `derive_signal_owner`, which is unchanged). Past the respawn
  threshold, `_escalate_rung` calls new `_respawn_suspect`: retires the suspect seat via
  `retire.py::retire_entry`, re-delivers its pending queue to the successor, and — via NEW
  `controlplane/orphan_policy.py::find_orphaned_workers` — surfaces (never auto-reparents) a retired
  manager's still-running workers in the same respawn event. `SupervisorContext` gains
  `escalation_sla_seconds`/`escalation_rung_seconds`/`respawn_after_rung`; `OperatorInboxEntry`
  gains `rung`; `OperatorInboxStore` gains `advance_rung`. No new lifespan task, no new
  `InboxMessageKind` values. Verification metadata pinned until closeout stamps the
  260707-HFX2-L4 commit.
- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 route impact (paste injector hardening, R1-R5): route
  gains `harness_adapters.py` (the one per-harness delivery adapter interface — claude-code, codex,
  generic fallback) and `injector.py` (the ONE delivery path, `deliver(row) -> {acked, landed-
  unacked, blocked(reason), failed(reason)}`). `inbox_delivery.py::deliver_inbox_entry` and
  `mcp/tools/terminal.py::_deliver_spawn_pastes` (the spawn-brief path) both now route through
  `injector.deliver` instead of calling `terminal_paste.TerminalPaster.paste` directly — the
  raw-spawn seam's separate delivery loop is retired into the same path the inbox/supervisor side
  already used. `pane_signals.py` gained `_HARNESS_BLOCKED_PATTERNS["codex"]` (issue #20 quota/
  rate-limit modal markers), `blocked_reason_label`, and `composer_state`; `turn_state.py` gained
  `boot_ready`. `TerminalPaster`/`terminal_paste.py` and `InboxDeliveryState`'s four existing values
  are UNCHANGED (a `blocked` outcome rides as a `NEEDS-ATTENTION:`-prefixed `deliveryDetail` string,
  a deliberate scoping decision to keep this leaf off the dashboard type and `inbox_backoff.py`).
  Every pre-existing test in `test_terminal_paste.py`, `test_pane_signals.py`, `test_supervisor.py`,
  `test_terminal.py`, `test_spawn_agent_session.py`, and `test_operator_inbox.py` passes UNCHANGED.
  Covered by two new suites: `test_harness_adapters.py` (per-harness fixtures: boot/ready/mid-turn/
  chip-stacked/quota-modal for both harnesses) and `test_injector.py` (every `DeliveryOutcome`
  branch + an end-to-end injection test against a scripted in-memory tmux pane). Verification
  metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (supervisor sweep + predicates, R1-R6):
  route gains `supervisor.py` (the deterministic sweep — five R2 predicate families, R4 action
  dispatcher, `run_supervisor_sweep`), `pane_signals.py` (the R2a pane-state classifier), and
  `supervisor_heartbeat.py` (the R5 self-liveness store). `app.py` gains a third lifespan task
  (`supervisor_loop`, following the `metrics_loop` template) and `supervisorHeartbeat` on
  `/api/state`/the SSE snapshot. Gives `missing_artifact()` its first caller and reserves the
  `mark_missed`/`mark_escalated` transitions for HFX2-L4's ladder. Covered by
  `test_pane_signals.py` (8 tests) and `test_supervisor.py` (16 tests, including one seeded-drift
  sweep integration test). Verification metadata pinned until closeout stamps the 260707-HFX2-L2
  commit.
- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 route impact (release-tail supervisor fix): the route's
  existing `supervisor.py` path now defers generic unacked escalation for `"no-hosted-session"` and
  `"unconfirmed"` delivery-failure rows until `PERSISTENT_FAILURE_ATTEMPTS` or an explicit
  `escalatedAt` handoff. No new predicate family, lifespan task, setting, or inbox kind; this is a
  liveness-contract fix inside `evaluate_escalation_findings`, covered by the existing HFX2-L5
  liveness simulations.
- 2026-07-08T02:55+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issues #12/#4): route gains `retire_policy.py` (server-side retire authority policy),
  `retire.py` (shared retire mechanics), `turn_state.py` (marker-based live turn-state classifier),
  and `seat_events.py` (observer event emitters); `app.py` gains `POST /api/terminal/{session}/retire`
  and `POST /api/terminal/{session}/rename`; `terminal_catalog.py` gains retirement provenance +
  `spawned_label` + `turn_state`/`turn_state_changed_at` columns and their copiers/write-points;
  `terminal_liveness.py` folds turn-state classification into the existing alive-probe sweep (no new
  hot loop) and gains an `on_turn_state_change` callback; `terminal_paste.py` gains the public
  `capture_pane` wrapper reused by the classifier. Covered by `test_seat_lifecycle.py` (45 tests / 5
  subtests). R2 fix round (F1, `controllers/worktree_tools.py`) widened the auto-retire completion-edge
  guard to the whole retire body so a catalog I/O fault can never fail an already-succeeded
  integrate/finalize — see that file's own sidecar for detail (out of this route's file list).
  Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact (small): `app.py`'s metrics sampling loop
  now also calls `await asyncio.to_thread(evaluate_provider_degradation, config)` right after
  recording the metrics snapshot, sharing the loop's existing exception-tolerant handling and 30s
  cadence — no new task, no new endpoint. The detector's own behavior (state machine, durable
  events, inbox alerts, critical failsafe) is owned by `providers/degradation.py` under the `mcp/`
  package overview, not this route. Verification metadata pinned until closeout stamps the
  HFX-L7 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L5 route impact (catalog liveness hysteresis): the route
  gains `terminal_liveness.py` — `TerminalCatalogLivenessSweeper` (rate-limited 10s, non-overlapping;
  rate-limited/concurrent callers get the persisted catalog without probing) +
  `observe_terminal_liveness`, the shared observation path behind `GET /api/terminal/sessions`,
  WebSocket attach, and `/paste` (all on the app's ONE injected clock). `terminal.py`'s probe is now
  evidence-bearing and stderr-aware (`TmuxProbeResult`; only explicit missing-session stderr ⇒
  definitive `pane-gone`, everything else ⇒ transient `tmux-command-failed`), and
  `terminal_catalog.py` persists the hysteresis state (`livenessFailures`/timestamps/evidence +
  `exitEvidence`) with `record_liveness_probe` + the success/failure transition copiers — a tmux
  command-failure storm can no longer mass-exit the fleet, false exits self-heal within one sweep,
  and `app.py`'s `_refresh_catalog_entries` is deleted. Covered by `test_terminal_liveness.py`.
  Verification metadata pinned until closeout stamps the HFX-L5 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4 route impact: terminal opener and attach-leaf routes now
  normalize accepted leaf refs to canonical qualified task-doc ids before catalog mutation and return
  `400 leaf-ref-not-found` / `400 leaf-ref-ambiguous` before any mutation on invalid refs; added
  `leaf_ref_validation.py` as the serving adapter. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 route impact (capture-verified delivery):
  `terminal_paste.py` reports delivery only after pane capture-verification against ONE
  pre-delivery origin baseline (both harness chip vocabularies; re-capture before any re-paste, so
  duplicate stacking is impossible; payload via stdin `load-buffer`; Escape refused, only Enter);
  failures are loud — `PasteResult.capture` rides the spawn tool's `deliveryCapture`, the `/paste`
  endpoint's unconfirmed `capture`, and the inbox push's bounded capture-tail `deliveryDetail`
  (`inbox_delivery.py`); `app.py`'s paste route is the same paster mechanic, no separate path.
  Verification metadata pinned until closeout stamps the HFX-L3 commit.
- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 finding 5 adds the shared
  `scope.decode_capped` codepoint-boundary read cap and wires it through `notes.read_note` /
  `files.read_file` + `_onboarding_doc_body` — an oversize file whose multi-byte char straddles the
  2-MiB cap now returns its first ~2 MiB with `truncated:true` instead of empty `binary`; the serving
  route model this overview describes is unchanged (detail in the file sidecars).
  (Stamp is part of the known pre-L2 timestamp-rot corpus condition — the entry predates the
  16:50 one below despite its stamp; MHR-L2 owns the forensic restamp.)
- 2026-07-07T16:50+02:00 — 260707-HFX-L1 route impact (containment R4): `app.py`'s lifespan now
  runs the provider metrics sampling task beside the projector — `sample_provider_containers` →
  `ProviderMetricsStore.record` every 30s (decoupled from the projection tick),
  exception-tolerant, cancelled at shutdown — making the serving daemon the central containment
  sampler feeding `provider_status`, the statistics board, and the HFX-L7 degradation protocol.
  Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `harnesses.py` grew the per-harness
  knob→flag mapping (two-vehicle claude effort vocabulary incl. session-level `ultracode`),
  effective-registry lookups, and the dispatch refusal helpers; `terminal_opener.py` applies the
  env-riding knobs onto the harness argv at launch resolution (validating effort/model, appending
  verbatim `launch_args`) and records the free-form + level spawn provenance on the catalog row;
  `terminal_catalog.py` carries the five new optional provenance columns; `app.py`'s
  `GET /api/harnesses` + open route resolve against the effective GLOBAL registry. Route relations
  unchanged (one opener, no parallel spawn path). Verification metadata pinned until closeout
  stamps the L16 commit.
- 2026-07-07T05:36+02:00 — 260703-L15 route impact (the change gate + the build stamp): `delta.py`
  compares stable forms (`VOLATILE_AGE_FIELDS` stripped; volatile-only ticks emit nothing —
  measured ~780 KB/tick → 0), `projector.py` caches the stable form per tick, publishes
  `(seq, projection)` atomically and exposes `revision(seq)` (boot nonce + content seq),
  `app.py`'s `/api/state` honors `If-None-Match` → 304 under a weak ETag and carries
  `servingBuild`, and NEW `build_info.py` resolves the boot-time serving stamp (version +
  best-effort short-hash + boot time) the SSE snapshot also carries. Updated the
  `app.py`/`projector.py`/`delta.py` Route Model bullets and added the `build_info.py` bullet.
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:59:54+02:00 — L14 review follow-up (L14R-3): the catalog column census now names `spawn_role`/`spawnRole` in both places (columns sentence + sessions-wire sentence) — a body edit, superseding the attestation-only entry. Verification metadata pinned until closeout stamps the L14 commit.

- 2026-07-06T23:59:24+02:00 — 260703-L14 (visual hierarchy + chat grouping) route impact: `terminal_catalog.py` gained the migration-safe `spawn_role` column (JSON `spawnRole`) and `terminal_opener.py` records `env["AR_SPAWN_ROLE"]` onto the row at first spawn (write-once, preserved across a role-less re-open) — the Chats command-tree grouping key; the sessions listing exposes it automatically via `entry.to_json()`. Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T09:30+02:00 — L9 adversarial-review follow-up (L9R-1): both the notes and files status mappers now map ValueError (null-byte paths) to 400 bad-path; regression tests in both suites. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-06T03:30+02:00 — No route impact: 260703-L11's additive `EnclosureNode.codeWorktreeExists`/`memoryWorktreeExists` flags pass through the serving layer unchanged (booleans are never `exclude_none`-dropped); `test_serving.py` re-run green with no serving-code change.
- 2026-07-06T01:40+02:00 — agent-orchestration L9 route impact: the route gains `notes.py`, the
  read-only coordination-notes API (`GET /api/notes/{list,read}` confined to
  `tasks/<repo>/<master>/notes/` via allow-list + single-segment master + `confine_rel`; missing
  folder → empty list; depth-capped honest listing; binary-tolerant size-capped reads), registered
  in `app.py` between the change-set routes and the static mount. Closes friction F-M (the notes
  tree had no dashboard surface). Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T23:43+02:00 — L8 route impact: `changeset.py`'s master net routes now resolve the series tip as the contract work branch while it exists, falling back to the source branch after landing/deletion; `/api/changeset/master` counters and `/api/changeset/file-diff?master=...` content share that resolver for code and memory. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: `/api/operator-inbox` now accepts
  agent-role/message/artifact metadata, attempts hosted push through
  `inbox_delivery.py`, and `terminal_paste.py` confirms delivery only on a real
  pasted draft/chip echo across the boot window. Verification metadata pinned
  until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — agent-orchestration L2 route impact: the route gains `terminal_opener.py`
  (the shared hosted-session opener extracted from `app.py`'s inline opener handler — leaf claim +
  env-seeded tmux ensure + catalog upsert; `resolve_terminal_launch`/`_terminal_label`/the role-scoped
  conflict check moved here) and `terminal_paste.py` (the server-side echo-confirmed stdin paste mirror
  of the frontend). `app.py`'s `POST /api/terminal/{session}` opener now delegates to the shared opener
  (so it and the `spawn_agent_session` MCP tool share ONE spawn path) and gains `POST
  /api/terminal/{session}/paste` + a `terminal_paster` `create_app` param; `terminal.py` gains the `env`
  knob-injection seam (`tmux new-session -e`); `terminal_catalog.py` gains spawned-by provenance columns
  (via `dataclasses.replace` copiers). Covered by `test_terminal_opener.py`, `test_terminal_paste.py`,
  `test_spawn_agent_session.py`. Verification metadata pinned until closeout stamps the L2 commit.
  (Distinct from the 260703-L2 daemon-supervision entry below.)
- 2026-07-03T12:57+02:00 — 260703 L2 route impact: the route gains `daemon.py` — the dashboard
  daemon supervisor (flock-guarded ensure: adopt/spawn/restart-on-mismatch; atomic `daemon.json`;
  identity-checked liveness; TERM→KILL stop; the threaded `maybe_autostart_dashboard` MCP boot
  hook). Covered by `mcp/tests/test_dashboard_daemon.py`. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-07-03T12:50+02:00 — No route impact: L15 changed only pyright-visible narrowing inside changeset.py; the serving surface and behavior are unchanged.
- 2026-07-02T17:25+02:00 — Reopened L6 copy-mode escape route impact: `terminal.py`'s `write_session`
  now cancels tmux copy-mode (new injectable `TmuxModeCanceller`, `tmux send-keys -X cancel` default)
  on the first typed input after mouse-report traffic, because copy-mode captures the keyboard and
  scrolled-up non-mouse panes swallowed typing until scrolled back to the bottom. At most one cancel
  per scroll-then-type cycle; mouse-aware panes never trigger it. Verification metadata pinned until
  closeout stamps the follow-up commit.
- 2026-07-02T17:04+02:00 — L9 route impact: added `terminal_leaf_assignment.py` and made
  `app.py`'s existing `attach-leaf` route a move/reassign route over the shared helper. The route now
  shares server-authoritative catalog conflict handling with the agent-facing MCP tool and preserves
  `leaf-taken` no-mutation semantics. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — Reopened L6 wheel fix route impact: `terminal.py` gained the injectable
  `TmuxConfigurer` seam (default `_tmux_enable_mouse`: per-session `tmux set-option mouse on`, failures
  suppressed, DEVNULL hygiene), asserted by `ensure` after create/probe and by every `attach`. Browser
  wheel input now reaches tmux as mouse reports, scrolling pane history for normal-buffer TUIs and
  passing through to mouse-aware TUIs; pane text selection becomes Shift+drag. Verification metadata
  pinned until closeout stamps the follow-up commit.
- 2026-06-30T00:00:00+02:00 — L5 follow-up route impact: leaf uniqueness is now per **(leaf, role)**. `terminal_catalog.py`
  gained `TerminalSessionRole` / `role_for_kind` / `entry.role` and a role kwarg on `active_for_leaf`; in
  `app.py` `_claim_leaf_or_409` is role-aware — the opener passes `role_for_kind(kind)` and `attach-leaf`
  passes `entry.role`, so a terminal can sit beside the leaf's agent chat (no 409) while a second chat or
  terminal still 409s. Updated the `app.py` opener/attach-leaf + `terminal_catalog.py` Route Model bullets.
  Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-30T00:00:00+02:00 — L5 (Sidebar chat) route impact: `app.py` gained the leaf→chat registry routes — the
  opener now takes a `leafKey`, claims the leaf via `_claim_leaf_or_409` (`409 leaf-taken`, running-only),
  persists + echoes it, and a new `POST /api/terminal/{session}/attach-leaf` claims a leaf for an existing
  session (`404` unknown/terminated). `terminal_catalog.py` gained `TerminalCatalogEntry.leaf_key`
  (migration-safe `to_json`), `with_leaf_key`, and `active_for_leaf` (running-only single-owner lookup).
  Updated the `app.py` + `terminal_catalog.py` Route Model bullets. Verification metadata pinned until
  closeout stamps the L5 commit.
- 2026-06-29T23:00+02:00 — operations-integration L4a route impact: `changeset.py`'s `task` + `file-diff`
  routes gained a `leaf` + `mode` selector (precedence `leaf > master > scope`) for the doc-reader leaf
  views — `committed` (`base → code_commit`) / `working` (`HEAD → worktree`), resolved by leaf-id off the
  persisted enclosure contract (works with no live worktree), with selector validation (400/404). Updated
  the `changeset.py` Route Model bullet. Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T17:00+02:00 — operations-integration L4 follow-up route impact: `changeset.py`'s `master`
  endpoint is now the **NET** series diff (`git diff <master-base> <series-tip>` for code + memory, per-file
  inspectable) rather than the sum-of-leaves, and `/api/changeset/file-diff` gained an optional `master`
  param (the series net file-diff). Updated the `changeset.py` Route Model bullet. Verification metadata
  pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T15:30+02:00 — operations-integration L3 route impact: added `scope.py` (the shared browse-scope layer extracted from `files.py` — `FileScope`/`resolve_scope`/`run_scoped`/`language_for`/active-enclosure enumeration) and `changeset.py` (the read-only `GET /api/changeset/{task,file-diff,master}` change-set API: per-task `base → current` code+memory counts + status + `hasSidecar`, BEFORE/AFTER file content for the L4 MergeView, and master accumulation) to the Route Model, both registered before the static mount; `files.py` now shares `scope.py`. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-28T22:41+02:00 — operations-integration L1 route impact: added `files.py` (the read-only `GET /api/files/{repos,list,read,onboarding}` files API) to the Route Model — the first serving module to bridge to the kernel `CoordinationContext`, registered before the static mount. Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the raw `/api/events` channel (`events.py`) now does
  **one** retained-backlog scan per connect, streams that bounded backlog in **chunks** instead of
  materializing the whole history, **filters `lifecycle.heartbeat`** out of the river, and prunes expired
  logs on a slow cadence. Updated the `events.py` Route Model bullet, the Hot Path Summary, and the
  two-resume-models invariant. Verification metadata pinned until closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: `delta.py` now emits an `activeWorktreeGroups` whole-value
  delta (wrapped `{"activeWorktreeGroups": [...]}`) when the set changes. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: raw `/api/events` now emits a one-shot `ready`
  event after retained backlog replay, and `/api/actions/dismiss` accepts targetless actionable-drift
  acknowledgements while keeping provider/gate dismissals scoped. Verification metadata pinned until
  closeout stamps the task-29 code commit.
- 2026-06-28T06:08+02:00 — Task 29 route impact: the raw `GET /api/events` channel now applies
  lifecycle-aware backend retention on fresh connections through `observer.event_retention`.
  Terminal lifecycle logs are pruned after the grace window, workspace/lifecycle-less rows are
  age-bounded, active lifecycle histories remain uncapped, and valid `Last-Event-ID` cursors retain
  exact byte-offset resume. Verification metadata pinned until closeout stamps the task-29 code
  commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: live `create_app` installs a `ProviderStateRefresher`
  into `Projector` so each projection tick can refresh provider current-state before diffing and serving
  the snapshot; sim mode disables that refresher and continues to replay fixture provider state. Detail
  lives in the `app.py`, `projector.py`, and serving-test sidecars. Verification metadata pinned until
  closeout stamps the task-31 code commit.
- 2026-06-27T18:43+02:00 — No route impact: terminal.py added stdin=subprocess.DEVNULL on its 3 tmux subprocess.run sites (#49 stdio-pipe guard) — behavior-preserving hygiene; no change to serving architecture or surfaces.
- 2026-06-27T02:28+02:00 — Task 22 follow-up: the terminal opener now uses
  `TerminalHost.ensure` to create a detached tmux session instead of opening and closing a starter PTY
  client. This fixes new chats immediately becoming `exited` while preserving per-tab attach.
- 2026-06-27T01:25+02:00 — Task 22 follow-up: terminal WebSockets now attach independent
  `TerminalHost.attach` clients to the same durable tmux session, and the opener detaches its starter
  client after catalog persistence. This fixes multi-tab sharing without competing reads on one PTY fd.
- 2026-06-27T00:45+02:00 — Task 22 follow-up: WebSocket disconnect now detaches the local PTY client
  without ending the durable tmux/catalog row, fixing blank terminal rehydrate after browser refresh.
- 2026-06-27T00:25+02:00 — Task 22 follow-up: terminal catalog termination is now sticky against later
  WebSocket/PTY exit bookkeeping, so the `End` button cannot leave a row visible after refresh.
- 2026-06-26T23:05+02:00 — Task 22: added `terminal_catalog.py` and documented the durable terminal
  session flow across serving: opener persistence, `/api/terminal/sessions`, WebSocket rehydrate with
  tmux probe, explicit terminate, and catalog-backed image upload after restart. Verification metadata
  pinned until closeout stamps the task-22 code commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: serving actions now support gate-id-only cancel for stale workspace gates while keeping approve/reject/revision lifecycle-targeted.
- 2026-06-25T13:20+02:00 — Task 23/24: serving route now includes the operator-inbox dismiss endpoint used to delete stale pickup warnings.
- 2026-06-25T07:26+02:00 — Task 19: `/api/actions/{approve,reject}` now accepts targeted `gateId` and
  optional `note`, rejects blank No/reject reasons, maps stale targeted gate ids to `409 stale-gate`,
  and leaves `/api/operator-inbox` as the message-only Chat path. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: documented `POST /api/operator-inbox` as the serving-layer write side for external-chat responses, routing to `operator_inbox_post_payload` with developer/dashboard attribution when the frontend has no hosted session to inject into. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-19T20:30 — Task 6 slice 6f: `app.py` gained `POST /api/terminal/{session}/image` (save a validated screenshot under `<cwd>/.dashboard-pastes/` for path-injection) and now opens harnesses `suspend_unsafe`; `terminal.py`'s `write` strips Ctrl-Z (`0x1a`) for suspend-unsafe (bare-pane harness) sessions only — a shell keeps job control. Updated the `app.py`/`terminal.py` Route Model bullets. Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T14:05+02:00 — Task 6 slice 6e-4: `terminal.py`'s `_spawn_pty` now gives the child a controlling terminal via `os.login_tty` (`preexec_fn`, setsid + `TIOCSCTTY`) + a seeded default winsize, so tmux honors browser resizes instead of staying at 80×24; the explicit `stdin/stdout/stderr=slave` keeps the child off the MCP stdio pipe (GitHub #49). Updated the `terminal.py` Route Model bullet. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: added `harnesses.py` (the curated harness launch registry — Claude Code/Codex/Pi.dev + `shutil.which` detection) to the Route Model; `app.py` gained `GET /api/harnesses` (`detect_harnesses()`) and a `kind="harness"` opener branch (`resolve_terminal_launch` resolves the registry argv; absent/unknown/not-installed ⇒ 400). Updated Purpose + the `app.py` Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: `app.py` gained the `POST /api/terminal/{session}` **opener** — the dashboard spawns + owns a session (`TerminalOpenRequest` `kind` → the pure `resolve_terminal_launch` → `host.open(cwd=config.workspace_root, command=[$SHELL])`; server-resolved command, unknown kind ⇒ 400), so the WebSocket has a real session to attach to. Updated the `app.py` Route Model bullet. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: `app.py` gained the `@app.websocket("/api/terminal/{session}")` Mode B2 bridge (attach to the `TerminalHost` or `close(4404)`; PTY output via `loop.add_reader` → binary frames; JSON `stdin`/`resize` in via the pure `_apply_terminal_input`; `{type:exit}` on child exit; tmux-persistent on disconnect) + the module-level bridge helpers + the `terminal_host` `create_app` param; `pyproject.toml` added the `websockets` core dep. Updated the `app.py`/`terminal.py` Route Model bullets + Hot Path + Purpose. Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-18T15:40+02:00 — Task 6 slice 6d-1: added `terminal.py` (the Mode B2 terminal host — `TerminalHost` over tmux-wrapped stdlib-`pty` sessions, injectable spawn, fixed-argv/localhost posture) to the Route Model + Invariants; the WebSocket bridge + `websockets` dep are 6d-2, the xterm.js viewport 6e. Also corrected the stale "(inert) POST action return-channel" wording in Purpose (6b made gate decisions binding). Verification metadata pinned until closeout stamps the 6d-1 code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the POST action plane became enforcing-adjacent — `actions.py`'s `evaluate_action` emits a `GateDecisionIntent` for gate-decision verbs and `app.py` records it as a developer/dashboard-attributed decision (`gate_decide_for_lifecycle`); lifecycle transitions stay the 4b no-mutation skeleton. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): `sim.py`'s `build_sim` materializes the fixture's structural surfaces into the sim root (`_materialize_surfaces`); `events.py` single-encodes the raw channel (`stream_raw_events` emits `json.loads(line)`, matching `/api/stream`; was double-encoded). Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T11:30+02:00 — Updated for slice 04 commit 4b: added `events.py` (raw `event`
  channel + byte-offset resume), `sim.py` (replay clock + feeder over the projector seams), and
  `actions.py` (the POST action skeleton) to the Route Model; `app.py` now carries
  `GET /api/events` + `POST /api/actions/{action}` and `projector.py` the `now`/`before_tick`
  seams. Verification metadata pinned until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the dashboard serving spine
  (`app.py`, `projector.py`, `delta.py`, `static.py`) over the observer read side — one
  shared projector, snapshot + per-entity SSE deltas, the static mount, localhost posture.
  The raw `event` channel, sim mode, and the POST action skeleton land in 4b. Verification
  metadata pinned until closeout stamps the 4a code commit.
### 260713-PHA-L6 Reload Boundary

The serving cutover is shared by the dashboard daemon, MCP-owning clients, bridge-backed session
runners/adapters, and browser tabs; reloading only the dashboard can leave in-memory inbox/catalog
schemas incompatible with durable rows. This is an operational contract, not a resource-polling
change.
