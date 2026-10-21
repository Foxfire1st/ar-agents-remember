# mcp/tests/test_reconsideration_repoint.py

## Governing Overview

[tests route overview](overview.md)

## Current source account — the judged re-point of a fired link

Each case writes a `still_rejected` row through the real writer over the surfacing fixture, with `repoint: [{link, path, locator}]` naming the 0-based position of a fired `reconsider_on` link. The admitted case removes the symbol the link names, writes the row, and finds the link at the new target, the decision's revision at 2, and the stored row's `repoint` entry carrying `before` (path and the old symbol) and `after` (the new symbol with its content); the report's note names the link, both targets and the reason, and a recompute reports the item satisfied by that row.

A rerun of the same row writes the same bytes, records nothing and bumps nothing. On a two-link item only the named link moves while the other refreshes as today. A `repoint` on a link whose fired target still maps is refused as `the fired target maps to C` with the advice to remove the re-point; a link re-authored by hand is refused with the advice to restore its base target in `records` or raise; a raise carrying a re-point is refused as `a raise carries no 'repoint'` with no question published. A present `refresh_not_current` entry is answered by a re-point that must name the item in its `items`, records the target the item fired on as `before`, and refuses an intervening answer rather than overwriting it. The stored shape refuses a re-point on a raise, a target without `path`, and a link listed more than once.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- A `still_rejected` row re-points the fired link, bumps the revision once, records both targets with content, and satisfies the item [1]
- The stored row refuses a re-point on a raise, a target without `path`, and a link named twice [2]
