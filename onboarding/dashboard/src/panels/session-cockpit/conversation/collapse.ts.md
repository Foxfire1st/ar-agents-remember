# dashboard/src/panels/session-cockpit/conversation/collapse.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/collapse.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

Pure **visual grouping** of consecutive identical-summary unknown-vendor evidence (design §12.2;
round-1 F10). A brand-new codex session can emit a wall of identical `unknown vendor event` rows; §12.2
permits summarizing consecutive items visually AS LONG AS each underlying item stays addressable and
identity is never mutated. It produces a flat `DisplayRow[]` the feed virtualizes.

## Code Commentary

### Logic

- **`DisplayRow`** (L12-L14): either a passthrough `item` row or an `unknown-run` row carrying the run's
  members, a summary, and the first member's `ordinal`.
- **`unknownVendorSummary`** (L16-L21): derives the run key from the first `unknown-vendor` block's
  `vendorType: safeSummary` (fallback `unrecognized vendor event`).
- **`groupUnknownVendorRuns`** (L23-L55): scans items; a maximal run of `unknown-vendor` items sharing
  the same summary and of length `>= MIN_RUN` (3) collapses to one `unknown-run` row keyed by the first
  member's `itemId`, with `ordinal = run[0].globalOrdinal`; every other item (and short runs) passes
  through as its own `item` row.

### Invariants And Boundaries

- Identity is NEVER mutated — members keep their own itemId/ordinal and stay individually addressable
  (the feed can expand the run to list them).
- Only runs of ≥3 identical-summary unknown-vendor items collapse; a mixed or short run stays expanded.
- The function is pure (no store/DOM), so it is unit-testable and virtualization-safe.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The pure run-grouping and its `DisplayRow` output. | L12-L55 | [collapse.ts](collapse.ts) |
| The `ConversationItem` + `unknown-vendor` block types it reads. | — | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The feed that renders the grouped rows and expands runs. | — | [ConversationTimeline.tsx](ConversationTimeline.tsx) |
| The pure-grouping proof. | — | [collapse.test.ts](collapse.test.ts) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the pure unknown-vendor run
  collapse — a run of ≥3 identical-summary events folds to one de-emphasized addressable row (first
  ordinal as posinset), identity never mutated (F10). Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
