# mcp/tests/test_quality_continuation_declaration.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Protects continuation-snapshot admission in both `DiagnosticExecutionEngine` and `FinalCodexExecutionEngine`, ensuring the reconstructed Dagger host declaration preserves `AUTHORITY_SCHEMA_VERSION`, exact manifest shape, `declaration_digest`, snapshot-sourced provenance, and round-trip re-parsing.

## Code Commentary

Fixture helpers build a dual-profile `CanonicalRailRegistry` (`_dual_profile_registry`) pairing the certifying profile from `test_final_codex_models.py` (gates 1-5) with `portable-diagnostic` (gates 1-4), generate green gate 1-3 prerequisite manifests (`_green_prerequisites`), and admit one initial `AdmittedDaggerAuthority` against a temporary `AuthorityRegistry` (`_initial_authority`) using `FakeInspector` and `engine_environ(DECLARATION_V1)`.

- `test_diagnostic_continuation_preserves_host_declaration_schema_and_digest` calls `DiagnosticExecutionEngine.admit` with `continuation_snapshot=initial.snapshot` and asserts that `attempt.admitted.declaration` keeps `schema_version == AUTHORITY_SCHEMA_VERSION`, `as_manifest()["schemaVersion"] == AUTHORITY_SCHEMA_VERSION`, exact manifest equality with `initial.declaration.as_manifest()`, identical `declaration_digest`, `source == f"snapshot:{initial.snapshot.snapshot_digest}"`, and digest equality after `parse_host_declaration(declaration.as_manifest(), ...)`, always releasing the admitted authority in a `finally` block.
- `test_final_codex_continuation_preserves_host_declaration_schema_and_digest` runs the symmetric continuation-admission check through `FinalCodexExecutionEngine.admit` with `FinalCodexManifestStore` and `build_final_codex_run_spec`, verifying identical schema-version, manifest, digest, snapshot source, and re-parse preservation before releasing authority.

## Relationships

Tests continuation admission across [`diagnostic_executor.py`](../src/agents_remember/worktrees/modules/quality/diagnostic_executor.py.md), [`final_codex_executor.py`](../src/agents_remember/worktrees/modules/quality/final_codex_executor.py.md), and [`dagger_authority.py`](../src/agents_remember/worktrees/modules/quality/dagger_authority.py.md), reusing portable rail and authority fixtures from [`test_final_codex_models.py`](test_final_codex_models.py.md). Declared in the `unit-regression` lane of [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md) and named in [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md) as an exact consumer of `_user_settings_guard.py` and the Node-profile `package-lock.json`.

## Evidence

- `DiagnosticExecutionEngine.admit` with `continuation_snapshot` preserves `AUTHORITY_SCHEMA_VERSION`, manifest equality, `declaration_digest`, `snapshot:<digest>` source provenance, and `parse_host_declaration` round-trip digest equality. [1]
- `FinalCodexExecutionEngine.admit` with `continuation_snapshot` preserves `AUTHORITY_SCHEMA_VERSION`, manifest equality, `declaration_digest`, `snapshot:<digest>` source provenance, and `parse_host_declaration` round-trip digest equality. [2]
