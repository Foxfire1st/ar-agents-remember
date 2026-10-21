# dashboard/src/panels/ — Cockpit Panels Overview

## Governing Overview
[dashboard/src overview](../overview.md)

## Purpose

This route contains reusable cockpit panels and focused reading and interaction surfaces. Its parent is the dashboard/src overview. The product bar offers Chats, Operations, Knowledge and File Viewer. Chats is the default; a Knowledge reader hash opens Knowledge. Operations, File Viewer, Knowledge and Chats have retained shell layers so switching destinations preserves their mounted state. Engine Room and other retained layouts are not additional product-bar destinations.

No session-cockpit directory remains as a current owner. Full-page native Chats belongs to cockpit/RoleChats.tsx; lifecycle-list and detail-panel compose Operations navigation and task reading; engine-room owns enclosure/process visualization; file-viewer, changeset and notes-reader own their readers; sprint-graph owns the optional execution graph. ReviewSurface composes the review page through review/reading and review/tree, governed in detail by the [review route overview](review/overview.md). Knowledge-reader composition remains governed here.

`review/canvas/` holds the generated page's panel and its transport: `canvasApi` types the saved-first answer and carries a server refusal as its own error, `canvasModel` derives the panel's phase and keeps a saved page tied to the comparison number and entrypoint it was published against, `canvasHooks` reads a frame state and issues the one explicit start, `canvasDocument` watches the mounted frame for entry, departure and challenge answers so a departed document's channel is revoked, and `CanvasPanel` mounts the sandboxed frame above the untouched deterministic detail. Mounting the panel performs a read and starts no model; authoring begins only from its Generate, Replace presenter or Resume controls, each of which requires an admitted comparison or a recorded attempt. Native task-document chat lives under cockpit/document-chat/, outside this panels directory, and occupies the Operations right rail rather than another full-page Chats destination.

Panels present canonical task hierarchy, structural document-and-role seats, current occupants, source comparisons, knowledge and operational state. The inherited structural contract addresses a seat by document plus role; replacement changes its occupant. Spawn ancestry and lifecycle/session identifiers do not substitute for the task address. Native chat launch, submission and host-state authority belong to RoleChatsPane and document-chat with their retained backend ports; no removed session-cockpit owner is implied.

Family-center member order follows the sidebar's served outline under the same stored order, while retaining per-revision content and a no-outline fallback. Currentness state marks keep their exact entry/state/side words with supplied reasons beside them outside disclosures. Selected one-sided statements and non-authored field rows retain the explicit absent/unreadable/recorded-empty distinctions in the main reading area; Technical details remains an identity/provenance owner.


## Hot Path Summary

Ordinary masters now compose Now then the shared derived Order and ready-next rows. Task heads show both dependency directions; optional Non-goals and Acceptance occupy fixed slots. The complete native task identity/state/head chrome precedes Objective; there is no separate selected lifecycle/series page. Compact progress uses major steps only with cached pointer-rest child details and full nested task reading. Completed master lists use completion time, a newest-five preview and ephemeral reversible sorting; these are display, not start/closeout authority.

Operations selects a projected task/document and mounts its reader. Task prose and references can open registered requirement packets through TaskRequirementLinks. TaskNotes shows a Notes root-folder count, references and recorded role-start reports without constructing a notes-tree total. TaskArtifactReaderTarget currently distinguishes notes, requirements, task-report and decisions. DecisionPreview shows the five newest authored decisions, excluding product-written records from that preview; an omitted-entry link opens the complete log and names the authored decision count. The shared artifact reader owns the corresponding takeover and transport.

A leaf's Intent review control opens task context without requiring a returned subject. Its resolved task/worktree facts select the live or recorded target; it gates the working change-set action, not the intent-review entry. The entry reads changed-intent summary counts, with a separate attribution count, rather than borrowing source-line totals. Pending, partial, unavailable, refused and unrecorded states remain distinct from measured zero. Summary revalidation follows the leaf's own facts and the entry generation; the inherited policy does not promise live delivery while an unchanged detail panel remains open.

The cockpit mounts ReviewSurface through ReviewMain inside Operations’ railed grid for a target carrying review context, with optional family/invariant selector and history. Its tree and ReadingColumn share one comparison-bound change-set model; the page opens unselected unless explicitly addressed. Pending or unavailable subject reads retain the page structure while the selected slot names the requested state. TechnicalDetails receives only the subject’s current answer as that subject’s records.

Knowledge is a task-independent, read-only repository reader addressed by URL hash and memory-tree selection. A followed document opens at its top; Back restores the place left. Citations open beside the document on wide screens and navigate as a page at 70rem and below. Phone browsing exposes the tree through Browse while preserving the document place.

## Construction And Ownership

The review page preserves its tree and reading-column structure across subject reads. Its opening reads task context, catalogue, comparison summary, leaf-wide trees, shown-invariant cards and the lane; card batches start after leaf-wide code facts and catalogue settlement. Selecting a subject reads its own semantic answer and uses the page’s existing card set. ReadGate separates opening work from gesture-gated in-view work. Family guarantee wording keeps its authored operands and separate owner. The document chat may show shared host-start and shown-agent waiting/loading/failure reasons without taking host navigation authority.

### Operations task column

