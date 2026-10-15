# dashboard/src/panels/ — Cockpit Panels Overview

## Governing Overview
[dashboard/src overview](../overview.md)

## Purpose

This route contains reusable cockpit panels and focused reading and interaction surfaces. Its parent is the dashboard/src overview. The product bar offers Chats, Operations, Knowledge and File Viewer. Chats is the default; a Knowledge reader hash opens Knowledge. Operations, File Viewer, Knowledge and Chats have retained shell layers so switching destinations preserves their mounted state. Engine Room and other retained layouts are not additional product-bar destinations.

No session-cockpit directory remains as a current owner. Current full-page native Chats belongs to `RoleChatsPane` in cockpit/RoleChats.tsx outside panels; lifecycle-list and detail-panel for Operations navigation and task reading; engine-room for enclosure/process visualization; file-viewer, changeset and notes-reader for their respective readers; and sprint-graph for the optional execution graph. The intent reviewer and Knowledge reader have file cards under review/ and knowledge-reader/ but no separate route overview: this parent governs their composition. Native task-document chat lives under cockpit/document-chat/, outside this panels directory, and occupies the Operations right rail rather than another full-page Chats destination.

Panels present canonical task hierarchy, structural document-and-role seats, current occupants, source comparisons, knowledge and operational state. The inherited structural contract addresses a seat by document plus role; replacement changes its occupant. Spawn ancestry and lifecycle/session identifiers do not substitute for the task address. Native chat launch, submission and host-state authority belong to RoleChatsPane and document-chat with their retained backend ports; no removed session-cockpit owner is implied.

Family-center member order follows the sidebar's served outline under the same stored order, while retaining per-revision content and a no-outline fallback. Currentness state marks keep their exact entry/state/side words with supplied reasons beside them outside disclosures. Selected one-sided statements and non-authored field rows retain the explicit absent/unreadable/recorded-empty distinctions in the main reading area; Technical details remains an identity/provenance owner.


## Hot Path Summary

Ordinary masters now compose Now then the shared derived Order and ready-next rows. Task heads show both dependency directions; optional Non-goals and Acceptance occupy fixed slots. The complete identity/body/series chrome precedes Objective. Compact progress uses major steps only with cached pointer-rest child details and full nested task reading. Completed master lists use completion time, a newest-five preview and ephemeral reversible sorting; these are display, not start/closeout authority.

Operations selects a projected task/document and mounts its reader. Task prose and references can open registered requirement packets through TaskRequirementLinks. TaskNotes shows a Notes root-folder count, references and recorded role-start reports without constructing a notes-tree total. TaskArtifactReaderTarget currently distinguishes notes, requirements, task-report and decisions. DecisionPreview shows the five newest authored decisions, excluding product-written records from that preview; an omitted-entry link opens the complete log and names the authored decision count. The shared artifact reader owns the corresponding takeover and transport.

A leaf's Intent review control opens task context without requiring a returned subject. Liveness selects the live or recorded target; it gates the working change-set action, not the intent-review entry. The entry reads changed-intent summary counts, with a separate attribution count, rather than borrowing source-line totals. Pending, partial, unavailable, refused and unrecorded states remain distinct from measured zero. Summary revalidation follows the leaf's own facts and the entry generation; the inherited policy does not promise live delivery while an unchanged detail panel remains open.

The cockpit mounts ReviewSurface for a change-set target carrying review context, including optional family/invariant selectors and history. ReviewSurface composes navigation, the question-bound read cycle, bounded cache, refresh/retry, workspace and technical disclosure. A subject answer is shown under the question it answers. Pending or unavailable subject reads can keep the workspace mounted over the last admitted task-context frame while the reading area states the requested subject's status. Technical records receive only the current answer.

Knowledge is a task-independent, read-only repository reader addressed by URL hash and memory-tree selection. A followed document opens at its top; Back restores the place left. Citations open beside the document on wide screens and navigate as a page at 70rem and below. Phone browsing exposes the tree through Browse while preserving the document place.

## Construction And Ownership

### Operations task column

LifecycleList owns the complete left task tree, priority words, completed folds and selection/keyboard reach; AttentionQueue overlays its height with source-scoped open/dismiss/Clear all and accessible severity. rowState separates document truth from reporting lifecycle state and keeps current task/lifecycle/progress/worktree facts in the hover. Removed ChatActivityIndicator and PickupDismiss are not current presentation/action owners. TaskGroupDisclosure retains its shared caret and held-selected-descendant policy. None of these presentation facts changes worktree admission or authors task state.

