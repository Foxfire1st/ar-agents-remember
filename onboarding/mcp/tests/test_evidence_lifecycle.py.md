# mcp/tests/test_evidence_lifecycle.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_evidence_lifecycle.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Forces durable test evidence to have complete, source-observable ownership and lifecycle metadata,
including real consumers, executable replacement contracts, expiry behavior, and explicit
governance of task/date-shaped baselines and large unknown fixtures.

## Code Commentary

### Logic

The `_Project` fixture constructs a minimal Git-backed test repository and emits lifecycle catalogs
plus observable consumer code. Tests compare the real repository inventory with the governed set,
reject uncataloged fixtures/shared support and incomplete or invented consumers, require task/date
baselines and size-threshold fixtures to be governed, reject missing artifacts or stale contract
rows, and require temporary evidence to name an existing executable replacement before expiry.

### Conventions

Catalog rows are generated from one frozen `_Artifact` model so individual tests change only the
dimension under examination. Consumer completeness is checked against real source observations;
the catalog cannot declare unsupported readers.

### Invariants And Boundaries

- Lifecycle metadata describes existing evidence and observable consumers; it cannot create
  authority by assertion.
- Unknown governed artifacts fail closed, including ordinary shared support and large uncommon
  fixture suffixes.
- Temporary evidence requires a real executable replacement and an unexpired deadline.
- Contract identities must have real owners/nodes and must actually be referenced.

### Todos

None.

## Docs References

No Domain Documentation source is configured; durable-evidence governance is an internal contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for this lifecycle forcing suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository closure, uncataloged evidence, and source-observed consumer completeness are forced. | `test_repository_inventory_is_closed_over_governed_artifacts`; `test_new_fixture_or_ordinary_shared_support_without_metadata_is_refused`; `test_source_observed_missing_or_unsupported_consumers_are_refused` | mcp/tests/test_evidence_lifecycle.py:122-175 |
| Task/date baselines and configured large-fixture thresholds cannot escape governance. | `test_task_or_date_shaped_baseline_is_governed`; `test_configured_size_threshold_governs_unknown_fixture_suffixes` | mcp/tests/test_evidence_lifecycle.py:177-204 |
| Missing artifacts, contradictory authority, nonexistent owners, and stale contract identities fail closed. | `test_stale_or_contradictory_metadata_is_refused`; `test_nonexistent_registered_contract_and_stale_contract_rows_are_refused` | mcp/tests/test_evidence_lifecycle.py:206-242 |
| Temporary evidence requires an executable replacement and obeys expiry. | `test_temporary_evidence_requires_a_real_executable_replacement`; `test_expired_migration_fails_even_when_its_replacement_exists`; `test_future_migration_with_an_existing_replacement_is_valid` | mcp/tests/test_evidence_lifecycle.py:244-323 |

## Cross-Repo References

No meaningful cross-repository boundary applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite constructs its own temporary repository; it does not assert a sibling-repository contract. | — | — |

## Update History

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: created the missing sidecar for closed-world
  evidence lifecycle ownership, consumer truth, replacement contracts, and expiry.
