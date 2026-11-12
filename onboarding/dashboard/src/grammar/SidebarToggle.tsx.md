# dashboard/src/grammar/SidebarToggle.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Provide the shared sidebar visibility hook, in-place panel props and accessible panel-toggle button.

## Code Commentary

### Logic

useSidebar defaults open and remembered, storing 1/0 under cockpit.sidebar.<page>.<side>. Invalid or unavailable storage uses the caller’s initial value; storage-write failure keeps the in-memory choice for the mounted page.

sidebarPanelProps removes a hidden panel from layout and reachability with display:none, aria-hidden and inert, while sidebarHandleProps hides/disables its handle without unmounting either.

SidebarToggle renders a native button with the supplied sidebar name, expanded state and controls id. Its Hide/Show title can show a key hint; the SVG divider and filled open band follow the sidebar’s left/right side.

### Invariants And Boundaries

Callers own placement and actual visibility changes. Review chat is the explicit remember:false/initial:false exception whose owner resets state for each review target.

## Evidence

- Per-page/side visibility and persistence policy [1]
- Hide in place and remove reachability [2]
- Native accessible button and side-aware icon [3]
