# dashboard/src/panels/detail-panel/taskReader.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Compose a single entry/summary reader with fixed sprint/master/task content ordering. Head, bounded blocks and own views keep their modules; this owner retains page state and navigation wiring without synthetic series/leaf dispatch.

## Code Commentary

Each form renders the identity head, body notice and ReaderHead change-set chrome before the bounded ObjectiveLead; a task’s direct-grant slot also precedes the objective. Objective bounds, more/full-view links and entry-keyed open state remain. A sprint composes Now, its scoped closeout queue, inline Order rows, grouped Masters, Requirements, Registers, Decisions/Open questions, Further notes and Notes. A master places optional Non-goals after its objective, then Now, the scoped closeout seam, projected Order, grouped Tasks, Requirements, Design, Acceptance, Decisions/Open questions, Further notes and Notes. Thus both overview forms put Now before CloseoutQueue. Their ordinary index groups retain received order, while the projected graph and completed-task table have their own display ordering. A task places optional Non-goals after its objective, then Steps, Review, Requirements, Design, Acceptance, proposed-code titles, Decisions/Open questions, one References and reports block, Further notes and the single Notes line. Each block omits actual absence; introducing structured prose and discarded-before-start audit remain meaningful content, not duplicate lists. No waitsFor topology or completion timestamp is authored here.

TaskPage is keyed by the canonical `entry.key`: choosing a different entry resets its own view and objective/note/row expansion, while body arrival for the same entry preserves reader state. The inline requirement-link provider scopes the existing requirement-link provider to the viewed repository/task document and forwards internal artifact navigation on every form. Own-view content uses `DocContentView`; form-specific collection, whole-graph and code-example views stay here.

References/reports and Notes use the entry’s exact reference repository and task-root-relative path. Ancillary reads wait until body loading settles; final Notes reads the root-folder count, not the tree/content. Unavailable bodies keep honest summary fallback.

indexRows/task-groups follow served children and exact entry-key navigation. The head/objective composition is local to this reader; readerTop supplies only TaskBodyNotice. DecisionPreview remains in skeletons and is re-exported. A graph-less sprint retains its scoped queue; full graph is an Order own view. No master-less series/slice fallback remains.


**L184 — INV-XZYGEB.** This reader is where the page's task entry arrives, so the limit fact it may show has to be passed here. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Boundaries

No authored document-model mutation, lifecycle acceptance or native review occurs here. The extracted directGrant owner posts Give/Revoke through its dedicated adapter; this is external-store mutation, not task JSON authoring or browser permission authority. Form-specific content follows the served summary form; no browser form fallback reconstructs task topology. Revision-keyed register/further preparation is retained in the bounded store resource only after body availability; handlers remain selection-local. Shared Panel/Markdown/token styling remains unchanged; pageStyles.ts scopes the task-page look. The worktree spine, change-set authority, requirement reader and Notes transport keep their existing owners.

## Direct execution on the selected task

Only a planned subTask's own page composes TaskDirectGrant from directGrant.tsx after DocHead and before the body notice, ReaderHead and objective: one Direct execution label, a track-and-knob switch and given-by words when granted. Pending disables the switch without moving its served position. directGrant.tsx owns canonical adapter requests, served-state synchronization by document key and giver/time content, typed notice and late-answer suppression; refusals retain the actual grant.

Other granted subTask states render bare Direct · given by words and no control; grantless states show nothing. Masters and sprints render neither a row control nor a row mark. This deliberately replaces the old rowDirectGrant/LeafExtra and preserved text-button presentation under the developer's revised scope. It does not change the external grant store, backend start-evidence gate or permission owner.

## Evidence













- StepsBlock owns the full served step table and derives its header marks from those steps; taskReader supplies doc.steps and the served done/total counts. [4]





- The relocated DecisionPreview keeps five newest authored decisions and an authored-only all-link to the records-retaining whole-log target. [5]





- The planning-task switch stays rendered while pending, disables its action and displays served giver words and adapter notice. [7]





- Only a planning subTask receives the switch; other granted states receive bare words. [8]



- TaskPage identity is the canonical entry key; the surrounding clock runs for shown entries that carry an event time or a served limited status. [9]

- Both overview forms compose Now before the scoped closeout queue and Order. [10]
