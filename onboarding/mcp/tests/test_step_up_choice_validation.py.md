# mcp/tests/test_step_up_choice_validation.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Holds the regressions around step-up choice validation and the advice given after a publication: a
refused feature names the key the user authored, an omitted mode takes the host default without changing
the base, a no-op step-up refuses by file and key, and a failure after the commit still returns the
recorded review.

## Code Commentary

### Logic

`launch_world` from `paseo_launch_test_support` provides the launch fixture; `_user_settings_guard`
writes the settings tree, and the cases drive `role_launch_defaults` and the task-document tools.

- **Refusal names what the user authored.** `test_step_up_feature_refusal_names_authored_key_before_retirement`
  and `test_per_level_step_up_refusal_preserves_settings_file_and_exact_feature_key` keep the refusal on
  the authored key and leave the settings file untouched.
- **Omitted mode.** `test_cross_model_omitted_mode_uses_host_default_without_changing_base` takes the
  host default for an omitted mode while the base role's choices stay as they were.
- **A no-op step-up refuses.** `test_effective_noop_step_up_refuses_with_authored_file_and_key` refuses a
  step-up whose authored values make no change, naming the file and the key. The cases compare
  equal model values and equal `priority` tier values across the native and alias keys; they do not
  infer equivalence between arbitrary host labels and IDs at settings-parse time.
- **After the commit.** `test_post_commit_settings_hint_failure_returns_the_recorded_review` proves a
  failure of the settings hint after publication still returns the review that was recorded.
- **Predecessor material.** `test_receipt_loss_uses_durable_destination_as_predecessor_in_takeover_material`
  reads the predecessor from the durable destination when the receipt is lost.
- **Alias and tier.** `test_same_scope_native_tier_step_up_is_not_hidden_by_inherited_alias` keeps a
  same-scope native tier choice visible through an inherited alias. Its host catalog offers ID
  `priority` with label `Fast`: the inherited `fast` choice starts, but a native step-up value
  `not-offered` is refused by its exact settings key before the original agent is archived.

### Conventions

Each case builds its own settings tree and launch world, edits only the key under test, and asserts on
both the answer and the bytes of the settings file.

### Invariants And Boundaries

- A refusal never rewrites the settings file to make itself true.
- A post-commit failure does not discard the review already recorded.

## Evidence

- Source assertion: test_step_up_feature_refusal_names_authored_key_before_retirement. The declaration is not an execution receipt. [1]

- Source assertion: test_cross_model_omitted_mode_uses_host_default_without_changing_base. The declaration is not an execution receipt. [2]

- Source assertion: test_effective_noop_step_up_refuses_with_authored_file_and_key. The declaration is not an execution receipt. [3]


- A per-level refusal preserves the settings file and the exact feature key. [4]


- Source assertion: test_post_commit_settings_hint_failure_returns_the_recorded_review. The declaration is not an execution receipt. [5]

- Source assertion: test_receipt_loss_uses_durable_destination_as_predecessor_in_takeover_material. The declaration is not an execution receipt. [6]


- A same-scope native tier step-up is not hidden by an inherited alias. [7]
