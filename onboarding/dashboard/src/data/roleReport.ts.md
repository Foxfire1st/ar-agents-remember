# dashboard/src/data/roleReport.ts

## Governing Overview

[Route overview](overview.md)

## Purpose

The small client module reads the one report of a selected role execution through the launcher's selection-addressed route.

## Code Commentary

`readRoleReport(selection, requestId)` POSTs the launcher's selection and the recorded request ID to `/api/role-launch/report`, with no path input of its own. A non-OK answer becomes a readable operation-prefixed message (the route's named refusal detail when the body carries one); a network failure names the dashboard connection. The returned content (`path`, `language`, `size`, `truncated`, `content`) is handed to the shared notes reader unchanged.

## Invariants And Boundaries

The module never builds a file path and never falls back to another file: the recorded report the route serves is the only thing it can receive. The failure text it produces is what the launcher's one line shows (MIK-R75 rule 4). It does not decide whether a report exists, and it does not interpret the report's content.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The one dashboard call to the report route; readable operation-prefixed errors keep raw parser or network text off the launcher's failure line. [1]
- A report read failure reaches the launcher as a readable line instead of `[object Object]`, a JSON parse error or `Failed to fetch`. [2]
