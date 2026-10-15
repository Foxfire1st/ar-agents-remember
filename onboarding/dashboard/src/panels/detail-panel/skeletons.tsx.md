# dashboard/src/panels/detail-panel/skeletons.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Own shared bounded document blocks, own-view scroll state and the relocated decision preview; re-export DocHead and ObjectiveLead from their owning module while the form readers compose their order elsewhere.

## Code Commentary

`useDocView` captures the actual scrolling DetailPanel element at view entry, falling back to window only when no panel scrolls. It saves that owner's offset, opens at the top, and restores the same owner on Back on the next animation frame. Escape delegates to Back. The captured owner must not be recomputed after view replacement changes scrollability. The D229 refactor makes Back a stable `useCallback` reading those saved refs; the Escape listener depends on the open-view boolean and Back, so switching between open views does not reinstall it.

Requirements preview eight lines, registers five last-written rows and four visible columns. The register all-link exists even for a short table so surrounding prose remains reachable; its own view renders the complete original section body. Register cells and expanded columns retain Markdown navigation, and nested link clicks do not toggle a row. Long prose has both line and character bounds; a single huge paragraph cannot evade them.

`DecisionPreview` preserves newest-first parsed-time ordering, five authored decisions and an omitted-entry link naming only the authored decision count. Product records count toward neither decision totals nor numbering. They are omitted from the preview, not erased from the whole-log target; records alone still trigger its link. DecisionList whole mode renders text and rationale without a row expansion control; decisionNumbers numbers authored decisions from oldest to newest, excluding records. Open questions remain under Decisions, and introducing prose alone keeps a meaningful Decisions block. Further notes name free-form section sizes; form-specific classification prevents a second structured index or objective echo. The change-set chrome waits until body loading has settled. FixedMarkdownBlock omits absent optional text, bounds its closed preview, and expands the original full structured text locally without a new reader route or own-view kind.

## Boundaries

Shared visual primitives live in pageParts.tsx; the head, task-only blocks and index groups have separate owners. This module neither selects the document nor changes task/knowledge state. Scroll-call unit observations do not substitute for real browser restoration evidence.

## Evidence


- Own views capture and restore the entry-time scroll owner; stable Back reads saved refs and Escape listens while an own view is open. [1]



- The preview shows five newest authored decisions, excludes product records from counts/numbering and links to the records-retaining whole log with an authored-only label. [2]


- Short and long register previews retain a link to every original section byte. [3]
- Complete register section prose is rendered in its own view, not reconstructed from preview rows. [4]
