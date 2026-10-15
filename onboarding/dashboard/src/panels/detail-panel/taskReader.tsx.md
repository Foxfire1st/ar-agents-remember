# dashboard/src/panels/detail-panel/taskReader.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Compose one fixed document reader skeleton per sprint, master and task form. Identity/head, bounded block implementations and own-view dispatch have their own modules; this file owns their page order, selected-document state lifetime and navigation wiring.

## Code Commentary

Each form renders the identity head, body notice and ReaderHead series/change-set chrome before the bounded ObjectiveLead; a task’s direct-grant slot also precedes the objective. Objective bounds, more/full-view links and document-keyed open state remain. A sprint composes Now, its scoped closeout queue, inline Order rows, grouped Masters, Requirements, Registers, Decisions/Open questions, Further notes and Notes. A master places optional Non-goals after its objective, then the existing scoped closeout seam, Now, projected Order, grouped Tasks, Requirements, Design, Acceptance, Decisions/Open questions, Further notes and Notes. Its ordinary index groups retain received order, while the projected graph and completed-task table have their own display ordering. A task places optional Non-goals after its objective, then Steps, Review, Requirements, Design, Acceptance, proposed-code titles, Decisions/Open questions, one References and reports block, Further notes and the single Notes line. Each block omits actual absence; introducing structured prose and discarded-before-start audit remain meaningful content, not duplicate lists. No waitsFor topology or completion timestamp is authored here.

Every reader is keyed by `docIdentity`: choosing a different document resets its own view, objective/note/row expansion, while body arrival for the same identity preserves reader state. `TaskRequirementBoundary` scopes the existing requirement-link provider to the viewed repository/task document and forwards internal artifact navigation on every form. Own-view content uses `DocContentView`; form-specific collection, whole-graph and code-example views stay here.

Task report requests pass the task-root-relative document path from `taskDocumentRefForDoc`, falling back to docPath only when no reference resolves. A projected filesystem path is not the server's canonical report address. Ancillary references/reports and Notes are mounted after body loading settles; the task's final Notes island reads the root-folder count, never the note tree or content. Full-body unavailability keeps honest summary fallback.

Typed commanded-master and cross-series index navigation is implemented in indexRows.tsx, with task-groups.tsx importing and re-exporting the shared helpers. OverviewTop and TaskBodyNotice are implemented in readerTop.tsx; this file imports them and re-exports TaskBodyNotice. DecisionPreview moved to skeletons.tsx but remains re-exported for existing consumers; its five-newest-authored and whole-log semantics are preserved. A graph-less sprint can still show its scoped closeout queue; the full wave-grid graph is now an Order own view, not a second inline list. Discard-before-start remains an audit distinct from live rows and completion totals. A master-less series retains the clickable slice-list fallback and its creation ordering.

## Boundaries

No authored document-model mutation, lifecycle acceptance or native review occurs here. The grant control posts Give/Revoke through its dedicated adapter; this is external-store mutation, not task JSON authoring or browser permission authority. Form-specific rendering follows projected form with the model's older-cache fallback. Shared Panel/Markdown/token styling remains unchanged; pageStyles.ts scopes the task-page look. The lifecycle spine, change-set authority, requirement reader and Notes transport keep their existing owners.

## Direct execution on the selected task

Only a planning subTask's own page composes DirectExecutionSwitch after DocHead and before the body notice, ReaderHead and objective: one Direct execution label, a track-and-knob switch and given-by words when granted. Pending disables the switch without moving its served position. useDirectGrant owns canonical adapter requests, served-state synchronization by document key and giver/time content, typed notice and late-answer suppression; refusals retain the actual grant.

Other granted subTask states render bare Direct · given by words and no control; grantless states show nothing. Masters and sprints render neither a row control nor a row mark. This deliberately replaces the old rowDirectGrant/LeafExtra and preserved text-button presentation under the developer's revised scope. It does not change the external grant store, backend start-evidence gate or permission owner.

## Evidence


- readerTop’s OverviewTop draws identity, body notice and series/change-set chrome before the bounded objective, then optional Non-goals on non-sprint forms. [10]




- TaskReaderPage draws DocHead, the task direct-grant slot, body notice and ReaderHead before ObjectiveLead and optional Non-goals, then Steps. [11]



- The grant hook synchronizes served content and rejects late replies after identity turnover. [9]


- Reader entry dispatch selects the sprint/master/task skeleton for the resolved document. [1]
- Typed form pages retain their index and own-view composition owners. [2]
- The master-less slice fallback retains authored-document navigation and creation ordering. [3]

- StepsBlock owns the task’s full step table and receives cached major-step payloads for header marks; reader composition only supplies served steps and counts. [4]



- The relocated DecisionPreview keeps five newest authored decisions and an authored-only all-link to the records-retaining whole-log target. [5]


- Task references/reports use a task-root-relative document address after body loading settles. [6]

- The planning-task switch stays rendered while pending, disables its action and displays served giver words and adapter notice. [7]



- Only a planning subTask receives the switch; other granted states receive bare words. [8]
