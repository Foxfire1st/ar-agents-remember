# dashboard/src/panels/detail-panel/seriesNotes.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The task-notes behavior suite split from `DetailPanel.test.tsx` by the
260731-EFA-L8 test split. Since L126 it pins the task page's Notes line for the
doc's own series (not the retired L9 series-notes list rendering): the folder is
fetched for the doc's own series, one resolution request carries the doc's
references, and no list is ever drawn. The L9 list-era prose below is superseded;
the retired whole-tree list suite was deleted with its endpoint (see the folder
suite), while this suite is collected live source asserting current behavior.


## 260831-CCR-L23 Kind-Tagged Open Payload

The series-notes click expectation now asserts the discriminated artifact target:
`onOpenNotes` fires `{ kind: "notes", repo, master, path }`.

## Code Commentary

### Logic

Renders the detail panel for a leaf doc and asserts: the Notes line appears via
`notes-root-count` (not a "Series notes" list); the folder URL carries the doc's
own repo/master with `path=&offset=0`; no report-path row is drawn
(`queryByText` null); the notes-file reference is an openable link (click fires
`onOpenNotes` with the notes target) while the code-path reference stays plain
text (`note-ref-2` null).

### Invariants And Boundaries

Live L126 assertions (folder fetch, Notes line, reference links); the L9
list-rendering assertions are superseded, not preserved.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The series-notes suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.
