# dashboard/src/panels/detail-panel/taskReader.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Compose one fixed document reader skeleton per sprint, master and task form. Identity/head, bounded block implementations and own-view dispatch have their own modules; this file owns their page order, selected-document state lifetime and navigation wiring.

## Code Commentary

Each form renders the complete shared head, then ObjectiveLead as its first block, before Now or Steps. The objective bound, more/full-view links and document-keyed open state are preserved. A sprint composes Now, its scoped closeout queue, inline Order rows, grouped Masters, Requirements, Registers, Decisions/Open questions, Further notes and Notes. A master keeps Now, grouped Tasks, Requirements, Decisions/Open questions, Further notes and Notes; its task order remains received order. A task keeps Steps, Review, Requirements, Design, proposed-code titles, Decisions/Open questions, one References and reports block, Further notes and the single Notes line. Each block omits actual absence; introducing structured prose and discarded-before-start audit remain meaningful content, not duplicate lists.

Every reader is keyed by `docIdentity`: choosing a different document resets its own view, objective/note/row expansion, while body arrival for the same identity preserves reader state. `TaskRequirementBoundary` scopes the existing requirement-link provider to the viewed repository/task document and forwards internal artifact navigation on every form. Own-view content uses `DocContentView`; form-specific collection, whole-graph and code-example views stay here.

Task report requests pass the task-root-relative document path from `taskDocumentRefForDoc`, falling back to docPath only when no reference resolves. A projected filesystem path is not the server's canonical report address. Ancillary references/reports and Notes are mounted after body loading settles; the task's final Notes island reads the root-folder count, never the note tree or content. Full-body unavailability keeps honest summary fallback.

Typed commanded-master and cross-series index navigation moved to task-groups.tsx. DecisionPreview moved to skeletons.tsx but remains re-exported for existing consumers; its five-newest-authored and whole-log semantics are preserved. A graph-less sprint can still show its scoped closeout queue; the full wave-grid graph is now an Order own view, not a second inline list. Discard-before-start remains an audit distinct from live rows and completion totals. A master-less series retains the clickable slice-list fallback and its creation ordering.

## Boundaries

No authored document-model mutation, lifecycle acceptance or native review occurs here. The grant control posts Give/Revoke through its dedicated adapter; this is external-store mutation, not task JSON authoring or browser permission authority. Form-specific rendering follows projected form with the model's older-cache fallback. Shared Panel/Markdown/token styling remains unchanged; pageStyles.ts scopes the task-page look. The lifecycle spine, change-set authority, requirement reader and Notes transport keep their existing owners.

## Direct execution on the selected task

Only a planning subTask's own page composes DirectExecutionSwitch after the head and objective: one Direct execution label, a track-and-knob switch and given-by words when granted. Pending disables the switch without moving its served position. useDirectGrant owns canonical adapter requests, served-state synchronization by document key and giver/time content, typed notice and late-answer suppression; refusals retain the actual grant.

Other granted subTask states render bare Direct · given by words and no control; grantless states show nothing. Masters and sprints render neither a row control nor a row mark. This deliberately replaces the old rowDirectGrant/LeafExtra and preserved text-button presentation under the developer's revised scope. It does not change the external grant store, backend start-evidence gate or permission owner.

## Evidence

- Sprint and master composition draws the complete head, then one bounded objective, before body and Now. [10]

- Task composition draws the complete head, then the objective, before the task body and Steps. [11]

- The grant hook synchronizes served content and rejects late replies after identity turnover. [9]


- Reader entry dispatch selects the sprint/master/task skeleton for the resolved document. [1]
- Typed form pages retain their index and own-view composition owners. [2]
- The master-less slice fallback retains authored-document navigation and creation ordering. [3]
- Task-only steps are rendered by the shared table owner rather than the retired StepList primitive. [4]
- The relocated preview preserves newest-authored selection and whole-log navigation. [5]
- Task references/reports use a task-root-relative document address after body loading settles. [6]
- The planning-task switch keeps served position while pending and exposes giver and server notice. [7]

- Only a planning subTask receives the switch; other granted states receive bare words. [8]
