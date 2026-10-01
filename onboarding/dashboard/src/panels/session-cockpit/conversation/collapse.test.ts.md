# dashboard/src/panels/session-cockpit/conversation/collapse.test.ts

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The pure-grouping proof for `collapse.ts` (design §12.2, round-1 F10): it pins that consecutive
identical-summary unknown-vendor evidence collapses to one expandable display row while every other
item passes through unchanged and identity is never mutated.

## Code Commentary

### Logic

Three cases over `groupUnknownVendorRuns`:

- **collapse a run of ≥3** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:24-24): a `[message, unknown×3, message]` sequence maps to
  `[item, unknown-run, item]`; the run holds all three members and its `ordinal` is the FIRST member's
  server `globalOrdinal` (posinset honesty — the collapsed row advertises the run's starting ordinal).
- **do NOT collapse a short run (<3)** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:24-24): two consecutive unknown-vendor items stay as two
  separate `item` rows, each keeping its own article.
- **do not merge different summaries** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:24-24): two runs of three with different `safeSummary`
  values yield two distinct `unknown-run` rows — grouping is by identical summary only.

### Invariants And Boundaries

- The grouping is pure/deterministic and never mutates item identity; a collapsed run remains fully
  addressable through its member list (each keeps its `itemId`/ordinal).
- The `MIN_RUN = 3` threshold and the "first member's ordinal" rule are the exact posinset-honesty
  contract the feed relies on.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The pure grouping function under test. [1]
- The item wire type the fixtures build. [2]
- The timeline consumer that virtualizes the grouped display rows. [3]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
