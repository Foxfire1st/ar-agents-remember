# dashboard/src/panels/knowledge-reader/TruthView.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Renders one record with meaning first, kind-ordered remaining fields, its relevant relationships, a bounded owner-provided timeline and labelled file/admission/origin at the end. Record framing is separate from raw JSON; decision status is the supplied derived status when available.

## Code Commentary

`LEAD`, `ORDER` and `FRAME` distinguish the lead, ordered meaning fields and framing fields. `Value` renders lists and labelled object pairs. The page preserves realizations/proofs, family members/locations, decisions and both link directions; an unreadable outgoing list is named, and history-row incoming links lead to their subject record.

The timeline now owns local paging state from its initial record answer. Show older sends the owner continuation; Load first page omits it and replaces rather than appends events. The loader uses the current reader navigation repository/commit and the initial record id, with one request in flight. It rejects a non-view answer, absent timeline, explicit refused timeline or changed selection treeKey/memoryRevision. Admitted continuation events append in the owner’s order, not a client recomputed sort. Failed or mismatched reads leave existing events and show the failure/restart/reload controls. Inactive completions are ignored, not aborted.

History rows show their delivered owner, disposition, recorded effect and open fact, with explicit attempt/path provenance. A changed family row with no string effect gets “effect not recorded”; the guard itself does not infer a label or verify the historical era. Requirement because-references are labelled as external task-document facts rather than turned into memory-record links. Stored record because-references keep normal navigation. The timeline does not rewrite history.

## Invariants And Boundaries

Meaning and labelled field order remain ahead of relationships; timeline stays near-last and origin last. New timeline controls do not replace the record’s selection or the page’s meaning data. A bounded timeline is not the whole history until its owner has supplied the remaining pages; an unreadable source is never represented by inventing a favorable result.

<details>
<summary>Historical prior account — retained, not the current contract</summary>

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

- The record page in its fixed order. (historical reference 14)
- The header with kind, id, state, derived status and revision. (historical reference 15)
- The field order and the per-kind lead. (historical reference 16)
- A history-row source leads to the record it is about. (historical reference 17)
- The combined newest-first timeline. (historical reference 18)
- The labelled file, admission and origin close. (historical reference 19)

### Cross-Repo References

No cross-repo boundary is crossed by this file.

</details>

## Evidence

No Domain Documentation entries are configured; current repository bodies and caller boundaries supply the evidence below. The prior source-only accounts are preserved above, not promoted to a fresh execution result.

- The record page keeps lead/fields/relationships/timeline/origin order while wiring timeline paging by the initial answer. [14]
- Kind/id/state/derived-or-stored status/revision are supplied by the current header. [15]
- Per-kind lead/order and framing exclusion govern labelled meaning values. [16]
- An incoming history-row link names and navigates its subject record. [17]
- The bounded timeline renders owner-ordered events and source problems, with attempt/path facts and paging controls. [18]
- File path, admission and origin close the page as labelled values. [19]
- Timeline loads reject non-view/absent/refused responses and changed selection keys, with restart replacing and continuation appending events. [20]
- History effects, historical omissions, requirement labels and record links remain distinct delivered facts. [21]
