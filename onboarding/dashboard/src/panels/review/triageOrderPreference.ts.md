# dashboard/src/panels/review/triageOrderPreference.ts

## Governing Overview

[review route overview](overview.md)

## Purpose

Remember the page's one Sort choice in browser-local state, defaulting to Priority when no recognized stored value is available.

## Code Commentary

`sortOf` maps the earlier triage spelling to priority, accepts members of REVIEW_SORTS and uses priority for anything else. The existing review.tree-order.v1 key preserves that stored choice; authored remains an admitted sort. `readTreeOrder` also returns priority when storage is absent or throws.

The vanilla store is seeded once from browser storage. setOrder attempts to persist the chosen ReviewSort and always updates live page state, even when storage fails; useTreeOrder subscribes to that value. This is a display preference, not a server review or durable knowledge state.

## Evidence

- triageOrderPreference.ts current behavior at this source owner. [6]
- triageOrderPreference.ts current behavior at this source owner. [7]
