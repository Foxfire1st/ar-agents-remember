# mcp/src/agents_remember/application/knowledge_worklist/recorded_base.py

## Governing Overview

[Application overview](../overview.md)

## Purpose

Resolve the memory base named by a leaf worktree contract before a caller compares memory.

## Code Commentary

The resolver reads `memory.base_commit` as a commit and verifies that Git can name its tree. It checks ancestry against the memory commit supplied by a leaf pair judgment or against the real memory worktree's HEAD for a live comparison. A captured candidate tree supplies content without supplying an ancestry witness.

A missing or unreadable base, unreadable ancestry input, or unrelated base raises `RecordedMemoryBaseError`. The caller maps that exception to its own incomplete, unavailable or refused response.

## Relationships

The worklist, onboarding trace, writer card comparison, live review and carry-over use this resolver for leaf memory. Explicitly held comparison sides retain their captured base.

## Evidence

- The leaf base is the contract's readable commit and tree, with ancestry checked against the judged memory commit or the real memory worktree's HEAD. [1]
- Git revision failures become a recorded-memory-base error. [2]
- The leaf pair judgment refuses an unrelated judged commit even when its memory tree matches the accepted one. [3]
