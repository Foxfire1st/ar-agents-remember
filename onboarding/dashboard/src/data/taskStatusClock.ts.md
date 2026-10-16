# dashboard/src/data/taskStatusClock.ts

## Purpose

One display clock for visible task-status words.

## Code Commentary

The first subscriber starts a 10-second interval; all visible subscribers observe one instant. Last unsubscribe clears it; inactive/server readers return undefined. Time labels do not infer stage or activity.

## Governing Overview

[Area overview](overview.md)

## Evidence

- Implementation [1]
