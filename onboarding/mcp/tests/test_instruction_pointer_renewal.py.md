# mcp/tests/test_instruction_pointer_renewal.py

## Governing Overview

[Overview](overview.md)

## Purpose

Checks pointer-policy preservation and corrective renewal diagnostics through fixture commands.

## Code Commentary

The cases withdraw generated rows, reject unadmitted pointers, check reader and CLI diagnostics, and require retained policy to be used before pruning. Retry and repair cases distinguish unresolved authoring input from successful renewal. No result is inferred merely from these test definitions.

## Relationships

These cases load the pointer planner through `instruction_renewal.renewal_module`; they define their withdrawal and retry fixtures in this module. Product errors expose the canonical next action rather than a traceback.

## Evidence


- Retained policy is checked before pruning and repaired fixtures can renew. [2]

### Repo-Internal References (renewed)

- Tests use the checkout’s renewal_module loader and local withdrawal fixture, reject unadmitted or dangling pointers, and expose the canonical remedy. [1]
