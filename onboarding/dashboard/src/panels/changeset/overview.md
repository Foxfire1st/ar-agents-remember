# dashboard/src/panels/changeset/ — Change-Set Viewer Overview

## Governing Overview

[dashboard/src/panels overview](../overview.md)

## Purpose

`changeset/` is the Change-Set Viewer: a task-scoped screen for inspecting changed code and onboarding files, with up to three columns for the changed-file lists, the selected file's diff, and its code↔sidecar partner. It consumes the read-only change-set API at `GET /api/changeset/{task,file-diff,master}` and reuses the File Viewer's read-only editor, theme, language extensions and persisted view flags, plus the shared Markdown renderer.

The target selects an enclosure scope, a series master net, a leaf's committed or working range, or a numbered recorded review comparison. The cockpit opens the screen as a full-bleed takeover from change-set controls, hides its underlying body while the takeover is open, and restores that body when the reader goes back.

This route also declares the target variant for Intent Review. A target carrying `review` is dispatched to the reviewer instead of mounting the Change-Set Viewer. The reviewer belongs to `panels/review/`; the task entry belongs to `panels/detail-panel/`.

## Hot Path Summary

A change-set control opens the cockpit takeover → the viewer reads the selected range and lists changed code/onboarding files with status and counters → selecting a row reads its before/after content into a read-only split or inline diff → the row's partner affordance can open a third column. Per-column toggles select collapsed diff, full-file diff, plain after-content or rendered Markdown. A master view also lists per-leaf counters and can retarget the same takeover to a leaf. Back closes the takeover and reveals the underlying cockpit view.

## Construction

### Targets, requests and generations

`ChangeSetTarget` carries the repository and optional scope, master, leaf, mode, master-generation pins and comparison number. Request selection follows comparison → leaf → master → scope. Comparison reads use recorded code_base→code_candidate trees; memory uses converted_base when supplied, otherwise memory_base, through memory_candidate, restricted to knowledge/ and onboarding/. The answer uses the task change-set shape with mode comparison. A leaf is qualified by its master and defaults to committed mode in the viewer's requests. An enclosure scope reads base→worktree; a committed leaf reads its recorded base→landed endpoint; a working leaf reads worktree HEAD→worktree. A master reads the net between its declared base and selected integrated result, or the endpoints supplied by explicit pins.

The list request for a master asks for `includeLeaves: true`; the master counters control does the same. The client still supports omitting the breakdown for a caller that requests only the net. `seriesLeaves` returns no breakdown unless this is a series view and the response has a `leaves` field.

A master response publishes code and memory endpoint pairs, a deterministic digest and currentness. `boundSeriesGeneration` prefers the response's generation over the entry's pins and passes it into every master file expansion. `SeriesGenerationTag` displays the short digest, currentness and integrated scope when the response supplies a generation. The entry control carries the published endpoint pins into the viewer target. This binds file expansion to the listed endpoints after the integration branch advances; it does not establish that a response's generation is chronologically newer than the entry's.

The header labels a working leaf as `working · <leaf> · uncommitted`, a committed leaf as `committed · <leaf>`, and a master as a series net. It renders the response's code and memory counters beside the back control.

### File lists, attribution and read states

`ChangeSetViewer` owns component state for the list, its initial read error, the active file and the two file-diff responses. The first column contains changed code and onboarding lists. Rows show path, Git status and insertion/deletion counts; the active row uses a 20% amber wash and hover uses 12%. Code files with a sidecar offer a partner action. An onboarding path must start with `onboarding/` and end with `.md` to enter partner mapping. After stripping those delimiters, names ending in `/overview`, `/entities` or `.index` are excluded. The root `onboarding/overview.md` becomes bare `overview`, passes this predicate and can expose a code-partner affordance; the predicate does not establish that the target exists or that its read succeeds.

The selected file occupies the second column through `ChangeSetPane`. A successfully read partner adds the third column. The workspace uses resizable panels. With a list response but no selected diff, zero files across both lists produce the named empty pane; otherwise it asks the reader to select a changed file. That prompt uses the siege-tank boomerang clip at opacity 0.18 when the shared backdrop's effects gate permits it.

`LeafBreakdown` renders a `by leaf (N)` rail beneath the changed-file lists, with each leaf's state and both halves' file/insertion/deletion counts. Its button opens working mode only for a row whose state is `working`; other states select committed mode. The cockpit supplies the callback, so selecting a leaf retargets the same takeover. Without that callback the leaf buttons are disabled.

