# dashboard/src/dev/taskSkeletonPage.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Mount the real DetailPanel and locally selected NotesReaderViewer artifact pane as an isolated developer demonstration surface for the reader forms and their artifact hand-off.

## Code Commentary

The form query selects a seeded sprint, master or task. long=1 deliberately augments the seeded representatives with synthetic long content; rich=1 replaces them with the fully invented taskSkeletonDocs set and installs only its supported response mocks. A requested width gives the panel its own container width, rather than pretending the window width is the cockpit middle column.

The demo applies its selected projection before mounting the DetailPanel. Rich-mode requests not covered by the fixture still use the original fetch, and the override is restored on unmount. The fixture choice/augmentation must stay disclosed when interpreting a screenshot or interaction. DetailPanel hands artifact targets to local state through onOpenNotes; an open artifact replaces the panel with NotesReaderViewer, and Back clears that target. This sandbox seam adds no production route; its onSelectNote callback is a no-op.

## Boundaries

This developer page is not a production route, older-server proof, real native task or generated evidence verdict. Using the real reader demonstrates its mounting seam, not every acceptance condition.

## Evidence


- The selected projection precedes reader mount, the rich fetch override is restored, and local artifact state switches between DetailPanel and NotesReaderViewer. [1]
