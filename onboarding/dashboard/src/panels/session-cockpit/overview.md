# dashboard/src/panels/session-cockpit/ — Session Cockpit Composition And Inherited Chats Intent

## Governing Overview
[panels overview](../overview.md)

## Purpose

This source family retains the rail/stage/inspector session cockpit and its structured conversation and history-library surfaces. Its purpose is to present shared session, conversation, delivery, lifecycle, and interaction evidence without becoming a second catalog, delivery ledger, or durable browser conversation database.

The present shell wiring must be distinguished from that inherited purpose: `dashboard/src/cockpit/Cockpit.tsx` mounts `RoleChatsPane` in its persistent Chats layer. `RoleChatsPane` composes the role launcher and, for an unbound selection, `PaseoChatFrame`. Chats remains the shell's default opening view, but the retained `sessions-view/SessionsView.tsx` is not the component selected by that examined shell layer. Its comment still calls it the canonical Chats cockpit; that comment does not override the composition expression.

The inherited FEUI-L8 consolidation retired the former `panels/Chats.tsx`, `SessionList.tsx`, and `data/sessionGroups.ts` product responsibilities into shell reconciliation, the session cockpit, `ChatContextBar`, and `railModel`. Preserve that duty-transfer intent and its historical attribution without claiming that the current shell still mounts `SessionsView`. The internal `data-view="sessions"` marker remains on the retained cockpit body. The former `RailChat.tsx` retirement under MIK-R95 rule 8 is historical; the current shell has its own role-chat composition.

Within the retained cockpit, controlled sessions default to a harness-neutral structured transcript. The previous-conversation library is a separate in-stage capability. A controlled PTY is a read-only diagnostic rather than the transcript renderer; an uncontrolled seat uses the legacy terminal body, labeled `legacy terminal · structured conversation unavailable`. The controlling predicate is a defined `controlState` other than `unsupported`, so undefined control state also takes the uncontrolled branch. Stage harness recognition includes Claude, Codex, Pi, and Eve.

## Hot Path Summary

1. Distinguish the product shell path from this retained composition: the shell's Chats layer selects `RoleChatsPane`; `SessionsView` delegates its own state/effects to `sessionsViewController` and rendering to `sessionsViewBody`.
2. In the retained cockpit, raw creation crosses `createSession`; `ChatContextBar` reports typed failures locally and emits only the accepted session id. Hosted creation crosses `openHostedSession` and the same underlying terminal opener. A valid open acknowledges exact caller-minted session, kind, harness identity, label, and running state before accepted-session handling.
3. Hosted settlement hydrates the shared catalog under captured catalog authority before focusing. An ambiguous outcome is watched by caller-minted id while the chooser remains open. Explicit dismissal ends that watch, so a later catalog row cannot steal focus through it. Ambiguity is not a proven server refusal or proof that no server session exists.
4. The controller separates focused inspection from live action/reload ownership, derives the task-document rail and attention rollup, and selects working evidence. Fresh live conversation status is preferred where available; catalog evidence remains a separate, potentially lagging source.
5. `ChatsStageBody` resolves submission authority, connects the structured projection, and switches presentation among conversation, library, and legacy terminal. Warm conversation projections are reused; cold or explicit-retry resolution refreshes authority. Per-session phases and generation checks prevent another session's resolve from painting the focused session.
6. Composer submission/withdrawal, adapter interaction answers, model/effort changes, lifecycle operations, cleanup, agent bus, and exact-turn interrupt retain their own authority routes. Palette, inspector, and live regions expose those results rather than inventing another operational truth.

## Construction And Ownership

`SessionsView` is now located under `sessions-view/`. It is a memoized wrapper around the controller and body. The body composes resizable rail, stage, and inspector panels; launch/palette overlays; cleanup notices; set-outcome notices; and mounted live regions. The inspector begins closed absent deliberate persisted opt-in. Responsive collapse is tracked separately from operator intent, and title-row controls reopen the rail or toggle the inspector. The inspector is supplementary evidence, not a prerequisite for core operation.

`ChatContextBar` owns raw launch feedback and the accepted-id callback. Hosted chooser state belongs to `LaunchFlow`, with one dialog-local catalog owner in `useHarnessCatalogRead`. Opening starts an abortable read; closing, superseding, or timeout revokes it. The timeout is five seconds. Ready, valid empty, timeout, and typed failures remain distinct; retry is explicit. A first non-null or changed serving boot identity supersedes discovery once. SSE connectivity loss is not itself this hook's discovery trigger. Preserve the inherited short/narrow-screen usability and visible `＋ Chat` entrance requirements as presentation intent, not a newly measured acceptance result.

