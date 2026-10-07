# dashboard/src/panels/knowledge-reader/TruthView.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The reader's truth view (MIK-R29 rules 3 and 4, ordered by MIK-R79 rule 12): one record with its
kind, identifier, states and revision on one line, its meaning as the lead, the remaining meaning
fields as labelled paragraphs in a fixed order per kind, its realizations and proofs, members and
locations, links in both directions, the timeline, and last the file, admission and origin as
labelled lines. The lead is the invariant's statement, the family's guarantee, the decision's
context, and so on per kind.

## Code Commentary

### Logic

- `TruthHeader` shows kind, id, the invariant's state badge, the derived decision status
  (`superseded` is never stored) and the revision. The lead field comes from `LEAD`; `RecordFields`
  renders the remaining fields in `ORDER[kind]` first and the rest sorted, framed fields excluded.
- `InvariantPart` renders realizations (with the states-at-code-tree line), proofs, families and
  linked records; `FamilyPart` renders members with their statements and states, routes and member
  locations. Empty lists are not drawn.
- `OutgoingSection` names an unreadable link list instead of showing none; `IncomingSection` maps a
  history-row source to the record the row is about, since a row has no page of its own.
- `TimelineSection` combines the record file's own log, the history rows about it and the
  realization/proof entries, newest first; `RecordOrigin` closes with the file path, admission and
  origin as labelled lines.

### Conventions

- Values render through `Value`: arrays as lists, objects as labelled pairs, empty arrays as
  "(none)", null as an em dash.
- Every reference to another record is a navigation; the reader never fabricates a missing record.

### Invariants And Boundaries

- **A record reads top to bottom** in the fixed order above; realizations and proofs follow the
  meaning fields, links follow those, and the timeline is near-last (rule 12).
- **A direction with no links is one plain line**, and an unreadable direction is named as
  unavailable rather than shown as empty.
- **A decision's status is the derived one**; a superseded decision renders as superseded without
  storing that status.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rule 12); it lives outside the code and memory repositories, so it
is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The record page in its fixed order. [14]
- The header with kind, id, state, derived status and revision. [15]
- The field order and the per-kind lead. [16]
- A history-row source leads to the record it is about. [17]
- The combined newest-first timeline. [18]
- The labelled file, admission and origin close. [19]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