Task detail prose, `TaskNotes.tsx`, and the shared notes reader use `TaskArtifactReaderTarget` for notes or registered requirement packets. A task page shows one Notes line with the root-folder count, its references, and its recorded role-start reports — no notes tree, no total over the tree. The Operations reader has one fixed skeleton per sprint/master/task form: one complete
head followed by the objective as its first block, before Now or Steps, with omitted empty blocks,
bounded previews and full own views. `detail-panel/taskReader.tsx` owns
form order and identity-keyed reader state; docHead/taskBlocks/skeletons/docViews/task-groups own their
head, tables, shared blocks/views and grouped indexes. Task references/reports have one placed heading,
Notes stays one root-count line, and current summary facts remain authoritative through body hydration.
The page-local appearance lives in pageStyles without repainting shared Panel/Markdown/tokens.
`detail-panel/taskReader.tsx` mounts the shared requirement-link context on every form and composes
the relocated five-newest decision preview from skeletons; `notes-reader/NotesReaderViewer.tsx` owns the kind-aware content transport and takeover, with the shared `ExplorerTree` fed one folder at a time.

The reviewer adds a compact recorded-effect badge to eligible changed outline rows while keeping navigation one line. MeaningEffects owns the open Recorded steps block beside selected intent/guarantee content and all nine keyboard-operable label explanations. Family/member and no-subject centers reject missing current fields without inventing labels. Worklist rows show their governing row’s effect only; earlier attempt judgments remain in the reading area.

The meaning-state join never changes the selected subject, primary change badge, family roster paging or source inspection state. Keyboard explanations use a native button; the complete Recorded steps block is open, while existing source/evidence disclosures keep their own owners. Older authored-envelope effect lists remain retired and are not the new recorded-history block.

### Shell and shared interaction surfaces

The removed session-cockpit, hosted-session chooser/rail, context bar, terminal, composer, reliable submit/withdraw and keyboard/palette surfaces have no current panels owner. Native full-page Chats is RoleChatsPane; native task-document chat is cockpit/document-chat, addressed by canonical document and role-launch records. Those hosts retain their own unavailable, Retry, acceptance and delivery boundaries; panels do not manufacture readiness or permission from a summary.

### Operations and operational diagnostics

LifecycleList owns task navigation, grouping, selection and re-show behavior. A bound lifecycle's raw state takes precedence over the task-document status mapping. Document status and lifecycle state are separate vocabularies; awaiting-developer belongs to the inherited live partition. Dot is decorative and aria-hidden: the containing panel must provide the state/severity name through a suitable semantic wrapper or named option.

DetailPanel resolves task, lifecycle and series reader targets. TaskSubTaskRefNode and SeriesSubTaskNode share row fields but retain different navigation/time fields: linkedLifecycleId is a master-task navigation capability, and creation ordering belongs to the series path that carries createdAt. Typed masterRef rows use docPathForRef when a projected destination exists and preserve the explicit unprojected rendering otherwise.

The sprint execution graph is optional. CloseoutQueue mounts independently when no execution-graph view is supplied; this rendering support does not prove graph-less atomic task authoring is admitted, and displays the producer's service/source/problem/member projection, including invalid-empty repair actions. The browser does not reconstruct readiness or mutate the queue. Discarded-before-start audit rows retain reason, timestamp and proof fingerprint; discarded counts are displayed separately and do not count as completion.

Hangar displays optional lifecycle-operation kind/status/phase/currentCommand only when projected; the command is ellipsized with full value in title. Engine Room composes selected enclosure processes, official ledger, boot and diagnostics without gate response. Source-lineage diagnostics are read-only, and recovery stays backend worktree-owned. Retirement of provider/gate presentation does not retire ledger/landing authority. FlowTab/flowModels are removed, not current design or runtime owners; eventSummary retains only its actual display seam.

### Intent reviewer reads and navigation

ReviewNavigation owns catalogue acquisition, selected subject, reader engagement and the catalogue rail. The opening hold is bounded at 750ms. A prompt catalogue can choose the initial subject before the first review request; a slow one releases task-context reading. A reader gesture freezes the subject against late catalogue selection, while an idle reader may still land on the first family without remounting. Catalogue refresh remains explicit and comparison-scoped rather than subscribing to unrelated analytics publications.

ReviewReadCycle owns question keys, read sequencing, retained coherent answers, the context-bound frame and refresh identity. Keys distinguish repository/master/leaf, live or history context, subject and page. Cleanup plus sequence checks prevent superseded replies from writing current panes. There is one specific reuse exception: a successful superseded whole-task read with no selected subject, no page selection and no carried refresh identity can be cached unshown. ReviewReadCache refuses that result if it conflicts with its known comparison generation. Superseded selected-subject replies are dropped.

A mounted ReviewReadCache holds at most 24 whole-review answers and 32 source-content answers with LRU eviction. Observing an incompatible comparison clears both stores. Cached returns avoid another request but are not live verification. Refresh invalidates the selected cached review and asks again. A carried digest is sent only by the refresh read whose sequence and question match the captured identity; another subject, history context or later read carries no such replacement identity. ReviewRefresh describes only the completed read that actually carried it, including both identities when superseded.

