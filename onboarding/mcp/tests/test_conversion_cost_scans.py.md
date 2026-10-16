# mcp/tests/test_conversion_cost_scans.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Protect deterministic conversion costs without changing table interpretation or anchor bytes. These source assertions are not elapsed-time budgets, installed acceptance or a final-cut RSS measurement.

## Code Commentary

The table-materialization case bounds scanner calls by the population of unfenced pipe-bearing lines at two prose sizes and checks concrete single/multi-column, escaped-pipe, code-span, fenced and malformed-header outcomes. The direct-Row case preserves constructed-row compatibility, table start/body results and equality with materialized rows. The blob case creates two separate `CodeObjects` instances and demands repeated counts and file/symbol/range content through two source paths; each instance splits the shared blob once while preserving CRLF, lone-CR and final-line bytes, and out-of-range content stays unresolved.

## Boundaries

The blob test uses a disposable repository through existing conversion support. Its two-instance split count is not a global parse-store promise. Registration in a lane/artifact catalog selects this evidence and does not establish that it ran. Memory overhead of the retained split-line cache is not measured here.

## Evidence

- Table materialization scans eligible lines at most once and preserves concrete boundary/cell results. [1]
- Directly constructed and materialized rows preserve table-boundary and equality behavior. [2]
- Each conversion-owned instance splits one blob once while repeated counts and content requests preserve byte semantics. [3]
