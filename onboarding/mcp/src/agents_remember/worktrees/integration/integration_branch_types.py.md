# mcp/src/agents_remember/worktrees/integration/integration_branch_types.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_branch_types.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-21T00:45+02:00 |
| lastVerifiedCommitHash | `e5cb139f66abbd6502d4dcc4be883eb5f49770fe` |
| lastVerifiedCommitDate | 2026-08-21T00:28:23+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Defines the immutable data contracts exchanged by task-derived integration branch authority without owning repository queries or lifecycle policy.

## Code Commentary

The module holds the public protected-surface, integration-target, proposed-work-branch, and repository-checkout request records together with the resolver's internal repository-side, task scope, and master-authority projections. Keeping these dependency-light records outside the policy resolver preserves its public imports while the resolver, Git fact owner, and lifecycle callers retain one implementation each.

## Invariants And Boundaries

- Records are frozen values; they do not perform Git, task-document, or contract I/O.
- Surface side and kind vocabularies remain closed literals shared by all authority callers.
- Repository and branch policy remains in `integration_branch_authority.py`; exact Git facts remain in `integration_branch_repository.py`.
- The move is structural and supplies no compatibility fallback or alternate authority route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Surface and target records carry exact side, kind, repository, branch, and owner identity. | `IntegrationSurface`, `IntegrationTarget` | mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:17-23; mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:26-32 |
| Workbench and checkout requests carry the task and repository facts required by the resolver. | `ProposedWorkBranches`, `RepositoryCheckoutRequest` | mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:61-69; mcp/src/agents_remember/worktrees/integration/integration_branch_types.py:72-80 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## Update History

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_branch_types.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-16T07:02+02:00 — 260815-DAG-L4: moved the integration authority data contracts into a bounded dependency-light owner to satisfy the enforced source-file size contract without duplicating policy.