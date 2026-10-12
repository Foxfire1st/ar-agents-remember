# Serving — Dashboard, Hosted Sessions, And Review Boundaries

## Governing Overview
[mcp/overview.md](../../../overview.md)

## Purpose

`mcp/src/agents_remember/serving/` composes the local dashboard, projection streams, hosted terminal sessions, normalized native harness control, structured conversations, deterministic agent notification, and task-scoped review/read surfaces. It exposes coordination authority through configured readers and injected application ports. Reducer interpretation, task authority, knowledge comparison, capsule compilation, and independent acceptance remain with their owners; serving also contains substantial session, scheduling, delivery, and lifecycle behavior, so the whole package is not merely transport.

Native Paseo role routes coexist with retained MIK review/read ports. The advertised MCP roster now contains 41 names versus 39 at the prior source revision, adding `role_start_set` and `retire_child`. Their native owners are `cli/paseo_role_tools.py::start_leaf_set` and `cli/role_retire.py::retire_native_seat`; native retirement uses receipt-tracked starter authority rather than the hosted retirement policy. Their inherited contract keeps canonical task/workspace identity, exact selected source/configuration, launch/replay identity, and separate model/effort/tier validation. Frame/plugin delivery binds the permitted parent origin, bridge protocol, and native selection. Requested launch intent, observed execution, and independent acceptance are distinct. Present checkout content does not establish replacement of a running installation.

The dashboard uses `McpRuntimeConfig` and configured observer/projection paths rather than accepting arbitrary host roots. Its always-on state and SSE projection carries task summaries, not complete task bodies; `GET /api/task-document` is the separate confined body reader. Review/read routes are transport shims over application-owned resolution. An unwired port is named unavailable, never represented as an empty list, file, comparison, or count.

## Hot Path Summary

`cli/dashboard.py` composes `app.create_app`; `app.py` constructs the app-scoped runtime and registers API routes before the greedy static mount. `_app_lifespan.py` migrates control-plane identity logs, compacts the workspace river, starts observer health, attempts one terminal-observation prime, primes the projector, and starts recurring work. The lifespan also starts a native held-message sweep independently of the hosted-seat notifier. `cli/role_held_messages.py::sweep_held_messages` advances bounded receipt-local waiting work without a model or browser poll; the loop contains sweep failures and drains its threaded worker on cancellation. Shutdown first calls the injected review-tree shutdown owner, then cancels and awaits background tasks, including that sweep, and shuts down the terminal host.

`projector.py` runs blocking projection work off-loop and drains an in-flight tick before propagating cancellation. Live change wakes invalidate reader domains; heartbeat refreshes retry pending task reads, and degraded wakes request full refreshes. Task-input refresh failure retains the last good task contracts, enclosures, documents, and series and schedules heartbeat retry. Landing observation has its own lifecycle-managed refresher whose immutable result feeds the network-free tick; simulation omits live observation by default, while interactive status retains its fresh-probe role.

The publication boundary derives snapshot/delta events, commits stable/current state, then notifies subscribers. Subscription registers before capturing current authority, without an intervening await. Failed-prime recovery publishes a full first snapshot; subsequent identical stable content produces no delta. The stream closes its subscription on disconnect/cancellation. The state response uses a boot-qualified weak ETag and revalidation; volatile ages and elapsed fields do not create content changes. `delta.py` owns deterministic entity upserts/removals and whole-block metrics, analytics, and active-worktree-group changes.

`change_watcher.py` watches existing projection-input roots, excluding worktrees with unreadable/high-churn provider data. It filters temporary files, dotfiles, own outputs, workspace non-input churn, and every durable-log lock suffix derived from `kernel.file_lock.lock_path_for`. Accepted unmapped paths invalidate all domains rather than silently retaining stale input. Native watches explicitly disable polling and skip permission-denied directories. Root sets are reconsidered every 30 seconds; re-established watches reconcile missed changes. Missing watchfiles leaves the watcher degraded; derivation/watch failures log and retry. Change pacing retains accumulated domains through work/rest/failure, applies debounce and a cadence floor, and rests after each completed or failed projection for `max(interval, min(duration, 3 seconds))`. Heartbeat and the three-second rest cap are scheduler rules, not end-to-end freshness guarantees. Watcherless simulation remains time-driven. Successful completed/drained projections, not attempted ticks, advance projection instrumentation.

Terminal truth advances independently of browser requests and notifier enablement. `_terminal_observation_loop` invokes the canonical sweeper through the cancellation-drained worker helper, ticks `LeafArchiveRecovery` on that same loop, and sleeps only after both attempts finish. Failures are contained separately and retried; archive recovery closes its cursor at exit. Starting-row/full-sweep rate limits remain inside the sweeper. The startup prime uses that same entry point, contains recoverable exceptions so serving can start, and records observer health for completed attempts; cancellation remains cancellation. Observer health diagnoses the producer stage separately from the notifier heartbeat and grants no readiness, queue, cursor, or task-authoring authority. Read routes do not rewrite it. `GET /api/terminal/sessions` serializes `catalog.list()` on a request worker; it performs no sweep. Its catalog lock can wait for a batch to commit, whereas the sweeper's nonblocking committed read may intentionally return older state.

The provider loop samples, records, evaluates degradation, and compacts metrics on its existing 30-second cadence. Provider metrics/degradation reclamation belongs to this dashboard loop; durable writes retain their store locks. The degradation owner holds durable detection, alerts, and critical-failsafe behavior; serving supplies configured stop and alert-delivery collaborators. Blocking operations are shielded and drained at cancellation. The workspace river has a separate slow live compactor and lock-consistent virtual cursors. Optional heap tracing and malloc trimming do not create unconditional loops.

## Construction And Ownership

The developer POST grant control uses the same pre-start/store owner as the architect function. Task summaries/body/series join readable external annotation; missing/broken display evidence is tolerated, while mutation/execution gates refuse. Display is not cached permission.

### Projection, HTTP, And Static Delivery

`app.py` builds a frozen serving runtime over one projector, terminal host/catalog/paster, liveness clock/config/sweeper, observer-health publisher, notifier heartbeat, build stamp, and injected ports/registrars. Handlers and background loops live in owned modules rather than per-app nested implementation closures. The app installs gzip for negotiated ordinary responses; event streams retain their streaming framing.

`GET /api/state` returns current projection or a not-ready response; `GET /api/stream` carries decorated snapshots and named folded-state deltas. `GET /api/events` is a separate raw-event channel: physical lifecycle offsets and lock-consistent virtual workspace offsets cannot be mixed with state-stream sequence identity. It scans retained backlog once per connection and streams bounded chunks, advances server-owned record boundaries across malformed/undecodable/blank/heartbeat/non-object records, parses accepted objects once, and emits `ready` after replay. Lifecycle-log reclamation belongs to projection, not stream reading.

Lifecycle transition actions validate `ActionAvailability` without performing those transitions. Targeted gate decisions are developer-attributed durable decisions, with gate-id staleness checks and rejection reasons; approve/reject/revision remain lifecycle-targeted, while gate-id-only cancel retains its explicit stale-workspace cleanup meaning. Targetless drift dismissal and operator-inbox posting/dismissal have their own durable owners. Files, notes, change sets, task documents, and task-local requirements retain confined read surfaces; requirements are rooted in the selected canonical `tasks/<repo>/<master>/requirements/` directory and single-segment master identity.

