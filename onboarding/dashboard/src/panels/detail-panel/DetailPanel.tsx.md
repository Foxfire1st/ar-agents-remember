# dashboard/src/panels/detail-panel/DetailPanel.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Canonical memoized Operations detail entry over the single served TaskEntry selection. It composes local selection/body state and the task page without creating a competing state, membership or runtime authority.

## Code Commentary

### Composition and selection

The original monolith was split by responsibility: state.ts owns selection/body state, model.ts pure
derivation, taskDocPanels.tsx entry composition, worktreeSpine.tsx bound code/memory checkout lanes and taskReader.tsx form
composition. The fixed-page head, blocks, own views, index groups and styles have separate owners
(docHead, taskBlocks, skeletons, docViews, task-groups, pageParts/pageStyles). The shared Panel remains
unchanged. A selected document has exactly one in-page ID/title; sticky Panel chrome keeps Back/parent
navigation, not a duplicate title or ProgressFill header.

Only a taskdoc-prefixed opaque entry key dispatches through TaskDocumentPanel. Addressless or unauthored entries are not converted into synthetic series documents. Entry summary supplies reader form/content; server TaskEntry supplies stage, activity, membership and counts.



### Durable hierarchy, progress and navigation

Entry-key navigation preserves full-list positions. Served children/stages drive groups; unresolved or addressless targets remain inert rather than inventing slug or lifecycle fallbacks. Completed table ordering and discarded-before-start audit retain separate presentation responsibilities.

Progress facts use projected stepsDone/stepsTotal, never a second count of a visible slice. Task steps
now have one table with marks/counts and their body content; index rows use StepMarks/ProgressBar as
appropriate. The standalone grammar ProgressFill still exists for other consumers but is not a
second task-page header. Structured step/code IDs compose with titles at render time rather than
being inserted into stored title strings. No aggregate task token figure is rendered.

### Body first and read-only artifacts

useDetailPanelState resolves the visible document and useTaskDocumentBody fetches its full body by
stable path/revision. Available summary content remains visible while loading, with the explicit
loading notice; unavailable full content retains the summary/failure notice. Current summary identity,
status, progress, step state and review aggregates remain authoritative. A matching revision can
restore longer marked previews/full collections without a stale body replacing current facts.
Ancillary Notes, references/reports and reader/spine change-set counters mount after body loading
settles, for both available and unavailable outcomes; their eager effects must not occupy its first
request slot. Requirement links retain the shared repository/task-qualified provider on every form.

The shared kind-tagged TaskArtifactReaderTarget carries notes, requirement packets and recorded task
reports through onOpenNotes into the existing reader takeover. The page reads no note tree/content:
its single Notes line uses the root count. Task reports use the path inside the task root, not the
physical projected filesystem path. Document-local own-view/expansion state resets on a different
docIdentity and persists on a same-document refresh; own-view Back restores its captured scroll owner.

ChangeSetBar retains the master net with includeLeaves:true and its own leaf attribution, not a fake
zero when breakdown is absent. Leaf working and single Intent review controls retain their own owners,
brief states/disclosures and task-context targets. No Lifecycle GateResponder or task-local gate response box is mounted. Native document chat retains its own separately owned conversation and permission boundaries.
Spine lanes remain read-only rendering of entry-bound code/memory checkout presence and cleanup facts, not command authority.
The no-selection Panel retains EmptyStateBackdrop and its existing effects/motion gating. Memoization
skips unchanged persistent selections but allows actual store/selection changes.

## Boundaries

Read-only navigation, hydration and projection display confer no authoring, review, landing or
lifecycle authority. Task JSON/qualified references remain the structural source of truth; the
reader never steals a leaf's parent content. The fixed form order deliberately supersedes the old
ad-hoc body/duplicate-header composition while preserving requirement links, Notes transport,
discard-before-start audit, progress ownership, durable gates and runtime spine separation.

## Evidence

### Repo-Internal References

- Component regressions pin body-first request ordering, complete field rendering, fallback visibility, one implementation-step copy, and revision caching. [3]
- `state.ts` derives a qualified leaf key from the selected non-master entry and publishes it with the canonical document reference through `onViewTask`; the task reader no longer derives or places a leaf key on its wrapper. [15]
- The shared qualified key is repo/master/leaf-id and requires all three parts. [16]


- Task progress forwards the projected done and total counts. [28]



- Task step progress/count is placed in the Steps table block, not a duplicate ProgressFill page header. [31]

- ProgressFill is the shared progress display primitive. [32]

- Full-index one-based positions stay stable across groups without generating visible task numbers. [33]




- Each index row uses its full-index position for test identity and the resolved qualified target for navigation. [35]


- The fixed page uses StepsBlock for its table/count; standalone ProgressFill remains a separate grammar primitive, not mounted as a duplicate task-page header. [37]


- Shared block text remains Markdown and the relocated decision preview retains newest-authored semantics. [44]

- The shared empty-state backdrop the no-selection state renders. [46]