familyWalkMerge owns an admitted roster continuation's merged payload. Admission requires the same comparison, candidate, revision selection, family-side walk and published cursor; stale/refused or conflicting continuations are rejected. Sparse later claims do not erase previously delivered exact member content. The latest admitted response still owns primary statements, inventory, evidence and assessments. Refresh and subject/history changes are replacement reads, not roster merges.

The rail's walkedTree is separate presentation state derived from admitted answers. In-tree selections keep previously read families and member context within the same comparison; families outside the selected answer are tagged kept and counted apart. The walk retains each family's last answer without reading it again or writing it into the current payload. Families sort by identifier before triage order is applied, so arrival order does not choose their display order. A kept family's continuation uses the furthest held roster cursor.

Catalogue/all-invariant selections, All source changes, opening task context after refusal, marker follow/return, opening context, refresh and incompatible comparisons start the tree afresh. Search, ordering, lane destinations, opening files, ordinary page controls, catalogue refresh and failed/refused reads do not independently erase the walk. Selecting a displayed kept family from the catalogue offers a return to that family alone. No claim here makes unreturned members present.

Focus requests are tied to the tree intent that created them and answered only by a later render. Reader-moved focus is respected. At 60rem and below, an in-tree selection reveals its reading area when answered or unavailable; an unavailable reveal moves no focus and preserves the retry's focus request. Refresh requests scroll the selected row after an answer; its failed/refused read drops the request, and retrying a failed refresh repeats refresh behavior. Other retries simply read again.

Page controls request only server-published cursors and the declared collection union, including family_members. A refused cursor shows the owner's refusal plus a first-page route for the requested collection. Reported remainder alone does not invent a next-page action. Historical task comparison is explicitly named and published on the surface root.

### Family, subject, source and record presentation

ReviewWorkspace provides intent-marker scope around WorkspaceBody and holds transient selection/layout/full-file/open-path/worklist state above read switching. Its rail separates compact family/invariant navigation, All/Unexplained/Unknown changes destinations and Worklist. Changed-file destinations mount the comparison-bound ChangeSetViewer over the retained reviewer; its central column swaps content while remaining mounted.

FamilyTree shows compact outline titles and one navigation badge with persisted Changed/All views, ordering and roving focus. Full guarantees, statements, semantic change facts and unchanged supplied siblings belong to FamilyReviewCenter, which also mounts the exported RosterNext control at published side cursors alongside expressions and evidence. SubjectReview owns the exact server-selected subject's statements and evidence. Confirmed no-family, unknown membership and ambiguous revision states remain distinct; family context is not a substitute for the selected subject's answer.

On tree comparisons, ExpressionCards group code and test expressions by path/range, show role/facet and exact side paths/ranges, place authored rationale above the exact-blob excerpt, name missing rationale and not-current states, and offer Full file and All changed files. Changed ranges show real diffs; unchanged ranges appear once and are labelled. Bounded roster wording states loaded members rather than implying the whole family. Dataset comparisons use ReviewExpressions and make no tree/card read. Planning marks use only a leaf-wide worklist whose comparison number matches the displayed tree comparison.

The inherited family excerpt arithmetic has a narrower meaning than Git change inventory: it groups realization claims by path plus recorded source identity. exact_recorded_blob is resolved; recorded_object_unavailable, not_requested and missing path/resolution are unmeasured; other supplied resolution values enter the changed collection. The named historical changed states include recorded_blob_mismatch, path_absent, unsupported_locator and entry_not_blob. Observed identities are attached per side, never added to the grouping key. All carried membership rows contribute, including divergent readings of one revision across sides. Rows retain revision identities so repeated display labels cannot erase different revisions. This resolution classification must not be described as the comparison's measured changed-path set.

SourceExplorer is absent from current source. ChangeSetViewer owns comparison-bound changed-file lists and diff expansion, with held lane facts supplying filters and badges. Its All code list retains published byte-form paths as explicitly nonopenable facts; attribution does not redefine the complete comparison list. Card Full file and the retained dataset expression renderer still use SourceContent at bound code trees, with bounded prefixes, admitted path relations and typed source refusal. Non-text or unreadable SourceContent sides remain named rather than becoming invented empty diff operands.

ReviewRecordPanes holds technical knowledge/source/evidence/submission records behind disclosure. Applicability treatment, true subject, relationships and counts come from the payload; contextual records do not expose a sibling's finding. Preservation/unresolved-question collections remain separate from detection signals. Retired authored-effects envelope tables are not an active list. Assessment absence remains UNASSESSED, not favorable judgment. The submission block names the existing curator authority, reason and next action; its disposition vocabulary is not publication approval.

