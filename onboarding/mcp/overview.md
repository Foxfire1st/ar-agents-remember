# mcp/ — MCP Package Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/`                                     |
| doc_type               | `route-local-overview`                     |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash | `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate | 2026-08-29T20:33:10+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[overview.md](../overview.md)

## IAS Source-Pair Coordination Boundary

Task documents remain upstream canonical planning truth and are always authorable. A task mutation
never waits on queue or atomic-series activation state: it publishes first, invalidates the affected
disposable scheduling projection, and lets current waiting candidates be recomputed.

Atomic implementation admission uses one source-pair-scoped replace-in-place selector. Multiple
live series are normal; selecting one pauses the previous series without retiring it. The selected
master remains `reconciling` until a contract-addressed sync brings the exact code/external-memory
base pair current, and only then becomes `active`. Genuine Git conflicts are retained in an
operation-owned worktree and stable enclosure-root journal for agent resolution, continuation, or
explicit cancellation.

The selector is not a lifecycle ledger, and the queue owns no claim, commit, certification,
integration, recovery, or terminal evidence. Terminal cleanup vacates only an exact selected owner
before its canonical contract pointer is deleted. Normal readers never fall back to task prose,
queue rows, old files, or ambient Git when activation/journal authority is absent or unreadable.
The focused route owner is [worktrees/overview.md](src/agents_remember/worktrees/overview.md).

## IAS Newest-First Ledger History

The external-memory ledger is ordered state history, not a globally unique code-to-memory map.
Settings-only memory changes may therefore create a new memory content commit and a newer ledger
row for unchanged code. `find_mapping` resolves the newest current row; exact-edge containment
preserves older audit history. Closeout/direct recovery, source-pair sync, integration, and
organizational completion all use that same distinction.

## L3 Canonical Scheduling-Register Boundary

The closeout queue consumes sprint judgments only from the exact orchestration-task Judgment and
Priority Register sections. Their template headings, headers, rectangular separator rows, and
outer Markdown pipes are part of the authority grammar; width-shaped prose or malformed table
rows fail closed before they can grade or order a candidate. Since 260815-DAG-L13 the fail-closed
side is the write/mutation path: sprint creation scaffolds the empty canonical registers,
`task_doc` writes validate register shape, and the queue's `status` read instead degrades to a
facts projection (absent/ok/malformed per register). Graph-less sprints project the
atomic-sequential default with waiting reasons derived from the source-pair selector; the retired
series-lane owner is not reconstructed.

## Current Structural Agent Boundary

Agent-facing dispatch, messaging, seat management, and gates use canonical task documents and roles.
A plane-injected hosted seat proves the caller; an ambient caller with no plane seat declares its
role + task document as request data and the same authorization validates it exactly like a seat
(260815-DAG-L16, L16-R2/R3/F5). `dispatch_agent` is the one public spawn tool for both caller kinds:
since 260821-ARSPAWN-L1 an ambient launcher (no `AR_HOSTED_SESSION_ID`) is resolved from the process
environment — not request data — spawns with the pinned brief and the same rollback, has no parent
seat (no child-scope), and still gets role-altitude validation; `spawn_agent_session` remains an
internal primitive only. Runtime session/lifecycle/gate/inbox identities stay
plane-only. The application resolves authorized parent/child seats and current occupants, with one
internally exact-pinned initial brief and replacement-aware ordinary messages. Startup migration is
one-way before strict current readers; there is no public exact-id compatibility surface.

## 260821-ARSPAWN-L2 Idempotent Structural Dispatch

The one public `dispatch_agent` operation now converges on the canonical task-document-and-role
seat for both ambient and plane callers. A bounded per-seat serializer covers spawn, durable
pinned-brief publication, receipt repair, and one proven-failed-generation replacement. Unknown
or contradictory post-commit state refuses without cleanup. Ordinary messages remain address-only
and re-resolve the incumbent or staged heir at delivery; public outcomes omit runtime occupant ids.

## Current Quality Execution Boundary

Python quality and pytest infrastructure now lives under the explicitly classified verification
package `mcp/test_support/agents_remember_test_support`, outside operational product code.
`code_quality/check_cli.py` owns only command-line construction while `code_quality/check.py`
retains scope derivation, rail execution, product-only scoring, causal preflight, and terminal
result ownership. Ruff, Pyright, structural limits, and dependency rails cover both product and
verification packages; Coverage.py, changed-line coverage, and CRAP score declared product roots
only. Product modules are forbidden from importing the verification package.

The package's development extra supplies pytest-xdist 3.x, while root pytest `addopts` owns
`-n=auto` for raw and wrapped runs alike. The quality wrapper adds only derived selection,
coverage, and retry-proof arguments. Every test file has one explicit evidence-lane declaration;
missing, stale, unknown, duplicate, or conflicting lane identity refuses collection. Retry proof
persists across real quality attempts in the locked `ar-quality-retry-v3` Dagger cache. Its key
binds the exact lane population and executor/tool identity; every cache miss is named before the
same admitted route runs fresh.

L23 makes the pinned Dagger graph the only Agents Remember acceptance environment. It materializes
the exact candidate tree and required Git ancestry into a clean Ubuntu image, streams progress,
and atomically replaces the enclosure's latest reports. Leaf/focused acceptance selects targeted
mode exactly once at leaf closeout; leaf integration and series closeout do not rerun it. Master
integration selects full mode once. Both require an explicit nonblank diff base, and
the Dagger function exposes source, bundle, base, mode, and cap through generated `Annotated`/`Doc`
help. Host pytest is refused and Candidate A's direct wrapper is absent; deterministic non-test checks remain
available for host feedback. A failed Dagger run never receives a host fallback. The same
slice adds durable asynchronous closeout/integration operations whose public address is the task
contract plus operation kind. Private operation keys, worker PIDs, approval fingerprints, and
candidate-tree identities remain plane-owned recovery state.

The current graph supplies a matching per-run nonce and in-container attestation to Python,
Playwright, the changed-lines CLI, and the direct quality wrapper. Those guarded rails refuse
startup outside that environment, so the old host-managed wrapper/test path cannot accidentally
become a second acceptance result. Direct targeted Vitest unit/component runs are deliberately
supported as fast non-certifying diagnostics; they provide no acceptance, changed-lines coverage,
or lifecycle evidence.

Durable lifecycle subprocess bootstrap is an installed-runtime boundary: the launcher preserves
the installed MCP environment instead of prepending task-checkout source, and the packaged worker
then declares the narrow `lifecycle-operation` execution mode before loading service/config
authority and binds default worktree services before task-addressed dispatch. That mode exists for
the plane-owned detached task worker only: it retains live operation authority without claiming
the MCP or dashboard daemon role, while undeclared checkout CLI execution remains isolated.

Native POSIX subprocess preparation rejects inherited Windows interop PATH entries, then prepends
only an existing native `$HOME/.local/bin`. That deterministic user-local admission lets installed
Linux harness commands and dashboard-local Node shebangs resolve without shell or version-manager
probing; it is part of the same fail-closed platform boundary, not a fallback search.

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

260715-FEUI-L9 established the stable protocol-neutral contract roof under `serving/conversation/`:
strict wire models and exactly two read ports now sit above the active transcript, conversation
library, and control child routes. Under `native_helpers/conversation_library/`, a locked private
Node helper normalizes repository-resolved harness observations into redacted evidence; it is not a
second server, store, or capability authority. The existing harness-control application factory
registers the conversation root once. The current child routes own their behavior beneath that roof;
the package does not thereby grant unrelated projector or renderer authority.

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
coordinator `system/settings.json`. The tool surface gained `task_reopen` cit:([`task_reopen`], mcp/src/agents_remember/mcp/registration/tasks.py:74-86):
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
respawn-after-rung threshold), consumed by the SAME `serving/app.py::_agent_notifier_context()` call
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
driving `run_agent_notifier_sweep` across multiple simulated ticks per incident: 6/8 pass fully
end-to-end; 2/8 (chip-stacked delivery stall, and the pane-classified half of never-briefed) are
proven hybrid (predicate-unit classify + real downstream sweep response) because `evaluate_predicates`
hardcodes a real, non-injectable `tmux capture-pane` call — documented as a real product gap and the
natural next leaf (make the pane capturer injectable through `AgentNotifierContext`), not silently
worked around. Results are filed in `notes/reports/260707-HFX2-L5-liveness-report.md`.

The packaged lifecycle/task-workflow projections now also carry M40@v2/M44@v2: semantic revisions
require explicit developer approval; formal worker attempts advance only at review handoff or after
reviewer rejection; internal implementation/test/evidence runs remain separate protocol events.
Lightweight requirement-specific journal records link content-addressed frozen expanded evidence,
and rebuildable summaries exclude protocol events and never become lifecycle, task, closeout,
integration, or queue authority. `scripts/sync-skills.py --check` remains the projection identity
proof.

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
bounded raw-free lifecycle status. `HarnessControlQueue` was a facade, not a second actor, and
260731-EFA-L6 deleted it outright. The shared
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
version-floor probe with fail-closed fallback. That probe stops and re-launches the SAME subprocess
transport, so the transport is a restartable resource: a completed stop releases process ownership
while a start against a live process still refuses.

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

The MCP package routes mutation tools through closed configured-contract admission, journal-rooted lifecycle controls, explicit enclosure adoption/legacy repair, and disposable door-based scheduling.

**260731-EFA-L21 — checkout coordination isolation.** An undeclared source-checkout invocation is
classified before runtime configuration is read: a linked worktree receives a synthetic
provider-disabled configuration rooted at `provider-runtime/dev-ar-coordination`, while a primary
checkout refuses live coordination access. Trusted MCP/dashboard declarations and installed
package execution retain the configured coordinator. The detached task-operation worker uses the
separate explicit `lifecycle-operation` mode because it must finalize one plane-owned durable
operation but is not a store daemon. The kernel policy and durable-store guard carry the invariant;
application startup, worker entry, and test bootstrap declare only their respective modes.

**260731-EFA-L1: `package_data/dashboard/` is no longer in this package's version-controlled
surface.** The bundle, its `dashboard.fingerprint` sidecar, and local `mcp/build/` / `mcp/dist/`
output are git-ignored. The recursive `package_data/**/*` glob in `mcp/pyproject.toml` still ships
whatever is present at build time, so the wheel and sdist carry a cockpit — placed by the release
job, verified by the release job. Building the package from a checkout with no bundle succeeds and
yields an installation whose `/` answers 503 with the build command. Two consequences for anyone
working in this package: a dashboard change produces **no packaged-asset churn to review**, and
`serving/build_info.py`'s `dashboardBuild` is routinely absent in a source checkout, so it must be
consumed as optional.

FEUI-MX-FIX-2 changed no MCP package source contract. Its `package_data/dashboard/` index,
fingerprint, and content-hashed assets were shipped output from the reviewed `dashboard/src/`
build, deliberately excluded from one-to-one onboarding: browser open authority is documented under
the dashboard source cards and overviews. (Historical: package parity was then proven by
`scripts/sync-dashboard.py --check`, and a generated rollover had to land as one complete
add/delete set. Neither applies now — the tree is untracked, the `--check` mode is gone, and the
release-time refusal to place a non-current `dist` is the surviving proof.)

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

Start in `src/agents_remember/mcp/config.py` for trusted settings parsing, then
`src/agents_remember/mcp/registration/` for the exposed MCP tools — since
260731-EFA-L2 the `@server.tool()` declarations live there, one module per tool
family, and `server.py` is reduced to process wiring: it installs
`mcp/compact_content.py` (tool-result text minification), installs the ambient
lifecycle, and walks `TOOL_REGISTRARS`, which is the only place that decides
which families a server advertises and in what order. The `mcp/tools/` package
still holds the payload builders those declarations call; verbose tools
additionally file bulk diagnostics under `temp/tool-reports/` via
`mcp/tool_reports.py` and return compact outcomes with a `reportPath`. Then
`models/tool_registry.py` for public response contracts,
`application/context_packet.py` for compact `ContextPacketV2` startup packets,
and `application/runtime_install.py` plus `install/runtime.py` for MCP-owned
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
application entry point surfaces it as the opt-in `include_freshness` packet section
together with a `ledgerMapsCodeHead` check, forming the lifecycle-start
staleness checkpoint. Route-index generation is split between
`kernel/route_index.py`, which renders route-local metadata, and
`kernel/route_index_census.py`, which validates the repository root and freezes
one exact Git/path-rule source snapshot for membership, coverage, and counts.
Tracked and untracked records are NUL-delimited, ignored/generated paths are
excluded by Git plus resolved storage rules, symlinks are classified without
following their targets, and ambient Git repository selectors are scrubbed by
`kernel/git_command.py` — which since 260731-EFA-L3 is the **only** module in
this package that spawns git at all, so that scrubbing is no longer a census
property. Application entry points and worktree closeout pass the resolved
repository identity and `StorageSettings` explicitly rather than rediscovering
authority inside the builder.

**`kernel/git_command.py` is the package's one git runner (260731-EFA-L3).** Six
near-identical private copies had drifted apart — in `worktrees/modules/git.py`,
`code_quality/diff_coverage.py`, `memory/carryover.py`,
`memory_quality/integrity/check_missing_onboarding.py`,
`memory_quality/integrity/onboarding_drift_check/git_ops.py` and
`kernel/route_index_census.py` — and only the kernel's passed
`env=git_environment()`. With `GIT_DIR` exported, the same logical operation
therefore landed in a *different repository* depending on which copy ran, and the
unguarded worktree copy sat behind `commit`, `merge --ff-only`, `reset --hard`,
`rebase`, `branch -D`, `worktree remove --force` and `push origin --delete`.
**Twenty-six package modules import from the single runner** — re-counted against the current
tree, and the count needs both import shapes to come out right: twenty-four take the symbol
(`from agents_remember.kernel.git_command import ...`) and two take the module
(`from agents_remember.kernel import git_command`, in `code_quality/check.py` and
`code_quality/diff_coverage.py`). Two of the twenty-six want `git_environment()` rather than, or
as well as, `run_git`: `benchmarks/runner_modules/commands.py` composes its own argv so the runner
cannot carry it; `worktrees/modules/landing.py::_pr_for` spawns `gh pr list`, which is not git but
resolves the repository *through* git, so an inherited `GIT_DIR` would list another repository's
pull requests. The quality-gate adapter no longer launches a host wrapper or builds a host
environment; it hands the reconstructed candidate and ancestry bundle to the pinned Dagger graph.

The runner always scrubs the eight selectors, always declares its stdin — `DEVNULL`, or
`input_text` for the `git patch-id` call in `memory/carryover.py` — and carries three
timeout classes in place of the former hard-coded `timeout=5`:
`GIT_LOCAL_TIMEOUT_SECONDS = 300` (a rebase or status over a large tree can
legitimately churn for minutes), `GIT_REMOTE_TIMEOUT_SECONDS = 120` (a remote that
has not moved bytes is wedged, and a wedged remote inside an MCP tool call has no
cancellation path), and `GIT_METADATA_TIMEOUT_SECONDS = 30` for constant-time reads
on interactive paths. Consolidating onto the old five-second bound unchanged would
have replaced a redirection bug with a five-second failure on every integrate.

**The class belongs to the command, not to the module that calls it.** Consolidating onto a runner
whose *default* is the local bound would have silently moved every `rev-parse` from 5s to 300s — a
60x loosening on reads that sit under `resolve_context`, which runs on essentially every tool call,
with no cancellation path for the client. So the band is named per command:
`rev-parse --is-inside-work-tree`, `rev-parse HEAD`, `branch --show-current` and
`rev-parse --abbrev-ref <branch>@{upstream}` take the metadata bound, while `status --porcelain`
and `rev-list --left-right --count` are not constant time (one stats the whole work tree, the other
walks history) and keep the local bound **explicitly named** rather than defaulted.
`kernel/git_facts.py::_git_stdout` makes `timeout` a *required* keyword-only argument for exactly
that reason — a call site that leaves the class to the default is a type error, not a quiet
inheritance. `kernel/git_freshness.py::fetch_remote` keeps its own 30s `DEFAULT_FETCH_TIMEOUT`.
`mcp/tests/test_git_command.py::TimeoutClassTests::test_one_command_means_one_bound_across_the_kernel`
pins the rule where it was already broken: `branch --show-current` and `rev-parse HEAD` are called
from both `kernel/coordination_context/cross_repo.py` and `kernel/git_facts.py`, and the test
asserts the two modules agree.

`mcp/tests/test_git_command.py` holds every half: a decoy repository the selectors
point at, an AST sweep that fails if a seventh runner appears, a guard-on-the-guard suite that
plants each bypass form the sweep must catch, and the per-command timeout assertions above.

Branch-memory carryover (`memory/carryover.py`)
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
`mcp/tests/test_sync_runtime.py` plus the generated-copy check that runs in both hook tiers. The
built dashboard cockpit ships under `package_data/dashboard/`, placed there from `dashboard/dist/`
by `scripts/sync-dashboard.py`. Since 260731-EFA-L1 that placement is a **release build step**: the
bundle is git-ignored, no hook or CI job checks it, and `scripts/sync-dashboard.py` has no
`--check` mode. It is covered by `mcp/tests/test_sync_dashboard.py` and driven by
`.github/workflows/publish-mcp-to-pypi.yml`.

`package_data/` has a **third population** since 260731-EFA-L3, and it is neither synced from a
canonical root folder nor built at release: `package_data/tiktoken/` holds the vendored `o200k_base`
vocabulary that `models/tokens.py` counts response tokens with. Unlike the dashboard bundle it is
**tracked in version control**, its file name is `sha1(<download URL>)` because that is the only name
`tiktoken.load.read_file_cached` can hit, and root `.gitattributes` names **that exact filename**
`-text` so no EOL filter can touch it on a `core.autocrlf=true` clone. It ships
because `mcp/tools/base.py` imports `models/tokens.py` and `DEFAULT_TOKEN_COUNTER` is built at module
scope: before the file was vendored, `tiktoken.get_encoding("o200k_base")` opened an HTTPS connection
to `openaipublic.blob.core.windows.net` while the server was still importing, so a fresh container,
an offline machine and a hermetic CI job could not start the server at all.

**This package verifies the vocabulary itself, and that is a correctness property rather than
belt-and-braces.** `vendored_vocabulary_cache` calls the private `_verify_vendored_vocabulary` first,
*before* it touches `TIKTOKEN_CACHE_DIR` at all, and that helper raises `TokenizerVocabularyError`
for three cases: an encoding this package does not ship, an absent file, and a file whose SHA-256
does not match `VENDORED_VOCABULARY_SHA256`. Leaving the digest check to tiktoken would not have
been equivalent — tiktoken checks the same hash but does **not** fail closed on it:
`read_file_cached` deletes the offending file and downloads a replacement over it, which pointed at
this package's directory means a network fetch on the startup path plus a rewrite of the installed
tree, or a `PermissionError` from the write-back on the read-only installs this is written for.
Checking first is what makes corruption behave like absence. Only the *verified* file's own parent
directory is then handed to tiktoken, so it cannot be pointed at a directory whose contents were not
checked, and the override is scoped to the one load (the vendored directory sits inside the
installed package, which is routinely read-only). `_CACHE_DIR_LOCK` is a `threading.RLock` rather
than a `Lock` because the guarded region spans the `yield`: the obvious use of an exported context
manager — `with vendored_vocabulary_cache(name): TiktokenTokenCounter()` — has the counter's own
load re-enter it on the same thread, which on a plain `Lock` is a permanent hang with no timeout and
no diagnostic. Counts and the reported `tiktoken:o200k_base` name are unchanged — the shipped bytes
are the download — and `mcp/tests/test_cold_start.py` is the regression line.

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
- `agents_remember.application` owns operation-level composition such as
  `context_packet`, provider tools, worktree tools, memory tools, benchmarks,
  and `runtime_install`.
- `agents_remember.models` owns public MCP response contracts and the
  tool-to-response-model registry used by the `mcp/tools/` payload builders.
- `agents_remember.tasks` owns JSON-primary task documents plus the strict persisted execution
  vocabulary: commanded-master nature, sprint reasoned AON graph, exact cross-document membership,
  deterministic derived waves, rendering, and rollback-safe publication. The application layer
  owns the explicit finite migration and validates supported task-doc edits before publication.
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
  260712-PTS-L1 makes contract READS…35938 tokens truncated…p`/`--no-access-log` with settings-default
  `--port`, `mcp/config.py` parses the fail-loud `dashboard` settings object (autoStart, port), and
  `mcp/server.py` `main()` gains the threaded `maybe_autostart_dashboard` boot hook. Covered by
  `mcp/tests/test_dashboard_daemon.py` + new `test_config.py` cases. Verification metadata pinned
  until closeout stamps the code commit.