Task projections copy validated scheduling facts: master nature, sprint graph/seats/master references, deterministic waves and render-ready graph view, and persistent discarded-unstarted history. Relevant document linkage/seat/history edits enter body revision identity. Serving does not choose priorities or invent graph positions. The closeout-queue projection reports source-fingerprinted disposable projection condition, bounded source problems, and waiting-generation members; it does not claim blockers, commits, or certification.

The cockpit is generated release/package data. A checkout without a built bundle receives a 503 naming the build remedy, with no placeholder UI; missing fingerprint data omits `dashboardBuild`. Successful HTML revalidates, hashed assets retain their caching semantics, and missing-bundle diagnostics use no-store. Unknown `/api` paths receive 404 even behind the static mount; the missing bundle preserves GET/HEAD versus unsupported-method behavior. `response_contract.py` declares strict wire models and shared refusal tables independently of conversation imports. A declaration does not prove response conformance: returning a `Response` bypasses automatic response-model serialization, and the earlier conformance suite was retired.

`build_info.py` owns one cached process identity used by serving and MCP projection. It includes version/boot/checkout facts, interpreter/package identity, optional dashboard fingerprint, and a digest over sorted relative Python source paths and bytes, excluding cache noise. This distinguishes equal-version/dirty candidates without embedding absolute installation paths in the digest. It is diagnostic/acceptance identity, not update policy. Historical production starter registration used refreshed latest-package launches; disposable acceptance used exact local source to avoid certifying a stale published artifact.

`daemon.py` remains an import-light supervisor: a nonblocking ensure lock prevents duplicate starts, healthy processes may be adopted, recorded process identity combines kill probe with cmdline/zombie checks, logs rotate at spawn, and stop uses bounded TERM/KILL. Host/port/version mismatch may trigger restart, but healthy adoption does not compare cadence; changed pacing reaches an existing daemon through explicit replacement. MCP autostart stays settings-gated, threaded, bounded, and stderr-only.

### Hosted Identity, Admission, And Launch

`HostedSessionRuntime` binds catalog and host together: durable identity and a live process are complementary authorities. `terminal_opener.py` is the shared launch transaction for dashboard and structural dispatch. Its catalog batch spans read/probe/ensure/upsert; a live reopen returns retained immutable process truth or a conflict, while dead replacement starts a clean generation. Wire clients name harness ids, not arbitrary launch argv. Controlled built-ins carry typed settings selection to a runner that applies adapter-owned selector conflict checks, token-free discovery, and model-local effort validation before vendor startup. Explicit mapped non-native harness knobs and the recorded free-form escape hatch remain separate declared mechanisms.

`task_binding.py` resolves supplied canonical documents before semantic mutual exclusion. `chat`, `terminal`, `bootstrap`, and `curator` are taskless seat roles: no document is required and structural altitude/lineage/parent validation is skipped, but a supplied document is still resolved and bad references still fail. Other roles require a document, validate its role altitude and source lineage, then validate structural parent. Shared binding admission is used by spawn and the opener's final pre-host seam. Open/attach publish typed stale/unavailable lineage evidence; inherited ordering intent is to make stale-lineage recovery actionable before spend/settings or host effects obscure it. This does not mean every route-local preliminary selection executes after binding.

Structural identity is document plus current role; canonical topology and qualified parenthood, including reviewer-parent context, decide altitude and occupancy. `spawnRole` is immutable provenance; `seatRole` is current binding. Sprint/master/leaf bindings and reviewer exceptions come from structural authority, not filename heuristics or a fake role-anchor leaf. Ambient caller resolution distinguishes a plane-seeded hosted caller from the ambient launcher without a hosted-session id. Spawn caller kind is preserved write-once and projected as `spawnedByKind`. Attach is level-neutral, requires an identity for an untyped hand-opened harness, and does not respawn.

`structural_dispatch.py` serializes seats using bounded 4,096-stripe locking, failing closed on setup/flock error without a local-only substitute or unlink race. Dispatch-specific receipts use the existing catalog transaction owner. Brief viability distinguishes live/retryable generations from superseded, unresolved, or expired evidence. Ordinary inbox messages resolve current occupancy at post and delivery, surviving vacancy and replacement; the initial dispatch brief alone is exact-generation pinned internally. Startup identity migration precedes strict readers; this is not a dual-schema catalog reader. Existing alias/diagnostic-only argument seams and legacy notifier coalescing spellings have narrower compatibility purposes and must not be described as absent throughout the package.

`launch_capsule.py` decides `capsule`, declared `legacy`, or `refused`; application compilation crosses an injected port because serving cannot import upward. Roleless/chat/terminal launches and harnesses without verified capsule channels retain named legacy reasons; an unavailable role capsule is a named refusal. Codex uses admitted `developerInstructions` at thread-open boundaries. Eve uses a carrier/environment channel and its consumer gate. Other harnesses do not gain an instruction channel by appearing in settings.

An admitted Eve workspace becomes the session cwd, resolved selection workspace, and carrier workspace through one artifact-derived rule. Codex instruction capsules bind no workspace, so they do not themselves move cwd. The opener prefers resolved `LaunchCapsule.codex_delivery`, then retains the caller-facing `control.capsule_delivery` seam. Codex delivery travels through `RunnerConfig`, conditional `capsuleDelivery`, parsing, factory, and adapter settings; Eve never uses that Codex field. Capsule-free construction omits the key. The parser treats absent or explicit null delivery as none, and refuses other undecodable non-null values; the factory refuses non-null Codex delivery on a non-Codex harness. The broader inherited intent is never to silently launch without a requested admitted capsule; the local null behavior alone does not decide whole-path admission.

The runner bounds its single encoded configuration argument before returning spawn argv: 131,072-byte kernel-derived limit less a 2,048-byte margin gives 129,024 bytes. Over-bound refusal identifies measured size, bound, limit, and capsule seat where available. The limit is for one encoded argument, not the total argv/environment budget; path length and base64 expansion matter. Historical measured widths are reports, not maintained capacity guarantees or permission to silently raise the bound.

Codex applies one capsule revision at a thread boundary, re-states identical bytes for the same recorded binding/digest, and selects a bounded fresh thread for changed/unknown revisions rather than stacking revisions. Host `instructionSources` remain observation; per-launch `project_doc_max_bytes: 0` suppresses the legacy project-document chain. Ordinary turn messages cannot be claimed to refresh a thread-open instruction field. Library reopen deliberately selects legacy instructions because forcing a fresh thread would destroy its exact resumed vendor identity; its future capsule-carrying reopen remains assigned to thread-lifecycle/final-verification ownership.

Eve is an AR-owned application, not a PATH terminal program. Its adapter carries and verifies binding but neither compiles nor selects a capsule. Launch proof precedes staging/port reservation and distinguishes partial declaration, unreadable carrier, digest mismatch, wrong binding, wrong workspace, and inadmissible Git worktree identity. Ambient binding values are stripped and reintroduced only from the launch specification. Entirely unbound launch remains unbound rather than inventing instructions; inherited runtime-route intent is refusal before model work. Clear/compact are bodyless session controls and do not rerun instruction resolvers. The authored runtime is outside this serving route and was outside the recorded onboarding pathRules.