KnowledgeStatements branches on declared side state: two present sides draw a two-sided diff; one present plus absent draws a named one-sided diff; one present plus binary/unresolved draws available content and explicitly claims no diff; neither present draws the side states alone. Mechanical field rendering distinguishes absent from recorded empty. Word-diff rendering on tree comparisons adds its own prose presentation without weakening these operand distinctions.

ReviewOutcome owns non-payload states and the shared problem block. It states code, detail, offending input or its absence, and next action or its absence. Only a network problem with a retry handler offers retry. An intent-only refusal can offer an explicitly requested task-context/source review; it is not silent substitution. A first refused read has no review payload. With an admitted frame, a later unavailable selection can retain navigation/context while its reading area states the problem and technical records remain unanswered.

### Tree-comparison extensions

Tree comparisons are identified through the review:trees:<n> limitation. Dataset reviews do not acquire these tree-only extensions.

Semantic change-kind facts arrive with family rosters. changeTriage retains their labels, weights, returned-occurrence breakdowns and unknown totals for main-page content without classifying source hunks. Its separate outlineGroups owner constructs compact catalogue navigation, using outline facts plus admitted member facts, one badge per row and Changed/All views. Authored and triage semantic ordering preserve supplied siblings; Changed navigation may hide unchanged rows. Triage remains the browser-local order preference under review.tree-order.v1.

ChangeBadges states the facts and reasons, including change-kind, membership and guarantee unknowns. The inherited accessibility intent is one statement per fact, with the member name as subject and facts in its description; two genuinely distinct unknown facts may share a cause and still need separate lines. changeTraversal follows displayed outline order, focuses and clicks real-change nodes, excludes unknown and unchanged stops, and leaves selection at either end with a polite status. Roster continuation is a main-page control and is neither a traversal stop nor an automatic page read. Status belongs to the rows/order for which it was issued and is discarded when committed rows change. The keymap binds review next/previous change on the reviewer zone only when change facts enable it; text-field handling belongs to that binding owner. Without an available outline, compact catalogue navigation is unbadged in All; dataset expression rendering remains separate from tree-only card reads.

Unexplained changes and Unknown attribution open comparison-bound ChangeSetViewer pages after the family navigation. ReviewSurface supplies one comparison-scoped lane answer to workspace and technical facts and holds it for page filters and per-file badges. Pending, unavailable and unmeasured lane scope remain distinct from zero. LaneFileFocus and its exact-blob windows are absent; card Full file remains a separate SourceContent surface. Worklist opens LeafWorklistView, which displays projected items, currentness, problems, history linkage and gate facts and links changed knowledge files to the comparison viewer. These displays grant no assessment, approval or waiver; closeout authority remains separate. The entry's attribution count remains independent of +N −N, including when intent counts are refused.

Hunk markers consume the same per-file classification, not a second client intersection. Confirmed-unregistered or wholly unreadable files receive file-level notes; other files expose owner-hunk marks with realizations and proofs separately. Family occurrences retain membership state and unknown reason; unknown attribution is not No recorded family. Compact labels apply below 40rem. Placement uses the owner's side line numbers and only hunks/changed lines the pane actually draws.

Marker scope shares in-flight classification acquisition for listed changed paths and keeps successful answers within scope. Non-ready attempts are released for another acquisition; there is no unconditional one-attempt-ever rule. A complete inventory's unlisted path has no marking read, while a partial inventory's unlisted path gets an explicit unlisted state. Full-source marks require the classification's blob pair to match drawn content. Excerpts compare only drawn sides, require differing side blobs, and place only drawn owner hunks. Loading, unavailable and content-mismatch notes are explicit, except card excerpts intentionally stay quiet while classification is loading.

Following a marker selects through ordinary subject navigation. Back restores subject, family selection, worklist selection, opened path, layout and full-file disclosure and clears the tree focus request so the originating marker owns return focus. The return is the visible Back control, not browser-history takeover. Pane-local reopening and the file-viewer gutter own collapsed-run expansion, reveal and bounded passive hold; the inherited hold ends on reader intervention, including wheel, and must clean up. Off-screen marks outside the editor's drawn area are not promised tab stops. The followed target's attribution state lasts until Back.

Tree-only IntentWordDiff presents changed statements, applicability, conditions, exclusions and guarantees as whitespace-preserving passages with removed/added runs or side-by-side text. Byte equality decides unchanged even at the same revision; same-revision changed text is named. Each side reads its own member row or pane/field rows filtered to selected revisions, including that filter on the dataset path. List alignment uses exact-text LCS, removes moved matches before gap pairing and pairs gaps only at equal counts. The word algorithm bounds its matrix at 2,000,000 cells and labels coarse/rewrite presentation; rewrite means a changed-word ratio strictly greater than 0.5 over the longer side. Inline override is unsaved per passage; layout preference uses review.intent-diff.layout.v1 with inline default. Whitespace-only detection removes all whitespace, so joining words by deleting whitespace remains an explicitly accepted historical limitation. Exact texts are disclosed and del/ins have removed/added accessible wording. Dataset reviews receive no word diff, and the layout control appears only where a word-diffed passage is drawn.

