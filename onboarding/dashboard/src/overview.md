# dashboard/src/ — Mission-Control Cockpit Frontend Overview

## Governing Overview
[agents-remember root overview](../../overview.md)

## Purpose

A configured Step up action stays in the shared wrapping launcher and sends canonical selection plus a reason, not preview permission overrides. The original request identity and trimmed reason survive saved taskless requests, remount and retry. A stepped-up receipt labels base mode, notes and feature chips non-applied and reports the request's selected model plus its step-up source — the host's observed model replaces it only when the host reports an applied model — with unreported mode/features explicit. This adds no chat navigation or acceptance authority.

The dashboard is the operator-facing React cockpit for server-composed task, lifecycle, enclosure, observer and native-host evidence. Its browser layer presents that evidence and requests explicitly owned operations; it does not become lifecycle, candidate-selection, certification, recovery, commit or integration authority.

The current product bar is Chats, Operations, Knowledge and File Viewer. Chats is the default; a valid knowledge-reader address selects Knowledge and a valid review address selects Operations with its review takeover. Injected retained views have no product-bar entry and establish no fresh mounted evidence.

Current Chats mounts the native Role Chats pane and embedded Paseo chat. The host owns chat navigation. The dashboard owns the role-launch controls, task/workspace/request addressing and report presentation around that frame. The older FEUI/CHATS structured-conversation architecture remains important inherited intent and child-route history; it is not the present shell's full-page Chats composition.

This overview governs the bounded `cockpit/` and `dev/` slices as well as the source-root composition. Focused children own transport/state, panel composition and visual grammar. The removed dashboard/e2e-chats route supplies no current suite or child overview.

## Hot Path Summary

Operations consumes one server-composed TaskEntry forest: authored task status supplies planned/started/aborted/completed, and only started entries receive works/paused/unknown plus an optional host eventAt. Bound in-turn or permission activity means works; a known complete host observation with no working contributor means paused; an unavailable or unreconciled host means unknown, never inferred pause. Ordered parent/children membership comes from the server's declared-list and record-master reconciliation independently of physical worktrees. For a documented subTask, an absent master can use its listing master; a present contrary or invalid master cannot. Other listed document kinds retain list placement under the existing identity/cycle guards, without validation of their own master by that path. Served disagreements stay visible on the relevant master without client repair. During unknown host observation the shell reports unavailability once, rows suppress works/paused figures and the task word remains started. The browser shares the keyed task map across the task column, reader, launch selectors and document chat, but the served status word and event age are rendered only in the task column and reader surfaces — launch selectors list a document's title/id and document chat shows launch, availability and warmup state — and neither derives a competing lifecycle. Raw Event River remains a separate diagnostic feed.

TaskSummary supplies revision-qualified prose, optional nonGoals, acceptance, completedAt and forward/reverse dependency references, with optional cycle-marked graph views. The producer generates the core schema and TypeScript/served tail; dev and manual snapshot values illustrate shape, not native derivation, task completion or host execution.

Start at cockpit/Cockpit.tsx for shared inputs, retained layers and takeover dispatch; cockpit/layout.tsx owns responsive styles and cockpit/reviewHash.ts owns review URL state. The narrow shell can scroll vertically while the change/review takeover is fixed; the older universal fixed-bars/hidden-overflow account is not a promise at every width. Retained readers and native chat still own activation and their own data.

For native role execution, follow `cockpit/RoleChats.tsx`, the role-launch model and launcher children, then `PaseoChatFrame.tsx` and its frame controller. The native Paseo role route retains canonical scope and exact request identity through RoleChatsPane composition, roleChatControls actions/storage, roleChatOptionsLoader adoption and RoleChatsView presentation. The shared RoleLauncher composes local controls with pure readiness/display and selection-repair owners; model/effort/tier and converted-memory/publication authorities remain separate. The launcher separates canonical document scope, options scope and exact execution request identity. Saved request receipts are matched by UUID rather than substituted by another execution with the same role. Result/report, Retry, Revive and restore remain tied to the selected request. Backend capacity and host execution remain backend responsibilities; a local receipt or missing browser guard is not evidence about the entire launch call path. The literal public MCP roster now contains 40 names, compared with 39 at 8d2e7547, adding role_start_set and retire_child; this source count establishes no execution result.

For task artifacts, start at `data/taskArtifacts.ts` and the cockpit's notes/requirements takeover. The shared artifact takeover selects `notes-reader`, `requirements-reader`, `decisions-reader` or `report-reader` from the artifact kind; these are takeover markers, not additional product-bar modes.

For change sets and Intent Review, start at `panels/detail-panel/changeSetBar.tsx`, `intentReviewEntry.tsx` and the existing change-set takeover. Masters request their series net with the per-leaf breakdown. Leaves expose committed change sets, live-only working change sets, and an always-present task-context Intent Review entry. Liveness selects live versus recorded review identity. The review entry's counts are changed-intent counts from the comparison summary, not changed-line counts or catalogue size.

The current card inventory link opens the existing change-set page for all changed files; measured inventory count and unavailable/unmeasured state remain distinct, and non-text file badges use the supplied inventory rather than Engine Room fixtures.

For projection contract changes, follow the producer schema and projection generator before generated TypeScript/schema or the manual snapshot. TaskEntry stage/activity/eventAt is the shared task-status input. The distinct enclosure lifecycle-operation envelope retains version, identity, component bindings, worker/approval/recommended-action facts and optional meaningful revision/task intent for operation diagnostics and recovery; those fields are not a second task activity clock or browser-created authority.

## Construction And Ownership