The settings-chain Eve seat path historically closed D22 by making launch effort a real runtime selection rather than weakening settings admission. The dashboard terminal opener still constructs a request with the default terminal-program backend, not an adapter-owned session backend. Its declared shipped-Eve/open exclusion and operator-taught PATH-row hazard must remain visible: historical role-configured opens refused at the capsule gate; shipped roleless open refused as bad-kind; a taught roleless PATH row could report running/legacy while not running the AR-owned runtime. Responsibility remains with the serving route owner. These are inherited observations, not a newly executed outcome matrix.

### Protocol Control And Conversations

Hosted readiness, activity, delivery, interaction, and completion use exact protocol evidence. Durable operator-inbox rows are inter-agent message roots; the adapter supplies delivery evidence, with correlated turn-boundary acceptance as acknowledgement/landing authority. Explicit model consume is optional attribution and does not mechanically settle delivery. Pane text, logs, copy mode, paste echo, and timing windows remain diagnostic and cannot authorize readiness, completion, or supervisor action. The dedicated readiness reader is bounded and ignores accepted legacy diagnostic keyword arguments.

`HarnessSubmissionAuthority` owns the sole epoch-bound ordinary prompt/setter order, FIFO, immutable id/source/payload admission, atomic queued withdrawal versus dispatch claim, exact operation-ref completion, response bypass, early-terminal dominance, and raw-free status. `SubmissionLedger` owns retained rows and reads under the same lock. The deleted queue facade is not an additional authority; descriptions of delegation through a queue are historical. Dispatch-now adapters cannot introduce a second prompt queue or settle by FIFO/id alone. Retention is bounded and refuses capacity when no terminal unpinned row is evictable; it preserves live/active/unknown evidence, discards terminal prompt bodies, and retains digest/correlation. Lookup batches are bounded to 64 ids. Only certified pre-dispatch busy failure is retry-safe; uncertain first-byte delivery reconciles under the same identity rather than blindly resending.

The private Unix control channel validates exact identity, epoch, protocol, receipt shape, and accepted-byte ambiguity. Response peer loss after accepted dispatch is contained across write/drain/close; malformed input, serialization, cancellation, identity failure, and unrelated errors stay loud. Completion correlates exact request id, or, for legitimate null ids, an exact unique accepted inbox row with textual vendor correlation in the same hosted session. Missing/ambiguous correlation fails loudly. Delivery metadata updates the same row without marking pending inbox state consumed. Idle/immediate and settling/queued describe actual replacement state rather than synthetic activity.

Evidence is diverted once from reserved `arEvidence` frames before redacted event publication. The bounded live window retains 2,000 frames, 32-KiB clipping markers, monotonic sequence, and honest eviction floor. Evidence deque and native-page coordinate domains are disjoint, epoch-bound, and validated for monotonicity/continuation/counts. Native Codex thread pages and Pi durable entries are distinct from the live window; Claude native paging fails closed. Unknown vendor shapes retain raw evidence without guessed semantics. Submission provenance is read through bridge delegation to the ledger. Catalog terminal-evidence lift validates envelopes, rejects unsupported projectors before reading, advances truncation only through the last returned sequence, and bounds Pi polling to 200 entries/page and eight pages/sweep without adding a history fallback.

Native interrupt uses a structural capability seam and bridge-stamped epoch. Codex guards exact active turn; Pi guards expected active operation before write; acknowledgements replay by observed pair and do not equal settlement. Unsupported adapters refuse by name. Operation timeline is bounded paged never-bodies evidence with latest/evicted sequence, truncation, and epoch; completeness is the union of pages, not one page. Asset submission uses references, confined endpoint-root paths, separator/dot-segment/NUL and component bounds, size/digest checks at admission and native construction, and honest unsupported receipts. Asset-free digest behavior remains unchanged; supported receipts add asset ids. Withdrawal captures exact pre-tombstone recovery body once only for cockpit-authorized withdrawal; replay returns none. The existing protocol version remains the substrate rather than introducing ACP transport.

Native discovery remains token-free and model/effort menus are dynamic, model-local evidence rather than maintained global enums. The capability catalog keeps one successful fingerprinted entry/lock per built-in harness, single-flights misses, and treats explicit refresh as an account boundary; failed refresh quarantines only the entry observed. `claude`, `codex`, `pi`, and `eve` are protocol built-ins, separate from the developer-curated terminal registry. Pre-session dashboard discovery exposes only id/name/detected.

Claude discovery removes supported pre-`--` MCP selectors only on its ephemeral catalog launch and inserts a strict empty set while preserving unrelated arguments and the positional suffix; normal startup remains caller-owned. Claude model/effort setters require correlated native result evidence and retain generic vendor refusals. Codex tracks desired/pending/captured/effective selection separately and promotes settings on an accepted fresh turn on the same thread. Pi uses provider-qualified identity, model-local thinking, fresh-state validation, atomic readback, and honest model-error/thinking-clamp asymmetry. Configured startup uses native flags or thread config, not composer paste; Claude effort may be validated flag evidence without an echo. Cancelled/late responses are reclaimed. Eve uses health/session identity and absolute event-index NDJSON continuation, with meta ids only for replay deduplication; acceptance, completion, and retirement remain separate. Ordinary Eve delivery queues explicitly rather than using cancellation-backed steer, lost submission reconciles without repeat, cooperative interrupt settles later, and runtime setters remain unsupported despite launch-time model/effort selection.

Conversation composition installs one immutable app-scoped `ConversationRuntime` and mounts one root over active/library/control children. Strict protocol-neutral models define identity, evidence-backed status/capability, page/event cursor scopes, operations, attachments, and telemetry. Authorization is server-resolved local operator/workspace authority, not authenticated browser identity: unknown/non-loopback peers fail closed, no principal/tenant input is accepted, and remote/multi-user use requires a different designed subsystem. Narrow dependencies let child owners consume runtime without rewriting shared composition.

Active conversation pages, selected-child history, and resumable events use purpose-branded HMAC cursors rebound to authorization. Bounded reconstructable-projector retention hydrates from native durable pages or the bounded live evidence window, never the flattened transcript deque. Ordered envelopes and typed gaps represent established-stream failures; idempotent tool upserts union blocks by block id. One status service classifies evidence for Chats and orchestration. Contract fixtures gate capability; version-string difference alone cannot demote it. Claude's unprobed active features remain honestly unverified while interrupt and conditional library gates retain their feature-specific exceptions, and historical Codex tool loss remains visible.

The library reads authorized dormant native catalog/history through Codex app-server and locked Claude/Pi helpers. Capability gates use live production-path probes keyed to installed executable identity; fixture/helper presence alone grants nothing. Signed cursor/key identity and generation from selected observable native signature fields keep project scope narrow; these signatures do not prove detection of every store edit. Exact open/status/reconcile launches a new tracked session through the shared opener, proves resumed catalog identity, and retires record-spawned failures honestly with bounded idempotent retention.

