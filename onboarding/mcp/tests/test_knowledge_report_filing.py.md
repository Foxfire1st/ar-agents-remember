# mcp/tests/test_knowledge_report_filing.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R74 rule 6: the selected reads, previews and dry-run paths file no per-call report.** The install preview and carryover authority-refusal cases leave no temporary report directory. The retained internal drift authority-refusal path also leaves no temporary directory. The install and carryover compactors omit `reportPath` when passed no report and retain it when passed a report path; this checks those fields, not preservation of every payload key or execution of a mutating install.

## Code Commentary

The drift-summary caller explicitly selects `write_report=False`: it returns a checked answer without a report pointer, Markdown report or observer log. The base-payload helper omits `drift_report` when supplied no report and retains it when supplied one. A positive control leaves the explicit drift report producer at its default output and observes both the Markdown report and observer snapshot with its report pointer. That explicit producer is deliberately outside the non-filing read mode; the file does not exercise live mutating install actions or claim they passed.

## Evidence

- Install dry run files no per-call report. [3]
- Carryover authority refusal files no per-call report. [4]
- The surviving install and carryover compactors omit or retain the pointer according to the supplied report path. [5]
- Non-reporting drift-summary mode files no Markdown report or observer log and returns no report pointer. [6]
- The explicit default-output report producer still writes the report and observer snapshot. [7]
- Base payload omits drift_report without a supplied report and keeps it with one. [8]

- The retained internal drift authority refusal creates no temporary report directory. [9]
