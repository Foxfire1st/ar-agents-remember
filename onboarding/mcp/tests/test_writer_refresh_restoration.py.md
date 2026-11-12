# mcp/tests/test_writer_refresh_restoration.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Describes the boundary between disappeared same-leaf refresh work and still-fired committed reconsideration after code reversion.

## Code Commentary

The first synthetic paired-tree case refreshes a link, reverts code so its fired item disappears, then asserts an empty writer operation restores the exact base link. The second commits the refreshed memory first; reverting code must leave refresh_not_current fired, and an empty write retains the authored refresh rather than treating it as the disappeared-item case.

## Invariants And Boundaries

Memory-base provenance changes the judgment. A code revert alone does not authorize resetting a committed link, and these source assertions are not a current run or acceptance result.

## Evidence Scope

No test execution, CODE/MEMORY grade, new producer capability or landing is claimed. No Domain Documentation source is configured for this slice.

## Evidence

- Describes the boundary between disappeared same-leaf refresh work and still-fired committed reconsideration after code reversion. Memory-base provenance changes the judgment. A code revert alone does not authorize resetting a committed link, and these source assertions are not a current run or acceptance result. [1]
