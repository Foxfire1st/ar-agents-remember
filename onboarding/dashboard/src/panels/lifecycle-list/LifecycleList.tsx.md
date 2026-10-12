# dashboard/src/panels/lifecycle-list/LifecycleList.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

The Operations task-navigation column: a controlled React Aria ListBox with BY REPO tree and BY PHASE flat grouping, one-line rows, and the attention bell in its head. The approved presentation replaces rank chevrons, tier frames and separate gate/chat/pickup chips with one mark, one priority word and a numeric figure; full facts remain in each row's hover. It neither authors task state nor widens row admission.

## Code Commentary

### Admission and durable identity

operationRows admits root/master documents, exact active-enclosure-matched leaves, folder-keyed series fallbacks when no master is projected, and runtime rows backed by a live-worktree enclosure. Physical code or memory worktree existence is the leaf admission fact, never cleanup state. Enclosure joins use exact case-insensitive document stem/id and taskRoot, not display numbering or shared master lifecycle. One enclosure yields one task entry: a bound lifecycle enriches that document row rather than adding a duplicate. When a document binding is absent, the contract lifecycleId and most-recent matching lifecycle anchor provide deterministic fallback. Doc-less runtime rows retain their taskRoot/series parent.

Root/master runtime binding is a distinct join: runtimeForDoc first looks up an explicit doc.lifecycleId directly and returns that lookup, even if it is missing. Only without that id does it look for a sibling enclosure at the document folder whose lifecycleId equals its taskId or taskName. This root branch is not the exact leafId/stem admission join or the most-recent enclosure-anchor fallback used to enrich leaf rows.

Root task documents remain readable without a worktree; loose/planning leaf documents do not become sidebar rows merely because the observer projects them. Reopened leaves return only when their worktrees exist again. Archived/deleted documents disappear with their projection. Keep this admission separate from completed-row folding: a fold contains already admitted rows, not every landed leaf of a master.

### Hierarchy, ordering and collapse

Orchestration documents derive the command tier from their nonempty orchestrates list; commanded masters derive their parent through taskHierarchy. Tier data and hierarchy remain, but tier chevrons, corner frames and ghost washes do not. Indentation is padding inside the bounded row. BY REPO delegates to treeItems: subtree need first, then creation/fallback order, completed/abandoned subtrees behind a scoped in-place count. Cycles cannot drop or duplicate input rows. BY PHASE is flat and creation-ordered within the phase/status groups; it does not use tree disclosures or folds.

The existing collapsed-parent set stays persisted by useCollapsedTaskGroups. Open completed folds are local presentation state and start closed. treeItems derives ancestor holding and held completed folds; heldFoldKeys collects only already-held fold keys from the emitted groups, never parent keys. RowCaret separately passes each non-flat parent row's collapsed/held facts to TaskGroupDisclosure. A selected descendant holds its ancestor chain and containing fold open without rewriting the reader's persisted choices; held parents/folds cannot be collapsed over that descendant. Choosing the parent itself does not force it open. Fold keys are not task-document identities, and activating a fold toggles it rather than choosing a document. Heading and group counts count admitted rows, including rows currently hidden by presentation folds.

### State, signals and secondary facts

rowState decides whether the document or a reporting lifecycle speaks. A lifecycle inferred without lastEventTs is not an observed pause; the document speaks, or waiting when no document exists. A reporting lifecycle retains its raw state mark and eligible local age; completed/abandoned use document-style marks. The single row word prioritizes durable gate, overdue/unacknowledged inbox, chat input, lifecycle asking/stopped state, active chat, then state. The complete hover retains kind, document status, current step, lifecycle/phase/inference, worktree fact, gate, qualified chat activity, pickup acknowledgment and repository.

The compact progress figure is done/total. Abandoned tasks remain outside the denominator, and abandoned/discarded counts remain in the hover rather than masquerading as completion. Chat activity uses the shared Chats-owned session catalog, exact task-document identity first and only unclaimed lifecycle fallback; it is not inferred from task progress, inbox acknowledgment or lifecycle state. Durable gate.kind remains informational: the retired bare-ask fallback is not restored.

