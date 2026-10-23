# mcp/src/agents_remember/worktrees/abandon_task_publication.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Join abandonment’s contract and task-document stage publication under the existing terminal guard.

## Code Commentary

The stage plan captures the canonical task and mirrored parent-row candidates before terminal completion. Publication passes the original and final contracts to the shared native outcome owner, which selects the admitted no-remains proof or the strict archive-backed proof before the transaction starts. The guarded publication writes those documents and the updated contract, and around that write it opens one abandoned-occurrence notice: the intent is discarded only when the publication raises before the native commit has committed, and it is kept for
recovery when a later cleanup raises after that commit; it is confirmed only after the publication succeeds, so a refused abandonment announces nothing; its rollback callback restores both the prior contract and captured document sources. The existing task-fact owner binds projection scopes to the exact candidates and rechecks source snapshots. This module does not choose abandonment authority, archive agents or bypass terminal admission.

## Evidence

- The existing terminal guard receives the paired publication and restoration callbacks. [1]
