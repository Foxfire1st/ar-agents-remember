# dashboard/src/panels/detail-panel/skeletons.tsx

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Own shared bounded document blocks, own-view scroll state and the relocated decision preview; the form readers compose their fixed order elsewhere.

## Code Commentary

`useDocView` captures the actual scrolling DetailPanel element at view entry, falling back to window only when no panel scrolls. It saves that owner's offset, opens at the top, and restores the same owner on Back on the next animation frame. Escape delegates to Back. The captured owner must not be recomputed after view replacement changes scrollability. The D229 refactor makes Back a stable `useCallback` reading those saved refs; the Escape listener depends on the open-view boolean and Back, so switching between open views does not reinstall it.

Requirements preview eight lines, registers five last-written rows and four visible columns. The register all-link exists even for a short table so surrounding prose remains reachable; its own view renders the complete original section body. Register cells and expanded columns retain Markdown navigation, and nested link clicks do not toggle a row. Long prose has both line and character bounds; a single huge paragraph cannot evade them.

`DecisionPreview` preserves newest-first parsed-time ordering, five authored decisions and an omitted-entry link naming authored versus total counts. Product records are omitted from the preview, not erased from the whole reader. Open questions remain under Decisions, and introducing prose alone keeps a meaningful Decisions block. Further notes name free-form section sizes; form-specific classification prevents a second structured index or objective echo. The change-set chrome waits until body loading has settled.

## Boundaries

Shared visual primitives live in pageParts.tsx; the head, task-only blocks and index groups have separate owners. This module neither selects the document nor changes task/knowledge state. Scroll-call unit observations do not substitute for real browser restoration evidence.

## Evidence

- Own views save and restore the same actual scroll owner selected at entry. [1]
- The moved decision preview preserves five authored newest entries and both-count link semantics. [2]
- Short and long register previews retain a link to every original section byte. [3]
- Complete register section prose is rendered in its own view, not reconstructed from preview rows. [4]
