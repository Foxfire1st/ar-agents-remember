# dashboard/src/panels/knowledge-reader/readerParts.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Shared pieces of the knowledge reader (MIK-R29, extended by MIK-R79 rules 8 and 9): navigation links,
state badges, sections, entry rows, a decision in full, and the onboarding prose whose `[n]` markers
link to their resolved references. Every document link is a navigation that changes the reader's
address (and so the URL); a `[n]` marker, a fragment and an external link each take their own local or
separate branch. Rules written in the prose work: a link to another card or overview
opens that page, a `[n]` marker opens the cited code beside the text, and an external link opens
separately.

## Code Commentary

### Logic

- `RecordLink`, `PathLink`, `CodeLink` and `TargetLink` render buttons that call the reader's
  navigation context; a missing record renders as "(not in this tree)".
- `ProseWithReferences` renders the text through the shared `Markdown` with `referenceMarkers` and
  `headingIds`. A `#reference-<n>` marker the reference list holds becomes a button that opens the
  reference (one code/test target opens the citation pane directly); a marker with no reference is
  plain text. Other links resolve through `proseLinkPath`: an authored `onboarding/...md` link opens
  the mapped card or route, an external link opens separately, and a link the memory cannot resolve
  stays readable as text. An unreadable reference list is named as unavailable.
- `DecisionCard` renders the decision's alternatives with statuses, reasons and
  `reconsider when`/`reopens on`; `EntryRow` renders an entry's id, kind, state, role, code link,
  facet and rationale.

### Conventions

- `ReaderNavContext` is the one navigation contract; every component in the reader uses it.
- State badges keep one tone per state; `Section` owns the uppercase section heading and its anchor.

### Invariants And Boundaries

- **A `[n]` marker in the prose links only when a reference exists**: the marker is rendered as a
  button only for a resolved reference, otherwise as plain text — a dead link is never drawn.
- **Unsupported prose links stay in place, external links open separately**, and the dashboard is
  never unloaded by a link (no full-page navigation).
- **A missing record is named in place**; nothing is rendered as an empty record.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 8 and 9); it lives outside the code and memory repositories,
so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The prose renderer, its marker buttons and its link mapping. [12]
- A `[n]` marker becomes a reference button only when the reference resolves. [13]
- The authored-link to memory-path mapping. [14]
- An unsupported link stays readable as text. [15]
- The one navigation context every link uses. [16]
- The decision card with its alternatives. [17]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
