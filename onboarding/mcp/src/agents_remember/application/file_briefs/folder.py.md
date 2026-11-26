# mcp/src/agents_remember/application/file_briefs/folder.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Writes derived file briefs and folder indexes inside a memory root.

## Code Commentary

A file lock serializes full and partial writes. Full writes replace previous output and record the memory tree in briefs/TREE. They preserve the index-free `briefs/_task/` folder for role-start reports. Partial writes refresh individual briefs and their folder indexes.

## Evidence

- The folder writer serializes publication and preserves the task-moment directory during a full refresh. [1]
- The first-line reader distinguishes a missing file from unreadable or unrecognized header bytes. [2]
