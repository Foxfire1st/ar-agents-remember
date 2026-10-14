# dashboard/src/data/ — Cockpit State And Authority Overview

## Governing Overview
[dashboard/src overview](../overview.md)

## Purpose

This route owns browser projections and the authority boundaries consumed by the dashboard. It normalizes terminal catalogue rows, retains session and per-seat cockpit state, reconciles server facts, coordinates launch, set, submit and lifecycle operations, and supplies derivations for task navigation, rail placement, commands, attention and visual state. Components render these facts; the enduring architectural intent is that they do not invent a second catalogue, delivery ledger, lifecycle authority or durable conversation database.

Read clients also belong here even when they retain no global state. Review, change-set, requirement and Knowledge adapters carry the server's question, identity, answer and refusal vocabulary to their consumers. Their TypeScript mirrors are not general runtime schema decoders: transport acceptance and each caller's admitted answer states must be distinguished from complete payload validation.

This overview governs the data plane beneath dashboard/src. The keymap, active-conversation and conversation-library directories have their own child overviews. Chats UI composition belongs to session-cockpit; review and Knowledge rendering belongs to their panel routes. The inherited placement decision keeps dev cockpit scenarios under the root overview because they are bounded fixture/transport seams rather than another product architecture. Legacy sessionGroups ownership was retired in favor of rail derivation and canonical Chats rendering; that historical placement decision does not establish the current details of every consumer.

## Hot Path Summary

1. terminalOpen.ts sends the identity-addressed POST to /api/terminal/<sessionId>. It classifies network, HTTP, protocol and server outcomes, checks the acknowledged session and kind, rejects contradictory harness/control claims for raw terminals, and requires an accepted row's label and running status.
2. sessions.ts materializes createSession only after that opener returns an accepted server row, then broadcasts the catalogue change. Catalogue hydration reconciles browser rows with server evidence. Inspection focus and the live action target are separate concerns.
3. The dashboard and per-seat stores supply rail, stage, inspector, composer, status and attention projections. taskIdentity.ts derives repository-qualified references from real projected task documents; railModel.ts places seats through those references and task containment rather than treating leaf display keys as hosted-seat addresses.
4. Submit, adapter answer, set, task assignment, terminate, cleanup and withdrawal use their dedicated server authority routes. Ambiguous delivery retains identity and operator text rather than authorizing a blind resend or a local-only withdrawal.
5. Review entry counts come from reviewIntentSummary.ts. Opening the reviewer loads its subject catalogue and review payload. A payload's review:trees:<n> limitation identifies the tree comparison for supplementary tree and lane reads; consumers that have no comparison disable those reads.
6. Knowledge navigation is addressed by #knowledge hashes. Reader calls carry the selected repository, memory selection and subject; typed refusal states remain answers rather than becoming empty views.
7. Catalogue invalidations and development scenario generation changes control ownership of asynchronous results. A retired request or scenario must not overwrite the successor surface.

## Construction And Ownership

`useTaskDocumentBody` hydrates longer/full body content by path and body revision without replacing
current summary identity, status, progress or review aggregates. A matching body revision can restore
body previews/full collections, while a changed-summary mismatch retains its current facts. First body
loading settles before the page's ancillary Notes/report/counter requests mount; this is page scheduling,
not a second transport owner. `taskReports.ts` still lists recorded starts in one bounded request;
the relocated page passes each reader target the path inside the task root rather than its physical
projected file path. None of these display changes grants canonical task or report write authority.

The review wire mirror transports recorded meaning steps with their own attempts/revisions and distinguishes readable none from unavailable. Subject answers and catalogue outline rows carry these facts through their existing routes; a browser-missing current field is a failure, not a default. Transport, paging and store owners remain independent.

### Sessions, catalogue and transport

sessions.ts owns OpenSession, the registry, activeId, attachment patches, connection registries and cross-tab catalogue notifications. createSession generates the requested identity and label, delegates opening to terminalOpen.ts, and leaves the registry unchanged on a failed result. terminal.ts supplies terminal transport and structural assignment; launchFlow.ts participates in the shared open flow. The inherited sole-open-authority intent belongs to terminalOpen.ts, not to locally reconstructed acceptance in each launch caller.