One tree-only leaf-wide read feeds subject worklist content and the separate Worklist destination. SubjectKnowledge joins selector identity to canonical record identity through the outline and mounts SubjectWorklistItems only for a tree comparison with a selected subject or family. Missing identity, mismatched comparison, incomplete worklist and read failures remain explicit. LeafWorklistView displays currentness, worklist/history/gate facts and links changed knowledge files to the comparison viewer; the former shared memory-diff panel is not mounted across family, member and unselected centres.

### Knowledge reader

KnowledgeReader owns toolbar, independently scrolling tree/document/aside composition, address-bound read, citation and outline. ReaderToolbar owns repository/tree selection, record lookup, selection/pin notes and named side-read failures. A single selection acquisition is shared with the Records branch. KnowledgeTree adapts shared ExplorerTree, consuming optional hasKnowledge/hasOverview/coverage facts, entry counts, Show every path and count rows. The Records branch includes families, decisions and other records; invariants remain in path views.

PathViews orders prose, invariant states, local/routed families, linked records and references last; directories use bounded summaries and paged subtrees, with without-proof and census views. Empty sections are omitted. TruthView renders record fields, invariant/family details, complete decisions using derived status, both link directions with unreadable links named, and timeline source states. History rows show effect and because: record targets navigate and requirements are named. Incoming history links identify the record the row concerns rather than inventing a history-row page. Reader parts link numbered markers in text nodes only; shared Markdown and referenceMarkers own headings/markers, and ReaderCode reuses FilePane. The inherited backend ownership assigns tree coverage to a code pass plus memory enumeration, with paths delegating tree listing rather than files enumerating directories.

The native role-chat model selects canonical role occupants without buildRailModel or a hosted session rail. FlowTab is removed and supplies no current drawing/prose, live chat or store authority.

## Invariants And Boundaries

The policies above are inherited semantic intent alongside specifically inspected source predicates. They are not newly adopted invariant or family records. Historical candidate lists for L31–L35 remain proposals, not ingestion or present acceptance.

Panels consume canonical stores and authority clients; they must not create private durable session catalogues, conversation indexes or submission ledgers. The structured conversation's browser projection is reconstructable. Native document chat and accepted-session-row consumers have distinct creation contracts; neither should be collapsed into the other's vocabulary. Reliable submission, withdrawal, interaction answers, bus replies and control remain separate channels without paste fallback.

Review remains display/navigation only: it cannot author assessment, waiver, approval or publication. Source inventory is complete within its declared scope regardless of attribution; partial knowledge, unreadable sides, missing totals and unmeasured counts retain their states and reasons. Cached content and kept families are prior reads, not current verification. Bound code trees, memory trees, history context, subject and page identity must remain visible rather than being silently re-resolved.

Keep-alive memoization is an inherited performance boundary: shell rerenders should not rebuild unchanged panels, while their own subscriptions remain live. Naming/splitting conventions use a canonical entry and short responsibility-based siblings. Hand-maintained sample/fixture builders demonstrate mirror-conforming shapes, not producer completeness; generated TypeScript schema and its stale check own the producer contract. Dot naming remains the containing component's responsibility.

The parent delegates detailed child mechanisms and preserves source-lineage ownership. Retired provider presentation, static flow prose and event-label fallback are distinct seams. No broad no-impact assertion or runtime tool availability follows from static source drawings.

## Historical And Verification Limits

This proposal read all original card prose and inspected bounded present-source witnesses at the stated source head. It ran no tests, imported no product entrypoint, exercised no browser or service, and produced no execution/acceptance verdict. Original test populations, mutation outcomes, fixture digest checks, provenance receipts, delivery approvals and rendered measurements are historical claims rather than fresh checks. Their original references remain the parent's preservation responsibility.

ICR-L33's Operations landed-leaf admission and second opened-key collapse store were explicitly withdrawn by the recorded a9a1a41b emergency revert. Their historical 110 landed rows, 19 auto-closed masters, 161-row subtree and count-tooltip behavior are not current claims. The inspected collapse hook has only operations.tasks.collapsed.v1 and toggleCollapsed; LifecycleList has the bare Tasks count. The separate change-set includeLeaves/generation behavior survived. The card's characterization of that emergency commit as lacking a curator pass is inherited history, not reconstructed Git adjudication.

