# mcp/src/agents_remember/application/review_unexplained_lane.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_unexplained_lane.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:36:31+02:00 |
| lastVerifiedCommitHash | `d3a22213ad3124603b0210afb7e3d049c5589b82`|
| lastVerifiedCommitDate | 2026-09-30T20:52:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The three public reads of the unexplained-changes lane (MIK-R32) over one comparison of four Git trees, all
through the one classification of `review_lane_classification.py`.**

| Read | What it answers | Transport |
| --- | --- | --- |
| `lane_summary(trees)` | The entry's count: file buckets only (changed total, attributed, unexplained, unknown). It reads no hunk, no subject catalogue and no family roster. | On the changed-intent summary as `attribution` (`review_intent_summary.py`), a tree comparison only |
| `unexplained_lane(trees)` | The two tree destinations, the bucket totals and every measured path's bucket (`paths`) | `/api/review/trees?comparison=<n>&lane=files` |
| `classify_changed_path(trees, path)` | The per-file classification response (definition 7) | `/api/review/trees?comparison=<n>&file=<path>` |

The last two are dispatched by `review_tree_knowledge.py`; the route and its bounds are `serving/review_trees.py`.

## Code Commentary

### Logic

- **The entry's count.** `lane_summary` opens the lane, observes the change inventory and answers:
  - `unavailable` with the observation's detail when the inventory is unavailable;
  - `partial` with `unmeasured` (`_unmeasured`: each undecodable name in its byte form, and each path whose content
    was not classified) and **no count** when the inventory is partial;
  - otherwise `counted`, with `bucket(path)` over the sorted set of changed paths.
  A `LaneReadError` or an `apsw.Error` (an index that fails mid-read) is `unavailable` with `_UNREADABLE`'s
  sentence, never a traceback or a zero.
- **The lane.** `unexplained_lane` classifies every inventory entry (`lane.classify`) and builds:
  - the totals and a one-line `detail` (`_lane_detail`), with the partial inventory's detail appended;
  - `unexplained_changes` and `unknown_attribution` from `_destination`: the files of the bucket first, sorted by
    path, then the **attributed** files that carry the destination's class (`_carries`): a hunk of that class, or
    a non-text change whose gate linkage is `unexplained` (for `Unexplained changes`) or `unknown` (for
    `Unknown attribution`). The destination counts its bucket files, its attributed files, the hunks of its class
    across every listed file, and its non-text changes;
  - `unmeasured` on a partial lane;
  - `paths`: every measured changed path with its bucket, in path order (ruling Q1).
- **One listed file.** `_lane_file` carries the path, status, content, bucket, reason, counts, the non-text fact,
  and `unknown_reasons`: one sorted sentence per side and reason of the file's attribution-unknown hunks.
- **The per-file response.** `classify_changed_path` refuses, with `_refusal`'s typed `source_content_unresolved`,
  a path the inventory does not list, an unavailable inventory, or unreadable trees. Otherwise `_classification`
  gives the bucket and reason, both sides (`_side`: the side's path, `None` where the file does not exist since the
  inventory lists a rename as a deletion and an addition; the blob; the knowledge state; every entry with its range
  or reason, `_entry_range`), every hunk (`_hunk`, with both spans), the non-text fact and the counts.
- **Links.** `_link` gives each intersecting entry per side: its ID, kind (a proof carries its facet), the invariant
  with `invariant_key` (`text_uuid("identity", …)`), the invariant's revision on that side with
  `invariant_revision_key` (`text_uuid("revision", "<id>@<revision>")`), the supplied range, and the family
  occurrences (`_occurrences`): the keys the landed payload addresses invariants, revisions and families by, which
  the later markers (MIK-R34) need.
- **Membership states (ruling Q5, accepted; L34 may refine, and kept them as mapped).** `_membership`: an after-side occurrence is `member`;
  a before-side one is `member` when the after record still lists the invariant, `removed_or_reassigned` when the
  after record exists without it, `before_only` when the after tree holds no record of the family (and every
  family record there was read), and `membership_unknown` when the after knowledge could not be read or a family
  record there did not parse. An invariant no family lists is `confirmed_no_family` only when every family record
  of the side was read, otherwise `membership_unknown`.

### Conventions

- Every read opens the lane with `open_tree_lane` and closes it on return; nothing is cached across reads here.
- A refusal's `offending_input` is the path clipped to the refusal's 1,024-character field and its `detail` to the
  prose cap (review R1 F2, ruling 2026-09-30T13:07:38), so every path the route admits answers the typed 200.

### Invariants And Boundaries

- **Candidate invariant (not ingested): on tree comparisons, the explorer and the technical details take their
  attribution from the lane, so no two surfaces disagree.** Realized by `paths` here, then
  `laneFocus.explorerAttribution` and `laneFocus.laneAttributionFacts` on the client (rulings Q1 at 12:19:20 and
  F1 at 13:07:38). Proved by `_every_path_bucket` in
  `test_every_changed_file_takes_one_bucket_and_the_destinations_reconcile` and by the surface cases in
  `ReviewSurface.lane.test.tsx`.
- **Candidate invariant (not ingested): lane reads are bounded and validated; every answer to a validated request
  is typed.** Realized by `_refusal` (clipped input and detail), the bounded reasons of the classification module,
  and `lane_summary`/`unexplained_lane`/`classify_changed_path` turning every read failure into `unavailable` or a
  refusal. Proved by `_long_paths_are_typed_refusals` (1,025 and 4,096 characters answer 200 with a 1,024-character
  `offending_input`), `test_a_reason_names_a_bounded_number_of_entries` (300 entries: the lane still answers
  `measured`) and `test_an_unmeasured_change_set_has_no_count`.
