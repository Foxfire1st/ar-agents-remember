# dashboard/src/panels/detail-panel/docViews.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Dispatch shared own-page text and record views for the sprint, master and task readers without inventing a second document model.

## Code Commentary

`DocContentView` accepts the active typed view, the hydrated reader document and Back/artifact handlers. Requirements, references, header notes, objective and design use the same text-view dispatch across forms; sections, registers and findings use the shared record dispatch. Form-specific collection views remain with the reader, not this module.

References retain server-resolved artifact navigation through `useTaskNotesData` and `TaskNotesReferencesSection`; an own view is not an inert rendering of link strings. A section/register lookup uses its heading and shows its entire body, including surrounding prose, rather than the bounded parsed preview. If the selected section disappears, the view explains that absence. A findings count reads the projection's whole-round `openFindings` and `totalFindings`, not the length or flags of a capped list.

## Boundaries

These views do not fetch the full task body or choose the current document. Hydration stays with `useTaskDocumentBody`, and document-local view/scroll state stays with `useDocView`. The dispatcher does not alter records or derive review totals.

## Evidence

- Shared content-view dispatch preserves form-specific collection ownership. [1]
- Reference views retain server-resolved artifact handlers rather than flattening links. [2]
- Record views preserve complete section bodies and whole-round review counts. [3]