LifecycleList owns the complete served native task tree, entry-own need bands, terminal folds and selection/keyboard reach; AttentionQueue overlays its height with source-scoped dismiss/Clear all and accessible severity, without claiming a task-navigation link. rowState formats each TaskEntry stage/activity through shared status presentation; its hover names current state/stage, repository, current step, progress, host event and unauthored-document facts rather than reporting-lifecycle or inferred worktree state. Removed ChatActivityIndicator and PickupDismiss are not current presentation/action owners. TaskGroupDisclosure retains its shared caret and held-selected-descendant policy. None of these presentation facts changes worktree admission or authors task state.

Task detail prose, `TaskNotes.tsx`, and the shared notes reader use `TaskArtifactReaderTarget` for notes or registered requirement packets. A task page shows one Notes line with the root-folder count, its references, and its recorded role-start reports — no notes tree, no total over the tree. The Operations reader has one fixed skeleton per sprint/master/task form: one complete
head followed by the objective as its first block, before Now or Steps, with omitted empty blocks,
bounded previews and full own views. `detail-panel/taskReader.tsx` owns
form order and identity-keyed reader state; docHead/taskBlocks/skeletons/docViews/task-groups own their
head, tables, shared blocks/views and grouped indexes. Task references/reports have one placed heading,
Notes stays one root-count line, and current summary facts remain authoritative through body hydration.
The page-local appearance lives in pageStyles without repainting shared Panel/Markdown/tokens.
`detail-panel/taskReader.tsx` mounts the shared requirement-link context on every form and composes
the relocated five-newest decision preview from skeletons; `notes-reader/NotesReaderViewer.tsx` owns the kind-aware content transport and takeover, with the shared `ExplorerTree` fed one folder at a time.

The shared task head is the task document’s tray collection surface: it supplies one `AddToTray` offer beside the task identity/status only when a canonical document reference exists, and builds that pick from the reference, ID and title. The head does not own tray deduplication or message delivery.

The reviewer adds supplementary recorded-effect badges to eligible changed outline rows. MeaningEffects owns the open Recorded steps block and keyboard explanations; missing current fields do not become none. Worklist displays the supplied gate verdict, appending effect only from its exact delivered witness rather than inferring a governing row from disposition or reason.

The meaning-state join never changes the selected subject, primary change badge, family roster paging or source inspection state. Keyboard explanations use a native button; the complete Recorded steps block is open, while existing source/evidence disclosures keep their own owners. Older authored-envelope effect lists remain retired and are not the new recorded-history block.

### Shell and shared interaction surfaces

The removed session-cockpit, hosted-session chooser/rail, context bar, terminal, composer, reliable submit/withdraw and keyboard/palette surfaces have no current panels owner. Native full-page Chats is RoleChatsPane. Operations and review share cockpit/document-chat in the same retained right rail; review binds its own canonical task reference, preloads while closed and names pending or missing task resolution. The shell’s TrayLayer accepts chat picks and dashboard highlights, with its separate Tray button beside the four view tabs. Native hosts retain unavailable, Retry, acceptance and delivery authority.

### Operations and operational diagnostics

LifecycleList navigates the one served TaskEntry forest and formats its own canonical stage and optional host activity. Unknown host activity is not paused, a browser clock does not infer state, and the removed raw-lifecycle-over-document precedence and awaiting-developer partition are historical only. Selection initially opens its ancestors and terminal fold. An explicit parent-caret or completed-fold click can release that hold, as can the existing plain arrow action on a focused parent; completed folds gain no arrow path. Releases expire on every selection change, even while the retained list is hidden. Modified browser chords and the list's other keyboard reach remain separate. Unknown activity uses the started word and suppresses row works/paused figures while the shell reports host unavailability once. Master-page list disagreements are served facts with their own count and present-record navigation, never browser membership repair. A started Order target retains the golden in-work graph accent independently of host activity. Shared decorative Dot usage still requires a containing semantic state/severity name; native task status/age presentation has its own shared owner.

DetailPanel resolves one native selected entry, hydrates only its addressed authored document, and composes the task reader with its bound worktree/provider facts. The old lifecycle/series target adapters and SeriesSubTaskNode navigation/creation-sort path are removed, not equivalent aliases. Qualified document references and opaque entry keys stay distinct; a file-less native dependency shows id/title without a document jump or invented state.

The sprint execution graph is optional. CloseoutQueue mounts independently when no execution-graph view is supplied; this rendering support does not prove graph-less atomic task authoring is admitted, and displays the producer's service/source/problem/member projection, including invalid-empty repair actions. The browser does not reconstruct readiness or mutate the queue. Discarded-before-start audit rows retain reason, timestamp and proof fingerprint; discarded counts are displayed separately and do not count as completion.

Hangar displays optional lifecycle-operation kind/status/phase/currentCommand only when projected; the command is ellipsized with full value in title. Engine Room composes selected enclosure processes, official ledger, boot and diagnostics without gate response. Source-lineage diagnostics are read-only, and recovery stays backend worktree-owned. Retirement of provider/gate presentation does not retire ledger/landing authority. FlowTab/flowModels are removed, not current design or runtime owners; eventSummary retains only its actual display seam.

### Intent reviewer reads and navigation

ReviewNavigation owns the catalogue, explicit subject choice and observed comparison generation. A target may name a subject; otherwise the page opens unselected and a catalogue answer selects nothing. Live-review memory input revalidates through the existing stream.

ReviewReadCycle owns keyed answers, retained frame, exact refresh identity and newest-read sequence. It also rejects an older memory-input epoch before the compatible superseded whole-task unshown-cache exception. Selected-subject superseded answers never become current panes or that exception.