The task reader presents one track-and-knob Direct execution switch only on a planned-stage subTask's own page, through the existing external grant adapter. Other granted task states show bare giver words; masters and sprints show neither a row control nor a mark. The client cannot self-grant by editing TaskDocument or settings, and projection evidence never authorizes execution.

### Shell and retained surfaces

`Cockpit` wires live inputs and chooses the hash-derived initial view. `CockpitShell` owns the screen wake-lock driver and shell state/actions. Removed AR session catalog/reconciliation feeds supply no current driver. Shell state owns navigation, selected native task-entry context, rail preference and widths, and artifact/change-set takeover targets.

Operations, File Viewer, Knowledge and Role Chats are mounted layers whose visibility changes. The File Viewer comment explicitly distinguishes retained reader state from its deferred boot catalog read. Notes are mounted after first opening and remain hidden after Back, preserving their listing and open note; a change-set takeover takes screen precedence. Change-set/review takeovers are conditionally mounted through their common target. Retention claims must therefore be scoped to the layer that actually owns them.

The shell's main viewport deliberately hides overflow: panels own their scrollports. This is a composition obligation, not proof that every possible injected panel is scrollable. Rails likewise delegate scrolling to their panel children. Memoized layers, stable callbacks and identity-stable store slices express the intent to avoid reconciling entire retained surfaces on each navigation change; old timing measurements do not certify present performance.

The task list fills the left rail; attention lives behind its header bell in a bounded overlay rather than a sibling height-consuming block. Compact grouping, bell and Clear all controls share viewTabLook authority. These presentation changes retain existing action and identity contracts.

Operations' right rail selects Event River or the selected task's native document chat. The removed contextual RailChat path is not the current owner. There is no shell-mounted HighlightComposer. Native tasks come from `s.tasks` as a memoized `Object.values` array; the stable empty-array fallback belongs to `analytics?.engineProcesses`, not a second task-document collection.

### Native Chats and execution identity

`RoleChatsPane` retains launch selection, scoped options, execution receipts, request restoration and report state. It checks current document/request scope before accepting execution results. Request-addressed roles distinguish a saved unresolved request from an accepted receipt, preserve retry payloads and withhold Start/Revive when the saved request has no receipt. Options reads are activated by a complete visible selection, can be aborted, and handle the backend's launch-in-progress answer with a bounded delayed reread. This scoped reread must not be confused with the historical prohibition on background retry loops for serving-build identity.

The embedded frame obtains its descriptor from the backend, distinguishes not-configured, unreachable, origin-not-listed and backend failures, and offers explicit Retry. Its controller follows receipt-derived agent/workspace identity and retains the frame while the pane is hidden. The inherited native-route policy keeps the host's own list as navigation, the launcher strip limited to controls and its failure presentation, and requested model/effort/service-tier intent distinct from observed host values. The inherited Parent-control contract follows the current native child's SDK parent/workspace relation only while the live front value is known; that plugin-side relation was not independently re-adjudicated here.

Sprint provenance remains an inherited cross-dashboard identity requirement: `spawnRepo`/`spawnSprint` must not collapse equal role names from different sprints, command groups are sprint-specific, and unbound legacy rows stay isolated. Current native execution scope and older session-flow provenance are related responsibilities, not interchangeable implementations.

### Data, projection and grammar

`data/` owns server transport, normalization, reconciliation and browser stores. `panels/detail-panel/pageParts.tsx` owns the shared task-status words, their tones and the status key; `grammar/` owns badges, panels and markdown treatment. `panels/` composes focused task/artifact/operator surfaces. Browser caches project server facts; they are not a durable replacement conversation-history database.

The dashboard store owns bounded task bodies and pure reader preparation across navigation, keyed by canonical reference and bodyRevision; callbacks stay with the live reader. A response is retained under the revision it actually returns, and a mismatched body cannot supply current head/step/review facts. Store-owned change-set and file-diff results use bounded conditional reads, with ETag revalidation and abort/identity guards; keeping bytes is not proof of present currentness. The serving app separately owns generation-revalidated full task-body preparation. Neither cache reconstructs membership or task stage/activity.

The projection generator reads `WorkspaceProjection.model_json_schema()` and the served tail from `ServedWorkspaceProjection.model_json_schema()`. It emits the TypeScript mirror and schema, and its stale-file comparison checks committed output against freshly rendered output. `fixtures/snapshot.json` remains a manually maintained sample. Generated producer parity and sampled fixture coverage are separate claims.

The inherited contract discipline requires served-tail changes to move the producer, generated artifacts, sampled values and vocabulary/known-unsampled registries together. Typed fixture builders demonstrate generated-mirror shape conformance, not universal copying from a served sample. Current taskEntry defaults copy sampled key/id/title/reference and step counts, but explicitly supply planned stage, empty children/worktrees and zero count buckets. TaskSummary copies sampled bodyRevision, kind, form and type while explicitly defaulting collections/headerNotes and truncation flags. L127's earlier derived-form/empty-type admission is historical, not the current initializer. `AsJsonModule` preserves structural checking through JSON-module widening; `Overrides<O,T>` rejects explicit undefined at its deliberately bounded fresh override call sites.

TaskEntry uses planned/started/aborted/completed stages and optional works/paused/unknown activity, with taskCounts carrying stage and started-activity buckets. Metrics now carries ignoredHostAgents and stalenessHistogram, not lifecycle-state buckets. TopBar reads taskCounts through the shared status labels. Topology reads the bound entry through that same status-key/tone owner; an unbound enclosure is idle and not selectable as a task. The old State/LIVE_STATES/TERMINAL_STATES/ACTIVE_STATES split, awaiting-developer segment and inferred-state degradation are historical session-projection design, not the present task vocabulary or topology algorithm.