Control owns exact-turn interrupt/status/reconcile, source-aware never-bodies operation queues, cockpit-only withdrawal with an authorization-bound 900-second recovery lease, typed staged/rebound/submitted attachments in a confined 0700/0600 spool, read-only effective policy, and evidence-bound telemetry. Signed opaque references rebind per wire; bounded per-session/epoch ledgers and serialization sit above replay caching. Pi settlement uses clip-preserved terminal identity. Shared composition remains the owner of runtime and grammar, not an alternate control implementation.

### Notification, Retention, And Terminal Lifecycle

The deterministic agent notifier reads canonical stores directly, never projected dashboard state and never a model polling layer. Mechanical predicates cover deadline/report staleness, undelivered rows, seat liveness, structural state/boundary signals, escalation, and dead upstream. Observation cadence, redelivery floor, and owner-signal cooldown are separate. Chain progress can defer stale findings; owner routing resolves the current manager; one row takes at most one transition per sweep. Completion/artifact delivery readdresses current responsibility. Persistent hosted-delivery failure stays in redelivery until its threshold or escalation marker rather than entering generic escalation prematurely.

State-signal emission revalidates current subject binding and owner just before posting. Vacancy creates neither a durable row nor marker and remains sweep-eligible; typed document refusal fences the subject rather than aborting unrelated work. Signal posting orders durable row/renewal, sweep fold, marker callback, then delivery. Marker failure leaves a pending unmarked row without submission. Shared redelivery checks the current source's exact normalized ask/evidence marker; boundary drain inherits this action guard. State-signal coalescing keys exact subject agent plus normalized ask; other kinds retain document/role identity, so replacement seats cannot renew each other's state signal. Existing supervisor/agent-notifier creator and ask-prefix spellings still coalesce as the same legacy root cause.

Boundary drain requires pending/unlanded evidence, a nondead unambiguous current target at a timestamped turn boundary, and a boundary strictly after the last parseable attempt. No attempt clock is admitted only for state-signal rows, covering replacement rebinding; other rows retain ordinary redelivery and malformed attempt clocks refuse.

The timed control-plane ladder and orphan-detector modules are retired. Their earlier suspicion, custody and no-automatic-reparenting policies remain historical intent, not current module ownership. Current structural routing and mechanical relay use their surviving owners; old respawn/orphan delivery claims require their original witnesses. Confirmed-gone reconciliation considers only eligible notifier nudge/escalation rows; catalog termination proves death, compacted tombstones require successful exact-name tmux observation, and probe failure fails closed. Reconcile/compact occurs under the inbox lock before redelivery and emits only aggregate body-free non-no-op evidence. TTL/cap rules and active/landed/exited retention remain separate.

Execution evidence must be registered into durable task truth before bounded source reclamation. Liveness releases its catalog batch before registration and compacts only confirmed ids; notifier registers its snapshot before inbox reconciliation/compaction. Missing registrars authorize no task-bound deletion and do not activate another evidence reader.

Terminal WebSockets attach independent tmux clients only after live-host proof. Disconnect closes the browser client's PTY, preserving the underlying session for refresh/other tabs. Dashboard-owned clients strip inherited tmux identity and enforce browser PTY grammar while preserving unrelated environment. Canonical hysteresis observes exits and repairs false exits; attach/paste use the same app clock. Raw terminal input/paste remains its own terminal channel, not a native model/effort or inbox-delivery fallback. Validated screenshots use the separate image path.

Landed classification preserves successful seats for inspection; explicit landed cleanup closes only still-landed rows. Terminate kills the host and updates catalog state; retire adds provenance and policy. Retirement forbids self-retirement, allows a manager's own worker/reviewer/curator leaves and same-master reviewer, allows an architect's structurally bound same-sprint plan-review reviewer, and gives orchestrator portfolio-wide authority. Already-retired HTTP handling remains idempotent. Rename changes identity text while preserving original spawned label and immutable spawn role. Startup-failed control shutdown may retain the honest stopped-queue detail while still reaping the host and reaching terminal state.

### Review And Host Runtime Owners

The intent-review family has four GET routes and four injected ports: comparison, entries, source-content, and summary. Comparison admits task context alone or an invariant/family selector pair; partial/unknown selectors refuse. Paging is admitted in transport vocabulary, capped at 64, with failed input named; continuation without collection refuses. History admits only the declared recorded spelling, with empty meaning absent. Previous binding digest uses the model's SHA256 shape; transport checks shape, while the owner decides stale comparison identity. Entries intentionally takes no history selector. Comparison/entry/content success uses refusal absence, unavailable adapter maps to 503, unresolved/not-live/dataset-absent/subject-unresolved maps to 404, and other refusals to 400. Shared exception mapping gives bad-path/not-found actionable bodies. Summary independently returns typed states as 200 and unwired as 503.

Source expansion carries task context, repository-relative path, and both caller-supplied tree ids together. The application admission owner accepts a listed requested-generation change, or measured-unchanged context linked by realization/proof in the same comparison. If the requested generation cannot be measured, only a path listed by the leaf's measured current comparison is admitted; unchanged context is not. Answers publish the admission/path bound and read both sides by object identity, not filesystem/HEAD substitution. The browser does not select an arbitrary repository root or dataset. The current recorded-comparison file UI is `ReviewSurface.tsx::ReviewChangeOverlay` mounting `ChangeSetViewer`; `SourceContent.tsx` retains the structured source-content reader. The deleted `SourceExplorer` and `LaneFileFocus` components are not current owners.

Tree review uses its own GET port, 16-thread executor, cancellation event and arrival context; disconnect/cancellation signals the worklist and cancellation drains the worker. Selection permits recorded number/history and at most one focused invariants/files-lane/file question, with bounds of 500 invariant ids, 64 characters/id, and 4,096 characters/path. Invalid selection is 400, unwired is 503, and all typed owner answers are 200. A live application read may pin comparison trees and write its record; same-tree reuse can recreate missing comparison pins through the owner's `_pin` calls, and dataset review does not invoke this tree route. The independent knowledge reader needs no task, supports the declared repository/tree views and continuation, returns invalid-request as 400, unwired as 503, and other typed states as 200; it authors no knowledge truth; derived-index/cache preparation is a separately admitted runtime write.

Committed leaf change sets bind recorded base/closeout-or-integrated commits, never moving HEAD. Unrecorded code publishes explicit unrecorded/stateDetail, and unrecorded memory may yield nothing while preserving code's independent answer. Unresolvable recorded objects refuse. `_leaf_range` also returns empty for a missing repository before invoking the endpoint owner; the endpoint helper's own no-repository refusal must not be mistaken for whole-call-path behavior. Working mode is separately labeled HEAD-to-worktree and requires the live code worktree. The task and file-diff change-set routes also accept `comparison=<number>` with repo, master and leaf. They select the exact recorded comparison, using its code trees and its converted memory base when present; the list returns `mode: "comparison"` and all four tree operands. Supplying any `mode` query parameter alongside comparison refuses with 400, including an empty value; missing comparisons or unreadable trees refuse with 404. `changeset_comparison.py` owns these reads and uses one listing diff per code/memory half, with separate sidecar-presence reads. Master net compares endpoints rather than summing leaves: live selection uses declared integration result, pins freeze exact generations, digest covers four endpoint commits, and same-call currentness is current/superseded/unmeasured. No later source tip repairs a missing endpoint; unreadable diff is refusal, not exact-looking zero. Leaf breakdown state remains beside the integrated net.

