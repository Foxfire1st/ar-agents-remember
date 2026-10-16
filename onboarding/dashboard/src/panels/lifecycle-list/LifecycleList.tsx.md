# dashboard/src/panels/lifecycle-list/LifecycleList.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

The Operations task-navigation column: a controlled React Aria ListBox with BY REPO tree and BY PHASE flat grouping, one-line rows, and the attention bell in its head. The approved presentation replaces rank chevrons, tier frames and separate gate/chat/pickup chips with one state mark, one task-state word and a progress figure, with cached major-step marks for non-master document rows; full facts remain in each row's hover. It neither authors task state nor widens row admission.

## Code Commentary

### Admission and durable identity

Every served TaskEntry is admitted, including planned/terminal/addressless rows without worktrees. Exact parent/children drive BY REPO; shared stage/activity drives BY PHASE, whose group order is `works`, `paused`, `unknown`, `started`, `planned`, `completed`, `aborted` (`PHASE_ORDER`). No document/series/session join remains; addressless entries only limit document navigation.





### Hierarchy, ordering and collapse

Command hierarchy follows served parent/children; no orchestrates or taskHierarchy reconstruction remains. Indentation and local collapse retain presentation ownership without tier frames, ghost washes or rank chevrons.

The existing collapsed-parent set stays persisted by useCollapsedTaskGroups. Open completed folds are local presentation state and start closed. treeItems derives ancestor holding and held terminal folds directly from served membership. RowCaret separately passes each non-flat parent row's collapsed/held facts to TaskGroupDisclosure. A selected descendant holds its ancestor chain and containing fold open without rewriting the reader's persisted choices; held parents/folds cannot be collapsed over that descendant. Choosing the parent itself does not force it open. Fold keys are not task-document identities, and activating a fold toggles it rather than choosing a document. Heading and group counts count admitted rows, including rows currently hidden by presentation folds.

### State, signals and secondary facts

The row uses shared taskStatusKey/TaskStatusWord from entry stage/activity, with display-only host-event age. rowBand orders own works first, then started, planned and terminal entries; it does not prioritize gates, inbox or chat facts.

Progress reads entry stepsDone/stepsTotal for task summaries or served child counts for parents, excluding aborted from the denominator and preserving aborted/discarded audit in hover. Up to twelve major-step marks may expose cached pointer detail; larger populations use an aggregate bar. For non-task forms the figure prefixes progress with the server’s `counts.works` and `counts.paused`, adding `counts.unknown` only when nonzero; task forms show `StepMarks` instead. No local child-status recount or physical-worktree admission is introduced.

There is no PickupDismiss or operator-inbox dismissal interaction in LifecycleList. The mark wrapper remains named inside ListBoxItem option semantics; accessibility must not depend on a removed action. Row selection/hover keep their retained owner without restoring press suppression for a deleted button.

### Selection and keyboard reach

Selection is the opaque taskdoc-prefixed entry key. One-time focus reveal marks the selected entry and holds served ancestors/folds open; a missing-row request is consumed without later motion. No attention-lifecycle carrying-row translation remains.

Typeahead uses the displayed short id plus title for numbered master children, and preserves title-prefix matching for sprint/master/standalone labels. A standalone task can now display a separate id cell while still matching its historical title prefix. Unmodified right/left arrows open/close a focused parent only; task and fold rows receive no such tree action, and browser/system modifiers are untouched. Existing up/down, Enter and typing stay owned by React Aria. TaskGroupDisclosure remains a separate accessible native control with press propagation stopped.

### Task-page text sizes

columnPresentation.tsx owns these recipes: rowItem supplies 0.8rem to ordinary row titles, matching a task-page row; rowTitle retains ellipsis and its parent weight. Its completed/abandoned fold variant explicitly uses 0.72rem. Ids in both groupings, repository, state word, progress figure and group headings use 0.72rem, as does the shared caret. These are the task page's smaller-text size, not the approved proposal's 0.875 font conversion. Titles truncate rather than wrap or shrink, full text stays in the row hover, and the text-size recipes retain their bounded lanes. The new major-step marks use additional progress-lane space; source inspection does not re-establish mounted narrow-column acceptance for that addition. Decorative Dot glyphs retain their em-relative scale; shared Panel chrome retains its own typography.

### Bounds and kept-alive execution

The approved column uses shared Panel chrome and columnTabButton; the bell and bounded Popover do not consume tree height. Grouping/head/layer controls wrap inside a narrow rail. One-line title/word ellipsis is intentional and its full facts remain one hover away; minmax(0,1fr), constrained tracks and row padding prevent the list from expanding its owner. Do not impose this column's overflow rule on Panel globally.

TaskStatusWord uses one shared visible clock to advance published host-event age. Hidden-list subscriptions are paused; time labels never infer stage/activity from elapsed silence. Missing age/event facts stay unknown.

### Historical boundary to preserve



## Evidence



- columnPresentation supplies 0.72rem group headings and 0.8rem ordinary row text. [34]





- columnPresentation gives IDs, fold text, repository, state word and figure explicit 0.72rem while rowTitle retains ellipsis. [35]



- The shared caret uses 0.72rem without changing its fixed lane. [36]
- Task-page rows and smaller labels/counts supply the two text sizes. [37]






























- Unmodified horizontal arrows affect only a focused parent and do not collapse a held parent; modifiers remain untouched. [26]



- Typeahead preserves title-only matching and the displayed prefix for numbered rows. [27]




- Pure row state/word/hover and pure tree flattening own the presentation derivation. [29]

- The remaining component behavioral suites hold row admission, hierarchy and independent Operations signals; this is source inspection, not a new run. [30]

- Non-task forms show served child works/paused counts and a nonzero unknown count before progress; BY PHASE groups use the explicit works-to-aborted order. [38]
