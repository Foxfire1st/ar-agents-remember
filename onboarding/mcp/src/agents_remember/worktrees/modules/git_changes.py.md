# mcp/src/agents_remember/worktrees/modules/git_changes.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Read exact Git-range file statuses and counts using NUL-delimited native output.

## Code Commentary

Name-status and numstat parsing preserve tabs, newlines and backslashes in file names. Rename/copy records consume both paths and report the destination; incomplete records raise instead of silently omitting a path. Binary counts remain None rather than measured zero. Working-tree mode includes nonignored untracked plain files as additions with decoded line counts; committed mode uses the explicit base/head range. Output sorts by path. Reads disable automatic index refresh to preserve real index generations. Separate Git reads and filesystem line counting are not a transaction or an atomic currentness guarantee.

## Evidence

- NUL status parsing and rename/copy destinations. [1]
- NUL numstat pairing and binary unknown counts. [2]
- Exact ranges, deletions and working untracked additions. [3]