One mounted ReviewReadCache retains at most 24 whole-review answers. Generation changes invalidate incompatible whole-review entries; memory invalidation clears them while preserving the observed generation. Explicit refresh forgets the selected review and carries its digest only for the captured key/read. Cache reuse is a prior answer, not fresh verification. Card/source reads have their own transport owners; the removed SourceContent cache is no longer part of ReviewReadCache.

familyWalkMerge owns an admitted roster continuation's merged payload. Admission requires the same comparison, candidate, revision selection, family-side walk and published cursor; stale/refused or conflicting continuations are rejected. Sparse later claims do not erase previously delivered exact member content. The latest admitted response still owns primary statements, inventory, evidence and assessments. Refresh and subject/history changes are replacement reads, not roster merges.

The walked tree remains presentation state derived from admitted answers. In-page selections normally keep the walk under a compatible comparison; previously read families retain their last admitted answer without rereading or replacing the current payload. useReviewPage supplies those kept rows to changeSetModel, and the resulting shared order drives the tree and reading column. Kept-family roster continuation uses its held published cursor.

Explicit task-context substitution, marker follow/return, target or restored outside selection, refresh and incompatible comparisons start the walk afresh. Ordinary in-page subject/block selection keeps it. Search affects the tree alone; sort, view and the existing All changes overlay preserve page ownership. No returned roster is promoted to complete by retained navigation. The page-level selection, URL and kept semantic context remain distinct.

Focus requests are tied to the selection’s tree intent and a later layout effect. Once an answer is available, focus lands on the selected tree row with preventScroll and local tree reveal, provided the reader has not moved focus. Failed/refused answers land once and keep the request for retry. Refresh scrollOnly requests reveal without focusing and wait for a new answer. Page scrolling belongs to the selection’s separate one-scroll owner.

Page controls request only server-published cursors and the declared collection union, including family_members. A refused cursor shows the owner's refusal plus a first-page route for the requested collection. Reported remainder alone does not invent a next-page action. Historical task comparison is explicitly named and published on the surface root.

### Family, subject, source and record presentation

ReviewSurface provides comparison-scoped intent markers and composes ReviewGrid, PageTree and ReadingColumn. reading/useChangeSet owns one leaf-wide trees read plus the page’s summary, lane and shown-invariant card reads; its one changeSetModel feeds both tree and reading order. ReviewWorkspace now supplies selected semantic content and focus helpers, not the whole page’s rail, center or marker provider. The existing ChangeSetViewer opens separately over the retained page.

tree/ReviewTree draws family headings, subject rows, changed locations and explicit unchanged/not-comparable groups from the shared model. Its Changed/All view, one Sort control, tree-only filter and roving focus belong to the new tree. FamilyTree retains exact-revision roster helpers and published-cursor continuation. FamilyReviewCenter and SubjectReview provide a selected subject’s guarantees, statements, semantic facts and revision-specific evidence. Confirmed no-family, unknown membership and ambiguous revisions remain distinct; family context cannot replace an invariant’s own answer.

On measured tree comparisons, the page’s card read supplies exact realization/proof entries to changeSetModel. Shared regions draw one ReviewBlockCard with each entry’s rationale and tray action; currentness keeps its exact entry/state/side and supplied reason. Changed ranges show real before/after diffs; unchanged ranges appear once. The one Changes only / Full context control governs every code range, while content width chooses split or unified layout. Whole-file inspection follows the tree’s All changes and path links. Unmeasured tree comparisons keep code locations unavailable and perform no card read. Worklist marks require the displayed comparison’s matching leaf-wide answer.

The inherited family excerpt arithmetic has a narrower meaning than Git change inventory: it groups realization claims by path plus recorded source identity. exact_recorded_blob is resolved; recorded_object_unavailable, not_requested and missing path/resolution are unmeasured; other supplied resolution values enter the changed collection. The named historical changed states include recorded_blob_mismatch, path_absent, unsupported_locator and entry_not_blob. Observed identities are attached per side, never added to the grouping key. All carried membership rows contribute, including divergent readings of one revision across sides. Rows retain revision identities so repeated display labels cannot erase different revisions. This resolution classification must not be described as the comparison's measured changed-path set.

SourceExplorer and SourceContent are absent. ChangeSetViewer owns comparison-bound changed-file lists and whole-file expansion, with a held lane answer for filters and badges; byte-form All code paths remain explicitly nonopenable. Within review, ReadingColumn shows the Code without invariant lane and exact comparison-bound file diffs, with named non-text, unavailable and truncated states. No per-card Full file surface or dataset expression renderer is mounted.

reading/TechnicalDetails owns one closed provenance disclosure at the reading column’s end: raw movement and comparison records, task/subject identities, origins and hand-off evidence, revision/family context and entry identifiers. Main subject slots retain required judgments, statements and currentness reasons outside it. ReviewRecordPanes still renders selected field rows and supplied record identities. Current judgments and independent proof are distinct from retired assessment/signal/evidence envelopes; none grants approval or waiver.

KnowledgeStatements preserves present/absent/unresolved semantic operands and exact selected revision identity. Two present sides can be diffed; a known absent side differs from an unavailable/unresolved one. Non-authored fields still distinguish missing from recorded empty. Binary belongs to physical source expansion rather than the semantic statement-side union.

ReviewOutcome owns non-payload states and the shared problem block. It states code, detail, offending input or its absence, and next action or its absence. Only a network problem with a retry handler offers retry. An intent-only refusal can offer an explicitly requested task-context/source review; it is not silent substitution. A first refused read has no review payload. With an admitted frame, a later unavailable selection can retain navigation/context while its reading area states the problem and technical records remain unanswered.