Hosted launch selection uses an advertised complete model/effort pair or explicit vendor defaults with both knobs omitted. Model changes re-gate effort against that model's advertised launch-settable menu; native ordering and provider-qualified keys remain intact. Launch evidence distinguishes retained selection from readiness. Server-first leaf attach/move, old-row local lifecycle routing, and cross-tab catalog invalidation remain inherited duties of the context/actions layer.

`SessionRail` renders task-derived sprint/master/leaf grouping, completed folders, attention, termination confirmation, and landed cleanup; a separately selectable spawn-edge tree is provenance inspection. Current grouping admits only resolvable, altitude-valid document/role combinations and checks reviewer parent context. Masters not listed by a sprint can remain top-level masters. The unattached population includes missing/unresolved documents, invalid role/altitude placement, reviewer-context mismatches, and duplicate master-role occupants; it is not expressly legacy-only. Planned retirement rows are excluded, whereas bare termination remains crash evidence and landed sessions remain inspectable completion evidence.

Preserve the inherited goal of stable structural seat addresses across replacement, but do not describe it as established by these implementations: leaf and sprint seat populations are arrays of sessions, and rendered occupant rows use runtime session ids as keys and selectors. Master manager/reviewer slots select one occupant; additional occupants become unattached. Live labels remain single-line and ellipsized with full tooltip text. Runtime identity is therefore used for rendered row identity as well as focus/actions.

Rail optimization begins beyond 50 rows actually rendered in the selected hierarchy/tree mode, including the appropriate completed population. It applies browser `contentVisibility` containment rather than proving a measured fleet baseline. Inspector list virtualization begins beyond 100 rows and retains list cardinality. Historical dev scenarios cover fleet, failure, launch, submit, interaction, ended, PTY-drop, and stale-catalog situations; they are not a fresh execution receipt.

`ChatsStageBody` owns stage archetype selection, epoch acquisition, conversation DOM retention, and the persistent legacy PTY sibling. Cold resolution calls `readSubmissionAuthority(..., {refresh:true})`, avoiding a remembered cached epoch. Transport failures, unexpected throws, and typed failures with null HTTP status or status at least 500 retry with exponential delays starting at 250 ms and capped at one second, within a 30-second elapsed retry window. Other typed failures fail immediately. Successful authority read connects the projection and patches the session's `controlState` to `ready`; subsequent catalog hydration can confirm or replace it. Failure remains visible with explicit retry, and a later catalog transition to ready can re-drive resolution once per observed transition. The window bounds retry admission, not necessarily total wall time including an individual outstanding request.

Warm refocus touches the retained projection instead of re-reading authority. Focus changes release the prior conversation stream slot while preserving warm projection/cursor/DOM state. The conversation DOM pool follows the data layer's six-entry LRU limit; nonfocused entries that are no longer warm are pruned, along with their epoch-phase records. Scroll memory separates hidden retained geometry from whole-view geometry loss and restores intentional position.

The legacy PTY layer mounts lazily on first terminal focus, remains a sibling of the conversation pool, and remembers its last genuinely visible box to avoid hidden harness chrome resizing xterm. `PtySurface` keeps visited running/landed panes mounted while inspectable, prunes terminal tombstones, and makes landed panes read-only. A transient missing focus must not dispose unrelated visited terminals. Ended terminal presentation does not create an inspectable terminal/socket. The shared `Terminal` asks its current connection for a boot-owned reattach without an xterm remount. Preserve the inherited requirements that stale callbacks cannot demote a replacement connection and transport close cannot fabricate durable terminal exit; the examined component seam alone is not a whole-transport proof.

`TerminalDiagnosticsDrawer` keeps its closed section inert and aria-hidden, but conditionally mounts its read-only `PtySurface` only while open. Closing therefore removes that diagnostic PTY subtree. This differs from the persistent legacy-terminal sibling and should not be described as universal diagnostic xterm continuity. Hidden conversation/PTY pool wrappers use visibility styling and aria-hidden; they do not themselves apply `inert`. Preserve hidden-surface noninteraction as intent without claiming that every wrapper carries the attribute or inferring whole-call-path accessibility failure.

