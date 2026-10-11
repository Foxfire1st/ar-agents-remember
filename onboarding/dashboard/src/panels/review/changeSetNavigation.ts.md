# dashboard/src/panels/review/changeSetNavigation.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Open the change-set viewer from the reviewer (MIK-R86): one context carrying the opener for a change filter, an optional path and a code-or-memory kind.

## Code Commentary

- `OpenReviewChanges` opens the viewer on a `ReviewChangeFilter` with an optional path and kind; `ReviewChangeSetNavigation` provides it (or null where no viewer is offered) to the rail destinations, the worklist view and the center's change openers.

## Evidence

- Viewer opener for a filter, path and kind [1]
- Context shared by rail, worklist and center [2]
