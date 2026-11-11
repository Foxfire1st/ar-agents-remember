# dashboard/src/panels/detail-panel/activityPhrase.test.ts

## Governing Overview

[Panels overview](../overview.md)

## Purpose

Pin the two forms of a master's child-activity phrase.

## Code Commentary

The first case gives 6 works, 0 waiting and 2 paused and expects `6 works · 2 paused`: no waiting part while nothing waits. The second gives 1 works, 3 waiting and 0 paused and expects `1 works · 3 waiting · 0 paused`: the waiting count sits between works and paused, and a zero paused count is still written. These are pure function cases; they render neither the row nor the page.

## Relationships

The cases call `activityPhrase` from `activityPhrase.ts`. The mounted row figure that renders the phrase is exercised in `lifecycle-list/hierarchy.test.tsx`.

## Evidence

- With nothing waiting the phrase is works and paused only. [1]
- A waiting count sits between works and paused, and a zero paused count is still written. [2]
