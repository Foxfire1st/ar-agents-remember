# mcp/src/agents_remember/worktrees/sync_transaction_state.py

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Strict enclosure-root durable state for one resumable sync generation.

## Code Commentary

### Logic

Side records pin repositories/worktrees/branches, source/pre-sync/base facts, authority refs, phase progress, file conflicts, structural report and parked stash/path facts. Operation records bind generation and original bases; quarantine preserves damaged evidence without rollback authority. [4]

The narrow _drop_retired_knowledge_keys adapter removes old knowledgeConflict and knowledgeReconciliations on read because a sync already in flight at retirement must resume/cancel. No current row diagnosis/decision is stored; other extras remain forbidden. [7]

The stable store rejects malformed/nonregular normal records and preserves evidence before explicit recovery. Projection distinguishes retained merge from parked reapply, and empty structural report is omitted. [5] [6]

### Invariants And Boundaries

- Observation grants no mutation authority.
- Old keys are read tolerance, never a current reconcile route.

## Evidence

### Repo-Internal References


- Current strict side/operation records. [4]


- Optional report serialization. [5]


- Retained phase/parked candidate projection. [6]


- Specific old-key adapter and current file resolution. [7]


### Cross-Repo References

No cross-repository contract is established by this file.
