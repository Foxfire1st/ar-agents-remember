# Engine Room Enclosure Process Map

## Governing Overview
[panels/ overview](../overview.md)

## Purpose

`dashboard/src/panels/engine-room/` presents server-composed worktree enclosures as a process map: integration/source refs, code and external-memory worktrees, code ⇄ memory ledger links, worktree/sync/integration conduits, landing and closeout progress, missing observations, recoverable gates, attention, and terminal conflict. The route joins and presents served facts; it does not acquire Git facts, decide safety, or execute worktree operations itself.

The current composition is enclosure-only. Provider stacks, gauges, clone arcs, provider-specific block/dropout overlays, fault/reindex effects, and provider boot checklist rows have left the rendered surface. Provider-shaped projection fields, fixtures, helper definitions, and old comments can remain without restoring those visuals. The historical all-eight-prototype-modes account therefore describes the former design, not current visual parity.

The map preserves the distinction between observed, derived, planned, missing, stale, and otherwise unresolved facts. Provisional pre-contract enclosures must communicate their block rather than impersonate a live enclosure. Ordinary affordances and canvas recovery labels describe availability; the diagnostics gate responder is a separate interactive boundary.

## Hot Path Summary

`EngineRoom.tsx` subscribes separately to process and ledger analytics using `stableEquals`, reads lifecycles, and memoizes `buildEngineRoomModel`. The builder joins each process to its optional lifecycle and gate, exposes `worktreeGroup` as `enclosureKey`, then sorts by phase and leaf/task label. It no longer builds a workspace provider stack or legacy provider fallback.

The selected worktree group resolves to its process, falling back to the first process when the selection is unavailable. The parent finds the official ledger by repository and composes the header, enclosure list, process-map stage, and timeline/diagnostics column inside a fill panel. Store generation keys the process map for scenario-reset remounts; this is distinct from the stable enclosure identity used by the model and selection.

`EnclosureProcessMap` owns the effects-gated backdrop and teardown records. Abandon wraps the whole canvas in a dim/desaturated dissolve. Successful cleanup reports a landed record and leaves the official side bright; worktree-side disappearance depends on the projected refs and canvas transitions. The old HTML fleeting banner is gone.

`EnclosureCanvas` resolves presentation state through `scene.ts`, paints structural layers, then paints failure pointers above the nodes. Its separate sibling effects SVG shares the 1200 × 660 view box and carries coupler surge and attention breathing. Both SVG roots feed the timeline selector.

External memory is present in the scene only when `memoryMode === 'external'` and a memory-worktree object exists. Worktree materialisation means an observed or derived ref. A ledger-map running before memory materialisation selects the memory-source scan; worktree-add running before code materialisation selects the code-source scan, with memory scan priority. A missing memory-worktree fact or blocked ledger-map ghosts only the ledger-map conduit.

Fleeting is derived from a missing-fact string matching “contract not yet written.” A stale base requires a positive code-source behind count, blocked presentation, and fleeting. The former provider-plan distinction no longer overrides fleeting. Memory movement requires a real memory worktree and a positive memory-source behind count: before blocking it yields the moved notification; after blocking it yields the live memory gate only when ledger-map is blocked. This does not reclassify a code-side blocked sync edge.

Terminal presentation is selected by `integration-blocked`; the STOP itself additionally needs a blocked integration edge. That edge is excluded from ordinary edge gates. Terminal non-fleeting scenes suppress recovery chips. Other blocked edges retain steady gates; failure/reroute flashes are separate from gates. Recovery labels deduplicate next action, retry setup when retry arguments exist, and enabled action names. Fleeting displays at most three choices.

Landing chips omit missing refs and appear only in the listed landing phases or when an integration strategy is present. Stale remote observations remain inspectable with stale tone/text and optional age. Directional flow eligibility requires observed refs: origin-feat makes push available; an observed merged PR advances to pull; observed pushed origin-mem-main advances to carry and push-mem. Carry and push-mem can both be active at that frontier. The closeout train appears only during closeout-pending and reads code → onboard → quality → memory → ledger.

## Construction And Ownership

