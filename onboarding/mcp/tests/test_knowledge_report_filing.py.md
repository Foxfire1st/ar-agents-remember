# mcp/tests/test_knowledge_report_filing.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R74 rule 6: reads, previews and dry runs file no per-call report.** A diagnostic read, a watcher status read, a watcher/install dry-run preview and a carryover plan write nothing under `temp/tool-reports/` and carry no `reportPath` pointer; their answers keep every content key. Only an executed mutating action files its report.

## Code Commentary

Module rule, matching the codebase's own drift-check idiom: `compact_*` omits `reportPath` when no report is filed and keeps it when one is. The drift-summary read files no temp report, the base payload omits the drift report without filing, and the explicit report producer still writes both — so the omission is a read filing nothing, never a dropped report.

## Evidence

- Diagnostics reads file no per-call report [1]
- Watcher status and dry runs file no per-call report [2]
- Install dry run files no per-call report [3]
- Carryover plan refusal files no per-call report [4]
- Compacts omit the pointer only when nothing is filed [5]
- Drift-summary read files no temp report [6]
- Explicit report producer still writes both [7]