ICR-L44's mixed fixture generations and inaccessible current-route reproduction were recorded as superseded by MIK-L31 recapture, including the six formerly retained old bodies and refreshed case headers. L31/L32/L34/L35 merge, rerun and Todo resolutions remain recorded history; no recapture or digest verification was repeated here. The historical claim that 29 unconverted reads were unchanged before MIK-R37 remains bounded to that rerun, not all current datasets or leaves.

ICR-L36's divergent family rendering was evidenced through a labelled captured familyReview.walkFinal fixture, not discovered live data. Its historical live scan attempted 36 leaves, resolved one leaf serving three families, and received candidate_dataset_absent from the other 35, including ICR-L36 itself. Zero divergence among those three served families says nothing about the 35 unreachable leaves. The named f1/raw/live-truth.json and f1v/raw/vf1-live-scan.json witnesses were not available as examined evidence in this source-only adjudication; preserve their exact historical scope and refusal rather than declaring live divergence absent. The recorded grouping measurements of eight side-counted instances into two keys are fixture/build measurements, not present acceptance. Use each side's reading/resolution wording; the superseded phrase implying every changed address was resolved collides with exact_recorded_blob.

ICR-L25's responsive verification used the review-surface root, not just the inner workspace. Its historical correction measured 51 reviewer descendants past the edge becoming zero while 13 cockpit-chrome elements remained, pane widths 565→294px, user-scrollable count 0→1 and wheel movement 0→800px. Those browser witnesses were not re-examined here. Present source gives ReviewSurface its own vertical scrollport, but source styling alone does not re-establish those measurements or clear the remaining shell-owned chrome. The shell's hidden viewport overflow and internally scrolling panels remain separate composition responsibilities.

The historical amber repair removed copied wash literals through an oklab mix of var(--amber); it did not establish zero computed oklch values, since tokens themselves use oklch. Browser acceptance and keyboard traversal assigned to ICR-R24, and assembled acceptance assigned to ICR-R25/A14/A15, are not supplied by this source adjudication or by mounted fetch-stubbed component evidence. Earlier paging/history/applicability leaves explicitly retained those ownership limits.

L47's late-catalogue remount/focus and file-size findings were recorded as delivered by L48; obsolete line counts are not current architecture. Superseded early entry gates, catalogue-derived entry state, removed catalogue refresh/invalidation controls, three-pane-first composition and whole-file-only expressions must not be presented as active behavior.

Accepted historical notes remain named: whitespace deletion can join words yet classify whitespace-only; a control-placement decision can require an extra bounded diff; separate unknown facts can show the same cause twice; the triage bar could slide under Back for one step. R34's short R4 confirmation was pending in its historical curation text and is not converted here into acceptance. Performance notes, fixture-version updates, debounce teardown changes and test-case counts establish no new delivery certification.

