# mcp/tests/test_wire_contract.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_wire_contract.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Tests for the post-``model_dump`` mutation fitness function.

## Code Commentary

### Logic

Module-level surface:

- `_wire` (function, lines 27-39) — What the rule reports for a single-module ``source``, as ``line [form]`` strings.
- `PostDumpMutationTests` (class, lines 42-63) — The armed check. It runs in the ordinary suite, so it runs wherever the suite does.
- `FunctionBoundaryTests` (class, lines 66-152) — Detect dump-derived values returned across a function boundary.
- `WireSweepReachTests` (class, lines 155-247) — Every mutation and laundering form the rule claims to catch.
- `WireSweepFalsePositiveTests` (class, lines 250-317) — Known-good constructs the package really contains. None of these may be reported.
- `SanctionedOwnerTests` (class, lines 320-388) — The one permitted serve-time tail builder -- an owner, not an exception entry.
- `OffenderReportTests` (class, lines 391-410) — L6-R15: the message names every offender and the fix, or the check is unusable.

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
| Defines the function `_wire` (lines 27-39) — What the rule reports for a single-module ``source``, as ``line [form]`` strings.. | `_wire` | mcp/tests/test_wire_contract.py:27-39 |
| Defines the class `PostDumpMutationTests` (lines 42-63) — The armed check. It runs in the ordinary suite, so it runs wherever the suite does.. | `PostDumpMutationTests` | mcp/tests/test_wire_contract.py:42-63 |
| Defines the class `FunctionBoundaryTests` (lines 66-152) — Detect dump-derived values returned across a function boundary.. | `FunctionBoundaryTests` | mcp/tests/test_wire_contract.py:66-152 |
| Defines the class `WireSweepReachTests` (lines 155-247) — Every mutation and laundering form the rule claims to catch.. | `WireSweepReachTests` | mcp/tests/test_wire_contract.py:155-247 |
| Defines the class `WireSweepFalsePositiveTests` (lines 250-317) — Known-good constructs the package really contains. None of these may be reported.. | `WireSweepFalsePositiveTests` | mcp/tests/test_wire_contract.py:250-317 |
| Defines the class `SanctionedOwnerTests` (lines 320-388) — The one permitted serve-time tail builder -- an owner, not an exception entry.. | `SanctionedOwnerTests` | mcp/tests/test_wire_contract.py:320-388 |
| Defines the class `OffenderReportTests` (lines 391-410) — L6-R15: the message names every offender and the fix, or the check is unusable.. | `OffenderReportTests` | mcp/tests/test_wire_contract.py:391-410 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
