# mcp/tests/test_paseo_role_messages.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers role messaging between role agents against a fake bridge: how a role resolves to its live agent
through the receipts, which recipients are refused and which are held, how a refused or unanswered send
is delivered exactly once, and how a wait reports the turn that consumed the message. Delivery is
at-most-once even when the recipient's own timeline already holds the copy.

## Code Commentary

### Logic

`RoleMessageTests` drives the role-tool surface (`paseo_role_tools`) with `role_held_messages`,
`models.role_agents`, the host-activity observer and its projection, and the worktree boundary.

- **Addressing.** `test_a_role_resolves_through_the_receipts_to_its_live_agent` resolves a role name to
  one live agent, `test_several_live_agents_of_a_role_are_refused_with_their_ids_never_chosen_among` and
  `test_a_leaf_seat_with_two_live_agents_refuses_by_role` refuse ambiguity instead of picking, and
  `test_the_caller_is_no_candidate_of_its_own_role_address` keeps a caller out of its own address.
- **Reachability.** `test_only_an_agent_id_of_this_lines_receipts_is_a_recipient` bounds recipients to
  the line's receipts; `test_every_execution_of_a_taskless_role_that_is_not_stopped_is_asked_about`
  asks about every unstopped execution of a taskless role, and
  `test_more_executions_than_are_asked_about_are_refused_and_the_cut_is_said` refuses past that bound
  and says where it cut.
- **Holding.** A recipient whose start has not finished, one waiting for a permission decision, and one
  whose host does not answer are held rather than dropped; `test_a_held_batch_preserves_the_reported_replacement_and_warning`
  keeps the host's replacement and warning, and `test_a_delivery_that_takes_held_messages_answers_ok`
  proves no validation error follows a delivery of held work.
- **At-most-once.** `test_a_copy_the_recipient_already_holds_is_not_sent_again` settles a duplicate from
  the recipient's own timeline, and `test_an_unknown_send_outcome_is_not_delivered_twice` resends with the
  same id, so an unknown outcome is not a second copy.
- **Turns.** `test_a_running_turn_is_steered_or_held_by_its_provider_and_never_cut_off` and
  `test_a_refused_send_is_held_and_no_answer_names_a_cancellation` keep steering provider-scoped and a
  refusal held; `test_the_hosts_own_activity_record_holds_a_message_the_snapshot_calls_idle` lets the
  host's own activity record decide too.
- **Waits.** `test_a_wait_returns_the_outcome_of_the_turn_that_consumed_the_message`,
  `test_a_wait_follows_the_message_into_the_turn_that_consumes_it` and
  `test_a_wait_that_times_out_leaves_the_message_delivered` keep a wait tied to the consuming turn and a
  timeout a delivered message.
- **Text and refusals.** `test_the_delivered_text_opens_with_the_line_that_names_the_sender` and
  `test_the_results_and_refusals_are_exactly_the_named_ones` pin the delivered prefix and the named
  result and refusal codes.

### Conventions

Cases use `paseo_role_tools_test_support` for the bridge and message fixtures, and
`runtime_that_names_no_turn()` / `message_with()` to vary what the runtime reports about a turn.

### Invariants And Boundaries

- No message is delivered twice, whether the outcome was unknown, the copy was already held or a wait
  timed out.
- Ambiguity is refused by name; a role is never resolved by guessing between live agents.

## Evidence


- Role addressing, reachability bounds, holding, at-most-once delivery, turn steering and waits are asserted here. [1]



- A message file carries one timestamp, sender and recipient and reports its returned SHA-256, while a bodyless delivered text keeps its existing form. [2]



- Controlled-runtime cases hold permission, start-unfinished and unwritable-turn messages, deliver waiting work in order, refuse two live leaf occupants, and keep a completed holder's seat until archived. [3]