### Tree-comparison extensions

Tree comparisons are identified through the review:trees:<n> limitation. Dataset reviews do not acquire these tree-only extensions.

Semantic change-kind facts remain supplied facts, not source-hunk classification. changeSetOrder combines the served outline, admitted card/code/currentness facts and kept rows into one model for tree and reading order. Changed/All controls which subjects and locations the model shows; the tree filter narrows tree rows without filtering the reading page. The one Sort preference uses review.tree-order.v1, with Priority as default, legacy triage interpreted as Priority, Authored retained, and unavailable memory sorts disclosed rather than guessed.

ChangeBadges states supplied change, membership and guarantee facts with their reasons. Subject content keeps semantic badges separate from the one-line tree’s compact state. j/k traversal uses displayed changed block identities, followed by loaded lane hunks in file order; shared-region aliases are one stop. Unknown/unchanged blocks and roster-continuation controls are excluded. Traversal selects through the page owner, reports either end without moving selection, and is disabled while the comparison overlay is open.

Code without invariant is an inline reading section and a tree destination with its lane files. Unexplained and Unknown attribution also offer Full page links into a comparison-bound ChangeSetViewer. One scoped lane answer supplies their counts, file membership and held overlay filters; pending, unavailable and unmeasured scope remain distinct from zero. Worklist replaces the change-set body in the reading column and keeps its currentness, problems, history/gate facts and changed-knowledge links. The task entry’s attribution count remains independent of source-line totals.

Hunk markers consume the same per-file classification, not a second client intersection. Confirmed-unregistered or wholly unreadable files receive file-level notes; other files expose owner-hunk marks with realizations and proofs separately. Family occurrences retain membership state and unknown reason; unknown attribution is not No recorded family. Compact labels apply below 40rem. Placement uses the owner's side line numbers and only hunks/changed lines the pane actually draws.

Marker scope shares in-flight classification acquisition for listed changed paths and retains successful answers within comparison scope; non-ready attempts can be reacquired. A complete inventory’s unlisted path causes no marking read, while partial inventory retains an explicit unlisted state. Card excerpts compare only drawn sides, require differing side blobs and place drawn owner hunks. Loading, unavailable and content-mismatch notes remain explicit, including intent marks loading…; SourceContent’s full-source marking branch has been removed.

Following a marker selects the invariant’s own review through ordinary page navigation, retaining an explicit family/member context when supplied. Back restores the prior subject, family selection and worklist choice, clears the tree focus request and returns focus to the originating marker. The visible Back control owns that return. Opened-path, local diff-layout and Full file state no longer belong to workspaceState; code context is page-wide and code layout follows reading width. Pane/gutter expansion and passive-hold cleanup retain their separate owners, and off-screen editor marks are not promised tab stops.

Tree-only IntentWordDiff presents the supplied exact text and per-revision conditions/exclusions/guarantees without creating semantic approval. textDiff compares ordered non-whitespace tokens: whitespace-only changes preserve those tokens, whereas joining or splitting a word changes them. Its bounded token matrix can fall back to exact coarse runs; rewrite uses a strict ratio above0.5. List alignment separately refuses guessed pairs over its cell budget and pairs remaining in-bound gaps only at equal cardinality after exact moved matches. Layout preference and exact-text disclosure remain presentation owners.

One comparison-bound leaf-wide read feeds subject worklist content and the separate Worklist view. PageReading places LeafWorklistView in ReadingColumn’s replacement slot. Selected semantic details still join canonical identity through SubjectKnowledge/SubjectWorklistItems and name absent identities, mismatched comparisons, incomplete worklists and failed reads. Shared memory-diff content remains outside the family/member/unselected semantic centers.

### Knowledge reader

KnowledgeReader owns toolbar, independently scrolling tree/document/aside composition, address-bound read, citation and outline. ReaderToolbar owns repository/tree selection, record lookup, selection/pin notes and named side-read failures. A single selection acquisition is shared with the Records branch. KnowledgeTree adapts shared ExplorerTree, consuming optional hasKnowledge/hasOverview/coverage facts, entry counts, Show every path and count rows. The Records branch includes families, decisions and other records; invariants remain in path views.

The Knowledge document column keeps its shared tree/outline toggles outside the panels they hide. Left/right `knowledge` state controls the corresponding mounted panel and resize handle; a citation opened in the local aside first shows that aside. The tree toggle is hidden where Browse owns the full-screen tree at 40rem and below, and the outline toggle is hidden where its aside is not shown beside the text at 70rem and below. The reader’s mounted citation case checks reopening an initially hidden aside without replacing the prose or changing its scroll/hash; this is stubbed-media DOM evidence, not a browser geometry measurement.

PathViews orders prose, invariant states, local/routed families, linked records and references last; directories use bounded summaries and paged subtrees, with without-proof and census views. Empty sections are omitted. TruthView renders record fields, invariant/family details, complete decisions using derived status, both link directions with unreadable links named, and timeline source states. History rows show effect and because: record targets navigate and requirements are named. Incoming history links identify the record the row concerns rather than inventing a history-row page. Reader parts link numbered markers in text nodes only; shared Markdown and referenceMarkers own headings/markers, and ReaderCode reuses FilePane. The inherited backend ownership assigns tree coverage to a code pass plus memory enumeration, with paths delegating tree listing rather than files enumerating directories.

