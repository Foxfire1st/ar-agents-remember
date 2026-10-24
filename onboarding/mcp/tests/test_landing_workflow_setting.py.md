# mcp/tests/test_landing_workflow_setting.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Pins the landing-workflow setting and its single reader: the value lives in a repository's memory settings under `landing`, a missing key means a local landing, and any other spelling is refused by name at the parse.

## Code Commentary

The suite builds settings documents and asserts what the parser makes of each one, so the accepted spellings and the default are checked where they are consumed rather than described in prose. The refused spellings are exercised as refusals, which is what makes the parser's strictness a tested property instead of a convention.

## Invariants And Boundaries

The suite covers the parser for the setting; it does not read a live repository or prove that a publication run honoured the value. A landing that ignores the setting is a different defect, proven by the operation traces that exercise the guard.

## Evidence

### Repo-Internal References

- The suite pins the setting’s accepted value, its default and the refused spellings. [1]
