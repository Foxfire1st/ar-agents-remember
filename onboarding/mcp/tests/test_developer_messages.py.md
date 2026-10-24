# mcp/tests/test_developer_messages.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the developer's send from the tray and the host-wide seat list (MIK-R188 evidence 3): a send composes one
message per target in the declared order, every reference kind has a written form opening with its call, and a
body, a reused id, an unsupported image or a malformed body is refused by name before anything is filed. A held
outcome is filed and logged, and the seat list joins live agents with current records.

## Code Commentary

### Logic

`record_text()`, `revision_id()`, `commit_tree()` and `references()`/`parsed_reference()` build the memory
records and wire references a send can name, while `text_pick()` and `image_pick()` build the tray's picks.

- **Composition.** `test_a_send_to_two_targets_composes_one_message_each_in_rule_8_order` and
  `test_each_reference_kind_has_a_written_form_that_opens_with_its_call` fix the per-target message and the
  reference grammar.
- **Refusals before filing.** `test_bounds_and_a_reused_message_id_are_refused_by_name_before_anything_is_filed`,
  `test_a_body_over_its_bound_is_refused_by_name_before_it_is_parsed`,
  `test_an_unsupported_image_type_and_a_malformed_body_are_refused_by_name` and
  `test_a_reference_whose_parts_name_different_objects_is_refused_before_it_is_filed` keep each refusal ahead
  of any write and each answer named rather than a bare 422.
- **Targets.** `test_a_busy_target_is_held_as_text_that_names_the_message_file`,
  `test_an_archived_target_is_refused_by_name_and_the_other_target_is_served` and
  `test_a_limited_target_is_held_with_the_reset_time_it_was_stored_with` keep a busy or limited target held with
  its reason and an archived one refused without costing the other target.
- **References.** `test_references_from_a_comparison_name_the_leafs_memory_and_their_tree` and
  `test_record_references_name_the_revision_the_memory_side_they_name_holds` require a reference to name its
  revision and the leaf's memory, and `test_a_chat_pick_whose_provenance_is_no_agent_id_or_no_time_is_refused_by_name`
  checks the chat pick's provenance before Send.
- **Filing.** `test_a_filing_that_fails_leaves_no_new_pick_and_keeps_one_another_message_names` removes the picks
  it saved itself while keeping one another message names, and
  `test_a_held_send_that_ends_undelivered_is_filed_and_logged_undelivered` and
  `test_a_held_send_after_a_partial_drain_is_answered_by_its_own_message` keep a held send's fate recorded per
  send.
- **Seat list.** `SeatListTests.test_the_seat_list_joins_live_agents_with_current_records_and_pages` joins live
  agents with current records and pages the answer, including a taskless seat.
- **Bounded logs and routes.** `SentLogBoundTests.test_the_sent_picks_log_keeps_its_latest_lines_and_its_latest_recipients`
  keeps the sent log bounded, and `TrayRouteGuardTests.test_the_dashboard_serves_the_tray_routes_and_refuses_a_foreign_page_before_them`
  refuses a foreign page before the tray routes.

### Conventions

A send is asserted on the file it wrote — its folder, its head and the SHA-256 it names — as well as on the
answer, so a correct answer over a wrong file fails.

### Invariants And Boundaries

- A refusal is named: an argument, reference, provenance or bound refusal happens before anything is filed, while an archived-recipient refusal is filed and kept as its `.undelivered.md` message file.
- A held send is not lost: it is filed, and its eventual undelivered outcome is logged against its own message.

## Evidence

- Developer send composition, exact references, file-first recovery, held outcomes and bounded recipient and log routes. [1]
- The same contract over the send's references and their written forms. [2]
- The same contract over the tray's bounds and refusals. [3]
- The same contract over held sends and their logged outcomes. [4]
- The same contract over the seat list and the tray route guard. [5]
- The same contract over the reference grammar and provenance checks. [6]
- The same contract over filing failure and pick cleanup. [7]
- The same contract over the bounded sent log. [8]

- Checks developer send composition, exact references, file-first recovery, held outcomes and bounded recipient/log routes — mcp/tests/test_developer_messages.py:1-13. [9] [10] [11] [12] [13] [14] [15] [16] [17] [18]