The conversation child route owns the harness-neutral feed grammar: server-ordinal articles, stable item identities, inline thinking, tool/diff/interaction/result presentation, evidence-bound telemetry, and labeled unknown vendor evidence. Required image labels are intended to render without image fetching; absent telemetry must not become reassuring zeroes. Live thinking coalesces into a stable active-turn row with completion cleanup. Native sub-agent history hydration is driven by visible, effective selected-agent focus. Roster identities derive from item evidence; remembered agent focus survives projection eviction but is validated against the rehydrated roster. ArrowLeft/ArrowRight cycle parent/agent lanes and Escape returns to parent; editable and interactive targets retain key ownership. Operator-driven visible focus changes receive polite announcements.

The library child route owns indexing, preview, and exact-open resume. Sub-agent conversations use the same selection/preview/open flow through their server-issued conversation keys, and `agentsNote` reports partial/unavailable agent history verbatim. New-row focus requires `openedForFocus` and an operation session id; unsuccessful or uncertain outcomes must preserve the current chat's draft, focus, and scroll rather than simulate an open.

`SessionComposer` owns reliable submission and authoritative withdrawal/pop-back, with `QueuePreview` inside the composer. Ambiguous delivery retains exact draft/request identity. Raw terminal-kind seats receive no dashboard composer in the current body. `InteractionBar` remains separate and is mounted only for a focused live row: parent singular pending interaction first, additive plural entries next, de-duplicated by interaction id. Entries without usable ids remain visible as unanswerable evidence. Agent labels come from adapter-bound payload evidence and are not fabricated. Answers use the exact session's direct interaction route even without a lifecycle. Structured questions collect all required answers together; scalar choices/free text use their appropriate response shape. Store-backed answering/error/answered states remain distinct, sibling bars do not inherit another interaction's status, and poll-bounded acknowledgement does not mean the agent has already proceeded.

Exact-turn interrupt belongs to `useConversationControls` and the `conversation.stop` command. The hook resolves turn identity from canonical status or item evidence, uses stable request identity for reconciliation, and distinguishes acknowledgement from settlement. It enables a working, resolvable turn unless capability is hard-unavailable or the current turn has a typed refusal; pending prevents another dispatch. It does not require capability state `supported`. Controlled-seat stop presentation now docks beside Send in `SessionComposer`; only terminal-kind seats receive the line-hosted interrupt in `WorkingLine`. The working slot prefers `ConversationWorkingLine` for a live harness conversation and otherwise uses catalog/cockpit cues.

`CommandPalette` and keyboard zones consume effective bindings. The `?` reference includes `Intent reviewer — while focus is inside it`, filtered from bindings whose zones include review, so rebinding appears in the reference. Preserve reviewer-local chord ownership, focus trapping/restoration, and immutable F6 region escape, including Vim composer mode. Mounted polite/assertive live-region roots, hydration batching, and keyed repeat announcements remain the inherited accessibility contract.

`SeatInspector` retains Evidence, Capabilities, and Bus panels behind hidden tabs; bus age-clock activity depends on visibility and the selected tab. `LandedCleanupNotice` sits outside the collapsed rail. Unavailable cleanup results retain exact intended targets and retry; partial results retain skipped reasons. Successful termination/retirement control-stop residuals are informational rather than false termination failures. Current stage composition removes stacked stop notices while retaining lifecycle details for inspection. Failed launch copy remains verbatim with retire/corrected-launch actions rather than silent automatic launch retry.

## Invariants And Boundaries

The inherited one-roof intent is one full-page Chats destination, one browser terminal-open authority, adapter-owned harness differences, reconstructable transcript/history projections, and no second durable browser catalog or delivery ledger. The current shell's persistent RoleChats layer and this retained SessionsView composition must not be conflated.

No rejected open may fabricate a local accepted row, readiness, focus, or dependent delivery. An ambiguous POST may later acquire authoritative catalog evidence; that does not weaken refusal handling or permit success reconstructed from request fields. Operator text, reliable submission/withdrawal, interaction answers, lifecycle gates, agent bus, and control commands must not silently cross channels or fall back to shared paste.

Focused inspection and live action/reload preference remain separate. Current body predicates withhold working/composer/interaction slots from nonrunning focused rows. Landed PTYs remain read-only until cleanup. Do not generalize that body predicate into proof of every structured control's call-path guard.

The no-durable-conversation-database boundary concerns conversation data. Hide-thinking is the persisted conversation presentation preference; agent focus and scroll memory are retained UI state, and the wider cockpit also persists layout/inspector intent, keymap, and active-session preference. Thus hide-thinking is not the cockpit's only persisted UI bit.