The opener's concrete identity checks cover session id, terminal kind and the requested harness. Raw terminal responses may carry neither a non-null harness nor a non-null controlState. Other accepted row fields are normalized from the server response; the phrase 'exact requested identity' must not be expanded into an assertion that every optional request field is compared byte-for-byte.

catalogPoll.ts owns catalogue reading and reconciliation, including refcounted polling and eager/cross-tab reconciliation. The inherited shell-lifetime policy calls for one driver and reconciler rather than timers introduced by view remounts. preferLiveSession restricts the action route to a running row, while focusedSessionId may retain a landed or ended row for inspection. Successful remote termination is removed locally and excluded from its confirming read so a stale catalogue echo does not resurrect it. Equal catalogue content preserves existing row/state identity; changed authoritative content must replace a differing local pre-apply.

Terminal WebSocket loss is separate from durable terminal exit. terminal.ts recognizes an explicit server exit control frame; losing a socket alone does not mean the session ended. Reattachment consumes a serving boot identity once, guards superseded socket callbacks and replays resize before buffered input. This recovery is boot-owned rather than a periodic reconnect loop.

buildIdentity.ts owns the executing bundle fingerprint and comparison with the optional server dashboard build identity; the pure comparison does not reload the page. harnessCatalog.ts validates the narrow pre-session id/name/detected envelope and distinguishes ready, valid-empty, network, HTTP and protocol outcomes. Signal-less boot reads share an in-flight request and have a 10-second request bound. Caller-signalled reads retain separate ownership; dialog cancellation and retry are caller concerns. fetchWithTimeout.ts bounds hung requests and inflight.ts owns per-key sharing only until settlement, with identity-safe slot removal rather than a persistent result cache.

### Cockpit state, attention and lifecycle

sessionCockpitStore.ts owns ephemeral per-seat UI evidence, drafts, queues, focus, poll health and layout intent. The inherited inspector default is closed; responsive geometry must not overwrite deliberate operator intent. Exited, retired and landed rows are catalogue evidence rather than live PTYs, and remain inspectable until authoritative cleanup removes them.

liveTurnWorking is a fresher conversation-projection signal merged for the focused view, not a catalogue field written into the registry. stateGrammar.ts considers landed, terminated, exited, failed-control, human-blocked and waiting guards before using that signal. It therefore cannot override an actual end, fault or wait with apparent liveness. sessionHasPendingInteraction combines the singular parent-thread slot with the non-empty plural sub-agent slots. Attention, announcements and rail question triage must preserve that combined meaning so a seat blocked solely on a sub-agent approval remains visible.

announcer.ts supplies shared polite/assertive announcements. The inherited accessibility intent batches urgent transitions from one hydration, preventing synchronous seat changes from replacing one another before observation, and suppresses redundant focused-seat prompts using pending-interaction evidence.

sessionLifecycle.ts retains terminate outcomes, focus-independent stop residuals and landed-cleanup outcomes. A successful termination can retain an informational control-stop residual without becoming a failure. Cleanup without an authoritative answer retains the exact id/label target snapshot in cleanupFailure for visible retry; partial success preserves both closed rows and skipped rows with their reasons.

### Submission, withdrawal and controls

submitClient.ts is the whole-message submission driver over the shared per-seat store. It carries immutable request identity and text, distinguishes accepted, queued, rejected and unsupported outcomes, reconciles uncertain results and announces focused-seat receipts. A browser fetch rejection is ambiguous: automatic resend is authorized only by explicit pre-dispatch evidence, using the same request id and immutable text, not by guessing from HTTP status or error wording.

submissionLifecycleClient.ts owns authoritative submission lookup, polling, epoch handling and lifecycle observation. submissionWithdrawal.ts owns withdrawal targeting and orchestration over that transport and evidence. Withdrawal resolves the queued request and sends its expected bridge epoch; it is not a local queue deletion. Only authoritative withdrawn evidence allows the corresponding local projection. Recovery preserves newer drafts and withdrawn text rather than silently overwriting either. A queued receipt proves acceptance, not that dispatch has not begun; authoritative lifecycle facts determine withdrawability. Dispatching or unknown outcomes wait for a terminal result under the bounded reconciliation policy, retaining endgame/recovery evidence when convergence is uncertain.