Generated task/projection shapes retain organizational super-to-leaf lineage, sprint seats and master references, optional execution-graph views, and independently mounted closeout scheduling visibility for graph-less sequential sprints. Closeout scheduling is disposable exact-current projection state: classifications, ordering, priorities, source conditions/problems and repair actions remain producer-owned. Audited discard-before-start identity, reason, timestamp and proof are distinct from completion; discarded work never increments completion. JSON Schema owns numeric/string/fingerprint/collection refinements, while TypeScript documents refinements it cannot structurally enforce.

The lifecycle-operation envelope includes schema/state-matrix versions, incoherent status and optional meaningful revision/task intent. Meaningful revision is a server observation cursor; task intent is a canonical digest. The recovery phase `recovering-private-preparation` is projected through the existing enclosure lifecycle-operation diagnostics and adds no frontend recovery command. Ledger display remains distinct from transaction authority; removal of ledger-mutation vocabulary does not mean removal of displayed ledger evidence. The inherited publication boundary permits real code and memory outputs, not invented ledger transaction outputs. Python 3.14's local `$defs` enum representation does not itself change the vocabulary's meaning.

### Change sets and Intent Review

The master viewer and bar both request `includeLeaves: true`. A landed/non-working per-leaf row opens that leaf's committed historical range without requiring its live worktree; a row reported as still working opens the leaf's working delta (`leaf.state === 'working'` selects working mode, otherwise committed). The adapter's net-only option remains available, but the inherited optimization describing dashboard master readers as net-only is superseded.

A counter read distinguishes loading, refusal/unreadable/unanswered failure, unrecorded committed endpoints, measured empty and measured counts. An unrecorded live-leaf committed range withholds its total: `+0 −0` would falsely present an unmeasured range as a zero measurement. Named refusal details carry the owner's code, its reason and the echoed repo/scope identifier where the route supplies one; the change-set client decodes no next-action field. The viewer likewise names refusal and explicitly distinguishes a change set measured empty in both code and memory halves from the pick-a-file backdrop. Unknown leaf, invalid mode and enclosure scope remain inherited distinct route refusals; they were not newly exercised here.

Intent Review is a variant of `ChangeSetTarget`. Presence of its `review` field selects the reviewer; an empty object is a task-context review, not absence of the variant. The takeover dispatch mounts ReviewSurface instead of ChangeSetViewer and forwards optional selector and recorded-history identity. Within the reviewer, All/Unexplained/Unknown changes actions separately mount ChangeSetViewer on the recorded comparison over the retained review. Card Full file and the retained dataset expression view still use bound SourceContent. The browser addresses the record it was given; the server resolves the candidate/comparison.

The task entry reads the comparison summary, never the subject catalogue. Summary availability labels the control and does not gate navigation. Every leaf has the review control: live leaves use `{}`, closed leaves use `{ historical: true }`. Working change sets alone remain live-gated. The reviewer owns catalogue loading, subject choice and explicit comparison refresh. Added/removed intent revisions, partial/unresolved intent, and unexplained/unknown attribution are separate facts. Unavailable knowledge prints a named state without counts; partial counts stay marked partial. Attribution partial/unknown has its own disclosure, and zero attribution, pending reads and dataset comparisons do not invent an unexplained count.

Review transport has its own body-first decoder. It reads JSON regardless of HTTP status and returns bodies carrying a string `state`; caller-side admission determines which states are understood. A non-route body is unreadable, and no HTTP response is a network failure. Refusal conversion preserves published facts. This is deliberately distinct from the other clients' throw-on-non-2xx semantics and is not a generic validation of every returned field.

The review cycle keys task, subject, page and live/recorded history. Sequence/cleanup and memory-input epoch checks exclude old answers, including from the compatible unshown whole-task exception. Refresh carries the displayed digest only for its exact question/read. An active live reviewer registers memory notifications on the existing stream, engages the current subject, invalidates whole-review cache and refreshes; it does not open a second poller. Family continuation remains separately admitted. This source account is not browser or semantic acceptance.

The reviewer owns its scrollport and narrow-width wrapping. Current source retains token-based amber washes, path `overflow-wrap: anywhere`, minimum-width reductions and a scrollable ReviewSurface root. Token-resolved `oklch` remains intentional: removal of hand-copied amber literals never meant that computed styles must contain no `oklch`. The inherited narrow-jump and chosen-in-this-column wording intent remains useful; earlier placement and layout measurements are historical witnesses rather than current coordinates.

### Development and verification support

`dev/` contains fixtures consumed by separate driver TypeScript projects; the pinned source has no browser-probe module and no shared window contract for one. The solution config references app, node and driver projects; the inherited real typecheck command is `tsc -b`, not a vacuous root `tsc --noEmit` over `files: []`. Driver coverage includes the e2e program; the node project historically gained Panda configuration checking.

Fixture-honesty support discovers wire vocabulary from `src/types/` or the first-line TypeScript/Browser mirror marker. Rule 1 spans all scanned files; rules 2–5 are restricted to test/spec, fixture, src/test, src/dev and e2e surfaces. Sanctioned production decode assertions are site-specific and bidirectionally reconciled, not file-wide exemptions. The named holes below remain part of its contract.

Engine Room currently composes enclosures, their process map/stack, boot timeline and diagnostics. Named seed/clone/provider dev scenarios remain projected inputs and historical captions, some explicitly naming retired visuals. They do not restore provider gauges/arcs, seed/clone arrows, provider fallback presentation or tool exposure. A retained definition or fixture title is not proof of a mounted visualization.


### Native selection and source-owner qualifications

