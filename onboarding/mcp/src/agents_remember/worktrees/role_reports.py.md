# mcp/src/agents_remember/worktrees/role_reports.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Collects agent-owned reports into canonical notes before working folders are reclaimed, within fixed budgets and without following links.

## Code Commentary

`canonical_group_messages` resolves the canonical task-record messages directory (the master's `notes/messages` for a series, or the leaf's messages folder from its terminal leaf document) so whole-folder terminal cleanup and abandon (`group_messages.collect_group_messages`) move out regular files from a real `messages` directory before deleting the task folder. `remove_group_role_folders` (used by directory-only sprint-archive retirement) still unlinks `messages` only when it is a symlink and preserves a non-link with `not-a-link-preserved`; linked canonical task-record message files are never followed or deleted.

Reclamation removes launch locators (and only those aliases): `close_execution_role_folders` removes a non-leaf request's locator after report collection, `remove_group_report_locators` removes a group's locators ahead of whole-folder terminal removal, and `remove_group_role_folders` removes each request folder's locator after collection for directory-only sprint-archive retirement, reporting the result under `handover-locators`. A name that is not the product's link, or that leads outside the folders being reclaimed, is left standing and reported, and nothing is removed when collection refused.

`collect_report_folder` copies safe regular files with size and link checks, skips unchanged files by recorded source/canonical stamps, stages through fsynced temp files with source/readback validation and atomic replacement, and refuses removal on any failure. Collection is bounded (10,000 entries, 2 GiB); oversize evidence must be archived first. `collect_execution_reports` and `collect_group_reports` serve receipts and terminal cleanup/abandon; legacy `task-reports` aliases are collected but only unlinked, never followed for deletion. `remove_group_role_folders` collects first and only then deletes local report, scratch, alias and task-document folders; `close_execution_role_folders` reclaims only confirmed archived or replaced non-leaf executions.

The explainer's report inventory uses the canonical collection named by each selected execution receipt. It lists regular text reports and admits a JSON measurement when an explicitly cited local path resolves to that collection. `_launch_carrier` excludes launch handovers (`.handover.txt`, `.handover.json`), legacy flat detail snapshots (`<stem>.detail-*`), nested detail trees (`<stem>.details/**`), direct opening offload sidecars (`<stem>.opening-message.md`), and held-batch offload sidecars (`<stem>.held-batch-*.md`).

## Evidence


- Report folders copy safe regular files with stamp checks, fsynced staging and atomic replacement. [1]

- Execution receipts collect through the same collector. [2]
- Group collection serves terminal cleanup and abandon paths. [3]
- Canonical report discovery intersects cited JSON paths with eligible files in the execution collection. [5]

- Group folder removal collects evidence before reclaiming the local folders. [4]

- `_launch_carrier` excludes `.handover.txt`, `.handover.json`, legacy `.detail-*`, nested `.details/**`, `.opening-message.md`, and `.held-batch-*.md` launch carriers from `canonical_execution_reports`. [7]