`serving/paseo/` owns host command/daemon/plugin/provision/install, Node acquisition, convergence, locks, package checks, start receipts and remedies. Dashboard start/status only observes or ensures a configured host. Install/provision owns configuration, package tree and plugin writes; start-only supervision can write its own outcome receipt but does not install, configure, or reload the host. Provision ordering preserves pinned-version activation, stop-before-start-only-config changes, accepted configuration replacement, and plugin-loaded stamping so interrupted work converges. Shared host settings remain authority.

Started-agent metadata is published to the private plugin using product-owned parent/role/task/report facts. The host turn-end callback can send a fixed metadata wake when the role sent no parent message, holding it while the parent is busy or permission-waiting. It does not read semantic verdict content, approve work, bypass permission or add a public message/dashboard endpoint; runtime consumption remains an independent witness.


### Native selection and source-owner qualifications

Serving adds native role routes beside retained MIK review/read ports, with exact selected source/configuration authority. The lifespan additionally owns the native held-message sweep task: it advances workspace-local waiting work without a model or browser poll, contains a failed sweep, and drains an in-flight threaded sweep on cancellation. This is independent of the retained hosted-seat notifier and uses the native role-launch/message path rather than the retained terminal-catalog/inbox path. Frame/plugin delivery binds the permitted parent origin, bridge protocol and native selection. Requested launch intent, visible execution and independent acceptance remain separate. Imported source does not imply that a running installation has already been replaced.

The serving boundary exposes a packaged dashboard fingerprint without fabricating one when the
artifact is absent. Since 260731-EFA-L1 that absence is **routine rather than exceptional**: the
cockpit bundle and its `dashboard.fingerprint` sidecar are generated at release time and are not in
version control, so an unbuilt source checkout serves no cockpit and reports no `dashboardBuild`. Both
absences are answered honestly — a 503 naming the build command at `/`, and an omitted key on the
wire — never with a placeholder page or a fabricated identity. The boundary also sends revalidation
policy only on successful HTML, and keeps pre-session harness
discovery to `id`/`name`/`detected`. Raw event cursors realign to server-owned record boundaries and
advance past malformed, undecodable, blank, heartbeat, and non-object records; accepted top-level
objects are parsed once and reused by SSE. Dashboard-owned tmux clients strip inherited tmux
identity and force the browser PTY grammar while preserving unrelated environment settings.

The active/library/control children below remain implemented and mounted for the retained hosted-session conversation service. Their vendor-native pages, bridge epochs, cursors and control receipts are service-local authority; they do not define Paseo `role_message` acceptance, canonical task acceptance or Git landing. The original empty-router account is history; the implemented children are not.

For the retained terminal-catalog/tmux hosted-session service, exact adapter snapshots govern readiness, liveness/activity, interactions and terminal projection. Its inbox-rooted inter-agent delivery persists durable operator-inbox rows and uses the exact-session adapter as their wire. A correlated `accepted` receipt at a turn boundary authorizes only that row's formal inbox `landed` delivery state; a busy `queued` receipt is not a landing. Model `consume` remains optional attribution and does not change mechanical retry or terminality. None of these states is canonical task acceptance or Git landing. Native `role_message` instead uses bound agent identity, launch receipts, filed message artifacts and the workspace-local held-message store; host `taken`/turn-finished evidence is transport/turn evidence, not AR acceptance. Pane text, terminal logs, copy mode, paste echoes and timing windows remain diagnostic-only for protocol readiness and acceptance; older pane/log/paste descriptions below are history.

Within the retained terminal-catalog service, hosted-seat identity is the real task document plus role: sprint roles bind the sprint document,
manager binds the master, and worker/reviewer/curator bind leaves. `ambient_seat.py` proves callers
from plane-seeded hosted context and — since 260821-ARSPAWN-L1 — resolves the ambient launcher (a
process with no `AR_HOSTED_SESSION_ID`) as a typed `AmbientCaller` for `dispatch_agent`;
`structural_seats.py` qualifies parent/child relations and singular current occupants. Spawn
provenance now includes caller kind (`spawned_by_kind`, written when set), mapped write-once onto
the catalog row by `terminal_opener._opened_catalog_entry` via `_preserved` and surfaced on the
spawn wire as `spawnedByKind`. `terminal_task_assignment.py` is the one level-neutral binding primitive. Ordinary retained-service
inbox traffic is persisted, then re-resolved at post and delivery time so replacement is transparent within that bus;
the initial dispatch brief alone stays exact-pinned internally. One-way startup migrations run before
strict catalog/control-plane readers; no dual-schema compatibility reader remains. Agent-notifier
predicate helpers consume the existing `TaskHierarchy` protocol, while production constructs the
filesystem-backed `TaskDocumentTopology`; this preserves one hierarchy authority without forcing
callers to depend on its concrete implementation.

The state-signal, boundary-drain, marker-order and coalescing rules in the next three paragraphs are retained catalog/operator-inbox notifier rules. They neither route native role-message held stores nor judge requirements; `role_held_messages.py` explicitly does not call the hosted-seat messaging/controlplane stores.

**For each retained hosted harness bridge, `HarnessSubmissionAuthority` is the sole epoch-bound prompt/setter
timeline.** It owns prompt FIFO, immutable id/source/payload admission, atomic queued-withdraw versus
dispatch claim, exact full-operation-ref completion, early-terminal dominance, response bypass,
raw-free cockpit status, and bounded privacy-aware retention. `HarnessControlQueue` no longer exists:
260731-EFA-L6 deleted the compatibility facade outright, so the authority is reached directly.
Codex, Claude, and Pi are dispatch-now adapters with guarded first-byte seams;
none may create a native/adapter queue or release work by FIFO/id alone.

**The retained hosted bridge's additive, read-only vendor-native evidence and resume substrate.** Mappers
place full native frames under the single reserved `arEvidence` raw key on events they already emit;
the bridge diverts each payload at its one `_run_events` consumption point into a bounded
per-session evidence deque (2,000 frames, 32 KiB clip with a visible marker, monotonic adapter-event
sequence, honest eviction floor) and reduces/publishes the redacted event, so `snapshot.raw`,
catalog `control_raw`, SSE projections, and every existing consumer stay byte-identical. Three
additive IPC reads cross only the user-private socket: `evidence` (deque-domain page),
`evidence-native-page` (native-domain page with typed identity and an opaque `nextCursor`, codex
`thread/read` and pi `get_entries(since)`; claude fails closed typed), and `submission-provenance`
(epoch-checked batch over all three sources through the bridge → authority delegation).
Every evidence response carries `bridgeEpoch`, the two coordinate domains are disjoint and rejected
cross-typed, and the validated client enforces monotonicity, continuation coherence, and exact
counts. The codex-only `resume_thread_id` channel rides opener → `RunnerConfig` payload → factory
kwarg → the sole `CodexAppServerSettings` site, refusing non-codex or malformed values before any
spawn. No existing action, DTO, consumer, deque, or snapshot reduction changed shape; unknown
native shapes cross as unknown-vendor evidence with raw preserved and semantics never guessed.

**The retained hosted bridge's additive vendor-native control-plane substrate remains inside the same family.** A
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
delegation runs authority → bridge → IPC → validated client exactly like the evidence provenance reads.
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

