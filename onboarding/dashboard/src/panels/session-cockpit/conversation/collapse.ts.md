# dashboard/src/panels/session-cockpit/conversation/collapse.ts

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

Pure **visual grouping** of consecutive identical-summary unknown-vendor evidence (design §12.2;
round-1 F10). A brand-new codex session can emit a wall of identical `unknown vendor event` rows; §12.2
permits summarizing consecutive items visually AS LONG AS each underlying item stays addressable and
identity is never mutated. It produces a flat `DisplayRow[]` the feed virtualizes.

## Code Commentary

### Logic

- **`DisplayRow`** (cit:(["type DisplayRow"], dashboard/src/panels/session-cockpit/conversation/collapse.ts:23-23)): the declared output row type for the collapse helper.
- **`unknownVendorSummary`** (cit:(["function unknownVendorSummary"], dashboard/src/panels/session-cockpit/conversation/collapse.ts:37-37)): the declared helper for unknown-vendor summaries.
- **`groupUnknownVendorRuns`** (cit:(["groupUnknownVendorRuns"], dashboard/src/panels/session-cockpit/conversation/collapse.test.ts:24-24)): the declared grouping entry point for unknown-vendor runs.

### Invariants And Boundaries

- Identity is NEVER mutated — members keep their own itemId/ordinal and stay individually addressable
  (the feed can expand the run to list them).
- Only runs of ≥3 identical-summary unknown-vendor items collapse; a mixed or short run stays expanded.
- The function is pure (no store/DOM), so it is unit-testable and virtualization-safe.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The declared `DisplayRow` output type. [1]
- The declared pure grouping entry point. [2]
- The unknown-vendor content block type. [3]
- The `ConversationItem` wire type. [4]
- The `ConversationTimeline` feed component. [5]
- The grouping test suite. [6]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
