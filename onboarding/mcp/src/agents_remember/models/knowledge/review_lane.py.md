# mcp/src/agents_remember/models/knowledge/review_lane.py

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
  `unknown`, and an optional bounded `subject` containing the changed-line content identity at the base and candidate. An unhashable hunk leaves `subject` absent and cannot receive a grade; this does not change its attribution class. `ReviewLaneLink` names the side, entry ID, kind, a proof's `facet`, the invariant with
  `invariant_key`, its revision on that side with `invariant_revision_key`, the range and the family occurrences
  (`ReviewLaneFamilyOccurrence`: family, `family_key`, family revision, membership state and now
  `reason`). Its new validator requires a reason exactly for `membership_unknown`; the supplied
  string has length bounds but no whitespace-stripping/nonblank check. Known membership states
  must carry no reason. `ReviewLaneUnknown`
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

- **Summary and lane partials differ.** A `ReviewLaneSummary` has totals only in `counted`;
  `partial`/`unavailable` summaries have none. A `ReviewUnexplainedLane` instead carries its measured
  totals in both `measured` and `partial`, and none in `unavailable`. Both use `_totals_problem`
  with different admission predicates. The path-count check establishes list cardinality, not
  uniqueness or independent truth of each reported path.
- **The three buckets sum to the changed-file total**, and hunk totals never change a file total.
- Nothing here is an assessment, an approval or a suggested explanation.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured for this repository. The design authority is the requirement packet
`MIK-R32@v1` (adopting `ICR-R33@v1`) and its rulings in `32_unexplained-changes-lane.json`; they live outside the code
and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The three shapes, the buckets and the hunk classes, in the module's own words. [1]
- The lane's literals. [2]
- One entry's range or reason. [3]
- Family occurrences add a bounded reason exactly for unknown membership; links retain invariant/revision keys, ranges, facets and family occurrences. [4]
- A hunk's facts follow its class. [5]
- One side, the non-text fact, and the counts per class. [6]
- The per-file response and one listed file. [7]
- A destination lists exactly its totals; one path and its bucket. [8]
- The lane admits measured/partial totals and unavailable absence, checking bucket sums and the number of paths, not uniqueness of path identities. [9]
- The entry's count, never a zero when unmeasured. [10]
- The optional attribution summary travels on the intent result; lane destinations and per-file classification travel on the tree result. [11]

### Cross-Repo References

No cross-repo boundary is crossed by this file.

- A lane hunk may carry the changed-line content identity of its base and candidate in a bounded subject. An unhashable hunk has no subject and cannot receive a grade; attribution class is unchanged. [12]

