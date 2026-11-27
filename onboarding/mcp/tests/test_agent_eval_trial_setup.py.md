# mcp/tests/test_agent_eval_trial_setup.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Controlled native fixture provisioning, host identity and cleanup ownership are the subject of this regression module.

## Code Commentary

`TrialSetupTests.setUp` isolates `HERMES_HOME` to `self.root / "source-home"` and patches `agent_evals.trial_setup.resolve_hermes_auxiliary` to `[]` with `addCleanup` teardown (preserving per-test overrides and `HermesDestinationTests` direct resolver coverage), and `test_native_repository_wave_admission_and_material_alias` asserts `providerIsolation.credentialBorrowing.sourceHome` matches that test-owned directory.

### Invariants And Boundaries

The source declares controlled assertions and retained-data scenarios. Reading this card establishes neither a fresh test run nor native host or model acceptance.

## Evidence

- The source defines this file's responsibility and the boundaries described here. [1]