## L23 Plane-Owned Source Lineage

The MCP now resolves task identity to contract-backed super/master/leaf Git
edges before structural spawn, assignment, attach, start, or reopen. Strict
models, application translation, observer projection, and dashboard transport
share one evidence shape. Unavailable or stale ancestry fails closed and points
to ordered contract-addressed `worktree_sync`; agent-carried ids are not part of
the protocol.

## L23 Current Lineage And Package Boundary

The MCP package now groups runtime installation, startup, and skill installation under
`application.runtime`, and lifecycle responses, finalization, and durable operation DTOs under
`models.lifecycles`. Task-derived source lineage is enforced at start/resume, immediately before
curator dispatch, and through closeout/integration preflight, post-quality, and final mutation
boundaries. The MCP transport remains a thin registration/forwarding layer over those application,
model, and worktree owners.

## R39 Dagger-Only Enforcement Route

The package now owns a shared nonce/file Dagger environment validator used by pytest collection and
the direct quality wrapper before planning. The lifecycle adapter has no host executor: Agents
Remember requires its self-owned wrapper, leaf closeout runs targeted once, leaf integration
reuses that commit, and master integration runs full once. Series/master closeout records clean
landed code. Settings expose only Dagger and an optional container-inner cap.

## R42 Recovery And Test Ownership

