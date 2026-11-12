# dashboard/src/panels/detail-panel/worktreeSpine.tsx

## Purpose

Read-only worktree lanes for an entry-bound enclosure.

## Code Commentary

WorktreeSpine takes an enclosure and a group name and renders two lanes: the code checkout and its `ar-<repo>` memory twin. Each lane shows its repo name and one status line: `worktree present` or `worktree absent`, then the cleanup word the enclosure carries. The head names the supplied group name, else the repo name. Nothing here reads engine or provider state, so an enclosure recorded before the provider removal and one recorded after it render identically. An absent lane is only ever reported absent: the enclosure carries no field that separates a cleaned-up checkout from one that never existed.

## Governing Overview

[Area overview](../overview.md)

## Evidence

- Implementation [1]
