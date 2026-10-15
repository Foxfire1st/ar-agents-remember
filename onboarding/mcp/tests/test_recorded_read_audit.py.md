# mcp/tests/test_recorded_read_audit.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Describes isolated interpreter audits of retained versus examined filesystem dependencies for worklist, gate and reviewer computation.

## Code Commentary

The child script builds an explicit fixture and records open/list/scandir events under the coordinator, excluding object stores and writes. Each observed dependency must occur in recorded_reads or examined. The reviewer computation owner is deliberately inlined in this audited child; transport is not being tested by that seam. A ruled-out master must be opened and examined but absent from kept reads. The mutant reads an unused task file and must produce an unrecorded failure.

## Invariants And Boundaries

The parent launches Python directly, not nested pytest, and checks the child result. Source-defined audit coverage and a mutation control do not establish that this candidate was executed or that unrelated host files were audited.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- Describes isolated interpreter audits of retained versus examined filesystem dependencies for worklist, gate and reviewer computation. The parent launches Python directly, not nested pytest, and checks the child result. Source-defined audit coverage and a mutation control do not establish that this candidate was executed or that unrelated host files were audited. [1]