Queue rows, submit history, withdrawal recovery, composer drafts and notices are projections of the same per-seat state. Failure or ambiguity must not discard the operator's draft or move the active route. Operator text, agent-bus messages, lifecycle controls and adapter answers remain separate authority channels.

capabilityCatalog.ts, sessionCapabilities.ts, setClient.ts and launch/set helpers separate pre-session discovery from exact-session control truth and preserve pending, clamped and refused evidence. The inherited adapter-answer rule uses direct exact-session routes with bridge-epoch evidence: structured questions send an all-or-nothing answers map, while permission, arbitrary-choice and composer modes send a response string. Lifecycle gates do not transport adapter answers. The keymap child owns effective bindings, browser-reserved rejection, the immutable F6 focus escape and Emacs/Vim composer profiles.

### Task identity, hierarchy and artifacts

taskIdentity.ts derives a canonical repository/path reference only from a projected task document with a repository and a recognized tasks/<repository>/ path ending in .json. sessions.ts stores task-document and role binding separately from runtime lifecycle correlation. railModel.ts uses document references, task containment and role eligibility to place sprint, master and leaf seats; reviewers additionally require the corresponding parent match. Missing, unresolved or ineligible bindings are detached rather than fabricated into a task hierarchy. Landed rows have completed placements. Diagnostic spawn ancestry remains a separate model.

The older TES-L6 repository+sprint provenance account is historical. Present rail placement is document-based: sprint orchestration documents, master documents and their leaf containment are the deciding owners. Historical unbound rows remain relevant migration context, but the current unattached collections must not be described as exclusively historical migration buckets.

taskHierarchy.ts keeps SeriesSubTaskNode separate from TaskSubTaskRefNode. ParentTaskMatch.ref is a series row because it is read from series.subTasks. orderedByCreation sorts only when every row has a truthy createdAt; otherwise it returns authored order. Rows whose model has no creation timestamp are not made sortable by borrowing another model's fields. The inherited server-first ordering policy makes this browser helper a preservation boundary rather than a new ordering authority.

requirements.ts lists and reads requirement documents using repo/master/document context, and resolves reserved requirements/ addresses against the registered listing. Its low-level readRequirement also accepts and forwards a path argument; this client alone does not prove arbitrary-path rejection. Registered-document admission is a server/consumer contract that must be checked at those owners before asserting complete enforcement. Requirement rendering must retain the backing document identity rather than grant authority to arbitrary Markdown links.

taskArtifacts.ts discriminates notes, requirements, task-report and decisions targets. Notes may address a folder or note; requirements retain document plus path; reports retain role/request and task identity; decisions retain their supplied projected content and identity. The shared reader target is broader than the historical two-way notes/requirements union.

### Reconstructable conversations

conversation/ owns the active-conversation projection: its pure reducer applies cursor-ordered events, deduplicates eventId/cursor evidence, gates block deltas by revision, requests re-page on retained gaps, resets on conflicting payloads at the same revision and rehydrates from replacement pages. It creates no optimistic durable item. The store coordinates page, stream, recovery and bounded retention/LRU over server/native authority.

conversation-library/ owns paged historical lists, previews and exact-open tracking. It does not mark a conversation active itself. Focus is permitted only by opened operation/catalogue proof, with a caller-stable requestId used for reconciliation. The inherited R1 boundary is reconstructability: reload and server pages/events rebuild these projections, with no durable browser conversation index. The hide-thinking preference is the inherited persisted UI exception. Controlled sessions use the structured conversation surface; runner line logs belong to the default-off read-only diagnostics drawer and legacy raw body, rather than becoming a duplicate vendor TUI history authority.

conversation/agents.ts recognizes roster items by backend identity prefixes plus notice/system/agent predicates. Other agent-tagged notices, including selected-child history state, remain timeline items and do not mint duplicate seats. Terminal agent statuses alone authorize final-message previews.

