# mcp/src/agents_remember/worktrees/sync_transaction_git/_base.py

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Shared result and refusal vocabulary for exact managed-sync Git operations.

## Code Commentary

The memory domain excludes only its root memory.md cache; the code domain retains ordinary semantics for that name. Expected content distinguishes bytes, absence and failed construction rather than equating an unreadable path with valid absence. CancelTreeAssessment separates later work, unproved paths and explicitly stash-owned untracked paths. Later/unproved sets feed save-first recovery, not new ownership. Memory merge validation refusal leaves the staged merge; incoming fast-forward validation refusal is a source-line problem before refs move. SideMergeOutcome distinguishes a content stop from a repository-hook commit stop.

This module defines result/error vocabulary, not Git process execution. The Git mechanics use shared runners, while the repository commit-check owner can start Git/hook processes directly. `SyncGitProofError` exposes an unproved transition; its `SyncKnowledgeValidationError` subclass is handled first by the driver as `sync-knowledge-validation-refused`. Domain/path-specific cache stripping is never an ours/theirs policy for other files.

## Evidence

- ExpectedReappliedContent: qualified source contract. [1]
- CancelTreeAssessment: qualified source contract. [2]
- SyncKnowledgeValidationError: qualified source contract. [3]
- SyncFastForwardValidationError: qualified source contract. [4]

- SideMergeOutcome: qualified source contract. [5]
