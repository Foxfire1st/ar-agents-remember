# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/unknownRun.tsx

## Governing Overview

[session-cockpit/conversation overview](../overview.md)

## Purpose

The collapsed unknown-vendor run row of the Conversation Timeline, extracted from
`ConversationTimeline.tsx` by the 260731-EFA-L8 split. `UnknownVendorRun` renders
the expandable dim mono gutter row for a run of ≥3 identical-summary items;
`isEditableTarget` / `inOverflowRegion` back the keyboard contract.

## Code Commentary

### Logic

Members stay addressable (`#ordinal · evidenceRef`) and identity is never mutated;
the copy is honest (`N unknown vendor events (same summary)` — members share a
summary but carry distinct evidence ids).

### Conventions

The toggle is a de-boxed underline text affordance.

### Invariants And Boundaries

Collapse only applies to runs of ≥3 identical summaries; expanded members indent
under the summary row.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The collapsed-run row and keyboard helpers. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
