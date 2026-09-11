# mcp/test_support/agents_remember_test_support/testing/lane_manifest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/testing/lane_manifest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Python test evidence infrastructure](overview.md)

## Purpose

Loads the one exhaustive, explicit lane assignment for every current Python test file and bounded
class/node override.

## Code Commentary

### Logic

The loader validates schema, categories, confined paths, current selectors, duplicates, conflicts,
missing test files, and stale rows. It produces a digest plus full included/excluded population for
cadence and retry compatibility.

### Conventions

File lanes are mandatory; narrow overrides are explicit and most-specific.

### Invariants And Boundaries

- No unknown item defaults to unit.
- Diagnostic evidence cannot enter accepting lanes.
- Retry identity binds the full lane population, not only selected files.

### Todos

None.

## Docs References

The lane taxonomy is repository-owned in `docs/design/python-evidence-system.md`.

## Repo-Internal References

The authority file is `mcp/tests/test-evidence-lanes.toml`; `test_evidence_lanes.py` forces missing,
unknown, and conflicting cases.

## Cross-Repo References

No cross-repository boundary applies.

## Update History

- 2026-08-27T11:08+02:00 — Created to remove the unmarked-unit default.
