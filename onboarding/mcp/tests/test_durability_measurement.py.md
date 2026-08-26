# mcp/tests/test_durability_measurement.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_durability_measurement.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

The durability instrument refuses zero-attempt and incomplete stress results.

## Code Commentary

### Logic

Module-level surface:

- `_result` (function, lines 16-30)
- `DurabilityMeasurementTests` (class, lines 33-97)

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
| Defines the function `_result` (lines 16-30). | `_result` | mcp/tests/test_durability_measurement.py:16-30 |
| Defines the class `DurabilityMeasurementTests` (lines 33-97). | `DurabilityMeasurementTests` | mcp/tests/test_durability_measurement.py:33-97 |

## 2026-08-26 Evidence-Lane Classification

The durability measurement class is explicitly marked `evidence_stress`. Its zero-attempt,
minimum-reclaim, error, straggler, and persistence assertions are unchanged, but selection now
belongs to the scheduled stress evidence lane instead of ordinary deterministic acceptance.

## Update History

- 2026-08-26T10:44:52+02:00 — Recorded the explicit `evidence_stress` lane classification for durability measurement without changing its refusal semantics.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
