# dashboard/src/panels/review/explainer/StalePartsList.tsx

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The trusted record of what is stale against the bound comparison: each part's title and reason, the true total, stale grades, and the selective regeneration press.

## Code Commentary

- The list is drawn from the host's own staleness answer, outside the frame; marks the page draws for itself are advisory and change nothing here.
- Each part carries its title and its reason, and the reasons stay outside the frame; the header states the true count, `none`, or `unreadable`.
- When only grades are stale the body says so; when nothing is stale it says every claim's basis still resolves; when staleness cannot be read it claims no part current.
- The footer adds how many more parts are stale than are listed, and offers regeneration only when something is stale and a press was supplied.
- The regeneration button is disabled while its press runs, and a failed press shows its own words instead of silence.

## Evidence

- The box carries the counted total, the listed count and the stale-grade count, and states the trusted nature of the list [1]
- Parts are listed with title and reason; grades-only, nothing-stale and unreadable each get their own sentence [2]
- The header reads unreadable, none or the counted number rather than a zero [3]
- The summary keeps the true count, the remainder and whether anything is actually stale [4]
- The footer adds the unlisted remainder, offers regeneration only when something is stale, and names a failed press [5]