- **An unmeasured change set is never a count or an empty lane:** `partial` names its unmeasured scope and
  `unavailable` carries only its reason (MIK-R32 rules 9 and 11).
- **Ruling Q3 (12:19:20):** a gate-held non-text change is listed under `Unexplained changes` only for an attributed
  file; in a file of unknown attribution it stays under `Unknown attribution`, marked `gate unexplained`, and is not
  listed twice. After review F3 a gate linkage over a side not read whole is `unknown`, so it lists under
  `Unknown attribution` then.
- **Ruling Q4:** an unexplained hunk in a file of unknown attribution stays in that file's `Unknown attribution`
  row with its per-class counts; the `Unexplained changes` hunk total counts only the files it lists (rule 10).
- Nothing here assesses, approves, waives or suggests an explanation (the adopted Exclusions).

### Todos

- **Resolved by MIK-L34 (review R1 F5, carried by ruling 2026-09-30T13:07:38):** every owner hunk a focused diff
  window draws, a neighbour inside its context lines included, carries its own per-hunk intent mark
  (`dashboard/src/panels/review/LaneFileFocus.tsx`, from this module's per-file response).
- **Ruling Q5 (L34 may refine the membership states): L34 kept them as mapped.** Each state maps directly onto a
  marker target, and ruling 2026-09-30T16:19:34 Q2 left the response unchanged. The dashboard's
  `hunkMarkers.unknownReason` restates `_membership` and `_occurrences`' rule for an unknown membership and names this
  module as its owner (review R1 N1): **if that mapping changes here, that sentence must change with it.**

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
| The three reads and the membership-state rule, in the module's own words. | "the entry's attribution count"; "A family occurrence's membership state compares the side's family record" | mcp/src/agents_remember/application/review_unexplained_lane.py:1-27 |
| The entry's count: buckets only; unavailable, partial or counted. | `lane_summary` | mcp/src/agents_remember/application/review_unexplained_lane.py:87-110 |
| The unmeasured scope named. | `_unmeasured` | mcp/src/agents_remember/application/review_unexplained_lane.py:113-123 |
| The two destinations, the totals and every path's bucket (ruling Q1). | `unexplained_lane`; "paths=tuple(" | mcp/src/agents_remember/application/review_unexplained_lane.py:129-155 |
| A destination: its bucket's files, then attributed files carrying its class or its gate linkage. | `_destination`; `_carries` | mcp/src/agents_remember/application/review_unexplained_lane.py:170-185; mcp/src/agents_remember/application/review_unexplained_lane.py:192-200 |
| One listed file with its unknown reasons. | `_lane_file` | mcp/src/agents_remember/application/review_unexplained_lane.py:207-220 |
| The per-file response, or the typed refusal with clipped input (review F2). | `classify_changed_path`; `_refusal` | mcp/src/agents_remember/application/review_unexplained_lane.py:226-244; mcp/src/agents_remember/application/review_unexplained_lane.py:247-255 |
| Both sides, every entry's range or reason, and every hunk. | `_classification`; `_side`; `_entry_range`; `_hunk` | mcp/src/agents_remember/application/review_unexplained_lane.py:258-313 |
| A link's keys, revision and family occurrences. | `_link`; `_occurrences` | mcp/src/agents_remember/application/review_unexplained_lane.py:316-356 |
| The membership states (ruling Q5). | `_membership` | mcp/src/agents_remember/application/review_unexplained_lane.py:359-370 |
| The lane and file reads dispatched. | "return _focused(query, trees, lane=unexplained_lane(trees))"; `_file_view` | mcp/src/agents_remember/application/review_tree_knowledge.py:122-127; mcp/src/agents_remember/application/review_tree_knowledge.py:216-230 |
| The entry's count carried on the summary. | "return summary.model_copy(update={\"attribution\": lane_summary(resolved.trees)})" | mcp/src/agents_remember/application/review_intent_summary.py:139-142 |
| Destinations and reconciliation; the entry count reads no hunk. | `test_every_changed_file_takes_one_bucket_and_the_destinations_reconcile`; `test_the_entry_count_reads_file_buckets_only` | mcp/tests/test_review_unexplained_lane.py:356-373; mcp/tests/test_review_unexplained_lane.py:430-441 |
| Links, revisions, proofs and membership states. | `test_a_linked_hunk_names_its_entries_revisions_and_family_occurrences` | mcp/tests/test_review_unexplained_lane.py:493-509 |
| Unmeasured change sets, and long paths answered typed. | `test_an_unmeasured_change_set_has_no_count`; `_long_paths_are_typed_refusals` | mcp/tests/test_review_unexplained_lane.py:596-618; mcp/tests/test_review_unexplained_lane.py:682-695 |

## Cross-Repo References

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T20:36:31+02:00 — 260928-MIK-L34 curator (staged change set on `ar/260928-mik-l34`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; reviews R1 to R3 changes-required, each followed by a fix round): **Both carried Todos are resolved** (ruling 2026-09-30T13:07:38 F5 and ruling Q5): MIK-L34 marks every owner hunk a lane window draws, a neighbour shown as context included, and kept the membership mapping as it is; the Logic heading and the Todos section record both, with the one dependency the dashboard now has on `_membership` and `_occurrences` (the restated unknown-membership reason, review R1 N1). The source file is unchanged.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T14:06:33+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`; review R1 pass-with-notes, fixes, R2 pass): created this card for the new module MIK-R32 adds, recording rulings 2026-09-30T12:19:20 Q1 (`paths` for the explorer), Q3, Q4, Q5 and Q7, review R1 F2 (typed refusal for long `file=` values) fixed at 13:07:38, F5 carried to L34, and two candidate invariants. The verification stamp is left empty: the file is new and uncommitted; closeout owns the real stamp.
