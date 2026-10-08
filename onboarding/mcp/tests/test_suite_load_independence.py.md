# mcp/tests/test_suite_load_independence.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Guards the repository's Python test/support timing patterns and the product's closed process-state
register. Findings name a path, line and rule; the guards do not certify arbitrary scheduling or
state behavior.

## Code Commentary

The timing scanner traverses Python syntax, detects short literal timeouts/defaults/module wait
constants and clock deadlines, fixed sleeps without a condition (including bounded poll loops),
and elapsed-clock comparisons with literal numbers. Clock-derived local names propagate through
assignments. A real comment on the finding line or preceding line may explain
`load-independent: <reason>`; strings containing that text are not exemptions. Condition polling is
allowed, and the shared waits owner is excluded from the repository sweep.

The process-state scanner detects empty module collections, `global` declarations, supported
cache decorators and assignments to known class attributes, resolving import aliases where those
patterns use them. Its exact discovered set must match the register with no duplicates or stale rows.
The syntactic scan is deliberately bounded: it does not discover every mutation, alias or dynamic
state allocation, and a reasoned marker is an explicit exception rather than a runtime proof.

## Evidence

The tests inject scanner examples and prove that an unreached shared wait names its condition.


- Timing violations are path-line-rule findings from the bounded AST scanner. [1]
- The state guard compares syntactically found owners with the closed register in both directions. [2]
- Real comments exempt explained patterns while string literals do not. [3]
- Shared waits report the unreached sync or async condition. [4]
