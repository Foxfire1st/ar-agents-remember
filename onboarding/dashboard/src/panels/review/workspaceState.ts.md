# dashboard/src/panels/review/workspaceState.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Mounted review display state and selection intent.

## Code Commentary

Own chosen family/member, query, layout, full-file choice, opened path, Worklist view, center ref, focus request and numbered tree intent. Initial layout uses max-width 40rem once: inline on narrow, split above; subsequent user choice is not overridden by resize. beginSelection increments intent and carries keep. Choosing a row leaves Worklist and reveals common center only above narrow width; narrow choice does not reset page top. openFromCenter/closePath remember and restore opener focus, whereas setOpenPath is focus-neutral for marker follow/return. Choices survive rerenders while the hook owner stays mounted, not arbitrary component remounting. Subject identity/read retention belongs to callers; this local state is neither persisted nor server authority.

## Invariants And Boundaries

This is the inspected source contract, not an execution certificate. Parent and direct callers retain authority for identity, reads and state.

## Evidence

- FocusRequest declares the originating element, numbered intent and optional scroll/answered flags; this interface alone does not enforce their consumption. [1]
- WorkspaceState declares local display values, callbacks, center/focus refs and tree intent; it is not server authority or persistent storage. [2]
- The mounted hook owns display state, numbered selection intent, initial media-query layout and focus-neutral versus focus-restoring path callbacks. [3]
- Revealing a selected center skips narrow screens and otherwise resets the containing review surface scroll, without moving focus here. [4]