Preserve the FB7 terminal grammar intent: shared `well` color `#070b0f`, gutter glyphs `●`/`✻`/`·`, lowercase phase words, left-rule washes, and line-grid rhythm instead of boxed uppercase phase chips and per-article hairlines. Preserve collapse-or-explain chrome, nonalarming zeroes, humanized durations through `format.humanizeDuration`, and short identity display through `format.shortId` with full-value disclosure. StatusLine and rail-bus footer retirement move actions to the title and working feedback toward the conversation/composer.

RV-2's inherited whole-action-group wrapping requirement differs from current source: both `rowShell` and `rowActionGroup` set `flexWrap: nowrap`. Titles still absorb available width and ellipsize. Do not reassert the historical width acceptance as current measured behavior. RV-1 retains its load-bearing word-break warning: the WebTUI base cascade historically defeated component overflow-wrap patches; `index.css` contains the unlayered root `word-break: normal` remedy and raw identifiers may explicitly break. Computed browser values, not source inspection alone, decide whether the cascade works in a rendered build.

## Historical And Verification Limits

All prose in the input card was examined. This proposal is source adjudication at the named checkout, not test execution, visual acceptance, runtime verification, delivery certification, or a new lifecycle status. Original numbered reference identities, targets, maps, and excluded metadata remain parent-owned.

FEUI-L8 duty transfer, FEUI-L9R chooser/terminal continuity, FEUI-MX-FIX-2 accepted-row focus, CHATS-L4 one-roof realization, L5I keep-warm state, CHATS-IM-L2 selected-agent acquisition, and CHATS-L5P `PASS-WITH-NOTES` are inherited historical claims. Their old reviewer/task/history-pack witnesses were not re-established here. Preserve their responsibilities and exceptions; do not turn their chronology or delivery labels into fresh acceptance.

Named historical limits remain explicit: review R1 F9 reported that the session palette's key-reference page was inaccessible during reviewer takeover and left that condition as ruled; present shell replacement means the old observation cannot automatically establish today's reviewer path. L3.5 described stale L1 interrupt capability evidence and attempt-and-reflect rather than a clean proactive capability GET/refresh gate. Current interrupt predicates still permit non-hard-unavailable evidence, but this browser hook is not proof that no server capability route exists. The L5-Facing Register's measured virtualization/scale baseline and environmental faults E1/E2 remain named historical hardening limits; their old witnesses were not examined or discharged.

EFA-L4's inherited fixture rule is that cockpit suites should use `test/fixtures/wire.ts` and `conversationWire.ts` builders rather than authoring or casting wire nodes. Its seven-suite migration removed impossible required-capability and partial-analytics payloads, restored the four capability groups (`live`, `history`, `controls`, `telemetry`), populated analytics defaults described then as thirteen keys, and derived page `totalItems`. Those counts describe the old migration, not present schema completeness or passing cases.

The historical LaunchFlow proof narrowed: removing undeclared `control: starting` fields made surviving `not.toContain("adapter starting")` assertions unable to prove suppression of that stale field. The inherited replacement was a typed `HarnessInfo[]` literal plus explicit row-key checks, not restored rendering coverage. Current `HarnessInfo` still lacks the mirror-discovery header. The guard documents first-line `TypeScript mirror of` or `Browser mirror of` discovery plus `src/types/`, and names unmarked `harnessCatalog.ts`, `submissionLifecycleClient.ts`, `changeset.ts`, `files.ts`, and `notes.ts` as a blind spot. Its source also explicitly documents expression-kind gaps, generic helpers, predicates/assertion functions, and value-level gaps; a nominally discovered vocabulary is not comprehensive payload validity.

Keep the inherited three-link verification limit: hand-maintained fixture builders versus TypeScript mirrors, mirrors versus hand-maintained `snapshot.json`, and the unestablished `snapshot.json` ↔ `observer/projection.py` link. Historical contract checks measured mirror ⊇ served, served ⊇ mirror, and fixture ⊇ mirror plus runtime string vocabularies; they were not merely one-way subset checks. Neither a repository-wide absence of generators nor automatic Python-to-snapshot synchronization was established by this bounded source review. The old claim that the third link was held by nothing remains a named historical limit, not a newly proven universal absence.

EFA-L23 and DAG teardown claims concern shared fake-timer/scroll-geometry support and flushing the virtualizer's 150 ms debounce before jsdom teardown; they do not change product behavior or establish today's passing suite. Historical live-thinking acceptance pins and source-size rails likewise remain historical evidence.

The input's statements that no Domain Documentation source or cross-repository governing implementation was configured were not revalidated against memory settings. Toad/T3 and Claude/Codex TUI references remain historical visual-design derivations, not imported implementation authorities. No external documentation, product tools, tests, network calls, sync, or publication occurred in this adjudication.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

