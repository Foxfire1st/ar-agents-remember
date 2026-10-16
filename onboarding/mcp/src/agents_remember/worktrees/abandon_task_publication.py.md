# mcp/src/agents_remember/worktrees/abandon_task_publication.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Join abandonment’s contract and task-document stage publication under the existing terminal guard.

## Code Commentary

The stage plan captures the canonical task and mirrored parent-row candidates before terminal completion. The guarded publication writes those documents and the updated contract; its rollback callback restores both the prior contract and captured document sources. The existing task-fact owner binds projection scopes to the exact candidates and rechecks source snapshots. This module does not choose abandonment authority, archive agents or bypass terminal admission.

## Evidence

- The existing terminal guard receives the paired publication and restoration callbacks. [1]
