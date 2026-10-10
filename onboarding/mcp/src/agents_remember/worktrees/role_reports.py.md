# mcp/src/agents_remember/worktrees/role_reports.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Collects agent-owned reports into canonical notes before working folders are reclaimed, within fixed budgets and without following links.

## Code Commentary

`collect_report_folder` copies safe regular files with size and link checks, skips unchanged files by recorded source/canonical stamps, stages through fsynced temp files with source/readback validation and atomic replacement, and refuses removal on any failure. Collection is bounded (10,000 entries, 2 GiB); oversize evidence must be archived first. `collect_execution_reports` and `collect_group_reports` serve receipts and terminal cleanup/abandon; legacy `task-reports` aliases are collected but only unlinked, never followed for deletion. `remove_group_role_folders` collects first and only then deletes local report, scratch, alias and task-document folders; `close_execution_role_folders` reclaims only confirmed archived or replaced non-leaf executions.

## Evidence

- Report folders copy safe regular files with stamp checks, fsynced staging and atomic replacement. [1]
- Execution receipts collect through the same collector. [2]
- Group collection serves terminal cleanup and abandon paths. [3]
- Folder removal collects first and only then deletes. [4]
