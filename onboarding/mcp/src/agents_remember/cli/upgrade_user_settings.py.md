# mcp/src/agents_remember/cli/upgrade_user_settings.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The explicit whole-file settings upgrade command: preview or move the old coordination file to the user configuration directory.

## Code Commentary

`add_arguments` takes a required absolute `--coordination-root` and `--dry-run`. `run` refuses a relative root and delegates to the install owner's `upgrade_user_settings`, printing the result JSON; settings or OS failures print an error naming the old path and exit non-zero without migrating anything.

## Evidence

- The explicit upgrade run moves the whole file once with refusal and dry-run. [1]
- The command takes coordination-root and dry-run arguments. [2]
