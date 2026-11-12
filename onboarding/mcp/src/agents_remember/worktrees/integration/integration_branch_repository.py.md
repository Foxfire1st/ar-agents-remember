# mcp/src/agents_remember/worktrees/integration/integration_branch_repository.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Resolves the exact Git repository and local-branch facts consumed by integration authority without owning topology or lifecycle policy.

## Code Commentary

The module canonicalizes local branch spellings and symbolic aliases, resolves remote-only code default authority, admits the exact initialized external-memory default when its ref exists, and enumerates linked worktrees that own a canonical local branch. Each query fails closed when Git cannot prove the requested identity.

## Invariants And Boundaries

- Code repository defaults come only from a valid remote `origin/HEAD`; a local config value cannot replace PR-gated code authority.
- The local external-memory default is the exact `main` authority installed by `memory_init`, and its local ref must exist before lifecycle mutation.
- Symbolic aliases, cycles, malformed targets, and Git errors do not degrade to ordinary branch spellings.
- This module reports repository facts; task-derived protected-surface ownership remains in `integration_branch_authority.py`.

## Evidence

### Repo-Internal References

- Canonical local-branch identity rejects ambiguous symbolic authority. [1]
- Code and external-memory default resolvers keep their authority sources distinct. [2]
- Linked-worktree enumeration reports exact canonical branch owners. [3]

### Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Bounded Repository Failure Detail

Git failures while resolving canonical branch authority or linked-worktree ownership now surface
stable unreadable-authority messages. Raw stderr/stdout, repository paths, and backend-specific
detail stay behind this lowest repository boundary.

- Symbolic branch resolution translates Git failure to a bounded authority message. [4]
- Linked-worktree enumeration applies the same bounded failure posture. [5]

## 260918-TSIP-L6 `BranchAuthorityUnavailable`: A Condition, Not A Crash

`BranchAuthorityUnavailable` (`:11-28`) is new, and it is a **typed member of the product's error
family** (`AgentsRememberError`) rather than a bare `RuntimeError`, so a caller can answer it in
the response envelope instead of losing `ok`/`status`/`nextAction` to a traceback. The two raise
sites are `repository_default_branch` (`:58-69`, no `origin/HEAD`) and
`memory_repository_default_branch` (`:70-107`, the memory repository does not record its default
branch); each message already named its own remedy, which is what makes the condition answerable.

Deliberately **not** this class: a recorded authority that is malformed, or that names a ref which
does not resolve. Those refuse a state a caller must understand and change rather than an absence
a sibling tool already reports, and they keep raising — widening this type would move the boundary
the authority tests hold. The first consumer is
`application/memory_tools.py::memory_baseline_adopt_tool`, which now catches exactly this type
(`T34`).
