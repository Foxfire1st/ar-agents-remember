# mcp/src/agents_remember/worktrees/integration/configured_contract_authority.py

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Current configured-contract authority at a mutation boundary. Re-proves configured repository/contract authority at existing mutation boundaries.

## Code Commentary

The public surface is `reread_configured_contract` and `require_configured_contract_repositories`. The mutation owner re-reads the already admitted configured contract under its existing serialization and compares exact repository authority. `require_configured_contract_repositories` returns the same `RepositoryScope` whose identity it checked, so callers that need the authoritative roots perform no second, potentially inconsistent settings read.

A contract that carries the removed `disabled` mode is admitted here only with `allow_disabled_memory` — the status, attach, and guarded-abandon path. Every other route refuses it with the opt-out refusal before reaching here. With the flag set and a non-external mode, the check runs through `_require_configured_repository_authority_except_mode`: configured code-repository authority and candidate-worktree identity are still proved, but the memory-mode comparison and the external-memory separation check are skipped. Without the flag, repository roots, external-memory separation, and the mode comparison are all checked, and candidate-worktree identity is checked by default; an exact-pair consumer may explicitly delegate only that live-candidate check to the canonical pair validator by passing `require_candidate_identity=False`. The mode comparison itself stays in `_require_configured_repository_authority`, so the except-mode split cannot silently become the default.

`require_configured_terminal_contract_repositories` binds archived deletion authority without requiring already-deleted candidates, with the same allow-flag shape: a mode-only mismatch is admitted only under the flag, and cleanup otherwise keeps its external-only shape.

It translates expected reread failures through the shared admission refusal projector; it does not become a second public admission API or add a common lock. Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.

## Evidence

- Live authority with the mode-excepted admission path [3]
- Terminal authority with the same allow shape [4]
- Mode comparison stays in the strict path [5]
- Allow path checks everything except the mode [6]
- External-memory separation check, strict path only [7]
- Already-admitted contract reread under serialization [8]