**Scope of the operating context below.** Conversation, controlled-adapter, terminal-catalog, operator-inbox and notifier accounts remain the retained hosted service's operating context. Vendor-native protocol evidence and inbox delivery are not the native Paseo role-message bus. Projector/SSE, task/requirements/knowledge/review reads, provider sampling and host supervision retain their named owners; read/display observations do not grant canonical task mutation, review acceptance or Git landing. Recorded installed-runtime matrices and resource numbers remain historical measurements.

The original contract-only leaf established structure before live endpoints: consumers validate hostile
normalized products through `models/conversations/`; the now-implemented active and library services
satisfy their separate read ports and cursor purposes; mutations stay on the control
router. The root composition is mounted once beside existing harness-control routes. The locked
repository helper and redacted installed-runtime fixtures are compatibility evidence only and may
not promote a capability by being present.

The change-or-heartbeat pacing described here and in the route model includes the current live completion-relative rest, `max(interval, min(tick duration, 3s))`. The heartbeat is a wake/deadline input, not by itself an elapsed projection-freshness guarantee: running/next projection time and that additional rest still count. Watcherless/simulation replay keeps its established fixed-interval path.

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
`lifecycle.heartbeat` out of the river (lifecycle-log reclamation belongs to the projection
pass, never to this stream); `POST /api/actions/{action}`
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
dashboard's 1s polling, self-healing false exits), and `POST /api/terminal/{session}/terminate`, authorized retire, and landed cleanup are explicit terminating paths in this retained service.

The harness/adapter/hosted-session members below are retained service owners, not a recipe for the native role launcher. `app.py` composes those members beside `ServingCollaborators.extra_api_routes`, which the CLI binds to `register_role_launch_routes`. Task/knowledge/review/requirements/projection and host-package members keep their separate current owners.

- `app.py` — `create_app(config, *, cadence, replay, live_inputs, collaborators)` builds
  the FastAPI app
  (`ProjectionCadence` paces it; `ProjectionReplay` is the sim seam; `LiveProjectionInputs` resolves
  the three live world-input toggles together against that seam — each `None` = infer, so live
  serving injects a `ProjectionInputWatcher` for change-driven pacing while `--sim` stays
  time-driven, and `cadence.heartbeat` bounds quiet-world staleness; `ServingCollaborators` are the
  injectable long-lived objects). Since 260731-EFA-L2 the handlers, background loops and route
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
  `POST /api/terminal/{session}/paste` (retained terminal input: protocol harnesses receive one correlated whole-message submission through `submit_control_prompt`; a legacy harness with no control endpoint and an unsubmitted harness draft are refused. Only a plain terminal uses the pane-input transport. Pane capture is not harness acceptance authority),
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

## Invariants And Boundaries

Keep exact task, session generation, bridge epoch, operation reference, comparison generation, and authorization identity separate. Ordinary replacement-safe addresses are not pinned dispatch receipts. Accepted writes, observed execution, terminal settlement, inbox consumption, and independent acceptance are different facts. Unavailable measurement must not be reported as measured empty content or zero; explicitly declared degradation and current implementation exceptions must be named rather than generalized away.

Honor one owner for canonical topology, projection publication, terminal observation, prompt/setter order, retained ledger, durable inbox delivery, native evidence, and each reclaim cadence. Ports preserve serving/application rank; capsule admission is consumed as a value rather than compiled in serving. No pane/log/paste timing fallback may acquire protocol authority. No fixture version, catalogue enum, generated artifact presence, or green historical test count promotes capability or delivery acceptance.

Store bounds, privacy, confinement, and reclamation are behavioral requirements: retain live ambiguity, distinguish coordinate domains, rebind signed tokens, verify assets twice, persist recovery/markers before delivery, and drain blocking writes before teardown. Recoverable startup/observation failure is intentionally contained, while cancellation and typed identity/refusal boundaries keep their meaning. Existing explicitly implemented degradation/compatibility seams are not permission to create new ones.

## Historical And Verification Limits

The slice-04 through HFX transport-only, pane-classification, JSONL delivery, capture-verified paste, setter/daemon queue, role-anchor/leaf-normalization, and initial empty conversation-router accounts are superseded provenance. Their enduring intent is one shared opener, durable delivery roots, explicit ownership, diagnostic honesty, bounded work, no duplicate queues, and replacement-safe routing. Historical calibrated paste windows, payload lengths/hashes, catalog counts, resource figures, route/test counts, smoke/fixture versions, and release claims are not fresh acceptance at this source head.

Retain CAPS-L5's named limits: vendor effect of re-sending developerInstructions on thread/resume was unmeasured and IN_PLACE was schema/unit evidence only; FORK_THREAD had no production caller; that leaf did not exercise a live terminal_opener spawn. Its unbounded-argv D12 claim is superseded by CAPS-L11's present encoded-token check, but historical 120,536-character/92-percent and later 126,096/126,352-byte width reports remain historical measurements with thin path-sensitive headroom. Bound growth requires explicit re-derivation, never silent rebound.

CAPS-L15 historically reported production-chain first-prompt and Eve consumer-gate evidence; CAPS-L17 reported closure of D22 through settings-chain/provider-boundary measurement and retained the dashboard shipped-Eve exclusion/taught-PATH hazard. The named checkout witnesses `notes/reports/260915-CAPS-L15-evidence/E8-fix-r1-production-chain.txt`, `notes/reports/260915-CAPS-L17-evidence/s5-settings-chain.json`, and `notes/reports/260915-CAPS-L17-evidence/s6-s7.json` are absent here. Those reports and their live acceptance conclusions cannot be independently renewed from this checkout. Library reopen's declared legacy identity-preservation exclusion remains visible separately.

LOCR-R18's historical ordering witness did not constrain prime versus migration/compaction; that edge is visible in present straight-line production order, not independently reverified witness coverage. Observer health supersedes the older claim that prime had no health surface. Unbound worker active-phase credit remains the inherited accepted follow-up; credited unbound reviewer/curator progress does not erase it. Resource-performance work remained queued. Claude's unprobed conversation contract, historical Codex tool-loss visibility, unsupported native/history/control operations, and honest absent effort echo must not be upgraded by narrative consolidation.

This proposal examined every prose chunk of the supplied 139,481-character card and selected present source owners. It did not run tests, import product entrypoints, start services, validate installed runtimes, repair code, or establish a new execution/certification verdict. Unchecked inherited contracts above retain their semantic intent; material present-code corrections have deciding anchors below.


### Retained source and evidence qualifications

**Retained hosted-service scope.** The task-binding, controlled-adapter readiness and CAPS launch accounts below describe the retained terminal-catalog/tmux service and its carrier seams. They do not define the native Paseo role launcher: that path resolves `RoleSelection` through `application/role_launch_context.py` and starts/messages agents through `role_start`/`role_message` using bound tool-server identity and launch receipts. Historical vendor probes, token widths and leaf acceptance transcripts remain evidence of their recorded epoch, not claims about a running installation.

