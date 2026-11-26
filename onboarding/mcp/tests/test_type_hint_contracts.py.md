# mcp/tests/test_type_hint_contracts.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Pins runtime `typing.get_type_hints` resolution (in both module and class scope) for dataclasses whose public field names previously shadowed imported module names, and pins the canonical `Final[tuple[RecordKind, ...]]` typing of `authoring_rows.RECORD_ROW_KINDS`.

## Code Commentary

Because all three target modules use `from __future__ import annotations`, a dataclass field with the same name as an imported module causes `get_type_hints(cls, localns=dict(vars(cls)))` to fail or mis-resolve when evaluating stringified annotations in class scope.

- `test_enclosure_publication_artifacts_outside_scratch_type_hint_resolves` confirms `EnclosurePublicationArtifacts` keeps its public `outside_scratch` dataclass field and resolves `outside_scratch` to `OutsideScratchRoot | None` in both module scope and class scope (`localns=dict(vars(EnclosurePublicationArtifacts))`).
- `test_check_config_targeted_scope_type_hint_resolves` confirms `CheckConfig` keeps public `targeted` and `targeted_scope` dataclass fields and resolves them to `bool` and `TargetedScopeResult | None` in both module scope and class scope.
- `test_record_row_kinds_typed_as_canonical_record_kind_tuple` asserts that `authoring_rows.RECORD_ROW_KINDS` is non-empty, contains only members of `get_args(RecordKind)`, and resolves via `get_type_hints(authoring_rows)["RECORD_ROW_KINDS"]` to `Final[tuple[RecordKind, ...]]`.

## Relationships

Guards the anti-shadowing and typing fixes in [`lifecycle_operation_location.py`](../src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py.md), [`quality_plan.py`](../test_support/agents_remember_test_support/code_quality/quality_plan.py.md), and [`authoring_rows.py`](../src/agents_remember/application/knowledge_writer/authoring_rows.py.md). Declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md) and named in [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) as an exact consumer of `_user_settings_guard.py` and the Node-profile `package-lock.json`.

## Evidence

- `EnclosurePublicationArtifacts.outside_scratch` keeps its public field name and resolves to `OutsideScratchRoot \| None` under both module-scope and class-scope `get_type_hints`. [1]
- `CheckConfig.targeted` and `CheckConfig.targeted_scope` keep their public field names and resolve to `bool` and `TargetedScopeResult \| None` under both module-scope and class-scope `get_type_hints`. [2]
- `authoring_rows.RECORD_ROW_KINDS` is non-empty, contains only canonical `RecordKind` literals, and resolves via `get_type_hints(authoring_rows)` to `Final[tuple[RecordKind, ...]]`. [3]
