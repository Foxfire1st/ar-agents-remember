# mcp/src/agents_remember/tasks/progress.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Define presentation counts and the current work label separately from completion-readiness policy.

## Code Commentary

Total is the number of major steps; done is the number of major steps explicitly marked done. Nested steps neither add display units nor infer their parent completion.

Current work first scans major and nested units in declared order for inProgress or blocked state, then for an unfinished unit; empty/all-done work returns None. This label can name a nested unit even though the aggregate counts majors. The readiness owner still checks unresolved major and nested units; presentation progress is not permission to finalize.

## Evidence

- Major-only display counts coexist with nested current-work labels and separate readiness ownership. [1]
