# mcp/tests/test_consolidator_role.py

## Governing Overview

[MCP Tests](overview.md)

## Purpose

Verifies the Consolidator's role-launch authority, user-settings schema acceptance (`consolidator` and `consolidation-reviewer` rows), field-by-field Reviewer overlay precedence, and consolidation-leaf sibling `leafSeats` hand-over.

## Code Commentary

Subclasses `test_paseo_role_tools.RoleToolsTestCase` with an expanded three-model catalog (`gpt-a`, `gpt-b`, `gpt-c`) and exercises the real start path without reading instruction text. `ConsolidatorStartTests` asserts that Architect, sprint-owning Orchestrator, and master Manager can start `consolidator`, while Worker, Reviewer, and a foreign-sprint Orchestrator are refused with zero host agents created. `ConsolidationSettingsRowTests` verifies that `load_agentic_settings` accepts all 11 role rows (including `consolidator` with `stepUp`, `consolidation-reviewer` with `extraArgs`, and per-level `rolesPerLevel.leaf.consolidation-reviewer`) and rejects misspelled row keys; that `consolidator` uses its own row; that an ordinary task's Reviewer ignores `consolidation-reviewer`; that a consolidation task's Reviewer overlays `consolidation-reviewer` field by field over `reviewer` (even before any Consolidator starts) and falls back cleanly on an empty row; and that explicit start-time model overrides win over both rows. A standalone pytest test verifies `leaf_seats` restricts consolidation siblings to `consolidator` and `reviewer` while ordinary leaves keep `worker`, `reviewer`, `curator`.

## Relationships

Exercises `cli.leaf_seat_handover.leaf_seats`, `cli.seat_variant_rows`, `cli.role_launch_defaults.role_defaults`, `cli.role_launch_preparation`, and `kernel.agentic_settings.load_agentic_settings`. Reuses `RoleToolsTestCase`, `paseo_launch_test_support.CATALOG`, and `_user_settings_guard.user_settings_path_for_write`. Complements `test_consolidation_pass.py` and `test_consolidation_state.py`.

## Evidence

- `ConsolidatorStartTests` proves Architect, own-sprint Orchestrator, and Manager can launch `consolidator`, while Worker, Reviewer, and foreign-sprint Orchestrator are refused without creating agents. [1]
- Verifies `load_agentic_settings` admits all 11 role rows (including `consolidator` `stepUp`, `consolidation-reviewer` `extraArgs`, and leaf-level overrides) and rejects typos like `consolidation-reviewr`. [2]
- Verifies a consolidation task's Reviewer inherits the `reviewer` model while taking `effort` from `consolidation-reviewer`, even when started before any Consolidator. [3]
- Verifies `leaf_seats` exposes only `["consolidator", "reviewer"]` (and single-sibling `roleMessageArguments`) on a consolidation leaf versus `["worker", "reviewer", "curator"]` on an ordinary leaf. [4]
