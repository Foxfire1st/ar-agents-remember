# mcp/tests/test_tool_entry_point_read_only.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

The read-only mark's sweep cases (MIK-R109 rule 7): a tool that only reads says so, and no advertised read writes the world.

## Code Commentary

The cases require every registered tool to stand in exactly one part of the read list and every advertised mark to match that list. They then run each marked read and compare the coordination and repository censuses, so a read that changes a file fails. `_read_variants` adds non-default invocations that are still read-only, including legacy-argument refusals, unknown views and absent contracts: each answers inside the envelope and is watched too, so a refusal path cannot hide a mutation. The controls require the sweep to catch a git metadata write, a non-index runtime write and an ordinary write, and require a freshness fetch to write only under a false mark. The census ignores the log and knowledge-index paths, which reads are allowed to touch.

## Invariants And Boundaries

A refusal is still an invocation: it is swept like an answer. The ignored prefixes are named constants rather than a filter at the assertion, so what a read may write is stated once.

## Evidence

### Repo-Internal References

- Every advertised read changes no file of the coordination root or the repositories. [1]

- The sweep catches a git metadata write, a runtime write outside the index and an ordinary write. [2]
