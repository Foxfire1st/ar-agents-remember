# mcp/src/agents_remember/serving/ — Dashboard Serving Layer Overview

## Native API composition and persistent frame delivery

Serving adds native role routes beside retained MIK review/read ports, with exact selected source/configuration authority. Frame/plugin delivery binds the permitted parent origin, bridge protocol and native selection. Requested launch intent, visible execution and independent acceptance remain separate. Imported source does not imply that a running installation has already been replaced.

- Current imported source owns this scoped route boundary. [84]
- Current imported source owns this scoped route boundary. [85]
- Current imported source owns this scoped route boundary. [86]
- Current imported source owns this scoped route boundary. [87]
- Current imported source owns this scoped route boundary. [88]

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/serving/`               |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## The Tree View Route

[`review_trees.py`](review_trees.py.md) is the transport of the reviewer's tree view,
`GET /api/review/trees?repo&master&leaf[&comparison=<n>][&history=recorded]`. It holds no review logic: it checks the
query, calls the port and serializes the typed result once.

- **The question.** The task context is `repo`, `master` and `leaf`, never a path. `comparison=<n>` names a recorded
  comparison and `history=recorded` the leaf's latest record. At most one focused question is allowed:
  `invariants=<id,id,...>` for the realization and proof entries of those invariants, `lane=files` for the
  unexplained-changes lane, or `file=<path>` for one changed path's classification. Without one the answer is the
  leaf-wide view. The parameters arrive as one `ReviewTreesSelection`, whose `problem()` refuses a history other than
  `recorded`, a negative comparison number, more than `MAX_ENTRY_INVARIANTS` (500) names, a name longer than
  `MAX_INVARIANT_KEY_LENGTH` (64), a lane other than `files`, an empty file path or one longer than
  `MAX_FILE_PATH_LENGTH` (4096), and more than one focused question.
- **The answers.** Every typed answer of the port is a 200: `trees`, `not-converted` and `refused`, with the owner's
  refusal in the body. A refused selection is a 400 with `status: invalid-request`. A process composed without the port
  answers 503 with `status: unavailable`.
- **The wiring.** [`_app_common.py`](_app_common.py.md) declares `ServingCollaborators.review_trees` and
  `review_trees_shutdown`. [`app.py`](app.py.md) registers the route after the review summary route and before the
  knowledge reader route, and copies `review_trees_shutdown` into the runtime. `cli/dashboard.py` binds the port to
  `application/review_tree_knowledge.read_review_trees` with the worklist process owner it composes, and supplies
  that owner's `shutdown`.
- **The route's own threads.** `register_review_trees_route` creates one `ThreadPoolExecutor` of
  `REVIEW_READ_THREADS` (16) threads for the route. The handler is a coroutine; the blocking port runs on those
  threads, never on the event loop and never on the loop's shared default executor, so background work that fills the
  default executor cannot delay a tree read.
- **Cancellation and arrival.** `_request_result` binds a cancellation event and the request's arrival time to the
  call (`worklist_request`), so the deadline of a worklist computation runs from the arrival. While the port runs,
  the coroutine checks every 0.1 seconds whether the client has disconnected and sets the event when it has. When the
  coroutine itself is cancelled it sets the event, waits for the worker and raises the cancellation again. A worklist
  computation that no request needs any more is thereby stopped and its child process reaped before the request ends.
- **Shutdown.** [`_app_lifespan.py`](_app_lifespan.py.md) calls the runtime's `review_trees_shutdown` first when
  serving ends, on a worker thread, before it cancels its background tasks. This stops and reaps every worklist child.
- The route is GET-only. A read of a live comparison may create the Git refs that pin the comparison's uncommitted
  candidates and its record under the task's reports; a repeated read of the same trees writes nothing. A dataset
  review never calls this route.

- The bounds of a selection and the size of the route's thread pool. [100]
- The value handed to the port, and whether it asks a focused question. [101]
- The one selection value and its refusals. [102]
- The port runs on the route's executor with cancellation and arrival bound; a disconnect and a cancellation set the event. [103]
- The route: its own executor, the unwired 503, the selection's 400 and the typed 200. [104]
- The collaborator that stops the route's child computations. [89]
- The runtime receives the shutdown callable from the collaborators. [90]
- Serving shutdown calls it on a worker thread before the background tasks are cancelled. [91]
- The composition root composes one worklist process owner. [92]
- It supplies that owner's shutdown to the app. [93]
- The tree port passes the process owner to the application. [94]
- A live read reuses the record of the same trees, and pins before it writes a new record. [95]
- A payload without a tree comparison number is a dataset review, for which no tree read is made. [96]
- A busy default executor cannot delay a tree read. [97]
- A disconnect, the deadline, shutdown and a queued request each end with the children reaped. [98]
- The lifespan fixture asserts one shutdown call per serving lifetime, off the main thread. [99]

## 260928-MIK-L29 The Knowledge Reader Route, A Port Of Its Own

**Route meaning extended (MIK-R29).** One new route module, [`knowledge_reader.py`](knowledge_reader.py.md) (carded,
governed here): `GET /api/knowledge/reader/{view}?repo[&commit][&path|id|census|locator|blob|continuation]`,
transport only. The view is one of `selections`, `tree`, `path`, `subtree`, `record`, `records`, `census`,
`without-proof` and `code`; `commit` is `published` by default, a memory commit's hexadecimal name, or
`leaf:<scope>`. Every typed answer is a 200 (a view, `not-converted`, `not-found`, `unavailable`, a subtree
`refused`); `invalid-request` is a 400 (an unknown view, a path with `..` or a control character, a malformed
locator; rulings F3 and F15); a process composed without the port answers a named 503. It is **not** a reviewer
route: the reader needs no task, so [`_app_common.py`](_app_common.py.md) declares its own
`ServingCollaborators.knowledge_reader` port (typed by the route module), [`app.py`](app.py.md) registers the route
right after the tree view route and before the static mount, and `cli/dashboard.py` binds the port to
`application/knowledge_reader.read_knowledge_reader`. The route is GET-only and never writes; the landed routes keep
their bodies byte for byte (the unconverted comparison, base against worktree).

- The query, the port and the GET handler with its three answer classes. [3]
- The collaborator port and the registration before the static mount. [4]

## 260921-ICR-L32 The Taskless Seat Set Gains The Curator

The shared task-binding admission now admits a **document-less curator session**: `TASKLESS_SEAT_ROLES` is
`{chat, terminal, bootstrap, curator}` on the developer's 2026-09-24 ruling, so a session opened for the
curator with no task document receives the curator's capsule (`free-agent:curator`) instead of `400
task-binding-required`. Everything else about the gate is unchanged — the structural altitude check still
does not run for a taskless role, a supplied document is still resolved and still refused when bad, and every
other role still takes the structural path — and the second reader of the set
(`serving/terminal_task_assignment.py`) reads the same constant rather than restating it.
`mcp/tests/test_memory_branch_authority.py`'s pinning assertions were updated with the constant, and a
route-level case pins the five-arm status table so the admission is held by behaviour and not by the constant
alone.

## ARSPAWN-L5 A005 Shared Task-Binding Admission

`task_binding.py` is the one preflight for canonical document resolution, role altitude, current
source lineage, and generation-bound reviewer parent. The plane-private spawn application invokes
it before settings resolution; `terminal_opener.py` invokes the same API at the final pre-host seam.
This ordering keeps stale-lineage recovery actionable and prevents a launch-selection refusal from
hiding a malformed structural claim. There is no filename, settings, or compatibility fallback.

## ARSPAWN-L5 Real Role Startup And Headless Delivery

Codex role seats now remain in startup until the native app-server reports one connected configured
MCP server advertising exact `dispatch_agent`. The shared readiness parser owns pagination, status,
tool shape, settled absence, and timeout; the adapter has no alternate tool-name or discovery
fallback. Dispatch briefs allow one bounded spawn-to-bridge convergence window without creating a
second caller attempt. Agent-notifier sweeps refresh canonical terminal liveness themselves, so
queued brief/message progress does not accidentally depend on dashboard browser polling; the serving
lifespan is now the steady-state owner of that refresh, so notifier enablement is no longer part of
the observation contract (see *Current Terminal-Observation Ownership*). Control
socket diagnostics distinguish absent, refused, and timed-out endpoints without claiming process
death from socket state alone.

## ARSPAWN-L4 Shared Candidate Identity

`build_info.process_serving_build()` now owns one cached identity for the Python process and feeds
both dashboard serving composition and MCP `server_info`. In addition to version/boot/checkout
facts, the stamp content-addresses sorted importable Python source and names the exact interpreter
and package root. This distinguishes equal-version or dirty candidates without making paths part of
the content digest. `models/core.py` is the one strict wire authority; served state only
composes it and MCP only projects it.

This identity is diagnostic and acceptance evidence, not package-update policy. Production starter
registrations continue to launch `uvx --refresh-package agents-remember-mcp
agents-remember-mcp@latest`; the disposable ARSPAWN acceptance runner launches exact local source
only so it cannot accidentally certify a stale published artifact.

## 260915-CAPS-L5 Codex Capsule Delivery

> **Superseded in part by `260915-CAPS-L15` (see the L15 section).** The chain below is still exactly
> right, but the field it starts from is no longer the only source: the launch point now resolves the
> capsule and the opener reads `TerminalLaunchRequest.capsule` first, falling back to
> `launch.control.capsule_delivery` (L5's own caller seam) second. L5's two invariants and its declared
> limits stand unchanged.

**One new route member and five touched ones, and the capsule is a value the whole way.** The new
module is `capsule_delivery.py`: the delivery value type (`CodexCapsuleDelivery` over a
`CapsuleBindingIdentity`), the refresh decision (`plan_refresh`), and the legacy-chain switch
(`legacy_instruction_switch`). It sits at `serving` rank deliberately — the compiler (L2) and the
admission surface (L4) rank **above** `serving`, so the capsule arrives as an admitted value this rank
may consume but must not import. It defines what the seam consumes over `models`-rank imports only.

The carrier chain, which is the route-level fact:

```
TerminalLaunchRequest.control.capsule_delivery   terminal_opener.py (caller-facing field)
  -> RunnerConfig.capsule_delivery               harness_control_runner.py
  -> payload key "capsuleDelivery"               ONLY when a capsule is present
  -> parse_runner_config                         (malformed value REFUSES)
  -> both factory calls in _prepare_controlled_launch
  -> create_harness_protocol_adapter(capsule_delivery=...)
  -> CodexAppServerSettings.capsule_delivery     codex_app_server_session.py
