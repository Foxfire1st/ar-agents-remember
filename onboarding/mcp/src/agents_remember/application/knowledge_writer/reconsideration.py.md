# mcp/src/agents_remember/application/knowledge_writer/reconsideration.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The writer's side of MIK-R14 rule 4: the `still_rejected` and `raise` rows that answer a
`reconsideration_candidate`.** `Authoring._reconsideration_row` calls it to check what a row's subject names, to
compose a `raise` row's question, and to refresh the fired links on `still_rejected`; `writer.py` calls
`append_questions` before any knowledge file is written. `OpenQuestions` is the port to the leaf task document's
`openQuestions` (implemented by `open_questions.TaskDocOpenQuestions`). The curator never reverses a decision:
neither row changes an alternative, its status or the chosen option.

## Code Commentary

### Logic

- **What a subject names** (`reconsidered_alternative`): the subject must parse as `reconsider:<DEC-ID>#<i>`, the
  memory tree must hold a `decision` record with that ID, the alternative at `i` must be `rejected` or `deferred`
  (`_alternative`), and a `reconsider_on` link must address it (`_addresses`). Each failure is named ("names no
  decision record", "has no alternative 7", "only a rejected or deferred alternative is reconsidered", "no
  reconsider_on link … addresses alternative").
- **`raise`** (`raise_question`): the question is keyed by `question_key` (`[reconsider:<DEC>#<i> raised by
  <leaf>]`) and composed from the option, its status, the curator's reason, the row ID, the rejection reason and
  `reconsider_when`, ending "The decision is under_reconsideration until the developer decides." The text is
  mechanical (worker Q7); a rerun finds the key and appends nothing, so a reworded reason is not re-appended.
- **`append_questions`** runs in a committing run before any file is written; every refusal (no task owner, or the
  owner's own reason) is returned so `writer.py` refuses the whole operation.
- **`still_rejected` refresh** (`refreshed_links`, rulings 04:37:56 Q2/Q3 and 05:31:11 F1–F4). Only the links whose
  trigger fired on the answered item and is in `REFRESHED_TRIGGERS` are touched; a `record_file` or `history_row`
  link is left as it is. A fired link must still be a `reconsider_on` link of the same alternative at the same
  index (`_at`, review N2), or the row is refused "no longer a reconsider_on link of alternative …; recompute the
  worklist". The refresh target (`_refreshed_target`):
  - `requirement_version`: the endpoint is re-pointed to the item's `latestApproved` and `latestPacket` (F4: never a
    fresh manifest read); an item with no packet refuses the row ("the manifest entry names no file");
  - `anchor` / `anchor_stale`: `carry.mapped_anchor` maps a `line_range` through the zero-context diff from the
    link's recorded blob, or re-binds a symbol, at C (F1); an anchor that cannot be mapped refuses the row, naming
    `links.<i>` and asking to re-author the link in `records` first.
- **The K_B target the item fired on** (`_fired_target`, review R3-1): the base record's link at the fired position
  (`MemoryState.base_record`, which is memory `HEAD`, so K_B until the leaf commits memory) when its
  `link_target_key` still equals the fired target; else, for an anchor, the K_B anchor the facts carry
  (`facts.changed[].entry.anchor`); else (a requirement whose refresh is already committed) only the key is known.
- **The link states** (`_link_state`, `_requirement_state`, `_anchor_state`, `_refreshed_anchor_state`; reviews R3
  to R5, rulings 07:13:54, 10:05:18, 10:39:15, 11:01:18 and 11:24:12). Each fired K_C link is judged against that
  K_B target; only exact equality counts.

| State | Condition | What `_outcome` does |
| --- | --- | --- |
| unchanged (`UNCHANGED`) | the link equals the K_B target (by key when only the key is known) | refreshed; a new judgment, so `judged` is true and the decision is placed once in the leaf (F2) |
| carried (`CARRIED`) | an earlier refresh that still stands: a requirement at the item's version and packet, or an anchor whose mapping to the current C equals the refresh of the K_B target and whose content survives that mapping (R4-1, R5-1) | the carried target is written with no further bump; a plain rerun writes identical bytes (R3-1, R5-3) |
| a new change: earlier version (`EARLIER`) | a requirement refreshed earlier to a version newer than the fired one and older than the item's `latestApproved` (R4-3, R5-2 upper bound) | a plain rerun is refused naming both versions and the new item; a row naming the new item's ID in `items` re-points it (the explicit answer, 10:39:15) |
| a new change: changed again (`CHANGED`) | an anchor whose content changed again inside its range after the refresh (R5-1) | a plain rerun is refused naming the old and new content and the new item; a row naming the new item is a new judgment |
| stale item (`STALE_ITEM`) | the item's own `facts.changed[].entry.candidate.content` is not the content at the current C: the worklist predates the change (11:24:12) | refused: "recompute the worklist and answer its item" |
| re-authored (`RE_AUTHORED`) | anything else, including a curator-set unapproved version (R5-2) or an anchor re-pointed to other code | refused naming `links.<i>` and the fired target |

`_new_change` composes the two new-change refusals; `_newer` compares versions through `version_number`;
`_seen_content` reads the content the item saw at C.

- **Result.** `Refresh(links, problems, judged)`: `judged` is true when a link was newly judged, so
  `Authoring._refresh` places the decision through the record path; a carried-only refresh is written in place.
- **`CodeAtC`** bundles the code candidate's trees and per-path blobs for `mapped_anchor`.

### Conventions

- Every refusal names `links.<i>: why`, so the curator can see which link and what to do. The refusal message for
  the stale item names its own fix (accepted note R6-3).
- A `raise` leaves the links untouched: the reconsidered revision re-authors them (ruling Q2/Q3).

### Invariants And Boundaries

- **`still_rejected` refreshes only the fired link, to the judged state mapped through the diff, and refuses a link
  that was re-authored or cannot be mapped.** Candidate invariant. Realized by the `REFRESHED_TRIGGERS` filter,
  `_at`, `_fired_target`, `_link_state` and `_refreshed_target` over `mapped_anchor`; proved by
  `test_the_refresh_maps_a_line_range_and_refreshes_only_the_fired_links` (a carried range stays byte-identical;
  a touched one maps to lines 19–20), `test_a_range_that_cannot_be_mapped_refuses_the_row_naming_the_link`,
  `test_the_repoint_takes_the_items_approved_version_not_a_fresh_read`,
  `test_a_refresh_refuses_a_fired_link_re_authored_or_moved_in_the_leaf`,
  `test_a_committed_lookalike_or_re_author_stays_refused` and
  `test_an_anchor_link_re_authored_to_other_code_is_refused`, each checked by the worker's and reviewers' mutation
  runs (every guard removed fails a test).
- **Every new change to a judged target needs a new explicit answer; a rerun of the same answer is idempotent, and
  nothing absorbs an unjudged change.** Candidate invariant. Realized by the carried / new-change / stale-item
  states and the `names_item` condition; proved by
  `test_a_rerun_after_a_requirement_refresh_is_written_and_bumps_nothing`,
  `test_a_rerun_after_an_anchor_refresh_is_written_and_bumps_nothing`,
  `test_a_rerun_after_more_code_changes_carries_the_refreshed_anchor`,
  `test_a_version_approved_after_the_refresh_is_named_and_needs_the_new_item`,
  `test_a_second_change_inside_the_anchored_range_needs_the_new_item` and
  `test_a_curator_set_unapproved_version_is_re_authored`; and by review R6, which found no path that absorbs a
  change to a judged target without a new explicit answer.
- **The curator never reverses a decision.** Neither row touches `alternatives`; `raise` only sets `status`.

### Todos

- **Accepted note R6-1 (ruling 11:53:13):** a same-leaf revert of the anchored code after a refresh leaves the
  refreshed content, which never lands; the next leaf raises `anchor_stale` once (loud, not silent).
- **Recorded limit (ruling 04:37:56 Q7, review F7):** the question append and the knowledge write are two stores;
  an `OSError` between them, or a second `raise` whose append fails, leaves a question with no knowledge written. A
  rerun appends nothing twice (key prefix).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R14@v2` of task
`260928_maintained-invariant-knowledge` and its leaf document `14_reconsideration-surfacing.json` (rulings
2026-09-30T04:37:56 to 11:53:13); they live outside the code and memory repositories, so they are named here and
not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: both rows, the refresh, and the five link states it names. [1]
- The task owner's `openQuestions` port. [2]
- What a subject names: a decision, a rejected or deferred alternative, and a link addressing it. [3]
- The `raise` question and its key. [4]
- The append in a committing run; every refusal is returned. [5]
- The code candidate a refresh maps anchors to. [6]
- The link states. [7]
- What a row answers, and the refresh's result. [8]
- Only fired, refreshable links; each judged against its K_B target. [9]
- One fired link to a target or a refusal; the new-change refusals. [10]
- The K_B target: the base record's link, the facts' anchor, or the key alone. [11]
- The state dispatch and the requirement states, with the R5-2 upper bound. [12]
- The anchor states: stale item, unchanged, carried only when the content survives, changed again. [13]
- The refresh target: the item's version and packet, or the anchor mapped to C. [14]
- `still_rejected` refusals of a wrong subject or extra field. [15]
- A requirement link re-pointed once, bumped once; the next leaf raises nothing. [16]
- An anchor re-anchored; a `raise` leaves it; a second change raises a new item. [17]
- Only fired links; a range mapped through the diff (F1). [18]
- An unmappable range, or a row naming another item, refuses. [19]
- The re-point takes the item's facts (F4). [20]
- Re-authored, lookalike and moved links refuse (N1, N2). [21]
- Idempotent reruns (R3-1). [22]
- Carried after an edit outside the range; committed re-authors and lookalikes refused (R4-1, R4-2). [23]
- A newer version needs the new item named (R4-3, explicit answer). [24]
- A second change inside the range needs the new item; a stale worklist is refused (R5-1). [25]
- A curator-set unapproved version and an anchor re-pointed to other code are re-authored (R5-2). [26]

### Cross-Repo References

No meaningful cross-repo references found: the task document is reached only through the `OpenQuestions` port.

No cross-repo boundary is crossed by this file.
