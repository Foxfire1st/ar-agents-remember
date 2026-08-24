# PDLS Onboarding Maintenance Input Ledger

| Field | Value |
| --- | --- |
| repository | agents-remember |
| mode | existing-memory-slice-maintenance |
| task | 260824-PDLS Python diagnostic lane separation |
| capturedAt | 2026-08-24T21:43+02:00 |
| source candidate | `23d35f7799153e0c7f3d126291fe2da1662fb87b` |
| source registry | `system/sources.md` |
| domain documentation | none configured for this boundary |
| cross-repository sources | none allowed |

## Authoritative Inputs

- The committed source delta `fbfd37ca..23d35f77`.
- The approved 260824-PDLS master requirement index and full decision-rationale pages.
- Existing onboarding for code quality, worktree quality publication, models, and tests.
- The completed CodeRabbit advisory ledger, with decisions retained by the architect.

Existing onboarding supplied history and route structure but could not override current source.
No external specification defines this repository-owned test-evidence boundary.

## Source Inventory

In-scope path rules cover root `AGENTS.md`/`README.md`, `mcp/**`, and `scripts/**`; the standard
generated/vendor/build/cache exclusions are present. The final source delta contains 46 modified
paths, 30 additions, two behavior-preserving moves, and one deletion. Wave 002 adds two
behavior-preserving file splits: typed worktree requests and pure lifecycle enclosure binding.
Excluded `docs/**`, `CONTRIBUTING.md`, `.dagger/**`, and generated/package data were read as design or
implementation evidence where relevant but do not receive file-level onboarding cards.
