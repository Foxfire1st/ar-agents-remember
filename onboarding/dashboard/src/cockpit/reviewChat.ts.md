# dashboard/src/cockpit/reviewChat.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Hold the review page’s chat-column selection, visibility, width and placement while reusing the shell’s right rail.

## Code Commentary

### Logic

reviewChatTask matches leaf id, repository and master folder against the shared task map. Before hydration it returns pending; an absent task after hydration returns unknown with explicit text.

useReviewChat holds openFor by the review-target object, so a different target, leaving and reopening, or reloading starts closed without storing visibility. Widths are stored separately above 1600px and at or below it, with 500/420px defaults and 14/12px gutters.

Placement is grid from 1440px, overlay below it, and narrow at the shell’s 40rem breakpoint. Expanding the tray opens the column; a first pick while closed defers its default target until the column can show its chat, and leaving clears that wait.

### Invariants And Boundaries

It resolves only this review’s task chat; pending or unknown task identity does not select an architect. Width persistence is separate from the intentionally unremembered review-chat visibility.

## Evidence

- Exact task matching and named pending/unknown states [1]
- Width classes, gutters and placement [2]
- Tray coupling and target-scoped visibility [3]
