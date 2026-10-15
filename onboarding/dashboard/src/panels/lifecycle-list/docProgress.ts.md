# dashboard/src/panels/lifecycle-list/docProgress.ts

## Governing Overview

[Area overview](../overview.md)

## Purpose

Adapt a task document’s existing progress facts into the sidebar’s numeric figure and noun.

## Code Commentary

Non-master documents delegate to taskStepProgress and use Steps done. Masters delegate to subTaskProgress, retain a separate discarded default of zero and use Tasks completed.

The adapter does not recount nested work, author major-step completion or decide lifecycle readiness. Numeric progress and the sidebar’s cached step-dot payload are distinct presentation inputs.

## Evidence

- Progress adaptation delegates to existing task/master helpers and keeps discarded facts separate. [1]
