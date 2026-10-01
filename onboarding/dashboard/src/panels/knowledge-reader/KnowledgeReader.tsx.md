# dashboard/src/panels/knowledge-reader/KnowledgeReader.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The Knowledge area (MIK-R29): a read-only reader of one repository's knowledge at any memory tree, browsed
like a file explorer, needing no task.** Its address (repository, memory tree and path or record ID) is the
URL hash, so every link is a navigation and a view can be shared. Left: the explorer (`KnowledgeTree`). Top: the
toolbar (repository, memory-tree selector, record lookup, "without proof [under path]" and "census"). Centre:
the selection banner and the view the address names. The Cockpit renders it as the transient `knowledge` view,
labelled "Knowledge" in the mode bar.

## Code Commentary

### Logic

- **The address.** `useReaderAddress` keeps the address in state, follows `hashchange`, and `go` writes the
  hash (`readerHash`) and the state together, so reload and back keep the view. `useRepositories` lists the
  repositories (`fetchRepos`) and, when the hash names none, lands on the first repository's **root summary**
  (`path: '.'`), the bounded landing of ruling 2026-09-30T09:42:58 F2.
- **The answer.** `useAddressAnswer` reads the address's own view (`readAddress`) and ignores an answer that
  lands after the address changed (a `live` flag). `ViewPane` shows it only when its hash still matches;
  a transport failure is named ("The reader could not be reached").
- **The banner.** `SelectionBanner` names the selection kind, tree key, memory revision, code tree and its
  note (`selectionLine`), and `PartialIndex` names every file a partial index could not read. For `published`
  or a leaf, a clean tree's `pinnedCommit` is offered as "pin this view to memory …" (`PinButton`, ruling N2),
  which keeps the view and switches to that commit.
- **Which view.** `AnswerView` renders a `view` answer through `VIEWS` (record, without-proof, subtree, census,
  code; otherwise the path view). A census, code or subtree answer names its own non-view states on its own
  view. Everything else goes to `NotServed`: `not-converted` is said as such, and other refusals show their state
  and detail. Nothing is rendered as an empty view.
- **Side reads (F11).** `useRead` keeps a failed side read (the selector's `selections`, the lookup's
  `records`) as a named failure instead of an empty list; `SideFailures` shows it beside the toolbar, including
  `commitsState` when the commit list could not be read.
- **The selector.** `CommitSelect` offers `published (default)`, the live leaves, and the memory commits, with
  unconverted commits disabled ("(not converted)"); an address naming a commit the list does not hold (an older
  commit opened by URL, F10) is still shown as the selected option.

### Conventions

- Reads are GETs through `data/knowledgeReader.ts`; nothing writes. Panda CSS owns the looks.
- Every link is a navigation through `ReaderNavContext` (`readerParts.tsx`), never local view state.

### Invariants And Boundaries

- **Rule 1: the reader works without any task:** the Knowledge view is a Cockpit mode, reachable with no
  selected task.
- **A failed source is shown as partial or unavailable, never as empty:** the banner, `NotServed`,
  `SideFailures` and the transport-failure message each name what failed.
- **Preservation:** the existing panels are unchanged; the Cockpit gained one mode and one hash check.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement
packet `MIK-R29@v1` with its rulings in `29_path-based-knowledge-reader.json`; they live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The component's own statement: no task, the address in the hash. [1]
- The address in the hash, followed on `hashchange`. [2]
- The pin offered for a clean tree (N2), and the partial index named. [3]
- The banner: tree, memory revision, code tree and its note. [4]
- The view per answer, and refusals named. [5]
- The memory-tree selector, unconverted commits disabled. [6]
- Side reads kept as named failures (F11). [7]
- The address's answer, and the root summary as the landing. [8]
- The toolbar and the view pane. [9]
- The panel. [10]
- The Cockpit's Knowledge view. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
