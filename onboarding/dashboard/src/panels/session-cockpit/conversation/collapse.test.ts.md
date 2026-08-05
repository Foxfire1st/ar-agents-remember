# dashboard/src/panels/session-cockpit/conversation/collapse.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/collapse.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The pure-grouping proof for `collapse.ts` (design §12.2, round-1 F10): it pins that consecutive
identical-summary unknown-vendor evidence collapses to one expandable display row while every other
item passes through unchanged and identity is never mutated.

## Code Commentary

### Logic

Three cases over `groupUnknownVendorRuns`:

- **collapse a run of ≥3** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:25-39): a `[message, unknown×3, message]` sequence maps to
  `[item, unknown-run, item]`; the run holds all three members and its `ordinal` is the FIRST member's
  server `globalOrdinal` (posinset honesty — the collapsed row advertises the run's starting ordinal).
- **do NOT collapse a short run (<3)** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:41-44): two consecutive unknown-vendor items stay as two
  separate `item` rows, each keeping its own article.
- **do not merge different summaries** cit:([`groupUnknownVendorRuns`], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:46-58): two runs of three with different `safeSummary`
  values yield two distinct `unknown-run` rows — grouping is by identical summary only.

### Invariants And Boundaries

- The grouping is pure/deterministic and never mutates item identity; a collapsed run remains fully
  addressable through its member list (each keeps its `itemId`/ordinal).
- The `MIN_RUN = 3` threshold and the "first member's ordinal" rule are the exact posinset-honesty
  contract the feed relies on.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pure grouping function under test. | `groupUnknownVendorRuns` | dashboard/src/panels/session-cockpit/conversation/collapse.ts:23-55 |
| The item wire type the fixtures build. | `ConversationItem` | dashboard/src/data/conversation/types.ts:158-176 |
| The timeline consumer that virtualizes the grouped display rows. | `groupUnknownVendorRuns` | dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:357-357; dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:462-462 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: converted the three case prose
  citations to cit form (25-39, 41-44, 46-58) and normalized the 3 reference rows (collapse.ts
  23-55, types.ts 158-176, ConversationTimeline.tsx 357 + 462). Zero findings remain.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the F10 collapse
  proof — ≥3 identical-summary unknown-vendor runs collapse to one row keyed to the first member's
  server ordinal, short runs and differing summaries do not merge, and identity is never mutated.
  Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
