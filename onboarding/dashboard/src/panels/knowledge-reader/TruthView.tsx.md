# dashboard/src/panels/knowledge-reader/TruthView.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/knowledge-reader/TruthView.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:41:49+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db`|
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The knowledge reader's truth view (MIK-R29 rules 3 and 4): one record with every field, its states, its links
both ways and its timeline, newest first.** It renders an invariant, a family, a decision, an incident or any
other facet record from the backend's `record` answer.

## Code Commentary

### Logic

- **The header (ruling 2026-09-30T09:42:58, F9).** `TruthHeader` shows the kind, ID, the invariant's MIK-R03
  state, the status and the revision. A decision's status is its **derived** one (`superseded` is never
  stored), so a superseded decision is headed "superseded".
- **Every field.** `RecordFields` lists every recorded field except those the kind's own sections show
  (`SHOWN_ELSEWHERE`: schema, links, alternatives, members, routes, supersedes); `show` renders strings, string
  lists and JSON. The record's explanation prose is shown when present.
- **Kind parts.** `InvariantPart`: realizations (with the code tree the states were measured at, and the reason
  when unverifiable), proofs, families, and linked records with a decision in full. `FamilyPart`: members with
  their states and statements, the stale-member count, routes, and every member location with its entries.
  A decision is shown by `DecisionCard`.
- **Links both ways.** `OutgoingSection` lists each outgoing relation with its target (and the alternative for
  a decision's `reconsider_on`); when the record's links could not be read it says so
  (`record-outgoing-unavailable`) instead of "no outgoing link" (F11). `IncomingSection` lists every relationship
  towards the record with its source kind and origin path.
- **The timeline.** `TimelineSection` names each source's state: a read source with its event count, a source
  that could not be read with its reason (`timeline-source-unavailable`), never as no history. Each event shows
  its commit (or "uncommitted"), date, subject and source: a record event with its meaning diff
  (`RecordLine`), a history row with its leaf and disposition (`HistoryLine`), and an entry event with its
  change and its from/to paths and locators (`EntryLine`, which shows `moved` and `re-anchored` as the backend
  labels them).

### Conventions

- Every record, path and code target is a navigation link from `readerParts.tsx`.

### Invariants And Boundaries

- **A failed source is shown as partial or unavailable, never as empty:** unreadable links and unreadable
  timeline sources are each named.
- **A decision's alternatives and derived superseded status are shown whole** (the rule carried from L13), in
  the decision's own view and in an invariant's linked records.
- Proved by `KnowledgeReader.test.tsx`: the invariant case (three sources newest first, a meaning diff, a moved
  entry event), the family, decision and incident case, the superseded-header case, the failed-source case and
  the unreadable-links case.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component's own statement of the truth view and its timeline. | "The reader's truth view (MIK-R29 rules 3 and 4)" | dashboard/src/panels/knowledge-reader/TruthView.tsx:1-3 |
| Every field except those the kind's sections show. | `SHOWN_ELSEWHERE`; `RecordFields` | dashboard/src/panels/knowledge-reader/TruthView.tsx:39-46; dashboard/src/panels/knowledge-reader/TruthView.tsx:57-70 |
| The header with the derived decision status (F9). | `TruthHeader` | dashboard/src/panels/knowledge-reader/TruthView.tsx:81-98 |
| Outgoing links, or why they could not be read; incoming links. | `OutgoingSection`; `IncomingSection` | dashboard/src/panels/knowledge-reader/TruthView.tsx:100-126; dashboard/src/panels/knowledge-reader/TruthView.tsx:136-155 |
| The truth view. | `TruthView` | dashboard/src/panels/knowledge-reader/TruthView.tsx:157-181 |
| The invariant and family parts. | `InvariantPart`; `FamilyPart` | dashboard/src/panels/knowledge-reader/TruthView.tsx:183-242; dashboard/src/panels/knowledge-reader/TruthView.tsx:244-293 |
| History rows, entry events and record events with meaning diffs. | `HistoryLine`; `EntryLine`; `RecordLine` | dashboard/src/panels/knowledge-reader/TruthView.tsx:295-304; dashboard/src/panels/knowledge-reader/TruthView.tsx:316-324; dashboard/src/panels/knowledge-reader/TruthView.tsx:326-344 |
| The timeline, each source's state named. | `TimelineSection` | dashboard/src/panels/knowledge-reader/TruthView.tsx:352-389 |
| The invariant, and family, decision and incident cases. | "opens an invariant truth view with its states, links and a three-source timeline"; "opens a family, a decision and an incident with every field and their links" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:235-290 |
| The superseded header, and unreadable links named. | "heads a superseded decision with its derived status"; "names record links that could not be read instead of claiming there are none" | dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:449-453; dashboard/src/panels/knowledge-reader/KnowledgeReader.test.tsx:491-503 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:41:49+02:00 — 260928-MIK-L29 curator (follow-up after the coordinator's test-only edit, staged): No content impact: this card's source is unchanged. The five-line debugging block removed from `KnowledgeReader.test.tsx` sat above the unreadable-links case, so that row was re-measured by the exact −5 shift (`496-508` → `491-503`). No claim was reworded. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:06:02+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`; review R3 and post-sync pass-with-notes, with R3-1 and R3-2 fixed): created this card for the new view MIK-R29 adds, recording the carried L13 rule, rulings 09:42:58 F9 (the derived status in the header), F11 (unreadable links named) and F6 (the failed timeline source tested), and 10:44:14 F17 (the unreadable-links display tested). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