streamLiveness.ts supplies a visible-tab watchdog for state/conversation EventSource channels. Timer suspension is positive sleep/freeze evidence; ordinary silence spends at most one quiet resubscribe per episode of observed life. Hidden tabs are exempt from judgment, and handshake traffic must not re-arm the silence backstop into a repeating loop. Failed replacement subscriptions follow the ordinary error path instead of preserving a false live cue.

### Review and change-set readers

review.ts is the public read-only Intent Reviewer client. It mutates no dashboard store and carries omitted fields as omitted rather than fabricating attribution or an identity. intentReview asks canonical task context and optionally a recorded invariant/family subject; without a selector it asks the task's source inventory. The browser does not choose the comparison dataset by a filesystem path. intentReviewEntries asks task context alone and supplies recorded selector identities with before-only, after-only or both presence and labelled catalogue totals. Its refusal is a normal typed outcome; it does not remove reachability of an admitted task-context review.

reviewTransport.ts is the shared review decoder used by intent, entries, source-content, trees, lanes and intent-summary reads. It makes one GET, reads JSON regardless of HTTP status and accepts a body with a string state. This is shallow transport recognition, not proof that the complete body satisfies its TypeScript type. Callers admit their own states and required fields. A typed refusal retains code, reason, offending input and next action. The closed failure tokens are not-initialized, unavailable-history, validation, authority, not-found, domain-refused, network and unreadable; unknown non-empty codes remain domain-refused with their code unchanged. reviewer_busy and inputs_changing map to unavailable-history. Loading and known-empty are not failures. Intent-only refusal classification may support a separately requested source inventory, never an automatic substitute chosen by this client. files.ts retains the non-2xx throwing semantics of its separate getJson.

Review source inventory preserves exact textual paths, non-UTF-8 path bytes, changed status, mode change, content classification, partialness, generation trees and reasons. Measured-empty, unavailable and partial are distinct meanings. Source expansion echoes the inventory's before/after code tree IDs and exact path; it does not resolve a replacement generation. It carries present, absent, binary, symlink, submodule or unavailable sides; optional text is the mirrored server contract, not a runtime type guarantee. currentness separates current, superseded and unmeasured. path_bound names requested_generation or leaf_change_set; admission distinguishes changed entries from attributed_unchanged realization context. Unchanged context never becomes an inventory changed-file count.

Review pagination echoes opaque server cursors without constructing or parsing them. The present collection union is knowledge | family_members; only knowledge is cursor-less walkable. family_members continues a specific family's roster cursor. records was retired with the review matrix and is no longer an offered page, although its refusal codes can still be decoded. carriedPage normalizes omitted and null page values; requested-page refusal remains separate from an empty page. continuationOf offers a next action only when a cursor and positive remainder exist. Page totals retain selection versus walk basis, scope and server counts; reset wording uses the refusal code so a foreign cursor is not called a moved comparison.

history admits only recorded and is omitted for live reads. previousBindingDigest names the identity being replaced, never the identity to substitute for the current candidate. reviewQuery declares its wire spelling once. Its empty-string normalization specifically covers that refresh digest; selectors, history and continuation have their own presence checks, not a universal empty-string filter.

reviewFamily.ts carries revision selection, authored guarantees, bounded roster pages, member occurrence identities and source references. Locator kind, resolved ranges, locator state, role and rationale travel as supplied facts; unresolved locators never gain guessed ranges. review.ts re-exports the locator vocabulary. Tree-only change_kinds carries intent/implementation/membership facts, proof, text_differs, range_unresolved, server-derived primary/marks and separate evidence, unknown and membership reasons. The five change types are imported directly from reviewFamily.ts rather than through review.ts. Renderers may order and count these facts, not recompute their classification. Absence of family_context is distinct from a measured no_family_recorded result; applicability labels likewise remain optional, with absence meaning no supplied label. Displayed treatments are direct, historical, candidate and unresolved; labelled context preserves the true other subject without importing its judgment into this review.

