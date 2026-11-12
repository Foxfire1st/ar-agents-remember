# dashboard/src/cockpit/launcherDefaultsMemory.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The launcher's memory of the role defaults a reviewer last settled for a scope.

## Code Commentary

Reopening the launcher offers the choices the reviewer last settled for that role and document scope instead of empty ones, and the memory is per scope, so one role's choices cannot appear as another's. Forgetting clears them all, which is what a sign-out does.

## Boundaries

The obligation above is the whole of what this file must keep true; the route account says what the surrounding surface promises.

## Evidence

- Reopening the launcher offers the choices last settled for that role and scope, not empty ones. [1]

- One scope's remembered choices cannot be read as another's. [2]
