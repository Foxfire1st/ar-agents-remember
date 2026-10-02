# dashboard/src/panels/knowledge-reader/TruthView.tsx

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
- **History rows and decisions, both ways (L37, MIK-R29 rules 4 and 5).** `HistoryLine` shows a row's `effect`
  after its disposition ("changed · replace") and, under `because`, each target of the row's `because`
  (`becauseTargets`): a record ID is a navigation link, a requirement is named as elsewhere in the reader. A row
  with neither renders as before. `IncomingSource` shows a link whose source is a history row as the record the
  row is about (`sourceSubject`, a navigation link) followed by "row <ROW-ID>"; a row served without its subject
  stays the plain row ID.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The component's own statement of the truth view and its timeline. [1]
- Every field except those the kind's sections show. [2]
- The header with the derived decision status (F9). [3]
- Outgoing links, or why they could not be read; incoming links. [4]
- The truth view. [5]
- The invariant and family parts. [6]

- History rows, entry events and record events with meaning diffs. [7]

- The timeline, each source's state named. [8]
- The invariant, and family, decision and incident cases. [9]
- The superseded header, and unreadable links named. [10]

- A history row's line: its effect, and its because targets as links. [11]
- A row's because: a record ID navigates, a requirement is named. [12]
- An incoming link from a history row names the record the row is about. [13]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