reviewTrees.ts carries the four code/memory trees and pinning refs, knowledge and index degradation, reopened code-side state, memory diff grouped by record/source, currentness, worklist/history linkage and realization/proof entries on both code sides. Its vocabulary is snake_case. Requests address live, recorded or numbered comparisons and optionally invariants, not arbitrary paths/tree IDs. Trees, not-converted and refused are distinct answers. Hooks abort superseded reads; the leaf-wide hook also uses sequence guards and retries only reviewer_busy/inputs_changing, up to seven retries after the initial read with delays 1500, 2000, 3000, 4000, 5000, 6000 and 8000 ms. Loading remains until the final outcome, and abort ends the wait. Claims that the server stops work on disconnect require server-path evidence beyond the client abort itself.

reviewLane.ts carries server classification of measured paths and hunks without recomputation. File buckets are attributed, unexplained or attribution_unknown; hunk linkage is range intersection, not coverage. Unknown knowledge/range reasons stay explicit. The two destinations open comparison-bound change-set pages filtered by the held lane answer, separating unexplained changes from unknown attribution while retaining distinct file and hunk facts. Missing requested values are unavailable rather than an empty lane. Hooks retain answers with their URLs and suppress superseded results. readFileClassification supplies the same per-file answer as a promise, converting thrown errors into unavailable; intentMarkerScope.ts retains answers per surface/path and makes no request without a tree comparison.

reviewIntentSummary.ts is the entry's summary read, not a catalogue-size or line-total derivation. Counted, partial and unavailable remain distinct, with unavailable carrying refusal rather than zero counts. Tree attribution counts travel in the same answer on counted/partial and refused states, never through a more eager entry read. Task-local facts and revalidation generation govern refresh; unrelated workspace publications do not constitute a new task answer. intentEntryRevalidation.tsx uses local context state for re-show and reviewer refresh, with a no-provider generation-zero/no-op behavior.

useReviewCatalogue.ts keys answers by task/record and generation and rejects superseded responses. A generation reread quarantines prior entries and outline; catalogueForComparison also suppresses incompatible semantic fields synchronously. The observed generation includes code trees and known knowledge snapshots. Its current request calls intentReviewEntries with repo/master/leaf only: history and generation affect the hook key, not the wire request. Missing entries/totals in an entries body are defaulted or derived locally, so the implementation is more permissive than an unqualified claim that complete recorded counts are always preserved.

changeset.ts carries task/leaf recordedness and verbatim stateDetail, preserving unrecorded versus measured empty. comparisonChangeset and comparisonFileDiff additionally address a recorded review comparison by number, without substituting a live or committed leaf range. Master net reads carry optional generation pins, published generation identity, currentness and integrated scope; master file expansion threads the same pins rather than re-resolving a newer tip. Its own decoder reads refusal bodies regardless of status, accepts non-null JSON on success, and throws ReviewTransportError carrying named failure facts otherwise. This is not full runtime validation of a successful change-set. The inherited rendering rule withholds +0 −0 for unrecorded ranges and distinguishes loading, refusal and answered counts; fresh rendered verification was not performed here.

### Projection stability, fixtures and development boundaries

servedAges.ts mirrors the server volatile-age set, including elapsedSeconds. Stable equality ignores those keys while retaining structural content and arrival anchors; display ages advance from served evidence rather than creating structural changes from render clocks.

The inherited fixture policy links generated types/projection.ts to the producer schema and requires wire builders, the manual snapshot sample, contract coverage and fixture opt-out guards to respect that mirror. wire.ts and snapshot.json remain hand-maintained artifacts; generation does not make their coverage automatic. The historical all-vocabulary sample and servedProjection parameter checks address fixtures that previously used casts to conceal invalid/missing fields. These are policy and historical protection claims, not executed acceptance here.

Development scenarios replace transport rather than weaken production acceptance. The inherited generation policy revokes unresolved catalogue, capability, snapshot, submission, withdrawal and connection ownership before successor fixtures are seeded. dashboardStore.reset() performs one transaction, increments gen once and clears scenario-owned projections including closeoutQueues. ScenarioPlayer calls that seam. Such reset exports are development authority seams, not ordinary production recovery APIs.

selectors.ts retains engineState/groupEngines definitions. driftSegments consumes projected reporting counts, orders recognized classifications and appends unanticipated classifications; it does not establish exposure of a drift_check tool. Retained provider-shaped data or selectors do not restore the removed EngineRoom provider consumer or its visuals.

