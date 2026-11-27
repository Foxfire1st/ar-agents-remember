# mcp/src/agents_remember/cli/seat_variant_rows.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

Resolves task-kind-specific settings-row overlays for a leaf seat launch so a consolidation task's Reviewer reads `consolidation-reviewer` field by field over the base `reviewer` row before start-time overrides are applied.

## Code Commentary

`seat_variant_row(context)` returns `CONSOLIDATION_REVIEWER_ROW` (`"consolidation-reviewer"`) only when `context.role == "reviewer"`, `context.task` is present, and `names_consolidation_list(context.task.document)` is true; otherwise it returns `None`. Because the decision comes solely from the task document, the Reviewer receives the refinement whether started before or after the Consolidator. `seat_launch_knobs(settings, context)` resolves the seat's own `RoleKnobs` at `ROLE_LEVELS[context.role]` and, when a variant row applies, overlays `_bound_over(own, settings.resolved_role_knobs(row, level))` onto `own` via `overlay_role_knobs`. `_bound_over` rebinds each origin entry in the variant row to the effective `provider` (variant harness or seat harness) and `model` (variant model or seat model when its provider matches) so an effort or feature specified without repeating harness/model is not dropped as model-unbound during launch resolution. Explicit start-time choices (`agent`, `model`, `effort`) still outrank both rows in the caller.

## Relationships

Called by `mcp/src/agents_remember/cli/role_launch_defaults.py` (`seat_launch_knobs`). Depends on `kernel._agentic_settings_core` (`CONSOLIDATION_REVIEWER_ROW`, `overlay_role_knobs`), `kernel.agentic_settings` (`AgenticSettings`, `RoleKnobs`), `models.role_identity.ROLE_LEVELS`, `application.role_launch_context.RoleLaunchContext`, and `tasks.consolidation_task.names_consolidation_list`. Exercised end-to-end by `ConsolidationSettingsRowTests` in `mcp/tests/test_consolidator_role.py`.

## Evidence

- `seat_variant_row` selects `CONSOLIDATION_REVIEWER_ROW` exclusively for a `reviewer` whose task document names a `consolidationList`. [1]
- `seat_launch_knobs` resolves the role's level-scoped settings and overlays the bound variant row via `overlay_role_knobs`, leaving the seat row unchanged when no variant applies. [2]
- `_bound_over` inherits the base row's provider and compatible model into variant choice origins so effort or feature overrides authored without repeating harness/model survive launch selection. [3]