The native role-chat model selects canonical role occupants without buildRailModel or a hosted session rail. FlowTab is removed and supplies no current drawing/prose, live chat or store authority.

## Invariants And Boundaries

The policies above are inherited semantic intent alongside specifically inspected source predicates. They are not newly adopted invariant or family records. Historical candidate lists for L31–L35 remain proposals, not ingestion or present acceptance.

Panels consume canonical stores and authority clients; they must not create private durable session catalogues, conversation indexes or submission ledgers. Native document chat and full-page host chat keep their distinct selection/creation contracts and host-owned delivery/readiness. The removed project-session submission, withdrawal and interaction controls are not restored by these panel projections or by compatibility event rendering.

Review remains display/navigation only: it cannot author assessment, waiver, approval or publication. Source inventory is complete within its declared scope regardless of attribution; partial knowledge, unreadable sides, missing totals and unmeasured counts retain their states and reasons. Cached content and kept families are prior reads, not current verification. Bound code trees, memory trees, history context, subject and page identity must remain visible rather than being silently re-resolved.

Keep-alive memoization is an inherited performance boundary: shell rerenders should not rebuild unchanged panels, and their own subscriptions stay live except the hidden task list, which remains mounted with a no-op subscription and catches up when active. Naming/splitting conventions use a canonical entry and short responsibility-based siblings. Hand-maintained sample/fixture builders demonstrate mirror-conforming shapes, not producer completeness; generated TypeScript schema and its stale check own the producer contract. Dot naming remains the containing component's responsibility.

The parent delegates detailed child mechanisms and preserves source-lineage ownership. Retired provider presentation, static flow prose and event-label fallback are distinct seams. No broad no-impact assertion or runtime tool availability follows from static source drawings.

## Historical And Verification Limits

This proposal read all original card prose and inspected bounded present-source witnesses at the stated source head. It ran no tests, imported no product entrypoint, exercised no browser or service, and produced no execution/acceptance verdict. Original test populations, mutation outcomes, fixture digest checks, provenance receipts, delivery approvals and rendered measurements are historical claims rather than fresh checks. Their original references remain the parent's preservation responsibility.

ICR-L33's Operations landed-leaf admission and second opened-key collapse store were explicitly withdrawn by the recorded a9a1a41b emergency revert. Their historical 110 landed rows, 19 auto-closed masters, 161-row subtree and count-tooltip behavior are not current claims. The inspected collapse hook has only operations.tasks.collapsed.v1 and toggleCollapsed; LifecycleList has the bare Tasks count. The separate change-set includeLeaves/generation behavior survived. The card's characterization of that emergency commit as lacking a curator pass is inherited history, not reconstructed Git adjudication.

ICR-L44's mixed fixture generations and inaccessible current-route reproduction were recorded as superseded by MIK-L31 recapture, including the six formerly retained old bodies and refreshed case headers. L31/L32/L34/L35 merge, rerun and Todo resolutions remain recorded history; no recapture or digest verification was repeated here. The historical claim that 29 unconverted reads were unchanged before MIK-R37 remains bounded to that rerun, not all current datasets or leaves.

ICR-L36's divergent family rendering was evidenced through a labelled captured familyReview.walkFinal fixture, not discovered live data. Its historical live scan attempted 36 leaves, resolved one leaf serving three families, and received candidate_dataset_absent from the other 35, including ICR-L36 itself. Zero divergence among those three served families says nothing about the 35 unreachable leaves. The named f1/raw/live-truth.json and f1v/raw/vf1-live-scan.json witnesses were not available as examined evidence in this source-only adjudication; preserve their exact historical scope and refusal rather than declaring live divergence absent. The recorded grouping measurements of eight side-counted instances into two keys are fixture/build measurements, not present acceptance. Use each side's reading/resolution wording; the superseded phrase implying every changed address was resolved collides with exact_recorded_blob.

ICR-L25's responsive verification used the review-surface root, not just the inner workspace. Its historical correction measured 51 reviewer descendants past the edge becoming zero while 13 cockpit-chrome elements remained, pane widths 565→294px, user-scrollable count 0→1 and wheel movement 0→800px. Those browser witnesses were not re-examined here. Present source instead gives ReadingColumn the scrollport above 40rem and the stacked ReviewMain the scrollport below it; styling alone does not re-establish those measurements or clear the remaining shell-owned chrome.  The shell's hidden viewport overflow and internally scrolling panels remain separate composition responsibilities.

The historical amber repair removed copied wash literals through an oklab mix of var(--amber); it did not establish zero computed oklch values, since tokens themselves use oklch. Browser acceptance and keyboard traversal assigned to ICR-R24, and assembled acceptance assigned to ICR-R25/A14/A15, are not supplied by this source adjudication or by mounted fetch-stubbed component evidence. Earlier paging/history/applicability leaves explicitly retained those ownership limits.

L47's late-catalogue remount/focus and file-size findings were recorded as delivered by L48; obsolete line counts are not current architecture. Superseded early entry gates, catalogue-derived entry state, removed catalogue refresh/invalidation controls, three-pane-first composition and whole-file-only expressions must not be presented as active behavior.

Historical notes below retain their epochs, not current predicates: whitespace deletion previously could join words while being called whitespace-only; the current token-boundary predicate corrects that. Prior control-placement, repeated-unknown and sticky-step observations remain historical rather than new execution or acceptance.

