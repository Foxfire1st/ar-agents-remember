# mcp/ — MCP Package Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/`                                     |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-07-30T12:51+02:00 |
| lastVerifiedCommitHash | `3a8ff703d796dc585b86a458daaf9eb2af6b2b31` |
| lastVerifiedCommitDate | 2026-07-30T13:59:13+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## Purpose

260718-CHATS-L1 implements the active conversation serving the structured Chats architecture
assigned to the active child. Under `serving/conversation/active/`, the two authorized
production routes (native-hydrated page plus resumable SSE events) project the exact running
Codex/Claude/Pi conversations behind the L0 composition — HMAC-signed purpose-branded cursors
re-bound per wire, epoch verified against the live authority per request, a bounded
reconstructable-projector LRU per app — while `serving/conversation/projectors/` holds the pure
per-harness frame grammars (codex thread items/notifications, claude stream-json plus the exact
submission echo, pi durable entries/live tool upserts) with stable native identity and
unknown-vendor preservation. Hydration re-pages native authority only (never the flattened
transcript deque); the idempotent store unions tool-call blocks (review F1); established streams
fail as one typed gap + close (review F2/F3); the canonical `ConversationStatusService` is now
the single classification both Chats and orchestration consume
(`hosted_control_projection.snapshot_turn_state` delegates); capabilities stay fixture-gated
(claude `unverified` for a never-probed contract reason — since 260718-CHATS-L5F R4 THE CONTRACT
IS THE ONLY GATE and no version-string comparison demotes any capability, so the prior "installed
2.1.214 vs locked 2.1.211" version demotion is removed; codex historical tool loss visible). The
L0 composition, wire grammar, and library/control shells are untouched. The
`mcp/tests/` regression set gains four focused suites, and the foundation pin asserts the active
child's exact two routes.

260718-CHATS-L2 implements the dormant native conversation library inside the L9 contract roof.
Under `serving/conversation/library/`, five authorized routes expose each normalized harness's
native catalog/history (Codex direct app-server; Claude/Pi through the repository-locked Node
helpers gained operation entries `claude.ts`/`pi.ts` plus protocol serve/probe/sign/page
primitives) and open a selected native identity as a new idempotently tracked AR session only
after exact catalog proof. Live production-path gates decide capability honesty per
installed-executable fingerprint; a per-app HMAC-signed cursor/key authority binds scope,
purpose, and content-derived catalog generations; the bounded open ledger keys one stable
requestId/fingerprint, and record-spawned failures retire honestly while absorbed foreign
sessions are never disturbed. The L0 composition and wire grammar are untouched. The
`mcp/tests/` regression set gains six focused suites plus the opt-in
installed-runtime gates, and the foundation pin asserts the library child's exact five routes.

260718-CHATS-L0E lands the additive, read-only native evidence and resume substrate inside the
existing hosted harness-control family. Per-harness mappers stop dropping native frames by placing
full payloads under one reserved `arEvidence` event key; the control bridge diverts them at its
single consumption point into a bounded per-session evidence deque and publishes redacted events,
so every existing snapshot/catalog/SSE projection stays byte-identical. Three additive
epoch-scoped IPC reads — deque-domain evidence pages, native-domain history pages with typed
identity and opaque continuation (codex `thread/read`, pi `get_entries`; claude honestly
fail-closed), and the all-sources submission-provenance batch — cross only the user-private
control socket under the unchanged v1 protocol, with strictly validated client reads across two
disjoint coordinate domains. A codex-only `resume_thread_id` launch channel rides the opener →
runner payload → factory path into the sole `CodexAppServerSettings` site, refusing non-codex or
malformed values before any spawn. The substrate enables no feature; it is the closed baseline
later conversation leaves consume without editing shared harness-control seams.

260718-CHATS-L2E lands the additive native control-plane substrate inside the same hosted
harness-control family. A native interrupt write dispatches bridge-side through a structural
`InterruptCapableAdapter` sub-protocol — epoch-guarded and bridge-stamped, codex exact-active-turn
`turn/interrupt`, pi expected-operation-guarded RPC `abort`, replay-once per pair, claude
fail-closed typed, settlement untouched on the landed completion path. A paged never-bodies
operation-timeline enumeration reads the authority's retained ledger (all prompt sources plus
set-model/set-effort identity) under a count cap and the shared 48 KiB-class budget with
latestSequence/eviction-floor/truncated/epoch on every page, delegated authority → queue →
bridge → IPC → validated client. An asset channel rides submit as digest-verified references only
— resolve-and-verify confinement under the endpoint's own assets root, admission plus
construction-time sha256 verification, codex `localImage` and pi base64 native forms, unsupported
receipts on non-capable adapters — and the withdrawal-recovery payload crosses the exact
pre-tombstone body once inside the already `cockpit_only` response. Two additive IPC actions keep
`ar-harness-control/v1` (now 20 actions) with every pre-existing action, DTO, consumer, deque,
and snapshot reduction byte-preserved; redacted `control-plane/*` fixture rows record the
installed-runtime proof without enabling anything. The `mcp/tests/` regression set gains the
contract suite plus the opt-in installed-runtime capture.

260718-CHATS-L3 implements the authoritative control child over that L2E substrate, filling the
last behavior-empty conversation router. Under `serving/conversation/control/`, seventeen registered
routes deliver exact-turn interrupt (idempotent request/status/reconcile with acknowledgement never
equal to settlement), the complete source-aware never-bodies operation queue with cockpit-only
withdrawal and a bounded authorization-bound 900 s recovery lease, typed attachment stage/rebind/
submit through the L2E asset channel into a confined 0700/0600 spool, read-only effective policy
with no mutation surface, and evidence-bound telemetry (codex cumulative token usage). Opaque
control references are HMAC-signed, purpose-branded, and re-bound per wire; the per-app service holds
bounded per-(session, epoch) ledgers with per-session serialization above the L2E replay cache; the
pi settlement reads the L3E-preserved evidence terminal identity. The `mcp/tests/` regression set
gains four focused service/route suites, a shared control topology, and an opt-in installed-runtime
proof; the slice is governed by `conversation/control/overview.md`.

260715-FEUI-L9 adds two deliberately bounded package routes. Under `serving/conversation/`, strict
wire models, exactly two read ports, and three behavior-empty child routers establish the stable
protocol-neutral contract roof for active transcript, conversation library, and future control
behavior. Under `native_helpers/conversation_library/`, a locked private Node helper normalizes
repository-resolved harness observations into redacted evidence; it is not a second server, store,
or capability authority. The existing harness-control application factory registers the new root
once. L9 does not yet claim a native-history projector, control implementation, or Chats renderer.

260718-CHATS-L0 repairs the production composition boundary under that contract roof. The same
single harness-control registration now constructs and installs one immutable app-scoped
`ConversationRuntime` — workspace/coordination scope, terminal catalog/host, effective harness
registry, liveness clock/config, and capability evidence — plus a server-resolved local-operator
authorization resolver on the app exactly once, with `create_app` passing `coordination_root` for
the scope. Child leaves consume the runtime only through two narrow request dependencies
(`get_conversation_runtime`, `resolve_conversation_authorization`) and never edit the shared
registration again; the local-operator ruling is loopback-only with no browser principal/tenant
channel. The shared error family gains `ConversationCompositionError` for missing, duplicate,
foreign, or missing-member composition failures. The route remains behavior-free: no projector,
native-history service, control implementation, or renderer.

