# mcp/tests/test_crossing_dependent_writer.py

## Governing Overview

[MCP tests](overview.md)

## Purpose

Exercise the mounted knowledge writer's dry plan for a dependent record changed on both sides of a crossing merge.

## Code Commentary

The fixture passes the series code branch reference to the crossing route. The plan updates the existing dependent and reports its next revision. The resolved code commit supplies the confirmation identity and tree. The test checks that the dry plan leaves the stored record and merge index unchanged.

## Evidence

- The crossing dry plan updates the existing record and confirms the resolved committed code state. [1]
