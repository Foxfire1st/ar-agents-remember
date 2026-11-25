# scripts/renew-instructions.py

## Governing Overview

[Overview](../overview.md)

## Purpose

Provides the public command for renewing instruction facts and declared package copies from canonical authored inputs.

## Code Commentary

The command builds the complete plan before publishing replacements. `--check` reports changed JSON leaves, file presence or file bytes without applying the plan and returns failure when replacements remain. `--list-targets` reports carriers before constructing a renewal plan. Repeated bindings use `--bind-unit UNIT=FILE:START-END`, `UNIT@evidence:N=FILE:START-END` for one evidence association, `UNIT@clause:PLACE:N=FILE:START-END` for one clause, and `--bind-pointer ID=FILE:LINE`. They supply explicit choices where the planners require them. The command prepends both `mcp/src` and `mcp/test_support` to `sys.path`; the manifest and pointer planners import the repository test-support helpers.

## Relationships

The planner owns computation and publication. This command renders its notices and errors and names `mcp/.venv/bin/python scripts/renew-instructions.py` as the remedy for stale generated values.

The contributor guide prescribes renewal for instruction facts and the generated skills and tool-details copies. The skills reference directs contributors to run the same command for the generated skills copy and points to the contributor guide. The release checklist requires a clean renewal check and current facts and package copies. The Git hook checks the generated skills with renewal alongside the projection and runtime copy checks.

## Evidence



- Checking reports differences without applying replacements; renewal applies the computed plan. [1]
- Diagnostics distinguish changed JSON leaves from file presence and raw byte changes. [2]

### Repo-Internal References (renewed)

- The command and its manifest/pointer planners load repository test support. [3]

- The contributor guide gives the command for instruction facts and the generated skills and tool-details copies, with a read-only check mode. [4]
- The skills reference names the exact renewal command for the generated skills copy and points to the contributor rules. [5]
- The release checklist requires a clean renewal check and current instruction facts and package copies, including tool-details. [6]
- The hook checks projection, skills and runtime copies. Skills use the instruction renewal command. [7]
- The hook runs the named copy checker with the check flag. [8]
- The fast tier invokes the generated copy checks. [9]
- The targeted tier invokes the fast tier. [10]