Chats mounts one persistent RoleChats/Paseo iframe; Operations retains its own one-frame document-chat surface. The host's list, not a dashboard list of chats, owns navigation. View/result reads retain the frame. On Operations a known selection switches by trusted ar.open with the click; bounded tree preknowledge is refreshed by one batch while pane and tab are visible, and a fresh document answer corrects it. An unknown lookup keeps the application's current screen visible and inert under one waiting line. Only a confirmed agentless selection hides the retained frame behind its bound launcher. The role-launch selectors and document-chat bindings resolve the shared entries' ordered children and canonical references; they do not reconstruct hierarchy from a second task-document/series catalogue.

A slow host or native drawing answer remains waiting while the application answers pings. Recovery URL loads require application-ping silence, explicit Retry or a returned host; a plugin explicitly unable to open agents keeps its separate URL-only path. With the current plugin, input belongs to the selected native screen once on-chat is reported, the waiting line stays through drawing, and the application's own failed-load pane/Retry ends that wait without dashboard-invented failure prose. A less capable older plugin still switches and its notice names provisioning and any early-answer limitation. Draft/scroll preservation is only the host's native behavior, not an extra dashboard promise.

The plugin's Parent action retains the live selected-source/relation checks. Canonical selection, exact launched-request identity, dynamic model/effort/tier validation and observed host values remain their existing owners; chat cache and display messages acquire no task acceptance or launch authority.

The dashboard frontend is the operator-facing React cockpit. Product views are native Chats, Operations, Knowledge and File Viewer, with notes/change-set/review takeovers; task detail is the Operations layer's persistent panel, not a takeover. Retained internal/dev layouts project observer and provider evidence; the terminal-catalog and adapter/control owners are not in the pinned source, and a retained layout does not add a product-bar entry.

- [data overview](data/overview.md) — retained projection state, task/document identity and the
  review, change-set, file and knowledge transports, with their authority boundaries.
- [panels overview](panels/overview.md) — shared panel composition.
- Existing focused child overviews under data, grammar, and panels own their routes. The bounded
  `cockpit/` and `dev/` source slices remain governed here rather than gaining thin overview files.
  The former dashboard/e2e-chats sibling and its historical harness journey are not a current source route or suite.

No terminal/catalog create client exists in the pinned source: there is no `data/terminalOpen.ts` and no `/api/terminal/` caller, so the opener's exact request/response-identity acceptance rule, the session store's commit-and-broadcast rule and the local-row prohibition are historical requirements with no current owner. Native role starts have their own role-launch adapter and receipt authority.

The terminal catalog and adapter/control routes are not registered in the pinned serving source; no retained terminal/session surface reads them. Native role-chat identity and steering instead use role-launch receipts, the native host and the trusted frame protocol. Browser projection/cache is not a replacement conversation-history database.

The current product Chats layer mounts `RoleChatsPane` in `MainLayers`, backed by the shared native `PaseoChatFrame`, and stays mounted while other dashboard views are shown. The host's own chat list and screen, not the retained controlled-session cockpit or `ConversationSurface`, own this product destination. Operations has its separate retained document-chat frame; neither route promises an additional dashboard conversation-history database.

The product bar contains Chats, Operations, Knowledge and File Viewer. Notes Reader, Change-Set Viewer and review are focused takeovers with their own owners; task detail is the Operations layer's persistent panel, not a takeover. Engine Room, Memory, Topology and Hangar have no product-bar entry; retained layouts can be exercised through injected initialView or dev/test composition. Their existing internal overviews are not an additional production destination.

- Chats is the opening view and there is exactly one full-page Chats destination; Operations is a product destination (260928-MIK-L79).
- The shell owns its wake lock and navigation state; native host/reader owners supply their respective data.

## Invariants And Boundaries

- Present navigation has four destinations and one full-page native Chats destination. Injected pages and historical structured Chats must retain their own scope.
- Shared task-map and bounded resource ownership lives in the dashboard store. Browser projection/cache and observer rendering do not acquire server transaction authority.
- Focus/inspection may address landed history; inherited live-row action and reload routing must not silently convert a historical row into a live actor.
- Exact request, document, workspace and execution identity must survive restore and asynchronous results. Requested launch intent is disclosed separately from observed host facts.
- The hosted terminal opener is gone from the pinned source; its retained contract was to post to `/api/terminal/{encodedSessionId}` and accept only a parseable successful response acknowledging exact session/kind/harness identity, with raw terminal responses claiming harness/control facts treated as protocol contradictions and the session store committing and broadcasting only after acceptance. These hosted-session semantics do not describe native role-launch transport.
- Reliable submission and withdrawal are retained requirements of the removed hosted-session transport — request/epoch identity, no blind resend, no manufactured authoritative success — with no current dashboard implementer. User submissions, agent bus messages, lifecycle/control commands and adapter-interaction answers remain distinct paths; agent communication must not collide with operator paste/input.
- Inherited structured-session presentation keeps inspectors supplementary, diagnostics read-only and default-off, PTYs mounted across focus/transient handoffs, and ended rows from acquiring live sockets. These are scoped hosted-session responsibilities, not a claim that the current native Chats frame renders the old structured stage.
- Missing transport, capability, history or measurement facts remain explicit. Unknown, unavailable, unrecorded, measured-empty and refused are different states.
- Review subject availability and summary counts do not gate the task-context entry. Liveness selects its record; the browser does not choose the candidate.
- Review refresh claims belong to the exact question/read/comparison they describe. Displayed failures and retained coherent generations must not relabel an old answer as a new subject's answer.
- The shell delegates scrolling to panels. Narrow-layout source repairs do not establish fresh viewport measurements.
- Generated producer contract, manually sampled coverage, runtime schema refinements, static fixture restrictions and execution verification remain distinct evidence classes.

