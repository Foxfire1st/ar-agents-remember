# dashboard/src/panels/lifecycle-list/LifecycleList.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

The Operations task-navigation column: a controlled React Aria ListBox with BY REPO tree and BY PHASE flat grouping, one-line rows, and the attention bell in its head. The approved presentation replaces rank chevrons, tier frames and separate gate/chat/pickup chips with one state mark, one task-state word and a progress figure, with cached major-step marks for non-master document rows; full facts remain in each row's hover. It neither authors task state nor widens row admission.

## Code Commentary

### Admission and durable identity

operationRows admits root/master documents, exact active-enclosure-matched leaves, folder-keyed series fallbacks when no master is projected, and runtime rows backed by a live-worktree enclosure. Physical code or memory worktree existence is the leaf admission fact, never cleanup state. Enclosure joins use exact case-insensitive document stem/id and taskRoot, not display numbering or shared master lifecycle. One enclosure yields one task entry: a bound lifecycle enriches that document row rather than adding a duplicate. When a document binding is absent, the contract lifecycleId and most-recent matching lifecycle anchor provide deterministic fallback. Doc-less runtime rows retain their taskRoot/series parent.

Root/master runtime binding is a distinct join: runtimeForDoc first looks up an explicit doc.lifecycleId directly and returns that lookup, even if it is missing. Only without that id does it look for a sibling enclosure at the document folder whose lifecycleId equals its taskId or taskName. This root branch is not the exact leafId/stem admission join or the most-recent enclosure-anchor fallback used to enrich leaf rows.

Root task documents remain readable without a worktree; loose/planning leaf documents do not become sidebar rows merely because the observer projects them. Reopened leaves return only when their worktrees exist again. Archived/deleted documents disappear with their projection. Keep this admission separate from completed-row folding: a fold contains already admitted rows, not every landed leaf of a master.

### Hierarchy, ordering and collapse

Orchestration documents derive the command tier from their nonempty orchestrates list; commanded masters derive their parent through taskHierarchy. Tier data and hierarchy remain, but tier chevrons, corner frames and ghost washes do not. Indentation is padding inside the bounded row. BY REPO delegates to treeItems: subtree need first, then creation/fallback order, completed/abandoned subtrees behind a scoped in-place count. Cycles cannot drop or duplicate input rows. BY PHASE is flat and creation-ordered within the phase/status groups; it does not use tree disclosures or folds.

The existing collapsed-parent set stays persisted by useCollapsedTaskGroups. Open completed folds are local presentation state and start closed. treeItems derives ancestor holding and held completed folds; heldFoldKeys collects only already-held fold keys from the emitted groups, never parent keys. RowCaret separately passes each non-flat parent row's collapsed/held facts to TaskGroupDisclosure. A selected descendant holds its ancestor chain and containing fold open without rewriting the reader's persisted choices; held parents/folds cannot be collapsed over that descendant. Choosing the parent itself does not force it open. Fold keys are not task-document identities, and activating a fold toggles it rather than choosing a document. Heading and group counts count admitted rows, including rows currently hidden by presentation folds.

### State, signals and secondary facts

rowState chooses the document or reporting lifecycle. An inferred lifecycle without lastEventTs has not reported; the document speaks, or waiting when no document exists. Reporting lifecycle states retain their own mark/word and eligible local age; completed/abandoned use document-style status. rowWord says only that task state: it does not prioritize gates, inbox, chat input or activity. Remaining task/progress/lifecycle/worktree/repository facts stay in the actual hover without removed gate/chat/pickup fields.

The compact progress figure is done/total. Abandoned tasks remain outside the denominator, and abandoned/discarded counts remain in the hover rather than masquerading as completion. No session-catalog/chat activity, gate.kind or pickup acknowledgment fact is selected or rendered by this owner. The progress figure and current hover are not evidence of any of those removed signals. Non-master document rows carry doc.steps to StepMarks beside the served done/total figure; nested steps do not add marks. A done parent stays done; a started or done child promotes an unfinished parent to current. Up to twelve marks can expose cached pointer details via StepDot; larger populations use the aggregate bar. Masters, series fallbacks and runtime-only rows carry no steps payload for that display. docProgress now owns document numeric-progress mapping; none of these presentation additions admit landed leaves.

There is no PickupDismiss or operator-inbox dismissal interaction in LifecycleList. The mark wrapper remains named inside ListBoxItem option semantics; accessibility must not depend on a removed action. Row selection/hover keep their retained owner without restoring press suppression for a deleted button.

### Selection and keyboard reach

