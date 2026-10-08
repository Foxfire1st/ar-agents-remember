# dashboard/src/cockpit/role-launcher/useRoleLaunchProgress.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Reads the launcher's one working notice for an in-flight start.

## Code Commentary

While a request id is known the hook polls `/api/role-launch/progress/<requestId>` every 500 ms and maps the returned phase to "Preparing workspace…" or "Starting agent…". The working notice is disposable: if it cannot be read, the dispatch receipt stays the authority and the row falls back to the preparing label rather than inventing a state.

## Evidence

- The hook polls the exact request's notice and falls back to the preparing label when unavailable. [1]
