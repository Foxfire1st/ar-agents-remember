# mcp/src/agents_remember/cli/upgrade_user_settings.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The explicit whole-file settings upgrade command: preview or move the old coordination file to the user configuration directory.

## Code Commentary

`add_arguments` takes a required absolute `--coordination-root` and `--dry-run`. `run` refuses a relative root and delegates to the existing install owner, printing result JSON. Settings or OS exceptions print the old-path error and exit2; that wrapper is not an all-failure rollback guarantee. The install owner transfers the whole file exclusively, copies metadata before unlinking the old file, then attempts file0444/folder0555 closure. An OSError from that final closure is reported as permissionsNote without undoing the completed move; every normal answer includes the protection report.

## Evidence

- The explicit upgrade run moves the whole file once with refusal and dry-run. [1]
- The command takes coordination-root and dry-run arguments. [2]
