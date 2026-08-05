# mcp/tests/_durability_measurement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/_durability_measurement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Non-vacuity contract for one durability stress result.

## Code Commentary

### Logic

Module-level surface:

- `VacuousRunError` (class, lines 14-15) — The instrument did not complete enough requested work to report a durability number.
- `require_stress_measurement` (function, lines 18-55) — Return a complete stress result or name every fact that makes it vacuous.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `VacuousRunError` (lines 14-15) — The instrument did not complete enough requested work to report a durability number.. | `VacuousRunError` | mcp/tests/_durability_measurement.py:14-15 |
| Defines the function `require_stress_measurement` (lines 18-55) — Return a complete stress result or name every fact that makes it vacuous.. | `require_stress_measurement` | mcp/tests/_durability_measurement.py:18-55 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