Selection keys remain typed taskdoc:, series: and lifecycle:. A lifecycle chosen by an attention entry stays the shell's lifecycle selection; its carrying task row is only marked, held open and focused/scrolled once for that bell request. Clicking that row chooses its document. A request with no carrying row is consumed without motion, including when a row arrives later; selection and row revelation are different facts.

Typeahead uses the displayed short id plus title for numbered master children, and preserves title-prefix matching for sprint/master/standalone labels. A standalone task can now display a separate id cell while still matching its historical title prefix. Unmodified right/left arrows open/close a focused parent only; task and fold rows receive no such tree action, and browser/system modifiers are untouched. Existing up/down, Enter and typing stay owned by React Aria. TaskGroupDisclosure remains a separate accessible native control with press propagation stopped.

### Task-page text sizes

columnPresentation.tsx owns these recipes: rowItem supplies 0.8rem to ordinary row titles, matching a task-page row; rowTitle retains ellipsis and its parent weight. Its completed/abandoned fold variant explicitly uses 0.72rem. Ids in both groupings, repository, state word, progress figure and group headings use 0.72rem, as does the shared caret. These are the task page's smaller-text size, not the approved proposal's 0.875 font conversion. Titles truncate rather than wrap or shrink, full text stays in the row hover, and the text-size recipes retain their bounded lanes. The new major-step marks use additional progress-lane space; source inspection does not re-establish mounted narrow-column acceptance for that addition. Decorative Dot glyphs retain their em-relative scale; shared Panel chrome retains its own typography.

### Bounds and kept-alive execution

The approved column uses shared Panel chrome and columnTabButton; the bell and bounded Popover do not consume tree height. Grouping/head/layer controls wrap inside a narrow rail. One-line title/word ellipsis is intentional and its full facts remain one hover away; minmax(0,1fr), constrained tracks and row padding prevent the list from expanding its owner. Do not impose this column's overflow rule on Panel globally.

Age values remain server-served: [servedAges](../../data/servedAges.ts.md) stamps each applied object at arrival and advances its served seconds only by elapsed time since that arrival. Missing served ages remain missing, and unanchored fixtures keep their served value; the renderer never invents an event age from its own clock. A ten-second local served-age clock is disabled while the kept-mounted rail is hidden. The memoized render child retains the hidden collection; re-showing renders current subscribed truth. The nested attention bell owns its own subscription/memo gate and is not a second sibling attention block.

### Historical boundary to preserve

The earlier landed-leaf admission/default-collapse extension was emergency-reverted (a9a1a41b); landedLeaves, appendLandedLeafRows and markAutoCollapsed are not current APIs. That earlier proposal is not revived by the new completed fold. Physical worktree admission and one row per enclosure still govern. The old two-array opened/collapsed storage form was also withdrawn: parent collapse remains the single operations.tasks.collapsed.v1 set. The original file/test split put this entry under lifecycle-list and divided suites by behavior; subsequent presentation changes do not change that ownership.

## Evidence



- columnPresentation supplies 0.72rem group headings and 0.8rem ordinary row text. [34]





- columnPresentation gives IDs, fold text, repository, state word and figure explicit 0.72rem while rowTitle retains ellipsis. [35]



- The shared caret uses 0.72rem without changing its fixed lane. [36]
- Task-page rows and smaller labels/counts supply the two text sizes. [37]


- Admission is derived only from documents and physical live-worktree enclosures with one row per enclosure; removed session-catalog selection is not an admission input. [20]



- enclosureForDoc matches taskRoot and exact case-insensitive leafId against document stem or ID, with no display-number or reopen-suffix heuristic. [21]





- groupRows uses the need-ordered tree for BY REPO and creation-ordered flat rows for BY PHASE, counting admitted members. [22]





- TaskRow composes caret, named state mark, ID/title, task-state word and progress; non-master document payloads add cached major-step marks in the figure lane. [23]





- readChoice preserves lifecycle selection while independently marking its carrying task row. [24]





- useRevealChosen consumes each bell request once, reveals/focuses a current carrying row and consumes an absent-row request without later motion. [25]





- Unmodified horizontal arrows affect only a focused parent and do not collapse a held parent; modifiers remain untouched. [26]



- Typeahead preserves title-only matching and the displayed prefix for numbered rows. [27]




- Pure row state/word/hover and pure tree flattening own the presentation derivation. [29]

- The remaining component behavioral suites hold row admission, hierarchy and independent Operations signals; this is source inspection, not a new run. [30]




- runtimeForDoc first returns the explicit document lifecycle lookup; without it, a distinct sibling-enclosure join supplies the fallback. [31]






- treeItems derives held ancestors and completed folds; heldFoldKeys collects only emitted fold keys already marked held. [32]




- Applied-object arrival stamps advance only server-served ages and preserve missing values. [33]