**Declared limits on this route, stated as limits.** The vendor-side effect of re-sending
`developerInstructions` on `thread/resume` is unmeasured (0.151.0 persists no rollout until a real turn
runs), so `IN_PLACE` is schema- and unit-proven only; `FORK_THREAD` has no production caller; no live
spawn through `terminal_opener` was exercised; and, at L5's recorded tip, the delivered payload was bounded by nothing here (superseded by the L11 bound below) —
the largest shipped capsule measures **120,536 chars, 92.0 % of Linux `MAX_ARG_STRLEN` (131,072)** with
~10 KB headroom, and past that the spawn fails with `E2BIG` before any AR surface can report it
(defect `D12`, routed to the final-verification leaf with a required bound and pre-encoding refusal).

**Route meaning changed for the retained hosted capsule launch path; this section accounts for that path, not the native role launcher.**
Before this change set, the capsule chain was built and individually proven at every link — the
compiler (L2), the admission/MCP surface (L4), the Codex instruction seam (L5), the eve carrier (L7) —
and **no production launch point supplied a capsule to any session**. A dispatched seat and a free
agent both launched with no instructions at all, and every green test hand-supplied the intermediate
value, which is why no leaf's suite could see the gap.

**The three production launch points in this retained capsule-chain account, per point:**

This replacement-safe dispatch account describes the retained structural/catalog and operator-inbox path. Native `role_message` resolves launch receipts; addressing an archived agent is refused with successor guidance rather than silently routing that agent-id message to a replacement.

**L11's recorded width, and the reason the figure is a report rather than a guarantee.** The largest shipped
pair measures **126,096 B** with the settings-resolved launch a real launch always carries (2,928 B
under the bound; 126,352 B at the widest realistic shape, where an eve carrier binds the admitted
worktree to a 102-character cwd — 2,672 B under). At roughly 96 % of the limit the margin is thin,
and the route to the bound is a **path length** as much as a capsule: the token grows ~1.3320 encoded
bytes per `cwd` character — the base64 4/3 expansion, so it is the encoding's property rather than
this capsule's — first crossing the bound about 2,297 characters beyond the server workspace root.
**Any pair measured over 129024 is a bound re-derivation that stops the loop, never a silent
re-bound.**

**Superseded count (`260921-ICR-L3`): the reviewer surface now serves three routes over three ports,
and it is no longer true that no route accepts a path; the later summary route makes the current intent-route count four.** This section records the two-route, two-port
landing as it was; every statement below about *counts* is superseded by the `260921-ICR-L3` section at
the end of this narrative, while the reasons it gives for the split — a second **path** rather than a
second adapter, and one application resolution behind both answers — remain current.

The intent-review surface is reached through **four GET routes** (comparison, entries, source-content and summary), and none of them is a mode of another.

