# mcp/tests/test_replay_freeze.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_replay_freeze.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-04T22:23+02:00 |
| lastVerifiedCommitHash | `e84c004c37a4bad082e1a7f1bdc4bd062282a185` |
| lastVerifiedCommitDate | 2026-09-04T22:06:05+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fully standalone CCR-R17 (leaf 260831-CCR-L17) forcing suite for the measured-replay freeze and population contracts in `certification/replay/freeze.py`: deterministic digest-bound freeze compilation, tamper refusal, baseline/treatment comparability across every frozen dimension, observation-metadata non-interference, and the append-only three-view incident population (compile order, denominator exclusion of dated supplements, duplicate refusal, closed stratum/generation windows, and rewrite refusal). Every fixture is constructed in this module; no certification-run, evidence-lifecycle, telemetry-stream, or Dagger artifact is shared, and numeric reduction thresholds are never asserted.

## Code Commentary

### Logic

- `test_freeze_compile_digest_is_deterministic_and_self_consistent` (lines 50-56) compiles two identical inputs and asserts equal, matching digests.
- Tamper and refusal cases (`test_freeze_rejects_tampered_digest`, lines 59-67; `test_source_revision_change_refuses_pair`, lines 80-91; `test_profile_change_refuses_pair`, lines 94-103; `test_plan_configuration_and_runtime_changes_refuse_pair`, lines 104-120) prove digest and frozen-dimension refusals.
- `test_observation_metadata_never_changes_the_freeze` (lines 122-156) proves observation metadata is outside the frozen identity.
- Population cases (`test_population_compile_orders_and_digests_rows`, lines 158-163; `test_population_denominator_excludes_dated_supplements`, lines 165-169; `test_population_rejects_duplicate_generations`, lines 171-186; `test_population_stratum_generation_ranges_are_closed`, lines 188-206; `test_append_only_population_guard_refuses_rewrites`, lines 208-255) pin the three-view population contract.

### Conventions

Standalone per the evidence-lifecycle isolation rule; the module imports only `agents_remember.*` production sources and never a pre-existing `mcp/tests` support module.

### Invariants And Boundaries

- The freeze digest is deterministic and tamper-evident.
- A pair is comparable only when no frozen dimension changed; observation metadata never invalidates a pair.
- The population is append-only; dated supplements are excluded from the denominator and never rewrite frozen rows.

### Todos

None recorded.

## Docs References

No external Domain Documentation source is configured for this repository-owned suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source governs this test module. | - | - |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The freeze/population contracts under test. | `compile_replay_freeze`; `compare_replay_freezes`; `compile_replay_population`; `require_append_only_population` | mcp/src/agents_remember/certification/replay/freeze.py:119-124; mcp/src/agents_remember/certification/replay/freeze.py:134-157; mcp/src/agents_remember/certification/replay/freeze.py:267-278; mcp/src/agents_remember/certification/replay/freeze.py:311-336 |
| The population row vocabulary under test. | `PopulationGeneration` | mcp/src/agents_remember/certification/replay/models.py:115-132 |
| The explicit unit-regression lane registration. | `test_replay_freeze.py` | mcp/tests/test-evidence-lanes.toml:149 |

## Cross-Repo References

No cross-repository implementation boundary is owned here.

| Finding | Anchor | Source |
| --- | --- | --- |
| Same-repository forcing suite; nothing crosses repositories. | - | - |

## Update History

- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass: created for the new CCR-R17 freeze/population forcing suite (deterministic digests, frozen-dimension comparability, append-only three-view population). Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).