- `buildEngineRoomModel.ts` and `engineRoomTypes.ts` own the React-free join and enclosure view shape. Server process semantics remain owned by the observer projection and reducer; current implementations of the process builders live in `observer/reducer_impl/_processes.py`.
- `EnclosureCanvas.tsx` owns structural composition. `scene.ts` owns presentation predicates; `geometry.ts` owns coordinates, straight paths, state treatments, and polarity derivation. `sceneLayers.tsx` owns ordered render layers and their conditional presence.
- `engines.tsx` now renders branch nodes, despite its historical filename. Planned nodes are hidden/offset, observed and derived nodes settled, missing/stale/unknown nodes use distinct opacity treatments. Detaching movement applies when the ref's presentation opacity reaches zero. Labels truncate to fit while hover titles retain details.
- `conduits.tsx` renders only edge kinds with geometry: worktree-add, ledger-map, sync, integration, and integration-mem. Worktree-add and sync share a centerline. Every settled path is straight, including replay integration; replay survives as a data attribute and hover explanation. Running conduits alone receive draw markers, arrowheads, and effects-gated packets. Planned and retiring conduits fade out.
- `ledger.tsx` owns chain-link couplers and accessible click/Enter/Space popover triggers. These links represent the memory.md code ⇄ memory mapping, not the task-series contract. Official rows come from the repository's `LedgerNode`; worktree rows and counts come from the process node. The worktree coupler's visibility follows memory materialisation.
- Ledger preview shows eight rows, expands to the served window, and reports older rows remaining in memory.md. The server I/O owner in `serving/projections/snapshots_impl/_analytics.py` bounds both windows to 25 rows and probes commit metadata best-effort, keeping the reducer pure. Missing, invalid, or unreadable worktree ledgers yield an empty window; unreadable official ledgers are omitted. Missing local commit metadata, failed Git probes, and timeouts retain hashes without invented messages or dates. The display has six data fields plus a separate ⇄ seam cell; dates are compacted by string slicing without viewer-timezone conversion. The popover anchors high, opens downward without flipping, and uses its styled scroll area for overflow.
- `remote.tsx` owns positioned origin chips and the PR merge arrow. Code refs occupy the top dock and memory-main the bottom. Planned is muted/dashed, live amber, landed mint, and stale explicitly distinguished. Full labels and freshness detail remain in hover titles.
- `BootTimeline.tsx` owns boot, steady, and teardown sequences. Boot leads with “Contract anchor,” then code worktree and external-memory ledger/worktree materialisation; non-external memory is shown as skipped. The contract row is currently hardcoded complete, including for provisional input; it is not proof that a contract exists. Dispose phases include integration-blocked and carryover-pending. Conflict marks closeout complete, push blocked, and later steps pending. Abandon skips landing steps and marks disposal complete.
- `DiagnosticsPanel.tsx` owns commit fact chips, phase/health/setup/heartbeat text, completed and failed phases, missing observability, source files, and optional source-lineage state with its summary in a hover title. Cleanup and abandon display “powering down” and mute completed-phase marks. A lifecycle ID plus a gate whose kind matches closeout/push/integration/cleanup mounts the compact `GateResponder`; otherwise actions render as `Affordance`.
- `useShouldAnimate.ts` gates effects on document/window availability, the document effects flag, and OS reduced-motion preference. It reacts to effects-attribute and media-query changes. `useEngineTimeline.ts` owns DrawSVG reveal/retraction, MotionPath packets, scan expansion, surge, attention breathing, terminal flash, and one-shot refused flashes. Its signature includes phase, running kinds, landing state/fact-state, failed/stale kinds, and memory mode; worktree group separately participates in effect dependencies. Completed draw stamps prevent repeated sweeps, are cleared on departure, and are set only after completion to avoid the documented StrictMode interruption.
- `useElementVisible.ts` supplies an IntersectionObserver gate, initially visible and remaining a no-op where the observer is unavailable. The timeline pauses context-recorded tweens off-screen and resumes them without rebuilding merely for visibility. The backdrop pauses/plays on visibility; the header's repeating phase pulse additionally requires visibility. `EngineFxOverlay.tsx` now owns surge and attention only.
- `styles.ts` re-exports the six semantic domains: layout, stage, ledger, flow, remote, and backdrop. The historical semantic-axis split remains an ownership rationale; old physical-line counts are not current size measurements. Fixtures, render tests, model/gate tests, and dev scenarios are specimens and source-level assertions, not execution receipts.

Landing retains three render-position tiers: the integration/source line, a middle feat/source tier shown only when `showLanding` is true, and the worktree tier. `EnclosureCanvas` mounts `BranchTier` with that scene condition; branch nodes obtain their displayed branch text from the projected ref rather than a hardcoded `main` label. Memory tiers additionally depend on the memory ref’s presence.

## Invariants And Boundaries

