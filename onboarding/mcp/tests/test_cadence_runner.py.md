# mcp/tests/test_cadence_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_cadence_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T14:18+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Forces the non-accepting cadence runner to remain Dagger-admitted, trigger-specific, explicit about
its selected evidence lane, and incapable of becoming a shadow quality-acceptance route.

## Code Commentary

### Logic

The fixture patches provenance and subprocess execution while writing real report-log and phase
artifacts. Tests prove that host invocation is refused before inventory or execution, scheduled
stress runs serially with the `evidence_stress` marker and non-accepting metadata, provider bumps
use their own population, an empty migration window is honestly not applicable, and release or
diagnostic triggers are refused because they have separate owners.
Dedicated cases delete or corrupt the phase report and require a nonzero result plus an explicit
failure artifact, proving that missing evidence cannot be accepted as a successful cadence run.

### Conventions

Assertions inspect the exact subprocess command and emitted JSON rather than trusting a successful
mock return code. Synthetic phase data includes collected, selected, deselected, and reported
counts so population claims remain checkable.

### Invariants And Boundaries

- Cadence evidence never sets `acceptanceEligible` or `certifying` true.
- Host execution must fail before reading inventory or starting pytest.
- Scheduled durability stays serial; provider and migration triggers cannot silently reuse it.
- Release and diagnostic work retain their own explicit routes.

### Todos

None.

## Docs References

No Domain Documentation source is configured; this is a repository-owned test contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external contract is required to interpret this forcing test. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Host admission precedes inventory and execution; scheduled evidence is serial and explicitly non-accepting. | `test_host_process_is_refused_before_inventory_or_execution`; `test_scheduled_stress_is_serial_loud_and_explicitly_non_accepting` | mcp/tests/test_cadence_runner.py:73-113 |
| Provider-bump and empty-migration behavior remain trigger-specific. | `test_provider_bump_uses_its_own_population`; `test_empty_migration_window_is_not_applicable_without_running_pytest` | mcp/tests/test_cadence_runner.py:115-173 |
| Release and diagnostic triggers are rejected as shadow cadence routes. | `test_release_and_diagnostic_triggers_are_not_shadow_quality_routes` | mcp/tests/test_cadence_runner.py:174-184 |
| The implementation under test owns the Dagger admission, trigger expression, provenance, and artifacts. | `run_cadence_evidence` | mcp/test_support/agents_remember_test_support/testing/cadence_runner.py:54-136 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository contract participates in this test. | — | — |

## Update History

- 2026-08-28T14:18+02:00 — Reconciled cadence-test symbols and ranges against the committed PDLS
  candidate after final test renames; the proof obligation is unchanged.

- 2026-08-28T11:32+02:00 — Added missing and unusable phase-report forcing; both must emit durable
  failure artifacts and fail the route.

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for the final
  Dagger-admitted cadence contract and recorded its non-accepting, trigger-specific boundaries.