## Invariants And Boundaries

Server catalogue, bridge, task and knowledge contracts remain the authorities; browser stores and read clients are projections. Accepted session creation, live-action selection, recorded task binding, request identity, expected epoch and exact generation must remain attached to the operation they authorize. Inspection, display helpers and local caches must not acquire mutation authority.

Missing, unreadable, unrecorded, unavailable, partial, unknown, refused, not-compared and measured-empty are different facts. Optional fields must retain their actual contract meaning; TypeScript declarations and source comments alone do not enforce every semantic predicate at runtime. Review transport recognizes a state-bearing body shallowly, change-set transport recognizes successful JSON shallowly, and requirement path admission needs its server/consumer owner. No whole-call-path guard absence is inferred from a local adapter lacking validation.

Conversation pages/events are reconstructable evidence, not durable optimistic browser history. Ambiguous submission must preserve drafts and reconcile identity; withdrawal must obtain authoritative evidence. Pending plural interactions, ended/fault/wait state precedence, cleanup residuals, cursor ownership and unavailable historical trees must not be collapsed into convenient defaults.

## Historical And Verification Limits

This proposal read all 59,089 characters of the input card and confirmed its supplied SHA256. The examined checkout HEAD is 8d2e754789e30f0d3be10fdd33f83cf6fe367141. It is source adjudication only: no tests, mounted captures, delivery runs or publication were performed.

The card's ICR-L3 direct-fetch exception is superseded by the shared review transport. Its early ICR-L22 entry-refusal/no-button account is superseded by reachable task-context review and summary-owned entry counts. ICR-L13's R12/R24 swallowed-refusal debt is historical; the present change-set decoder carries refusal reasons. TES-L6 sprint provenance remains historical context alongside the present document-based rail. ICR-L10's two-collection account predates retirement of records; only knowledge and family_members remain. ICR-L44's 'no rendering reads the new fields yet' is a dated limit, not a present renderer verdict.

Named historical witnesses not re-established here include the 2026-09-30 Q1/Q2/Q6/F1 rulings, ICR/MIK requirement and task/reviewer records, the recovered same-repository history pack, the earlier six-suite/seven-suite fixture conversion, the snapshot growth from two to six lifecycles, historical module line counts and browser-console-zero criterion. The parent preserves their original references. Their historical test and delivery language is not fresh acceptance, and inaccessible old witnesses remain named rather than silently promoted to current proof.

