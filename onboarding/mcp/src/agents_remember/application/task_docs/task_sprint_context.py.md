# mcp/src/agents_remember/application/task_docs/task_sprint_context.py

## Governing Overview

[task_docs overview](overview.md)

## Purpose

> **Retained historical source account — superseded by the current contract:**
> Reads the addressed sprint and captures its source snapshot for sprint operations.

## Code Commentary

### Current Contract

SprintLinkageRequest threads the optional configuration to linkage-report destination resolution. Fact collection edits no tasks. A real linkage_report still needs a resolvable report/log root and can refuse with linkage-report-unwritable; dry run computes facts without writing its per-call JSON report. Absence of config is not a promise of a successful no-file apply.

`_sprint_context(request, operation)` requires the shared `TaskDocument.is_sprint` predicate. A graphless sprint whose last master was retired remains a sprint through its retained retirement row, so ordinary linkage reads and later attachment still work. No retirement-only flag or caller assertion grants this identity. The module also carries the linkage request/error and serving-schema preflight boundary.

## Evidence

- Sprint admission uses the shared model predicate and captures accepted sources. [5]
- A master with command membership or a retained retirement row is a sprint. [6]

- SprintLinkageRequest threads the optional configuration to linkage-report destination resolution. Fact collection edits no tasks. A real linkage_report still needs a resolvable report/log root and can refuse with linkage-report-unwritable; dry run computes facts without writing its per-call JSON report. Absence of config is not a promise of a successful no-file apply. [7]
