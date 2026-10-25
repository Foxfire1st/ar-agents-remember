# dashboard/src/panels/knowledge-reader/ReaderToolbar.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Owns the Knowledge reader’s one-line repository/tree/record controls, free-form commit-or-branch choice, selection banner, narrow-width Browse control and named side-read failures. The parent owns full-screen tree layout and returning to the document; this file supplies the Browse/Document button and callback.

## Code Commentary

`CommitSelect` offers published, live leaves and listed memory commits, including a URL-selected unlisted value, and disables listed unconverted commits. The added `CommitField` sends a nonblank name to the path reader at repository root, with one request in flight for that mounted field. Only a `view` answer navigates; it uses the returned selection commit when present, otherwise the trimmed name. Failures are shown; inactive completions do not navigate. No request-abortion guarantee is made.

`useRead` owns one promise for the mounted hook’s view and JSON-serialized parameters. Answer/failure is tagged by that key, old-key answers are hidden and late effect completions are ignored. The parent passes one records acquisition to lookup and the tree’s Records loader. A rejected promise remains that key’s promise; this is not a cross-remount cache or an unconditional retry/network-request promise.

The selection banner prints the supplied identities. A non-commit selection offers a pin only when the supplied `pinnedCommit` is present; this renderer does not independently measure cleanliness. `SelectionNotes` shows the supplied code note and every supplied partial-index problem in the document. `SideFailures` names choices/commit-list/record-list failures rather than turning them into an empty catalogue.

## Invariants And Boundaries

The header keeps flex-row/nowrap controls with horizontal overflow; phone widths shorten controls and show Browse. The added name field does not introduce another header row. Repository/tree navigation and record lookup retain their owners. Asynchronous reads state their own pending/failure conditions and do not write knowledge.

<details>
<summary>Historical prior account — retained, not the current contract</summary>

# dashboard/src/panels/knowledge-reader/ReaderToolbar.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The Knowledge reader's fixed single-line header and its truthful side reads (MIK-R79 rules 2 and 3):
the repository selector, the memory-tree selector, the record lookup and its open control, the
selection banner, the two count rows' counterparts in the tree, and the named failures of the reads
that feed them. The right side carries the selection's memory/code identifiers and the pin control;
"Browse" appears at phone widths to open the tree as a full screen of rows.

## Code Commentary

### Logic

- `useRead` is the one side-read primitive: it memoizes one promise per `view + selection`, publishes
  the answer only when its key still matches (an old selection's answer is hidden), and keeps a
  failure as a named value. `ReaderToolbar` calls it for the tree choices; the KnowledgeReader parent
  calls it for the record list and passes the same `load` to the tree, so the lookup and the Records
  branch share one acquisition.
- `CommitSelect` offers `published (default)`, the live leaves and the memory commits, disabling
  unconverted commits and still showing an older commit named by an opened URL. `SideFailures` names
  an unreadable tree-choices read, a non-listed commit list and an unreadable record list, beside the
  control each feeds.
- `SelectionBanner`/`SelectionNotes` name the selection kind, tree key, memory revision and code
  tree; a partial index names every file that could not be read; a clean published or leaf tree
  offers "pin" to its memory commit. `PinButton` switches the view to that commit.

### Conventions

- The toolbar is one flex line: it scrolls horizontally rather than wrapping, and labels lose their
  text at phone widths.
- Every read is a GET through `data/knowledgeReader.ts`; nothing here writes.

### Invariants And Boundaries

- **A failed side read is kept and named, never turned into an empty list.**
- **One promise per current selection:** a repo or commit change clears the old answer immediately,
  a late answer cannot be displayed, and a rerender, hide/show or Back does not add a request.
- **A pin is offered only where the tree can move** (`published` or a leaf) and only when the tree is
  clean.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the
requirement packet `MIK-R79@v1` (rules 2 and 3) with its O1 ruling; it lives outside the code and
memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- One memoized promise per view and selection; late answers never published. (historical reference 1)
- The failures of the toolbar's own reads are named beside it. (historical reference 2)
- The memory-tree selector with live leaves and unconverted commits disabled. (historical reference 3)
- The selection banner and its pin. (historical reference 4)
- The partial index and code note lines. (historical reference 5)

### Cross-Repo References

No cross-repo boundary is crossed by this file.

</details>

## Evidence

No Domain Documentation entries are configured; current repository bodies and caller boundaries supply the evidence below. The prior source-only accounts are preserved above, not promoted to a fresh execution result.

- One mounted view/parameter promise, keyed visibility and ignored inactive effect completions. [1]
- Named choices, commit-list and record-list failures. [2]
- Published/live-leaf/commit options, including disabled unconverted entries and the URL-selected value. [3]
- Supplied selection identities and a supplied non-commit pin, not a renderer-owned cleanliness measurement. [4]
- The code note and complete supplied partial-index problem list. [5]
- The added mounted name-selection field validates through a root path read and navigates only on a view answer. [6]
- One-line control layout and the narrow-width Browse callback remain separate from parent full-screen layout. [7]

- The parent’s single records acquisition feeds lookup and the Records loader. [8]
