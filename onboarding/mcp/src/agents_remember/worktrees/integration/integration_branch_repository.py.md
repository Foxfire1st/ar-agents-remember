# mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:51+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Resolves the exact Git repository and local-branch facts consumed by integration authority without owning topology or lifecycle policy.

## Code Commentary

The module canonicalizes local branch spellings and symbolic aliases, resolves remote-only code default authority, admits the exact initialized external-memory default when its ref exists, and enumerates linked worktrees that own a canonical local branch. Each query fails closed when Git cannot prove the requested identity.

## Invariants And Boundaries

- Code repository defaults come only from a valid remote `origin/HEAD`; a local config value cannot replace PR-gated code authority.
- The local external-memory default is the exact `main` authority installed by `memory_init`, and its local ref must exist before lifecycle mutation.
- Symbolic aliases, cycles, malformed targets, and Git errors do not degrade to ordinary branch spellings.
- This module reports repository facts; task-derived protected-surface ownership remains in `integration_branch_authority.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical local-branch identity rejects ambiguous symbolic authority. | `canonical_local_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:10-39 |
| Code and external-memory default resolvers keep their authority sources distinct. | `repository_default_branch`, `memory_repository_default_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:39-48; mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:51-79 |
| Linked-worktree enumeration reports exact canonical branch owners. | `branch_worktree_owners` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:113-133 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Bounded Repository Failure Detail

Git failures while resolving canonical branch authority or linked-worktree ownership now surface
stable unreadable-authority messages. Raw stderr/stdout, repository paths, and backend-specific
detail stay behind this lowest repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Symbolic branch resolution translates Git failure to a bounded authority message. | `canonical_local_branch` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:10-36 |
| Linked-worktree enumeration applies the same bounded failure posture. | `branch_worktree_owners` | mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py:113-133 |

## Update History

- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled bounded Git authority failures. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-16T03:24+02:00 — 260815-DAG-L4: split exact Git repository and branch facts from the integration authority owner to satisfy the bounded source-file size gate without duplicating policy. Verification remains closeout-owned.