```

Two invariants of this route must survive any later edit, and both are measured rather than asserted:

1. **The capsule-free wire is byte-identical to base.** The payload key is *omitted*, not null: the
   base module and the candidate module produce the same eight keys, the same 344-character encoded
   token and the same token sha256. Anything that makes the key unconditional breaks every existing
   launch path.
2. **A malformed or channel-less capsule refuses.** `_optional_capsule_delivery` raises rather than
   dropping it, and `_require_capsule_channel` refuses a capsule for any harness other than `codex`.
   A caller that asked for a capsule must never receive a capsule-free process.

**Lifetime.** The installed app-server (measured `codex-cli 0.151.0`) exposes instruction fields on
`thread/start`, `thread/resume` and `thread/fork` and **none** on `turn/start`, so an ordinary message
cannot re-apply the role corpus. The seam therefore applies one capsule per admitted binding at a
thread-open boundary, re-states identical bytes on the same digest, and for a changed revision opens a
bounded fresh thread (or a fork when the caller offers one) instead of stacking a second revision — an
unsupported refresh is reported through the plan's reason, never faked. The host's own
`instructionSources` list is published verbatim as observation, and the legacy startup chain is
suppressed per launch through the existing thread `config` key `project_doc_max_bytes: 0`.

**Declared limits on this route, stated as limits.** The vendor-side effect of re-sending
`developerInstructions` on `thread/resume` is unmeasured (0.151.0 persists no rollout until a real turn
runs), so `IN_PLACE` is schema- and unit-proven only; `FORK_THREAD` has no production caller; no live
spawn through `terminal_opener` was exercised; and the delivered payload is bounded by nothing here —
the largest shipped capsule measures **120,536 chars, 92.0 % of Linux `MAX_ARG_STRLEN` (131,072)** with
~10 KB headroom, and past that the spawn fails with `E2BIG` before any AR surface can report it
(defect `D12`, routed to the final-verification leaf with a required bound and pre-encoding refusal).

## 260915-CAPS-L15 The Launch Paths Compile And Supply The Capsule

**Route meaning changed for the whole launch path, and this section is the current account of it.**
Before this change set, the capsule chain was built and individually proven at every link — the
compiler (L2), the admission/MCP surface (L4), the Codex instruction seam (L5), the eve carrier (L7) —
and **no production launch point supplied a capsule to any session**. A dispatched seat and a free
agent both launched with no instructions at all, and every green test hand-supplied the intermediate
value, which is why no leaf's suite could see the gap.

**One decision point, three answers.** `serving/launch_capsule.py` is new and is the only place a
launch decides its instruction mode: `capsule` | `legacy` | `refused`. Every launch point calls
`resolve_launch_capsule` **before any host side effect**; the compile itself crosses an injected port
(`LaunchCapsuleResolver`, filled by `cli/dashboard.py::serving_collaborators`) because `serving` ranks
below `application` in `layers.toml` and may not import the compiler. A second place that decides a mode
is the severed chain again, one level up.

**One workspace authority, and it is read out of the artifact.** A launch whose capsule admits a
workspace runs **there**: `session_workspace(capsule, server_workspace=…)` is the single rule and
`selection_for_workspace` moves the settings selection's workspace to match, because
`harness_control_runner.py:175` refuses a launch whose selection names another workspace. The value
itself is read back out of the carrier the consumer re-verifies
(`application/role_capsules/launch.py::_compile_eve_task` →
`LaunchCapsule.session_workspace`), so the session cwd, `ResolvedLaunch.workspace` and the child's
`AR_WORKSPACE_ROOT` are **one value by construction** rather than three that have to agree. Only an eve
carrier admits a workspace; the Codex instruction carrier has none, so **no Codex launch's cwd moves**,
and free agents and legacy launches keep `config.workspace_root` unchanged.

**The three production launch points, per point:**

| # | Launch point | State after this change |
| --- | --- | --- |
| 1 | `application/terminal_tools.py::_spawn_launch_request` (the primitive `dispatch_agent` drives) | **wired** — resolves the capsule before any host side effect, passes it on the request, publishes `instructionMode`; refuses `capsule-unavailable` **by name** |
| 2 | `serving/_app_terminal_routes.py::_open_terminal_response` (the dashboard opener — the only production point that starts a **free agent**) | **wired** — same gate through the port; refusal is HTTP 400 `capsule-unavailable`; the per-run record rides the response |
| 3 | `serving/conversation/library/open_service.py` (the conversation-library reopen) | **declared-excluded** — `LIBRARY_REOPEN_LEGACY_REASON`; see that card. Owner of any future capsule-carrying reopen: the final-verification leaf, with the thread-lifecycle leaves |

**What each harness receives, and through its own chain.** `codex` gets the capsule on the app-server's
own `developerInstructions` field: `LaunchCapsule.codex_delivery` →
`terminal_opener._codex_capsule_delivery` → `RunnerConfig.capsule_delivery` → the conditionally emitted
`capsuleDelivery` payload key → the adapter settings (**L5's chain, unchanged**). `eve` gets it as the
launch environment its runtime verifies per request (`LaunchCapsule.eve_env` →
`terminal_opener._eve_capsule_env` → the child environment → `launch_spec_binding` →
`verify_capsule_binding` → the runtime's own gate). **The Codex field stays `None` for eve**, so
`harness_control_factories.py:113`'s codex-only guard was *not* relaxed — the boundary is real, and no
change to it was needed. Any other harness (`claude`, `pi`, a settings-defined id) has **no verified
channel** and runs the legacy chain **by declared decision**, with the reason recorded per run.

**The acceptance evidence is the consumer's own first prompt.** A task-attached seat and a free agent
were each started through a production launch point, the runner argv the launch point itself built was
parsed back out of the base64 the child would exec, and the capsule was read from the `thread/start`
request the session sent to the vendor boundary — compared against the compiler's own result, never a
hand-built expectation (`mcp/tests/test_capsule_launch_wiring.py`). For eve, the launch point's own
captured cwd **and** env were fed to the consumer's own gate (`launch_spec_binding` →
`verify_capsule_binding` → **ACCEPTED**) and a live eve runtime started from those same values carries the
carrier block and its semantic digest in its own system block
(`notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt`).

## 260915-CAPS-L17 The settings-chain eve Seat Dispatches, And The Route Exclusion Is Declared

**The limitation this route carried is now closed for the seat path.** The section above recorded that a
role-configured eve seat could not be dispatched: the capsule gate passed and the **next** refusal was
inherited and downstream, because `application/terminal_tools.py::_resolve_harness_dispatch` requires
model **and** effort from the settings chain while eve's honest capability catalogue advertised no
launch-settable effort (`supports_effort=False`). That was defect **D22**, developer ruling route
**(A)**. This leaf discharges it by making the capability real rather than by relaxing the gate that
noticed its absence: the pinned application now consumes `AR_EVE_EFFORT` through eve's own
`defineAgent({ reasoning })`, and `serving/eve_adapter.py::_capability_snapshot` therefore publishes the
effort axis with its default. A settings file naming harness `eve`, a model and an effort for a role now
resolves through the real dispatch, the runner's PREPARE accepts, the adapter starts the pinned runtime,
and the model request the runtime issues carries the configured level — read at the provider boundary,
in the request body a recording provider received, **not** asserted from the catalogue
(`notes/reports/260915-CAPS-L17-evidence/s2-*-provider-requests.jsonl`; the settings-chain launch is
`s5-settings-chain.json`).

**No file in this chain moved, and that is the point.** `serving/harness_launch.py`,
`application/terminal_tools.py` and `serving/_app_terminal_routes.py` are **unchanged** by this leaf;
what changed is that the catalogue stopped refusing, so `validate_launch_selection` now has a
launch-settable effort to validate against instead of an empty menu. `harness_launch.py`'s
settings-chain policy and this route's capsule gate are the same code they were.

**The dashboard route's inability to start the *shipped* eve row is a declared, owned limitation, not
a repair.** The route deliberately never sets `TerminalLaunchRequest.session_backend`, so
`resolve_terminal_launch` asks the terminal-program question, and eve's runtime is the AR-owned
application the session adapter starts itself rather than a `PATH` program. Four requests through the
real dashboard app measure the outcome exactly (`notes/reports/260915-CAPS-L17-evidence/s6-s7.json`):

| Case | Answer |
| --- | --- |
| shipped row, role-configured open | **400 `capsule-unavailable`** at the eve carrier gate |
| shipped row, roleless open | **400 `bad-kind`**, naming the terminal-program decision |
| operator-taught row (`orchestration.harnesses.eve` naming a real PATH program), role-configured open | **400 `capsule-unavailable`** at the same gate |
| operator-taught row, roleless open | **200 `running`**, `instructionMode: legacy` |

**Reason:** an adapter-owned harness has nothing for this route to exec; the caller that asks for a
session backend is `application/terminal_tools.py` (`session_backend=True`, :765) and this route
deliberately does not. **The last row is the hazard and is named rather than smoothed:** an
operator-taught PATH row makes a roleless open return a green `running` session with `legacy`
instructions — an `eve` session that is **not** the AR runtime. That is the pre-existing teach-a-TUI
feature, and it is the one route by which the dashboard reports success for `eve` while nothing
adapter-owned runs. **Owner: the serving/route surface — whichever leaf next owns
`serving/_app_terminal_routes.py`** — carried in the master's obligation ledger by the
final-verification leaf. Product pin:
`mcp/tests/test_eve_product_integration.py::EveTerminalLaunchTests::test_the_declared_exclusion_belongs_to_the_route_and_is_owned`.

**Behaviour 6 — the legacy path — is measured, not asserted.** Three legacy launch shapes (no role, a
`chat` seat, a worker on `claude`) are **byte-identical** on both trees: the capsule-free payload is the
same eight keys, no `capsuleDelivery` key appears, and diffing the two transcripts is empty.

- The one decision point: three modes, the legacy-by-declaration reasons, the named refusals, and the no-resolver refusal. [9]
- The one workspace rule and the selection that follows it. [10]
- The runner's own agreement check, which makes the rule product-enforced rather than test-enforced. [11]
- The two channels that exist, named as the only two. [12]
- The compiler behind the port, and the workspace read back out of the carrier the consumer re-verifies. [13]
- The opener's two carrier readers, and the defensive refusal beside them. [14]
- The codex-only guard that stayed untouched, because the eve carrier does not use the Codex field. [15]
- The enumeration guard: every `TerminalLaunchRequest(` site is wired or declares its legacy chain, and the set cannot change silently. [16]
- The declared legacy exclusion, with its reason. [17]
- The two acceptance transcripts read from each started session's own first prompt, and the production-chain eve case. [18]
- The production-chain evidence: the consumer's own gate from the launch point's own cwd and env, the live system-block read, and the negative control. [19]
- The two limitations, with their owner and the evidence that measures them. [20]

## Completion-paced live background work

The existing watcher explicitly registers native events on supported local roots. The existing live pacer applies completion-relative bounded rest while retaining domains through work/rest/failure; the projector reports real completed/drained ticks. Landing observation remains its own projection owner and excludes recurring terminal history. The rest cap is additional scheduler time, not total freshness. Publication/subscription, stable deltas, observer/session ownership and watcherless replay remain with their established owners.

## Purpose

### 260731-EFA-L23 Route Delta

L23 adds batched notifier expiry writes, product-agnostic Codex initialize diagnostics, lifecycle-operation projection on enclosures, and volatile elapsed-time stripping. Durable task state remains the authority; no private operation identity crosses the serving boundary.

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

The original `serving/conversation/` contract-only leaf established the protocol-neutral roof for the
Chats interface. Its initial state is recorded in this paragraph; the production children below supersede the empty-router state. Strict Pydantic wire models normalize harness identity, active transcript/event
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
and correlated adapter acceptance at a turn boundary is acknowledgement/landing authority. Model
`consume` is optional attribution with no mechanical effect. Pane text, terminal logs, copy mode,
paste echoes, and timing windows are diagnostic-only and cannot authorize readiness, delivery,
completion, or supervisor action. Older pane/log/paste descriptions retained below are semantic
history, not current authority.

### Current Structural Seat And Routing Contract

Hosted-seat identity is the real task document plus role: sprint roles bind the sprint document,
manager binds the master, and worker/reviewer/curator bind leaves. `ambient_seat.py` proves callers
from plane-seeded hosted context and — since 260821-ARSPAWN-L1 — resolves the ambient launcher (a
process with no `AR_HOSTED_SESSION_ID`) as a typed `AmbientCaller` for `dispatch_agent`;
`structural_seats.py` qualifies parent/child relations and singular current occupants. Spawn
provenance now includes caller kind (`spawned_by_kind`, written when set), mapped write-once onto
the catalog row by `terminal_opener._opened_catalog_entry` via `_preserved` and surfaced on the
spawn wire as `spawnedByKind`. `terminal_task_assignment.py` is the one level-neutral binding primitive. Ordinary
inbox traffic is persisted, then re-resolved at post and delivery time so replacement is transparent;
the initial dispatch brief alone stays exact-pinned internally. One-way startup migrations run before
strict catalog/control-plane readers; no dual-schema compatibility reader remains. Agent-notifier
predicate helpers consume the existing `TaskHierarchy` protocol, while production constructs the
filesystem-backed `TaskDocumentTopology`; this preserves one hierarchy authority without forcing
callers to depend on its concrete implementation.

State-signal actions revalidate the subject's current task-document binding and derive the structural
owner immediately before posting. A role/document address without a current occupant is left
eligible for a later sweep and cannot create a durable row or emitted marker; a typed task-document
refusal fences only that subject so unrelated findings continue. The canonical structural owner and
shared delivery path remain the authorities for replacement, ambiguity, and boundary handling.

Boundary handling is now explicit at the drain gate: `state_signals.evaluate_boundary_drain_findings`
admits a pending row at its target's turn boundary only when `_boundary_follows_last_attempt` says
that boundary follows the row's last recorded attempt, and a row carrying *no* attempt clock is
admitted only for a `state-signal` row. That is exactly the state a replacement occupant creates,
because rebinding a held signal restarts its attempt clock while the generic redelivery path keeps
suppressing it as a held signal; without the state-signal-scoped admission such a row had no
delivery path at all. Every other row kind keeps the ordinary redelivery path, and an unparseable
attempt clock is still refused.

State signals now carry an explicit durable order — row persisted, marker stamped, delivery
attempted — enforced at the posting primitive rather than by the emitter's call sequence.
`owner_signals._post_owner_signal` runs `OwnerSignalOptions.after_persist` after the row is durable
and on the sweep fold and strictly before `deliver_inbox_entry`, and `_emit_state_signal` is its only
supplier today (it stamps `state_signal_emitted_for` there instead of after the post returns), so a
failed marker write leaves one pending unmarked row and makes zero adapter submissions. Delivery
eligibility is re-checked at the shared action: `_agent_notifier_actions._state_signal_awaits_marker`
refuses a pending state-signal row whose own seat still reports that row's evidence without the
marker, and `_drain_boundary` inherits the guard by delegating to `_redeliver`. Predicate order is
therefore not what protects the row — the boundary-drain finder reaches the shared action without the
held-on-boundary filter the generic finder applies. Coalescing follows the same source identity: a
`state-signal` row renews on the exact `subjectAgentId` plus the normalized ask, so an R08 rebind
renews and re-addresses that row while two replacement seats never renew each other; every other kind
keeps the structural task-document + role key.

**`HarnessSubmissionAuthority` is the sole epoch-bound prompt/setter
timeline.** It owns prompt FIFO, immutable id/source/payload admission, atomic queued-withdraw versus
dispatch claim, exact full-operation-ref completion, early-terminal dominance, response bypass,
raw-free cockpit status, and bounded privacy-aware retention. `HarnessControlQueue` no longer exists:
260731-EFA-L6 deleted the compatibility facade outright, so the authority is reached directly.
Codex, Claude, and Pi are dispatch-now adapters with guarded first-byte seams;
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

### Current Terminal-Observation Ownership

Terminal catalog observation is a serving-lifespan responsibility, not a request-driven side effect.
`_app_lifespan.py::_terminal_observation_loop` is the route's one steady-state owner: it calls the
existing `TerminalCatalogLivenessSweeper.refresh` through the drained off-loop helper and sleeps
`DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` only after each attempt returns, so the cadence is
completion-relative and non-overlapping, and a closed dashboard, a headless process, a model turn, or
a disabled agent notifier cannot stop catalog turn truth from advancing. The notifier's own inline
refresh remains a consumer of the same sweeper and is not the ownership contract. The
terminal-session GET route is **projection-only and names no sweeper at all** — it serializes the
current catalog snapshot and cannot itself make that snapshot newer — so it is not a consumer of
this clock either (`LOCR-R02@v1`). The sweeper's starting-row and full-sweep clocks stay inside the
sweeper.

Steady state is not the whole contract: the same file also takes **one pre-serve observation prime**
(`_app_lifespan.py::_prime_terminal_observation`, `LOCR-R18@v1`). The lifespan order is migrate → compact → **start the serving-lifetime observer-health accumulator and attempt its initial record** → one contained observation prime → `runtime.projector.prime()` → create the recurring loops
→ yield, so the initial projection and the first notifier sweep read a catalog a canonical pass has
already committed rather than depending on the first scheduled tick or on a request. The prime is the
same canonical sweeper entry point as every later pass — no startup-only reader, cursor, or catalog
mutation — and it is a due full sweep, not an extra one. Its `except Exception` containment is the
requirement and not a defect: a recoverable observation failure must not become a serving outage, so
the projection prime and every recurring loop still start and the steady-state owner retries on its
first cadence, while `CancelledError` still propagates into the shutdown drain. The prime now also PUBLISHES: every completed observation attempt — the prime's included, with
`phase="startup"` — records the observer stage's own health through
`terminal_observer_health.py` (`LOCR-R17@v1`), so the earlier statement that this route defines no
health surface for a prime outcome is superseded. What stands is the boundary: this route owns the
observer's own reading and no readiness gate, cursor, queue or task-authoring authority derives from
it, and the read routes never rewrite the record. One limit is still recorded rather than implied: the
delivered ordering witness does not constrain prime-versus-migration/compaction — that edge rests on the production straight-line order.

### Historical Slice-04 Through HFX Serving Account

The following migration account predates the current protocol-owned hosted and conversation paths above. Its pane/log delivery and transport-only framing are history, not current authority.

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
lists. `terminal_task_assignment.py` is the shared level-neutral binding primitive used by operator
APIs and internal structural dispatch. `TaskDocumentTopology` validates real sprint/master/leaf
documents; no leaf-normalization adapter or role-anchor leaf remains. `terminal_opener.py` is the
shared hosted-occupant opener that both the operator route and structural dispatch compose over, so
there is no parallel spawn path — and `terminal_paste.py`, the server-side capture-verified stdin
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
third decoupled-cadence lifespan task (`supervisor.py::run_agent_notifier_sweep`, default ~10s,
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
`settings.supervisor.signal_cooldown_seconds` into `AgentNotifierContext`; `inbox_delivery.py` threads
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

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

Serving composes the dashboard application, hosted-session control, projections and notifier. Start at `app.py` for route/lifespan composition, `projector.py` for atomic snapshots and cancellation draining, and `change_watcher.py` for change-or-heartbeat pacing. Watcher lockfile exclusion derives from `kernel.file_lock.lock_path_for` and filters every watched directory; moving this import does not alter suffix, debounce or wake behavior. The host registry and coordinator retain separate policies above that shared kernel mechanism.

## Serving Operating Context

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

The catalog terminal-evidence lift is a consumer of that bounded substrate:
`terminal_evidence.py::_validated_evidence_cursor` validates the deque envelope before
`latest_terminal_evidence` maps frames, rejects unsupported projectors before reading, and
advances truncated pages only through the last returned sequence. Its Pi path remains bounded
at 200 entries per page and eight pages per sweep; `test_terminal_evidence_cursors.py` retains
the focused cursor, refusal, continuation, and liveness-containment checks. This lift does not
add a history fallback or alter the canonical projector owners.

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

The original contract-only leaf established structure before live endpoints: consumers validate hostile
normalized products through `conversation/models.py`; the now-implemented active and library services
satisfy their separate read ports and cursor purposes; mutations stay on the control
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
own-adapter port, serialized with prompt submission through `HarnessSubmissionAuthority`
(until 260731-EFA-L6 this was reached through the `HarnessControlQueue` facade, now deleted).
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

Claude, Codex, Pi, and eve built-ins negotiate the structured fields their adapters
consume; exact package versions are fixture/smoke evidence only. Rolling inbox compatibility is
limited to optional `adapterDeliveryState` and `adapterDeliveryDetail`, and cutover reloads the
daemon, every MCP-owning client, per-session runners/adapters, and browser tabs. Resource
performance work remains queued.

Codex parent terminal completion carries the durable operation id as protocol `requestId` and the
native turn id as vendor correlation. The direct id lets an initially queued receipt converge onto
its exact inbox row when the turn completes. A terminal record that legitimately has a null
`requestId` is resolved only through its text vendor correlation on exactly one accepted inbox row
for the same hosted session; missing, non-text, unmatched, or ambiguous correlation fails loudly.
Completion projects onto that same row as adapter delivery metadata while explicit inbox state
remains `pending` and unconsumed. With no actual queued replacement the adapter reports `idle` /
`immediate`; `settling` / `queued` means a replacement is actually queued. This is protocol-owned
structured behavior, not fixture-version, parser, pane, or resource-performance behavior.

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

The superseded pre-protocol delivery implementation used harness JSONL as submitted-delivery authority across spawn, inbox,
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

Task-document snapshot serving now carries the compact execution-topology facts needed by the
dashboard: a commanded master's optional nature, a sprint's canonical graph, and deterministic
derived waves. The serving route copies validated task authority; it does not choose priorities or
invent graph positions.

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
loop it already owns. **Since 260731-EFA-L5 that one loop is also the declared compaction owner of
both provider stores** (`PROVIDER_METRICS_OWNERSHIP`, `PROVIDER_DEGRADATION_OWNERSHIP`, both
`compaction_owner="dashboard"`): `_metrics_loop` calls `metrics_store.record`,
`evaluate_provider_degradation` and `metrics_store.compact` on one tick, and the ownership is
enforced *structurally* — each reclaim has exactly one caller and it is inside this loop. Neither
store earned the operator-inbox's `compaction_owner=None` exception, because nothing in the MCP
process removes a provider row, so a single owner was available and the contract requires one where
it is. The route consequence to remember: the reclaim of both provider logs now follows this loop's
30s cadence and nothing else, and every write on this path holds its log's lock. `GET /api/stream` consumes one atomic projector subscription: it emits the
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
- `harness_submission_ledger.py` — `OperationRecord` and `SubmissionLedger`: enrolment, retention,
  eviction (`make_room`) and the paged never-bodies `operation_timeline`, split out of the authority
  in 260731-EFA-L6.

- `harness_capabilities.py` and `harness_control_adapter.py` — the normalized capability contract:
  `CapabilitySnapshot` contains dynamic `ModelCapability` rows with model-local `EffortOption`
  menus; ACP Sense 1 projects category-keyed select options; `LaunchKnobs` includes adapter-owned
  selectors and `SetResult` establishes the setter evidence boundary. The combined launchable adapter
  seam joins synchronous cached advertise, transient native discovery, and native launch knobs. No
  ACP transport, global effort enum, or composer-paste fallback belongs in this port.
  `BUILTIN_PROTOCOL_HARNESSES` names four ids (`claude`, `codex`, `pi`, `eve`); this is the
  **protocol-adapter** registry and it is deliberately separate from the kernel's developer-curated
  terminal harness set, which still carries no `eve` row.

- `eve_adapter.py` with `eve_events.py`, `eve_protocol.py`, `eve_stream_cursor.py`,
  `eve_interactions.py`, `eve_runtime_client.py` and `eve_runtime_launch.py` — the native eve
  session adapter (260915-CAPS-L6), and the only built-in whose native process is an **AR-owned
  application** rather than a `PATH` command. It speaks eve's documented HTTP session protocol
  exclusively: health-derived readiness, a durable session id bound to one bridge epoch, and the
  NDJSON event stream consumed on an **absolute event-index cursor** (`meta.id` deduplicates an
  overlapping replay but is never the resume position). Acceptance is reported separately from turn
  completion and from session retirement; ordinary deliveries are queued explicitly rather than
  inheriting eve's cancellation-backed `steer`; a lost submit response reconciles
  accepted/rejected/unresolved from durable evidence and is never repeated; `interrupt` is
  turn-addressed, replayed once per observed pair, and reports acceptance only because eve's cancel is
  cooperative and settles later on the stream. Session identity and the stream cursor are published on
  the existing `AdapterSnapshot` (`vendor_session_id`, `raw["streamCursor"]`), so no second
  orchestration registry exists. The adapter **carries** `AR_BINDING_REF` / `AR_CAPSULE_DIGEST` /
  `AR_WORKSPACE_ROOT` to the runtime but compiles and selects no capsule — that seam belongs to the
  capsule/workspace route — and its model/effort setters report `unsupported` honestly because eve's
  model is a compiled application value. The controlled application itself lives in the repo-root
  `eve_runtime/` tree, which sits outside this route and outside the repository's onboarding
  `pathRules`.

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
  lets the native authenticated catalog choose its default without creating a second authority. Since
  260915-CAPS-L5 the same path also carries one optional admitted role capsule
  (`capsule_delivery`) from the launch boundary to the adapter settings, through a payload key that is
  emitted **only** when a capsule is present — so a capsule-free launch is byte-identical to base — and
  the factory refuses a capsule for any harness without a verified instruction channel. The
  resolved-selection factory call now passes its selection as one `LaunchSelection` pair, a
  no-exemption answer to `PLR0913` rather than a behaviour change.

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
  readiness; later turns reuse the resolved effort. Initialize identity accepts a product-agnostic
  server-product/version followed by optional diagnostics ending in the exact clientInfo name/version suffix, while the
  primary product version must still agree with thread evidence. When a role capsule is delivered
  (260915-CAPS-L5), this session occupies the schema-supported `developerInstructions` field at the
  thread-open boundary only — there is no turn-level instruction field — compares the **recorded**
  binding identity and semantic digest before re-stating identical bytes, drops `threadId` and opens a
  bounded fresh thread for a changed revision or an unknown one, publishes the host's own
  `instructionSources` verbatim, and suppresses the host's project-document load per launch through
  `project_doc_max_bytes: 0`. A capsule-free open is unchanged.

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
  answers "does this session exist" alone, and a row read against the wrong host is
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
  (the task-binding + `host.ensure` + catalog-upsert composition delegates to the
  shared `terminal_opener.open_terminal_session` — `resolve_terminal_launch` / `_terminal_label` / the
  role-scoped conflict check all left `app.py` for that module — so operator opening and structural
  dispatch use one opener; it accepts optional `model`/`effort`, requires a complete pair for
  built-in native harnesses, and maps `bad-kind`→400 / `seat-taken`→409 /
  `launch-conflict`→409 / `opened`→200. Successful and conflicting responses report the actual
  retained row's launch/control facts rather than echoing the attempted request. Server-resolved
  harness id, never argv on the wire; the opener passes `suspend_unsafe=(kind=="harness")` so
  later host writes strip Ctrl-Z for bare-pane harnesses and persists a `TerminalCatalogEntry`
  carrying occupant/launch facts plus `taskDocumentRef`, `seatRole`, replacement declaration, and
  spawn provenance without opening a starter PTY client; uniqueness is per task-document-and-role
  seat, with topology/altitude validation before persistence),
  `POST /api/terminal/{session}/paste` (server-side capture-verified
  context-packet delivery to a hosted session with no attached browser client, over
  `terminal_paste.TerminalPaster`; delivery is confirmed against the pre-delivery origin capture —
  a new chip in either harness vocabulary or the payload head, not mere pane output; 404 on
  unknown/gone session, else `{delivered, submitted}` plus the pane `capture` on an unconfirmed
  outcome),
  `POST /api/terminal/{session}/attach-task` (validate the canonical task document and role, then
  claim or move the structural binding for an existing session without respawn; delegates to
  `terminal_task_assignment.assign_terminal_session_to_task`, returning typed invalid/taken/unknown
  refusals without mutation or the accepted binding), `GET
  /api/terminal/sessions` (a PROJECTION of stored state only: it serializes
  `runtime.catalog.list()` through `_catalog_payload` and cannot itself make that snapshot newer —
  no sweep, no adapter probe, no evidence-cursor advance, no row mutation, no compaction, and the
  module names no sweeper at all. Observation is the serving lifespan's own clock, so a caller may
  observe a snapshot between two background ticks and a closed dashboard, a headless process, or a
  disabled notifier cannot stop turn truth from advancing. `list()` rather than `list_committed()`
  because a request thread waits for an in-flight batch on the catalog `RLock` and then reads
  committed bytes, whereas `list_committed()` is the sweeper's own non-blocking contention read and
  can serve a demonstrably older snapshot; the resulting wait is bounded, lands on a threadpool
  worker because the handler is a plain `def`, never the event loop, and is strictly smaller than
  the full inline sweep it replaced; WebSocket attach + the paste
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
  projection's own outputs, workspace non-input churn, and — since 260731-EFA-L5 — **every
  control-plane lockfile by suffix in every watched directory**, through
  `_DURABLE_LOG_LOCK_SUFFIX`, which is *derived* from `kernel.file_lock.lock_path_for`
  rather than spelled out: the old literal `operator-inbox.lock` had stopped matching once the
  lock naming moved to `operator-inbox.jsonl.lock`, and a workspace-scoped basename list could
  never have covered the per-lifecycle `gates.jsonl.lock` at all. These are the busiest writes in
  the watched tree — every durable-store append and rewrite opens one `a+b` — and none is a
  projection input),
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
- `response_contract.py` — the **declared HTTP wire** (260731-EFA-L4): `WireResponse`
  (strict/frozen/camel-aliased, `populate_by_name`) and the declared model classes covering every route's
  success and refusal shapes, plus three shared `responses=` tables — `SCOPED_READ_RESPONSES`
  (the files/notes/change-set family), `SESSION_CONTROL_RESPONSES` (every `harness_control_api`
  route) and `ACTION_RESPONSES`. Declared here; the former response-conformance suite was retired. FastAPI validates only the two routes
  that return a bare `dict`; see the 260731-EFA-L4 route impact for the exact boundary. Deliberately
  free of any `serving.conversation` import so the response-contract module can load independently of conversation composition. The requirement additions declare packet/list/content responses; returning a Response object bypasses automatic response-model serialization; the declaration alone does not prove conformance.

## L23 Structural Host Boundary

Serving resolves lineage after task-role validation and before host creation or
catalog mutation. Open/attach HTTP routes publish stale/unavailable refusals as
409 with strict evidence, while projector shutdown now drains any in-flight
filesystem tick before temporary worktree cleanup.

## R44 Metrics Shutdown Drain

The metrics background loop now shields and drains each blocking worker-thread operation before
propagating lifespan cancellation. Shutdown therefore cannot finish while sampling, record,
degradation evaluation, or compaction can still mutate provider metrics state.

## 260815-DAG-L14 Serving Route

The served task-document projection carries sprint `seats` and typed `masterRef` rows; the body
revision covers `subTasks` + `seats` so an open sprint reader refetches on linkage/seat edits.


## 260815-DAG-L12 Route Impact

The task-documents projection readers now wire the render-ready sprint graph view (L12-R4): `_task_documents.py` builds the `executionGraphView` through the `_execution_graph_view` serving seam (tasks-domain walk feeding the primitives-only builder) with the `_master_docs_by_ref` join table, and splits `_task_doc_node` into `_reader_fields` + `_execution_graph_fields`. The dashboard renders projected facts verbatim.


## 260815-DAG Master Full-Gate Repair Route Impact

Serving projection/snapshot modules updated their imports to the moved `worktrees/queue/*` and `models/queue/*` locations.

## 260821-CLIVE Serving Route Impact

Serving now preserves leaf execution evidence before bounded retention can reclaim its source row.
The app composes explicit terminal-catalog and operator-inbox registrars. Terminal liveness releases
its catalog batch before registering terminated worker/reviewer/curator rows in task truth, then
compacts only ids the registrar confirms. The notifier likewise registers its inbox snapshot before
reconcile-and-compact. Missing registrars authorize no task-bound deletion; they do not activate a
secondary evidence reader or compatibility route.

The serving projection is also aligned with final scheduling ownership. `_closeout_queue.py` reads
the source-fingerprinted disposable projection and exposes invalid-empty/valid-built condition,
bounded source problems, and waiting-generation members—never claims, blockers, commits, or
certification. `_task_documents.py` projects audited discarded-unstarted subtasks as persistent task
history and includes them in body revision identity.

## 2026-08-26 Projection Retry Reconciliation

The serving projection input state now publishes task-domain snapshots atomically. A failed task
refresh retains the last good contracts, enclosures, task documents, and series, marks the task
refresh pending, and forces a later heartbeat to retry even when no new task-domain change signal
arrives. This keeps transient read failures from poisoning the live dashboard projection or
requiring an unrelated filesystem event to recover.

## 260821-ARSPAWN-L2 Replacement-Safe Dispatch

`structural_dispatch.py` owns the bounded 4,096-stripe seat serializer and the durable
pinned-brief queries. Setup or `flock` failure is typed and fail-closed; there is no local-only
fallback, repository-global lock, or unlink race. Brief viability distinguishes a live or
retryable generation from superseded, unresolved, or expired evidence.

`DispatchBriefReceiptStore` owns dispatch-specific receipt mutation over the existing catalog
lock/read/write unit. This keeps commit-point evidence out of the general `TerminalCatalog` lifecycle
surface without adding a second persistence path or compatibility reader.

`structural_seats.py` resolves a canonical address independently of current occupancy and delegates
generation selection to `current_seat_occupant`. Inbox delivery resolves the occupant at delivery
time, while exact dispatch briefs remain pinned to the private spawned generation. This lets
ordinary messages survive vacancy and incumbent-to-heir replacement without exposing a session id.

## 260831-CCR-L23 Task-Local Requirements Routes

L23 registered the read-only task-local requirement surface: `serving/requirements.py`
walks one canonical `tasks/<repo>/<master>/requirements/` root selected by repository +
single-segment master + canonical task-document reference and serves the confined GET endpoints
`/api/requirements/{list,read}` with declared models (`RequirementsListing` /
`RequirementContents`) under the shared scoped-read refusal table. The route family grew
from 61 to 63 HTTP routes; composition adds one `register_requirements_routes(app, config)`
call in `create_app` after the notes routes and before the static mount.


## Evidence

### Shared Lock Owner References

The watcher keeps one naming dependency on the actual lock owner; it does not acquire coordinator authority or change projection input scope.

- The shared naming primitive appends the same physical lock suffix. [21]
- Every-directory filtering retains lock suffix exclusion. [22]

## 260915-CAPS-L7 The Eve Capsule Launch Proof

The eve adapter's route now **proves** the capsule binding it carries, before a process exists. This is
a route-meaning change for `eve_runtime_launch.py`: it was a pass-through for the binding's environment
values and is now an all-or-nothing admission gate.

- **`verify_capsule_binding` runs first in `resolve_runtime_spec`** — ahead of staging an application
  root or reserving a port — so a launch that cannot be bound correctly is never given a model. Six
  refusals each name a distinct defect: a partly declared binding (`AR_BINDING_REF`, `AR_CAPSULE_PATH`
  and `AR_CAPSULE_DIGEST` must arrive together), an unreadable carrier, a carrier whose bytes are not
  the declared digest, a carrier written for another binding, a carrier whose workspace is not this
  launch's workspace, and a workspace that is not the admitted git worktree.
- **An entirely undeclared binding stays unbound** and returns `None`. It is started without a binding
  and refused by the runtime's own session routes rather than executing without admitted instructions —
  the gate does not invent a default.
- **The workspace check reads git metadata, not the path.** `_require_admitted_git_worktree` requires
  `HEAD` to be the admitted work branch, or the admitted base commit when detached. A directory that
  exists at the admitted path is not the admitted worktree: a sibling task's checkout, a copied tree and
  a detached checkout all satisfy "the path exists" while executing somewhere nobody admitted.
- **Ambient binding names no longer survive into a child.** `build_runtime_env` pops `AR_BINDING_REF`,
  `AR_CAPSULE_PATH` and `AR_CAPSULE_DIGEST` alongside the existing `AR_EVE_RUNTIME_ROOT`/`AR_EVE_NODE`
  pops, because the runtime treats a complete set of those names as an admitted capsule. They are re-set
  strictly from the binding this launch declares, and `launch_spec_binding` reads **only** the launch
  spec — an ambient value in the server's own environment is not this launch's binding.
- **The session controls send no body.** `eve_runtime_client.py` gained `compact_session` and
  `clear_session`, both ID-addressed routes. They matter here because a cleared or compacted session
  does **not** rerun instruction resolvers, which is why the mandatory capsule is applied at the route
  gate in the system role rather than through a per-turn resolver.

The produce side of this seam is **not** in this route: it is
`application/eve_capsule/__init__.py::materialize_eve_binding`, and since `260915-CAPS-L15` it **has a
production caller** — `application/role_capsules/launch.py::_compile_eve_task` materializes the carrier
for a wired launch point (see the L15 section above). The `L7R-4` transfer that asked for that wiring is
discharged on the **produce** side ("the produce side has a production caller, verified at the
consumer's gate"); the **live-seat** half was open at L15's tip and is **closed by
`260915-CAPS-L17`** — see the `## 260915-CAPS-L17` section above, which records the settings-chain
launch and the provider-boundary measurement rather than the catalogue's word (D22, discharged by
L17).

- The launch-time proof, its six refusals and its unbound case. [23]
- The git-identity requirement that distinguishes the admitted worktree from a directory at the same path. [24]
- The ambient-binding pops and the launch-spec-only reader. [25]
- The two body-less session controls and the resolver-not-rerun fact behind the system-role choice. [26]
- The channel-level binder that refuses an unbound launch before any model work, guarding every session route. [27]
- The cases pinning the proof in both directions, including the wrong-branch workspace. [28]

## 260915-CAPS-L11 The Argv Bound Is Stated, Enforced, And Measured

`harness_control_runner.py` on this route now carries **D12's bound** as three constants and one
refusal, and the route's contract is that the check runs where the encoded token first exists —
**before any caller can spawn it**:

| Symbol | Value | What it is |
| --- | --- | --- |
| `MAX_ARGV_TOKEN_BYTES` | `131072` | Linux `MAX_ARG_STRLEN`, the limit on **one** `execve` argument |
| `ARGV_TOKEN_SAFETY_MARGIN_BYTES` | `2048` | the declared margin held under the kernel limit |
| `ARGV_TOKEN_BOUND_BYTES` | `129024` | the enforced bound = limit − margin |
| `_refuse_over_bound_token` | — | refuses by name, before any spawn |

**The whole launch configuration travels as one base64 token** (`argv[3]`), which is why
`MAX_ARG_STRLEN` — not `ARG_MAX`, which bounds argv and environment together — is the limit that
binds this mechanism. Past it `execve` fails with `E2BIG` **at spawn**, before this process can
report anything: otherwise AR-invisible, and indistinguishable from a runtime that crashed on start.

**The refusal names the measured size, the bound, the kernel limit it is derived from, and the seat
the capsule was compiled for**, because "the session did not start" is not an operator message. The
margin is deliberately small: the check measures the same byte string the kernel counts, so the
margin does not have to absorb an approximation, and a larger one would refuse capsules the kernel
accepts.

**Current width, and the reason the figure is a report rather than a guarantee.** The largest shipped
pair measures **126,096 B** with the settings-resolved launch a real launch always carries (2,928 B
under the bound; 126,352 B at the widest realistic shape, where an eve carrier binds the admitted
worktree to a 102-character cwd — 2,672 B under). At roughly 96 % of the limit the margin is thin,
and the route to the bound is a **path length** as much as a capsule: the token grows ~1.3320 encoded
bytes per `cwd` character — the base64 4/3 expansion, so it is the encoding's property rather than
this capsule's — first crossing the bound about 2,297 characters beyond the server workspace root.
**Any pair measured over 129024 is a bound re-derivation that stops the loop, never a silent
re-bound.**

## 260915-KS-L45 The Reviewer Serves Two Routes Over Two Ports

**Superseded count (`260921-ICR-L3`): the reviewer surface now serves three routes over three ports,
and it is no longer true that no route accepts a path.** This section records the two-route, two-port
landing as it was; every statement below about *counts* is superseded by the `260921-ICR-L3` section at
the end of this narrative, while the reasons it gives for the split — a second **path** rather than a
second adapter, and one application resolution behind both answers — remain current.

The reviewer surface is reached through **three GET routes**, and none of them is a mode of another:

| Route | Answers | Port | Inputs |
| --- | --- | --- | --- |
| `/api/review/intent` | what one comparison renders | `KnowledgeReviewPort` | task context + one recorded subject selector |
| `/api/review/intent/entries` | which subjects the resolved pair can be compared on | `KnowledgeReviewEntriesPort` | task context alone |
| `/api/review/intent/source-content` | one listed entry's actual content at the two bound code trees (added by `260921-ICR-L3`) | `ReviewSourceContentPort` | task context + the entry path + both bound code tree ids |
| `/api/review/intent/summary` | the comparison's changed-intent counts for the task entry (added by `260921-ICR-L47`; its own module `review_summary.py`; every typed state is a 200, unwired is a 503) | `ReviewIntentSummaryPort` | task context alone |

The split is a second **path** rather than a second adapter, and the source comment gives the reason:
a caller that had to guess a subject id to reach the comparison route would be choosing the candidate,
which the browser may not do. Both routes answer from **one application resolution** — the entry list
resolves through the identical operation the comparison uses — so the entry a task view is offered and
the review it then opens cannot name different candidates. The entry route is the only one a task view
can call *before* it knows a subject, which is why it takes the task context and nothing else.

The status idiom is now one mapping over three result types (`260921-ICR-L3` widened the union).
`_status_for` reads success as `refusal is None` rather than `state == "review"` — which is how an
`entries` state, a `review` state and a `content` state all serve `200` without a second local table —
and `subject_unresolved` joins
`candidate_unresolved`, `candidate_not_live` and `candidate_dataset_absent` among the codes that answer
`404`. The comparison route keeps its own `200`/`400`/`404`/`503` behaviour: `503` when no adapter is
wired into the process, `404` for a candidate that does not resolve, is not live, or has no dataset,
and `400` for a selector kind the surface does not admit.

**No adapter is a named refusal on all three routes, and neither the entry route nor the expansion
route may answer it with a list or with an empty file.** The comparison route's `503` says no review
adapter is wired and that the surface is not served rather than served empty. The entry route has its
own body (`_UNWIRED_ENTRIES`, `status: "unavailable"`, the same reason and next action) because an empty
entry list would say "nothing is reviewable here", which is a different fact from "this process cannot
answer", and only one of them is true when the process was composed without the port. The expansion
route's own body (`_UNWIRED_SOURCE_CONTENT`, added by `260921-ICR-L3`) is the same answer with the one
word that matters changed — **"not served rather than served as an empty file"** — because an empty
document would read as a file this repository does not hold.

The comparison route accepts no path, and the entry route takes the task context alone. The expansion
route (`260921-ICR-L3`) is the one that does: a **repository-relative entry path**, always sent with
both bound code tree ids, and read only if a **measured** change set lists it — the requested
generation's own, or, when that measurement is unavailable, the change set the leaf's review publishes.
It is not a filesystem path and no route accepts one, so the browser still cannot choose which dataset
or which repository is read. The comparison route's inputs are a repository, a master, a leaf id
and one recorded subject selector, with the selector kind closed at the two identity seeds the read
operation declares — `invariant` and `family`; every other seed kind addresses a revision, a membership
or a claim rather than a subject a curator reviews, so it is refused by name instead of being mapped
onto one of the two, and the refusal carries the offending input, the expected set and the next action.
That closure is what keeps the browser out of candidate selection: the resolution behind the ports
chooses which dataset is reviewed, and no route can be handed one.

Why ports rather than direct imports is a rank fact: `layers.toml` ranks `serving` below
`application`, so this module may not import the read, diff and view operations the reviewer composes.
It takes all three ports the way the launch route takes the capsule compiler, wired by the composition
root in `cli/dashboard.py`. Registration also carries an ordering constraint its siblings share — the routes
must be registered before the greedy static mount — and the module's own docstring records it,
alongside the statement that the registrar accepts the runtime config for symmetry and resolves nothing
from it.

- **The comparison route's handler over its injected port.** [29]
- **The entry route's handler: the task context alone, and an unwired process answered with a named refusal rather than an empty list.** [30]
- **The expansion route's handler and the module-level transport behind it (`260921-ICR-L3`).** [31]
- **The unwired-entry body: `unavailable` with the "not served rather than served empty" reason and next action — and, since `260921-ICR-L3`, its sibling for the expansion route.** [32]
- **The entry route constant, and the comment recording why it is a second path rather than a second adapter.** [33]
- The two admitted selector kinds, refused rather than mapped. [34]
- The query parser that admits only those two. [35]
- **The status mapping the routes inherit from the change-set routes: success is `refusal is None`, and the four candidate codes — including `subject_unresolved` — answer `404`.** [36]
- The refusal code a process with no adapter produces. [37]
- The 400 a selector kind outside the admitted set gets. [38]
- The 404 for a candidate that does not resolve. [39]
- **The registration that must precede the static mount and that takes all three ports.** [40]
- **The entry port type: the task context in, one typed entry result out — and, since `260921-ICR-L3`, the expansion port beside it.** [41]
- **The unwired-entry body: `unavailable` with the "not served rather than served empty" reason and next action.** [42]
- **The registration that must precede the static mount and that takes both ports.** [43]
- **The entry port type: the task context in, one typed entry result out.** [44]

## 260915-KS-L22 The Intent-Review Transport Over An Injected Port

The L22 section below records the comparison route as it was first shipped, with one route and one port.
The section above supersedes its count; the status idiom, the selector closure and the rank reason it
recorded are still right.

`serving/review.py` is this route's new shim, and it does transport only: it validates a query string,
builds the one typed request the composition consumes, calls the injected port, and maps the typed
result onto the change-set routes' own status idiom. `200` serves the review; `503` is returned when no
adapter is wired into the process, because the surface is not served rather than served empty; `404`
covers a candidate that does not resolve, is not live, or has no dataset; `400` covers a selector kind
the surface does not admit and the two path-shaped failures the port's call can raise. The value it
returns is the port's own typed result serialized once, through the model that declares its shape.

It accepts no path. The route's inputs are a repository, a master, a leaf id and one recorded subject
selector, and the selector kind is closed at the two identity seeds the read operation declares —
`invariant` and `family`. Every other seed kind addresses a revision, a membership or a claim rather
than a subject a curator reviews, so it is refused by name instead of being mapped onto one of the
two; the refusal carries the offending input, the expected set and the next action. That closure is
what keeps the browser out of candidate selection: the resolution behind the port chooses which
dataset is reviewed, and the route cannot be handed one.

Why a port rather than a direct import is a rank fact: `layers.toml` ranks `serving` below
`application`, so this module may not import the read, diff and view operations the review composes.
It takes `KnowledgeReviewPort` the way the launch route takes the capsule compiler, wired by the
composition root in `cli/dashboard.py`. Registration also carries an ordering constraint its siblings
share — the route must be registered before the greedy static mount — and the module's own docstring
records it, alongside the statement that the registrar accepts the runtime config for symmetry and
resolves nothing from it.

- The GET-only route handler over the injected port. [45]
- The two admitted selector kinds, refused rather than mapped. [46]
- The query parser that admits only those two. [47]
- **The status mapping the routes inherit from the change-set routes; the signature accepts all three typed results and reads success as `refusal is None`.** [48]
- The refusal code a process with no adapter produces. [49]
- **The 400 a selector kind outside the admitted set gets, inside the comparison handler.** [50]
- **The 404 for a candidate that does not resolve, is not live, or has no dataset half.** [51]
- **The 200/refusal split the entry handler makes: `entries` serves `200`, anything else goes through `_status_for`.** [52]
- The registration that must precede the static mount. [53]
- **The status mapping both routes inherit from the change-set routes; the signature now accepts either typed result and reads success as `refusal is None`.** [54]

## 260921-ICR-L1 The Committed Change-Set Range Binds Recorded Commits, Never HEAD

This route gained one module and changed one mode's meaning. **`serving/changeset_endpoints.py` now owns
which exact Git objects a committed change-set range binds**, and `serving/changeset.py`'s leaf views
call it.

`mode=committed` is the range between the two commits the enclosure contract **recorded** — the base it
forked from and the commit its closeout or integration wrote. The superseded behaviour is stated because
this route's earlier change-set narrative describes the old rule: a still-live leaf whose landed commit
was not recorded yet fell back to the worktree's moveable `HEAD`, which advanced with every ordinary
commit the task made. That published a range that was not the leaf's landed delta under a label that
said it was, and it answered differently on the next poll of the same URL.

**260921-ICR-L25 supersedes the refusal half of the paragraph above, and the distinction is the whole
point of the change: an *unrecorded* endpoint is not an *absent* resource.** It was a named `404`
(`RecordedEndpointAbsent`, a `FileNotFoundError` carrying a `kind`) whose message named the leaf, the
missing cell and the two actions — read `mode=working` while the task is live, or reopen after closeout
records the range — and never named the live `HEAD`. It is now **answered**: `_leaf_range` carries that
sentence in its own return value and `leaf_changeset` publishes it as the body's `state: "unrecorded"`
and `stateDetail`, with the counters a measured zero of nothing and the client withholding its total.
The reason is that a legitimate state **every live leaf passes through** was being reported as a
missing resource, and the change-set bar probes this view as soon as a leaf document is opened, so the
`404` was a browser console error on the page whose accepted criterion is zero (register B6). **The
other three answers are untouched**: an unknown leaf is still a named `404`, a bad or absent `mode` is
still a `400`, and an enclosure `scope` view is still its own `404` selection — the state was not
bought by answering everything.

**The two halves resolve independently, so one side's silence never discards the other's answer.** An
unrecorded **memory** half degrades to `[]` with zeroed counters — the degradation this side has always
published for a leaf that does not run memory — while the code half, resolved from its own recorded
commit, is still published; the **code** half carries its own `not-recorded` absence in the body rather
than refusing it, so the view still publishes no list for it while the fact is named. `no-repository`
and `unresolvable` (a recorded commit this checkout does not hold, checked with `git cat-file -e`) stay
refusals on both sides, because reporting either as an empty range would publish
a measurement the caller never made.

**`mode=working` is unchanged and stays a separate population**: `worktree-HEAD → worktree`, the one view
whose after-side is a filesystem location, and its own `mode` says so. The two modes are never mixed.

- **The new owner: which exact Git objects a committed range binds, the three absence kinds, and the one absence that may degrade to empty.** [55]
- **The caller that owns the degradation policy and (260921-ICR-L25) carries the code half's named absence instead of raising it: the two sides resolve independently, and only an unrecorded memory half empties.** [56]
- **The doc-reader entry point that publishes the unrecorded state in the body.** [57]
- **The cases that measure this route's half of the change: the recorded range bound and unmoved by a later commit, the state answered instead of a `HEAD` read with the route's own `200`, and the one-half degradation.** [58]

## 260921-ICR-L13 The Master Net Is Generation-Bound, And Selection Is A Module Of Its Own

This route gained one module and the master entry changed meaning. **`serving/master_net_generation.py`
now owns which exact Git objects a master NET change-set binds** — the declared integrated result
for a live request, or the exact recorded endpoints a pinned request names — and
`serving/changeset.py`'s master entry delegates to it.

A master review exposes one exact, generation-bound net comparison between its declared
source/knowledge base and its selected result, computed endpoint-to-endpoint rather than summed
from leaf counters. The list publishes `generation` (four commits + deterministic digest) with
`current`/`superseded`/`unmeasured` currentness and the one scope `integrated`, so a completed
master's recorded URL keeps resolving after its source branch advances; generation pins on both
master routes freeze the list and the file expansion to the listed generation. Breakdown rows
carry `committed`/`working` state beside the net, never inside it. A missing code endpoint is
a named refusal (`MasterEndpointAbsent`, the committed-range vocabulary applied to the master),
never a substitution with a later tip; only an unknown master degrades to empty. The net is
exact when served and refusal when unreadable: a post-validation diff failure refuses as
`unresolvable`, never as an exact-looking zero (F1). No new route was added and no route was
removed; both master routes share one 400/404 mapping, and the master list route newly
declares the shared refusal table. `serving/changeset.py`'s card carries the corresponding
body correction and citation re-derivation; the two new modules' cards (`master_net_generation.py`,
`test_master_net_generation.py`) carry the selection and the nine measuring cases.

- **The new owner: which exact commits a master net binds, the deterministic digest, same-call currentness, and the named refusal for a missing endpoint.** [59]
- **The thin delegating entry and the pinned file view, with the shared master 400/404 mapping.** [60]
- **The served vocabulary: the generation identity, the net's `generation` + `currentness` + `scope`, and the `committed`/`working` leaf-row state.** [61]
- **The nine cases that measure this route's half of the change, through real contracts, repos and routes.** [62]

## 260921-ICR-L2 The Review Route Admits "No Selector At All"

**Route meaning changed: the Intent Reviewer's transport now has two admitted request shapes instead of
one.** `review_request_from_query` took a required `selector_kind`/`selector_id` pair; both parameters
are now optional, and **both absent** is the task context — the review is opened from the task alone and
lists the complete source change inventory of the pair it resolves. One named kind with its id is still
a reviewed subject, and a half-named selector or an unadmitted kind is still refused with `None`, so the
route did not lose a refusal; it gained an answer.

The route's `400 bad-request` body was extended with the option the caller actually has: `expected`
names the two admitted kinds **or no selector at all**, `nextAction` says to name both parameters or
omit both, and `offendingInput` falls back to whichever of the two was supplied, so a half-named pair is
still reported with the value that was wrong. Nothing else on the route moved: the two port fields, the
unwired `503`/refusal answers, the status mapping and the serializer are unchanged.

- **The parser's two admitted shapes, and the refusals it keeps: a half-named selector and an unadmitted kind still return `None`.** [63]
- **The route's optional query parameters and the `400` body that now names the "omit both" option and reports whichever parameter was supplied.** [64]
- The status mapping and the serializer, unchanged by that leaf (the mapping serves a third result type since `260921-ICR-L3`). [65]
- **The composition the task-context answer reaches, which is where the complete inventory is measured.** [66]
- **The case that admits exactly the two reviewable selector kinds and refuses every other spelling, and the case that drives the same route with no selector parameters at all.** [67]

## 260921-ICR-L3 The Reviewer Gains Its Expansion Route, And The Inventory Rows Open Into Their Bound Content

**Route meaning added: the reviewer surface now serves a third GET route over a third port, and one
sentence of this route model had to be corrected rather than extended — "no path is accepted" is no
longer true of every route.**

`GET /api/review/intent/source-content` opens **one listed entry's actual content** at the two bound
code trees the inventory published. It is a third **path** rather than a field on the payload, and the
source comment gives the reason: the inventory is the whole task's change set, so a payload carrying
every changed file's text would be a document dump; the browser asks for exactly the row a reader
opened. The route is GET-only and takes a selector value (`SourceContentRef`) whose three parts travel
together because any one of them alone selects nothing: the task context, the entry path, and both
bound code tree ids — the last two named by the **caller**, read out of the listing it is looking at,
which is what keeps an expansion bound to the generation the reader was looking at.

The corrected boundary is the one a reader of this route model most needs. This is the only review route
that accepts a `path`, and it is **not** a filesystem path: it is a repository-relative entry path, and
the application owner behind the port reads it only if a **measured** change set lists it — the
requested generation's own change set, or, when that measurement cannot be made, the change set this
leaf's review actually publishes (its recorded baseline against the candidate tree it binds now). The
admitting measurement is published on the answer as `path_bound`/`path_bound_detail`. No route accepts a
root, and no route accepts a filesystem path, so the browser still cannot choose which dataset or which
repository is read; the whole path-confinement boundary the L45 and L22 sections describe for the other
two routes is unchanged.

The refusal shape is the same idiom with one new fact. `_UNWIRED_SOURCE_CONTENT` answers a process that
composed no expansion port with `503` and **"the surface is not served rather than served as an empty
file"** — an empty document would read as a file this repository does not hold, which is exactly the
confusion the L45 section's entry-list argument makes for lists. `ReviewSourceContentPort` joined
`ServingCollaborators` as its own third port rather than a field on the review payload, for the same
reason it is a third path. `_status_for` and `_json` widened to the third result type: `content` serves
`200`, and the expansion's refusal code `source_content_unresolved` reaches `400` through the same
fall-through as `comparison_refused`. A query that does not name the generation whole (a blank path or a
blank tree id) is a `400` naming the exact expected set rather than a server-chosen generation. The
application owner, its vocabulary and the dashboard renderer are on their own routes
(`mcp/src/agents_remember/application/overview.md`, `mcp/src/agents_remember/models/overview.md`,
`dashboard/src/panels/overview.md`); this section records only what the serving route model gained.

- **The third route constant, GET-only, with the comment recording why it is a third path rather than a payload field: the inventory is the whole task's change set and a payload carrying every file's text would be a document dump.** [68]
- **The expansion's whole selector as one value: the task context, the entry path, and both camel-case tree ids, which travel together because any one alone selects nothing.** [69]
- **The parse that refuses a blank component rather than defaulting it — a defaulted tree id would make the server choose a generation.** [70]
- **The one-line route registration, and the module-level transport behind it: the unwired `503`, the incomplete-generation `400`, and the same two exception shapes the comparison handler uses.** [71]
- **The expansion route's own unwired answer: "not served rather than served as an empty file".** [72]
- **The third port type and the third collaborator field, with the reason it is a port rather than a payload field.** [73]
- **The status mapping widened to the third result type, where the expansion's refusal code reaches `400` through the same fall-through as `comparison_refused`.** [74]
- The `400` body for a query that did not name the generation whole, and the exact expected set it names. [75]
- The registration call in the app factory, which passes all three collaborator ports and still precedes the greedy static mount. [76]
- **The composition root's third review port, whose docstring names the two facts the route rests on: the caller's generation rather than the server's choice, and no working tree or `HEAD` as a source of bytes.** [77]
- **The application owner behind the port: the admitted paths (a changed path of a measured change set, or unchanged context a recorded realization of the same comparison links — decided by the admission owner), both bound trees read by object id, and the per-side states.** [78]
- **The cases that drive the new route through the real composition: an incomplete query refused by the transport, an unwired process refused by name, and an unmeasured generation that still confines the path to a measured change set.** [79]

## 260921-ICR-L16 One 400/404 Mapping In The Review Transport, And Two Bodies That Now Carry An Action

`serving/review.py` (349 → 401 lines) changed in one place, for one reason: a reader has to be able to
**act** on a refusal, and this route publishes its refusals in the body of the status they map to.

The duplicated exception mapping is gone. Where the comparison handler and `_source_content_response`
each carried their own `try/except AuthorityError/FileNotFoundError`, both now call
`_port_outcome(port, request)` and return its `Response` unchanged when it is one — so the `400`/`404`
idiom has **one** implementation, and its bodies have **one** builder,
`_transport_refusal(status, detail, *, next_action, offending_input=None)`. That is what keeps the two
routes from drifting apart about which fields a transport-level refusal carries.

The behaviour change is on two bodies. `bad-path` gained `_AUTHORITY_NEXT_ACTION` and `not-found` gained
`_NOT_FOUND_NEXT_ACTION` plus the offending path (`path` and `offendingInput`), so both now carry the
same `status`/`detail`/`nextAction` shape the route's other refusals already had. Nothing was removed: no
route, status, key or model changed, and the fields are additive on this route's own bodies, which is why
the change stayed inside the packet's scope rather than needing a ruling.

Rank is unchanged and is still the reason for the port indirection — `serving` may not import
`application`, so an injected port remains the only way this module reaches an answer, and an injected port
is therefore how a test reaches the mapping at all.

- **The one mapping and the one body builder: the `400`/`404` idiom cannot differ between the two adapters.** [80]
- **The two actions the bodies gained, and where they are named.** [81]
- The expansion read's whole transport, whose docstring now states the shared mapping. [82]
- The published surface, unchanged: the three route constants, the three ports and the two parsers. [83]

## 260921-ICR-L10 The Route Admits The Page In Its Own Vocabulary, And Names The Input Each Refusal Is About

`260921-ICR-L10` (`ICR-R10@v1`) moves the paging inputs through this route without letting a request
model's validation escape as a server error. The route now takes the paging pair as one `Depends()`
reference each (`ReviewPagingRef`, `ReviewSelectorRef`, with `NO_PAGING` and `NO_SELECTOR` for the absent
spellings), admits the page size itself in `_admitted_paging`, and answers an out-of-range size with this
route's own `400` naming the value and the maximum — 64 is served, 65 and −1 are refused by name, and a
size the request model's own literal would have rejected is no longer an uncaught `ValidationError`.

`paged_review_request` returns a typed `UnadmittedReviewQuery` carrying **the input that actually
failed**, so the `400` body names the offending value rather than the request as a whole;
`review_request_from_query` keeps its long-standing contract for its existing callers, which is why the
two spellings exist rather than one widened signature. A cursor that names no collection is refused as an
input, not silently routed to an owner.

The route remains transport-only: it reaches every answer through its port, so the page it publishes is
the composition's page and never one this layer built.

## 260921-ICR-L12 The Route Admits One Historical Spelling And Packages The Question Whole

`260921-ICR-L12` (`ICR-R12@v1`) changes this route's review transport in two ways. The admitted
vocabulary gains **one** form — `RECORDED_HISTORY`, the request model's own literal re-exported under a
name this transport can read, so the route decides nothing about which records exist — and
`ReviewSelectorRef` becomes `ReviewQuestionRef`, because the fields are one question: which subject of
which reviewable kind and which record the read is addressed to. The old name is kept as an alias, so
the modules and cases that already spell it keep working on the same value.

**The admission is where an unknown spelling is refused, and it is refused by name.** `_admitted_history`
reads an absent spelling and the empty spelling a form sends as "no record named", admits the one
historical form, and answers any other name with this route's own 400 vocabulary — including the
expected value — rather than resolving it to the leaf's record. A caller that asked for a generation the
surface does not address must not be handed a different one, and a name outside the model's literal
must not reach the model as an uncaught validation error.

**The entries route deliberately takes no record parameter.** FastAPI drops a parameter the route does
not declare, and the route's own comment records why that is correct rather than an omission: a list is
offered for a *leaf*, and a leaf whose enclosure is closed lists the subjects of the comparison its
records hold — the one record a review of that leaf can be opened on.

## 260921-ICR-L17 The Review Route Admits The Previous Binding In Its Own Vocabulary

`260921-ICR-L17` (`ICR-R17@v1`) gives the review route one more admitted query parameter and one more
admission step, and it keeps the transport's division of labour intact.

- **`previousBindingDigest`** (`ReviewQuestionRef.previous_binding_digest`) carries the comparison the
  caller was already looking at. It is admitted as part of the **same question** as the record, not as a
  sixth route parameter.
- **`_SHA256_DIGEST` compiles `SHA256_PATTERN` from the models** rather than re-spelling it, so the
  transport cannot come to accept a shape the request model would refuse.
- **`_admitted_binding_digest` treats an empty spelling as absent, not as a value** — `previousBindingDigest=`
  is what a form sends when nothing was displayed — and refuses a non-digest with the offending input
  named and an `expected` that says what the field is for.
- **`AdmittedQuestion` and `_admitted_question` answer for the record and the previous identity as one
  decision**, which is why `paged_review_request` now calls one admission instead of two.
- **The transport only checks shape.** It does not compare, resolve or repair the digest: whether it is
  the comparison that is there now is the owners' answer, and a digest that no longer matches is reported
  as `stale` rather than refused.

## 260928-MIK-L96 The host runtime package

This route gained the `serving/paseo/` package: the moved command/daemon/plugin/provision modules plus the new install host part, Node acquisition, settings/convergence helper, start supervision, home lock, package-lock check, start-outcome receipt and terminal remedy. The dashboard start/status paths only observe or ensure the host — they never install, configure or reload it. Inside this shared package, the install host part (`paseo_install`) and the provision pass (`paseo_provision`) are the writers of host configuration, the plugin copy and the package tree; the start path composes the read-only `paseo_start` owner.

- The start-only supervision the dashboard composes. [105]
- The install host part. [106]
- The host acquisition. [107]