The finalization proof and typed memory-closeout outcome now live with the other irreversible-cell
recovery primitives in `worktrees/closeout_recovery.py`; `worktrees/modules/closeout.py` imports
them and remains the coordinator. Two focused test modules split direct environment authorization
and exact staged gate scope out of oversized suites without changing the production boundary.

## 260815-DAG-L2 Packaged Planning Doctrine

The packaged `l-01-agent-lifecycles` assets now mirror the canonical nature-aware planning
contract. Architect owns the initial strategist and plan-review loop; orchestrator adopts the
ruled topology choice and a graph only when one exists, records queue judgment, and recomputes the
ready frontier; managers distinguish organizational direct-super leaves from atomic branch-backed
blockers. Graph-less atomic-sequential execution is a valid reviewed topology. A sanctioned
strategist skip transfers the complete dependency, route, seam, classification, priority, and
topology-reasoning duty to the orchestrator rather than requiring a graph. The package also carries
the exact proposed-candidate master-exit handoff and leaf-owned remediation boundary.

## 260821-DAGQC-L4 Doctrine And Review Closure

Packaged review inventories treat untracked input as hostile filesystem evidence: NUL-safe
enumeration precedes no-follow type/mode/content inspection, and reports record disposition plus
race limits instead of silently omitting or following entries. Candidate priority has one effective
value — candidate override, otherwise master default — while the orchestrator retains portfolio
comparison authority. Graph-less atomic-sequential is valid; choosing a graph from that state first
attaches every master, then publishes one complete nodes-plus-evidence-edges batch.