The standing intent of the rail is to make the master net attributable by leaf. The implementation supplies per-leaf counters alongside the net, but computes those counters against each leaf's own base and current worktree or recorded commit. They are not a decomposition whose sum is guaranteed to equal the integrated net. A live leaf's breakdown counters are base→worktree, whereas clicking its working row opens HEAD→worktree. The source and the attribution intent therefore describe different ranges; this overview does not certify them as equivalent.

The initial list read can restore a matching cached answer through `peekChangeSet`, then uses the shared `loadChangeSet` request owner. A missing answer shows an explicit loading placeholder; a rejection is retained as a `ReviewFailure`. `ChangeSetRefusal` renders its code, optional HTTP status, detail, offending input and next action when supplied. The client decodes non-success response bodies and carries the route's refusal in `ReviewTransportError`, using the shared failure vocabulary rather than a separate viewer decoder.

The counters control in `changeSetBar.tsx` distinguishes loading, unrecorded, measured-empty and failed/refused reads. It renders a brief failure state in the control and the owner's code and reason in a disclosure beside it. The existing rendering case inspects that disclosure and clicks the control to assert the target it opens; this describes the test source, not an executed test result.

A working leaf refresh starts its timer without requiring an initial successful list, unless a recorded comparison was selected. Each refresh starts list and active-file requests together, waits for both to settle and independently applies each result; success replaces its value and clears its problem, while rejection clears its value and stores the named failure. The next timer is scheduled after settlement at 2500 milliseconds, and teardown cancels it. This refresh concerns the active main diff, not the partner column. `ChangeSetWorkspace` displays list failures; `ChangeSetMainPane` displays the independent selected-diff failure. A failed initial working list can therefore recover through the normal timer rather than becoming a permanent loading gate.

The server explicitly returns an unrecorded state when a leaf's committed code endpoint has not been recorded. The counters control displays that state. The viewer's main-pane decision checks file-list lengths, without reading `state` or `stateDetail`; consequently an unrecorded response with empty lists reaches its measured-empty wording. The intended distinction between an unrecorded range and a measured empty range remains visible here as an implementation discrepancy.

The changed-file rail uses shared `changeset` left-sidebar visibility and a header toggle outside the rail. Hidden panel and handle props keep the rail mounted while removing it from layout and reachability; the same state controls the stacked list on narrow comparison layouts. This visibility state is separate from each diff column's persisted presentation flags.

### Diff columns and shared editor construction

`ChangeSetPane` maps its persisted flags to three source views: collapsed change-set diff; full-file diff with highlighting; and full-file with highlighting off, which uses `FilePane` on the after-content. Split⇄inline selects the diff layout. Each column supplies its own `keyPrefix`, so view flags persist independently across file switches and reloads. Markdown-language files also offer a rendered toggle that uses the shared `Markdown` component in a scrollable container; it renders after-content, or before-content when the after text is empty.

`DiffPane` builds a read-only CodeMirror merge pane imperatively in an effect. `splitView` creates a `MergeView` with before and after editors; `inlineView` creates a single after editor with `unifiedMergeView`. Both use the shared theme and lazy language extension, read-only/non-editable state and line wrapping, with no revert or accept/reject controls. The asynchronous language resolution has a disposed guard, and teardown destroys the constructed view.

The normal host styles draw changed text as dark muted green addition rectangles and red deletion rectangles. `firstLine` supplies each side's file-relative numbering through `numberedFrom`; absent values start at line 1. The fitted review-page host instead grows to its content, leaves its editor/merge scrollers overflow-visible and has no internal maximum-height box. ChangedExcerpt passes file line origins, fit, marks and the page's collapse setting. LaneFileFocus and its lane windows remain retired. ChangeSetPane remains the comparison viewer's unmarked diff owner.

The optional marks prop connects DiffPane to useMarkedPane. Each builder places its side's marks gutter first and reports its drawn editors; teardown reports drawn(null). Non-fitted panes rebuild on placement changes, while fitted review panes reconfigure mark-gutter compartments in place. Expression-card excerpts pass marks; ChangeSetPane remains unmarked. The former card Full file path through SourceContent, lane windows and SourceExplorer are retired owners.

### Review entry and takeover dispatch

The presence of `ChangeSetTarget.review` selects the review variant; `{}` is the task-context entry, and optional selector kind/id fields can name a recorded subject. The optional `historical` field addresses the leaf's recorded comparison. These are review dispatch fields, rather than additional change-set modes.

