# dashboard/src/panels/detail-panel/taskReader.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Compose one fixed document reader skeleton per sprint, master and task form. Identity/head, bounded block implementations and own-view dispatch have their own modules; this file owns their page order, selected-document state lifetime and navigation wiring.

## Code Commentary

The shared head contains the objective first under the title, then facts/notes. A sprint composes Now, its scoped closeout queue, inline Order rows, grouped Masters, Requirements, Registers, Decisions/Open questions, Further notes and Notes. A master keeps Now, grouped Tasks, Requirements, Decisions/Open questions, Further notes and Notes; its task order remains received order. A task keeps Steps, Review, Requirements, Design, proposed-code titles, Decisions/Open questions, one References and reports block, Further notes and the single Notes line. Each block omits actual absence; introducing structured prose and discarded-before-start audit remain meaningful content, not duplicate lists.

Every reader is keyed by `docIdentity`: choosing a different document resets its own view, objective/note/row expansion, while body arrival for the same identity preserves reader state. `TaskRequirementBoundary` scopes the existing requirement-link provider to the viewed repository/task document and forwards internal artifact navigation on every form. Own-view content uses `DocContentView`; form-specific collection, whole-graph and code-example views stay here.

Task report requests pass the task-root-relative document path from `taskDocumentRefForDoc`, falling back to docPath only when no reference resolves. A projected filesystem path is not the server's canonical report address. Ancillary references/reports and Notes are mounted after body loading settles; the task's final Notes island reads the root-folder count, never the note tree or content. Full-body unavailability keeps honest summary fallback.

Typed commanded-master and cross-series index navigation moved to task-groups.tsx. DecisionPreview moved to skeletons.tsx but remains re-exported for existing consumers; its five-newest-authored and whole-log semantics are preserved. A graph-less sprint can still show its scoped closeout queue; the full wave-grid graph is now an Order own view, not a second inline list. Discard-before-start remains an audit distinct from live rows and completion totals. A master-less series retains the clickable slice-list fallback and its creation ordering.

## Boundaries

No authored document-model mutation, lifecycle acceptance or native review occurs here. The grant control posts Give/Revoke through its dedicated adapter; this is external-store mutation, not task JSON authoring or browser permission authority. Form-specific rendering follows projected form with the model's older-cache fallback. Shared Panel/Markdown/token styling remains unchanged; pageStyles.ts scopes the task-page look. The lifecycle spine, change-set authority, requirement reader and Notes transport keep their existing owners.

## Landed direct-grant control in the fixed pages

The sync retains L94's `rowDirectGrant`/`DirectGrantControl` block and `grantButton` style byte-for-byte at their landed owner. The React import gains `useEffect`, `useRef` and `useState`; `ReactNode` was already imported. The control offers developer Give/Revoke only for an authored subTask with a canonical document reference, disables pending actions, and exposes typed refusal. The backend owns the ordinary-start evidence gate; a local badge or control state cannot authorize direct execution.

`leafRowGrant` supplies the giver badge and preserved control through the `LeafExtra` row adapter to master Now, waiting Tasks, and leaf group-view rows. `TaskDirectGrant` places the selected leaf's badge/control directly below DocHead. Row badges are beside the drill-in link, not inside it; the selected badge is below rather than inside the bounded head. These are explicit placement differences, not an equivalent-layout claim. Sprint/master rows receive no leaf control. Passing the adapter into task-groups avoids importing the reader back into the row module.

Reviewer source-only placement/sync PASS does not establish whole-feature or MEMORY acceptance. The retained Worker eslint capture exits 1 with exactly the three Owner-admitted L150 errors in the unchanged control; the reader is not lint-clean. The inherited Python-format hunk, absent new layout picture and spent ONE campaign remain separately disclosed in task evidence. New memory review is delta reading only.

## Evidence

- Reader entry dispatch selects the sprint/master/task skeleton for the resolved document. [1]
- Typed form pages retain their index and own-view composition owners. [2]
- The master-less slice fallback retains authored-document navigation and creation ordering. [3]
- Task-only steps are rendered by the shared table owner rather than the retired StepList primitive. [4]
- The relocated preview preserves newest-authored selection and whole-log navigation. [5]
- Task references/reports use a task-root-relative document address after body loading settles. [6]
- The landed control retains its authored-leaf guard, pending state and typed refusal without browser authorization authority. [7]
- Leaf-row and selected-leaf adapters place the preserved badge/control in the fixed page structure. [8]