Server semantics and client presentation remain distinct. The client may derive visual predicates from served states, but this does not authorize new lifecycle decisions, Git operations, clocks, or fabricated observations. The server still carries provider-related facts and produces provider seed/clone edges; their absence from the current rendered geometry is a surface retirement, not proof of removal from the serving pipeline.

Refused polarity is derived from edge state, never a dedicated payload field: failed → red, stale → amber, only for cgc-seed, grepai-clone, integration, and integration-mem. The overlay must also obtain a shared path. Because current geometry omits provider seed/clone kinds, those retained helper arms do not produce seed flashes. Integration paths retain the transient flash and terminal STOP specimen behavior. No conduit stamps a refused-polarity attribute; the flash overlay carries its own derived polarity.

The inspected server edge builders emit worktree-add, cgc-seed, ledger-map, grepai-clone, and sync, not integration or integration-mem. The retained integration arms have a documented historical reason: integration belongs to the projection's commented kind vocabulary and the integration lane/conflict scenarios were authored as fixture coverage. Integration-mem is the companion mirror, absent from that comment vocabulary. This is inherited design intent, not a promise to add a producer. The projection forbids extra fields, but kind/state are strings with documented vocabularies rather than enum validation; absence from a comment alone does not prove a value is rejected.

Stable enclosure identity is `worktreeGroup`, rather than the changing process-node ID. This preserves selection/list identity across provisional-to-contract transitions. The process-map shell uses Motion layout when effects are enabled, but its current parent key is store generation; the overview must not imply that this map is keyed directly by enclosureKey.

The intended honest-motion rule is settled state under effects-off or reduced motion, with GSAP and Motion owning different properties and CSS providing static presentation. The timeline constructs no context while the effects gate is false, and visibility pauses its recorded tweens. These are scoped source predicates, not a claim that every possible animation or ticker in the application is absent. In particular, landing packet circles are rendered whenever their flow is active, while the GSAP hook remains effects-gated.

The historical alarm policy limits flicker to three flashes per second. Current timeline source specifies a terminal flash sequence followed by steady state and a single refused flash, alongside slower repeating scan/surge/breath/packet motion. This retains policy intent without claiming a fresh accessibility or mounted-motion acceptance result.

The landing order remains code-first, memory-after. However, the timeline and canvas do not enforce identical freshness predicates: canvas flow helpers require observed facts, while disposeFrontier accepts broader non-planned origin-feat facts and tests PR/memory states without an observed-fact check. Keep the shared-progression intent separate from this implementation difference. Likewise, the two carryover lines may be simultaneously active; “one cyan flow” is not a literal current guarantee.

Canvas recovery chips are descriptive labels, not operation buttons. The T7B specimen offers retry/abandon without disabled-memory choice, retaining the policy that memory cannot be disabled for an individual task. `resolveRecovery` itself does not filter such a choice from arbitrary served actions; this local observation does not establish whether upstream policy enforcement exists elsewhere.

The diagnostics responder is an exception to display-only action presentation. Its current owner records durable gate decisions and, for non-adapter interactions, posts an operator-inbox response. Adapter interactions use the durable decision as their response source and avoid a duplicate inbox message. The route passes lifecycle/gate data into this owner and places no responder inside the canvas. The old claim of only injecting instructions into hosted chat is too narrow for current ownership; backend effects and authorization are outside this bounded adjudication.

## Historical And Verification Limits

The inherited design history spans the state-backed slice 5e, lifecycle motion 5f, two-world/prototype presentation 5g, successful landing and ledger lookup 5h, scenario-stage construction/teardown 5i, property-ownership correction 05k, DrawSVG/MotionPath adoption 05n, and the 05o failure library. Preserve their enduring intent: honest fact-state rendering; stable provisional identity; source-node-anchored scans and block pointers painted above nodes; recoverable steady gates distinct from transient faults/reroutes and terminal all-or-nothing conflict; abandonment without landing; successful worktree retirement into the official line; readable labels; bounded ledger lookup; and separate motion owners. Their incremental delivery chronology does not establish current mounted parity.

The former eight-mode library comprised T3B memory/ledger block, T1B stale-base block, T7B provider-plan block, T9B seed fault, T9C reindex reroute, T12B live-memory sync, T14C integration conflict, and T18 abandon. T3B/T1B/T12B enclosure predicates, T14C integration specimens, and T18 teardown remain represented. T7B now reads as fleeting when its missing facts say the contract is unwritten. Provider dropout, seed flash/fault, reindex, gauges, clone arcs, structural petals/bezel palette, and official provider-engine wiring are historical visuals. Historical gold-bezel/petal and provider-slot-honesty policies should not be presented as current rendered obligations.

