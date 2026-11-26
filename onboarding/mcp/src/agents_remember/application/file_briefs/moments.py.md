# mcp/src/agents_remember/application/file_briefs/moments.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Composes the Reviewer and Curator start notices and their detailed files.

## Code Commentary

The composer checks tracked and untracked worktree changes against the task base and counts each touched rule once. It puts moved rules first. When the message limit admits the minimum notice, the bounded text keeps the counts and the full report pointer. With converted memory the file goes to `briefs/_task/` when Git effectively excludes it. Otherwise it goes to the recipient's recorded task scratch. The notice for unconverted memory has no file.

## Evidence

- The composer binds the memory root and changed paths before writing the role’s report. [1]