`mcp/` is the package-managed Agents Remember MCP server. It turns coordinator
startup and provider lifecycle behavior into typed, host-side operations backed
by importable Python services instead of model-edited coordinator scripts or
coordinator `system/settings.json`. The tool surface gained `task_reopen` (L11):
reopen a fully landed leaf task under its exact leaf id — a task-domain state reset
whose worktree recreation stays with `worktree_start`. The agent-orchestration L2
adds `spawn_agent_session` — the agent-facing **dispatch** tool that CREATES a
role-configured, leaf-attached, context-primed hosted session by composing the
existing serving primitives (the shared session opener + optional leaf attach with
server-arbitrated `leaf-taken` + a capture-VERIFIED context paste (260707-HFX-L3) with optional
submit), resolves model/effort/free-form spend controls from settings only, rejects caller spend
overrides before spawning, and records spawned-by provenance — so orchestrators spawn managers and
managers spawn workers without dashboard clicks. HFX-L6 splits the developer-facing architect from spawned backend
orchestrators and adds the curator role to the runtime skill/package mirrors, settings role vocabulary,
dashboard role projection, and manager/worker dispatch chain. The package-data runtime skill mirror now carries the L5
super-integration doctrine for orchestrated series: super branches from main,
masters branch from super, leaves branch from masters, C-11 carries every edge,
the orchestrator integrates completed masters from a super-sourced worktree, and
the final super-to-main PR is followed by main-memory carry-over and push. L6
sharpens the same runtime skill mirror's adversarial review procedures: managers
spawn master-exit reviewers, orchestrators spawn super-exit reviewers, verdicts
land in series `notes/reports/`, and the handover gate carries
`reviewer-verdict` evidence refs that L4 policy may require. Since L12 every managed
provider container carries an explicit compose memory cap (watchers 512m,
falkordb/ollama 2g, runner 1g, postgres 512m) with self-recycling OOM behavior.
260707-HFX-L1 adds the containment layer above those per-container caps: the
on-disk authority settings — never a running server's boot snapshot — are the
provider LAUNCH authority (launch-capable operations re-read them fail-closed;
stop/status/cleanup are never gated, so `providers: {}` on disk is a live
fleet-wide kill-switch), provider setup is serialized host-wide by a
HOST-scoped setup-lock flock in the system temp dir (one non-dry-run prepare
at a time bounds the aggregate container load — the 2026-07-07 OOM was
concurrent setups summing past the host; the lock lives outside every
coordination root because those trees are prunable/per-workspace), and the
serving daemon centrally samples labeled provider containers
into a metrics store that provider status attaches. 260707-HFX-L2 extends the
same posture to the INDEX lifecycle: a HEAD difference between a seed source
and a worktree checkout is a state to catch up from, not a teardown — small
diffs become index UPDATES via watcher-event catch-up (the seed clones the
near-perfect graph and fresh mtimes/touches drive the event-driven watchers
over exactly the delta), the implicit refresh-all fallback is off by default,
and from-zero rebuilds are explicit only (`cgc refresh` or the opt-in
fallback flag); index-lifecycle rows ride the same central metrics log.
260707-HFX-L7 builds the RESPONSE protocol on top of that same central metrics log: NEW
`providers/degradation.py` is a provider-only detector/state-machine
(healthy/degraded/critical, hysteresis-gated so alerts do not flap) that `serving/app.py`'s
sampling loop calls once per tick; on a state-change transition it writes a durable event/state
pair under `logs/observer/providers/degradation-*` (survives daemon restart), posts
role-addressed `degradation-alert` inbox rows to the orchestrator and every active manager
(instructing managers to stop starting providers with no kill authority, and the orchestrator to
dispatch the new `system-specialist` role before ordering a fix or stopping providers), and — at
`critical` with the failsafe armed — stops provider stacks through the always-legal teardown path,
capturing (never losing) a raising stopper's failure inside the durable event. NEW
`mcp/provider_degradation_settings.py` is the dedicated `providerDegradation` settings parser
(15-key fail-loud allowlist, conservative enabled/armed defaults) `mcp/config.py` wraps into
`ConfigError`. This iteration is providers-only by developer ruling; Sentry
(260703_spotlight-dev-observability) is the designated future detection source that can
replace/feed the same response protocol without redoing it.
260707-HFX-L8 adds seat lifecycle management to the terminal catalog tool surface: NEW
`session_retire` (+ `POST /api/terminal/{session}/retire`) terminates a tracked chat session and
marks the catalog row retired with provenance, authority-checked server-side (owner-never-self-
retires; a manager may retire only its own master's worker/reviewer seats; the orchestrator may
retire any seat) via NEW `serving/retire_policy.py` + `serving/retire.py`. **Superseded by
260707-HFX2-L11**: the `worktree_integrate`/`lifecycle_finalize_task` completion edges no longer
call `retire`/terminate a successful seat automatically; they call NEW `serving/landing.py::
land_seats_for_leaf` instead, which marks the row `status:"landed"` (kept alive, non-terminated,
fully inspectable) — successful completion is not chat cleanup (ruled design constraint 10);
explicit `session_retire` or the dashboard's landed-archive group-cleanup control are what actually
reclaim chat volume. Settings are `autoLandOn{Integration,Finalize}` (still config-gated, both
default ON, still best-effort so a catalog fault can never fail the edge it rides; legacy
`autoRetireOn*` keys are honored as aliases). `serving/retire.py`'s manual/authority-checked retire
behavior described above is otherwise unchanged. NEW `session_rename` (+
`POST /api/terminal/{session}/rename`) updates a chat's display label post-spawn without touching
its role. NEW `serving/turn_state.py` classifies live seat turn-state (working/turn-ended/
awaiting-input/stale) from pane text on the existing L5 liveness-sweep cadence; NEW
`serving/seat_events.py` emits observer events on retire/rename/turn-state transitions.
260707-HFX-L12 closes a master-exit-review-caught gap: `controlplane/operator_inbox_records.py`'s
`AgentRole` gains `"architect"` and `"curator"`; `InboxMessageKind` gains `"decision-item"` and
`"decision-ruling"`. The HFX-L6-ratified minimal decision-item relay (orchestrator posts a
decision-item to the architect; architect posts a decision-ruling back) was landed as doctrine but
the schema previously rejected both calls with `ValidationError` — the architect seat could not
receive any typed inbox row. No other consumer of these Literals enumerates them exhaustively, so
this is a pure schema extension with no downstream edits; a new round-trip test in
`mcp/tests/test_operator_inbox.py` pins the fix through the real tool-payload seam.
260707-HFX2-L1 adds a durable what-must-happen-by-when layer that spans three tool families at
once, not just one route: NEW `controlplane/expectation_rows.py` is the `ExpectationRowStore`
primitive (`briefed-by`/`turn-report-by`/`verdict-by`/`ack-by` rows, `pending`/`overdue`/
`find_by_source` queries, idempotent `mark_met`/`mark_missed`); `mcp/tools/terminal.py`'s
`spawn_agent_session_payload`, `mcp/tools/gates.py`'s `gate_create_payload`/`gate_decide_payload`,
and `mcp/tools/operator_inbox.py`'s `operator_inbox_post_payload`/`operator_inbox_consume_payload`
each now write (or meet) their expectation row in the SAME call as the dispatch/decision/ack
itself (R2) — a deadline is a durable row an L2 sweep can scan, never an in-memory timer a
daemon/MCP restart would erase. R1 sharpens the operator-inbox ack contract to match: `consume` is
the ONLY terminal outcome on `OperatorInboxEntry` (new `attemptCount`/`lastAttemptAt`/
`nextAttemptAt`/`escalatedAt` fields) — a confirmed `delivered` paste still schedules a further
redelivery attempt, since pasted is not perceived. NEW `controlplane/inbox_backoff.py` (R3) is the
redelivery backoff-ladder math and per-target rate limiting a future sweep will drive; NEW
`controlplane/signal_routing.py` (R4) derives a one-hop routed owner (worker→its manager,
manager→its orchestrator, `decision-item`→architect) from `serving/terminal_catalog.py` spawn
provenance, and `OperatorInboxEntry` gains `ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields
stamped once at post time from that derivation. `kernel/agentic_settings.py` gains the
`orchestration.expectations` settings family (`ExpectationSettings`,
`DEFAULT_EXPECTATION_SLA_SECONDS`) — an SLA-per-kind duplicated by hand against
`ExpectationKind` to avoid a kernel↔controlplane import cycle. The redelivery sweep, escalation
ladder, and dashboard consumption of `escalatedAt` are explicitly OUT of scope for this leaf (a
sibling leaf's job); this leaf only lands the durable rows, the backoff math, and the routing
derivation the sweep will consume.
260707-HFX2-L2 adds the `orchestration.supervisor` settings family to the same package-level
loader — `SupervisorSettings` (enabled/interval/staleness-cutoff/redeliver-rate-limit) parsed by
`kernel/agentic_settings.py` — consumed across TWO other package routes: `serving/app.py`'s new
supervisor-sweep lifespan task (the sweep subsystem itself — the predicate library, action
dispatcher, and self-liveness heartbeat — is documented in full in `serving/overview.md`, which
this file governs) and `mcp/tools/base.py`'s per-tool-call staleness banner attachment
(`supervisorBanner`, exception-contained at the call site). Same cross-route-consumption shape as
the 260707-HFX2-L1 expectation-row family documented above.
260707-HFX2-L4 adds the `orchestration.escalation` family to the same loader (`EscalationSettings`
— per-`message_kind` ack SLA, per-rung dwell timings, the renudge rate limit, the
respawn-after-rung threshold), consumed by the SAME `serving/app.py::_supervisor_context()` call
site the supervisor family already wires through — no new lifespan task, no new settings-read
seam. The family backs the P-15 tier-3 escalation ladder (`controlplane/escalation_ladder.py`,
`controlplane/orphan_policy.py`, and a new two-hop `signal_routing.derive_skip_level_owner`/
`is_seat_dead` pair kept SEPARATE from the existing one-hop `derive_signal_owner`), fully documented
in the `controlplane/` and `serving/` route overviews this file governs.
260707-HFX2-L5 closes the loop on the same P-15 mandate from the doctrine side: the role files this
package data ships (`package_data/runtime/skills/l-01-agent-lifecycles/{SKILL.md, roles/manager.md,
roles/orchestrator.md, roles/worker.md, templates/turn-report.md}`) invert from active owner-side
vigilance ("Monitor the worker" / "monitor turn-report artifacts") to a passive process-and-ack
contract: the HFX2-L2 sweep + HFX2-L4 ladder do the watching, and a role's own duty is to be woken
with its pending signals, process and ack every one, then end its turn — silence is supervised, so
`lifecycle_turn_end_notification` is never a liveness gap. An explicit watcher ban (uniform-mechanism
ruling 2026-07-07) forbids any seat-local watcher/poll/monitor of any kind, one mechanism for
everyone. Doctrine-only change set, propagated by `scripts/sync-skills.py` to all 9 downstream
package copies plus the canonical `skills/` source — zero Python touched. The SAME leaf adds NEW
`mcp/tests/test_liveness_simulations.py` (11 tests, 8 named P-15 fixture-zoo incident classes),
driving `run_supervisor_sweep` across multiple simulated ticks per incident: 6/8 pass fully
end-to-end; 2/8 (chip-stacked delivery stall, and the pane-classified half of never-briefed) are
proven hybrid (predicate-unit classify + real downstream sweep response) because `evaluate_predicates`
hardcodes a real, non-injectable `tmux capture-pane` call — documented as a real product gap and the
natural next leaf (make the pane capturer injectable through `SupervisorContext`), not silently
worked around. Results are filed in `notes/reports/260707-HFX2-L5-liveness-report.md`.
260707-HFX2-L8 closes the two liveness gaps a live dead-seat-storm incident (2026-07-08) exposed in
the supervisor loop itself, spanning four package routes. `kernel/agentic_settings.py` gains one
`orchestration.supervisor` field — `redeliverBudget` (default 250, defaults-safe) — the per-sweep
redelivery floor so a large redeliverable set degrades gracefully instead of one sweep grinding the
whole backlog. `controlplane/operator_inbox_records.py` gains a durable `ladder-resolved` terminal
inbox state (distinct from ack): a pending row at the terminal escalation rung whose target seat is
provably dead (retired / no hosted session) terminates instead of redelivering forever — excluded
from `redeliverable()`/`is_due()` via a state-keyed predicate in `controlplane/inbox_backoff.py`
(mid-climb / live-seat rows untouched, L1-R1 preserved) and dropped by
`controlplane/interaction_retention.py` compaction. HFX3 supersedes the old immortal-pending
contract: pending rows expire after 48 hours, the folded inbox is capped at 500 current ids, and
durable truth lives in artifacts rather than notification rows.
`serving/supervisor.py` threads ONE in-sweep operator-inbox snapshot/index through every
finding/mutator (`record_delivery`, `mark_escalated`, `advance_rung`, `mark_ladder_resolved`,
respawn reads), killing the per-finding full-log re-fold (O(n^2)) so a sweep's cost is bounded by
finding count and the self-liveness heartbeat ticks unconditionally under backlog;
`serving/supervisor_heartbeat.py` surfaces `pendingInboxCount`/`redeliverableInboxCount`/
`lastSweepDurationSeconds` onto `/api/state` and the dashboard header as a forward backlog signal.
`worktrees/leaf_refs.py` gains a minimal boot-safety skip of non-task JSON siblings (schema-marked
malformed task docs still fail loud). The cross-route change is documented in the `controlplane/`,
`serving/`, and `dashboard/src/` overviews this file governs; a non-destructive recovery runbook
lands in `docs/design/observable-lifecycle.md` and the settings table in
`docs/reference/settings-json.md`. New scale regression: a 2000-row dead-seat-storm sim in
`mcp/tests/test_liveness_simulations.py`. Results filed in
`notes/reports/260707-HFX2-L8-worker-report.md` and `-reviewer-report.md`.
260707-HFX2-L7 is the hotfix release tail for `3.0.0rc4`: package/version strings move from rc3 to
rc4, the packaged lifecycle doctrine refines Developer Clarification Triage to read the active
queue before choosing note-only handling, and the serving supervisor defers generic unacked
escalation for hosted-delivery failures until the persistent redelivery threshold has exhausted.

The serving package also contains the protocol-neutral harness control seam: normalized state,
one-adapter hosted bridges, bounded ordered input, private exact-identity IPC, and a surface-owned
draft/transcript layer. L1 defines this contract and reports unsupported adapters explicitly; no
vendor driver is registered or production cutover is implied.
260713-PHA-L3 extends that seam with a stable-only Codex app-server adapter. The pinned 0.144.3
 JSON-RPC transport and session own initialize, model/effort discovery, and exact thread
 start/resume; the adapter/state pair own correlated turns, structured approvals and elicitation,
 explicit steer-or-queue busy behavior, bounded evidence, and reconnect reconciliation without
 blind resend. This is a leaf-local protocol path: production registration and cutover remain L5
 scope.

260715-FEUI-L5 is the current production authority over that historical seam. One
`HarnessSubmissionAuthority` per bridge generation orders prompt/model/effort work, linearizes
withdrawal against guarded native dispatch, completes only exact full operation refs, and exposes
bounded raw-free lifecycle status. `HarnessControlQueue` is a facade, not a second actor. The shared
typed error family now distinguishes certified pre-dispatch busy, immutable-id conflict, and epoch
mismatch so only the exact certificate is retry-safe.

The hosted harness-control and conversation layers are multiplexed for harness sub-agents. The
codex app-server connection auto-attaches every spawned sub-agent thread to the seat's connection,
and the adapter demultiplexes per thread: a bounded thread registry tracks per-thread turns,
operations, and pending interactions; collab items (`collabAgentToolCall`, `subAgentActivity`) bind
agent identity into a snapshot-carried registry; malformed non-parent traffic degrades to preserved
raw evidence while parent shape errors still fail loud; server→client requests (approvals) are
accepted from any thread and answered by JSON-RPC request id. The wire grammar gains an additive
agent dimension (`ConversationAgentRef` on items, `EvidenceFrame.thread_id`,
`AdapterSnapshot.pending_interactions`), the active projector serves one multiplexed projection per
seat (one page, one SSE, one cursor domain) with per-thread native/live dedupe, the library groups
sub-agent conversations under their parent on both harnesses (codex `subAgent` source kinds, claude
`subagents/*.jsonl` enumeration), and claude launches gate `--forward-subagent-text` on a
version-floor probe with fail-closed fallback.

The multiplexed surface is load-shedding and concurrency-safe under real vendor traffic.
Server→client requests pend per thread in bounded maps keyed by rpc id (concurrent approvals
across any threads are normal traffic, answered by request id; the vendor's own clients track
them the same way); an unknown or experimental request method is answered with decline
semantics and preserved as degraded evidence on any thread, while a malformed shape on a known
stable method still fails loud on the parent only. Concurrent pendings — parent included — all
project into the interaction lane with singular-rotation settlement (the oldest holds the
singular slot; answering rotates the next in without falsely resolving it), and the authority's
parent guard is decided by the entry's own thread. The adapter's bounded event queue never
fails the bridge under a delta flood: the oldest high-volume delta events shed first with every
shed counted, and one load-shed notice crosses with the count when the consumer catches up
(including on consumer-side drain and before the close sentinel).

## Hot Path Summary

FEUI-MX-FIX-2 changes no MCP package source contract. Its `package_data/dashboard/` index,
fingerprint, and content-hashed assets are synchronized shipped output from the reviewed
`dashboard/src/` build. They are deliberately excluded from one-to-one onboarding: browser open
authority is documented under the dashboard source cards and overviews, while
`scripts/sync-dashboard.py --check` proves package parity. The generated rollover must land as one
complete add/delete set; it is not a second implementation route.

260715-FEUI-L9R crosses `mcp/` through the existing `agents_remember.serving` route and the shipped
dashboard boundary. Serving resolves the optional packaged dashboard fingerprint into
`build.dashboardBuild`, revalidates entry HTML while leaving content-hashed assets on ordinary
static caching, keeps pre-session `GET /api/harnesses` rows to `id`/`name`/`detected`, treats raw
event offsets as untrusted hints and emits only server-aligned top-level-object records parsed once,
and gives every dashboard-owned tmux client a clean tmux identity with `TERM=xterm-256color`.
Product mismatch/reattach behavior and request ownership remain governed by `dashboard/src/`; the
implementation contract lives in `mcp/src/agents_remember/serving/` and its regression boundary in
`mcp/tests/`. The synchronized `package_data/dashboard/` rollover is shipped output, not a second
source implementation.

260715-FEUI-L9 is a contract/foundation path, not yet a runtime projection path. Python consumers
validate normalized products and address separate active/library cursors through the new serving
route. The repository-only native helper and three installed-runtime fixtures supply redacted,
non-enabling evidence. Hostile contract tests and topology tests fail closed on provenance,
identity, generation, contradictory status/capability state, router drift, helper path drift, and
fixture promotion.

260715-FEUI-L5 routes exact-session submit/reconcile/status/withdraw through the daemon and private
IPC into one epoch-bound authority. Async adapter preflight precedes a lock-linearized final write
claim; Codex, Claude, and Pi dispatch now without native queues. Direct exact-ref completion reaches
authority before coalesced publication, early terminal truth can dominate unknown, and bounded
retention never evicts live/active/unknown work. Public responses remain cockpit-only/raw-free;
post-write loss remains ambiguous and reconciles under the same request id.

260714-ACPUI-L4 freezes the package's daemon-side own-adapter contract. A bounded
`HarnessCapabilityCatalog` discovers the installed/authenticated native catalog without a model
turn, fingerprints the executable/argv, single-flights by built-in harness, and quarantines the
observed entry after failed explicit auth refresh. FastAPI routes expose that normalized catalog,
an optional complete launch pair, exact-session advertise and honest setters, whole-message submit,
and same-id reconciliation. Live reopen returns retained process truth or conflicts without
rewriting it; request-byte ambiguity never triggers blind resend; duplicate ids converge on the
retained receipt; public responses strip adapter-private raw evidence; and liveness precedes
support classification. The route is server-only and preserves role spawn and the durable bus.

260714-ACPUI-L3 adds normalized same-session model/effort mutation to the native hosted-control
package. `HarnessControlBridge` sends both setters through the same bounded FIFO as prompts, and
the queue validates the exact five-value `SetResult` truth contract without inventing an effective
value. Claude uses structured stream-json commands plus exact replay/terminal evidence; Codex
binds each accepted prompt to its selection epoch and applies pending settings on a fresh
`turn/start` without reconnecting; Pi holds mutation, state readback, and refreshed catalog inside
one finite evidence transaction so model errors and thinking clamps stay distinct. Cancellation or
late vendor replies cannot poison the shared reader/queue, and no setter depends on composer,
tmux, session-command, or injector paths. Existing role/leaf spawn provenance and the durable
inter-agent inbox remain independent moats rather than alternate configuration transports.

260714-ACPUI-L2 connects the existing role-settings authority to the native hosted launch
boundary. A role-configured Claude, Codex, or Pi seat carries one complete typed
`ResolvedLaunch`; the hosted runner performs token-free per-install discovery, validates effort
under the selected model, refuses duplicate adapter-owned selectors before discovery, and applies
Claude flags, Codex `thread/start` configuration, or Pi's provider-qualified flags before the
configured vendor session starts. Missing selections refuse before tmux; later discovery/startup
failures remain queryable as exact failed/rejected control snapshots. Normalized model/effort is
never synthesized into a session command. Role/leaf provenance and the durable inter-agent inbox
continue through their existing catalog and control-plane paths.

The package-data lifecycle and install skills now teach the same dynamic/native contract. Their
canonical sources and harness mirrors are sync products outside this onboarding slice; the
eligible package-data copies remain the shipped runtime evidence documented here.

260713-PHA-L6 extends the package's protocol-backed serving contract with structured Claude,
Codex, and Pi capability negotiation and a strict two-field rolling inbox-reader compatibility
seam. The full cutover reload boundary includes the daemon, MCP-owning clients, per-session runners
and adapters, and browser tabs; R10 resource performance remains queued.

260713-PHA-L4 adds four unregistered serving modules for the pinned Pi 0.80.6 RPC boundary:
strict framing/schema parsing, owned subprocess transport, normalized event settlement, and the
L1-backed adapter with exact-session reconnect and post-cursor no-resend reconciliation. The
paired tests and isolated smoke live under `mcp/tests`; production registration remains L5 scope.

HFX2-L20 closes the live consume/redelivery resurrection race without changing a public payload:
consume remains an append-only terminal fact, and the shared current-state/retention fold refuses to
let a later stale pending delivery snapshot reverse it. Polling and supervisor redelivery therefore
stay terminal after acknowledgement; compaction remains the cleanup boundary.

HFX2-L17 splits immutable `spawnRole` provenance from current `seatRole` binding. The catalog
migrates legacy rows in place; spawn/attach liveness-check only the same `(leafKey, seatRole)`;
retire authority, expectations, inbox/supervisor findings, chain credit, landing, provider role
discovery, and dashboard rendering use the binding. The MCP/HTTP attach surfaces accept role and
return `role-required` for an untyped hand-opened harness, while role-suffixed leaf refs refuse with
canonical pair guidance. Tests cover the workaround museum and supervisor behavior at fleet sizes
3 and 30.

The regenerated dashboard assets are deliberately not onboarding subjects. Durable proof stays at
the dashboard source, `scripts/sync-dashboard.py` build/package parity check, and serving static
boundary. HFX2-L21 follows that existing boundary: its adjustable Chats sidebar is frontend-only,
while this route carries only the regenerated `package_data/dashboard/` bundle and fingerprint.

HFX2-L15 replaces screen-grammar dispatch credit with one repository-wide acceptance path:
`HarnessSessionLog` binds the unique id-bearing message in the spawn cwd, `injector.deliver`
applies calibrated Claude/Codex windows, and `TerminalPaster` permits one Enter re-press plus one
verified-absence clear/replace re-paste. Spawn, durable inbox, supervisor redelivery, and REST paste
all compose that path. Catalog provenance records resolved knobs, log binding, and an optional
`replacementForLeaf`; tests are pinned to this checkout so the full gate cannot import a sibling
editable install.

260707-HFX2-L13 closes the L12 package residuals and reconciles the reviewed HFX3 runtime seams that
round 2 actually changed. Observer storage now coalesces lifecycle heartbeats into bounded sidecars,
fully reclaims dormant unprotected lifecycle directories, and lock-guards live workspace compaction
with virtual cursor offsets. Projection/state broadcasts carry bounded body-free task/series summaries
with `bodyRevision`; the serving package exposes the path-confined on-demand task-body endpoint and
the dashboard fetches only the visible body. Control-plane/supervisor changes route leaf signals and
completion wake to the current manager, suppress stale predicates when the leaf chain progressed,
enforce a five-minute later-rung floor, and prevent duplicate same-sweep transitions. The CS-6 tests
pin two-size river/heartbeat/task-payload bounds plus the corrected lifecycle-log cache property.
Current code still excludes an unbound worker from active-phase chain credit; reviewer S1 remains the
accepted HFX2-L14 S7 follow-up, and this summary does not certify the separate post-integration HFX3
retro gate.

Start in `src/agents_remember/mcp/config.py` for trusted settings parsing,
`src/agents_remember/mcp/server.py` and the `mcp/tools/` package for exposed
MCP tools (`server.py` installs `mcp/compact_content.py` to minify tool-result
text; verbose tools additionally file bulk diagnostics under
`temp/tool-reports/` via `mcp/tool_reports.py` and return compact outcomes
with a `reportPath`), `models/tool_registry.py` for public response contracts,
`controllers/context_packet.py` for compact `ContextPacketV2` startup packets,
and `controllers/runtime_install.py` plus `install/runtime.py` for MCP-owned
runtime installation. Provider status is composed in `providers/status.py`; the serving/observer path can
refresh the persisted provider current-state snapshot before live dashboard projection so provider rows are
not limited to the last explicit diagnostics/status command.
`providers/metrics.py` (260707-HFX-L1, containment R4) is the central
containment metrics module: the serving daemon samples labeled provider
containers (label-discovered, read-only, dockerless-safe) into its store under
`logs/observer/providers/` (`metrics.jsonl` + replace-atomic
`metrics-current.json`), and `provider_status` attaches the current snapshot
even while providers are disabled so leftover stacks stay observable.
provider lifecycle settings are generated from MCP settings in
`providers/settings.py`. Provider lifecycle implementation is now split between
the `providers/lifecycle/` facade/shared helpers and provider-owned
`providers/cgc/lifecycle/` plus `providers/grepai/lifecycle/` packages; there
is no legacy `provider_lifecycle.py` facade. Memory-layer quality control lives under
`src/agents_remember/memory_quality/`: integrity checks include the onboarding
drift classifier/summary, and style checks currently include update-history
newest-first ordering. Shared onboarding-document parsing, route-overview discovery, and the
"meaningful body vs metadata/history" change classification live in
`kernel/onboarding_doc.py`; the closeout body gates in
`worktrees/modules/onboarding.py` consume them and accept explicit
`No content impact:` / `No route impact:` Update History markers as in-band
reviewed-no-impact attestations. Branch freshness (issue #54: is a local
branch current with its upstream, plus ahead/behind counts) lives in
`kernel/git_freshness.py` beside `kernel/git_facts.py`; the `context_packet`
controller surfaces it as the opt-in `include_freshness` packet section
together with a `ledgerMapsCodeHead` check, forming the lifecycle-start
staleness checkpoint. Route-index generation is split between
`kernel/route_index.py`, which renders route-local metadata, and
`kernel/route_index_census.py`, which validates the repository root and freezes
one exact Git/path-rule source snapshot for membership, coverage, and counts.
Tracked and untracked records are NUL-delimited, ignored/generated paths are
excluded by Git plus resolved storage rules, symlinks are classified without
following their targets, and ambient Git repository selectors are scrubbed by
`kernel/git_command.py`. Controllers and worktree closeout pass the resolved
repository identity and `StorageSettings` explicitly rather than rediscovering
authority inside the builder. Branch-memory carryover (`memory/carryover.py`)
plans route-overview candidates beside file sidecars (route-keyed, never
auto-carried when content differs), requires effective official-memory storage
authority through `memory/carryover_authority.py` before any write, regenerates
official-side route indexes after a carry from that same authority, guarded on
a clean official-ref checkout, and fast-forwards memory `main` to the official checkout tip
(`memory_main_advance`, issue #54) so non-main cycles no longer leave memory
main behind. Worktree lifecycle finalization lives in
`worktrees/modules/finalize.py` and is exposed as `lifecycle_finalize_task`;
it proves the landed commit is reachable from the contract's local
target/source branch, checks memory carryover, runs or verifies cleanup, and
reconciles JSON-primary task documents after landing. Runtime package data under
`src/agents_remember/package_data/` is synchronized from canonical root runtime
asset folders by `scripts/sync-runtime.py`, and the sync behavior is covered by
`mcp/tests/test_sync_runtime.py` plus the pre-commit check. The built dashboard cockpit
ships under `package_data/dashboard/`, synced from `dashboard/dist/` by
`scripts/sync-dashboard.py` (slice 05 replaces the slice-04 placeholder with the real
Vite/React bundle), covered by `mcp/tests/test_sync_dashboard.py` plus the
pre-commit/pre-push and CI `--check`.

## Route Model

- `src/agents_remember/serving/conversation/` — strict normalized structured-conversation models,
  exactly two read ports, and one root composing the independently owned `active`, `library`, and
  `control` child routers. The serving overview carries the detailed authority boundaries.
- `native_helpers/conversation_library/` — private locked Node helper for redacted repository-only
  runtime observations. Its output and fixture versions are evidence, never capability promotion.
- `serving/pi_rpc_protocol.py`, `serving/pi_rpc_process.py`, `serving/pi_rpc_events.py`, and
  `serving/pi_rpc_adapter.py` — the unregistered Pi RPC protocol/process/event/adapter chain;
  `mcp/tests/test_pi_rpc_adapter.py`, `test_pi_rpc_process.py`, `test_pi_rpc_real_smoke.py`, and
  the two `fixtures/pi_rpc/` files provide the fake, subprocess, and isolated pinned-smoke proof.

The MCP package separates three surfaces:

- `agents_remember.mcp` owns transport wiring, tool registration, and trusted
  settings parsing. Since 260703-L13 the authority file owns BOOT INFRASTRUCTURE
  only: the agentic orchestration family (`orchestration.*` — gate delegation,
  loop knobs, role knobs flat + per-level (`roles`/`rolesPerLevel`, incl. the
  L16 free-form launchArgs/promptKeywords/sessionCommands escape hatch),
  concurrency caps, spawn harness preference, and the L16 harness-definition
  table `orchestration.harnesses`) lives in
  the GLOBAL `<coordinationRoot>/system/settings.json` with
  `<code-repo>/system/settings.json` repo-local overrides, parsed PER-USE by the
  kernel loader `kernel/agentic_settings.py` (leaf-key deep merge, arrays
  replace, unknown `orchestration.*` keys fail loud naming the file; unknown
  top-level families tolerated — `contextProviders` is reserved to return
  there). `mcp/config.py` keeps ONE boot-snapshot consumer: gateDelegation is
  read from the global file at boot, with a warned one-cycle authority-file
  legacy fallback. The authority file's `providers` map runs the OPPOSITE way
  since 260707-HFX-L1 (containment R1): the boot snapshot is NOT launch
  authority — launch-capable operations re-read the map from disk through
  `reload_provider_authority`/`require_provider_launch_authority` (unreadable
  or invalid ⇒ fail-closed refusal, never a snapshot fallback), so editing
  `providers` to `{}` bites running servers immediately while stop/status/
  cleanup stay legal; `runtime_install` seeds the global file copy-if-missing and
  `spawn_agent_session` resolves its spend knobs through the loader (260703-L16 + HFX2-L10:
  repo-local level override > global level override > repo-local role default >
  global role default > spawn preference/detection-gated default; ids against
  the EFFECTIVE registry; model/effort validated per-harness at dispatch and
  APPLIED onto the harness argv; legacy caller spend fields, direct launch/session controls, and
  maintained harness-native spend/endpoint env keys refuse with `spend-override-unsupported` before
  spawning — manual: `docs/reference/harnesses.md`).
- `agents_remember.controllers` owns operation-level composition such as
  `context_packet`, provider tools, worktree tools, memory tools, benchmarks,
  and `runtime_install`.
- `agents_remember.models` owns public MCP response contracts and the
  tool-to-response-model registry used by the `mcp/tools/` payload builders.
- First-class service domains such as `kernel`, `providers`, `memory_quality`,
  `worktrees`, and `install` own deterministic behavior.
- `agents_remember.observer` owns the observable-lifecycle **event substrate +
  projection** (the 3.0 browser-dashboard direction): the append-only
  `ar-observer-event/v1` log, local ULID minting, the per-lifecycle event store,
  the ambient lifecycle + six `lifecycle_*` signal tools (with the `_tool_payload`
  emission hook attributing every tool call), and the **projection read side**: the
  pure reducer that folds the logs plus file snapshots into the resolved state tree
  — the structural surfaces (slice 3a) plus the slice-3b analytical surfaces (drift
  read from a persisted snapshot, sidecar staleness, setup, route coverage, tool
  reports, ledger), the derived rollups, and — slice 05 — the server-computed
  **attention queue** (`build_attention_queue` → the derived `Analytics.attentionQueue`), plus —
  slice 05 (5c) — paused **persistent lifecycles** synthesized from worktree contracts,
  **per-worktree provider stacks** (surface 4, bound to worktree/repo/role), Task 12's repo-covered
  workspace provider nodes (CGC watcher rows and GrepAI configured `targetRepos` become repo satellites;
  GrepAI `targetRepos` are addressable project targets inside one aggregate provider instance, not
  separate per-repo provider processes, while providers without explicit target evidence stay aggregate),
  and the **full task content** on
  `TaskDocNode` for the in-dashboard task reader. Task 29 adds lifecycle-aware raw-event lifetime
  handling and projection freshness hygiene: terminal lifecycle `events.jsonl` logs are physically
  pruned after the post-completion grace window, fresh raw-event SSE connections start from retained
  offsets instead of replaying all history, projection reads cache repo surfaces briefly, and worktree
  provider/runtime projection admits only active enclosure-backed groups instead of parked or stale
  worktrees. Task 29 S7 adds actionable-drift provenance/dismissal and keeps raw Event River row
  lifetime at the backend retention boundary rather than a frontend count cap. Task 34 re-keys that
  raw-event retention on **inactivity** rather than termination: `event_retention.py` prunes a fleeting
  or enclosure lifecycle log after >1h with no real (non-heartbeat) activity (not on `lifecycle.ended`),
  `ambient.py`'s heartbeat ticker decays after ~10 min idle so a dormant log ages out, and `/api/events`
  does one retained-backlog scan per connect, filters `lifecycle.heartbeat`, and streams a bounded
  chunked backlog. Task 32 adds physical retention for persisted
  drift snapshots: cleanup deletes the exact code-worktree snapshot for the contract being reclaimed,
  and projection prunes valid deleted-worktree drift snapshots before reading the analytical surface.
  Task 33 adds the `WorkspaceProjection.activeWorktreeGroups` field (sourced from the same
  `active_enclosure_worktree_groups` admission the Engine Room uses) that the dashboard Topology consumes
  to bound its constellation to active worktree enclosures.
  Task 21 adds the folder-keyed master token aggregate:
  `SeriesNode.seriesTokenTotal` is composed from projected sibling leaf task docs and lifecycle token totals.
  Slice 05l Part 1 (backend teardown
  visibility) extends the Engine Room surface: the reducer now projects the `abandoned` worktree
  phase (from `worktrees/modules/guidance.py`) and **drops disposed** (cleaned-up/abandoned)
  enclosures from the active `engineProcesses` so the frontend (05k) animates the teardown.
  Slice 05l Part 2 hardens the **landing-arc probe** (`worktrees/modules/landing.py`) so the
  dashboard follows a REAL remote landing: the protected target `origin/<base>` is probed **directly**
  via `git ls-remote` (visible across the whole landing window before any PR and even when `gh` is
  absent), and the PR ref carries gh's open/merge timestamp on the additive `LandingRefNode.at`.
  Slice 05m lands **carryover-before-cleanup** lifecycle correctness in `worktrees/modules/`
  (`guidance.carryover_done` reads the official ledger; `lifecycle_guidance` routes a
  `carryover-pending` phase before `cleanup-pending`; `cleanup_result` hard-refuses cleanup until the
  parked memory is carried home), and the observer reducer now follows it — `_GUIDANCE_PHASE` projects
  `carryover-pending` and the engine-room node carries the display-only `carryoverDoneAt` milestone
  (5k renders the seam). Task 13 corrects cleanup's branch and dry-run preview rules in the same
  worktree domain: task work branches are deleted only after explicit reachability proof against the
  contract source branch, and dry-runs classify worktree group directories after planned
  worktree/provider-runtime removals. Task 14 narrows cleanup to the finalized child edge: cleanup
  retires task work branches only and preserves parent/source branches for their own lifecycle edge.
  Task 23/24/L3 adds the interaction-retention read side: gate logs and operator-inbox rows are treated as
  disposable interaction records, `read_gates` can TTL-compact them, and `AgentPickupNode` projects
  pending inbox entries as waiting-for-agent/check-chat feedback for the dashboard, including L3
  sender/recipient role, message kind, artifact, and hosted-delivery metadata.
  The series-contract resolver helpers in `worktrees/task_resolver.py` now own task-name lookup,
  nested parent-task disambiguation, raw leaf `enclosures/<leaf-id>/series-contract.md` paths, archive
  exclusion, and root-task archival into `tasks/<repo>/0_archive/`; `worktrees/leaf_refs.py` owns
  qualified/doc-id/legacy-stem leaf-ref validation and canonical id normalization for write surfaces,
  including schema-marker screening for sibling task-document JSON and standalone/light `task.json`
  doc-id candidates.
  260712-PTS-L1 makes contract READS walk-free: `worktree_contract.load_contract` is
  read+parse+validate at O(one file) — a 2026-07-12 py-spy sample had the old per-read leaf-id
  resolution walk at ~9.7s of a 15s daemon sample — and leaf-id normalization is
  write-time/migration-only (master 260712-PTS decision). Legacy stem-shaped `leaf_id`s therefore
  surface RAW from reads until the explicit, idempotent `heal_contract_leaf_ids` sweep (CLI
  `heal-leaf-ids`, also on the `git_worktree_manager` facade) or a `write_contract` rewrite heals the
  file on disk; the heal cheap-skips canonical contracts via `leaf_refs.canonical_leaf_doc_ids`, one
  bounded per-task-root doc-id scan.
  Slice 09 (gate-signal
  adoption) removes the dirty-tree → `commit-approval-pending` branch from
  `worktrees/modules/guidance.py` (a visibility bug): a dirty worktree now projects its honest
  lifecycle-position phase (closeout-completed → `integration-pending`) rather than a fabricated
  commit-approval gate — the commit gate is owned by the closeout preview / a raised
  `closeout-approval` gate, never `git status`. Task 27 adds the **lifecycle
  next-step hint engine** ([next_step.py](agents-remember/mcp/src/agents_remember/mcp/tools/next_step.py)):
  a `NextStep` hint computed from the projected lifecycle state (phase +
  worktree-contract sub-state) and attached to EVERY tool response at the same
  `_tool_payload` choke point that emits the lifecycle events — the front half
  is a one-time prose rundown emitted by `lifecycle_start` (`frontHalfRundown`)
  plus a stable pointer, the linear half delegates to the worktree
  `guidance.lifecycle_guidance` state machine and overlays a gate-raise hint
  (`lifecycle_gate(kind=…)`) at the gate moments, and a terminal `lifecycle_end`
  returns a loop-back hint — generalizing the worktree-only guidance to the
  whole lifecycle spine. Task 28 introduces the **NOTIFY-AND-CONTINUE turn-end
  model**: a new non-terminal `awaiting-developer` lifecycle state
  (`observer/lifecycle_state.py` + `ambient.await_developer`/`resume_from_await`)
  and the public `lifecycle_turn_end_notification(summary)` tool (notify + stop,
  no wait/inbox) become the **active** turn-end path, the `_tool_payload` choke
  point auto-dismisses `awaiting-developer` on the next tool call, and the
  next-step hints (`decide`, the closeout/integration/cleanup overlays, the
  front-half rundown) are **repointed** from `lifecycle_gate` to it; the
  `lifecycle_gate`/`operator_inbox_*` stack is **parked** — kept and valid, but no
  longer hinted as turn-end choreography (the gate-open/blocked-gate double-emit is
  also fixed with a one-line reducer dedup). Task 30 updates the worktree closeout behavior at the
  package level: a re-closeout after a completed integration may reopen the
  integration state when new code or memory content is not yet on the source
  branch, while a clean no-op re-closeout preserves the completed integration
  markers. It is a service domain
  with its own route overview. See `docs/design/observable-lifecycle.md`.
- `agents_remember.worktrees.modules.finalize` owns the terminal
  `lifecycle_finalize_task` operation for one parent-child branch edge. It
  depends on completed closeout/integration/carryover facts, uses local Git
  ancestry against the contract source branch for both direct and PR-gated
  edges after the target branch is pulled, avoids squash-merge equivalence, and
  updates only the supplied leaf task plus immediate parent row after cleanup.
- `agents_remember.tasks` owns the **JSON-primary task document**
  (`ar-task-document/v1`): the persisted schema, the deterministic markdown renderer,
  and the JSON+md store; the `task_doc` MCP tool authors documents and the observer
  projects active JSON task docs with optional lifecycle context (slice 3c; closes note-03 gap #8).
  `task_doc` also exposes a schema-validated full-document `replace` operation for task
  resets/replans that need to rewrite structural arrays such as steps, examples, and decisions. Task 21
  adds same-root leaf-to-master row sync and batch leaf/master persistence for `task_doc` writes.
  A service domain with its own route overview.
- `agents_remember.serving` owns the **dashboard serving layer** (slice 04): a FastAPI
  app over the observer projection — one shared projector ticking `project_and_write`
  (since 260712-PTS-L3 change-driven with an idle heartbeat: `serving/change_watcher.py` watches
  the projection's input surfaces over the new `watchfiles` core dep, `--interval` is the busy
  fast-path cadence floor, `--heartbeat` — default 15s — bounds quiet-world staleness, and any
  watcher failure degrades loudly to the legacy fixed-interval ticking; `--sim` stays
  time-driven), a
  multiplexed `state` SSE stream (snapshot + per-entity deltas via `serving.delta`), a
  one-shot state endpoint, a raw `event` SSE channel with byte-offset resume
  (`serving.events`) plus a Task 29 S7 `ready` event after retained raw backlog replay, a
  `POST /api/actions/{action}` plane that records targeted gate-decision verbs as
  developer-attributed gate decisions (including stale-gate and rejection-note handling), allows
  gate-id-only `cancel` to delete stale workspace-shaped gate rows, and
  acknowledges lifecycle transitions without mutation and persists targetless actionable-drift dismissals
  (`serving.actions`), `POST /api/operator-inbox` for trusted developer/dashboard writes into
  the external-chat operator inbox, sim-mode replay over the projector's clock/feeder seams
  (`serving.sim`), and the static
  cockpit mount. Transport only (no interpretation), reading through `McpRuntimeConfig` +
  `observer.paths` (NS #5); launched by `agents-remember dashboard` (the umbrella
  `agents-remember` CLI under `cli/`; 260703 L1 makes `--config` optional there —
  `cli/discovery.py` walks upward from the working directory, the settings convention before an
  `.mcp.json` registration's recorded path, nearest wins, semantically probing usability so the
  repo's tracked placeholder template never shadows real settings). 260703 L2 adds **daemon
  supervision** (`serving/daemon.py`): `--daemon`/`--status`/`--stop` on the same CLI (state under
  `<coordinationRoot>/logs/dashboard/`; `--port` defaults from the new fail-loud `dashboard`
  settings object), and `dashboard.autoStart` makes every `agents-remember-mcp` boot ensure the
  daemon — adopt healthy, spawn absent, restart on version mismatch — via the threaded, total,
  stderr-only `maybe_autostart_dashboard` hook in `mcp/server.py` `main()`. Slice 6d-1 adds the **Mode B2 terminal host**
  (`serving.terminal`): a registry of tmux-wrapped stdlib-`pty` sessions that launch the harness
  render-not-scrape (fixed-argv, OS-user creds, localhost), opened by the
  `POST /api/terminal/{session}` opener (6e-2a/6e-2b — the dashboard spawns + owns a shell or a detected
  harness; `serving.harnesses` + `GET /api/harnesses` drive the per-harness launch buttons) and served
  over the `/api/terminal/{session}` WebSocket bridge (`serving.app`, slice 6d-2; the `websockets`
  core dep), with the xterm.js visual in 6e. Slice 6f hardens delivery into a session — the host strips
  Ctrl-Z for bare-pane harnesses, and `POST /api/terminal/{session}/image` (the `python-multipart` dep)
  carries a pasted screenshot by saving it under the session cwd for path-injection. Task 22 adds the
  durable dashboard terminal catalog (`serving.terminal_catalog`, persisted under
  `logs/dashboard/terminal-sessions.json`), `GET /api/terminal/sessions`, WebSocket rehydration of
  cataloged tmux sessions after server restart, stale-row exit marking, `POST
  /api/terminal/{session}/terminate`, and image-upload cwd fallback through the catalog. Task 22
  follow-ups keep that catalog durable across browser refresh and multi-tab use: openers create
  detached tmux sessions, each WebSocket attaches its own tmux client, browser disconnects detach
  non-destructively, and explicit termination stays hidden across later exit bookkeeping. L9 adds the
  shared `serving.terminal_leaf_assignment` move policy and the public
  `attach_terminal_session_to_leaf` MCP tool so an agent can move its hosted chat's durable `leafKey`
  through the same catalog uniqueness rules as the dashboard attach route. Agent-orchestration L2 adds the
  shared `serving.terminal_opener` (the single hosted-session opener the `POST /api/terminal/{session}`
  route and the agent-facing `spawn_agent_session` MCP tool both compose — no parallel spawn path) plus
  `serving.terminal_paste` (server-side capture-verified stdin paste — one origin baseline per delivery, history-inclusive window, probe ladder; 260707-HFX-L3 — backing a new
  `POST /api/terminal/{session}/paste` endpoint and the tool's context delivery); `serving.terminal` gains
  a `tmux new-session -e KEY=VALUE` env knob-injection seam and `serving.terminal_catalog` gains spawned-by
  provenance columns; HFX-L4 normalizes opener/attach leaf keys to canonical qualified task-doc ids
  before catalog mutation. 260707-HFX-L5 replaces task 22's immediate stale-row exit marking with
  **catalog liveness hysteresis**: the new `serving.terminal_liveness` module owns a rate-limited
  (10s default), non-overlapping probe sweeper behind `GET /api/terminal/sessions` plus the shared
  per-row observation path WebSocket attach and `/paste` use; `serving.terminal`'s probe becomes
  evidence-bearing and stderr-aware (`TmuxProbeResult` — only explicit missing-session stderr is
  definitive `pane-gone`, everything else is transient `tmux-command-failed`), and
  `serving.terminal_catalog` persists the hysteresis state via `record_liveness_probe` (3 command
  failures across ≥5s before an exit mark, pane-gone marks fast, false exits self-heal on the next
  alive probe, `terminated` never revives) — a tmux command-failure storm can no longer mass-exit
  a live fleet, and the dashboard's 1s polling no longer implies 1s tmux probing; pinned by the
  new `mcp/tests/test_terminal_liveness.py` suite. A service domain with its own
  route overview.
- `agents_remember.controlplane` owns the **gate control plane** (task 6): the durable,
  append-only `ar-gate-record/v1` `GateRecord` + `GateStore` (co-located with the observer
  event log under `observer_root`) and the five `gate_*` MCP tools (`mcp/tools/gates.py`)
  (slice 6a), plus the **enforcement policy** `enforcement.py` (slice 6b/L4): a
  `closeout-approval` gate, once developer-approved or approved by a configured
  delegated orchestration role, binds `worktree_closeout_apply` server-side (a
  model self-approval and an owner lifecycle self-approval are rejected; gateless
  lifecycles keep the chat commit gate). L4 adds `gate_policy.py`, default
  all-human settings, human-pinned integration/push/cleanup gates, and
  reviewer-verdict evidence refs for delegated approvals. Slice 09 extends `GateKind` to the full l-01
  gate spine (`plan-approval` / `worktree-intent` / `closeout-approval` / `push-approval` /
  `integration-approval` / `cleanup-approval` / `agent-question` / `provider-retry` /
  `alarm-ack`) — `closeout-approval` IS the commit gate (no separate `commit-approval`).
  `mcp/server.py` now advertises `lifecycle_gate` as the public agent-facing junction for this
  spine: it creates the typed gate, blocks the active lifecycle, waits for a developer decision or gate-specific inbox response,
  and forwards `required_decision`; the older split gate/block/wait helpers remain lower-level
  internals rather than normal public choreography. Task 28 **parks** this whole gate/inbox
  turn-end choreography behind the new NOTIFY-AND-CONTINUE `lifecycle_turn_end_notification` tool:
  `lifecycle_gate` stays registered and the durable-gate stack stays valid, but it is no longer the
  hinted turn-end path. Task 19 adds the single-current-gate invariant (new lifecycle gates
  append `expired` snapshots for older open gates), while dashboard/operator-inbox paths continue to
  provide the developer-attributed response side.
  Dashboard
  *projection* of gates is live. Task 10/L3 adds the durable operator/agent inbox
  in the same service domain: `OperatorInboxEntry` / `OperatorInboxStore`
  queue ask+response entries addressed by lifecycle, external agent, or recipient role, while
  `operator_inbox_post` / `operator_inbox_poll` / `operator_inbox_consume` expose the
  backend mailbox for chats the dashboard cannot inject into and for agent-to-agent messages that can
  also be pushed into hosted sessions. The dashboard serving layer's `POST /api/operator-inbox`
  endpoint writes the same entries with developer/dashboard attribution and L3 adds hosted push
  delivery through `serving.inbox_delivery`; `orchestration_nudge_manager` records/rate-limits nudges
  and queues manager inbox rows. A service domain with its own route overview.

The trusted MCP settings file must be absolute and outside the coordinator root.
It supplies `coordinationRoot`, `workspaceRoot`, allowed repository IDs,
allowed provider IDs, timeout caps, optional orchestration gate delegation, and
optional repository contract paths. The
server derives repository roots, memory roots, provider runtime roots, provider
data roots, and provider log roots from those settings. Tool calls name allowed
repo IDs and boolean options; they do not pass arbitrary host paths.

Provider runtime layout now uses a provider runtime root plus a central log
root under the coordinator:

```text
<coordinationRoot>/
  providers/
    runners/
      codegraphcontext/
      grepai/
    data/
      codegraphcontext/
      grepai/
  logs/
    mcp/
    providers/
      codegraphcontext/
      grepai/
      setup/
      status/
```

The `runtime_install` MCP tool operation copies runtime package assets to the
configured coordinator root and can run provider dependency installation through
package-local lifecycle code. It generates lifecycle settings from MCP settings,
not coordinator `system/settings.json`; provider setup records image locks,
setup summaries, and provider-state files through the package lifecycle code.
Settings-backed `grepai-memory` is Docker-only: the complete stack is the
managed runner image/container, PostgreSQL/pgvector, Ollama, and their shared
Docker network, with no host GrepAI binary or host Ollama fallback. Managed
GrepAI auto host-port selection prefers `61432` for PostgreSQL and `61434` for
Ollama so the dashboard/provider stack does not claim common neighboring
developer-service ports `5432` and `11434`.

The package data that `runtime_install` copies is not edited as an independent
source of truth. Canonical runtime assets live at the repository root in
`agents-md-files/`, `benchmarks/`, `providers/`, and `system/`; the sync script
replaces the corresponding package-data folders and reports missing, extra, or
changed files in check mode. Since the 260703-L10 one-vocabulary sweep the
synced coordinator and skills `AGENTS.md` templates speak the converged
`l-01-agent-lifecycles` vocabulary (Start Here — Route By Role; orchestrator
plan gate; reframe-research phase) with no retired skill names. Since
260703-L12 the synced `l-01-agent-lifecycles` tree carries the three-party-loop
build. HFX3/L14 makes the current routing explicit: otherwise-free-chat is a launcher; strategist
dispatch happens only after developer approval; a sanctioned skip routes orchestration-task
authorship to the orchestrator; the ladder ends in architect custody; and independent ready work
runs in parallel by default within the applicable concurrency cap. The tree includes
`roles/strategist.md`, `templates/orchestration-task.md` (the tenth template), and the
`criteria/` folder (five reviewer criteria
catalogs: code-seam, doctrine, onboarding-memory, report-verification,
plan-review), with the loop doctrine homed in the skill's SKILL.md and woven
into the role files.

## Invariants And Boundaries

- Route-index identity is one validated Git snapshot: repository membership and path-rule
  eligibility must not be recounted through a filesystem walk or at different moments. Git failures,
  timeouts, path-classification failures, and root mismatches stay typed and preserve their causes.
- Official-memory carryover is a write-authority boundary. Missing, invalid, unsupported, or
  semantically empty JSON/Markdown onboarding storage rules refuse before ledger, content,
  route-index, or commit mutation; parser defaults used for read/topology convenience cannot grant
  write authority.
- L9 conversation products are strict normalized contracts; package presence does not imply a
  projector, historical store, control service, or renderer.
- Active and library cursors are separate purpose-bound authorities. Exactly two read ports and
  three owned behavior-empty child routers prevent later leaves from collapsing those seams.
- The conversation-library helper resolves only inside this repository and emits redacted evidence.
  Runtime fixture versions/counts never become maintained capability declarations.
- MCP settings are authority; coordinator files can teach the model what to ask
  for but cannot grant provider or path authority.
- Hosted prompt/model/effort ordering has one bridge-generation authority. Only full operation refs
  complete work; only a certified pre-dispatch error retries; queue withdrawal is atomic with the
  native write claim; adapter/native queues and PTY paste cannot become fallback authority.
- MCP tool calls must not accept `coordinationRoot`, `sourceRoot`, provider
  runtime roots, or arbitrary filesystem paths.
- Provider install/status must use generated lifecycle settings from
  `McpRuntimeConfig`.
- Provider status reports watcher/current-state readiness and recovery actions;
  the prior runner-integrity gate was removed in the 1.0.0 remediation.
- `providers/runners`, `providers/data`, `logs/mcp`, and `logs/providers` are
  the active provider/runtime log layout; `providers/_bin`, `providers/_venvs`,
  `providers/<provider>`, and `provider-data` are not active runtime roots.
- CGC managed execution is Docker-runner owned; do not add host `venvRoot`,
  host `cgc` executable, or site-packages patch fallback paths.
- `grepai-memory` must remain Docker-or-bust in the MCP runtime; do not add
  host binary or host Ollama fallbacks.
- Resolver, provider lifecycle, memory quality, and worktree code under
  `mcp/src/agents_remember` is a package-local implementation surface. Original
  runtime scripts are not the MCP execution authority.
- Public MCP tool payloads should validate through
  `models.tool_registry.PUBLIC_TOOL_RESPONSE_MODELS`; compact context belongs
  in `ContextPacketV2`, and detailed provider state belongs in
  `provider_diagnostics`.
- Skipped provider details are still a modeled public contract: compact
  provider summaries report aggregate skipped state, omit provider detail rows,
  and rely on optional-null provider `ok` fields to survive JSON
  serialization/re-validation.
- On stdio transport the server's stdin/stdout ARE the JSON-RPC pipes:
  every `subprocess` call in the package must declare its stdin handling
  (`stdin=DEVNULL` or piped `input`), enforced by the
  `test_subprocess_hygiene.py` AST guard and the end-to-end stdio transport
  test (2.5.1, GitHub #49).
- Provider readiness is content-gated, not liveness-gated: global `ok`
  requires both running containers and actual graph/workspace content;
  healthy-but-busy targets surface in the compact summary's `indexing` list
  without degrading state (2.5.0).
- Long-running provider seed/clone operations are guarded by stall watchdogs
  (kill on zero progress), never by total-duration caps — copying index data
  instead of re-indexing is what makes rapid worktree provider deployment
  viable, and it scales with index size by design (2.5.1).
- Verbose tool responses are budgeted: bulk passthrough detail belongs in
  `temp/tool-reports/<tool>/` (keep-last-5 / 7-day write-time prune, secret
  redaction) with the compact inline outcome carrying `reportPath`;
  `test_tool_response_budgets.py` is the regression line (2.5.1/2.5.2).
- Long-running tool work must be observable, not silent: `worktree_start`
  returns within seconds and provider setup runs on a background thread that
  writes a durable, heartbeat-stamped `setup-progress.json` (`providers/
  setup_progress.py` + `worktrees/modules/provider_async.py`); `worktree_status`
  is the poll surface, a dead heartbeat projects as `stale`, and
  `retry_provider_setup` is the recovery path. The seed-refused→full-reindex
  transition is flagged as `seedFallback` the moment it happens (GitHub #53).
- In-container argv must be container-form: everything after `--` in a
  provider runner command executes inside the Linux container, so paths are
  rendered via `to_container_path` (`providers/context_common.py`) — host-form
  `C:/` paths fail silently into expensive fallbacks (GitHub #58).
- Provider containment (260707-HFX-L1): every launch-capable operation —
  watcher start/restart/invalidate-indexes, the one-shot GrepAI/CGC query
  runners, worktree provider setup, the runtime-install watcher rebind, and
  benchmark provider synthesis — re-reads the on-disk authority fail-closed
  (R1); stop/status/cleanup are never gated. Non-dry-run provider setup is
  serialized host-wide through the host-scoped `fleet_setup_lock_path()`
  flock in the system temp dir — never under a coordination root, which
  `runtime_install` prunes, nor a per-workspace benchmark root
  (R2). Containment metrics are daemon-sampled, label-discovered, and
  read-only (R4) so leftover stacks from dead sessions stay observable
  without any settings file.
- The shipped dashboard has a three-stage release boundary: editable inputs under
  `dashboard/src/` and the production config set build into `dashboard/dist/`;
  `scripts/sync-dashboard.py` copy-swaps that complete tree into
  `package_data/dashboard/` and records the build-input digest in the sibling
  `package_data/dashboard.fingerprint`; `serving.static.dashboard_static_dir()` resolves that
  packaged tree and `mount_static()` serves it at `/`. `sync-dashboard.py --check` must prove both
  source-fingerprint currency and byte-for-byte `dist`/package equality. Because the generated
  package tree is excluded from file-level onboarding, this route overview carries its release
  boundary. A hashed-bundle refresh must stage `index.html`, the fingerprint, every new asset, and
  every replaced asset deletion together; omitting either half can leave the installed wheel with
  broken asset references. The fingerprint is written during sync, so the canonical evidence order
  remains build, sync, `--check`, then served-package verification.

## Docs References

The active memory repository's `system/sources.md` has no configured Domain Documentation entries. The
generated dashboard-package boundary is established by same-repository sync code, tests, and the reviewed
FEUI-L8 build output.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external Domain Documentation source governs this generated package refresh. | `system/sources.md` checked | — |

## Cross-Repo References

The generated dashboard bundle is produced and served entirely inside `agents-remember`; no cross-repository
implementation governs its hash rollover or static mount.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Same-repository sync/build review | — |

## Repo-Internal References

### Current L9 evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The serving conversation route owns strict normalized products, exactly two read ports, and three owned child routers beneath one root — all now implemented (active L1, library L2, control L3), none behavior-empty. | L1-L1270; L1-L87; L1-L24 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py); [ports.py](agents-remember/mcp/src/agents_remember/serving/conversation/ports.py); [router.py](agents-remember/mcp/src/agents_remember/serving/conversation/router.py) |
| The private locked helper normalizes redacted observations and validates its protocol without becoming a runtime server or store. | L1-L272 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| Foundation tests pin helper resolution, fixture redaction/non-promotion, two ports, three routers, and one registration seam. | L1-L137 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |
| Hostile normalized-product matrices pin semantic authority and contradiction rejection. | L1-L1185 | [test_conversation_contracts.py](agents-remember/mcp/tests/test_conversation_contracts.py) |

### Legacy package map

| Finding | Source Path |
| --- | --- |
| MCP settings reject coordinator `system/settings.json`, forbid settings inside the coordinator, and derive provider runtime roots under `providers/runners/<provider>`. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The tool surface exposes `context_packet`, provider diagnostics, runtime, memory, worktree, benchmark, and install tools; handlers delegate to controllers and response validation flows through the model registry. | [mcp/tools/](agents-remember/mcp/src/agents_remember/mcp/tools/); [server.py](agents-remember/mcp/src/agents_remember/mcp/server.py); [tool_registry.py](agents-remember/mcp/src/agents_remember/models/tool_registry.py) |
| `server.py` installs a FastMCP shim that minifies the JSON text mirror of tool results without touching structured content. | [compact_content.py](agents-remember/mcp/src/agents_remember/mcp/compact_content.py) |
| `context_packet` composes resolver, git, worktree, compact provider summary, and optional drift and branch-freshness status into `ContextPacketV2`; detailed provider state is exposed by `provider_diagnostics`. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py); [context_packet model](agents-remember/mcp/src/agents_remember/models/context_packet.py); [provider models](agents-remember/mcp/src/agents_remember/models/providers.py); [git_freshness.py](agents-remember/mcp/src/agents_remember/kernel/git_freshness.py) |
| `runtime_install` derives install target and provider settings from `McpRuntimeConfig` and calls package-local install/lifecycle services. | [runtime_install.py](agents-remember/mcp/src/agents_remember/controllers/runtime_install.py); [install runtime](agents-remember/mcp/src/agents_remember/install/runtime.py) |
| Runtime package data is synchronized from canonical root asset folders, and tests verify missing, extra, changed, and target-scope behavior. | [sync-runtime.py](agents-remember/scripts/sync-runtime.py); [test_sync_runtime.py](agents-remember/mcp/tests/test_sync_runtime.py); [pre-commit hook](agents-remember/.githooks/pre-commit) |
| The built dashboard cockpit bundle is synchronized from `dashboard/dist/` into `package_data/dashboard/` and gated by `--check` — the built-bundle digest **plus** a source-freshness fingerprint of the build inputs (the `src` tree minus tests + the production configs, recorded in a sibling `package_data/dashboard.fingerprint`), so a `dashboard/src` change shipped without a rebuild is flagged at the commit gate the way a changed skill is. The serving app resolves and mounts this packaged tree rather than `dashboard/dist/`. | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py); [static.py](agents-remember/mcp/src/agents_remember/serving/static.py); [test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py); [test_serving.py](agents-remember/mcp/tests/test_serving.py); [pre-commit hook](agents-remember/.githooks/pre-commit) |
| Provider lifecycle settings are generated from MCP settings and include `providers/runners`, `providers/data`, `logs/mcp`, and `logs/providers` paths. | [settings.py](agents-remember/mcp/src/agents_remember/providers/settings.py) |
| Provider status reports watcher status and structured recovery actions; the prior runner-integrity check was removed in the 1.0.0 remediation. | [status.py](agents-remember/mcp/src/agents_remember/providers/status.py) |
| Provider lifecycle is now a facade plus focused provider/shared packages instead of a monolithic file. | [providers/lifecycle/](agents-remember/mcp/src/agents_remember/providers/lifecycle/); [CGC lifecycle overview](src/agents_remember/providers/cgc/lifecycle/overview.md); [GrepAI lifecycle overview](src/agents_remember/providers/grepai/lifecycle/overview.md) |
| Memory quality combines drift integrity and onboarding style checks for closeout. | [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py); [history_order.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |
| Deterministic route indexes consume one validated tracked/untracked Git census and resolved path-rule authority; route rendering reuses the frozen repository and eligible-path sets. | [route_index.py](agents-remember/mcp/src/agents_remember/kernel/route_index.py); [route_index_census.py](agents-remember/mcp/src/agents_remember/kernel/route_index_census.py); [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| Carryover validates effective official-memory JSON or Markdown storage authority before mutation and reuses it for official route-index refresh. | [carryover.py](agents-remember/mcp/src/agents_remember/memory/carryover.py); [carryover_authority.py](agents-remember/mcp/src/agents_remember/memory/carryover_authority.py); [test_carryover.py](agents-remember/mcp/tests/test_carryover.py) |
| The provider launch-authority reload/gate (containment R1), the fleet setup lock (R2), and the central containment metrics module (R4), pinned by the containment suite. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py); [provider_setup.py](agents-remember/mcp/src/agents_remember/providers/provider_setup.py); [metrics.py](agents-remember/mcp/src/agents_remember/providers/metrics.py); [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |
| The provider-only degradation detector/response protocol (260707-HFX-L7) and its dedicated settings parser, pinned by the degradation test suite. | [degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py); [provider_degradation_settings.py](agents-remember/mcp/src/agents_remember/mcp/provider_degradation_settings.py); [test_provider_degradation.py](agents-remember/mcp/tests/test_provider_degradation.py) |
| FEUI-L5 submission authority, typed lifecycle errors, public boundary, and focused race matrix. | [errors.py](agents-remember/mcp/src/agents_remember/errors.py); [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py); [harness_control_api.py](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py); [test_harness_submission_authority.py](agents-remember/mcp/tests/test_harness_submission_authority.py) |

## 260712-TRH-L4 Route Impact

L4 changes the MCP package public dispatch contract: spawn-only creation, exact-session hosted_session_readiness, and durable harness-log-confirmed dispatch-brief. The terminal catalog writer/reader contract is part of this boundary because readiness requires durable addressability.


### 260713-PHA-L5 Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## 260718-CHATS-L5I Current Route Impact

The MCP package now carries the L5I interactive-session backend hardening: active conversations reconnect through fresh server cursors, native interrupt and structured interaction answers are evidence-bound, serving avoids repeated projection/repository serialization, and terminal-backed sessions retain honest lifecycle and shutdown boundaries. Completed landing facts can freeze out of recurring remote probes but reopen into live observation. These are production behavior changes, not a new package route.

The package also owns the final mandatory commit-gate implementation: `code_quality.check` fails CRAP at or above the configured threshold by default; `worktrees/modules/code_quality_gate.py` invokes the exact worktree source and fails closed before closeout mutation; `closeout.py` and public MCP descriptions expose that order; focused tests prove default failure and zero mutation on gate failure. The pathRules-eligible packaged `c-12-closeout` skill and memory-repo git-workflow example carry the synchronized doctrine. Existing verification metadata remains pre-commit.

## 260727-CHATS-IM-L2 Route Impact

Two hot paths changed ownership without widening the MCP public surface. Active Chats projection is
now an authority-shaped package beneath `serving/conversation/active/projector/`, while the
workspace projector retains domain inputs and invalidates only the reader domains named by the
watcher. Codex history acquisition probes bounded native methods at runtime; the 128 MiB transport
fuse remains an emergency framing limit, separate from the 16 MiB materialized source-response
ceiling and smaller output-page budgets.

## Update History

- 2026-07-30T12:51+02:00 — 260727-CHATS-IM-L2 curator: the observer projection
  worker now carries explicit domain invalidations and retained fixed-slot inputs, while active
  Chats projection moved from one monolith into an authority-shaped `active/projector/` package.
  Codex native history uses runtime-probed bounded methods with typed child-local failure and a
  separate 128 MiB emergency transport fuse. Verification metadata remains pinned until closeout.

- 2026-07-26T22:20+02:00 — 260718-CHATS-L7R curator: added the load-shedding
  and concurrency-safety paragraph (per-thread pending maps, method-first
  degrade, all-pendings projection with rotation, entry-thread guard,
  load-shed event queue). Verification metadata remains pre-commit.
- 2026-07-26T18:45+02:00 — 260718-CHATS-L7 curator: added the multiplexed
  harness sub-agent paragraph (adapter thread demux, additive agent grammar,
  one-projection multiplexed serving, library grouping, gated claude text
  forwarding). Verification metadata remains pre-commit.
- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  added the mandatory quality-wrapper, closeout adapter, public-description,
  packaged-skill/example, and focused-test route impact. Verification metadata
  remains pre-commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T12:00+02:00 — No route impact: 260718-CHATS-L5P (dashboard-only cockpit chrome visual
  polish, PASS-WITH-NOTES) regenerated the shipped `src/agents_remember/package_data/dashboard/` bundle
  (rebuilt `assets/*.js`/`*.css`, `index.html`, `dashboard.fingerprint`) via the established
  `sync-dashboard.py` mechanism; `--check` confirmed the bundle matches `dashboard/dist`. This is shipped
  build output, not an `mcp/` source contract — zero backend `.py` edits (`ruff check mcp/src` clean).
  No package structure, route, wire contract, or capability changed. Verification metadata unchanged.
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: corrected the package overview's L1 capability
  line — since 260718-CHATS-L5F R4 (developer ruling 2026-07-21) THE CONTRACT IS THE ONLY GATE, so the
  "claude `unverified` at installed 2.1.214 vs locked 2.1.211" version-demotion wording was FALSE and is
  now the never-probed contract reason (no version-string comparison demotes any capability). The
  detailed half-time functional truths (R1 codex notification identity, R2 claude acceptance, R3 claude
  frame contracts, R5 per-session bounds/release, R6 exit-note + metrics timeout, R7 durable E2E) live
  in the `serving/` and `serving/conversation/` overviews. No package-level structure changed.
  Verification stays pinned until L5F closeout stamps the candidate commit.
- 2026-07-21T11:00+02:00 — No route impact: reviewed the 260718-CHATS-L5 production-E2E hardening
  (three source edits — the `terminal_liveness.py` per-entry hosted-interaction-synchronizer
  quarantine, the active projection-store input-authority pin, and the active projector's
  disjoint-id-namespace twin filter — plus new/extended regression suites) against this package
  overview. No package-level structure, route, wire contract, or capability changed, and the
  `serving.terminal_liveness` service-domain summary still holds (the module still owns the
  rate-limited sweep; H1 only contains a downstream side-effect failure per row rather than 500-ing
  the catalog). The conversation-slice hardening lands inside `conversation/active/` and
  `conversation/projectors/`, already routed to their governors and to the `serving/` and
  `mcp/tests/` overviews; detail lives there. Verification metadata unchanged.
- 2026-07-20T22:30+02:00 — No route impact: the only governed change under `mcp/` for 260718-CHATS-L4
  (structured Chats renderer, reviewer FINAL PASS) is the regenerated `package_data/dashboard/` bundle
  assets + `dashboard.fingerprint`, a generated artifact mirroring `dashboard/src`; the route's own
  claims are unaffected — shipped output produced by
  `scripts/sync-dashboard.py` from `dashboard/dist/`, exactly the sync mechanism this overview already
  documents; no mcp source, wire contract, route, or capability changed (backend diff-verified empty
  every review round; pytest 2741 passed unchanged). The renderer itself lives in `dashboard/src/` and
  is governed by the dashboard overviews; the "package presence does not imply a renderer" invariant
  and the leaf-scoped L9/L0 "no renderer yet" narrative remain accurate about the mcp package's Python
  contract. Verification metadata unchanged.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: documented the implemented authoritative control
  child at package granularity — the seventeen control routes (interrupt, source-aware queue with
  cockpit-only withdrawal recovery, typed attachments, read-only policy, evidence-bound telemetry)
  over the closed L2E/L3E substrate, the opaque signed reference authority, and the per-app control
  service — routed to the new `conversation/control/overview.md` and the `mcp/tests/` governor, and
  corrected the "three behavior-empty child routers" evidence row to the now-implemented reality.
  Verification metadata stays pinned until L3 closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: documented the additive native control-plane
  substrate at package granularity — the interrupt write, paged never-bodies timeline,
  digest-verified asset channel, and once-only withdrawal recovery inside the hosted
  harness-control family, with the regression set routed to `mcp/tests/overview.md` and detail to
  the `serving/` governor. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  package-granularity paragraph and history with the L1 active-serving paragraph after the
  master memory branch advanced; both implemented slices are documented, routed to the
  `serving/`, `conversation/`, `conversation/active/`, `conversation/projectors/`,
  `conversation/library/`, and `mcp/tests/` governors for detail. Verification metadata remains
  pinned until L1 closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: documented the implemented active
  conversation serving at package granularity — the two authorized active routes, signed cursor
  authority, bounded service/projector engines, idempotent store with the review-F1 block
  union, the canonical status service now backing orchestration's seat projection, fixture-gated
  capabilities, and the pure per-harness mapper grammars — routed to the `serving/`,
  `conversation/`, `conversation/active/`, `conversation/projectors/`, and `mcp/tests/`
  governors for detail. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: documented the implemented native
  conversation library at package granularity — the five authorized library routes and three
  dormant ports (Codex direct, Claude/Pi through the newly implemented locked helper entries),
  live capability gates, the per-app signed token authority, and the idempotent exact open with
  honest retirement — routed to the `serving/`, `conversation/`, `conversation/library/`,
  `native_helpers/conversation_library/`, and `mcp/tests/` governors for detail. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the native evidence and resume
  substrate at package granularity — reserved-key evidence diversion into the bounded bridge
  buffer with byte-identical projections, the three additive epoch-scoped IPC reads across
  disjoint coordinate domains, per-harness native pages (claude fail-closed), the sole-path
  provenance batch, and the codex-only resume channel — routed to the `serving/` and `mcp/tests/`
  governors for detail. Verification metadata remains pinned until closeout stamps the candidate
  commit.
- 2026-07-19T00:37+02:00 — 260718-CHATS-L0 curator: documented the conversation runtime
  composition repair at package granularity — the install-once immutable `ConversationRuntime`
  and server-resolved local-operator resolver bound through the existing harness-control
  registration, the `coordination_root` scope wiring, the two child-facing request dependencies,
  and the `ConversationCompositionError` family. Verification metadata remains pinned until
  closeout stamps the candidate commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: documented the one-snapshot Git/path-rule route-index
  boundary, explicit caller authority, typed census failures, and fail-closed official-memory
  carryover settings preflight. The kernel and memory folders remain governed by this package
  overview; no additional shallow route overview was introduced.
- 2026-07-18T15:22+02:00 — No route impact: FEUI-MX-FIX-2 only rolls the generated synchronized
  dashboard index, fingerprint, and hashed assets under `package_data/dashboard/`; authoritative
  session-open behavior lives in `dashboard/src/`, and package parity is proven by the dashboard
  sync check. Verification metadata remains pinned pending candidate closeout.

- 2026-07-18T13:04+02:00 — 260715-FEUI-L9R ancestor route repair: documented the MCP package's
  existing serving boundary for optional shipped-dashboard identity, HTML revalidation, narrow
  pre-session harness discovery, server-owned raw-event records, and clean dashboard tmux client
  identity. Browser recovery remains under `dashboard/src/`; serving detail and regression proof
  remain under `mcp/src/agents_remember/serving/` and `mcp/tests/`; synchronized dashboard assets
  remain generated package output.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the package-level structured
  conversation contract route, repository-only locked observation helper, exact two-port/
  three-router topology, single registration seam, hostile contract/foundation gates, and the
  non-promotion boundary for redacted runtime fixtures. Verification remains pinned to committed
  source truth until closeout stamps the candidate.
- 2026-07-18T07:43+02:00 — No route impact: 260715-FEUI-L8 rebuilt and synchronized the accepted
  dashboard source into `package_data/dashboard/**` and refreshed `package_data/dashboard.fingerprint`
  through the existing `scripts/sync-dashboard.py` boundary. The hashed asset churn is generated output
  excluded from file-level onboarding; it changes no MCP Python source, server contract, tool surface, or
  package architecture. Canonical Chats behavior is documented under `dashboard/src/` and its design
  evidence route. Verification metadata remains pinned until closeout stamps the L8 code commit.
- 2026-07-18T00:08+02:00 — No route impact: 260715-FEUI-L7 rebuilt and synchronized the accepted
  dashboard source into `package_data/dashboard/**` and refreshed
  `package_data/dashboard.fingerprint` through the existing `scripts/sync-dashboard.py` boundary.
  The generated bundle churn is excluded from file-level onboarding and changes no MCP Python
  source, server contract, tool surface, serving boundary, or package architecture; the L7
  inspector/status behavior is documented under `dashboard/src/`. Verification metadata remains
  pinned until closeout stamps the L7 code commit.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: documented the package-level sole submission
  authority, epoch/full-ref identity, atomic dispatch/withdraw, certified retry/error family,
  raw-free bounded lifecycle API, and dispatch-now native adapter boundary.
- 2026-07-17T10:21+02:00 — No route impact: 260715-FEUI-L4 fix round 4 rebuilt and
  synchronized the accepted dashboard source into `package_data/dashboard/**` and refreshed
  `package_data/dashboard.fingerprint` with `scripts/sync-dashboard.py`. The hashed asset churn is
  generated output excluded from file-level onboarding; it changes no MCP Python source, server
  contract, tool surface, or package architecture. The frontend behavior remains documented at
  the `dashboard/src/` route. Verification metadata remains pinned until closeout stamps the L4
  code commit.
- 2026-07-17T06:35+02:00 — No route impact: 260715-FEUI-L3 shipped-dashboard bundle resync —
  the `package_data/dashboard/**` asset churn plus the refreshed
  `package_data/dashboard.fingerprint` are the generated artifact copy of the rebuilt
  `dashboard/dist` per `scripts/sync-dashboard.py` (the source-aware sync invariant this overview
  already documents); this leaf made NO mcp source, server, or architecture change. Reviewed and
  unaffected; hashed generated assets stay outside file-level onboarding, and the frontend change
  itself is documented at the `dashboard/src/` route. Verification metadata remains pinned until
  closeout stamps the L3 code commit.
- 2026-07-17T04:20+02:00 — No route impact: 260715-FEUI-L6 shipped-dashboard bundle resync —
  the `package_data/dashboard/**` asset churn plus the refreshed
  `package_data/dashboard.fingerprint` are the generated artifact copy of the rebuilt
  `dashboard/dist` per `scripts/sync-dashboard.py` (the source-aware sync invariant this overview
  already documents); this leaf made NO mcp source, server, or architecture change (the leaf's
  answer path CONSUMES the existing `/api/actions/approve` gate route and terminate/landed-cleanup
  endpoints unchanged). Reviewed and unaffected; hashed generated assets stay outside file-level
  onboarding, and the frontend change itself is documented at the `dashboard/src/` route.
  Verification metadata remains pinned until closeout stamps the L6 code commit.
- 2026-07-17T02:30+02:00 — No route impact: 260715-FEUI-L2 shipped-dashboard bundle resync —
  the `package_data/dashboard/**` asset churn plus the refreshed
  `package_data/dashboard.fingerprint` are the generated artifact copy of the rebuilt
  `dashboard/dist` per `scripts/sync-dashboard.py` (the source-aware sync invariant this overview
  already documents); this leaf made NO mcp source, server, or architecture change. Reviewed and
  unaffected; hashed generated assets stay outside file-level onboarding, and the frontend change
  itself is documented at the `dashboard/src/` route. Verification metadata remains pinned until
  closeout stamps the L2 code commit.
- 2026-07-17T00:50+02:00 — No route impact: 260715-FEUI-L1 shipped-dashboard bundle resync —
  the `package_data/dashboard/**` asset churn plus the refreshed `package_data/dashboard.fingerprint`
  are the generated artifact copy of the rebuilt `dashboard/dist` per `scripts/sync-dashboard.py`
  (the source-aware sync invariant this overview already documents); no mcp source, server, or
  architecture change. Reviewed and unaffected; hashed generated assets stay outside file-level
  onboarding, and the frontend change itself is documented at the `dashboard/src/` route.
  Verification metadata remains pinned until closeout stamps the L1 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: documented package-wide daemon advertise,
  complete-pair launch, exact-session set, reliable whole-message submit/reconcile, install/auth
  cache fencing, live-reopen truth, first-byte ambiguity, idempotent request ids, public raw
  stripping, and liveness-first status classification while preserving role spawn and the durable
  bus. Verification metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: documented the package-wide same-session set
  port, shared FIFO ordering, exact `SetResult` vocabulary, Claude correlated terminal proof,
  Codex desired/pending/effective fresh-turn state, Pi bounded response/readback/catalog coherence,
  cancellation reclamation, and the complete no-paste delegate boundary. Role/leaf provenance and
  the durable inbox bus remain unchanged. Verification metadata remains pinned until closeout
  stamps the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added the package-wide settings-to-native
  launch path, model-gated token-free validation, pre-discovery conflict refusal, exact failed-state
  evidence, no-normalized-paste boundary, role/bus preservation, and synchronized packaged-doctrine
  impact. Verification metadata remains pinned until closeout stamps the L2 code commit.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the package route body for
  structured harness negotiation and the complete serving reload boundary; R10 remains deferred.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator: added the Codex app-server adapter to the MCP
  package route model, including the exact-version stable protocol boundary, protocol-only effort,
  bounded state, and no-production-cutover ownership. Verification remains pinned until closeout
  stamps the leaf commit.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: documented the package-route impact of the
  unregistered Pi RPC protocol/process/event/adapter chain and its fixtures/tests. Verification
  metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: refreshed the package route body for
  the normalized harness-control contract, bounded bridge, private IPC, and no-cutover boundary.

- 2026-07-12T20:24+02:00 — 260712-PTS-L3 route impact: the serving projector's pacing is now
  change-driven + heartbeat (new `serving/change_watcher.py`; `--heartbeat` on the dashboard CLI
  and daemon ensure/spawn; `--interval` re-documented as the fast-path cadence floor) and
  `pyproject.toml` gained the `watchfiles>=1.1,<2` core runtime dependency. The old behaviour
  re-projected the whole world every 1s regardless of change (py-spy 2026-07-12: `_tick_sync`
  11.1s of a 15s sample). Detail in the `serving/` route overview and the
  `change_watcher.py`/`projector.py`/`app.py`/`daemon.py`/`cli/dashboard.py`/`pyproject.toml`
  sidecars. Verification metadata pinned until closeout stamps the PTS-L3 commit.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1 route impact: worktree contract reads are now walk-free
  (`load_contract` = read+parse+validate, O(one file); the removed per-read leaf-id resolution walk
  cost ~9.7s of a 15s py-spy daemon sample on 2026-07-12), leaf-id normalization is
  write-time/migration-only, and the explicit idempotent `heal_contract_leaf_ids` sweep (CLI
  `heal-leaf-ids`; facade re-export) rewrites legacy stem-shaped leaf ids to doc ids once — legacy ids
  surface RAW from reads until healed. Detail in the `worktrees/worktree_contract.py`,
  `worktrees/leaf_refs.py`, `worktrees/modules/cli.py`, and `worktrees/git_worktree_manager.py`
  sidecars. Verification metadata pinned until closeout stamps the 260712-PTS-L1 commit.
- 2026-07-12T17:50 — No route impact: 260712-TRH-L6 only changed the frontend `dashboard/src/panels`
  Operations presentation and its generated `package_data/dashboard` bundle. No MCP Python module,
  serving contract, tool surface, package route, or generated MCP artifact changed; the dashboard route
  and its six handwritten sidecars carry the behavior detail.
- 2026-07-12T17:45+02:00 — No route impact: L7's required dashboard prepare/build/sync regenerated `package_data/dashboard/`, its fingerprint, index, and hashed assets only; the mcp package route contract and Python-serving responsibilities are unchanged. L7 behavior remains documented by the in-scope `dashboard/src/`, `observer/`, `serving/`, and `worktrees/modules/` routes.

- 2026-07-12T16:55+02:00 — No route impact: L1's dashboard build/sync changes only the generated
  `package_data/dashboard/` assets and sibling fingerprint within the already-documented static
  build/package/serve boundary; no MCP route, tool, Python package, or serving contract changed.

+## 260712-TRH-L4 Route Impact

L4 changes the MCP package public dispatch contract: spawn-only creation, exact-session hosted_session_readiness, and durable harness-log-confirmed dispatch-brief. The terminal catalog writer/reader contract is part of this boundary because readiness requires durable addressability.

- 2026-07-12T13:46+02:00 — No route impact: 260712-TRH-L3 is dashboard-only. The collapsible task-group
  source change and the generated `package_data/dashboard` hash rollover do not change MCP routing or
  runtime responsibilities. Verification metadata remains pinned until closeout.
- 2026-07-12T13:36+02:00 — No route impact: 260712-TRH-L2 body review confirms the changeset API refinement is documented at the governing `mcp/src/agents_remember/serving/` route; the broader `mcp/` package route inventory and purpose are unchanged. Verification metadata remains pinned until closeout.
- 2026-07-12T12:28+02:00 — No route impact: 260712-TRH-L1 changes the MCP package only through
  the rc5 version/fallback bump, the already-established generated dashboard bundle boundary, and a
  calendar-stable harness-log test fixture. No MCP tool, response model, Python package route, or
  serving contract changes in this leaf.

- 2026-07-10T22:18+02:00 — 260707-HFX2-L20 package route impact: documented monotonic terminal
  inbox folding and durable consume retention across the control-plane store and MCP consume tool.

- 2026-07-10T21:59+02:00 — No route impact: 260707-HFX2-L21 is frontend-only. The adjustable,
  persisted Chats sidebar rebuild changes `package_data/dashboard/` and its fingerprint, but no MCP
  Python source, tool surface, package route, or serving contract. `sync-dashboard.py --check` and
  the package-sync tests verify the existing release boundary.

- 2026-07-10T19:49+02:00 — No route impact: positional 260707-HFX2-L19 F1 adds one focused
  `test_supervisor.py` regression for the already-documented hosted-delivery retry-exhaustion
  boundary. It changes no MCP tool, response model, package route, production behavior, or entity
  split; the existing Supervisor Sweep entity is refreshed separately because its production
  evidence path already changed in the release-tail candidate.

- 2026-07-10T18:30+02:00 — No route impact: 260707-HFX2-L18 is a behavior-preserving strict-CRAP
  decomposition inside the existing spawn controller and terminal catalog plus two focused tests.
  It adds no MCP tool, response model, package route, threshold/configuration change, or L19
  release-tail behavior.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17 package route impact: documented end-to-end pair
  binding across catalog, tools, control plane, supervisor, provider discovery, dashboard, and
  tests, plus the source/build/serve-only package-sync evidence boundary. Verification metadata
  remains pinned until closeout stamps L17.

- 2026-07-10T13:56+02:00 — 260707-HFX2-L16 final package route impact: documented the complete
  dashboard source-to-build-to-package boundary, runtime static resolution from the packaged tree,
  the dual fingerprint/tree `--check`, and atomic staging of hashed additions with replaced-asset
  deletions. Verification metadata remains pinned until closeout stamps the eventual L16 code
  commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 package route impact: documented the harness-log
  acceptance path, calibrated duplicate-safe recovery, explicit Codex argv, catalog/replacement
  provenance, and checkout-local test pin. Verification metadata remains pinned until closeout
  stamps the eventual L15 code commit.

- 2026-07-10T02:39+02:00 — HFX3/L14 combined route impact: reconciled packaged runtime doctrine
  to the free-chat launcher, approval-gated strategist with sanctioned-skip authoring, architect
  terminal custody, and parallel-by-default dependency scheduling. Replaced the superseded
  immortal-pending route claim with the 48-hour TTL / 500-row health cap. Verification metadata
  remains pinned until closeout stamps the eventual two-parent code commit.

- 2026-07-10T01:27+02:00 — 260707-HFX2-L13 closeout-follow-up route impact: added the governing
  package summary for live virtual-cursor river compaction, heartbeat coalescing/reclamation,
  summary-only task broadcasts plus on-demand bodies, manager-first completion/signal routing,
  chain-aware supervisor suppression, rung pacing, and the cross-route CS-6 regressions. Preserved
  reviewer S1 as HFX2-L14 S7 and the separate HFX3 retro gate. Verification metadata remains pinned
  until closeout stamps the eventual L13 code commit.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: reviewed route impact for the CS-6 store/projection/process scaling sweep and updated the route summary for changed files. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 route impact (landed chat archive + group cleanup):
  `controllers/worktree_tools.py`'s completion-edge hooks (`worktree_integrate`/
  `lifecycle_finalize_task`) now call `serving/landing.py::land_seats_for_leaf` (new file) instead of
  auto-retiring successful worker/reviewer/manager seats; `serving/terminal_catalog.py` gains a
  `status:"landed"` state with landing provenance; `serving/terminal_liveness.py`'s background sweep
  skips landed rows (a CS-6-class fix, see the leaf's reviewer verdict); `mcp/config.py` renames the
  auto-behavior settings to `autoLandOn{Integration,Finalize}` (legacy `autoRetireOn*` aliased);
  `serving/retire.py` keeps manual/explicit retire authority unchanged and drops the now-dead
  `retire_seats_for_leaf` bulk helper. Per-file detail lives in the already-updated `serving/`
  sub-route overview and file sidecars. Verification metadata pinned until closeout stamps the
  260707-HFX2-L11 commit.
- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 route impact (spawn settings authority): refreshed the
  package overview's spawn-dispatch and agentic-settings route model so settings are the spend
  authority; caller spend fields/env overrides now refuse with `spend-override-unsupported` instead
  of forming an explicit-argument precedence rung. Detail lives in `mcp/tools/terminal.py`, the
  settings/harnesses reference docs, and the spawn tests. Verification metadata pinned until
  closeout stamps the 260707-HFX2-L10 commit.
- 2026-07-09T11:45+02:00 — No route impact: 260707-HFX2-L9 (supervisor redelivery cadence + signal
  throttling) adds a 900-second redelivery floor and a new persisted signal cooldown store
  (`controlplane/supervisor_signals.py`). Per-file detail lives in the already-updated
  `controlplane/` and `serving/` sub-route overviews and their sidecars (curator pass,
  260707-HFX2-L9); the mcp package's own layout and routing are unchanged. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-09T11:25+02:00 — No route impact: 260707-HFX2-L8 (stability/bounded-resource/guaranteed-
  reclamation doctrine) touches `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-
  lifecycles/criteria/code-seam.md` and `.../plan-review.md` (CS-6/PR-6 candidate criteria added) and
  root `AGENTS.md` (one cross-reference sentence). This is a skill-catalog CONTENT change synced from
  the canonical repo-root `skills/` tree via `scripts/sync-skills.py`, not a package structure or
  module-responsibility change; the package layout and routing this overview describes are
  unchanged. Per-file detail lives in the already-updated `code-seam.md`/`plan-review.md` package-
  data sidecars (curator pass, 260707-HFX2-L8). Verification metadata pinned until closeout stamps
  the 260707-HFX2-L8 commit.
- 2026-07-09T00:20+02:00 — 260707-HFX2-L7 route impact (CORRECTED LABEL 2026-07-09: this entry was
  written and landed while the dead-seat-storm fix leaf was still numbered L8, before the same-day
  positional renumbering moved it to L7; the content below is L7's, not the current L8 doctrine
  leaf) (dead-seat redeliver termination + bounded
  inbox sweep): the package-level `kernel/agentic_settings.py` loader gains one `orchestration.
  supervisor` field — `redeliverBudget` (default 250, defaults-safe, `_require_positive_int`). NEW
  durable `ladder-resolved` terminal inbox state on `controlplane/operator_inbox_records.py`,
  excluded from redelivery via a state-keyed `is_ladder_resolved` predicate in
  `controlplane/inbox_backoff.py` and compacted by `controlplane/interaction_retention.py` (pending/
  unacked always preserved). `serving/supervisor.py` threads one in-sweep inbox snapshot through all
  mutators (kills the per-finding O(n^2) re-fold); `serving/supervisor_heartbeat.py` surfaces backlog
  counts + last-sweep duration onto `/api/state` and the dashboard header. Minimal boot-safety
  non-task-JSON skip in `worktrees/leaf_refs.py` (schema-marked malformed docs still fail loud).
  Cross-route change fully documented in `controlplane/`, `serving/`, and `dashboard/src/` overviews
  this file governs; recovery runbook in `docs/design/observable-lifecycle.md`, settings row in
  `docs/reference/settings-json.md`. New scale regression: a 2000-row dead-seat-storm sim in
  `mcp/tests/test_liveness_simulations.py`. Reviewer verdict APPROVE-WITH-NITS, R1-R6 all PASS.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L7 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 route impact (doctrine rewrite + focused liveness
  simulations): the `l-01-agent-lifecycles` package-data doctrine mirror inverts from active
  owner-side vigilance to a passive process-and-ack contract across 5 canonical files (`SKILL.md`,
  `roles/manager.md`, `roles/orchestrator.md`, `roles/worker.md`, `templates/turn-report.md`), synced
  to all 9 downstream package copies; explicit watcher ban (uniform-mechanism ruling 2026-07-07).
  Zero Python touched. New test sidecar: `mcp/tests/test_liveness_simulations.py` (11 tests, 8 named
  P-15 fixture-zoo incidents, 6/8 fully end-to-end through `run_supervisor_sweep`, 2/8 honestly
  hybrid pending a pane-capturer injection follow-up — see `Supervisor Sweep`'s Migration Notes in
  `entities.md`). Results filed in `notes/reports/260707-HFX2-L5-liveness-report.md`. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L5 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 route impact (P-15 tier 3 escalation ladder + dead-man
  respawn): the package-level `kernel/agentic_settings.py` loader gains the `orchestration.escalation`
  family (`EscalationSettings` — per-kind SLA, per-rung dwell, renudge rate limit,
  respawn-after-rung), consumed by the SAME `serving/app.py::_supervisor_context()` call site the
  supervisor family already wires through (no new lifespan task). Backs two new `controlplane/`
  modules (`escalation_ladder.py`, `orphan_policy.py`) and a new two-hop `signal_routing.
  derive_skip_level_owner`/`is_seat_dead` pair, plus two new `serving/supervisor.py` predicates/
  actions. Fully documented in `controlplane/overview.md` and `serving/overview.md`, both governed
  by this file. New test sidecar: `mcp/tests/test_escalation_ladder.py`. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L4 commit.
- 2026-07-08T22:30+02:00 — No route impact: 260707-HFX2-L3 (paste injector
  hardening, R1-R5) adds two `serving/` modules (`harness_adapters.py`, `injector.py`) and refactors
  `serving/inbox_delivery.py` + `mcp/tools/terminal.py::_deliver_spawn_pastes` onto the one delivery
  path they introduce; no new package-level settings family, no change to `kernel/agentic_settings.py`
  or any tool's public parameter/response shape. Fully documented in `serving/overview.md`, which
  this file governs. New test sidecars: `mcp/tests/test_harness_adapters.py`,
  `mcp/tests/test_injector.py`. Verification metadata pinned until closeout stamps the
  260707-HFX2-L3 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 route impact (supervisor sweep + predicates): the
  package-level `kernel/agentic_settings.py` loader (governed here, since `kernel/` has no own
  route-local overview) gains the `orchestration.supervisor` family — `SupervisorSettings` (enabled/
  interval/staleness-cutoff/redeliver-rate-limit), consumed across TWO other package routes:
  `serving/app.py`'s new supervisor-sweep lifespan task and `mcp/tools/base.py`'s per-tool-call
  staleness banner. Same cross-route-consumption shape the L1 entry above documents for the
  expectation-row family — a genuine package-level settings addition, not confined to one child
  route's onboarding. The sweep subsystem itself (`serving/supervisor.py`,
  `serving/pane_signals.py`, `serving/supervisor_heartbeat.py`) is documented in full in
  `serving/overview.md`, which this file governs. Verification metadata pinned until closeout
  stamps the 260707-HFX2-L2 commit.
- 2026-07-08T16:15+02:00 — 260707-HFX2-L1 route impact (curator delta round 2, closeout-preview
  gap; not reviewed in this leaf's first curator pass, which only touched the child
  `controlplane/overview.md`/`observer/overview.md`): the new durable expectation-row/backoff/
  routing stack (R1-R4) is genuinely package-level shape, not confined to one child route — it adds
  a new controlplane primitive (`expectation_rows.py`) consumed atomically by THREE separate
  `mcp/tools/` payload builders (`terminal.py`, `gates.py`, `operator_inbox.py`), plus two more new
  controlplane modules (`inbox_backoff.py`, `signal_routing.py`) and new `OperatorInboxEntry`
  fields. Added a Purpose paragraph naming all four R-numbers and the cross-tool dispatch pattern,
  matching this file's established per-leaf narrative convention. Verification metadata pinned
  until closeout stamps the 260707-HFX2-L1 commit.
- 2026-07-08T15:45+02:00 — 260707-HFX2-L7 release-tail route impact: `mcp/pyproject.toml`,
  `mcp/src/agents_remember/mcp/__init__.py`, and README pins/status move to 3.0.0rc4; packaged
  `l-01-agent-lifecycles` runtime doctrine now classifies developer clarifications by active queue
  and current-diff fit before note-only handling; and `serving/supervisor.py` keeps
  `"no-hosted-session"`/`"unconfirmed"` delivery-failure rows in the redelivery path until
  `PERSISTENT_FAILURE_ATTEMPTS` or `escalatedAt`. No new MCP tool signature, settings family, or
  inbox kind.
- 2026-07-08T15:27+02:00 — No route impact: 260707-HFX2-L6 is a package-data lifecycle doctrine
  clarification only. The synced runtime skill mirrors now tell agents that a developer-declared
  role takeover means the named task leaf is the seat and the current dashboard terminal catalog
  session must be attached/renamed/verified before lifecycle work continues; close/current/small
  developer clarifications that fit the active leaf should be implemented in that leaf instead of
  filed as future notes; and accepted orchestrated-series authority lets owning seats perform
  subordinate closeout/integration/finalization/cleanup after clean previews without repeated
  developer formality. Final super/PR-carryover, raised human-pinned gates, scope changes,
  out-of-scope red checks, and quo-vadis decisions still stop for the developer. No MCP tool
  signature, controller, schema, provider, worktree, or serving route behavior changed.
- 2026-07-08T04:25+02:00 — 260707-HFX-L12 route impact (master-exit fix leaf, closes Finding 1):
  `controlplane/operator_inbox_records.py`'s `AgentRole` gains `architect`/`curator`;
  `InboxMessageKind` gains `decision-item`/`decision-ruling` — making the HFX-L6-ratified minimal
  decision-item relay representable and round-trippable through the operator inbox for the first
  time (previously the exact doctrine-mandated call raised `ValidationError`). Pure schema
  extension; no other consumer enumerates these Literals exhaustively. Pinned by a new round-trip
  test in `mcp/tests/test_operator_inbox.py`. Verification metadata pinned until closeout stamps
  the HFX-L12 commit.
- 2026-07-08T03:05+02:00 — 260707-HFX-L8 route impact (seat lifecycle: retirement + live identity +
  turn-state, issues #12/#4): NEW `serving/retire.py`, `serving/retire_policy.py`,
  `serving/turn_state.py`, `serving/seat_events.py`; new `session_retire`/`session_rename` MCP tools
  (+ matching `POST /api/terminal/{session}/retire`/`rename` routes); server-side retirement
  authority policy (owner-never-self-retires; manager scoped to its own master; orchestrator
  portfolio-wide); automated retirement at the `worktree_integrate` and `lifecycle_finalize_task`
  completion edges (config-gated, best-effort, never able to fail the edge it rides); a live
  turn-state classifier riding the existing L5 liveness-sweep cadence. Per-file detail lives in the
  `serving/`, `mcp/tools/`, `models/`, and `controllers/` route overviews and the touched file
  sidecars.
- 2026-07-08T02:10+02:00 — No route impact: 260707-HFX-L11 (curator activation) adds one new
  package-data-mirrored doctrine file (`templates/curator-brief.md`, propagated by
  `scripts/sync-skills.py` into `package_data/runtime/skills/l-01-agent-lifecycles/templates/`
  alongside the existing worker-brief/manager-brief templates) and edits the prose bodies of six
  existing package_data-mirrored skill files (`roles/curator.md`, `roles/manager.md`,
  `templates/manager-brief.md`, `SKILL.md`, `c-12-closeout/SKILL.md`,
  `c-05-create-or-update-onboarding-files/SKILL.md`) — same mechanism (sync-propagated bundle
  copies of the canonical `skills/` tree) this package already documents; no new module, package
  boundary, or route shape. Per-file detail lives in the touched file sidecars.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 route impact: the package gains the provider degradation
  protocol — NEW `providers/degradation.py` (detector/state-machine + durable events +
  role-addressed inbox alerts + critical-threshold failsafe stop) and NEW
  `mcp/provider_degradation_settings.py` (the `providerDegradation` settings parser
  `mcp/config.py` now wraps); `serving/app.py`'s metrics sampling loop calls the detector once per
  tick. Providers-only this iteration; Sentry (260703_spotlight-dev-observability) is the
  designated future detection source. Verification metadata pinned until closeout stamps the
  HFX-L7 commit.
- 2026-07-08T00:05+02:00 — 260707-HFX-L5 route impact (catalog liveness hysteresis): the serving
  domain gains `serving.terminal_liveness` — a rate-limited, non-overlapping liveness sweeper
  behind `GET /api/terminal/sessions` plus the shared per-row observation path WebSocket attach
  and `/paste` use — replacing `serving.app`'s immediate stale-row exit marking;
  `serving.terminal`'s probe is now evidence-bearing/stderr-aware (`TmuxProbeResult`) and
  `serving.terminal_catalog` persists hysteresis state via `record_liveness_probe`
  (evidence-scaled thresholds, self-healing false exits, `terminated` never revived). NEW suite
  `mcp/tests/test_terminal_liveness.py` pins storm/pane-gone/self-heal/rate-limit/overlap/stderr
  behavior. Verification metadata pinned until closeout stamps the HFX-L5 commit.
- 2026-07-07T23:55+02:00 — 260707-HFX-L6 route impact: the package role surface now
  distinguishes developer-facing architect sessions from spawned backend orchestrators and includes
  curator in the runtime skill mirrors, settings role vocabulary, dashboard role projection, and
  manager/worker closeout chain. Verification metadata pinned until closeout stamps the HFX-L6
  commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2 route impact: the qualified leaf-ref resolver now skips
  non-task sibling JSON artifacts by raw task-document schema marker, keeps malformed marker-bearing task
  docs loud, indexes standalone/light `task.json` docs, and preserves read-path legacy contracts when
  active-task resolution cannot prove a mapping. Verification metadata pinned until closeout stamps the
  260707-HFX-L4 commit.
- 2026-07-07T23:30+02:00 — 260707-HFX-L4 route impact: added dedicated
  `worktrees/leaf_refs.py` ownership for qualified leaf-ref validation, moved start leaf-ref handling out
  of `start.py`, normalized terminal catalog writes/spawn provenance to canonical qualified ids, and
  expanded terminal response models for leaf-ref refusals. Verification metadata pinned until closeout
  stamps the 260707-HFX-L4 commit.
- 2026-07-07T23:20+02:00 — 260707-HFX-L3 route impact (delivery integrity): the dispatch/paste
  narration upgrades from "echo-confirmed" to CAPTURE-VERIFIED — `contextDelivered` flows only from
  a pane capture proving the paste landed (one origin baseline per delivery over a history-inclusive
  window, strongest-first probe ladder incl. the payload-specific codex chip; a landed paste is never
  re-sent), failures ship the pane capture as evidence (spawn `deliveryCapture`, inbox capture tail,
  endpoint capture on delivery/submit failure), and Escape is refused at the paster (the SF-1/F-V
  blind-seat + 7-paste-stacking class is dead at this seam).
- 2026-07-07T19:30+02:00 — 260707-HFX-L2 route impact (provider index lifecycle): a HEAD
  difference is a state to catch up from, not a teardown — `providers/cgc/seed.py` seeds through
  relatable divergence (refusing only unrelatable heads) and `providers/provider_setup.py` adds
  the post-watcher diff-scoped catch-up stage (touch ≤ `delta_max_files`; above: `staleIndex`
  served + explicit `cgc refresh`), flips `cgc_refresh_fallback` off by default, and records
  index-state rows into `providers/metrics.py`'s log (`ar-provider-index-state/v1`);
  `worktrees/modules/start.py`'s mtime sync leaves divergent-content memory files fresh so
  grepai re-embeds exactly the delta. NEW suite `mcp/tests/test_provider_index_lifecycle.py`
  pins the cycle. Verification metadata pinned until closeout stamps the HFX-L2 commit.
- 2026-07-07T18:40+02:00 — No route impact: 260703-L18 (review fix batch) hardens
  `kernel/agentic_settings.py` (finding 6: a `null` at a known `orchestration.*` family key refuses
  loudly in either layer; finding 4: `effortSessionCommand` templates are validated post-merge) and
  adds regression tests across the mcp suites; no mcp route surface or module split changed (detail in
  the file sidecars).
- 2026-07-07T17:40+02:00 — 260707-HFX-L1 review fixes: the setup lock moved HOST-scoped
  (`fleet_setup_lock_path()` in the system temp dir — B1: `runtime_install` prunes `providers/`;
  B2: benchmark workspace roots must serialize on the same host lock); the benchmark filter's
  `None` default is fail-closed with an env escape (B4); `mcp_registration.py` gained the
  stale-registration sweep opened by both service entry points (B3); query funnels gate on their
  SPECIFIC provider; `docker stats` is fed only running names. Detail in the file sidecars.
  Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:50+02:00 — 260707-HFX-L1 (provider containment) route impact: the on-disk
  authority's `providers` map is now the LIVE launch authority (`mcp/config.py`:
  `ProviderAuthority`/`reload_provider_authority`/`require_provider_launch_authority`,
  fail-closed) consumed by the provider/worktree/benchmark controllers, the runtime-install
  rebind, and worktree provider setup; provider setup is serialized fleet-wide
  (`providers/provider_setup.py` `.setup.lock`, R2); NEW `providers/metrics.py` (R4) is the
  central containment metrics store/sampler, fed by the serving daemon's 30s loop and attached
  to `provider_status`; NEW suite `mcp/tests/test_provider_containment.py` pins the layer.
  Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-07-07T16:20+02:00 — No route impact: 260703-L17 is frontend-only — the only mcp-side change is the generated `package_data/dashboard` mirror advancing with the rebuilt dashboard dist (sync-dashboard); no mcp source or behavior changed.
- 2026-07-07T10:55+02:00 — No route impact: L15's mcp-side changes live in the serving/observer sub-routes (stable-form deltas, build info, tokenSeries decimation) — the mcp package route model is unchanged; details in the sub-route overviews and file sidecars.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application) route impact: the L13 knob chain is
  now APPLIED at the harness boundary. `kernel/agentic_settings.py` gained the free-form role-knob
  fields, `orchestration.rolesPerLevel`, and the `orchestration.harnesses` effective-registry
  family; `serving/harnesses.py` carries the per-harness knob→flag mapping (two-vehicle claude
  effort vocabulary incl. session-level `ultracode`) + dispatch refusal helpers;
  `serving/terminal_opener.py` applies env-riding knobs onto the argv and records free-form + level
  provenance (`serving/terminal_catalog.py` columns); `mcp/tools/terminal.py` + `mcp/server.py`
  grew the `launch_args`/`prompt_keywords`/`session_commands`/`level` parameters with pre-spawn
  `effort-invalid`/`model-invalid`/`level-invalid` refusals (`models/terminal.py`);
  `serving/app.py` resolves the dashboard surface against the effective global registry;
  `mcp/config.py` message-only. Suites extended unmodified-existing: `test_agentic_settings.py`,
  `test_harnesses.py`, `test_terminal_opener.py`, `test_spawn_agent_session.py`. New manual
  `docs/reference/harnesses.md`; `docs/reference/settings-json.md` documents the three-layer knob
  model. Verification metadata pinned until closeout stamps the L16 commit.
- 2026-07-07T06:10+02:00 — No route impact: PR #100 review fixes (merge `e358c4a`, landing the
  260703_agent-orchestration series) added an empty-list refusal to `kernel/agentic_settings.py`'s
  free-form knob parsing and a memory-source-branch guard to `worktrees/modules/start.py`'s
  reconciliation, with matching tests. Package surface and route model unchanged (detail in the
  file sidecars). Post-merge onboarding refresh, developer-approved.

- 2026-07-07T05:44+02:00 — 260703-L15 attestation: reviewed this overview against the L15 test
  changes — `tests/test_serving.py` gained the change-gate delta cases + `StateEtagTests` +
  `BuildInfoTests`, and `tests/test_observer_projection.py` the token-series decimation cases;
  the tests route model as described still holds (details in the two test sidecars).
  Verification metadata pinned until closeout stamps the L15 commit.
- 2026-07-06T23:59:58+02:00 — No route impact: L14's mcp-package changes live in the tools/controllers/models/serving sub-routes (orchestrates field, spawnRole seam) — the mcp package route model this overview describes is unchanged; details in the sub-route overviews and file sidecars.

- 2026-07-06T23:59:48+02:00 — 260703-L14 (visual hierarchy + chat grouping) test-route impact: five suites extended — `test_task_document.py` (orchestrates schema/render/set_field), `test_observer_projection.py` (TaskDocNode.orchestrates exposure), `test_terminal_catalog.py` (spawnRole round-trip), `test_terminal_opener.py` (AR_SPAWN_ROLE recording + write-once preservation), `test_spawn_agent_session.py` (spawnRole in the payload). Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-06T23:00+02:00 — 260703-L13 route impact (settings unification): NEW kernel module
  `kernel/agentic_settings.py` (the two-layer agentic settings loader + typed models + the
  install seed) with its suite `mcp/tests/test_agentic_settings.py`; `mcp/config.py` re-homes
  gateDelegation to the global file (boot-snapshot, warned legacy fallback, authority-file
  loops/roles/concurrency now fail loud) and drops the dead `memorySettingsIncludes`
  plumbing; `mcp/tools/terminal.py` + `mcp/server.py` make `spawn_agent_session.harness`
  optional with settings-driven resolution; `install/runtime.py` seeds the global file
  copy-if-missing; the provider lifecycle readers lose the implicit coordinator-settings
  fallback (GQ3 — see the providers/lifecycle route overview); synced c-13 (new Stage 2
  interview) and l-01 (knob home fixed) skill mirrors ride along. Verification metadata
  pinned until closeout stamps the L13 commit.
- 2026-07-06T17:40+02:00 — 260703-L12 round 2 route impact (doctrine deltas inside already-covered synced skills): OM-1 re-cited to the verifiable record and OM-3/RV-2/RV-3 re-tiered to candidates in the two criteria catalogs; verdict.md gains Rule 6 + the Criteria Catalog Results section + the Loop-Review Adaptation; manager/SKILL direct-tier glosses pinned (worker implements, manager never builds); reviewer opening made count-honest; the orchestrator Hand-Off Protocol and the c-09 Integration section carry the orchestrated-run standing-approval carve-out; strategist duty 6 aligned with its Tool Surface. All via sync-skills (9 targets); no new files, no route-model change. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T15:40+02:00 — 260703-L12 route impact (three-party loops): the synced `package_data/runtime/skills/l-01-agent-lifecycles/` tree gains 7 files (roles/strategist.md, templates/orchestration-task.md, criteria/{code-seam,doctrine,onboarding-memory,report-verification,plan-review}.md) and rewrites SKILL.md (loop doctrine home, six-role registry, 10-template + criteria companions) plus the four woven role files, all via `scripts/sync-skills.py` (9 targets); in mcp source the controlplane role vocabularies gain `strategist` (see the controlplane route overview and the two file sidecars) with a new test in `test_orchestration_comms.py`. No MCP tool signature or route model changed. Verification metadata pinned until closeout stamps the L12 commit.
- 2026-07-06T13:40+02:00 — 260703-L10 round 2 route impact (L10R-2, small): the `read_ar_files` docstring in `mcp/server.py` and the synced coordinator-template / `c-04` mirrors under `package_data/runtime/` now say "build decision" instead of the pre-convergence "build/job decision" (docstring/prose only — no tool signature, payload, or schema change; wrapper re-run green). Detail lives in the `server.py` and template/skill sidecars. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T12:10+02:00 — 260703-L10 route impact (generated mirrors only): `sync-runtime.py` re-synced `package_data/runtime/agents-md-files/` after the root templates' one-vocabulary sweep — the coordinator template's Start Here became Route By Role (unified `l-01-agent-lifecycles` skill, orchestrator plan gate, reframe-research routing bullet) and the skills template's Reference Style example cites the `l-01-agent-lifecycles` skill. No MCP tool, controller, or schema changed; detail lives in the two template sidecars. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-06T10:50+02:00 — No route impact: L11's mcp-side changes are test-layer only (observer projection test updates, the new mcp/tests/test_sim_fixture_builder.py regression suite, and build_rich_sim.py's materialize_worktrees fixture fix) — the mcp package route model this overview describes is unchanged; details live in the file sidecars.

- 2026-07-06T03:10+02:00 — No route impact: route model unchanged — 260703-L9 added a read-only
  coordination-notes API (`serving/notes.py`: `GET /api/notes/{list,read}` confined to
  `tasks/<repo>/<master>/notes/`) registered in `serving/app.py`, plus its API-layer suite
  `mcp/tests/test_serving_notes.py`, and the regenerated `package_data/dashboard/` bundle
  (+ fingerprint) for the task reader's notes view. These are serving-layer additions documented
  in the `serving/` route overview and the file sidecars; the mcp-package overview's subsystem
  narrative is unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-05T19:55+02:00 — No route impact: route model unchanged — 260703-L8 cycle 7 is the adversarial-review-4 remediation inside existing routes (wait=false enclosure requirement at mcp/tools + the server docstring, integrate dry-run guard reporting + the unmatched-gate warning at worktrees/modules, doctrine sentences inside the lifecycle/c-09 skill trees). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T19:10+02:00 — No route impact: route model unchanged — 260703-L8 cycle 6 hardens seam internals inside existing routes (integrate guard re-addressing at worktrees/modules, all_current at controlplane, wait=false seam restriction + ambient gate_list at mcp/tools, integrate policy pass-through at controllers) plus doctrine/template updates inside the lifecycle skill tree. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T18:24+02:00 — No route impact: route model unchanged — 260703-L8 cycle 5 lands the seam channel (gates wait/decide semantics documented at mcp/tools; store.find at controlplane; the integrate consumer at worktrees/modules) plus doctrine/template updates inside the lifecycle skill tree and a next_step summary wording fix. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:32+02:00 — No route impact: route model unchanged — 260703-L8 cycle 4 lands the seam-ruling remediation (reviewer.md rename + manager-brief.md inside the lifecycle skill tree; config wires the at-seams flag through parse_gate_delegation; next_step rundown re-worded; four skill mirrors touched). Tool signatures unchanged; the new gate kind is documented at the controlplane route. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T04:40+02:00 — No route impact: 260703-L8 de-harnessing pass: the two .claude-code.md runtime-mirror overlays are deleted and their sub-agent doctrine folded into the portable orchestrator/worker files as capability-conditional sections; SKILL resolution drops the variant layer. Markdown doctrine only; file cards for the two overlays retire with their sources; no mcp source or route model change.

- 2026-07-05T04:16+02:00 — No route impact: 260703-L8 reopened pass restructures four runtime-mirror doctrine files inside skills/l-01-agent-lifecycles (orchestrator = event loop + three jobs; designer = the hat; SKILL registry/router wording; manager flat-run + reopen rule) — markdown doctrine only, no mcp source, tool signature, or route model change.

- 2026-07-05T01:32+02:00 — No route impact: route model unchanged — 260703-L9 lifecycle convergence merges the two runtime lifecycle skill trees into `skills/l-01-agent-lifecycles/` (SKILL.md = router + minimal frame; `roles/` from `jobs/`; `lenses.md` from `job-variants.md`; templates gain `worker-brief.md` + the relocated `deep-research-report.md`); file cards moved/renamed accordingly and four c/w skill mirrors carry one-line reference updates. The mcp source deltas are name/path/comment-level only (orchestration_artifacts template root, next_step rundown wording, abandon/reducer comments); tool signatures and route behavior unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-04T23:43+02:00 — No route impact: L8 fixes `serving/changeset.py` master net diff tip resolution inside the already-documented change-set serving route; no MCP tool signature, response shape, package route model, or higher-level subsystem boundary changed. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-04T13:16+02:00 — No route impact: 260703-L6 sharpened the synced
  `l-02-agent-orchestration` runtime skill docs/templates only — adversarial reviewer seam-specific
  rubrics, verdict variants, `notes/reports/` artifact placement, and `reviewer-verdict` gate evidence
  refs. No MCP Python source, tool signature, response schema, or package route behavior changed.
  Verification metadata pinned until closeout stamps the L6 commit.
- 2026-07-04T13:03+02:00 — 260703-L5 route model update: the synced
  `l-02-agent-orchestration` runtime skill mirror now carries the full super integration branch
  topology (super from main, masters from super, leaves from masters), orchestrator master-to-super
  worktree integration, C-11 memory carry-over at every edge, ledger mapping, final super-to-main PR +
  main-memory carry-over + push, and the 260630-derived master finalize/archive plus parallel-master
  reconcile follow-ups as sequenced manual backlog. Verification metadata pinned until closeout stamps
  the L5 commit.
- 2026-07-04T12:32+02:00 — 260703-L4 route impact: the MCP package now parses
  opt-in `orchestration.gateDelegation`, exposes the gate policy/controlplane
  schema, enforces policy-valid delegated closeout approvals server-side, and
  projects gate evidence refs. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-04T12:31+02:00 - L3 route impact: MCP now includes generalized
  agent-to-agent inbox metadata, hosted push delivery, orchestration nudge
  helpers, and dashboard-visible delivery projection. Verification metadata
  pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — agent-orchestration L2 route impact: added the public `spawn_agent_session`
  MCP tool (agent-facing session dispatch) — it changes the mcp tool/model surface (`mcp/tools/terminal.py`
  + `models/terminal.py` + `base.py`/facade/`server.py`/`tool_registry.py`) and extends the `serving`
  subsystem with the shared `terminal_opener` + `terminal_paste` modules, the `tmux -e` env seam, the
  spawned-by catalog columns, and a `POST /api/terminal/{session}/paste` endpoint. Composition-only over
  existing serving primitives (no parallel spawn path). Updated the Purpose tool-surface note and the
  `agents_remember.serving` route-model bullet. Verification metadata pinned until closeout stamps the L2
  commit. (Distinct from the 260703-L2 daemon-supervision entry below.)
- 2026-07-04T11:00+02:00 — No route impact: route model unchanged — orchestration 260703-L1 adds the new `l-02-agent-orchestration` skill tree (14 files: `SKILL.md` = the orchestration frame, five `jobs/<role>.md` job files + two `jobs/<role>.claude-code.md` per-harness variants, six `templates/` report shapes) under `package_data/runtime/skills/`, sync-propagated via `scripts/sync-skills.py`. Registered 14 new file cards in this route's `coveredFiles`, bumped `coverageCounts` (sourceFilesInScope 499→513, fileSidecars 193→207). Skills are model-interpreted markdown, not mcp Python; no mcp source, tool signature, or route behavior changed. Verification metadata on the new file cards pinned until closeout stamps the L1 commit.
- 2026-07-04T10:15+02:00 — No route impact: orchestration 260703-L0 resynced the generated shipped dashboard bundle (mcp/src/agents_remember/package_data/dashboard, a build artifact excluded from memory scope) plus dashboard.fingerprint via scripts/sync-dashboard.py after dashboard-source changes; no mcp Python source, tool, or route behavior changed. Reviewed, overview body accurate as-is.
- 2026-07-03T12:59+02:00 — No route impact: 260703 L4 release bump only (pyproject version +
  SERVER_VERSION fallback to 3.0.0rc2); no mcp behavior or structure change.
- 2026-07-03T12:58+02:00 — No route impact: 260703 L3 rewrote `mcp/README.md`'s Install And Run
  (the PyPI page gains the uv-tool + dashboard + daemon install story; detail in the
  `mcp/README.md` sidecar). Documentation only — the mcp package route model, structure, and
  behavior are unchanged.
- 2026-07-03T12:57+02:00 — 260703 L2 route impact: `serving/` gains `daemon.py` (dashboard daemon
  supervision), the CLI gains `--daemon`/`--status`/`--stop`/`--no-access-log` with settings-default
  `--port`, `mcp/config.py` parses the fail-loud `dashboard` settings object (autoStart, port), and
  `mcp/server.py` `main()` gains the threaded `maybe_autostart_dashboard` boot hook. Covered by
  `mcp/tests/test_dashboard_daemon.py` + new `test_config.py` cases. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-07-03T12:55+02:00 — 260703 L1 route impact: the umbrella CLI under `cli/` gains
  `cli/discovery.py` — trusted-settings auto-discovery making `--config` optional on
  `agents-remember dashboard` (upward walk, convention-then-registration, nearest wins, semantic
  usability probe vs the tracked placeholder template) — covered by
  `mcp/tests/test_cli_discovery.py`. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-07-03T12:50+02:00 — No route impact: L15 push-gate fixups (type narrowing + test import hygiene only; the pre-push quality gate now exits 0 across the tree).
- 2026-07-03T11:20+02:00 — No route impact: L14 release bump only (pyproject version + SERVER_VERSION fallback); no mcp behavior or structure change.
- 2026-07-03T02:58+02:00 — No route impact: L13 reopen drill second cycle (marker comment extension only).
- 2026-07-03T02:40+02:00 — No route impact: L13 reopen drill: a marker comment in mcp/tests/conftest.py only; no mcp behavior or structure change.
- 2026-07-03T01:55+02:00 — L12 route impact: provider compose templates gain memory caps; CGC watch hygiene fixed (enriched .cgcignore reaches the watch context, committed bundle excluded per-repo, fired debounce timers popped via a maintained patch, image revision ar2).
- 2026-07-03T00:35+02:00 — L11 route impact: task_reopen tool added (tasks/reopen.py + leaf_doc.py, task_doc-side controller/payload/model); worktree start honors cleanup=reopened and restamps leaf-doc lifecycles; the reducer projects abandon terminality from contracts.
- 2026-07-02T21:45+02:00 — No route impact: the L10 binding repair is a one-line-scale join fix inside
  `observer/snapshots.py` (described in the observer route overview) plus its
  `mcp/tests/test_observer_projection.py` regression; no MCP tool surface or subsystem narrative
  changed at this granularity. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-02T20:55+02:00 — No route impact: the L8-r1 correction (pill-click-triggered direct leaf
  paste instead of auto-paste-on-selection) is a dashboard frontend change; the only `mcp/`-route
  effect is the regenerated `package_data/dashboard/` bundle + `dashboard.fingerprint`. Verification
  metadata pinned until closeout stamps the L8-r1 commit.
- 2026-07-02T20:15+02:00 — No route impact: operations-integration L8 is a dashboard frontend change
  (direct leaf-chat highlight paste + obsolete response-UI cleanup); the only `mcp/`-route effect is the
  regenerated `package_data/dashboard/` bundle + `dashboard.fingerprint`. No MCP package source, tool
  surface, or subsystem narrative changed. Verification metadata pinned until closeout stamps the L8
  commit.
- 2026-07-02T18:35+02:00 — No route impact: operations-integration L7 repaired the `cgc_dependencies`
  native subcommand (`analyze deps`) inside `controllers/provider_tools.py`, refreshed the packaged CGC
  guidance table, and locked the argv contract in `mcp/tests/test_tools.py`. No MCP tool surface or
  subsystem narrative changed at this granularity. Verification metadata pinned until closeout stamps
  the L7 commit.
- 2026-07-02T17:25+02:00 — No route impact: the reopened-L6 copy-mode escape stays inside
  `serving/terminal.py` (typing after wheel scrolling cancels tmux copy-mode; described in the serving
  route overview) and its `mcp/tests/test_terminal.py` coverage. No MCP tool surface or subsystem
  narrative changed at this granularity. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-07-02T17:04+02:00 — L9 route impact: added a package-level agent-facing terminal reassignment tool
  (`attach_terminal_session_to_leaf`) and the shared serving helper used by both MCP and the dashboard
  route. This changes the public MCP tool/model surface and the dashboard terminal catalog subsystem.
  Verification metadata pinned until closeout stamps the L9 commit.
- 2026-07-02T16:35+02:00 — No route impact: the reopened-L6 wheel/paste fixes touch
  `serving/terminal.py` (the per-session tmux mouse `TmuxConfigurer` seam, described in the serving
  route overview), its `mcp/tests/test_terminal.py` coverage, and the regenerated
  `package_data/dashboard/` bundle + `dashboard.fingerprint`. No MCP tool surface or subsystem
  narrative changed at this granularity. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-07-02T15:03+02:00 — No route impact: the L6 alternate-buffer wheel follow-up rebuilt and
  re-synced the generated `package_data/dashboard/` bundle plus `dashboard.fingerprint` after the
  `Terminal` wheel routing change under `dashboard/src/`. The shipped bundle remains generated static
  package data served by the existing dashboard package path; no MCP package source behavior, tool
  surface, or subsystem narrative changed. Verification metadata pinned until closeout stamps the
  follow-up commit.
- 2026-07-02T14:15+02:00 — No route impact: L6 closeout rebuilt and re-synced the generated
  `package_data/dashboard/` bundle plus `dashboard.fingerprint` after the leaf-chat draft handoff and
  terminal scrollback frontend changes under `dashboard/src/`. The shipped bundle remains generated
  static package data served by the existing dashboard package path; no MCP package source behavior,
  tool surface, or subsystem narrative changed.
- 2026-07-01T01:43+02:00 — No route impact: L6 rebuilt and re-synced the generated
  `package_data/dashboard/` bundle plus `dashboard.fingerprint` after the right-rail chat context-handoff
  frontend changes under `dashboard/src/`. The shipped bundle remains generated static package data served
  by the existing dashboard package path; no MCP package source behavior, tool surface, or subsystem
  narrative changed. Verification metadata pinned until closeout stamps the L6 commit.
- 2026-06-30T00:00:00+02:00 — No route impact: L5 (Sidebar chat: leaf-keyed attachment) added the leaf→chat registry to
  the serving layer — `serving/app.py` gained the `leafKey` opener claim + `POST /api/terminal/{session}/attach-leaf`
  (`409 leaf-taken`, running-only) and `serving/terminal_catalog.py` gained `TerminalCatalogEntry.leaf_key`
  + `active_for_leaf`, and the generated `package_data/dashboard/` bundle (+ fingerprint) was
  rebuilt/re-synced for the sidebar-chat frontend (the rail River⇄Chat toggle + leaf attach). The serving
  change is documented in the `serving/` route overview + the `app.py`/`terminal_catalog.py` sidecars; the
  shipped bundle remains generated static package data; the mcp-package overview's subsystem narrative is
  unchanged. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-06-29T23:18+02:00 — No route impact: `worktrees/modules/start.py` now derives the recorded memory base from the source branch tip (not the repo HEAD); nothing at the mcp-package route level changes (detail in the start.py file sidecar; task 260629_post-landing-cleanup L3).
- 2026-06-29T23:00+02:00 — No route impact: operations-integration L4a — `serving/changeset.py` gained the
  doc-reader leaf change-set endpoints (`/api/changeset/{task,file-diff}` `leaf` + `mode` selector;
  committed/working views by leaf-id off the persisted contract), and the generated `package_data/dashboard/`
  bundle (+ fingerprint) was rebuilt/re-synced for the doc-reader change-set buttons + the diff-highlight
  rectangle. The serving change is documented in the `serving/` route overview + the `changeset.py` sidecar;
  the shipped bundle remains generated static package data; the mcp-package subsystem narrative is unchanged.
  Verification metadata pinned until closeout stamps the L4a commit.
- 2026-06-29T22:57+02:00 — No route impact: the `task_doc` MCP tool docstring now lists the `remove_subtask` op (server.py registration/forwarding only); nothing at the mcp-package route level changes (detail in the server.py / task_doc_tools.py file sidecars; task 260629_post-landing-cleanup L2).
- 2026-06-29T17:00+02:00 — No route impact: operations-integration L4 review follow-up — `serving/changeset.py` gained the master NET change-set (`master_changeset` net `base→tip` + `master_file_diff`, the `/api/changeset/file-diff` `master` param), and the generated `package_data/dashboard/` bundle (+ fingerprint) was rebuilt/re-synced for the master-inspection + code-view readability/scroll polish. The serving change is documented in the `serving/` route overview + the `changeset.py` sidecar; the shipped bundle remains generated static package data; the mcp-package overview's subsystem narrative is unchanged. Verification metadata pinned until closeout stamps the L4 follow-up commit.
- 2026-06-29T16:40+02:00 — No route impact: operations-integration L4 rebuilt and re-synced the generated `package_data/dashboard/` bundle (+ the sibling `package_data/dashboard.fingerprint`) with `scripts/sync-dashboard.py` after the Change-Set Viewer frontend source changes under the in-scope root `dashboard/src/` sub-project (new `@codemirror/merge` dep). The shipped bundle remains generated static package data served by the existing dashboard package path; no mcp-package source behavior or tool surface changed. Verification metadata pinned until closeout stamps the L4 code commit.
- 2026-06-29T15:30+02:00 — No route impact: operations-integration L3 added a read-only change-set API (`serving/changeset.py`: `GET /api/changeset/{task,file-diff,master}`) plus a shared `serving/scope.py` (scope resolution + error map extracted from `serving/files.py`) and a new `worktrees/modules/git.py` `changed_files_with_counts` primitive. These are serving-layer / worktrees-module additions documented in the `serving/` and `worktrees/modules/` route overviews and the file sidecars; the mcp-package overview's subsystem narrative is unchanged. Verification metadata pinned until closeout stamps the L3 code commit.
- 2026-06-29T09:06+02:00 — No route impact: operations-integration L2 rebuilt and re-synced the generated `package_data/dashboard/` bundle (+ the sibling `package_data/dashboard.fingerprint`) with `scripts/sync-dashboard.py` after the File Viewer frontend source changes under the in-scope root `dashboard/src/` sub-project. The shipped bundle remains generated static package data served by the existing dashboard package path; no mcp-package source behavior or tool surface changed. Verification metadata pinned until closeout stamps the L2 code commit.
- 2026-06-28T22:41+02:00 — No route impact: operations-integration L1 added a read-only dashboard files API (`serving/files.py`) plus a shared `kernel/sidecar_pairing.py` helper and its test. These are serving-layer / shared-kernel additions documented in the `serving/` route overview and the file sidecars; the mcp-package overview's subsystem narrative is unchanged. Verification metadata pinned until closeout stamps the L1 code commit.
- 2026-06-28T20:30+02:00 — No route impact: a `find_worktree_contract` archive-skip + docstring fix under `kernel/coordination_context/`; nothing at the mcp-package route level changes (detail in the contracts.py file sidecar; task 260628_post-landing-cleanup).
- 2026-06-28T16:17+02:00 — Task 35 route impact: `scripts/sync-dashboard.py --check` is now source-aware —
  `sync` fingerprints the dashboard build inputs (the `src` tree minus tests, plus the production configs)
  into a sibling `package_data/dashboard.fingerprint`, and `--check` re-verifies it, so the pre-commit gate
  flags a `dashboard/src` change shipped without a rebuild (not only the built-bundle digest), mirroring how
  the skill gate flags a changed skill. Covered by `test_sync_dashboard.py` `SourceFingerprintTests`.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T13:54+02:00 — Task 34 route impact: the package-level observer/serving summary now records
  **inactivity-keyed** raw Event River retention (superseding the post-termination grace-window pruning):
  `event_retention.py` prunes a fleeting/enclosure lifecycle log after >1h of no real (non-heartbeat)
  activity rather than on `lifecycle.ended`, `ambient.py`'s heartbeat ticker decays after ~10 min idle,
  and `/api/events` does one retained-backlog scan per connect, filters `lifecycle.heartbeat`, and
  streams a bounded chunked backlog. Detail lives in the observer and serving route overviews plus the
  `event_retention.py`, `ambient.py`, and `events.py` sidecars. Verification metadata pinned until
  closeout stamps the task-34 code commit.
- 2026-06-28T07:45+02:00 — Task 33 route impact: the observer projection now exposes an `activeWorktreeGroups`
  field (from `active_enclosure_worktree_groups`, shared with the Engine Room) that the dashboard Topology
  consumes for active-enclosure scoping. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T07:43+02:00 — Task 29 S7 route impact: the package summary now records actionable-drift
  provenance/dismissal, raw Event River `ready` hydration, and the no-frontend-count-cap boundary.
  Detail lives in the observer, serving, controlplane, memory-quality, and dashboard route overviews.
  Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T06:08+02:00 — Task 29 route impact: the package-level observer/serving summary now records
  lifecycle-aware raw Event River retention and active-enclosure projection admission. The raw
  `events.jsonl` substrate remains episodic rather than audit-grade: terminal lifecycle logs are pruned
  after the grace window, fresh raw SSE connections start from retained offsets, projection caches repo
  surfaces briefly, and worktree provider/runtime data is admitted only for active enclosure-backed
  worktree groups. Detail lives in the observer and serving route overviews plus the
  `event_retention.py`, `worktree_provider_admission.py`, `projection_store.py`, `snapshots.py`, and
  `events.py` sidecars. Verification metadata pinned until closeout stamps the task-29 code commit.
- 2026-06-28T03:33+02:00 — Task 32 route impact: the package-level observer summary now records
  physical retention for persisted drift snapshots — cleanup removes the exact code-worktree snapshot
  for a reclaimed contract and projection prunes valid deleted-worktree snapshots before reading
  analytics. Verification metadata pinned until closeout stamps the task-32 code commit.
- 2026-06-28T03:21+02:00 — Task 31 route impact: the package-level dashboard path now refreshes provider
  current-state before live projection ticks, inspects worktree provider containers for isolated stacks, and
  projects missing expected provider roles into Engine Room instead of leaving empty provider containers
  ambiguous. Detail lives in the `observer/`, `serving/`, `providers/`, and dashboard panel sidecars.
  Verification metadata pinned until closeout stamps the task-31 code commit.
- 2026-06-27T22:00+02:00 — Task 28 route impact (NOTIFY-AND-CONTINUE turn end): the
  `agents_remember.observer` next-step paragraph now records the new non-terminal
  `awaiting-developer` state + public `lifecycle_turn_end_notification(summary)` tool
  (notify + stop, no wait/inbox) as the **active** turn-end path, the `_tool_payload`
  auto-dismiss, the next-step hint **repoint** from `lifecycle_gate`, and the one-line
  reducer gate-open/blocked-gate dedup; the `agents_remember.controlplane` bullet now
  records that the `lifecycle_gate`/`operator_inbox_*` turn-end choreography is **parked**
  (kept and valid, un-hinted). Per-file detail lives in the `observer/`, `mcp/tools/`, and
  `models/` route overviews + the file sidecars. Verification metadata pinned until closeout
  stamps the code commit.
- 2026-06-27T21:20+02:00 — Task 30 route impact: the package-level worktree lifecycle
  summary now records the already-integrated re-closeout reset behavior in
  `worktrees/modules/closeout.py`: changed closeouts reopen integration for
  re-integration, while no-op re-closeouts keep completed integration markers.
  Detailed behavior lives in the `worktrees/modules` route overview and the
  closeout sidecar. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-27T20:16+02:00 — No route impact: the task-27 follow-up adds a gate-await
  branch to `mcp/tools/next_step.py` (a `blocked` lifecycle now hints
  `lifecycle_resume`, carrying the chain through the open gate). The next-step
  engine is already inventoried in this route's `agents_remember.observer` Route
  Model bullet and its architecture is unchanged (detail in the file sidecar).
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27 route impact: the `agents_remember.observer`
  Route Model bullet now records the lifecycle next-step hint engine
  (`mcp/tools/next_step.py`) — a `NextStep` hint folded from the projected
  lifecycle state and attached to every tool response at the `_tool_payload`
  choke point (one-time `lifecycle_start` `frontHalfRundown` front half, the
  linear half delegating to `guidance.lifecycle_guidance` with a
  `lifecycle_gate(kind=…)` gate overlay, and a terminal `lifecycle_end`
  loop-back), generalizing worktree-only guidance to the whole lifecycle spine.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T15:24+02:00 — Task 22 follow-up route impact: the package-level serving summary now records
  detached tmux session creation, independent per-browser WebSocket attaches, non-destructive browser
  disconnect, and sticky explicit termination for cataloged dashboard terminal sessions. Detailed
  behavior lives in the serving route overview and sidecars. Verification metadata pinned until closeout
  stamps the follow-up code commit.
- 2026-06-26T23:15+02:00 — Task 22 route impact: the dashboard serving route now persists terminal
  session metadata in `serving.terminal_catalog`, lists catalog rows, rehydrates live tmux sessions on
  WebSocket attach, marks stale rows exited, and terminates cataloged sessions on request. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-26T20:18+02:00 — Task 21 route impact: task-document writes now synchronize same-root master
  rows, and observer analytics expose `SeriesNode.seriesTokenTotal` for the dashboard master reader.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-26T19:40+02:00 — No route impact: task 20 reopened for Event River
  lifecycle-label fallback and only re-synced the generated
  `package_data/dashboard/` bundle under `mcp/` after frontend source changes
  in `dashboard/src/data` and `dashboard/src/panels`. The shipped bundle remains
  generated static package data served by the existing dashboard package path;
  no MCP tool surface, serving contract, or package route model changed.
  Verification metadata pinned until closeout stamps the reopened task-20 code
  commit.
- 2026-06-26T18:43+02:00 — Regression fix: package-level control-plane
  paragraph now records `lifecycle_gate` as blocking until a developer decision
  or gate-specific inbox response, with stale lifecycle-scoped inbox rows ignored
  by the public junction.
- 2026-06-26T18:23+02:00 — No route impact: task 20 rebuilt and re-synced the generated
  `package_data/dashboard/` bundle after Event River frontend source changes under `dashboard/src/panels/`.
  The shipped bundle remains generated static package data served by the existing dashboard package path;
  no MCP tool surface, serving contract, or package route model changed. Verification metadata pinned until
  closeout stamps the code commit.
- 2026-06-26T17:05+02:00 — Regression fix: package-level control-plane
  paragraph now records `lifecycle_gate` as create + block + bounded wait, so
  the public agent-facing junction is no longer described as wait-state
  initialization only.
- 2026-06-26T16:15+02:00 — Task 25 closeout verification: refreshed the package-level
  control-plane paragraph for the unified public `lifecycle_gate` registration and verified
  the `task_doc replace` summary against code commit `2017434`.
- 2026-06-26T15:33+02:00 — No route impact: task 25 preserves the source branch's
  `task_doc replace` operation; lifecycle-gate API consolidation is documented in the scoped
  control-plane, MCP-tool, model, and observer sidecars, so the package-level task-document summary
  remains the replacement-repair wording. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-25T14:02+02:00 — Task 24 reopened: MCP package overview records ambient-bound gate creation plus gate-id-only cancel cleanup for stale workspace-shaped gates.
- 2026-06-25T13:20+02:00 — Task 23/24: MCP package overview now records disposable gate/inbox interaction retention, agent-pickup projection, and the rebuilt dashboard bundle.
- 2026-06-25T09:55+02:00 — GrepAI provider lifecycle now documents and tests non-conflicting preferred auto host ports (`61432` PostgreSQL, `61434` Ollama) while retaining container service ports `5432`/`11434`.
- 2026-06-25T07:26+02:00 — Task 19 gate interaction polish: the MCP package now exposes
  `gate_response_wait`, keeps one open gate per lifecycle by expiring older gates, records targeted
  dashboard Yes/No decisions with rejection notes, preserves Chat as operator-inbox/message-only, and
  ships the rebuilt dashboard bundle. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-06-24T18:17+02:00 — No route impact: empty-state backdrop zoom-stability rebuilt and re-synced the
  generated `package_data/dashboard/` bundle after the frontend source and SC2 boomerang asset changes in
  `dashboard/src` / `dashboard/public/assets`. The shipped bundle remains generated output served by the
  existing MCP dashboard package path; no MCP tool surface, serving contract, or package route model changed.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T16:39+02:00 — Task 17 package route correction: refreshed the task-document summary so
  observer projection is active-doc-first with optional lifecycle context, rather than requiring a
  lifecycle key before Operations can show a task. Detail lives in the observer route overview and
  sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T13:59+02:00 — No route impact: the Task 17 progress-count follow-up only re-synced the
  generated dashboard bundle under `src/agents_remember/package_data/dashboard/` after a
  `dashboard/src/panels/DetailPanel.tsx` display fix; no MCP package service surface changed.
  Verification metadata pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:57+02:00 — No route impact: the Task 17 master-selection follow-up only re-synced the
  generated dashboard bundle under `src/agents_remember/package_data/dashboard/` after a
  `dashboard/src/panels/DetailPanel.tsx` fix; no MCP package service surface changed. Verification
  metadata pinned until closeout stamps the follow-up code commit.
- 2026-06-24T12:43+02:00 — No route impact: Task 18 rebuilt and re-synced the generated
  `package_data/dashboard/` bundle after the Operations task-title ellipsis fix in `dashboard/src`.
  The MCP package route model is unchanged; the synced assets remain generated output owned by
  `scripts/sync-dashboard.py` and checked by `mcp/tests/test_sync_dashboard.py`. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-06-24T12:21+02:00 — No route impact: Task 17 updates `mcp/tests/test_observer_projection.py`
  coverage for observer task/series `createdAt` and master objective projection within the existing
  observer/test route model; no new MCP service domain or package route was added. Verification
  metadata pinned until closeout stamps the code commit.
- 2026-06-24T08:59+02:00 — No route impact: observer task-document correction keeps
  `series-contract.md` as enclosure/process state only; lifecycle-readable task content comes from
  JSON-primary `ar-task-document/v1` docs. Detail lives in the `observer/` overview plus
  `snapshots.py`, `projection.py`, and `test_observer_projection.py` sidecars. The generated dashboard
  bundle under `package_data/dashboard/` was re-synced from `dashboard/dist`; no MCP tool surface
  changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-24T06:26+02:00 — Series-contract task resolver: refreshed the worktree lifecycle Route Model
  paragraph to mention `worktrees/task_resolver.py`, which centralizes task-name lookup, nested
  parent-task disambiguation, leaf enclosure contract paths, active archive exclusion, and completed
  root-task archival. Detail lives in the new `task_resolver.py` sidecar. Verification metadata pinned until
  closeout stamps the series-contract resolver code commit.
- 2026-06-24T00:16+02:00 — Task 14 cleanup correction: updated the worktree lifecycle Route Model paragraph to reflect the current child-edge cleanup contract. Cleanup still hard-refuses before carryover and proves task work branches against the contract source branch, but it no longer retires parent/source branches; those branches are finalized by their own lifecycle edge.
- 2026-06-23T23:04+02:00 — Dashboard task 14 adds the terminal `lifecycle_finalize_task` MCP operation. Refreshed the Hot Path Summary and Route Model for `worktrees/modules/finalize.py`: one branch-edge ancestry proof after landing, memory carryover check, cleanup verification, JSON-primary leaf + immediate parent-row reconciliation, no squash equivalence.
- 2026-06-23T22:31+02:00 — Task 12 S2 clarification: refined the observer summary to distinguish
  GrepAI process aggregation from addressable repo/project targets, so `targetRepos` can project as repo
  satellites without implying separate per-repo provider processes.
- 2026-06-23T22:09+02:00 — Task 12 S2 correction: refined the observer read-side summary after GrepAI
  target evidence was verified in MCP config/current-state flow. CGC watcher rows and GrepAI
  configured `targetRepos` now both project as repo-scoped workspace provider nodes; only providers
  without target evidence remain aggregate.
- 2026-06-23T21:58+02:00 — Task 12 S2 refreshed the observer read-side summary for repo-covered
  workspace provider projection: CGC per-repo watcher rows now become repo-scoped provider nodes,
  while unsupported provider coverage remains aggregate. Detail lives in the `observer/` route
  overview plus the `provider_nodes.py`, `snapshots.py`, `projection.py`, and
  `test_observer_projection.py` sidecars.
- 2026-06-23T16:17+02:00 — Task 13 cleanup correctness: refreshed the `agents_remember.observer` / worktree lifecycle Route Model paragraph for the cleanup source-branch proof and dry-run directory preview fix; detailed behavior lives in the `worktrees/modules` route overview and `cleanup.py` sidecar.
- 2026-06-23T16:02+02:00 — No route impact: task 12 S1 refreshed the shipped dashboard bundle under
  `src/agents_remember/package_data/dashboard/` with `scripts/sync-dashboard.py` after changing the
  topology frontend source. The MCP package route model and Python serving/control/tool behavior are
  unchanged; this is generated static frontend package data only.
- 2026-06-23T15:05+02:00 — Task 10 dashboard fallback: added the serving-layer `POST /api/operator-inbox` bridge to the package overview, tying the dashboard no-hosted-session path to the external-chat operator inbox. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T14:33+02:00 — No route impact: Task 11 refreshed the shipped dashboard bundle under
  `src/agents_remember/package_data/dashboard/` with `scripts/sync-dashboard.py` after changing the
  browser cockpit. The MCP package route model and Python serving/control/tool behavior are unchanged;
  this is generated static frontend package data only.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: documented the external-chat operator inbox as a control-plane sibling to gates and the three new `operator_inbox_*` tools. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption): refreshed the `agents_remember.controlplane` Route Model bullet for the `GateKind` extension to the full l-01 gate spine (`plan-approval` / `worktree-intent` / `push-approval` added; `closeout-approval` IS the commit gate, tracked by the `gate_create` docstring), and the `agents_remember.observer` bullet for the `worktrees/modules/guidance.py` visibility fix — `lifecycle_guidance` no longer reads a `commit-approval-pending` gate off `git status`, so a dirty worktree projects its honest lifecycle-position phase (closeout-completed → `integration-pending`). The mcp package route model this overview describes is unchanged; per-route detail lives in the `controlplane/` + `worktrees/modules/` route overviews + the `records.py` / `server.py` / `guidance.py` sidecars. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-23T01:40+02:00 — No route impact: slice 07b v1 carries the read's `repoId` on the `read.packet` — `observer/ambient.emit_read_packet` now takes `repo_id` and emits `data.repoId`, `controllers/read_files.py` passes `repo.repo_id`, and `mcp/tests/test_read_ar_files.py` asserts it (the dashboard `EventRiver` consumes it, out of this package). No MCP tool signature, controller surface, or schema changed; detail lives in the `controllers/` + `observer/` route overviews + file sidecars, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the slice-07b code commit.
- 2026-06-23T00:53+02:00 — No route impact: slice 07 S4+S5 is doctrine/docstring text only — the `read_ar_files` tool docstring (`mcp/server.py`) now states the research-phase-read role, the `controllers/read_files.py` + `observer/served_store.py` docstrings retarget the compact-reset producer to the post-3.0 agentic-control-plane (consumer + `refresh` kept as defensive scaffolding), and the synced runtime mirrors under `package_data/runtime/` (coordinator `AGENTS.md`, `c-04`/`l-01` `SKILL.md`) carry the research-phase-read doctrine. No MCP tool signature, controller surface, or schema changed; detail lives in the `controllers/` + `observer/` route overviews + file sidecars, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the slice-07 code commit.
- 2026-06-21T06:40+02:00 — Slice 05m (carryover-before-cleanup): refreshed the `agents_remember.observer` Route Model bullet for the carryover-before-cleanup lifecycle correctness landed in `worktrees/modules/` (`guidance.carryover_done` reads the official ledger; the new `carryover-pending` phase routes `memory_carryover_apply` before `cleanup-pending`; `cleanup_result` hard-refuses cleanup until the carry runs and then retires the work + PR'd source branches) and the observer reducer that now follows it (`_GUIDANCE_PHASE` projects `carryover-pending`; the engine-room node carries the display-only `carryoverDoneAt`). The mcp-package detail lives in the `worktrees/modules/` + `observer/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 05m code commit.
- 2026-06-21T05:30+02:00 — Slice 05l Part 2 (landing-arc probe hardening): refreshed the `agents_remember.observer` Route Model bullet for the hardened `worktrees/modules/landing.py` probe — the protected target `origin/<base>` is now probed directly via `ls-remote` (visible across the whole landing window before any PR and independent of `gh`) and the PR ref carries gh's open/merge timestamp on the additive `LandingRefNode.at`, so the dashboard can follow a REAL remote landing; carryover/cleanup lifecycle correctness is a separate upcoming slice (05m). The mcp-package detail lives in the `worktrees/modules/` + `observer/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 05l-P2 code commit.
- 2026-06-21T04:10+02:00 — Slice 05l Part 1 (backend teardown visibility): the `agents_remember.observer` reducer now projects the `abandoned` worktree phase (sourced from `worktrees/modules/guidance.py`'s new `cleanup == "abandoned"` branch) and **drops disposed** (cleaned-up/abandoned) enclosures from the Engine Room `Analytics.engineProcesses` so the frontend (05k) animates the teardown; refreshed the observer Route Model bullet. The mcp-package detail lives in the `observer/` + `worktrees/modules/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 05l-P1 code commit.
- 2026-06-21T02:44+02:00 — No route impact: slice 6g changes are observer-local — `observer/read_task_documents` contract-pairs masters + resolves cross-master links, and `observer/projection.TaskDocNode` gains `subTasks`/`sections`/`masterLifecycleId` (detail in `src/agents_remember/observer/overview.md`). The `mcp/` package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6g code commit.
- 2026-06-19T20:30+02:00 — Task 6 slice 6f: `agents_remember.serving` gained `POST /api/terminal/{session}/image` (save a validated screenshot under the session cwd for path-injection, `python-multipart` dep) and a harness-scoped Ctrl-Z strip on the terminal host. Refreshed the serving Route Model bullet; per-file detail lives in `serving/overview.md` + the `app.py`/`terminal.py` sidecars. Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-19T15:50+02:00 — No route impact: the 5h H4 cleanup teardown + landing-source flag fix only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The frontend change lives in the in-scope root `dashboard/src/`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T15:00+02:00 — No route impact: the 5h H3 remote/PR strip readability + connector pass only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The frontend change lives in the in-scope root `dashboard/src/`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T14:05+02:00 — No route impact: task 6 slice 6e-4 modified `serving/terminal.py` (controlling-tty via `os.login_tty` + a seeded winsize so tmux honors resize) and `mcp/tests/test_terminal.py` (added `test_spawn_seeds_default_winsize`); both are internal to the already-documented `serving/` sub-route (detail in `serving/overview.md` + the `terminal.py` / `test_terminal.py` sidecars). The `mcp/` package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 6e-4 code commit.
- 2026-06-19T13:57+02:00 — No route impact: slice 5h H3 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope; synced from `dashboard/dist`); no mcp-package source behavior changed. The H3 frontend change (engine-room remote/PR landing strip) lives in the in-scope root `dashboard/src/` with its own route + file sidecars. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T07:23+02:00 — No route impact: slice 3c R5 adds a `dry_run` flag to the `task_doc` tool (act-by-default false; true returns `rendered`/`diff`/`wouldLose` without writing) — an optional param on an existing tool, no new tool surface; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:39+02:00 — No route impact: the engine-room crash fix rebuilt the shipped dashboard bundle under `package_data/dashboard/` (synced from `dashboard/dist`); it is a generated artifact and no mcp package route surface changed. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T06:03+02:00 — No route impact: slice 3c reopened (R4, leaf-doc fidelity) adds leaf schema fields (`statusNote`/`headerNotes`/`HeaderNote`) + freeform leaf `sections` in the `tasks/` route, a `_MUTABLE_FIELDS`/`set_section` controller tweak, and the synced w-02 skill guidance under `package_data/runtime/skills/`; no MCP tool surface changed (the `task_doc` signature is unchanged) and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T05:15+02:00 — No route impact: slice 3c reopened (R3, deferred-examples honesty) adds an optional `codeExamplesNote` schema field + a renderer branch in the `tasks/` route and the synced w-02 skill guidance under `package_data/runtime/skills/`; no MCP tool surface changed (the `task_doc` tool signature is unchanged) and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T04:18+02:00 — No route impact: slice 3c reopened (R2, heading-vs-outcome) adds an optional `Step.outcome` + a renderer tweak in the `tasks/` route (the checkbox carries the distinct outcome; a bare step is heading-only); detail in the `tasks/` overview + the `document.py`/`render.py` sidecars. The mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-19T03:17+02:00 — No route impact: slice 3c reopened (R1, masters observable) adds a folder-keyed series/master projection inside the `observer/` route (`read_series_documents` + `SeriesNode`/`Analytics.series`) plus the `series_total`/`series_done` helpers in the `tasks/` route; both carry their own sub-route overviews and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T21:27+02:00 — Task 6 slice 6e-2b: `agents_remember.serving` gained `harnesses.py` (the curated harness launch registry — Claude Code/Codex/Pi.dev + `shutil.which` detection) + `app.py`'s `GET /api/harnesses` and a `kind="harness"` opener branch. Refreshed the serving Route Model bullet (opener now spawns a shell *or* a detected harness). Per-file detail lives in the `serving/` route. Verification metadata pinned until closeout stamps the 6e-2b code commit.
- 2026-06-18T21:25+02:00 — No route impact: slice 5h Tier 2 enriches the `observer/` ledger window with per-side commit message + date via a best-effort batched `git log` (detail in the `observer/` overview) and expands `mcp/tests/test_observer_projection.py` under this route with `LedgerCommitMetaTests` (real git repos); the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T18:00+02:00 — No route impact: slice 5h's ledger popover extends the `observer/` ledger surface (additive `LedgerNode.rows` / `EngineProcessNode.ledgerRows`; detail in the `observer/` overview) and expands `mcp/tests/test_observer_projection.py` under this route with the windowing tests; the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-18T17:40+02:00 — Task 6 slice 6e-2a: `agents_remember.serving` `app.py` gained the `POST /api/terminal/{session}` **opener** (the dashboard spawns + owns a shell session at `config.workspace_root` via the pure `resolve_terminal_launch` → `host.open`; server-resolved command). Refreshed the serving Route Model bullet. Harness kinds + per-harness buttons are 6e-2b. Verification metadata pinned until closeout stamps the 6e-2a code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: `agents_remember.serving` `app.py` gained the `@app.websocket("/api/terminal/{session}")` Mode B2 bridge (PTY ↔ WebSocket — binary out, JSON `stdin`/`resize` in, `{type:exit}` on child exit, attach-only + tmux-persistent) + the `terminal_host` `create_app` param; `pyproject.toml` added the `websockets` core dep (uvicorn's WS impl). Refreshed the serving Route Model bullet; per-file detail lives in the `serving/` route. The xterm.js visual is 6e. Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-18T15:40+02:00 — Task 6 slice 6d-1: `agents_remember.serving` gained the **Mode B2 terminal host** (`terminal.py` — a `TerminalHost` registry of tmux-wrapped stdlib-`pty` sessions, injectable spawn, fixed-argv/localhost posture) + `mcp/tests/test_terminal.py`. Refreshed the serving Route Model bullet; per-file detail lives in the `serving/` route. The WebSocket bridge + `websockets` dep are 6d-2, the xterm.js visual 6e. Verification metadata pinned until closeout stamps the 6d-1 code commit.
- 2026-06-18T14:05+02:00 — No route impact: task 6 slice 6c Part A is within the `agents_remember.observer` sub-route (gate projection — `read_gates` + `_attach_gates` / `_gate_attention` materialize a durable gate onto the lifecycle); the mcp package route model this overview describes is unchanged — detail lives in the `observer/` route overview + file sidecars (the `mcp/tests` test addition has no package-route impact). Verification metadata pinned until closeout stamps the 6c Part A code commit.
- 2026-06-18T12:10+02:00 — Task 6 slice 6b: the `agents_remember.controlplane` domain became **enforcing** — new `enforcement.py` (`evaluate_closeout_gate`) binds `worktree_closeout_apply` on a developer-approved gate, and `agents_remember.serving`'s POST plane records gate decisions (`gate_decide_for_lifecycle`). Refreshed the controlplane + serving Route Model bullets; per-file detail lives in those routes + the synced l-01/c-12-closeout skill sidecars under this package. Verification metadata pinned until closeout stamps the 6b code commit.
- 2026-06-18T08:51+02:00 — No route impact: slice 5h H1 adds the `worktrees/modules/landing.py` best-effort landing-arc probe (detail in the `worktrees/modules/` overview) and the `observer` `landing`/`integrationStrategy` projection fields (detail in the `observer/` overview); the new `mcp/tests/test_landing.py` + the expanded `test_observer_projection.py` under this route carry no mcp-package route-model impact. The mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 5h code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: new `agents_remember.controlplane` service domain (the gate control-plane substrate — `GateRecord` + `GateStore`) plus the four `gate_*` MCP tools registered through `server.py`/`mcp/tools`/`models` (47-tool surface). Added the controlplane Route Model bullet; per-file detail lives in the new `controlplane/` route and the `gates` sidecars. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-16T03:50+02:00 — No route impact: slice 5f S5 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S5 frontend change (lifecycle-phase header pulse) lives in the in-scope root `dashboard/src/`.
- 2026-06-16T03:40+02:00 — No route impact: slice 5f S4 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S4 frontend change (conduit power-up flow packets) lives in the in-scope root `dashboard/src/`.
- 2026-06-16T03:35+02:00 — No route impact: slice 5f S3 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S3 frontend changes (promotion morph + alarm-parity test) live in the in-scope root `dashboard/src/`.
- 2026-06-16T03:25+02:00 — No route impact: slice 5f S6 closed the §9 observability gaps in `observer/reducer.py` (the `_start_attention` attention source + `start_progress` threading) and `worktrees/modules/start.py` (happy-path start-progress emits); the mcp package route model this overview describes is unchanged — detail lives in the `observer/` + `worktrees/modules/` route overviews and the file sidecars.
- 2026-06-16T03:05+02:00 — No route impact: slice 5f S2 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S2 frontend changes (Engine Room birth motion + fleeting rendering) live in the in-scope root `dashboard/src/`.
- 2026-06-16T02:30+02:00 — No route impact: slice 5f S1 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S1 frontend change (full-bleed cockpit layout) lives in the in-scope root `dashboard/src/`.
- 2026-06-16T01:55+02:00 — No route impact: slice 5f S0 only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The S0 frontend changes live in the in-scope root `dashboard/src/` with their own route overviews + file sidecars.
- 2026-06-15T19:35+02:00 — No route impact: slice 5e's mcp-side changes (the observer `engineProcesses` surface + `worktrees/start_progress.py` §5.4) are captured in the `observer/` and `worktrees/modules/` route overviews + file sidecars; the mcp package route model this overview describes is unchanged.
- 2026-06-15T17:00+02:00 — No route impact: slice 5d only re-synced the generated dashboard bundle under `package_data/dashboard/` (excluded from memory scope); no mcp-package source behavior changed. The 5d frontend re-architecture (Panda + React Aria) lives in the now-in-scope root `dashboard/src/` with its own route overviews + file sidecars.
- 2026-06-14T23:30+02:00 — Slice 05 (5c): the `agents_remember.observer` read side now synthesizes paused persistent lifecycles from worktree contracts, reads per-worktree provider stacks (surface 4), and carries the full task content on `TaskDocNode`; `agents_remember.serving` `sim.py` materializes fixture structural surfaces and `events.py` single-encodes the raw SSE channel. Under `mcp/tests`, `test_observer_projection.py`/`test_serving.py` gained the matching cases plus a new `mcp/tests/fixtures/build_rich_sim.py` rich-sim generator (its own sidecar). Refreshed the observer Route Model bullet; the cockpit UI is frontend (out-of-scope root `dashboard/`). Verification metadata pinned until closeout stamps the 5c code commit.
- 2026-06-14T17:30+02:00 — Slice 05 (5b): the `agents_remember.observer` projection gained the server-computed **attention queue** (`AttentionItem` + the derived `Analytics.attentionQueue`, the pure `build_attention_queue` wired through `project_workspace`); refreshed the observer Route Model bullet. The expanded `mcp/tests/test_observer_projection.py` under this route carries no mcp-package route-model impact (detail in the file/route cards). The 5b cockpit panels are frontend, living in the out-of-scope root `dashboard/`. Verification metadata pinned until closeout stamps the 5b code commit.
- 2026-06-14T15:52+02:00 — Slice 05a: the package now ships the **real** dashboard cockpit bundle under `package_data/dashboard/` (the slice-04 placeholder is replaced by the Vite/React build, synced by `scripts/sync-dashboard.py`); added `mcp/tests/test_sync_dashboard.py` and wired `sync-dashboard.py --check` into both githooks + the CI workflow. The mcp package route model is otherwise unchanged (the cockpit React/TS sources live in the out-of-scope root `dashboard/`). Verification metadata pinned until closeout stamps the 5a code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4b: extended `agents_remember.serving` with the raw `event` SSE channel (`events.py` — byte-offset `Last-Event-ID` resume), sim-mode replay (`sim.py` — a replay clock + fixture feeder over the projector's `now`/`before_tick` seams), and the no-mutation `POST /api/actions/{action}` skeleton (`actions.py`); `app.py` gained `/api/events` + `/api/actions`, `cli/dashboard.py` the `--sim`/`--sim-speed` flags. Refreshed the serving Route Model bullet; per-file detail lives in the new + updated `serving/` sidecars. Verification metadata pinned until closeout stamps the 4b code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4a: new `agents_remember.serving` service domain (the dashboard serving spine — FastAPI app, shared projector, per-entity SSE deltas, static mount) with its own route overview, plus the umbrella `agents-remember` CLI (`cli/__main__.py` + `cli/dashboard.py`) and `fastapi`/`uvicorn` core deps. Added the serving Route Model bullet; per-file detail lives in the new `serving/` route + `cli/` sidecars. Verification metadata pinned until closeout stamps the 4a code commit.
- 2026-06-14T00:16+02:00 — No route impact: slice 3c commit 3 extends the `agents_remember.tasks` domain with `kind:"master"` (a `subTasks` series index + ordered `sections`) and the master `task_doc` ops (`set_subtask`/`set_section`); the per-route detail lives in the `tasks/`, `mcp/tools`, and controller overviews + the file sidecars, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 3c commit-3 code commit.
- 2026-06-13T23:10+02:00 — Slice 3c commit 2: the observer read side first added task-document projection (`read_task_documents` → `Analytics.taskDocuments`; later Task 17 made projection active-doc-first with optional lifecycle context), and the `w-02-light-task-workflow` skill under `package_data` adopted JSON-primary authoring (synced from canonical `skills/`). Updated the tasks Route Model bullet (the observer projects them, not "will project"). Verification metadata pinned until closeout stamps the 3c commit-2 code commit.
- 2026-06-13T22:34+02:00 — Slice 3c commit 1: new `agents_remember.tasks` service domain (the JSON-primary `ar-task-document/v1` schema + renderer + store) and the `task_doc` authoring tool registered through `server.py`/`mcp/tools`/`models` (43-tool surface). Added the tasks Route Model bullet; per-file detail lives in the new `tasks/` route and the `task_doc` sidecars. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T20:48+02:00 — Slice 3b: the `agents_remember.observer` projection read side gained the analytical surfaces (drift snapshot, sidecar staleness, setup, route coverage, tool reports, ledger) + the rollups; refreshed the observer Route Model bullet (no longer "analytical surfaces land in 3b"). The drift-producer snapshot write in `memory_quality/summary.py` and the expanded `mcp/tests/test_observer_projection.py` under this route carry no mcp-package route-model impact (detail lives in their file/route cards). Verification metadata pinned until closeout stamps the 3b code commit.
- 2026-06-13T19:30+02:00 — Slice 3a: the `agents_remember.observer` domain gained the projection **read side** (`reducer.py`, `projection.py`, `snapshots.py`, `projection_store.py`, plus the shared `paths.py`/`timeutil.py`); the observer Route Model bullet no longer says the read side "arrives in a later slice." Per-file detail lives in the `observer/` route. Verification metadata pinned until closeout stamps the 3a code commit.
- 2026-06-13T18:45+02:00 — No route impact: slice 2c extends the mcp-internal `observer` domain (resume + save gate: `save_gate.py`, ambient `promote`/`attach`) and forwards an `on_unsaved` argument through the lifecycle/worktree tools; the per-route detail lives in the `observer` and `mcp/tools` overviews, and the mcp package route model this overview describes is unchanged. Verification metadata pinned until closeout stamps the 2c code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: the `agents_remember.observer` domain gained the ambient lifecycle and the six `lifecycle_*` signal tools, and `server.py` + `mcp/tools/base.py` wired the `install_ambient` call plus the `_tool_payload` emission hook; updated the observer Route Model bullet. Per-file detail lives in the `observer/` and `mcp/tools/` routes. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-13T11:15+02:00 — New `agents_remember.observer` service domain (slice 2a of the 3.0 browser-dashboard series): the observable-lifecycle event substrate write side — `ar-observer-event/v1` envelope, local ULID mint, append-only per-lifecycle event store — with its own route overview under this package. Added it to the Route Model; per-file detail lives in the new `observer/` route. Later slices add the ambient lifecycle + signal tools and the projection read side.
- 2026-06-12T19:06+02:00 — No route impact: the issue #83 changes under this route are the worktree-manager facade re-exports, the test additions, the 2.9.1 version bump, and the synced c-12-closeout and l-01-session-job-lifecycle skill copies (issue #83 doctrine plus the two-turn gate protocol); the closeout worklist behavior itself is documented at the `mcp/src/agents_remember/worktrees/modules` route, and the package layout/routing this overview describes is unchanged.
- 2026-06-11T15:20+02:00 — No route impact: carryover gained the memory-only-doc and entity-catalog candidate kinds inside memory/carryover.py and the c-11 packaged skill doc; route structure and module responsibilities on this route are unchanged (detail lives in the per-file cards).
- 2026-06-11T14:07+02:00: No route impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-11T06:47+02:00 — No route impact: issue #62 removed the `direct_closeout_*` tool surface (server registrations, payload builders, controllers, models, CLI subcommand, tests) — closeout is worktree-only; the package structure this overview describes is unchanged (detail in the file sidecars and sub-route overviews).
- 2026-06-10T10:26+02:00 — No route impact: package version bumped to 2.8.0 (`pyproject.toml`, `SERVER_VERSION` fallback) for the GitHub #54 release; runtime skills (l-01/c-09/c-11) teach the new freshness checkpoints; route behavior unchanged.
- 2026-06-10T09:56+02:00 — Issue #54 sub-task D: new `worktree_sync` tool (mid-task atomic base-pair sync) and the fetch-free `worktree_status` freshness block; route detail lives in the `worktrees/modules` overview.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C: carryover apply reports `memory_main_advance`, fast-forwarding memory main to the official checkout tip after the carryover commits.
- 2026-06-10T09:30+02:00 — Issue #54 sub-task B: `worktree_start` gained the stale-base preflight (behind/diverged source branches block with `stale_base_choice` recoveries) and the memory source branch auto-template; route detail lives in the `worktrees/modules` overview.
- 2026-06-10T08:39+02:00 — Issue #54 sub-task A: added `kernel/git_freshness.py` (branch-vs-upstream freshness kernel) and the opt-in `context_packet` `include_freshness` section with `ledgerMapsCodeHead`.
- 2026-06-10T08:15+02:00 — No route impact: package version bumped to 2.7.0 (`pyproject.toml`, `SERVER_VERSION` fallback) for the GitHub #53/#58 release; route behavior unchanged.
- 2026-06-10T07:40+02:00 — GitHub #53/#58: added the background-observability invariant (async worktree provider setup with durable heartbeat progress, stale projection, retry path) and the container-form argv invariant; shared context helpers moved to `providers/context_common.py` (facade re-entrancy fix).
- 2026-06-10T06:05+02:00 — No route impact: package version bumped to 2.6.0 (`pyproject.toml`, `SERVER_VERSION` fallback) for the GitHub #56 release; route behavior unchanged.
- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3: the Hot Path Summary now records carryover route-overview candidates and guarded official-side index regeneration (`memory/carryover.py`).
- 2026-06-10T05:30+02:00 — Route body caught up with the 2.5.0–2.5.2 releases: content-gated provider readiness, the stdio subprocess invariant (#49), stall-watchdog doctrine, and the tool-report response-budget layer. Previous closeouts had only stamped the verification header (developer-flagged gap).
- 2026-06-10T05:20+02:00 — No route impact: sub-task 2 extended the body gates to route overviews and the c-05 skill doctrine; the route surface described in the sub-task 1 entry already covers both gates and the markers.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: added `kernel/onboarding_doc.py` (shared doc parsing + body/history classification) and the four-case sidecar body gate with in-band no-impact attestation markers to the route surface.
- 2026-06-09T14:52+02:00: Refreshed the MCP route overview against MCP 2.4.1 `main`; added the canonical root runtime asset sync boundary for package data.
- 2026-06-08T09:57+02:00: Re-verified the MCP package route after PR-39 restored context-packet provider-summary validation and made skipped-provider summaries a modeled optional-null contract.
- 2026-06-06T12:15: Re-verified against the current MCP package surface; corrected stale `mcp/tools.py` and provider lifecycle module references after the `mcp/tools/` package split and provider-first lifecycle packages.
- 2026-05-31T12:40+02:00: Removed the deleted `providers/integrity.py` runner-integrity prose and reference row after the provider-runner integrity feature was removed in the 1.0.0 remediation; `providers/status.py` no longer checks runner integrity.
- 2026-05-29T08:53+02:00: Updated after `server.py` began installing the `mcp/compact_content.py` shim that minifies tool-result text mirrors, and after dev-time tool-response conformance tests landed.
- 2026-05-28T19:52+02:00: Updated after public MCP response payloads were wired through Pydantic models, context packets moved to compact V2, provider diagnostics became the detail boundary, and controllers split by domain.
- 2026-05-28T13:40+02:00: Tightened MCP provider invariants to forbid CGC host `venvRoot`, host executable, and site-packages patch fallback paths.
- 2026-05-28T12:32+02:00: Updated after provider operator logs moved into the central `logs/` tree and provider status began writing current-state snapshots under `logs/providers/status/`.
- 2026-05-25T19:16+02:00: Updated after the legacy `provider_lifecycle.py` facade was deleted and `providers.lifecycle` became the sole lifecycle facade.
- 2026-05-25T19:01+02:00: Updated after provider lifecycle split into focused modules and GrepAI runtime became Docker-only without `_bin`, `_venvs`, host GrepAI, or host Ollama fallback.
- 2026-05-24T02:47+02:00: Updated after drift moved into `memory_quality.integrity` and `memory_quality_check` became the closeout quality gate.
- 2026-05-23T04:29+02:00: Created for the MCP package route after Phase 3 added MCP-owned runtime installation, provider layout convergence, and runner integrity checks.