## Historical And Verification Limits

This proposal is source-only on the named checkout. It reports no test execution, typecheck result, mounted capture, browser journey, performance result or delivery acceptance. Original reference identities and excluded route/status/coverage metadata belong to the parent's preservation operation.

The inherited card reported no configured Domain Documentation and no cross-repository implementation authority. Same-repository source, reviewed task evidence and recovered history were its authority; Toad/T3 informed framing only. Memory settings, domain-provider configuration and recovered historical witness packs were not consulted here, so these remain attributed historical provenance statements.

FEUI-L8 and CHATS-L1–L7/L4 describe the earlier full-page session cockpit and structured ConversationSurface: reliable composer/pop-back, interaction answers, lifecycle controls, capabilities/bus/status, history library, exact-turn interrupt, optional inspector and read-only PTY diagnostics. Active transcript and previous-conversation library were separate normalized server capabilities with no durable browser database. Sub-agent refs, lane-focus survival across LRU eviction, child-library grouping, verbatim partial-history notes and combined singular/plural pending-interaction attention are enduring scoped intent. The current shell instead mounts native Role Chats. Their old child-route behavior and broad multi-harness claims were not freshly verified.

Explicitly retain the CHATS L5-Facing Register's named limits: interrupt capability gating was attempt-and-reflect on L3 evidence pending a control-capabilities GET or L1-view refresh; virtualization/scale baseline and environmental faults E1/E2 were recorded there. The register's historical witnesses were not examined, so this proposal neither closes those limits nor declares them present native-frame defects. The inherited UA-1 history-capability claim is historical scope, not new acceptance.

The L33 landed-leaf admission/default-collapse change was recorded as withdrawn by `a9a1a41b`, with a direct emergency commit and no curator pass. The later physical-live-worktree Operations filter is itself superseded: current LifecycleList consumes every served task entry and follows its parent/children forest, including task entries with no worktree. The retained collapsed-key store is separate from ephemeral terminal folds, which stay open around the selected ancestry. Do not restore the withdrawn `N landed`, second persisted opened-set or tooltip claims. Historical 534-document/167-entry and 161-row-subtree figures are not current counts. The separate per-leaf change-set breakdown remains outside this task-membership change.

Review history includes L22's unreachable subject props, L45's server catalogue gating, L2's live task-context entry and L17's catalogue invalidation/refresh account. Those descriptions must not be merged into today's entry: its separate summary control reads no catalogue, has no subject picker or refresh of its own, and exists for closed as well as live leaves. L16's stale-header problem was routed to R17/R24; current ReviewReadCycle contains question/sequence guards. A01/A13 browser journeys were separately routed to R25 with R24/R17 and remain unverified here.

B3/B7/F2 historical narrow-layout evidence must retain the distinction between the inner review-workspace root and the reviewer's review-surface root. Round 2's claim that the residual was all outside the reviewer was withdrawn: 51 of 64 off-edge elements were attributed inside the reviewer, with 13 chrome elements outside. Round 3 reported reviewer overflow 51 to 0, panes 565 to 294 pixels, one scrollport and wheel movement 0 to 800 pixels. These figures, the earlier jump at y=1183 and root-width observations are historical, not fresh measurements. The 13 shell-chrome elements and shell-wide scrollport consequence were routed to R24. Current wrapping/scrollport source does not certify that those chrome issues are resolved.

B1's removal of raw amber literals is different from eliminating token-resolved `oklch`. The historical computed `oklab` wash and hue-215 search are not remeasured. The inherited live-thinking indicator, file-size claims and acceptance pins likewise provide historical implementation context, not present pass receipts. Pending/not-yet-landed pickup description and attribution-only inbox consumption remain inherited projection intent, not frontend authority over producer sweep predicates.

Fixture guard limits remain named: never-marked inline response modules (`data/changeset.ts`, `data/files.ts`, `data/notes.ts`) escape vocabulary discovery; marker loss differs from never having a marker. Rule 4 omits element access, await, new and non-null expression shapes. Generic helpers can defeat rules 1 and 4 together; type predicates/assertion functions narrow without casts; correct property names with explicit undefined evade name-based rules. Broadening discovery to headers mentioning Python was historically rejected because it also captured option types. `Overrides` currently binds fresh override literals in fixtures/wire.ts only; widened variables, nested required leaves and other Partial parameters remain outside it. The older wire/conversationWire two-module scope is historical.

The historical project-wide flag experiments reported 601 errors across 81 files for `noUncheckedIndexedAccess`, and 222 across 71 for `exactOptionalPropertyTypes`; these are reasons recorded for scoped devices, not current diagnostic totals. The earlier within-half duplicate-state/compile-time-overlap discussion belongs to the retired session vocabulary; it is not a current TaskEntry partition guarantee.

Historical test policy records a 20,000 ms Testing Library condition guard, 120,000 ms test/hook hang guards, fake time for product delays, and negative assertions after the relevant response/effect/timer opportunity. `loadIndependence.test.ts` owns a bounded source-pattern check with explicit marker/detection limits. None changes browser performance requirements or establishes current passing tests. Generator stale checks, sample coverage assertions and prior clean `tsc -b` claims were not executed here.

Serving-build identity retains the inherited distinctions: definite advertised/executing fingerprint mismatch offers explicit reload; absence is unknown; a new serving boot can cause one chooser reread and explicit socket reattach rather than SSE-loss retry loops. Reattach preserves mounted xterm/durable tmux and transport close is not terminal exit. Optional Python digest/interpreter/package root are diagnostics, never update/candidate-selection authority. Those data-owner paths were not independently retraced in this bounded adjudication.


