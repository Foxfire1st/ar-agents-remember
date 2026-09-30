# mcp/tests/test_reconsideration_surfacing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_reconsideration_surfacing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:22:59+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4`|
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**The MIK-R14@v2 cases (29 collected): reconsideration surfacing over real Git code and converted memory
repositories.** The fixture is MIK-R08's (`test_knowledge_worklist.World`) plus two decisions in K_B: D18
(`DEC-D18TXT`: the rejected "Canonical SQLite" reconsidered on an assumption record, the deferred "Both, kept in
sync" on a symbol anchor (`third` in `pkg/review.py`) and on the requirement endpoint `MIK-R21@v1`) and D12
(`DEC-D12RTE`: its rejected alternative reconsidered on a family and on D18 itself). A case commits a code candidate
C and a memory candidate K_C and computes the leaf's worklist; the writer cases write the rows as leaf
`260928-MIK-L99` through the real writer, and every answered item is checked against the stored predicate the gate
uses.

## Code Commentary

### Logic

- **Helpers.** `decision`, `assumption`, `d18`, `d12` build canonical records; `world` commits them into K_B;
  `_manifest` writes an `approved-requirement-corpus` manifest and `_task` the owning task with its v1 packet;
  `_v2_approved` adds an approved v2 with its packet; `_candidates`, `_triggers` and `_links` read the worklist's
  items and `reconsideration.links` summary; `FakeQuestions` stands in for the task owner (checks, appends, or refuses
  either); `_write` runs `write_knowledge` with `questions` and `worklist`; `_next_leaf` lands the leaf's memory
  (history file set aside) as the next leaf's base; `_reauthor_link` edits K_C's D18 link in the working tree;
  `_write_twice`, `_assert_refreshed_once` and `_assert_rerun_after_recompute` pin the rerun rule;
  `_approve_v3`, `_assert_names_both_versions` and `_assert_refused` serve the R4/R5 cases.
- **Cases, by rule and ruling:**
  - rule 2, the manifest lookup: v10 is newer than v2 by the integer after `v`, a draft and a superseded entry do not
    count, another ID is `not_approved`, a missing or wrong-format manifest is `unknown`;
  - rule 1, the triggers: a revised assumption (the packet's conforming example; an unchanged tree raises nothing),
    a `rerouted` row (and `no_impact` does not fire), a linked anchor `touched` and `moved_or_absent` (and `carried`
    does not fire; the link never joins `entries`), a requirement endpoint only on a newer approved version (no
    manifest, an unresolved endpoint or no coordination root never fires);
  - rule 3, one hop: D18 under reconsideration raises nothing for D12, whose link notes "one hop";
  - rules 4 and 5, the rows: `still_rejected` answers the item and the stored predicate agrees, with the writer's
    refusals (`no_impact`, an extra `effect`, the chosen alternative, an index out of range, an unknown decision);
    `raise` sets `under_reconsideration` at revision 1 and appends the question, and is refused writing nothing
    without a task owner, on a check refusal and on an append refusal; a real `task_doc` append keeps the earlier
    question, re-renders the `.md`, is a dry run under `check`, is idempotent, and refuses a leaf with no document;
  - L13's carried decision: a reorder of linked alternatives is refused (`R14.1`), a reword in place and an append
    pass, and both loops of `moved_linked_alternatives` are exercised; the row and item kinds are registered;
  - ruling 04:37:56: a route target fires only through a retiring row (Q1); a superseded decision is listed skipped
    (Q5); `still_rejected` re-points a persistent requirement link once and re-anchors a linked anchor so it stays
    live (Q2/Q3);
  - ruling 05:31:11: only fired links are refreshed and a line range is mapped through the diff (F1), an unmappable
    range or a row naming another item refuses, a stale link anchor raises `anchor_stale` (F3), the re-point takes the
    item's version (F4); the decision's revision goes to 2 (F2);
  - ruling 06:17:11: a re-authored, lookalike or moved link refuses (N1, N2);
  - ruling 07:13:54 (R3-1): reruns after a requirement or anchor refresh are written with no second bump;
  - rulings 10:05:18 and 10:39:15 (R4): a rerun after more code changes carries the anchor; committed lookalikes and
    re-authors stay refused; a link reverted after a committed refresh is refreshed again; a version approved after
    the refresh needs the new item named;
  - rulings 11:01:18 and 11:24:12 (R5): a second change inside the anchored range needs the new item, and a stale
    worklist is refused as a stale item; a curator-set unapproved version (v4) and an anchor re-pointed to other code
    are re-authored.

### Conventions

- The module is in the `unit-regression` lane (`test-evidence-lanes.toml:128`); the evidence catalog derives it as a
  consumer of `fixtures/repository_profiles/node/package-lock.json` (`evidence-lifecycle.toml:839`, the Forty-second
  deliberate re-pin).
- Refusal cases assert the decision file is byte-identical afterwards.

### Invariants And Boundaries

- The worker and reviewers removed each guard in turn (the one-hop guard, the refresh call, the superseded skip,
  `newer_than`, the append order, the second reorder loop, the stale handling, the line-range mapping, the item-ID
  check, `_place_record`, the N1 key check, `alternative != index`, the idempotent branches, the carried and
  new-change states, the R5-2 upper bound, the stale-item check, the packet comparison): each removal fails at least
  one case here.
- **Accepted note R6-2 (ruling 11:53:13):** the module is 1,172 lines, 28 under the 1,200 limit; the next addition
  splits it (for example into surfacing and writer-refresh cases).

### Todos

- Split the module before the next case is added (R6-2).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json`; they live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: the fixture's two decisions and the case shape. | "MIK-R14@v2: reconsideration surfacing over real Git code" | mcp/tests/test_reconsideration_surfacing.py:1-7 |
| D18's three links: an assumption, a symbol anchor and a requirement endpoint. | `d18` | mcp/tests/test_reconsideration_surfacing.py:115-127 |
| D12, reconsidered on a family and on D18. | `d12` | mcp/tests/test_reconsideration_surfacing.py:130-141 |
| The fixture world with both decisions and the assumption in K_B. | `world` | mcp/tests/test_reconsideration_surfacing.py:144-159 |
| The manifest and the owning task. | `_manifest`; `_task` | mcp/tests/test_reconsideration_surfacing.py:162-170; mcp/tests/test_reconsideration_surfacing.py:173-183 |
| Rule 2: the highest approved version by integer. | `test_the_manifest_lookup_returns_the_highest_approved_version` | mcp/tests/test_reconsideration_surfacing.py:212-231 |
| Rule 1 and the conforming example. | `test_a_revised_assumption_surfaces_the_rejected_alternative` | mcp/tests/test_reconsideration_surfacing.py:239-266 |
| Rule 1: rows, anchors and requirement endpoints. | `test_a_triggering_history_row_surfaces_and_other_dispositions_do_not`; `test_a_linked_anchor_triggers_when_touched_or_absent_and_not_otherwise`; `test_a_requirement_endpoint_triggers_only_on_a_newer_approved_version` | mcp/tests/test_reconsideration_surfacing.py:273-293; mcp/tests/test_reconsideration_surfacing.py:296-311; mcp/tests/test_reconsideration_surfacing.py:314-346 |
| Rule 3: one hop. | `test_one_hop_a_decision_change_never_chains_on` | mcp/tests/test_reconsideration_surfacing.py:349-358 |
| The task-owner stand-in and the writer call. | `FakeQuestions`; `_write` | mcp/tests/test_reconsideration_surfacing.py:366-381; mcp/tests/test_reconsideration_surfacing.py:384-402 |
| Rules 4 and 5: `still_rejected`, `raise`, and the real `task_doc` append. | `test_still_rejected_answers_the_candidate_and_the_stored_predicate_agrees`; `test_raise_sets_the_status_and_appends_the_question_or_is_refused`; `test_the_task_document_append_preserves_questions_through_task_doc` | mcp/tests/test_reconsideration_surfacing.py:417-443; mcp/tests/test_reconsideration_surfacing.py:461-479; mcp/tests/test_reconsideration_surfacing.py:503-542 |
| The reorder guard and the registrations. | `test_a_reorder_of_linked_alternatives_is_refused`; `test_the_row_kind_and_the_item_kind_are_registered` | mcp/tests/test_reconsideration_surfacing.py:561-601; mcp/tests/test_reconsideration_surfacing.py:604-611 |
| Ruling 04:37:56: route targets, superseded decisions and the refresh. | `test_a_route_target_fires_only_through_a_rerouting_or_retiring_row`; `test_a_superseded_decision_raises_nothing_and_its_links_are_listed_skipped`; `test_still_rejected_repoints_a_persistent_requirement_link_so_it_raises_once`; `test_still_rejected_reanchors_a_linked_anchor_so_it_stays_live` | mcp/tests/test_reconsideration_surfacing.py:636-665; mcp/tests/test_reconsideration_surfacing.py:668-681; mcp/tests/test_reconsideration_surfacing.py:709-742; mcp/tests/test_reconsideration_surfacing.py:745-765 |
| Ruling 05:31:11: F1, the unmappable range, F3 and F4. | `test_the_refresh_maps_a_line_range_and_refreshes_only_the_fired_links`; `test_a_range_that_cannot_be_mapped_refuses_the_row_naming_the_link`; `test_a_stale_link_anchor_raises_and_still_rejected_reanchors_it`; `test_the_repoint_takes_the_items_approved_version_not_a_fresh_read` | mcp/tests/test_reconsideration_surfacing.py:781-810; mcp/tests/test_reconsideration_surfacing.py:813-826; mcp/tests/test_reconsideration_surfacing.py:829-845; mcp/tests/test_reconsideration_surfacing.py:852-868 |
| Ruling 06:17:11: N1 and N2. | `test_a_refresh_refuses_a_fired_link_re_authored_or_moved_in_the_leaf` | mcp/tests/test_reconsideration_surfacing.py:885-916 |
| R3-1: idempotent reruns. | `test_a_rerun_after_a_requirement_refresh_is_written_and_bumps_nothing`; `test_a_rerun_after_an_anchor_refresh_is_written_and_bumps_nothing` | mcp/tests/test_reconsideration_surfacing.py:962-979; mcp/tests/test_reconsideration_surfacing.py:982-991 |
| R4: carried anchor, committed lookalikes, a reverted link, a newer approved version. | `test_a_rerun_after_more_code_changes_carries_the_refreshed_anchor`; `test_a_committed_lookalike_or_re_author_stays_refused`; `test_a_link_reverted_after_a_committed_refresh_is_refreshed_again`; `test_a_version_approved_after_the_refresh_is_named_and_needs_the_new_item` | mcp/tests/test_reconsideration_surfacing.py:1000-1017; mcp/tests/test_reconsideration_surfacing.py:1020-1039; mcp/tests/test_reconsideration_surfacing.py:1042-1055; mcp/tests/test_reconsideration_surfacing.py:1077-1093 |
| R5: a second change in the range, an unapproved version, an anchor re-pointed to other code. | `test_a_second_change_inside_the_anchored_range_needs_the_new_item`; `test_a_curator_set_unapproved_version_is_re_authored`; `test_an_anchor_link_re_authored_to_other_code_is_refused` | mcp/tests/test_reconsideration_surfacing.py:1111-1143; mcp/tests/test_reconsideration_surfacing.py:1146-1158; mcp/tests/test_reconsideration_surfacing.py:1161-1172 |
| The unit-lane row. | "mcp/tests/test_reconsideration_surfacing.py" | mcp/tests/test-evidence-lanes.toml:128-128 |
| The catalog consumer row. | "mcp/tests/test_reconsideration_surfacing.py" | mcp/tests/evidence-lifecycle.toml:839-839 |

## Cross-Repo References

No meaningful cross-repo references found: every repository, task root and coordination root the cases use is built
under `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T14:22:59+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `mcp/tests/test-evidence-lanes.toml`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. The Conventions bullet's lane-row mention moved with it (`test-evidence-lanes.toml:127` → `:128`: MIK-L32 inserted its own `unit-regression` row above this module's). No verification stamp was advanced.
- 2026-09-30T12:22:18+00:00: Generated citation repair: "mcp/tests/test_reconsideration_surfacing.py" repointed to mcp/tests/test-evidence-lanes.toml:128-128. No content impact: mechanical anchor-range projection bound to citation source snapshot d90e1a2e975376af7fa389d4799d24cecbe5d50c1e8d92b1e5b438c088e400a4; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T12:56:40+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` plus the staged delta; first curated over `b54d1b03`, then merged with L29's landed curation after the sync onto code `ce459423` / memory `a6075c76`, L29's committed lines kept byte-identical): created this card for the new test module MIK-R14 adds (29 collected cases, measured with `ast`), recording every ruling round the cases pin (04:37:56 to 11:24:12), the lane row and the catalog consumer, and the accepted note R6-2 (11:53:13).  After the sync the lane row is `:127` (L29's row at `:108` moved it). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
