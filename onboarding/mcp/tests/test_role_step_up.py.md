# mcp/tests/test_role_step_up.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the single step-up a task seat gets: what the user's settings admit, when a launch chooses a
step-up rather than a fresh role, and what stays intact when the seat's predecessor, its review evidence
or its receipt is missing. Settings are checked for exact keys and provenance, and a step-up that the
host refuses leaves the holder and the user's permission authority as they were.

## Code Commentary

### Logic

`write_role()` writes a role file into a settings tree reached through `_user_settings_guard`, so the
settings cases read the same file a real launch would. `launch_world()` builds the launch fixture from
`paseo_launch_test_support` and wires the command surface (`role_step_up`, `paseo_catalog`,
`paseo_role_tools`, the task documents and the review history).

- **Settings.** A user step-up accepts its own choices and defaults to three selections; an invalid one
  names the file and the exact key.
- **Counting.** A failed try is a review-kind round rather than a record check; a step-up selection uses
  its own choices and never steps down; the count selects a step-up at and above its threshold.
- **Provenance.** A step-up's provenance uses the actual predecessor's choices, and a catalog that does
  not offer the chosen tier or model is reported as an unoffered choice rather than silently replaced.
- **Seat handling.** A manual start replaces an idle holder and keeps the step-up across a restart; a
  step-up refuses an active turn or a pending permission without archiving the seat; a failed creation
  leaves an empty seat and the same request retries; a host refusal keeps the holder and the user's
  permission authority.
- **Degraded review.** An unreadable review launches the base role with a warning, or preserves an
  explicit or prior step-up, and the fallback keeps the raw evidence and the other validation.
- **Recorded rounds.** A recorded round names the step-up without granting a round; a third failed round
  changes the harness with its own mode and keeps the reviewer.
- **Replay.** A step-up replay reconciles the decision before the host and survives receipt loss; a host
  default successor model is observed without losing the requested provenance; an incomplete historical
  count warns without inventing tries.
- **No repository supply.** A repository cannot supply a step-up at all.

### Conventions

Cases build a settings tree and a launch world per case, and assert on the recorded decision, the seat's
state and the settings file rather than on internal call order.

### Invariants And Boundaries

- A step-up only ever steps the seat up; it never steps a seat down or invents a try.
- A step-up refused before replacement leaves the holder in place and the settings file unedited; a creation
  failure after the old holder is retired leaves an empty seat that the same request retries.

## Evidence

- Source assertion: test_user_step_up_accepts_own_choices_and_defaults_to_three. The declaration is not an execution receipt. [1]

- Source assertion: test_invalid_step_ups_name_file_and_exact_key. The declaration is not an execution receipt. [2]

- Source assertion: test_failed_tries_are_review_kind_rounds_not_record_checks. The declaration is not an execution receipt. [3]

- Source assertion: test_step_up_selection_uses_own_choices_and_never_steps_down. The declaration is not an execution receipt. [4]

- Source assertion: test_count_selects_step_up_at_and_above_threshold. The declaration is not an execution receipt. [5]

- Source assertion: test_step_up_catalog_provenance_and_unoffered_choice. The declaration is not an execution receipt. [6]

- Source assertion: test_manual_start_replaces_idle_holder_and_keeps_step_up_on_restart. The declaration is not an execution receipt. [7]

- Source assertion: test_step_up_provenance_uses_actual_predecessor_choices. The declaration is not an execution receipt. [8]

- Source assertion: test_step_up_refuses_active_turn_or_permission_without_archiving. The declaration is not an execution receipt. [9]

- Source assertion: test_recorded_round_names_the_step_up_without_granting_a_round. The declaration is not an execution receipt. [10]

- Source assertion: test_failed_step_up_creation_leaves_empty_seat_and_same_request_retries. The declaration is not an execution receipt. [11]

- Source assertion: test_host_refusal_keeps_holder_and_user_permission_authority. The declaration is not an execution receipt. [12]

- Source assertion: test_third_failed_round_changes_harness_with_own_mode_and_keeps_reviewer. The declaration is not an execution receipt. [13]

- Source assertion: test_unreadable_review_launches_base_with_warning. The declaration is not an execution receipt. [14]

- Source assertion: test_unreadable_review_preserves_explicit_or_prior_step_up. The declaration is not an execution receipt. [15]

- Source assertion: test_launch_review_fallback_preserves_raw_evidence_and_other_validation. The declaration is not an execution receipt. [16]

- Source assertion: test_step_up_replay_reconciles_decision_before_host_and_survives_receipt_loss. The declaration is not an execution receipt. [17]

- Source assertion: test_host_default_successor_model_is_observed_without_losing_requested_provenance. The declaration is not an execution receipt. [18]


- An incomplete historical count warns without inventing tries. [19]


- Source assertion: test_repository_cannot_supply_step_up. The declaration is not an execution receipt. [20]