### Retained source and evidence qualifications

The live-leaf "committed" change-set read used to swallow its own refusal detail, so a **refused** read and an **unanswered** one rendered identically — the defect `260921-ICR-L16` routed to this route's owners and R12/R24 both landed without taking. `260921-ICR-L32` applies the R16 treatment here: `data/changeset.ts` no longer clears the counters and stops on a rejected counters read, it carries the refusal's own code and reason through to the caller, while `data/files.ts` is the exception — its `FilesApiError` keeps only the status code and HTTP status, so the file reader is shown no reason. A read still in flight is a **third** state and is reported as one, so loading, refused-with-a-named-code-and-reason, and answered-with-counts are three distinguishable renderings rather than two. The rendering half lives on `panels/detail-panel/changeSetBar.tsx`; its source cases drive the click and assert the rendered reason. The route typecheck command is `tsc -b`; the earlier clean result is historical, not a new run on this pair.

> **WITHDRAWN by `a9a1a41b`, recorded by the `260921-ICR-L34` curation.** The paragraph below describes
> the landed-leaf admission and the collapse hook's second half — a change commit **`a9a1a41b`**
> (*"Revert L33's operations-list change; clear the pre-existing ruff-format red"*) took back out. That
> revert was a **direct emergency commit with no curator pass behind it**, so this route went on
> describing a deleted module: At that withdrawal epoch, `panels/lifecycle-list/landedLeaves.ts` existed in **neither** recorded tree (and
> its sidecar was deleted by this curation), the recorded `LifecycleList.tsx` was 1189 lines again with no landed pass
> or default-collapse rule, `hierarchy.test.tsx` was 355 lines, and `useCollapsedTaskGroups.ts` had
> returned to one collapse set with `toggleCollapsed(key)`. These sizes are historical observations, not current file-size measurements. The **second** half of this section — the
> per-leaf breakdown in the change-set readers — is **not** affected by the revert and stands.

**The review surface's raw colour literal is gone (B1), and the claim is stated in the form that is
true.** `panels/review/FamilyTree.tsx` carried the only two raw literals — `oklch(0.82 0.16 75 / 0.08)`
and `… / 0.16`, `--amber`'s channels copied by hand — and B1 replaced them with an `AMBER_WASH(percent)` helper
stating `color-mix(in oklab, var(--amber) N%, transparent)`. The present file retains the 8%/16%
colour-mix declarations inline rather than that named helper. The interpolation space is the reason it
matters: an `oklch` mix interpolates the **hue**, which is how the accepted page's own selected row first
came out visibly teal. **What is false as worded, and must not be repeated:** *"zero `oklch` users remain
in the review surface"* — the dashboard's own tokens are defined in `oklch` (`styles/tokens.css:8-23`) and
`getComputedStyle` resolves `var(--token)`, so token-resolved `oklch` values are everywhere in the surface
**by design**. **What the dated acceptance measured:** the raw amber-wash literal was gone, the wash computes as
`oklab(0.82 0.041411 0.154548 / 0.08)` through `var(--amber)`, and hue **215** appears nowhere in the
review sources. A reader scanning computed styles for the word `oklch` will otherwise conclude the fix
failed.

Historical pre-TaskEntry topology read-view account, retained as a quotation rather than a current implementation or typecheck claim:

> The subtle part is `STATUS_BY_DECLARED_STATE`, a `Partial<Record<string, ConstelStatus>>` **read
> view** over the same table. Indexing `Record<State, …>` directly types the miss away — `tsc` hands
> back `ConstelStatus`, never `undefined` — which would make `?? UNCLASSIFIED_STATUS` in
> `lifecycleStatus()` read as deletable dead code. The read view is what makes that fallback
> load-bearing: delete the `??` and `tsc -b` fails at that line. Remove the alias instead and the
> compiler goes quiet while an unclassified state's `undefined` flows onward.
> `noUncheckedIndexedAccess` would say the same thing project-wide; it is not on (the earlier diagnostic reported 601 errors
> across 81 files; those are not measurements of this pair).

Current topology instead resolves TaskEntry status through shared taskStatusKey/statusTone; it has no lifecycleStatus or STATUS_BY_DECLARED_STATE owner.

- `test/servedProjection.ts` — `resolveJsonModule` widens every literal in the payload (`"running"`
  becomes `string`, `3` becomes `number`), so `snapshot.json` can never be *assigned* to a mirror
  that types its vocabularies as literal unions. The old reflex was a double cast
  (`snapshot as unknown as WorkspaceProjection`), which turned off assignability and
  excess-property checking together.
  `AsJsonModule<T>` applies exactly the import's widening to the mirror and nothing else, so
  `asServedProjection()` is a full structural check of everything widening does not touch. Every
  test reading `snapshot.json` must come through it; a second `as unknown as` elsewhere silently
  re-opens the hole for that file.
- `test/fixtures/overrides.ts` — `Overrides<O,T>` guards required-field overrides at fresh call sites in `fixtures/wire.ts`; for example, the current header names `taskEntry({ stage: undefined })`, not a lifecycle factory. It is not project-wide exact optional typing and does not close widened-variable, deeper-property or other-Partial inputs. The former lifecycle example and wire/conversationWire scope are historical. The earlier recorded project-wide diagnostic of 222 errors across 71 files remains a historical experiment, not a measurement of this candidate.
- `dev/fixtures.ts` delegates projection, provider, enclosure and event construction to `test/fixtures/wire.ts`, passing gallery-specific defaults explicitly rather than maintaining a second required-field list. `engineRoomProjection` supplies scenario processes/workspace and the official ledger over `EMPTY_ANALYTICS`. Native tasks/counts are projection-root fields; no `metricsFor` rollup or harness-catalog stub remains. `dev/` remains fixtures, not a production authority.