The inherited CUR-C02/T7B title-body closure is supported here only by the present assertion source agreeing on fleeting, retry/abandon, no disabled-memory choice, and no retired provider markers/gauges. Its producer receipt was not inspected. This is not a new mounted capture, e2e run, or full-suite PASS. The integration test title still mentions a bent replay path, while its body checks data-strategy and current renderer source deliberately draws straight paths.

The 260712-TRH-L7 stale-landing intent survives in explicit stale chip/PR text, hover age, and observed-only directional-flow predicates. The 260727-CHATS-IM-L2 sibling-SVG ownership survives with surge/attention rather than reindex. The historical L5I keep-alive rationale has changed: current Cockpit conditionally mounts EngineRoom only for the engine view, and comments describe retained pages without a dashboard entry. Visibility gates and memoized slice subscriptions remain, but this source does not support describing Engine Room as a currently hidden keep-alive cockpit layer or claiming near-zero measured hidden-view CPU.

L23 source-lineage diagnostics remain an optional strict projection rendered as state plus hover summary. No agent-consumption guard or stale-context prevention is established by that diagnostic row alone.

Named historical limits retained without fresh adjudication: the full-history ledger viewer was deferred as agents-remember#88; further steady-state Hangar/Engine Room CPU work was developer-deferred and described as non-blocking for the historical leaf; cleanup power-down presentation was documented against a pre-05m runtime; old all-eight parity, screenshot stability, visual-result-unchanged, test-covered, and delivery-closure claims are historical assertions. Their original mounted captures, receipts, prior source revisions, and acceptance runs were not examined. The inherited all-history Git-search claim about state='refused' was not repeated and supplies no fresh proof here.

This proposal is based only on present source and static assertion inspection at the stated head. No tests, product execution, network probes, sync, code repair, new invariant records, or publication were performed.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/engine-room/`              |

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): The server composer of the process nodes the client renders. [1]
- Retained reference account (no fresh execution or acceptance inferred): The served `EngineProcessNode` / `Analytics.engineProcesses` contract. [2]
- Retained reference account (no fresh execution or acceptance inferred): The honest-motion gate the GSAP/Motion read. [3]
- Retained reference account (no fresh execution or acceptance inferred): The cockpit shell that hides the rails for the Engine Room view (§4.1). [4]
- Retained reference account (no fresh execution or acceptance inferred): `EngineProcessEdge` (`extra="forbid"`) with the documented `kind` and `state` vocabularies the flash derives from. [5]
- Retained reference account (no fresh execution or acceptance inferred): "def _seed_edge_state(" and "_DECISIVE_SETUP_EDGE_STATES: dict[str" — the only producers of a seed lane's state, including the "metrics=_metrics(lifecycles" reroute. [6]
- Retained reference account (no fresh execution or acceptance inferred): The client mirror of the edge, which no longer declares a polarity field. [7]
- Retained reference account (no fresh execution or acceptance inferred): Route still owns enclosure visualization, model/types, branch/coupler/ledger, straight worktree/sync/integration conduit — source ownership, not executed visual proof. [8] [9] [10] [11] [12]

- Pure lifecycle join, stable group identity, no provider model fallback [13]
- Slice equality, memoized join, repository ledger selection, generation map key [14]
- Memory/materialisation/fleeting and movement predicates [15]
- Terminal, recovery, and landing predicates [16]
- Provider geometry absent; integration paths straight; polarity state-derived [17]
- Replay metadata without bent geometry; observed-only landing progression [18]
- Bounded ledger window and best-effort metadata [19]
- Preview, matching row, missing metadata, downward popover [20]
- Actual producer vocabulary and seed-state precedence [21]
- Extra fields forbidden, kind/state string fields, optional lineage [22]
- Timeline freshness differs from canvas; abandon/conflict dispositions [23]
- Source-lineage diagnostic and responder admission [24]
- Responder records decisions and uses inbox/adapter routing [25]
- Motion gate, scoped context pause and cleanup [26]
- Current sibling overlay contains surge and attention [27]
- EngineRoom conditionally mounted, contrary to inherited keep-alive account [28]
- T7B assertion source agrees with retirement and recovery policy [29]

- BranchTier mounts integration/source and worktree tiers plus a conditional middle landing tier, with branch labels from projected refs. [30]
