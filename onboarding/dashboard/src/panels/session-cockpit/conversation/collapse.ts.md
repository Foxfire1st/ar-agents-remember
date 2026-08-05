# dashboard/src/panels/session-cockpit/conversation/collapse.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/collapse.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

- **`DisplayRow`** (cit:(["type DisplayRow"], dashboard/src/panels/session-cockpit/conversation/collapse.ts:12-12)): the declared output row type for the collapse helper.
- **`unknownVendorSummary`** (cit:(["function unknownVendorSummary"], dashboard/src/panels/session-cockpit/conversation/collapse.ts:16-16)): the declared helper for unknown-vendor summaries.
- **`groupUnknownVendorRuns`** (cit:(["groupUnknownVendorRuns"], dashboard/src/panels/session-cockpit/conversation/collapse.ts:23-23)): the declared grouping entry point for unknown-vendor runs.

### Invariants And Boundaries

- Identity is NEVER mutated — members keep their own itemId/ordinal and stay individually addressable
  (the feed can expand the run to list them).
- Only runs of ≥3 identical-summary unknown-vendor items collapse; a mixed or short run stays expanded.
- The function is pure (no store/DOM), so it is unit-testable and virtualization-safe.

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
| The declared `DisplayRow` output type. | `DisplayRow` | dashboard/src/panels/session-cockpit/conversation/collapse.ts:12-14 |
| The declared pure grouping entry point. | `groupUnknownVendorRuns` | dashboard/src/panels/session-cockpit/conversation/collapse.ts:23-55 |
| The unknown-vendor content block type. | `ConversationContentBlock` | dashboard/src/data/conversation/types.ts:63-105 |
| The `ConversationItem` wire type. | `ConversationItem` | dashboard/src/data/conversation/types.ts:158-176 |
| The `ConversationTimeline` feed component. | "function ConversationTimeline" | dashboard/src/panels/session-cockpit/conversation/ConversationTimeline.tsx:344-344 |
| The grouping test suite. | "describe(\"groupUnknownVendorRuns" | dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:24-24 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-04T11:35:04+02:00 — 260731-EFA-L6 S18-B10 curator: applied reviewer verdict D1-D25 deterministic whole-claim repairs; corrected operative source ranges and focused assertions, removed the false Pi gate-field claim, and rechecked this card through the locked exact-document fixer/check.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the pure unknown-vendor run
  collapse — a run of ≥3 identical-summary events folds to one de-emphasized addressable row (first
  ordinal as posinset), identity never mutated (F10). Verification is pinned to the leaf base
  (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
