# operations/recovery.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

Restore the same canonical AR task, admitted workspace and role agent after interrupted or uncertain execution.

## Current Contract

Recover saved task, request, agent, recipient, report and candidate references from the durable handover. A repeated `role_start` with the same request ID reconciles the same agent. Unknown message delivery remains addressed to the same agent; an unresolved result remains unknown with its IDs.

An existing leaf retains its admitted code/memory/contract pair. The bound server supplies canonical task/worktree facts; a resume restores execution rather than requirement acceptance or Git publication.

## Conventions

Canonical skills/l-01-agent-lifecycles/operations/recovery.md owns the instruction. scripts/sync-skills.py regenerates this exact packaged copy and the eight harness copies; no generated file defines a separate obligation.

## Invariants And Boundaries

No new owner, parallel Paseo Git worktree, global memory root, alternate transport, private store or background poller is created to bypass uncertainty or refusal. Name the actual prerequisite or missing semantic field and return it to its owner.

## Code Commentary

### Todos

None recorded.

## Evidence

### Repo-Internal References

| Finding | Anchor | References |
| --- | --- | --- |
| Saved exact identity, same-request reconciliation, paired workspace and visible unknown outcome. | lines 3-7 | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/operations/recovery.md:3-7 |

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The operation block's declared purpose, source path, and applicable roles. [1]
- The canonical source of this block. [2]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
