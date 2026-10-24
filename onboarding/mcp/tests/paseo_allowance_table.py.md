# mcp/tests/paseo_allowance_table.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Holds the vocabulary and the per-file allowance table the Paseo single-path scan is judged against (PNT-R02): for one rule and one file, how many uses are AR's own and the reason each is.

## Code Commentary

The nine rule names carry their reason strings (`PACKAGE`, `PROGRAM`, `LITERAL`, `COMMAND_LINE`, `RUNNER`, `SCRIPT`, `ADDRESS`, `SHELL`, `MANIFEST`), and three path prefixes group the callers: the CLI, the serving runtime and the PNT sandbox tooling. `ALLOWED` maps six of those names to entries of the form file to a count and a reason: package names, bare string literals, command-line beginnings, the runtime runner and repository addresses. `PROGRAM` is present with no file granted, and `SCRIPT`, `SHELL` and `MANIFEST` have no entry at all. The scan itself, its regexes and its planted cases live in the sibling single-path module.

## Invariants And Boundaries

A file may trip a rule exactly as often as its entry says. One use more is a second path until it is counted here with its reason, and an entry whose file is gone or trips the rule less often than its number says is stale; both fail the checkout scan. A legitimate second surface therefore needs an entry, not a wider prefix.

## Evidence

### Repo-Internal References

- Every allowance is a count and a written reason, per rule and per file, in the one table. [1]

- The three path prefixes and the nine rule names are the vocabulary the scan reports in. [2]