> **Retained hosted-session implementation and development history, not the current full-page Chats owner.** CockpitShell now mounts the native [RoleChatsPane](../../cockpit/RoleChats.tsx.md) / Paseo frame. The session-cockpit, structured transcript and in-stage library contracts below describe the retained legacy composition only; they do not transfer chat navigation or visual ownership from the native host.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/session-cockpit/`          |

| Responsibility | File onboarding |
| --- | --- |
| Full-route composition | [SessionsView.tsx](SessionsView.tsx.md) |
| Structured stage body composition | [ChatsStageBody.tsx](ChatsStageBody.tsx.md) |
| Structured renderer grammar | [conversation/ overview](conversation/overview.md) |
| In-stage history browser | [conversation-library/ overview](conversation-library/overview.md) |
| Rail and product-duty bar | [SessionRail.tsx](SessionRail.tsx.md) · [ChatContextBar.tsx](ChatContextBar.tsx.md) |
| PTY (diagnostics/legacy-raw) and ended presentation | [PtySurface.tsx](PtySurface.tsx.md) · [EndedSessionState.tsx](EndedSessionState.tsx.md) |
| Cleanup/lifecycle copy | [LandedCleanupNotice.tsx](LandedCleanupNotice.tsx.md) · [lifecycleCopy.ts](lifecycleCopy.ts.md) |
| Palette and keyboard binding | [CommandPalette.tsx](CommandPalette.tsx.md) · [useKeyboardZones.ts](useKeyboardZones.ts.md) |
| Launch chooser and request ownership | [LaunchFlow.tsx](LaunchFlow.tsx.md) · [useHarnessCatalogRead.ts](useHarnessCatalogRead.ts.md) |

## Evidence
- Retained reference account (no fresh execution or acceptance inferred): The reviewer's group on the keys page. [1]
- Retained reference account (no fresh execution or acceptance inferred): Full-route composition and shell ownership. [2]
- Retained reference account (no fresh execution or acceptance inferred): Legacy duty bar. [3]
- Retained reference account (no fresh execution or acceptance inferred): Structural role rail and data derivation. [4]
- Retained reference account (no fresh execution or acceptance inferred): PTY/ended continuity. [5]
- Retained reference account (no fresh execution or acceptance inferred): Cleanup authority notice. [6]
- Retained reference account (no fresh execution or acceptance inferred): Effective keyboard contract. [7]
- Retained reference account (no fresh execution or acceptance inferred): Dev end-to-end scenario authority. [8]
- Retained reference account (no fresh execution or acceptance inferred): The shared builders every cockpit suite seeds wire nodes from (projection side and conversation side). [9]
- Retained reference account (no fresh execution or acceptance inferred): The cast guard, its first-line mirror-marker discovery rule, and its own list of unmarked blind-spot modules. [10]
- Retained reference account (no fresh execution or acceptance inferred): The launch chooser's catalog types and the server model they mirror (`HarnessInfo` ↔ `DetectedHarness`). [11]

- The examined product Chats layer mounts RoleChatsPane, not the retained SessionsView composition. [12]
- RoleChatsPane renders RoleLauncher and an unbound Paseo frame; default selection is architect. [13]
- Retained SessionsView delegates controller and body rather than owning all composition directly. [14]
- Cold epoch resolution refreshes authority, retries transient failures within a 30-second elapsed window, and can recover on a ready transition. [15]
- Controlled classification requires defined non-unsupported control state. [16]
- Conversation retention follows the shared LRU; lazy terminal sibling survives archetype switches. [17]
- Closed diagnostics are inert/aria-hidden and have no PtySurface child; pool wrappers use aria-hidden without their own inert attribute. [18]
- Live-only body slots and composer-docked stop differ from the old universal WorkingLine placement. [19]
- Interrupt enables working resolvable turns unless hard-unavailable or refused, rather than requiring supported capability. [20]
- Ambiguous hosted opens reconcile by observed id only while the dialog remains open. [21]
- Unattached rows include structural mismatches and duplicate master-role occupants; leaf occupants are session arrays. [22]
- Occupant row identity uses session ids, and current row/action layout does not wrap. [23]
- Fleet optimization counts actually rendered rows in the selected tree/hierarchy. [24]
- Agent focus is roster-validated and native history acquisition requires visible selected-agent focus. [25]
- Library focus uses exact openedForFocus evidence and operation session identity. [26]
- Fixture vocabulary guard explicitly documents discovery and coverage limits. [27]
