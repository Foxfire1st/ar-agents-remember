# mcp/tests/test_dependent_deferrals.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Unit tests covering dependent-record deferral schema validation, byte-identical omission when empty, `knowledge_write` deferral operations (`defer`, `redefer`, `lift`, partial `resolveDeferrals`), history-row validation, and unedited-confirmation refusal.

## Code Commentary

### Logic

- Runs against real temporary Git code/memory repositories built via `dependent_deferrals_test_support` and is registered in the `unit-regression` lane of `mcp/tests/test-evidence-lanes.toml`.
- Covers invalid deferral inputs (`test_01`), confirmation preservation and revision bumps (`test_02`), history validator and rule-5 gate matching (`test_03`), unedited-confirmation refusal naming open deferrals (`test_04`), partial resolution keeping remaining deferrals open (`test_05`), note-only re-deferral refusal and changed-blob same-file re-deferral (`test_10`), multi-owner `DPD-W0T9V9` CAP+BUG partial resolve and re-deferral (`test_11`), byte-identical serialization when `deferrals` is absent (`test_17`), enforced `deferral_lifted` history row disposition including multi-op writes (`test_lift_requires_deferral_lifted_row_and_surfaces_in_multi_op_write`), and new-record confirmation+deferral refusal without edit (`test_new_dependent_with_confirmation_and_deferral_without_edit_is_refused`).

## Relationships

- Uses `mcp/tests/dependent_deferrals_test_support.py` and proves the model and writer invariants in `models/knowledge_files/` and `application/knowledge_writer/deferrals.py`.

## Evidence

- The module tests deferral validation, preservation of confirmation fields, partial resolution, re-deferral rules, byte-identity, lift row enforcement, and new-record confirmation refusal. [1]
