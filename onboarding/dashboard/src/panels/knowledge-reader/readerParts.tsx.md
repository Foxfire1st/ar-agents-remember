# dashboard/src/panels/knowledge-reader/readerParts.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The shared pieces of the knowledge reader (MIK-R29): navigation links, state badges, a decision in full, and
onboarding prose whose `[n]` markers link to their resolved references.** Every link here is a navigation: it
changes the reader's address (and so the URL), never local state (rule 5).

## Code Commentary

### Logic

- **Navigation.** `ReaderNavContext` carries the repository, memory tree and `go`; `useReaderNav` refuses to
  render a link outside the reader. `RecordLink` opens a record's truth view (a target the tree does not hold
  shows "(not in this tree)"), `PathLink` a path view, and `CodeLink` the code view at an anchor's locator
  (`codeAddress`). `TargetLink` picks the right one for any link or reference end: code or test, route, record,
  or another target (a requirement is named by ID, version and packet).
- **Entries.** `EntryRow` shows an entry's ID, kind, MIK-R03 state, role, its code link at the locator, the
  facet for a proof, the rationale and the state's reason.
- **A decision in full (the rule carried from L13).** `DecisionCard` shows the derived status as the badge (and
  the stored status when it differs, "(recorded …)"), the context, every alternative in order with its status,
  reason, `reconsider when` and the targets it reopens on (`AlternativeItem`), what it supersedes and is
  superseded by, and what it governs. An unreadable decision is named (`Unavailable`).
- **Prose with references (ruling 2026-09-30T09:42:58, F4).** `ProseWithReferences` renders the onboarding
  Markdown with `remarkReferenceMarkers`, a remark plugin that links `[n]` only in **text nodes** of the parsed
  Markdown: a code span or fenced block holds its text in `value` and is never rewritten, and an existing link's
  text is skipped. A marker with a known reference number becomes a button that highlights and scrolls to that
  reference; `ReferenceList` lists every reference with **every** target. Absent prose is said as such;
  unavailable prose or references are named.

### Conventions

- `StateBadge` tones states (current, stale, unverifiable, superseded and so on) through `BADGE_TONE`.
- Panda CSS owns the looks.

### Invariants And Boundaries

- **Rule 5: every link is a navigation.** Nothing here keeps view state except the focused reference.
- **A decision is shown whole wherever it appears** (the rule carried from L13): every view that shows a
  decision uses `DecisionCard`.
- Proved by `KnowledgeReader.test.tsx`: the file case (six markers, reference 2 lists 3 targets, the decision in
  full), the directory case (superseded-by link), and the code-span case (`reports[0]` and a fenced
  `candidates[3]` kept, only \[1] and \[2] linked); the reviewer's mutant that also rewrites code nodes was killed.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module's own statement: every link is a navigation. [1]
- The navigation context. [2]
- A part that could not be read, named. [3]
- Record, path and code links. [4]
- Any link or reference end, as a navigation. [5]
- One entry with its state and code link. [6]
- An alternative with its reason and `reconsider when`; the decision header with the derived status. [7]
- A decision in full, wherever it appears. [8]
- Markers linked in text nodes only (F4). [9]
- The reference list and the prose with its markers. [10]
- The file case and the code-span case. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
