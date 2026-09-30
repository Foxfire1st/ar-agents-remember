# mcp/src/agents_remember/models/knowledge/review_lane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/review_lane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:06:33+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The vocabulary of the unexplained-changes lane (MIK-R32) and the validators that make its answers reconcile.** It
fixes the three shapes the lane is served in, over one comparison of four Git trees, snake_case on the wire:

- `ReviewLaneSummary`: the bounded entry count (file buckets only), carried on the changed-intent summary;
- `ReviewUnexplainedLane`: the two destinations of the reviewer's tree, the bucket totals, the unmeasured scope and
  every measured path's bucket (`paths`);
- `ReviewFileClassification`: the one per-file response the triage badges (MIK-R33) and the per-hunk markers
  (MIK-R34) read.

The application owner is `application/review_unexplained_lane.py` over `application/review_lane_classification.py`.

## Code Commentary

### Logic

- **Literals.** `LaneSideName` (`before`, `after`); `LaneBucket` (`attributed`, `unexplained`,
  `attribution_unknown`); `LaneHunkClass` (`linked`, `unexplained`, `attribution_unknown`); `LaneRangeReason`
  (`recorded_blob_mismatch`, `path_absent`, `unresolved`, `unsupported_locator`, `unreadable`);
  `LaneUnknownReason` (`knowledge_unavailable`, `range_not_supplied`); `LaneMembershipState` (`member`,
  `before_only`, `removed_or_reassigned`, `confirmed_no_family`, `membership_unknown`); `LaneGateLinkage`
  (`linked`, `unexplained`, `unknown`).
- **Hunk facts.** `ReviewLaneSpan` is one side of a zero-context hunk (`start`, `count`; a zero count means the other
  side's lines sit after `start`, as Git prints it). `ReviewLaneHunk` carries both spans, its class, `links` and
  `unknown`. `ReviewLaneLink` names the side, entry ID, kind, a proof's `facet`, the invariant with
  `invariant_key`, its revision on that side with `invariant_revision_key`, the range and the family occurrences
  (`ReviewLaneFamilyOccurrence`: family, `family_key`, family revision, membership state). `ReviewLaneUnknown`
  names the side, reason, detail and every withheld entry.
- **File facts.** `ReviewLaneEntryRange` is one entry at the path on one side with its range or its reason.
  `ReviewLaneSide` is one side's path, blob, knowledge state, detail and entries. `ReviewLaneNonText` is a
  file-level change's content state, mode flag and the gate's linkage. `ReviewLaneCounts` counts the hunks per
  class.
- **Lane shapes.** `ReviewLaneFile` is one listed file (bucket, reason, counts, non-text fact and
  `unknown_reasons`). `ReviewLaneDestination` is one destination (`files`, `bucket_files`, `attributed_files`,
  `hunks`, `non_text`). `ReviewLanePath` is one measured path and its bucket (ruling Q1).
- **Reconciliation validators:**
  - an entry either supplies a range or names why it supplies none (`_range_or_reason`);
  - a hunk is linked exactly when it has links, and attribution-unknown exactly when it has reasons
    (`_facts_follow_the_class`);
  - every hunk takes exactly one class (`_classes_sum_to_hunks`);
  - a destination lists exactly its bucket files and attributed files (`_files_are_the_totals`);
  - a lane or summary carries totals only when measured (`counted`, or `measured`/`partial` for the lane), and then
    all four with the three buckets summing to the changed total (`_totals_problem`);
  - a measured or partial lane lists exactly `changed_total` paths, an unavailable one none (`_buckets_reconcile`);
  - a summary without counts says why (`_counts_only_when_counted`).

### Conventions

- Text fields are capped with the knowledge base's bounds (`REFERENCE_MAX_LENGTH`, `PROSE_MAX_LENGTH`,
  `PATH_MAX_LENGTH`), and a side's blob must match `GIT_OBJECT_PATTERN`. The application clips reasons and
  refusal input so a valid request never trips a cap (review R1 F2 and F4).
- `linked` asserts intersection only: never coverage, correctness or preservation.

### Invariants And Boundaries

- **An unmeasured change set can never read as zero** (MIK-R32 rules 9 and 11): `partial` and `unavailable` carry no
  totals, enforced by `_totals_problem`.
- **The three buckets sum to the changed-file total**, and hunk totals never change a file total.
- Nothing here is an assessment, an approval or a suggested explanation.

### Todos

No additional work is asserted by this card.

## Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R32@v1` (adopting `ICR-R33@v1`) and its rulings in `32_unexplained-changes-lane.json`; they live outside the code
and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The three shapes, the buckets and the hunk classes, in the module's own words. | "fixes the three shapes the lane is served in"; "intersection only -- never coverage, correctness or preservation." | mcp/src/agents_remember/models/knowledge/review_lane.py:1-34 |
| The lane's literals. | `LaneBucket`; `LaneHunkClass`; `LaneRangeReason`; `LaneMembershipState`; `LaneGateLinkage` | mcp/src/agents_remember/models/knowledge/review_lane.py:74-89 |
| One entry's range or reason. | `ReviewLaneEntryRange`; `_range_or_reason` | mcp/src/agents_remember/models/knowledge/review_lane.py:103-119 |
| Family occurrences and links with their keys. | `ReviewLaneFamilyOccurrence`; `ReviewLaneLink` | mcp/src/agents_remember/models/knowledge/review_lane.py:122-155 |
| A hunk's facts follow its class. | `ReviewLaneUnknown`; `ReviewLaneHunk`; `_facts_follow_the_class` | mcp/src/agents_remember/models/knowledge/review_lane.py:158-182 |
| One side, the non-text fact, and the counts per class. | `ReviewLaneSide`; `ReviewLaneNonText`; `ReviewLaneCounts` | mcp/src/agents_remember/models/knowledge/review_lane.py:185-220 |
| The per-file response and one listed file. | `ReviewFileClassification`; `ReviewLaneFile` | mcp/src/agents_remember/models/knowledge/review_lane.py:223-249 |
| A destination lists exactly its totals; one path and its bucket. | `ReviewLaneDestination`; `ReviewLanePath` | mcp/src/agents_remember/models/knowledge/review_lane.py:252-278 |
| The lane reconciles, with every measured path listed once. | `ReviewUnexplainedLane`; `_buckets_reconcile` | mcp/src/agents_remember/models/knowledge/review_lane.py:284-312 |
| The entry's count, never a zero when unmeasured. | `ReviewLaneSummary`; `_totals_problem` | mcp/src/agents_remember/models/knowledge/review_lane.py:318-361 |
| Where the summary and the lane travel. | "attribution: ReviewLaneSummary"; "lane: ReviewUnexplainedLane" | mcp/src/agents_remember/models/knowledge/review_intent_summary.py:108-108; mcp/src/agents_remember/models/knowledge/review_trees.py:262-262 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new model module MIK-R32 adds, recording ruling 2026-09-30T12:19:20 Q1 (`ReviewLanePath` and the `paths` validator) and review R1 F2/F4 (the caps the application now clips to). The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