`DocChangeSetBar` renders a series change-set control for a master. For a leaf it renders the committed control and `LeafEntries`: a working control when the leaf is live, plus `IntentReviewEntry` regardless of that liveness. `DocChangeSetBar` derives liveness with `entry.worktrees.some(worktree => worktree.codeWorktreeExists || worktree.memoryWorktreeExists)`. That result gates working reads and selects which review record the entry addresses; it does not gate the review entry on a subject or a catalogue answer.

`IntentReviewEntry` opens the repository/master/leaf task context with `review: {}` for a live leaf or `review: { historical: true }` otherwise. It uses its own comparison-summary read, rather than a `ChangeSetButton` or change-set line counters, and does not read the subject catalogue. The reviewer reads the catalogue through `useReviewNavigation` and `useReviewCatalogue`, whose request uses `intentReviewEntries`. The target carries identities rather than a filesystem path.

Cockpit dispatch maps the target history flag and optional subject to ReviewSurface. Reviewer destinations then mount the existing ChangeSetViewer on a recorded comparison with held lane/inventory and only a matching worklist; same-generation late delivery may enrich that captured context, but a different generation never silently retargets it. The reviewer stays mounted underneath. Closing removes the overlay and schedules opener focus return, without itself issuing a new review request; independent live input is not prohibited by that statement.

## Invariants And Boundaries

- Change-set reads use the GET API and do not mutate the dashboard store; the viewer owns its display state. Persisted view flags do write their localStorage preferences.
- The scope, master and leaf selectors retain distinct ranges. A master net and a committed leaf can be read without a live enclosure; working leaf reads require a live code worktree. Recorded committed endpoints are resolved from the contract, including its integrated endpoint when the closeout endpoint is absent, rather than substituting worktree HEAD.
- Listed master pins are threaded into file reads. Currentness labels the listed range relative to the integrated tips; a superseded generation remains the requested generation.
- Initial loading, list refusal and no-file selection have separate render paths. The standing distinction between unrecorded and measured-empty ranges is implemented in the counters control but is not enforced by the viewer's file-count-only empty-pane branch.
- The master net is a single endpoint diff. Its adjacent leaf summaries and working-leaf navigation must not be described as equal measurements: the inspected implementation computes them over different ranges.
- Panda CSS supplies this route's styles and React Aria `ToggleButton` supplies its view toggles. The standing no-CSS-animation / GSAP-or-Motion policy remains intent; the shared theme also states it, but this scoped source inspection does not establish its governing lifecycle authority.
- The viewer is a cockpit takeover, not a mode-bar tab. Back clears the takeover; a mode switch or node open also clears it. Closing it reveals the underlying cockpit body, which is not necessarily an Operations view if another view opened the takeover.
- Review dispatch belongs to the cockpit, review display and catalogue selection to `panels/review/`, and the task entry to `panels/detail-panel/`. The review dispatch field chooses no filesystem candidate path. Reviewer file destinations separately use the numbered recorded-comparison range; its filters and per-row badges consume held server lane facts rather than reclassifying hunks.

## Non-Operative Metadata

