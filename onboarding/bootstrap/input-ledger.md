# PDLS Onboarding Maintenance Input Ledger

| Field | Value |
| --- | --- |
| repository | agents-remember |
| mode | existing-memory-slice-maintenance |
| task | 260824-PDLS Python diagnostic lane separation |
| capturedAt | 2026-08-25T08:16+02:00 |
| source commit | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| source tree | `65a8c5fcae3551dd596421d6cb0c56a4ca64bc0d` |
| source registry | `system/sources.md` |
| domain documentation | none configured for this boundary |
| cross-repository sources | none allowed |

## Authoritative Inputs

- The emergency-landed source delta `fbfd37ca..cb662377` and exact source tree `65a8c5fc`.
- The approved 104-row 260824-PDLS requirement matrix and full decision-rationale pages.
- The whole-system reconciliation, immutable Candidate-A artifacts, and the final failed Dagger
  report retained as repair evidence rather than acceptance.
- Current source plus existing onboarding history for testing, code quality, models, application
  lifecycle, worktree publication, and test support.
- Official pytest-xdist hook documentation used only for the all-worker phase-reporter repair.

Existing onboarding supplies history and route structure but cannot override current source.
No external specification defines this repository-owned evidence authority.

## Source Inventory

The emergency-landed source candidate changes 250 paths with 11,943 insertions and 22,434 deletions
(net -10,491). The dominant deletion is obsolete non-Python/model-split evidence; the Candidate-A
design deliberately removes the generic dependency analyzer. Wave 003 predates several final
ownership splits, which remain explicitly pending rather than silently treated as onboarded.
Standard generated, vendor, build, and cache exclusions remain in force.