Master handover packets cite canonical candidate, code ancestry, memory ancestry, and per-leaf
ledger references so receivers revalidate authority without copied maps. Existing `add_edge`
examples already carried `judgmentId`; no fabricated code fix or lifecycle evidence was added.
Delegated-authority redesign, disabled-memory behavior, mandatory-graph runtime, and declared-caller
trust redesign remain outside this leaf. Canonical and generated skill copies were synchronized,
but that sync check and direct targeted Vitest diagnostics are not Dagger acceptance evidence.

## 260815-DAG-L3 Closeout Queue Control Plane

`closeout_queue` is the MCP route for declaring reviewed leaves before history moves, recomputing
their current readiness, and exposing deterministic ready/waiting/blocked/in-flight projections.
The application layer derives the structural caller from the ambient seat; the worktree service
separates manager logistics from orchestrator grading/selection; the models hold strict bounded
requests and durable state; the control plane owns the canonical sprint artifact plus one-record
WAL; and lifecycle hooks claim, certify, revalidate, consume, or reversibly release the exact
candidate around closeout and integration. The queue consumes canonical task-document judgment and
priority rows but never authors them.

## 260815-DAG-L4 L4 Integration-Authority Plane

The MCP runtime now owns repository-global protected-ref census, durable closeout/integration operations, cross-operation leases, queue-before-repository lock ordering, exact named-ref compare-and-swap, atomic-series sealing, and guarded terminal/memory writers. Public tools preview the same authority they apply; direct CLI/helper paths cannot widen it.