The preserved route metadata below is descriptive metadata, outside the operative promises above. Historical slice labels do not establish a current lifecycle status or executed qualification.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/panels/changeset/`                |

## Comparison filters and delivered witnesses

ReviewFilters and reviewChangeSet own explicit All/unexplained/unknown filtering over the held answer, including unavailable and zero states; they do not classify hunks again. The single row-badge map can combine delivered lane, inventory and worklist witnesses without guessing a governing row from a reason. Main-file request sequencing does not imply the same cancellation/sequence guarantee for partner or lazy requests. Working polling concerns the list and active main diff, schedules after their settlement, and does not refresh the partner column. Source/static regression inspection is not a browser/server execution grade.

## Source-content transition and retained historical references

The earlier account below belongs to the pre-A4-F5 fitted-pane and Full file implementation. Its former 32rem box, hard-coded collapse=false call and SourceContent consumer were replaced by the current page excerpts and same-editor mark update path.

> The shared host styles draw changed text as dark muted green addition rectangles and red deletion rectangles rather than thin underlines. `firstLine` supplies each side's file-relative numbering through `numberedFrom`; absent values start at line 1. `fit` selects a content-sized host whose split merge view has a 32rem maximum height. The reviewer's `ChangedExcerpt` passes file line origins, `fit` and `collapse={false}`. LaneFileFocus and its lane windows are absent from current source. `ChangeSetPane` remains the comparison viewer's unmarked diff owner.

> The optional `marks` prop connects `DiffPane` to `useMarkedPane`. Each builder places its side's marks gutter first, and the shared hook supplies no gutter extension for an unmarked side. The builders call `drawn` once their editors exist; the hook expands collapsed runs holding marks. Teardown calls `drawn(null)`, placement participates in the effect dependencies, and the portals render after the host. Card Full file through `SourceContent` and expression-card excerpts pass marks; `ChangeSetPane` does not. Lane windows and SourceExplorer are retired owners.

The following reference captions describe the prior source epoch. They are preserved as history; their reference numbers below are inert and do not claim current frontend consumers.

> - Card Full file and expression excerpts pass marks; the former lane-window owner is retired. (historical reference 34)

## Evidence

- The master request now asks for the per-leaf breakdown; presence of `leaves` is the discriminant. 

- The shell that hosts the takeover + restores the rails. 

- The detail panel button + counters that open this screen. 

- **The generation the open series view is bound to, and the caption that renders it.** 

- **The entry button threading the published generation into the viewer target.**

- Comparison requests are built for the recorded trees

- No-mark gutters, collapsed-run expansion and marked-pane construction.

- The net and leaf summaries are computed separately, over different ranges; leaf working reads require a live worktree, and committed lists publish unrecorded state.

- The existing refusal case checks the reason and clicks the control; no execution is asserted.

- Comparison takes precedence in list and file requests, and the held-lane filter does not classify hunks.

- Target-addressed list loads share the current request/cache owner, and an available cached answer can be restored at selection. 

- Working refresh does not require hasData, excludes comparisons and handles list/diff fulfillment and failure independently before scheduling its next timer. 

- The existing viewer composes delegated filters and one badge map from held facts; same-generation comparison context can accept late matching worklist/lane data without reopening another comparison. 

Anchor: `useReviewCatalogue` `intentReviewEntries` 

Anchor: `useReviewCatalogue` `intentReviewEntries` 

- Retired at the fifth freeze d59c3493: dashboard/src/panels/detail-panel/changeSetBar.tsx:112-125 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361; dashboard/src/panels/changeset/ChangeSetViewer.tsx:255-275 - the region it cited is not in the file at the candidate and no re-point was possible; dashboard/src/panels/detail-panel/changeSetBar.test.tsx:507-552 - the region it cited is not in the file at the candidate and no re-point was possible; dashboard/src/panels/changeset/ChangeSetViewer.tsx:253-295 - the region it cited is not in the file at the candidate and no re-point was possible; dashboard/src/panels/changeset/reviewChangeSet.ts:24-75 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; dashboard/src/panels/changeset/ChangeSetViewer.tsx::seriesLeaves - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 2e11db883f77bb1bf2827ae537b5d1d564e020b3; dashboard/src/cockpit/Cockpit.tsx::CockpitShell - the bytes it recorded now occur 13 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/detail-panel/changeSetBar.tsx::ChangeSetButton - the bytes it recorded now occur 10 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/changeset/ChangeSetViewer.tsx::SeriesGenerationTag - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/changeset/ChangeSetViewer.tsx::boundSeriesGeneration - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit f141d164265e926be9249acf6ae680ccf9ffae61; dashboard/src/panels/changeset/ChangeSetViewer.tsx::useChangesetLoad - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/changeset/ChangeSetViewer.tsx::applyWorkingRead - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit c861abfeff33c9ef8f1ca066604c8f971b613361; dashboard/src/panels/changeset/ChangeSetViewer.tsx::useWorkingChangesetPoll - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; dashboard/src/panels/review/ReviewSurface.tsx::useHeldPageLane - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The master request now asks for the per-leaf breakdown; presence of `leaves` is the discriminant.

## Retirements

- Retired at the fifth freeze d59c3493: dashboard/src/panels/file-viewer/markGutter.tsx:292-379 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit d3a22213ad3124603b0210afb7e3d049c5589b82. Retired means the anchor no longer stands, not that the cited subject was deleted.

- Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/changeset.py:147-213 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit ee7dabb917b4d8d205da097032c3de3cced909e3; mcp/src/agents_remember/serving/changeset.py:591-634 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit f141d164265e926be9249acf6ae680ccf9ffae61. Retired means the anchor no longer stands, not that the cited subject was deleted.

- The optional marks and the marked pane. [1]

- The two extracted view builders, each with its marks gutter. [2]

- The optional first lines and the content-sized host. [3]

- The card that passes them. [4]

- The rendered rail and its per-leaf counters, and the click that opens one leaf's own range. [6]

- The named refusal and the named measured-empty pane, i.e. the two states that are not a missing selection. [7]

- The cockpit re-target that keeps the opened leaf inside this route's takeover. [8]

- The L3 read-only change-set API this screen consumes. [9]

- The same-origin client wrapping that API. [10]

- The reused read-only CodeMirror pane + theme + lang map. [13]

- The markdown renderer the sidecar column + rendered-markdown toggle reuse. [14]

- The siege-tank empty-state backdrop shown until a file is picked. [15]

- The target variant this route's type gained. [16]

- The declaration's own statement that no change-set request comes from a review, and that an empty object on the field is the task-context entry rather than a missing selector. [17]

- **The reviewer entry: offered for every leaf beside the working/committed actions (the recorded comparison for a closed leaf, `ICR-R12`).** [18]

- **The identity the entry carries instead of a filesystem path: the task context only — `review: {}` for every leaf, live or closed, so a landed leaf opens the review on the pair it delivered rather than its own numbered record.** [19]

- **The read that supplies the subject now belongs to the reviewer, taking the comparison's task context and nothing else.** [20]

- **The entry’s code-or-memory worktree existence flags select the working control and live-versus-recorded review context.** [21]

- **The target type whose review field may carry no selector, with presence as the marker and an empty object as the task context.** [24]

- The detail-panel entry that hands the viewer this leaf's targets: the committed change set and the Intent review entry, whose target carries the task context and no subject. [25]

- The surface that receives it and asks for the task's own review. [26]

- One file's diff reads on the comparison's trees [28]

- Lane filters apply over the held lane facts [29]

- Persisted flags use component state and localStorage. [30]

- Shared numbering, theme and language construction. [31]

Retired at the fifth freeze d59c3493: dashboard/src/panels/file-viewer/markGutter.tsx:292-379 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit d3a22213ad3124603b0210afb7e3d049c5589b82. Retired means the anchor no longer stands, not that the cited subject was deleted [32]

- Diff highlight styling, fitting and effect teardown. [33]

Retired at the fifth freeze d59c3493: mcp/src/agents_remember/serving/changeset.py:147-213 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit ee7dabb917b4d8d205da097032c3de3cced909e3; mcp/src/agents_remember/serving/changeset.py:591-634 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit f141d164265e926be9249acf6ae680ccf9ffae61. Retired means the anchor no longer stands, not that the cited subject was deleted [35]

- Recorded leaf endpoints use closeout cells or their recorded integrated equivalents. [36]

- Master generation digest, selection and currentness use declared or pinned endpoint pairs. [37]

- The counters control distinguishes loading, unrecorded, unmeasured, empty and failure and discloses the reason. [38]

- Leaf entry construction gates working reads, not Intent Review. [40]

- Review dispatch, back, mode switches and node opens clear or replace the cockpit takeover. [41]

- The reviewer catalogue remains task-bound; navigation threads recorded history and current generation. [42]

- Recorded comparison ranges retain exact code/memory operands and named unavailable-tree states. [44]

- A list problem and selected-file problem have distinct display owners rather than silently leaving a stale successful pane. [47]

- The partner predicate excludes slash-suffixed overview/entities and .index bases, but root onboarding/overview.md strips to bare overview and can produce an affordance. Target existence/read success is not established; this predicate already exists at both actual BASE operands. [49]

- Current expression excerpts pass marks, file origins and the page collapse setting to a content-sized DiffPane; fitted mark updates reconfigure existing gutters, and card Full file is retired. [34]

- The changed-file rail remains mounted and shares one visibility state across wide and narrow workspace orientation. [50]

- The header toggle owns changeset-left visibility outside the changed-file rail. [51]

Anchor: `CockpitShell` [11]

Anchor: `ChangeSetButton` [12]

Anchor: `boundSeriesGeneration` `SeriesGenerationTag` [22]

Anchor: `peekChangeSet` `loadChangeSet` `useChangesetLoad` [45]

- The existing viewer composes delegated filters and one badge map from held facts; same-generation comparison context can accept late matching worklist/lane data without reopening another comparison. [48]

Retired at the fifth freeze d59c3493: dashboard/src/panels/changeset/ChangeSetViewer.tsx:222-222 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted. [5]

Retired at the fifth freeze d59c3493: dashboard/src/panels/changeset/ChangeSetViewer.tsx:222-222 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted [5]
