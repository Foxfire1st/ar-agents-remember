# dashboard/src/panels/session-cockpit/conversation/conversation-timeline/unknownRun.tsx

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `dashboard/src/panels/session-cockpit/conversation/conversation-timeline/unknownRun.tsx` |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-07T08:19Z                                           |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                  |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                                            |

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

## Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The collapsed-run row and keyboard helpers. | `UnknownVendorRun`; `isEditableTarget` | dashboard/src/panels/session-cockpit/conversation/conversation-timeline/unknownRun.tsx:12-20; dashboard/src/panels/session-cockpit/conversation/conversation-timeline/unknownRun.tsx:27-68 |

## Cross-Repo References

No cross-repository implementation source governs this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: created this sidecar for the
  unknown-run module extracted from `ConversationTimeline.tsx`. Verification pinned
  to the leaf base until closeout stamps the code commit.
