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

It resolves this review’s leaf explainer or placeholder when its exact address is available, retaining ordinary document chat for other targets; pending or unknown task identity does not select an architect. Width persistence is separate from the intentionally unremembered review-chat visibility.

## Evidence

- Exact task matching and named pending/unknown states [1]
- Width classes, gutters and placement [2]
- Tray coupling and target-scoped visibility [3]

A review with repository, master and leaf supplies a memoized explainer address plus planned/live-or-recorded and comparison-number context; a review without all three keeps the document chat. The leaf's stage comes from the exact shared task entry. The matching first-request event opens the existing column but starts nothing, and task hydration/missing-task states still prevent accidental Projects Architect binding. The default review recipient is the explainer or its placeholder; the Worker is never selected by default.

- A review with repository, master and leaf supplies a memoized explainer address plus planned/live-or-recorded and comparison-number context; a review without all three keeps the document chat. The leaf's stage comes from the exact shared task entry. The matching first-request event opens the existing column but starts nothing, and task hydration/missing-task states still prevent accidental Projects Architect binding. The default review recipient is the explainer or its placeholder; the Worker is never selected by default. [4]
