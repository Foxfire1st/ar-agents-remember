# mcp/src/agents_remember/worktrees/integration/integration_branch_types.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Defines the immutable data contracts exchanged by task-derived integration branch authority without owning repository queries or lifecycle policy.

## Code Commentary

The module holds the public protected-surface, integration-target, proposed-work-branch, and repository-checkout request records together with the resolver's internal repository-side, task scope, and master-authority projections. Keeping these dependency-light records outside the policy resolver preserves its public imports while the resolver, Git fact owner, and lifecycle callers retain one implementation each.

## Invariants And Boundaries

- Records are frozen values; they do not perform Git, task-document, or contract I/O.
- Surface side and kind vocabularies remain closed literals shared by all authority callers.
- Repository and branch policy remains in `integration_branch_authority.py`; exact Git facts remain in `integration_branch_repository.py`.
- The move is structural and supplies no compatibility fallback or alternate authority route.

## Evidence

### Repo-Internal References

- Surface and target records carry exact side, kind, repository, branch, and owner identity. [1]
- Workbench and checkout requests carry the task and repository facts required by the resolver. [2]

### Documentation References

No configured domain-documentation or cross-repository source applies to this file.