The dashboard route absorbed the L7 live-thinking change on top of the L8 split: that historical conversation-timeline family rendered one coalesced live `thinking` indicator per active turn (`collapse.ts` stable-row refactor + `ThinkingItem` animated indicator), with acceptance pins in `liveThinking.test.tsx` and `collapse.test.ts`; none of those modules or tests exists in the pinned source, whose Chats route mounts the native `RoleChatsPane` frame instead. The earlier L7 report described a clean file-size result. The project wrapper defines the detector's TS/TSX scope; this paragraph supplies no fresh file-size or rule6/full-final acceptance.

**Superseded 2026-09-20 (260915-KS-L45): the subject stopped being a prop, because as a prop it was
never supplied.** The L22 increment gave `DocChangeSetBar` optional `selectorKind`/`selectorId` props
and gated the entry on `live && selectorId`; no production caller supplied either, so the reviewer
takeover described above was unreachable by navigation. The props are gone. The bar now reads its
subject from `GET /api/review/intent/entries` through the `data/review.ts` client's
`intentReviewEntries(repo, master, leaf)`, carrying the whole catalogue via a `useReviewCatalogue` hook (ICR-R09: every recorded subject with per-row presence and totals, not `entries?.[0]`).
At that L45 epoch, a refusal, empty list or rejected promise left the subject undefined and no subject meant no button. The later ICR-L2 task-context entry below supersedes that subject-dependent admission: a live leaf can open the review without a supplied selector. This earlier account is historical, not the current button predicate.

**Route meaning changed: the reviewer entry no longer depends on the server offering a subject.**
`panels/detail-panel/changeSetBar.tsx` gates the button on liveness alone and sends an empty review
target when the entry read answers with nothing or refuses, so the task-context target reaches the
cockpit for every live leaf; `cockpit/Cockpit.tsx`'s takeover dispatch already forwarded an optional
selector, and its review branch now records that fact in a comment. `panels/changeset/ChangeSetViewer.tsx`
widened `ChangeSetTarget.review` to carry an optional selector, where the field's **presence** still marks
a review target and an empty object is the task context. The client (`data/review.ts`) and the review
panel (`panels/review/ReviewSurface.tsx`) carry the rest: the inventory's wire types, an optional
comparison identity and the then-introduced inventory-state renderer. The current ReviewPanes/ReviewWorkspace composition below supersedes that renderer; this is an L2 history account, not a current three-state inventory caption.