The card historically reported no configured Domain Documentation and no governing cross-repository implementation source. Provider/settings configuration and all production import destinations were not re-audited here; retain these as inherited scope statements, not newly verified whole-repository absence.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/`                          |

| Responsibility | File onboarding |
| --- | --- |
| Review child route — the shared change-set model, tree and reading page | [overview](review/overview.md) · [changeSetOrder.ts](review/changeSetOrder.ts.md) · [ReviewTree.tsx](review/tree/ReviewTree.tsx.md) · [ReadingColumn.tsx](review/reading/ReadingColumn.tsx.md)  |
| Review child route — the workspace and comparison-bound source navigation | [ReviewWorkspace.tsx](review/ReviewWorkspace.tsx.md) · [ChangeSetViewer.tsx](changeset/ChangeSetViewer.tsx.md) |
| Review child route — the leaf's knowledge panel and its notice | [LeafKnowledgeChanges.tsx](review/LeafKnowledgeChanges.tsx.md) · [LeafKnowledgeNotice.test.tsx](review/LeafKnowledgeNotice.test.tsx.md) |
| Review child route — the mounted family composition cases | [ReviewWorkspace.family.test.tsx](review/ReviewWorkspace.family.test.tsx.md) |
| Review child route — the walked tree and the traversal between changes | [walkedTree.ts](review/walkedTree.ts.md) · [changeTraversal.ts](review/changeTraversal.ts.md) |
| Review child route — the captured family bodies those cases are driven with | [familyReview.complete.captured.json](review/familyReview.complete.captured.json.md) · [familyReview.continued.captured.json](review/familyReview.continued.captured.json.md) · [familyReview.emptyRoster.captured.json](review/familyReview.emptyRoster.captured.json.md) · [familyReview.identical.captured.json](review/familyReview.identical.captured.json.md) · [familyReview.oneSided.captured.json](review/familyReview.oneSided.captured.json.md) · [familyReview.truncated.captured.json](review/familyReview.truncated.captured.json.md) · [familyReview.walkFinal.captured.json](review/familyReview.walkFinal.captured.json.md) · [familyReview.capture-provenance.json](review/familyReview.capture-provenance.json.md) |

## Task reader grant control

taskReader renders one Direct execution switch only on a document-backed subTask's own page when its native entry stage is planned, bare giver words on other granted task states, and nothing on grantless states. Master/sprint index rows carry neither a grant control nor a grant mark. The grant hook posts only through the existing adapter and preserves real state on refusal; client affordance/status is not the backend start-evidence gate.


## Current Behavior

the detail panel's change-set bar now aborts its own counter read on a task switch and renders no failure for it. The task-reuse and task-switch cases pin the other side: the left page's change set, summary and body end with the selection, while a revisited task is answered from the body the first visit retained with no second request. The mounted chat case pins the operation-level promise that the newly selected task's chat is dispatched and bound while four abandoned page producers remain slow.

MIK-R174 and MIK-R175 changed two visible Operations contracts. The started band now orders the paused rows the host timed newest first, ahead of the paused rows it did not time, which keep the server's order; a missing time is never read as zero or as now. And a step dot shows only its own tooltip: the row line and the figure box carry no native title, the row's hover text lives on its own cells, and the tooltip keeps its id and status word whole while only the title wraps. Both are presentation facts — served order, task state and row admission are unchanged.

## Evidence

- The started band orders host-timed rows newest first and leaves untimed rows in the server's order. [197]
- The row's native title is gone from every ancestor of a step mark while its own cells keep the hover text. [198]

- The list combines selection-episode releases with parent-only unmodified arrows and observes hidden selectedId changes. [194]
- The shared master-page disagreement renderer draws served rows and offers jumps only to records in the task map. [195]
- Marks only from the owner's response, placed on its side lines. [5]
- Every owner hunk a pane draws is placed; the list and the reveal of a return. [6]

- The unknown-membership state in the rail. [9]
- The explorer's and the details' labels from the lane. [10]

- The entry's count as its own element. [14]
- The decision, the ratio and rule 1a. [15]
- The tree-comparison scope, the statement area and the changed guarantee. [16]
- Each side's text from its own row, the filtered field rows, and the text-first decision. [17]
- On real bodies: a tree review word-diffed, a dataset review as landed, and one guarantee revision never called unchanged. [19]
- The receipt of the captured bodies (five since L31). [29]
- The receipt's MIK-L31 re-capture, which replaced the not-re-captured section. [30]
- The case header stating which bodies were re-captured (both captures since MIK-L31's follow-up). [31]
- The header count itself. **Withdrawn in part:** the tooltip this row cited stated *what* the count counts, and the L33 revert removed it with the landed-leaf change — the h2 is again a bare `Tasks · {count}`. [39]
- The bar's request for the net's per-leaf attribution. [40]
- The `Cockpit` view map contains the declared view map. [41]
- The current Chats cockpit keeps RoleChatsPane mounted while hidden; the former SessionsView topology is historical, not a current mount. [42]
- The current persistent Chats layer mounts one RoleChatsPane; the former SessionsView selected-context wiring is historical, not a current mount. [43]
- Dashboard state authority is held by `DashboardState`, `dashboardStore`, and `applySnapshot`. [44]
- The production application route is owned by `App`. [45]
- The production route returns `Cockpit`, which wires the live streams and renders `CockpitShell`, opening it on the Knowledge view for a `#knowledge?…` reader URL (MIK-R29). [46]
- `CockpitShell` defaults `initialView="chats"`; `VIEWS` is the four-entry product bar. [47]