## 260815-DAG-L14 Sprint-Structure Plane

The MCP `task_doc` surface now registers the sprint-structure operations — `attach_master`,
`detach_master`, `linkage_report` — routed to `application/task_sprint_linkage.py`; a sprint `get`
carries `linkageFacts`, and the task-document writer census admits the linkage module. The
`ar-task-document/v1` route carries first-class sprint `seats` and typed `masterRef` rows.


## 260815-DAG-L12 Route Impact

The MCP package renders and projects the sprint execution graph for humans: `tasks/render.py` emits the deterministic mermaid document diagram, `tasks/execution_graph_titles.py` owns the shared title join, `observer/projection_graph.py` builds the render-ready `executionGraphView`, and the serving task-documents readers wire it onto `TaskDocNode`. Application writers thread the joined titles through every publish/preview site.


## 260815-DAG-L15 Route Impact

New `tasks/serving_preflight.py` (served-build preflight, L15-R4) and `application/memory_quality_runs.py` (bounded async run registry, L15-R7); the `memory_quality_check` registration gained `wait`/`run_id`; topology/linkage authoring hardened (typed refusals, `create=False` dry-run locks); the L7 `worktrees/orchestration_portfolio.py` module + its test were deleted (recorded decision: doctrine + queue mechanism).

## 260815-DAG Master Full-Gate Repair Route Impact

New sub-package routes `application/task_docs/`, `models/queue/`, `worktrees/queue/`, `worktrees/integration/` (32 moved modules); the `task_doc` special-op wire-shape fix (`TaskDocResponse` fields + `_sprint_doc_identity`); closeout/reopen refactors; the package_data orchestration-task template copy re-synced.

## 260821-CLIVE-L1 Closeout Architecture

Closeout now crosses one explicit input boundary before lifecycle authority or Git. `worktrees/closeout_input.py` derives typed enabled/not-applicable legs and emits one stripped `EffectiveCloseoutInput`; worktree closeout journals that value and per-repository mutation evidence, while direct landing shares the input contract but remains synchronous, lock-serialized, and intentionally not crash durable in L1. Lifecycle records—not queue rows—own accepted input, mutation proof, recovery projection, and exact contract-finalization identity. The queue remains a scheduling projection outside this leaf. Strict schema 3.0 replaces compatibility readers, and `contract_publication_text` is the one serializer used by publication and hashes.

## 260821-CLIVE-L2 Current Architecture

