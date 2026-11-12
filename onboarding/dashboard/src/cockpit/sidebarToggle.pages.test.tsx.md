# dashboard/src/cockpit/sidebarToggle.pages.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Specify the shared sidebar toggle’s mounted behavior across the pages that own sidebars.

## Code Commentary

### Logic

PAGES enumerates Operations left/right, Knowledge left/right, File Viewer left, change-set left and notes-reader left. The fixtures replace only change-set content and use bounded route responses.

Each page walk hides its sidebar, verifies the toggle remains outside it and focusable, checks the main column receives the width, verifies per-page/side storage, remounts with the hidden choice and shows the sidebar again.

A decisions reader with no sidebar has no toggle; the review page’s own two sides are intentionally delegated to the separate chat/tree cases.

### Invariants And Boundaries

The seven parametrized page-side walks inspect DOM/layout props in checked-in tests, not a fresh viewport measurement or execution. Review is outside this file’s walk list.

## Evidence

- Exact page-side population [1]
- Hide/reachability/width/storage/remount contract [2]
- No-sidebar exception [3]
