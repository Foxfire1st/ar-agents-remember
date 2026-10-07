# dashboard/src/panels/file-viewer/FileViewer.test.tsx

## Governing Overview

[file-viewer/ overview](overview.md)

## Purpose

`FileViewer.test.tsx` proves the File Viewer's center-tab behavior: its registration as a full-bleed
view selectable from the mode bar, keep-alive mounting across view switches, and its repository
listing calls.

## Code Commentary

### Logic

The suite mounts `CockpitShell` and drives the mode bar. MIK-R79 moved the dashboard's opening view
from Operations to Chats, so the three tests that assert the File Viewer's hidden-not-unmounted
behavior on another view now mount `CockpitShell initialView="operations"` explicitly. The assertions
themselves are unchanged: the File Viewer is mounted from the start when another view is open, stays
the same DOM node across switches, and issues one repository listing.

### Conventions

Vitest + Testing Library, as the rest of the dashboard suites; views are selected by their radio name.

### Invariants And Boundaries

The tests mount the shell on an **injected** `initialView="operations"` and bind the File Viewer's
registration, hidden-not-unmounted keep-alive and deferred catalog behavior. They do not assert the
shell's Chats default (the separate shell default-view suite owns that) and do not re-test the
Knowledge reader or the hidden pages.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The requirement packet
`MIK-R79@v1` (rule 16) fixes the opening view and the product bar; it lives outside the code and
memory repositories, so it is named here and not cited as a row.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The suite mounts the shell on Operations for its keep-alive assertions. [6]
- The mode-bar entry the tests click. [7]
- The File Viewer the tests keep mounted. [8]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
