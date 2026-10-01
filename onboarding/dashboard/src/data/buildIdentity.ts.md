# dashboard/src/data/buildIdentity.ts

## Governing Overview

[data overview](overview.md)

## Purpose

This module is the browser-side build-identity seam. It exposes the dashboard fingerprint embedded
by Vite at bundle time and compares it with the optional fingerprint reported by the serving
process, allowing the shell to distinguish a matching client/server pair from a stale loaded page.

## Code Commentary

### Logic

`CLIENT_DASHBOARD_BUILD` is the compile-time `__AR_DASHBOARD_BUILD__` value. The pure
`clientMatchesServingBuild` helper returns `null` when an older server omits `dashboardBuild`, and
otherwise returns exact string equality. It diagnoses identity only: the cockpit stamp adds a
reload instruction to its tooltip on mismatch; this helper does not reload the page.

### Conventions

The compile-time constant is exposed through one named export, and comparison stays pure so UI
tests can exercise identity without rebuilding or mutating browser state.

### Invariants And Boundaries

- An absent server fingerprint is unknown compatibility, not a mismatch.
- Exact fingerprint equality is the only positive match signal.
- This module does not fetch state, mutate browser location, or infer identity from commit hashes.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

### 2026-07-24 Curator Delta

`servingCommitLabel` now appends `*` when the serving checkout was dirty at boot. The compact label
keeps the stamp readable while the cockpit tooltip supplies the explicit dirty explanation; an absent
commit still falls back to version identity rather than inventing a hash.

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources; current claims are
proven by repository source and direct consumers.

No relevant external or domain documentation is configured for this repository-local seam.

### Repo-Internal References

- The server projection still declares an optional dashboard fingerprint; the added process/source identity fields do not change the comparator's input. [1]
- Renders the comparison as a data attribute and adds a reload instruction to the mismatch tooltip. [2]
- Embeds the fingerprint into the compiled client. [3]

### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local seam.

The reviewed behavior is wholly repository-local.