The package surface now exposes retry, recover, cancel, revise, integrate, retire/supersede, bounded legacy handling, and enclosure adoption without private operation ids. Read-only degraded status remains separate from mutation admission. Expected lower reader/authority failures have one public projection; unexpected faults stay loud.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Public worktree payload surface. | `worktree_closeout_apply_payload`; `worktree_operation_control_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:119-128; mcp/src/agents_remember/mcp/tools/worktree.py:151-158 |
| Admission forcing across every consumer. | `test_every_public_consumer_exhaustively_refuses_each_semantic_category`; `test_public_consumers_do_not_enumerate_configured_reread_lower_families` | mcp/tests/test_configured_contract_admission_l2.py:184-274; mcp/tests/test_configured_contract_admission_l2.py:632-650 |

## 260821-DAGQC-L2 Packaged Doctrine Synchronization

No root-route responsibility changed. Packaged c-02 and curator doctrine mirrors now use the same
strict memory-quality request grammar as canonical sources; the package remains a synchronized
distribution target rather than a compatibility owner.

## 260824-PDLS — Python Testing Route

`agents_remember_test_support.testing` is the verification-only route for structural direct-test
eligibility, shared hermetic pytest bootstrap, Dagger admission composition, the canonical direct
runner, and route-neutral phase/causal reporting. Its lifecycle catalog governs 35 durable support,
data, policy, and task/date proof artifacts. Its explicit lane manifest classifies the complete
test-file population; nothing unmarked becomes unit evidence. The direct route is an explicit
content-sealed seven-node cohort, not a generic repository analyzer.

`models/test_evidence.py` separates diagnostic and certifying altitudes. The code-quality plane
keeps all Python lint/type/size/execution coverage while scoring product modules only, and one
source-derived dependency graph serves targeted selection, retry invalidation, and exact-node
causal localization. Lifecycle declarations are cross-checked against observed consumers and do
not self-prove completeness. The worktree plane consumes typed Dagger admission/evidence instead of reimplementing
test-route failure families. Removed analyzers, task/date baselines, and former global/random helper
owners have no compatibility facade.

## 260824-PDLS Final Package Reconciliation

The final tree moves the certifying pytest bootstrap to the verification-package root, keeps
diagnostics and route measurements non-certifying, consolidates dependency ownership and causal
failure evidence, and splits lifecycle and queue helpers by authority. The package retains one
Dagger acceptance path and introduces no fallback runner, compatibility facade, or queue-owned
commit evidence.

## MCAR Exact Future-Code Candidate Boundary

Ordinary leaf closeout now has one frozen, plane-derived pre-commit route identity: contract base,
stable observed HEAD, and the canonical isolated-index full add-all tree. Callers provide intent
and evidence but never the authoritative tree. Each concurrent observation uses a distinct
automatically cleaned enclosure-local index, so preview and admission cannot corrupt each other's
identity calculation or stage the user's real index.

This tree-bound semantic identity remains separate from lifecycle-operation reconciliation. A moved
HEAD is not treated as an operation output without unchanged operation identity or journaled commit
proof. Series/direct-existing landing stays on its committed-tree route. The focused source owner
and boundaries are documented in [worktrees/overview.md](src/agents_remember/worktrees/overview.md).

## MCAR Structured Curator-Coherence Authority

The MCP package now exposes one `curator_coherence` lifecycle API with
`status`/`prepare`/`publish`/`validate` actions. A stable task-local structured manifest selects one
content-addressed record and deterministic human projection; exact source-candidate judgments are
agent-owned and evidence-digest-bound. Requirement revision, delivery attempt, and immutable
content identity stay separate. Public memory readiness, closeout-door evidence, and closeout
admission invoke the same validator, so a ready memory result cannot later disagree with closeout
over a different hardcoded report. No historical-filename search or Markdown authority remains.

## Update History

- 2026-08-29T08:52+02:00 — MCAR-L02 A005: added the single structured curator-coherence authority,
  deterministic attestation bridge, and shared memory/closeout validator. Verification remains
  closeout-owned.

- 2026-08-29T05:28+02:00 — MCAR-L02: added the parent-route summary for immutable exact
  future-code identity, collision-free concurrent observation, and the separate
  operation-reconciliation boundary.

- 2026-08-28T15:52:15+02:00 — No route impact: the hook environment repair and its focused
  regression test preserve MCP package ownership and keep the host hook a deterministic non-test
  gate.

- 2026-08-28T10:03:40+02:00 — Reconciled the MCP quality-route summary with Candidate A's deletion;
  deterministic host checks remain, but no host Python wrapper exists.

- 2026-08-27T22:15+02:00 — Synchronized packaged lifecycle projections and structural proof for
  the pre-handoff correction versus post-handoff rejection boundary.
- 2026-08-27T21:53+02:00 — M40@v2/M44@v2 packaged-skill impact: synchronized review-handoff-only
  attempts, separate protocol events, lightweight content-addressed records, and non-gating summary
  semantics across all runtime projections.
- 2026-08-26T16:03+02:00 — Memory hygiene: removed a pre-existing tool-output truncation banner
  accidentally committed above the package overview title; route content is unchanged.


- 2026-08-26T14:32+02:00 — Corrected the package-wide ledger contract after IAS activation exposed
  an unrequested uniqueness rule: repeated code commits are valid newest-first memory history and
  all lifecycle consumers now distinguish current lookup from exact historical containment.
- 2026-08-26T12:30+02:00 — 260821-ARSPAWN-L2 package impact: recorded canonical-seat idempotency, bounded
  evidence-aware recovery, replacement-safe delivery, and runtime-id-free public outcomes.
  Verification remains closeout-owned.

- 2026-08-26T02:55+02:00 — Reconciled the MCP route with source-pair atomic activation,
  pause/reconcile switching, stable enclosure-root sync recovery, unlocked task authoring,
  disposable queue ownership, and exact terminal selector release.

- 2026-08-25T17:21+02:00 — Reconciled the final PDLS package ownership and evidence boundaries.
  Verification remains closeout-owned.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: documented the extracted quality CLI parser and its non-authority boundary at emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; the recorded Dagger gate remains red.

- 2026-08-25T01:56+02:00 — 260824-PDLS reconciled the explicit cohort, lifecycle/cadence registry,
  product-only scoring, shared ownership graph, and causal localization.
- 2026-08-24T21:23+02:00 — 260824-PDLS introduced the testing route and explicit evidence
  altitude boundary.

- 2026-08-24T14:19+02:00 — No route impact: 260821-DAGQC-L2 synchronized packaged memory-quality and curator examples to the canonical discriminated request while preserving concurrent L4 route material. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: reconciled packaged planning,
  review evidence, effective priority, graph-optional topology, atomic graph adoption, and
  canonical handover references. Also recorded direct targeted Vitest as diagnostic-only while
  guarded acceptance rails remain Dagger-attested. Canonical/generated sync is reported green;
  Dagger acceptance remains pending and closeout-owned.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: route claims reconciled to accepted candidate tree `4241908c`; verification metadata remains closeout-owned.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `dispatch_agent` becomes the one public spawn tool for both caller kinds; ambient launchers are resolved from the process environment (no `AR_HOSTED_SESSION_ID`) with role-altitude validation, and `spawn_agent_session` stays internal. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: new package routes (`application/task_docs`, `models/queue`, `worktrees/queue`, `worktrees/integration`); `TaskDocResponse` wire-field fix; closeout/reopen refactors; sync-skills orchestration-task copy. Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: new serving_preflight + memory_quality_runs modules, async memory-quality wait/run_id surface, hardened authoring dialect, and the L7 orchestration_portfolio deletion. Verified at code commit de3a0fd9.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 render-ready sprint graph: mermaid document diagram, shared title join, primitives-only projection builder, serving wiring, application title threading. Verified at code commit b7f2c8e2.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: seat-independent task-execution fallback
  (declared caller on closeout-queue and structural gate tools), branch-addressed `record_route_review`
  binding, and the `direct_landing` operation. Verified at code commit a9d50e08.


- 2026-08-20T05:02+02:00 — 260815-DAG-L14 route impact: `task_doc` registers
  `attach_master`/`detach_master`/`linkage_report` and carries `linkageFacts` on sprint gets; the
  sprint document route gains first-class `seats` and typed `masterRef` rows. Verified at code
  commit 8071a644.

- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: the canonical scheduling-register boundary
  now records the L13 split — mutations and document writes stay fail-closed (creation scaffolds
  the empty registers, writes validate shape) while the queue `status` read degrades to a facts
  projection, and graph-less sprints run the atomic-sequential default with a named series lane
  owner; new modules `worktrees/scheduling_mode.py` (mode/nature/lane resolution) and
  `worktrees/closeout_queue_blocker.py` (blocker transitions, extracted from `closeout_queue.py`)
  joined the route, and `migrate_execution_topology` was removed. Verification remains
  closeout-owned.
- 2026-08-19T04:20+02:00 — No route impact: 260815-DAG-L10 re-rooted the series contract `worktree_group` at `worktrees/<repo>/<master>-ar` so series reports are swept with the group; leaf enclosures and the mcp-route purpose are unchanged.
- 2026-08-18T12:00:00+00:00 — No route impact: 260815-DAG-L9 added `inventory_execution_topology` to `application/task_execution_topology.py`; the mcp-route purpose is unchanged.
- 2026-08-18T10:30+02:00 — No route impact: 260815-DAG-L7 added the orchestrator portfolio loop under worktrees; route purpose unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-18T01:24+02:00 — No route impact: 260815-DAG-L6 added the blocker-acquisition super-tip precondition (`_require_current_super_tips`) under mcp/src/agents_remember/worktrees; the route's purpose is unchanged.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added organizational-completion modules under mcp/src/agents_remember/worktrees; the route's purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T13:27+02:00 — No route impact: the Pyright repair is an explicit test-only
  optional-result narrowing; MCP source, routing, and behavior are unchanged.
- 2026-08-15T13:18+02:00 — No route impact: Ruff reformatted one strict evidence predicate and
  ten queue/topology test modules; MCP behavior, routing, and ownership are unchanged.
- 2026-08-15T13:08+02:00 — No route impact: the closeout fast-hook repair is import grouping and
  test-only binding cleanup; queue routing, public behavior, and ownership are unchanged.
- 2026-08-15T12:53+02:00 — L3 targeted-gate route impact: tightened canonical judgment-table
  parsing and atomic finalized-landing proof while splitting their exhaustive forcing by owner; no
  second queue, evidence authority, or test altitude was added.
- 2026-08-15T11:25+02:00 — L3 static-gate route impact: separated task-doc queue-scope
  classification and exact evidence comparisons from their orchestration callers without adding a
  second authority or compatibility path.
- 2026-08-15T11:07+02:00 — L3 Dagger-failure route impact: refined graph-governed task
  publication, exact queue refusal diagnostics, and worker-owned recovery of a committed but
  uncertified leaf while preserving one mechanistic queue and lifecycle authority.
- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: added the cross-layer closeout-queue route
  and its exact evidence, persistence, task-fact locking, and lifecycle boundaries. Verification
  remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2 route impact: synchronized packaged lifecycle roles,
  criteria, briefs, and verdict templates with the ruled organizational/atomic topology and
  auditable planning authority. MCP tool routing and worktree enforcement are unchanged in this
  leaf; verification remains closeout-owned.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: task-document identity mutations can
  no longer bypass sprint topology validation, and the new multi-root publisher is covered by the
  existing single-owner fitness census. Package routing and ownership remain unchanged.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: the MCP task-document surface gains one
  explicit, previewable execution-topology migration and projects the same canonical nature/graph
  contract. There is no implicit legacy inference or compatibility reader.

- 2026-08-14T14:03:04+02:00 — No route impact: R46 changes only the assertion spelling for the
  existing metrics-shutdown timeout in one test. MCP production, package authority, public
  behavior, and package routing are unchanged; verification remains pinned to the last committed
  source until closeout.

- 2026-08-14T11:48:55+02:00 — R42 curator: recorded recovery-proof ownership and the two focused
  test extractions. Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: added the shared environment guard, self-wrapper policy,
  and final altitude topology to the package route. Verification remains closeout-owned.

- 2026-08-14T09:08+02:00 — No route impact: reopened L23 narrows candidate-bound route-review
  admission to its already-documented leaf altitude so repeat series/master closeout can restamp
  the final leaf tip. MCP package ownership and public tool shape are unchanged; verification
  provenance remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final package review: reconciled the package authority map with
  Dagger-only acceptance, per-run suite attestation, exact-candidate recovery, route review, and
  transitive lineage rechecks. Verification provenance remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final quality-contract review: recorded Dagger-only Agents Remember
  acceptance, targeted leaf/focused versus once-per-master full altitude, mandatory explicit diff
  base, generated function help, and host execution's diagnostic-only status. Verification remains
  closeout-owned.

- 2026-08-13T12:26+02:00 — No route impact: L23 extracted closeout's existing external-memory
  quality-phase mechanics into a sibling worktree module, renamed internal registrar helpers, and
  adjusted test-only package-root imports. MCP package authority and public tool behavior remain
  unchanged; verification provenance remains closeout-owned.


- 2026-08-13T09:05+02:00 — L23 integration-gate follow-up: recorded the dedicated application
  runtime and lifecycle-model packages, pre-curator task-derived lineage proof, and closeout/
  integration transitive post-quality/final rechecks. Exact behavior remains in the application,
  models, worktree-module, lifecycle-skill, and test child routes; final verification provenance
  remains closeout-owned.
- 2026-08-13T00:07+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: documented MCP-package ownership of the explicit lifecycle-operation execution mode. The detached task worker declares it before config/service loading, retains live durable-operation authority, and does not claim MCP/dashboard daemon ownership; undeclared checkout CLI isolation remains unchanged. The owner reports 46 focused tests, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T21:18+02:00 — L23 curator follow-up: documented deterministic native `$HOME/.local/bin` admission after Windows-interoperability filtering; no shell/version-manager discovery or compatibility fallback was added. Verification remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented MCP-wide task-derived lineage admission and recovery ownership; verification remains closeout-owned.
- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime route review: detached lifecycle launch
  now preserves installed MCP code selection and the packaged worker composes real services before
  dispatch. Task checkout state remains input, never unpublished runtime code. Verification
  provenance remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added the explicit Dagger clean-quality executor and task-addressed durable lifecycle-operation boundary; verification provenance remains closeout-owned.

- 2026-08-12T10:08+02:00 — No route impact: MCP 3.0.0rc7 advances the existing package and
  kernel fallback version authorities without changing package routes, dependencies, entry
  points, or tool behavior. Verification metadata remains pinned until closeout.

- 2026-08-12T09:20+02:00 — No route impact: the 260731-EFA-L20 reopen changes only the executable shape of one checkout-isolation assertion; MCP package behavior and routing are unchanged.
- 2026-08-12T08:41+02:00 — No route impact: 260731-EFA-L20 adds no package behavior or source route; it repairs master-gate proof through test simplification and direct boundary coverage.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 route impact: settings,
  integration, closeout, packaged lifecycle doctrine, and regression tests now
  agree on host-managed full-gate RAM/swap with an optional explicit hard cap.
  Verification metadata remains pinned until closeout stamps L24.

- 2026-08-12T01:38+02:00 — No route impact: 260731-EFA-L22 makes leaf quality enforcement
  deterministic (exact Ruff pin and preserved file-size arm) and splits three oversized test
  responsibilities; package subsystems and public tool inventory are unchanged.

- 2026-08-12T00:20+02:00 — Corrected the package boundary: the dependency supplies pytest-xdist,
  root pytest configuration owns worker selection, and the wrapper contributes derived gate
  arguments only. Verification metadata remains pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded the package-level pytest-xdist dependency, automatic worker
  selection in the single pytest rail, and retry-proof invalidation across executor changes.
  Verification metadata remains pinned until closeout.

- 2026-08-11T19:58+02:00 — 260731-EFA-L19 curator: reconciled the package route with the public
  structural agent surface and private plane-owned session, inbox, and gate machinery; child-route
  overviews and one-to-one cards carry the implementation evidence.

- 2026-08-10T19:57:55+02:00 — 260731-EFA-L21 route impact: recorded checkout execution
  classification, the linked-worktree dummy coordination root, primary-checkout refusal, and the
  trusted MCP/dashboard plus explicit-test declarations. Detailed ownership remains in the
  application, kernel/primitives, controlplane, and tests route cards. Verification metadata
  remains pinned until closeout stamps the L21 code commit.

- 2026-08-10T13:00+02:00 — 260731-EFA-L9 curator: refreshed the mcp/ route body for the current
  staged package delta (application, models, registration/tools, memory-quality, worktree, and
  serving seams); file-level details remain in sidecars. Verification metadata remains pinned
  until closeout.

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
- 2026-06-14T23:30+02:00 — Slice 05 (5c): the `agents_remember.observer` read side added persistent
  lifecycle and per-worktree provider projections plus full task content; serving simulation/event
  fixes and matching tests landed. The then-added rich-sim generator was later retired by PDLS
  after it had no maintained consumer.
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