The comparison route accepts no path, and the entry route takes the task context alone. The expansion
route (`260921-ICR-L3`) is the one that does: a **repository-relative entry path**, always sent with
both bound code tree ids. The admission owner allows either a changed path of a measured pair
(or the leaf's published measured fallback) or, when the requested pair is measured, unchanged context linked by a recorded realization in that comparison.
It is not a filesystem path and no route accepts one, so the browser still cannot choose which dataset
or which repository is read. The comparison route's inputs are a repository, a master, a leaf id
and one recorded subject selector, with the selector kind closed at the two identity seeds the read
operation declares — `invariant` and `family`; every other seed kind addresses a revision, a membership
or a claim rather than a subject a curator reviews, so it is refused by name instead of being mapped
onto one of the two, and the refusal carries the offending input, the expected set and the next action.
That closure is what keeps the browser out of candidate selection: the resolution behind the ports
chooses which dataset is reviewed, and no route can be handed one.

The route's `400 bad-request` body was extended with the option the caller actually has: `expected`
names the two admitted kinds **or no selector at all**, `nextAction` says to name both parameters or
omit both, and `offendingInput` falls back to whichever of the two was supplied, so a half-named pair is
still reported with the value that was wrong. Nothing else on the route moved: the then-present port fields, the
unwired `503`/refusal answers, the status mapping and the serializer are unchanged.

**At the L3 landing, the reviewer surface gained a third GET route over a third port (the later summary route makes the current intent-route count four), and one
sentence of this route model had to be corrected rather than extended — "no path is accepted" is no
longer true of every route.**

The corrected boundary is the one a reader of this route model most needs. This is the only review route
that accepts a `path`, and it is **not** a filesystem path: it is a repository-relative entry path, and
the application owner behind the port admits a changed path of a **measured** change set — the
requested generation's own, or the leaf's published measured fallback — or, for a measured requested pair,
unchanged context linked by a recorded realization of that comparison. Unchanged context adds no inventory entry or count.
admitting measurement is published on the answer as `path_bound`/`path_bound_detail`. No route accepts a
root, and no route accepts a filesystem path, so the browser still cannot choose which dataset or which
repository is read; the whole path-confinement boundary the L45 and L22 sections describe for the other
two routes is unchanged.

This route gained the `serving/paseo/` package: the moved command/daemon/plugin/provision modules plus the new install host part, Node acquisition, settings/convergence helper, start supervision, home lock, package-lock check, start-outcome receipt and terminal remedy. The dashboard start/status paths only observe or ensure the host — they never install, configure or reload it. Inside this shared package, the install host part (`paseo_install`) and the provision pass (`paseo_provision`) are the writers of host configuration, the plugin copy and the package tree; the start path composes the start-only `paseo_start` owner, which may start the host and write its start-outcome receipt but does not install, configure or reload it.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `mcp/src/agents_remember/serving/`               |

### Native-source claim qualifications

- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands. A comparison combined with mode is refused by _comparison_mode_refusal, with explicit query-presence checks in register_changeset_routes.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/changeset_comparison.py:16-27`; `mcp/src/agents_remember/serving/changeset.py:636-642`.

- **The comparison route's handler over its injected port.**  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:661-709`.

- **The entry route's handler: the task context alone, and an unwired process answered with a named refusal rather than an empty list.**  Anchor: "def api_review_intent_entries("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:644-655`.

- **The expansion route's handler and the module-level transport behind it (`260921-ICR-L3`).**  Anchor: "def api_review_intent_source_content("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:657-659`.

- The query parser that admits only those two.  Anchor: "def review_request_from_query("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:294-327`.

- The refusal code a process with no adapter produces.  Anchor: `review_adapter_unavailable`

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- The 404 for a candidate that does not resolve.  Anchor: `status_code`

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The registration that must precede the static mount and that takes all three ports.**  Anchor: "def register_review_routes("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:627-709`.

- The review registrar is mounted before static routing and accepts three review transport ports; the summary route is mounted separately.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:627-709`.

- The GET-only route handler over the injected port.  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:661-709`.

- **The status mapping the routes inherit from the change-set routes; the signature accepts all three typed results and reads success as `refusal is None`.**  Anchor: "def _status_for("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The 400 a selector kind outside the admitted set gets, inside the comparison handler.**  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:661-709`.

- **The 404 for a candidate that does not resolve, is not live, or has no dataset half.**  Anchor: "def api_review_intent("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The 200/refusal split the entry handler makes: `entries` serves `200`, anything else goes through `_status_for`.**  Anchor: "def api_review_intent_entries("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:644-655`.

- The registration that must precede the static mount.  Anchor: "def register_review_routes("

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:627-709`.

- The shared status mapping accepts three typed transport result classes and treats refusal is None as success.

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`.

- **The status mapping widened to the third result type, where the expansion's refusal code reaches `400` through the same fall-through as `comparison_refused`.**  Anchor: `source_content_unresolved`

Source account retained from the parked claim (anchor currency not renewed here): `mcp/src/agents_remember/serving/review.py:607-624`; `mcp/src/agents_remember/models/knowledge/review_refusal.py:15-30`.

- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands.

## Evidence

- The query, the port and the GET handler with its three answer classes. [3]
- The collaborator port and the registration before the static mount. [4]
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
- The shared naming primitive appends the same physical lock suffix. [21]
- Every-directory filtering retains lock suffix exclusion. [22]
- The launch-time proof, its six refusals and its unbound case. [23]
- The git-identity requirement that distinguishes the admitted worktree from a directory at the same path. [24]
- The ambient-binding pops and the launch-spec-only reader. [25]
- The two body-less session controls and the resolver-not-rerun fact behind the system-role choice. [26]
- The channel-level binder that refuses an unbound launch before any model work, guarding every session route. [27]
- The cases pinning the proof in both directions, including the wrong-branch workspace. [28]
- **The comparison route's handler over its injected port.** [29]
- **The entry route's handler: the task context alone, and an unwired process answered with a named refusal rather than an empty list.** [30]
- **The expansion route's handler and the module-level transport behind it (`260921-ICR-L3`).** [31]
- **The unwired-entry body: `unavailable` with the "not served rather than served empty" reason and next action — and, since `260921-ICR-L3`, its sibling for the expansion route.** [32]
- **The entry route constant, and the comment recording why it is a second path rather than a second adapter.** [33]
- The two admitted selector kinds, refused rather than mapped. [34] [46]
- The query parser that admits only those two. [35] [47]
- **The status mapping the routes inherit from the change-set routes: success is `refusal is None`, and the four candidate codes — including `subject_unresolved` — answer `404`.** [36]
- The refusal code a process with no adapter produces. [37] [49]
- The 400 a selector kind outside the admitted set gets. [38]
- The 404 for a candidate that does not resolve. [39]
- **The registration that must precede the static mount and that takes all three ports.** [40]
- **The entry port type: the task context in, one typed entry result out — and, since `260921-ICR-L3`, the expansion port beside it.** [41]
- **The unwired-entry body: `unavailable` with the "not served rather than served empty" reason and next action.** [42]
- Review route registration precedes the static mount and accepts knowledge-review, entry-list and source-content ports. [43]
- **The entry port type: the task context in, one typed entry result out.** [44]
- The GET-only route handler over the injected port. [45]
- **The status mapping the routes inherit from the change-set routes; the signature accepts all three typed results and reads success as `refusal is None`.** [48]
- **The 400 a selector kind outside the admitted set gets, inside the comparison handler.** [50]
- **The 404 for a candidate that does not resolve, is not live, or has no dataset half.** [51]
- **The 200/refusal split the entry handler makes: `entries` serves `200`, anything else goes through `_status_for`.** [52]
- The registration that must precede the static mount. [53]
- The status mapper accepts the three review result types; success is refusal absence, with distinct unavailable and missing-subject/candidate refusals. [54]
- **The new owner: which exact Git objects a committed range binds, the three absence kinds, and the one absence that may degrade to empty.** [55]
- **The caller that owns the degradation policy and (260921-ICR-L25) carries the code half's named absence instead of raising it: the two sides resolve independently, and only an unrecorded memory half empties.** [56]
- **The doc-reader entry point that publishes the unrecorded state in the body.** [57]
- **The cases that measure this route's half of the change: the recorded range bound and unmoved by a later commit, the state answered instead of a `HEAD` read with the route's own `200`, and the one-half degradation.** [58]
- **The new owner: which exact commits a master net binds, the deterministic digest, same-call currentness, and the named refusal for a missing endpoint.** [59]
- **The thin delegating entry and the pinned file view, with the shared master 400/404 mapping.** [60]
- **The served vocabulary: the generation identity, the net's `generation` + `currentness` + `scope`, and the `committed`/`working` leaf-row state.** [61]
- **The nine cases that measure this route's half of the change, through real contracts, repos and routes.** [62]
- **The parser's two admitted shapes, and the refusals it keeps: a half-named selector and an unadmitted kind still return `None`.** [63]
- **The route's optional query parameters and the `400` body that now names the "omit both" option and reports whichever parameter was supplied.** [64]
- The status mapping and the serializer, unchanged by that leaf (the mapping serves a third result type since `260921-ICR-L3`). [65]
- **The composition the task-context answer reaches, which is where the complete inventory is measured.** [66]
- **The case that admits exactly the two reviewable selector kinds and refuses every other spelling, and the case that drives the same route with no selector parameters at all.** [67]
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
- **The one mapping and the one body builder: the `400`/`404` idiom cannot differ between the two adapters.** [80]
- **The two actions the bodies gained, and where they are named.** [81]
- The expansion read's whole transport, whose docstring now states the shared mapping. [82]
- The published surface, unchanged: the three route constants, the three ports and the two parsers. [83]
- Current imported source owns this scoped route boundary. [84] [85] [86] [87] [88]
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
- The bounds of a selection and the size of the route's thread pool. [100]
- The value handed to the port, and whether it asks a focused question. [101]
- The one selection value and its refusals. [102]
- The port runs on the route's executor with cancellation and arrival bound; a disconnect and a cancellation set the event. [103]
- The route: its own executor, the unwired 503, the selection's 400 and the typed 200. [104]
- The start-only supervision the dashboard composes. [105]
- The install host part. [106]
- The host acquisition. [107]
- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands. [108] [109]
- App registers three intent handlers plus separate summary, tree and reader ports before static delivery. [110]
- Startup ordering, native held-message sweep registration, worklist-first shutdown, and awaited background teardown are explicit. [111]
- Observation and archive recovery share a completion-relative loop; prime failure is contained. [112]
- Live pacing adds post-completion rest, so interval/heartbeat alone is not a total freshness bound. [113]
- Missing wheel exits degraded; watch establishment, retry and native-watch options are explicit. [114]
- Tick cancellation drains filesystem work; state commits before subscriber notification. [115]
- Encoded argument is checked before spawn argv; null capsule parses as absent. [116]
- Non-null Codex delivery on another harness is refused by the factory. [117]
- Taskless role skips structural validation only after supplied references resolve. [118]
- Dashboard open selects before capsule resolution and constructs default-backend launch. [119]
- Source content admits attributed unchanged context only with measured requested inventory. [120]
- Leaf range returns empty for missing repository before endpoint-owner admission. [121]
- Current retirement authority includes curator and structural reviewer exceptions. [122]
- State-signal posting persists/marks before delivery, and shared action guards unmarked evidence. [123]
- Only state-signal rows may drain without an attempt clock; other boundary predicates remain required. [124]
- Authority owns order while shared-lock ledger owns rows and eviction. [125]
- Conversation authorization resolves local workspace identity and refuses non-loopback peers. [126]
- Library reopen declares legacy to preserve exact vendor identity. [127]
- Host ensure is start-only, with observation, lock, and outcome receipt. [128]
- A numbered recorded comparison is looked up exactly; code/memory ranges use its recorded sides (converted memory base when present), and the list returns those four tree operands. [109]