- LifecycleList consumes native entry rows and preserves grouping, selection and one-shot reveal without the removed lifecycle hierarchy adapter. [52]



- DetailPanel resolves the selected native entry through its state owner and renders TaskDocumentPanel, rather than separate lifecycle/series reader targets. [53]



- Native task stage/activity/eventAt replaces the removed session State/Phase live-terminal partition as the Operations state input. This is a distinct model, not a renamed session vocabulary. [54]



- Native entry fixture defaults copy specific sampled identities while explicitly declaring planned/count/collection defaults; there is no current lifecycle factory or claim that every value is server-derived. [55]



- The typed native projection factory supplies tasks/taskCounts and analytics defaults. Mirror-conforming sampled shape is not producer completeness or fresh test/runtime acceptance. [56]

- `Dot` renders its state glyph inside `aria-hidden="true"`. [58]








- **The entry threading the published generation into the viewer target.** [63]
- **The generation state the button carries from a successful master read.** [64]
- Family excerpt arithmetic groups recorded addresses and distinguishes changed, resolved and unmeasured realization readings. [110]
- Per-side resolution and observed identities attach to the same recorded-address key. [111]
- **The mounted case: the rendered count is the body's distinct excerpt set, every row's collapse count is the body's own group size, and EVERY rendered row's `data-sides` is checked against the sides the body resolves that excerpt on — the page's own both-sides sentence verified row by row against the body, not read from the page.** [113]
- **The new unit lane for the same arithmetic, its own statement of which inputs are constructed, and the pair of cases that state the whole key contract between them (recorded keeps two blobs at one path apart; observed may not, because two sides of one address legitimately see different bytes).** [114]
- The compact control, its brief states and its disclosure (since MIK-L32 with the lane's count beside `+N −N`). [115]
- The entry mounted in place of a change-set button. [116]
- The leaf-scoped facts and re-validation generation. [117]
- A history row's line: its effect, and its because targets as links. [120]
- An incoming link from a history row names the record the row is about. [121]
- The panel: status line, degraded sides, diff, currentness, worklist. [125]
- The notice for a loading and for an unavailable read; nothing for any other phase. [126]
- The notice says that it is computing, as a status region. [128]
- The notice names the failure and its action. [129]
- The surface's hook composes navigation, read cycle, cache, selection, refresh and retry, and the reading status. [131]
- The read cycle: the read state bound to its question, and the task-context frame. [133]
- The bounded cache of one mounted surface and its generation test. [134]
- The one failure and refusal block, with the retry control of a network failure. [135]



- One step of the walk: an in-tree selection keeps, any other selection and another comparison replace. [144]
- A refresh starts the tree afresh and asks only for a scroll; the retry of a failed refresh is the refresh again. [147]
- The page controls: a next page only for a published cursor, and the refusal of a requested page. [151]
- The mounted case of the key walk on real data. [152]
- The mounted cases of the reviewer between a selection and its answer. [153]
- The notice draws nothing for a dataset review. [154]

- Current ownership/control, without execution or runtime tool exposure inferred. [159]







- The recorded-history block owns full step fields, strict states and native keyboard explanations, not a computed verdict. [163]

- The intent entry always opens task-context review; liveness selects the live or recorded target, while summary state labels rather than gates the button. [59]
- The subject-catalogue hook serves reviewer navigation, not task-entry admission; the task entry reads a summary and no catalogue. [60]
- `DocChangeSetBar` checks whether any entry worktree has `codeWorktreeExists` or `memoryWorktreeExists`; that liveness selects live versus recorded entry context, not catalogue-subject admission. [61]
- The catalogue client and subject shape serve reviewer subject navigation; task-entry summary and clickability are separate. [62]
- Artifact reader includes task reports and whole decision logs [165]
- Decision preview excludes product records and limits authored entries to five [166]
- Superseded successful whole-task reads have a guarded unshown-cache exception [167]
- Continuation admission checks identity and cursor; sparse claims preserve earlier content [170]
- Walked families preserve prior reads but reset across incompatible comparison/selection [171]
- Semantic triage counts returned facts, states unknown totals and keeps scoped weight at least unknown [172]
- Classification cache shares successful acquisition but releases non-ready attempts [174]
- Excerpt marker loading states the `intent marks loading…` note rather than staying quiet. [175]

- Family expression keys use recorded identity; observed readings stay per side [178]

- Network-only retry and intent-only source alternative remain explicit [181]
- The comparison page's All code list identifies byte-form inventory paths as explicitly nonopenable [182]
- Current intent entry uses liveness to choose recorded target rather than hide entry [183]
- Master change-set read includes leaves and carries published generation [184]
- Collapse hook has one stored key set and toggle API [185]
- Knowledge reads bind to address; reader shares records and responsive citation navigation [186]

- Exact currentness mark words coexist with an open supplied-reason sibling. [165]
- Non-authored field rows distinguish absent and recorded-empty values. [166]

- The task list head owns the attention bell and the actual row renderer. [190]
- The bounded Popover/Dialog retains source-scoped queue actions. [191]

- The remaining Operations rowState and treeRows modules own task-row facts and hierarchy; the removed chat activity indicator supplies no current state owner. [192]
- The conforming example on real data. [27]
- The one case: the landed workspace over a converted leaf's trees. [28]
- The hand-kept snapshot payload provides the generated timestamp. [57]
- **The two hoisted owners the member attribution and the family collection share, so the two readers cannot drift.** [112]


- Selected family and invariant centers join recorded steps to their own identities and preserve independent guarantee/statement/source/evidence content. [162]
- Four product destinations, Chats default and retained Operations/File/Knowledge composition Family-center order shares the outline ranking while retaining the semantic revision roster. [164]



- The task-page grant switch keys on native planned stage and the document subTask kind; other granted states show bare words. This does not move grant authority into the browser. [193]

- Whitespace-only classification preserves ordered non-whitespace tokens; rewrite ratio is strict, and bounded list alignment is a separate no-guessed-pairs mechanism. [177]
- Technical details projects the current payload without restoring retired assessment/evidence envelopes; open main facts remain a separate owner. [136]
- Semantic statement states and selected-revision operands govern rendering; missing/unresolved is not known absence. [180]

- Current composition owners for the review page account. [199]
- Current shell owners for the review page account. [200]
- Current navigation owners for the review page account. [201]
- Current reads owners for the review page account. [202]
- Current selection owners for the review page account. [203]
- Current chat owners for the review page account. [204]
- Current tray owners for the review page account. [205]
- Current watch owners for the review page account. [206]
- Current cache owners for the review page account. [207]
- Current model owners for the review page account. [208]
- Current markers owners for the review page account. [209]
- Current tree owners for the review page account. [210]
- Current family owners for the review page account. [211]
- Current source owners for the review page account. [212]
- Current lane owners for the review page account. [213]
- Current details owners for the review page account. [214]
- Current sort owners for the review page account. [215]
- Current traversal owners for the review page account. [216]
- Current worklist owners for the review page account. [217]
- Current layout owners for the review page account. [218]
- Current focus owners for the review page account. [219]
- Family/member semantic slots preserve guarantees, meanings, realization resolution, evidence and subject worklist; the reading page owns code blocks. [109]
- Inline lane content and Full page actions share one comparison-bound lane read and retained overlay filters. [11]
- Selected semantic details retain the subject worklist/knowledge notice owner; page-level Worklist is separate. [122]
- ReadingContext passes only the matching leaf-wide worklist to page cards and selected semantic content. [123]
- PageReading places WorklistView in the reading-column replacement slot; selected semantic details retain their own subject worklist. [124]
- useChangeSet owns leaf-wide trees, shown-invariant cards, summary and lane; one model feeds both columns. [127]
- useChangeSet supplies one comparison-scoped lane read to page content and held comparison-page facts. [13]
- Operations’ ReviewMain mounts the optional-subject/history reviewer beside the stable shared task chat. [130]
- Page structure persists over an admitted frame; TechnicalDetails labels subject records from shown answers only. [132]
- ReadingColumn is the persistent reading scrollport with page-level notes, summary, subject sections, lane, canvas and details. [137]
- changeSetModel applies the shared sort to subjects/locations without inventing semantic or source facts. [138]
- One Sort uses review.tree-order.v1; Priority defaults and legacy triage maps to Priority. [139]
- Traversal follows displayed changed blocks then loaded lane hunks and excludes continuation controls. [140]
- useBlockTraversal selects through the page owner and binds the reviewer-zone commands only while the overlay is closed. [141]
- Traversal end status is scoped to the committed stop identities. [142]
- ReviewTree renders the shared model, tree-only filter, Changed/All view and one Sort. [143]
- useReviewPage advances the walk and supplies one selection/model to the tree and reading column. [145]
- Every page selection advances tree intent; ordinary in-page selections keep the walk while explicit outside callers reset it. [146]
- Kept families feed the shared change-set model; ReviewNavigation no longer mounts a separate family catalogue control. [148]
- Previously read kept families retain admitted semantic context under the shared page model. [149]
- Selection focus lands locally on the tree after the relevant answer, preserves moved focus and keeps failed/refused requests for retry. [150]
- The page’s subject content renders recorded effect facts while compact tree rows keep their own single-line presentation. [160]
- ReviewTree’s compact rows are navigation over the shared model; semantic records remain in reading subject slots. [161]
- Reading page context remains mounted while selected answer status changes; the comparison overlay retains the hidden inert page underneath. [168]
- ReviewSurface owns the keyboard zone; ReadingColumn or stacked ReviewMain owns vertical scrolling. [169]
- Block traversal excludes unknown/unchanged blocks and admits loaded lane hunks in file order. [173]
- Marker Back restores subject, family selection and worklist, then returns focus to the origin marker. [176]
- Page cards and selected subject worklist content require the same comparison’s matching leaf-wide worklist. [179]
- Compact tree row labels and reasons come from the shared model, preserving one line and complete accessible names. [18]
- useChangeSet shares one leaf-wide comparison with model/cards/worklist; useSurface wires active live memory invalidation. [196]
- ReviewBlockCard renders a shared region with entry-specific rationale and tray actions. [24]
- changeSetModel groups shared regions and gives one order to tree and reading content. [25]
- Page card reads are tree-comparison-bound; worklist marks use the matching leaf-wide comparison. [26]
- ReviewSurface owns page markers around ReviewGrid and ReadingColumn; ReviewWorkspace supplies selected semantic content. [8]


- The task document head offers one canonical-reference task pick only when that reference exists. [220]
- A locally opened citation shows the Knowledge aside before selecting its citation. [221]
- The Knowledge document column provides shared tree and outline toggles. [222]
- Knowledge sidebar toggles follow the responsive tree and aside layouts. [223]
- The Knowledge toggles stay in the document column while the aside and its resize handle are hidden in place. [224]
- The mounted citation case checks recovery from a hidden aside while retaining the same prose node, scroll position and path address. [225]