The card historically reported no configured Domain Documentation and no governing cross-repository implementation source. Provider/settings configuration and all production import destinations were not re-audited here; retain these as inherited scope statements, not newly verified whole-repository absence.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/`                          |

| Responsibility | File onboarding |
| --- | --- |
| Review child route — the family tree and the central reading path | [FamilyTree.tsx](review/FamilyTree.tsx.md) · [FamilyReviewCenter.tsx](review/FamilyReviewCenter.tsx.md) |
| Review child route — the workspace and comparison-bound source navigation | [ReviewWorkspace.tsx](review/ReviewWorkspace.tsx.md) · [ChangeSetViewer.tsx](changeset/ChangeSetViewer.tsx.md) |
| Review child route — the leaf's knowledge panel and its notice | [LeafKnowledgeChanges.tsx](review/LeafKnowledgeChanges.tsx.md) · [LeafKnowledgeNotice.test.tsx](review/LeafKnowledgeNotice.test.tsx.md) |
| Review child route — the mounted family composition cases | [ReviewWorkspace.family.test.tsx](review/ReviewWorkspace.family.test.tsx.md) |
| Review child route — the walked tree and the traversal between changes | [walkedTree.ts](review/walkedTree.ts.md) · [changeTraversal.ts](review/changeTraversal.ts.md) |
| Review child route — the captured family bodies those cases are driven with | [familyReview.complete.captured.json](review/familyReview.complete.captured.json.md) · [familyReview.continued.captured.json](review/familyReview.continued.captured.json.md) · [familyReview.emptyRoster.captured.json](review/familyReview.emptyRoster.captured.json.md) · [familyReview.identical.captured.json](review/familyReview.identical.captured.json.md) · [familyReview.oneSided.captured.json](review/familyReview.oneSided.captured.json.md) · [familyReview.truncated.captured.json](review/familyReview.truncated.captured.json.md) · [familyReview.walkFinal.captured.json](review/familyReview.walkFinal.captured.json.md) · [familyReview.capture-provenance.json](review/familyReview.capture-provenance.json.md) |

## Task reader grant control

taskReader renders one Direct execution switch only on a planning subTask's own page, bare giver words on other granted task states, and nothing on grantless states. Master/sprint index rows carry neither a grant control nor a grant mark. The grant hook posts only through the existing adapter and preserves real state on refusal; client affordance/status is not the backend start-evidence gate.

## Evidence
- Marks only from the owner's response, placed on its side lines. [5]
- Every owner hunk a pane draws is placed; the list and the reveal of a return. [6]

- The scope provided around the landed workspace body. [8]
- The unknown-membership state in the rail. [9]
- The explorer's and the details' labels from the lane. [10]
- Unexplained and Unknown rail destinations open comparison-bound change-set pages filtered by the held lane answer. [11]

- The one lane read handed to the workspace and the details. [13]
- The entry's count as its own element. [14]
- The decision, the ratio and rule 1a. [15]
- The tree-comparison scope, the statement area and the changed guarantee. [16]
- Each side's text from its own row, the filtered field rows, and the text-first decision. [17]
- The rail's labels compare bytes on a tree comparison; with MIK-L33's change facts the badges state a text change and the labels do not repeat it. [18]
- On real bodies: a tree review word-diffed, a dataset review as landed, and one guarantee revision never called unchanged. [19]
- The card component. [24]
- Grouping by (path, range) and the bounded-roster scope. [25]
- Cards for a tree comparison, marks only from the same comparison. [26]
- The conforming example on real data. [27]
- The one case: the landed workspace over a converted leaf's trees. [28]
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
- `LifecycleList` owns Operations navigation, row grouping, the selection callback, and hidden-list re-show behavior. [52]
- `DetailPanel` resolves the selected task/lifecycle/series reader target and renders the task document content. [53]
- The lifecycle state vocabulary is the live/terminal partition consumed by the lifecycle panel; the `State`/`Phase` literals moved to `models/lifecycle.py` by 260731-EFA-L9 while the live/terminal sets stay in observer. [54]
- The shared fixture builders seed lifecycle and projection nodes from served fixtures, with required lifecycle fields copied from the served lifecycle. Ranges re-derived: the `lifecycle` occurrences this row names are at `:90-90`, `:243-243` and `:257-257`. [55]
- The typed lifecycle and projection factories are shape-aligned; the served lifecycle binding supplies copied identities without making every content/default value served-derived. [56]
- The hand-kept snapshot payload provides the generated timestamp. [57]
- `Dot` renders its state glyph inside `aria-hidden="true"`. [58]








- **The entry threading the published generation into the viewer target.** [63]
- **The generation state the button carries from a successful master read.** [64]
- **The family column's three parts and the collection mounted as the third, after the member context and before the shared explorer.** [109]
- Family excerpt arithmetic groups recorded addresses and distinguishes changed, resolved and unmeasured realization readings. [110]
- Per-side resolution and observed identities attach to the same recorded-address key. [111]
- **The two hoisted owners the member attribution and the family collection share, so the two readers cannot drift.** [112]
- **The mounted case: the rendered count is the body's distinct excerpt set, every row's collapse count is the body's own group size, and EVERY rendered row's `data-sides` is checked against the sides the body resolves that excerpt on — the page's own both-sides sentence verified row by row against the body, not read from the page.** [113]
- **The new unit lane for the same arithmetic, its own statement of which inputs are constructed, and the pair of cases that state the whole key contract between them (recorded keeps two blobs at one path apart; observed may not, because two sides of one address legitimately see different bytes).** [114]
- The compact control, its brief states and its disclosure (since MIK-L32 with the lane's count beside `+N −N`). [115]
- The entry mounted in place of a change-set button. [116]
- The leaf-scoped facts and re-validation generation. [117]
- A history row's line: its effect, and its because targets as links. [120]
- An incoming link from a history row names the record the row is about. [121]
- The panel, the notice, or nothing. [122]
- Planning marks only from a leaf-wide read of the same comparison. [123]
- The body passes the knowledge panel to the family, member and unselected centres. [124]
- The panel: status line, degraded sides, diff, currentness, worklist. [125]
- The notice for a loading and for an unavailable read; nothing for any other phase. [126]
- The workspace makes the leaf-wide read only for a tree comparison, pinned to the payload's number. [127]
- The notice says that it is computing, as a status region. [128]
- The notice names the failure and its action. [129]
- The cockpit mounts the reviewer for a change-set target that carries a review, with its optional subject and history view. [130]
- The surface's hook composes navigation, read cycle, cache, selection, refresh and retry, and the reading status. [131]
- The workspace is mounted over the answer or the frame, and the records only over an answer. [132]
- The read cycle: the read state bound to its question, and the task-context frame. [133]
- The bounded cache of one mounted surface and its generation test. [134]
- The one failure and refusal block, with the retry control of a network failure. [135]
- The record panes behind the "Technical details" disclosure. [136]
- The reading-area column is one node whose content alone is swapped. [137]
- The weights of the change kinds and the two orders, which only reorder. [138]
- The order preference and its storage key. [139]


- A step focuses and clicks the stop, and the chords are bound on the reviewer's zone only when the tree has change facts. [141]
- The end message is given out only beside the rows it was said for and is dropped in the commit that shows other rows. [142]
- The tree draws the walked families, hands the traversal the rows it shows, and mounts the triage bar only with change facts. [143]
- One step of the walk: an in-tree selection keeps, any other selection and another comparison replace. [144]
- The workspace advances the walk, marks the tree and the reading area apart, and selects rows of the walked tree. [145]
- Every selection numbers the tree intent, keeping only with `keepTree`. [146]
- A refresh starts the tree afresh and asks only for a scroll; the retry of a failed refresh is the refresh again. [147]
- The catalogue lists a row for every family the tree shows while one is kept. [148]
- The kept tag and the scope line that counts kept families apart. [149]
- The focus request is answered only by a render made after it; a pending or unavailable read is handled without spending it. [150]
- The page controls: a next page only for a published cursor, and the refusal of a requested page. [151]
- The mounted case of the key walk on real data. [152]
- The mounted cases of the reviewer between a selection and its answer. [153]
- The notice draws nothing for a dataset review. [154]
- Current ownership/control, without execution or runtime tool exposure inferred. [155] [156] [159]



- The reviewer adds a compact recorded-effect badge to eligible changed outline rows while keeping navigation one line. [160]

- The compact navigation keeps its own row facts and optional recorded-label badge; semantic record content lives in the main page. [161]

- Selected family and invariant centers join recorded steps to their own identities and preserve independent guarantee/statement/source/evidence content. [162]

- The recorded-history block owns full step fields, strict states and native keyboard explanations, not a computed verdict. [163]

- The intent entry always opens task-context review; liveness selects the live or recorded target, while summary state labels rather than gates the button. [59]
- The subject-catalogue hook serves reviewer navigation, not task-entry admission; the task entry reads a summary and no catalogue. [60]
- The shared leaf-liveness predicate chooses live versus recorded entry context; it is not a catalogue-subject admission gate. [61]
- The catalogue client and subject shape serve reviewer subject navigation; task-entry summary and clickability are separate. [62]
- Traversal selects displayed tree nodes with real-change primary facts and reports its ends; partial-roster continuation buttons are not traversal stops. [140]
- Four product destinations, Chats default and retained Operations/File/Knowledge composition [164]
- Artifact reader includes task reports and whole decision logs [165]
- Decision preview excludes product records and limits authored entries to five [166]
- Superseded successful whole-task reads have a guarded unshown-cache exception [167]
- Workspace can use the admitted frame while records receive only shown answers; comparison navigation retains the reviewer underneath [168]
- Review root owns its vertical scrollport and keyboard zone [169]
- Continuation admission checks identity and cursor; sparse claims preserve earlier content [170]
- Walked families preserve prior reads but reset across incompatible comparison/selection [171]
- Semantic triage counts returned facts, states unknown totals and keeps scoped weight at least unknown [172]
- Traversal selects shown real changes, excludes unknown/unchanged rows and has no continuation stop [173]
- Classification cache shares successful acquisition but releases non-ready attempts [174]
- Excerpt marker loading intentionally renders no note [175]
- Marker follow/return restores subject, family, worklist and pane state through ordinary navigation [176]
- Word-diff whitespace predicate and strict rewrite threshold [177]
- Family expression keys use recorded identity; observed readings stay per side [178]
- Planning marks require matching comparison; subject worklist rendering joins canonical identity and states unavailable reads [179]
- Statement state decides diff/content branches [180]
- Network-only retry and intent-only source alternative remain explicit [181]
- The comparison page's All code list identifies byte-form inventory paths as explicitly nonopenable [182]
- Current intent entry uses liveness to choose recorded target rather than hide entry [183]
- Master change-set read includes leaves and carries published generation [184]
- Collapse hook has one stored key set and toggle API [185]
- Knowledge reads bind to address; reader shares records and responsive citation navigation [186]

- Family-center order shares the outline ranking while retaining the semantic revision roster. [164]
- Exact currentness mark words coexist with an open supplied-reason sibling. [165]
- Non-authored field rows distinguish absent and recorded-empty values. [166]

- The task list head owns the attention bell and the actual row renderer. [190]
- The bounded Popover/Dialog retains source-scoped queue actions. [191]

- The remaining Operations rowState and treeRows modules own task-row facts and hierarchy; the removed chat activity indicator supplies no current state owner. [192]