An overdue handover offers dismissal even while a gate wins the priority word. PickupDismiss says chat × beside the gate and calls only the exact operator-inbox entry helper. Pointer-down, mouse-down, keyboard and click propagation are stopped because ListBox selection begins on press; dismissing must not select the row or dismiss the gate. The mark wrapper is named inside ListBoxItem's option role; moving it outside a naming widget would require its own accessible role.

### Selection and keyboard reach

Selection keys remain typed taskdoc:, series: and lifecycle:. A lifecycle chosen by an attention entry stays the shell's lifecycle selection; its carrying task row is only marked, held open and focused/scrolled once for that bell request. Clicking that row chooses its document. A request with no carrying row is consumed without motion, including when a row arrives later; selection and row revelation are different facts.

Typeahead uses the displayed short id plus title for numbered master children, and preserves title-prefix matching for sprint/master/standalone labels. A standalone task can now display a separate id cell while still matching its historical title prefix. Unmodified right/left arrows open/close a focused parent only; task and fold rows receive no such tree action, and browser/system modifiers are untouched. Existing up/down, Enter and typing stay owned by React Aria. TaskGroupDisclosure remains a separate accessible native control with press propagation stopped.

### Bounds and kept-alive execution

The approved column uses shared Panel chrome and columnTabButton; the bell and bounded Popover do not consume tree height. Grouping/head/layer controls wrap inside a narrow rail. One-line title/word ellipsis is intentional and its full facts remain one hover away; minmax(0,1fr), constrained tracks and row padding prevent the list from expanding its owner. Do not impose this column's overflow rule on Panel globally.

Age values remain server-served: [servedAges](../../data/servedAges.ts.md) stamps each applied object at arrival and advances its served seconds only by elapsed time since that arrival. Missing served ages remain missing, and unanchored fixtures keep their served value; the renderer never invents an event age from its own clock. A ten-second local served-age clock is disabled while the kept-mounted rail is hidden. The memoized render child retains the hidden collection; re-showing renders current subscribed truth. The nested attention bell owns its own subscription/memo gate and is not a second sibling attention block.

### Historical boundary to preserve

The earlier landed-leaf admission/default-collapse extension was emergency-reverted (a9a1a41b); landedLeaves, appendLandedLeafRows and markAutoCollapsed are not current APIs. That earlier proposal is not revived by the new completed fold. Physical worktree admission and one row per enclosure still govern. The old two-array opened/collapsed storage form was also withdrawn: parent collapse remains the single operations.tasks.collapsed.v1 set. The original file/test split put this entry under lifecycle-list and divided suites by behavior; subsequent presentation changes do not change that ownership.

## Evidence

- Admission is derived from documents and physical worktree enclosures with one row per enclosure, then augmented by exact session identity. [20]
- Exact case-insensitive stem/id and taskRoot joins determine leaf admission. [21]
- BY REPO uses the bounded need-ordered tree; BY PHASE stays flat with its own phase ordering. [22]
- The task row renders caret, named mark, id/title, priority word and figure within its hover-bearing line. [23]
- Lifecycle selection and carrying-row marking are deliberately separate. [24]
- A bell request reveals its current carrying row once and consumes an absent-row request without later motion. [25]
- Unmodified horizontal arrows act on a parent without overriding held selection reach. [26]
- Typeahead preserves title-only matching and the displayed prefix for numbered rows. [27]
- Overdue inbox dismissal names its target, blocks the row press and calls only the inbox helper. [28]
- Pure row state/word/hover and pure tree flattening own the presentation derivation. [29]
- The behavioral suites preserve admission, hierarchy/phase, signal and bare-ask boundaries on the actual component. [30]


- Root/master lifecycle binding first uses the explicit document id, otherwise its distinct sibling-enclosure join. [31]

- Parent holding is derived by treeItems; heldFoldKeys only collects already-held fold keys. [32]

- Applied-object arrival stamps advance only server-served ages and preserve missing values. [33]