The current review surface delegates its displayed payload to `ReviewWorkspace` and keeps comparison-bound changed-file navigation distinct from technical details. The former all-three-inventory-states caption is not a statement of this later renderer.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/`                                 |

### Native-source claim qualifications

- One generation-keyed frame shows native progress with held input and a bottom waiting line, rather than remounting on selection.

Source account retained from the parked claim (anchor currency not renewed here): `dashboard/src/cockpit/PaseoChatFrame.tsx (EmbeddedFrame)`.

- [State and authority architecture](data/overview.md) — companion documentation, not a code-anchor or fresh execution witness.
- [Panel composition](panels/overview.md) — companion documentation, not a code-anchor or fresh execution witness.

- ReviewPanes delegates comparison-bound review presentation to ReviewWorkspace and keeps changed-file navigation bound to its shown payload; the distinct EngineRoom dev scenario group is declaration/history evidence, not mounted provider visualization.

Source account retained from the parked claim (anchor currency not renewed here): `dashboard/src/panels/review/ReviewSurface.tsx:328-392`; `dashboard/src/dev/scenarios.ts:43-119`.

## Evidence

- Master validation in placement applies only to documented subTasks; other listed kinds retain list placement under existing identity/cycle guards, not a kind-rejection or own-master-validation rule. [73]






- The root already says Engine Room has no product-bar entry and is exercised through injected initialView. The changed so — source ownership, not executed visual proof. [42]
- The root already says Engine Room has no product-bar entry and is exercised through injected initialView. The changed so — source ownership, not executed visual proof. [43]
- The Knowledge destination in the registry. [1]
- A reader URL opens the shell on the Knowledge view. [2]
- The retained Knowledge layer renders the reader beside the path tree; the former transient ViewBody case is gone. [3]
- The header count itself. **Withdrawn in part:** this row cited a tooltip that stated *what* the count counts ("task entries this list carries"), and the L33 revert removed that tooltip with the landed-leaf change, so the h2 is again a bare `Tasks · {count}`. A reader must not read the number as "task entries" on the strength of this card. [4]
- Both master readers now ask for the per-leaf breakdown. [5]
- Shell navigation, persistent layers and shared drivers. [6]
- State and authority architecture. [7]
- Panel composition. [8]
- Fixture-honesty sweep, its five rules, its scanned roots, and the unmarked-module blind spot. The third anchor is the guard header's own question, quoted as it is written; this row previously carried a paraphrase that occurs in no file. [11]
- Historical lifecycle topology grammar: the former unclassified-state fallback is not the current TaskEntry status algorithm; the constellation palette is a separate retained concern. [13]
- JSON-module widening and the override type that survives `exactOptionalPropertyTypes` being off. [14]
- Public lifecycle recovery commits contain only real code and memory outputs. [15]
- The target variant that turns the existing takeover into a review. [18]

- At the Cockpit target dispatch, presence of the review field mounts ReviewSurface instead of ChangeSetViewer, and an empty object is the task-context entry. Within that reviewer, a separate comparison-bound changed-files overlay can mount ChangeSetViewer.  Anchor: "never mounted for one, so no change-set" [19]


- The root review target mounts ReviewSurface. Historical ICR-L3 inline inventory openers addressed an entry's content; current InventoryLink opens All changed files on the comparison-bound change-set page, while card Full file remains bound SourceContent.  Anchor: `ReviewSurface` [21]

- **The reviewer entry: offered for every leaf; since `260921-ICR-L47` it carries no subject (the reviewer chooses one) and shows the comparison's changed-intent counts.** [22]

- **The shared liveness predicate gates Working and selects live versus recorded Intent Review identity; it does not gate Intent Review availability.** [23]

- The shared catalogue hook takes repository/task context and calls the existing subject catalogue client. [24]
- **The entry that is offered for every leaf; since `260921-ICR-L47` the subject catalogue is read by the reviewer on entry (not by the task entry), and never gates it.** [25]
- **The review target whose selector is optional, with presence marking a review and an empty object meaning the task context.** [26]
- **The takeover branch that mounts the surface for a target with or without a selector.** [27]
- **The client's inventory types and the request that omits the selector when there is none.** [28]
- The case that measures the browser half: no subject offered, and the target is still a review. [30]
- **The shared client this route deliberately does not change, whose throw-on-non-2xx is right for the other serving routes.** [31]
- **The review route's own decode: the body is the answer whatever the status.** [32]
- **The one renderer every non-review state goes through.** [33]
- Current imported source owns this scoped route boundary. [34]
- The route's Role-chats pane owner. [35]
- The route's embedded chat frame. [36]
- Async conditions share one hang guard. [37]
- Test and hook completion share hang guards. [38]
- Bounded source guard scans dashboard test and support files. [39]
- This source owns the route’s Investigator selection or execution boundary. [40]
- The root already says Engine Room has no product-bar entry and is exercised through injected initialView. The changed so — source ownership, not executed visual proof. [41] [42] [43]


- Native execution results are scoped by document and request identity [46]
- Frame descriptor activation and explicit retry are separate from retained frame identity [47]
- Every leaf's review entry selects live or recorded identity independently of summary availability [48]
- Intent and attribution counts have separate partial/unavailable treatment [49]
- Review transport reads route-state bodies irrespective of HTTP status [50]

- Historical Operations admission: physical live-worktree filtering is superseded by the complete served TaskEntry forest; this retained reference is not current task-membership evidence. [52]
- Collapse state has one persisted collapsed set [53]
- Historical lifecycle partition generator account: the retired state/metrics partition is not the present task model. Generated schema/TypeScript stale comparison remains a distinct source responsibility. [55]
- Wire discovery and fixture scope retain named blind spots [56]
- Required-field override protection has explicit fresh-literal/depth/module limits [57]
- Historical lifecycle topology account: the former unknown/inferred-state degradation is not the current bound TaskEntry status mapping. [58]
- Engine Room's present body composes enclosure map, stack, boot and diagnostics [59]

- The surviving dashboard TypeScript solution declares its project references; the removed browser-probe module contributes no current import contract. [60]
- Cockpit review dispatch and comparison-page overlay have separate owners; card Full file remains bound source content. [61]
- Review inventory navigation displays the measured listed total or unmeasured state; change-set badges derive non-text identity from the supplied inventory. [64]
- Preclick knowledge is bounded and polling belongs to visible pane/tab lifetime. [63]

- Historical session State/phase vocabulary and lifecycle-state Metrics buckets, superseded by TaskEntry stage/activity and TaskCounts. [12]
- The generated lifecycle mirror carries the cursor beside coherent identity and version fields.  Anchor: "export interface LifecycleOperationProjection {" [16]
- The fixture supplies a meaningful revision for the sample operation.  Anchor: "\"meaningfulRevision\": 1," [17]
- Unknown chat ownership does not hide the frame; only confirmed absence does. [62]

- Authored stage wins over host observation; only started tasks receive bound contributor activity and eventAt. [65]
- Declared task sources become one entry forest with worktree binding kept separate from task admission. [66]
- Task-status words consume served activity/stage, while the shared display clock formats event age rather than deciding task state. [67]
- Retained body responses are keyed by the revision actually returned, not the requested revision. [68]
- Conditional reads retain only admitted successful bytes and guard abort/identity before publishing a response. [69]
- Task fixtures copy sampled identity/content fields while explicitly choosing planned stage and empty collections/count defaults. [70]
- Topology maps the bound task through shared status presentation; an unbound enclosure is idle. [71]

- A configured Step up action stays in the shared wrapping launcher and sends canonical selection plus a reason, not preview permission overrides. The original request identity and trimmed reason survive saved taskless requests, remount and retry. A stepped-up receipt labels base mode, notes and feature chips non-applied and reports the request's selected model plus its step-up source — the host's observed model replaces it only when the host reports an applied model — with unreported mode/features explicit. This adds no chat navigation or acceptance authority. [72]

- The four-entry product bar and retained product layers remain distinct from injected views; review URL state can override ordinary opening view. [44]
- The actual takeover dispatch selects intent-review versus changeset from target.review and forwards optional subject/history. [20]
- The common takeover forwards optional selector and live/recorded review history; its URL owner carries task/history, not subject selection. [45]
- Question/read identity and memory-input epoch prevent superseded responses from display or inappropriate unshown reuse; live-watch notification is separately wired by the surface. [51]
- Responsive shell style and the actual narrow railed/takeover consumers are separate from reviewer-local scroll ownership. [74]
