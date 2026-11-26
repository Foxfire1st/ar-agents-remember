# mcp/src/agents_remember/worktrees/role_reports.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Collects agent-owned reports into canonical notes before working folders are reclaimed, within fixed budgets and without following links.

## Code Commentary

`canonical_group_messages` resolves the canonical task-record messages directory (the master's `notes/messages` for a series, or the leaf's messages folder from its terminal leaf document) so whole-folder terminal cleanup and abandon (`group_messages.collect_group_messages`) move out regular files from a real `messages` directory before deleting the task folder. `remove_group_role_folders` (used by directory-only sprint-archive retirement) still unlinks `messages` only when it is a symlink and preserves a non-link with `not-a-link-preserved`; linked canonical task-record message files are never followed or deleted.

Reclamation removes launch locators (and only those aliases): `close_execution_role_folders` removes a non-leaf request's locator after report collection, `remove_group_report_locators` removes a group's locators ahead of whole-folder terminal removal, and `remove_group_role_folders` removes each request folder's locator after collection for directory-only sprint-archive retirement, reporting the result under `handover-locators`. A name that is not the product's link, or that leads outside the folders being reclaimed, is left standing and reported, and nothing is removed when collection refused.

`collect_report_folder` copies safe regular files with size and link checks, skips unchanged files by recorded source/canonical stamps, stages through fsynced temp files with source/readback validation and atomic replacement, and refuses removal on any failure. Collection is bounded (10,000 entries, 2 GiB); oversize evidence must be archived first. `collect_execution_reports` and `collect_group_reports` serve receipts and terminal cleanup/abandon; legacy `task-reports` aliases are collected but only unlinked, never followed for deletion. `remove_group_role_folders` collects first and only then deletes local report, scratch, alias and task-document folders; `close_execution_role_folders` reclaims only confirmed archived or replaced non-leaf executions.

`COLLECTED_REPORT_DIRECTORY` (`"notes/reports"`) and derived `COLLECTED_REPORT_PARTS` sit beside `ROLE_REPORT_DIRECTORY` and `LEGACY_ROLE_REPORT_ALIAS` as the single definition of the collected report root consumed by `collect_group_reports` and every role-launch `taskReportRoot` producer (`cli/role_launch_enclosure.py`, `cli/role_launch_workspace.py`). `collected_report_ref(relative)` maps a relative path under `role-reports/` to `notes/reports/<rel>` (refusing empty or `..` traversal with `ValueError`); `is_collected_report_ref(reference)` returns `True` only for non-absolute task-relative `notes/reports/<rel>` paths without `..` traversal.

The explainer's report inventory uses the canonical collection named by each selected execution receipt. It lists regular text reports and admits a JSON measurement when an explicitly cited local path resolves to that collection. It excludes launch handovers and their detail carriers.

## Evidence


- Report folders copy safe regular files with stamp checks, fsynced staging and atomic replacement. [1]

- Execution receipts collect through the same collector. [2]

- Group collection serves terminal cleanup and abandon paths and targets `contract.task_root / COLLECTED_REPORT_DIRECTORY`. [3]
- `collected_report_ref` and `is_collected_report_ref` define and validate the canonical `notes/reports/<rel>` collected form beside `ROLE_REPORT_DIRECTORY`. [6]


- Canonical report discovery intersects cited JSON paths with eligible files in the execution collection. [5]

- Group folder removal collects evidence before reclaiming the local folders. [4]
