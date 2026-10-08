# mcp/src/agents_remember/models/worktree.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Defines the strict public worktree response and sync projection vocabulary.

## Code Commentary

SourceLineageProjection reports the applicable code/memory edges and recovery facts. SyncOperationProjection carries the journal's actual state, phase, conflicts and next arguments. SyncResolutionProjection describes the side, worktree and files requiring content resolution, with wipRestore distinguishing parked-WIP recovery. Resolution input admits only its declared action. The old SyncKnowledgeConflict and canonical dataset reconciliation fields were retired; these DTOs do not decide conflict content or authorize staging.

## Evidence

### Repo-Internal References

- `SourceLineageProjection` owns the current boundary described above. [67]
- `SyncOperationProjection` owns the current boundary described above. [68]
- `SyncResolutionProjection` owns the current boundary described above. [69]
- `SyncResolutionInput` owns the current boundary described above. [70]
