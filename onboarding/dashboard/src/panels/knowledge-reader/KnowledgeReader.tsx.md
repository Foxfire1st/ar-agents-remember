# dashboard/src/panels/knowledge-reader/KnowledgeReader.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The Knowledge area (MIK-R29, relaid out by MIK-R79): a read-only reader of one repository's
knowledge at any memory tree, browsed like a file explorer, needing no task.** Its address
(repository, memory tree and path or record ID) is the URL hash, so every link is a navigation and a
view can be shared. MIK-R79 makes it a full-width retained layer on the File Viewer shell: a
resizable tree pane, the document pane and an aside that is either the "On this page" outline or the
cited code. The page is one of the four product views and its state survives a tab switch.

## Code Commentary

### Logic

- **The shell.** `KnowledgeReader` composes a single-line `Toolbar`, a `PanelGroup` with the tree
  pane (`KnowledgeTree`), the document pane (`ReaderDocument`) and the aside (`CitationPane` or
  `ReaderOutline`). The phone and mid-width layouts hide panes through `data-browsing` and
  `data-picker`; "Browse" and "Document" swap the tree and the document at 40rem and narrower, while
  the 40.001–70rem band swaps the aside for the document picker.
- **The address and the answer.** `useReaderNavigation` owns the hash and the Back history;
  `useAddressAnswer` reads the address's own view and ignores an answer whose hash moved on
  (`ViewPane` shows it only when its hash still matches; a transport failure is named "The reader
  could not be reached"). `AnswerView` routes `record`, `without-proof`, `subtree`, `census` and
  `code` answers to their views and everything else to `PathView`; `NotServed` names
  `not-converted` and every other refusal.
- **One records acquisition.** The parent creates `records = useRead<RecordListAnswer>('records', …)`
  for the current repo/commit and passes `records.load` to the toolbar's lookup and to
  `KnowledgeTree`; the `useRead` memo keeps one promise per selection, so the toolbar and the Records
  branch consume the same answer. A delayed or failed list is named beside the lookup and never gates
  the header, document or path tree.
- **Citations and reading place.** `useCitationNavigation` opens a single code/test target beside the
  text on a wide screen and as its own page at 70rem and narrower; multiple targets list first in the
  citation pane. `useVisibleReaderPlace` restores the last visible position when the document becomes
  visible again, and `save`/`remember` keep the position on the browser history entry.
- **The repository catalog.** `useRepositories` lists repositories and lands on the first
  repository's root summary when the hash names none; it settles once.

### Conventions

- Reads are GETs through `data/knowledgeReader.ts`; nothing writes.
- Every document link is a navigation through `ReaderNavContext` that changes the address; a wide-screen
  citation opens in the local citation pane, a `#` fragment scrolls locally, and an external link opens
  separately.
- Panda CSS owns the looks; the pane geometry is `react-resizable-panels` with `autoSaveId`s.

### Invariants And Boundaries

- **The reader works without any task** (MIK-R29 rule 1): the Knowledge view is a product mode,
  reachable with no selected task.
- **One selection-local records acquisition serves the lookup and the Records branch**; a repo or
  commit change clears old answers, late answers cannot overwrite the current selection, and the
  document, header and path rows stay usable during a delay or a failure (MIK-R79 O1).
- **Navigation opens a document at its top and Back returns to the place left** (MIK-R79 rule 11);
  the shareable address of MIK-R29 keeps working.
- **A failed source is shown as partial or unavailable, never as empty** (`SelectionNotes`,
  `NotServed`, `SideFailures`, the transport-failure message).
- **A document's records follow its text** and no empty section is drawn (rule 7); citations open
  beside unchanged prose (rule 9).

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 1, 2, 3, 7, 9, 10, 11, 13 and 15) with its O1 ruling; it
lives outside the code and memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The full-width shell with a resizable tree, document and aside. [12]
- One selection-local records acquisition is created here and shared with the tree and toolbar. [13]
- The address's own view is read and a late answer is hidden. [14]
- A single cited target opens beside the text, or as its own page at 70rem and below. [15]
- The outline and cited code share the aside. [16]
- The tree receives the shared records loader. [17]
- The outline that navigates the document's chapters. [18]
- The cited code pane that renders the File Viewer's code primitive. [19]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