The parent read the memory-root system/sources.md: it says 'No entries configured yet.' No configured Domain Documentation source supplies a competing account here. The inherited no-applicable-cross-repository-source statement likewise remains historical provenance, not a fresh repository-wide dependency audit. Retained selector definitions and provider-shaped fixtures prove neither restored provider visuals nor exposed tools. Client aborts prove request cancellation intent, not server computation shutdown without server witnesses.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/`                            |

| Responsibility | File onboarding |
| --- | --- |
| Catalog and session registry | [catalogPoll.ts](catalogPoll.ts.md) · [sessions.ts](sessions.ts.md) |
| Cockpit state and announcements | [sessionCockpitStore.ts](sessionCockpitStore.ts.md) · [announcer.ts](announcer.ts.md) |
| Lifecycle and cleanup | [sessionLifecycle.ts](sessionLifecycle.ts.md) |
| Reliable submit and withdrawal | [submitClient.ts](submitClient.ts.md) · [submissionLifecycleClient.ts](submissionLifecycleClient.ts.md) |
| Control/capability truth | [capabilityCatalog.ts](capabilityCatalog.ts.md) · [setClient.ts](setClient.ts.md) |
| Role/spawn rail derivation | [railModel.ts](railModel.ts.md) |
| Runtime bundle identity | [buildIdentity.ts](buildIdentity.ts.md) |
| Bounded boot transport and single-flight ownership | [fetchWithTimeout.ts](fetchWithTimeout.ts.md) · [inflight.ts](inflight.ts.md) |
| Strict pre-session harness discovery | [harnessCatalog.ts](harnessCatalog.ts.md) |
| Authoritative terminal open | [terminalOpen.ts](terminalOpen.ts.md) · [terminal.ts](terminal.ts.md) · [sessions.ts](sessions.ts.md) · [launchFlow.ts](launchFlow.ts.md) |
| Durable terminal transport | [terminal.ts](terminal.ts.md) · [terminal.test.ts](terminal.test.ts.md) |
| Stream liveness and visible-tab wake policy | [streamLiveness.ts](streamLiveness.ts.md) · [screenWakeLock.ts](screenWakeLock.ts.md) |
| Review client family mirror | [reviewFamily.ts](reviewFamily.ts.md) |

## Grant mutation adapter

directExecutionGrant.ts posts Give/Revoke to the developer endpoint and preserves typed refusal. The adapter shapes transport only; product grant and ordinary-start authority remain server-owned.

## Evidence
- The mirrored change types and the entry's optional facts. [1]
- One file's classification as a single read; a transport failure is `unavailable`. [2]
- The scope that keeps it per surface, only for a tree comparison. [3]
- The adapter's own statement: the server classifies once and this file only carries the answer. [4]
- The lane hook and the per-file single read share the classification transport; a dataset review names no tree comparison. [5]
- The summary carries the lane's count on both answered states. [6]
- The shareable hash, read and written. [7]
- A typed answer returned whatever its status; only transport failures throw. [8]
- The selection block every answer carries. [9]
- The three locator declarations. [15]
- The member source carrying them. [16]
- `useReviewCatalogue` owns the behavior described above. [17]
- The entry's summary read and its re-validation generation. [18]
- Catalog/session ownership and cross-tab reconciliation. [19]
- Per-seat UI and evidence state. [20]
- Reliable submission and authoritative withdrawal. [21]
- Lifecycle termination, residuals, and landed cleanup. [22]
- Structural task hierarchy and diagnostic spawn ancestry are built as separate models. [23]
- The shared creation-order helper sorts only when every row has createdAt; unstamped task-document rows retain input order. [24]
- The one full scenario-store reset restores every projected collection, including `closeoutQueues`, in one transaction and is invoked by the development scenario player. [25]
- Series sub-task rows carry optional creation time; task-document sub-task references have a separate shape and share a union for readers. [26]
- The server series builder sorts only fully stamped rows before projection. [27]
- The generated projection mirror this route's suites build fixtures from, the manual sample used for coverage, and the fixture/projection stale gates. [28]
- The route's read-only client and its comparison call. [29]
- **The entry call: the task context alone, because a selector is what it is being asked for.** [30]
- **The reviewed subject as the server's catalogue lists it — presence beside the label, the count field deleted (`ICR-R09@v1`), still the entry's only legitimate selector source, with no path field on purpose.** [31]
- **The entry read's typed envelope, whose refused form carries a refusal and no entries rather than throwing, and whose answered form carries the labelled totals of the whole catalogue.** [32]
- The endpoint the comparison call reaches, with no path among its parameters. [33]
- The closed selector union, the two kinds the server admits. [34]
- The no-store-mutation boundary, stated in the module header. [35]
- The typed result the client returns unchanged. [36]
- The field-for-field mirror of the server's review payload. [37]
- **The inventory's wire types, including the byte form of a name this surface cannot print.** [38]
- **The comparison identity that states whether knowledge was compared, and the staleness union that gained the task-context state.** [39]
- The payload whose comparison may be absent, and the pane that says which question was answered. [40]
- **The request that omits the selector when there is none — the task-context entry.** [41]
- Changed-file navigation belongs to the comparison page ChangeList; SourceContent renders the selected source operands. The retired SourceExplorer is not a current owner. [42]
- **The six-member state literal and the side value whose optional `text` is present only for the two textual states, so no missing or unrenderable side can arrive as an empty document.** [43]
- **The expansion value: both sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** [44]
- **The source-content envelope whose two states are the two answers this route gives, a refusal being a normal one.** [45]
- **The one call that reads its typed body whatever the HTTP status was, and the only one here that does not go through `getJson`.** [46]
- **The generation as an input: the caller's two published tree ids, echoed back in the spelling the route binds.** [47]
- Central expression cards mount SourceContent at the inventory exact tree IDs. [48]
- The renderer the expansion's fields feed, and its three state-decided branches. [49]
- **The generation pins, the published generation identity, and the pins threaded through both master reads.** [54]
- **The new family mirror module, and the re-export that keeps `data/review.ts` the route's one public entry.** [55]
- **The bounded-collection union that lists `family_members` because the server accepts it, and the mirror that never narrows it.** [56]
- **The set a request may name with no cursor, and the reason `family_members` is not in it.** [57]
- **The optional family context whose absence says the body did not come from this route.** [58]
- An incoming link may carry the record its history-row source is about. [59]
- The module comment: what the adapter carries and the three answers it keeps apart. [60]
- The answer of the route. [61]
- One entry on both code sides. [62]
- The request, addressed by number, recorded or invariants, with the optional signal. [63]
- The transient codes and the retry delays. [64]
- The bounded retry of a transient refusal. [65]
- One answer as a read state. [66]
- The comparison a payload names; without it no tree read is made. [67]
- The entries hook aborts a superseded read and returns null without a comparison. [68]
- The leaf-wide hook: abort on cleanup, sequence number, retry, and the enabled flag. [69]
- The workspace enables the leaf-wide read only for a tree comparison and pins it to the payload's number. [70]
- A superseded request is aborted and only the newer answer is shown. [71]
- Loading stays shown during the retries. [72]
- Unavailable is shown only after the bounded number of retries. [73]
- No camelCase key in the real body. [74]
- The module comment: one decode per read, nothing selected or substituted, and getJson unchanged. [75]
- The tokens a reader can be shown. [76]
- The codes and their tokens, with the two transient codes of the leaf-wide view. [77]
- An unknown code is carried as domain-refused. [78]
- The one GET: the optional abort signal, the body read whatever the status, and the two failures. [79]
- The review client imports and re-exports the transport surface. [80]
- A 404 typed refusal resolves through the review client with the refusal intact. [81]
- The same body is dropped by getJson: the shared client's semantics are unchanged. [82]
- selectors.ts changes only the memory-mirror comment from drift_check to drift reporting. driftSegments still uses projec — source ownership, not executed visual proof. [83] [84]

- Review reads share shallow state-bearing-body transport recognition across HTTP statuses. [86]
- Present paging excludes records and allows only knowledge without a cursor. [87]
- Entry catalogue refusal does not remove task-context review reachability. [88]
- Refresh empty-string normalization is specific, rather than universal query normalization. [89]
- Catalogue history/generation keying does not transmit those values; entries/totals can be locally defaulted, and incompatible semantic fields are quarantined. [90]
- Change-set refusal reasons are carried by the current decoder. [91]
- Requirement reads forward context and a path; registered address resolution is listing-based. [92]
- Artifact reader targets also include task reports and decisions. [93]
- Session creation commits only an accepted opener result. [94]
- Open request is identity-addressed and validates acknowledged id/kind and raw-terminal claims. [95]
- Rail placement uses real task document references and role/parent predicates. [96]
- Plural pending interactions count; end/fault/block/wait precede live-turn evidence. [97]
- Reader transport uses a 120-second bound and accepts a string-state body across statuses. [98]
- Reader hash writer omits empty subject keys while preserving explicit repository/commit. [99]
- Lane missing values become unavailable; undefined comparison suppresses the lane hook's request, while the marker client remains promise-based. [100]
- Entry intent counts and attribution share one response with distinct counted/partial/unavailable states. [101]
- Family change facts and source locator meanings are mirrored rather than recomputed. [102]
- Tree retry is bounded and superseded hooks abort and guard their results. [103]
- Creation ordering preserves partially stamped input. [104]
- Volatile-age equality includes elapsedSeconds. [105]
- Full scenario reset increments generation once and clears closeout queues. [106]
- Drift display consumes reporting counts while provider selector definitions remain. [107]
- Active conversation reducer preserves cursor/revision recovery intent without optimistic items. [108]
- Agent roster requires backend identity plus notice/system/agent predicates. [109]
- Historical conversation focus requires opened authority evidence. [110]

- The review wire mirror transports recorded meaning steps with their own attempts/revisions and distinguishes readable none from unavailable. [85]
