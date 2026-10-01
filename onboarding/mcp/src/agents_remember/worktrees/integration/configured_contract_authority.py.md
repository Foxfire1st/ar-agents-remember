# mcp/src/agents_remember/worktrees/integration/configured_contract_authority.py

## Governing Overview

[worktree integration overview](overview.md)

## Purpose

Current configured-contract authority at a mutation boundary.

## Code Commentary

### Logic

The public surface is `reread_configured_contract`, `require_configured_contract_repositories`. The mutation owner re-reads the already admitted configured contract under its existing serialization and compares exact repository authority. Repository roots and external-memory separation are always checked. Candidate-worktree identity is also checked by default; an exact-pair consumer may explicitly delegate only that live-candidate check to the canonical pair validator by passing `require_candidate_identity=False`. It translates expected reread failures through the shared admission refusal projector; it does not become a second public admission API or add a common lock.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- The candidate-identity option is strict by default and is a single-owner transfer to exact-pair
  validation, not a weakened repository-authority mode or fallback.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

### Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

- The module defines `reread_configured_contract`; `require_configured_contract_repositories` as its public seam. [1]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Live Versus Terminal Authority

Configured repository identity is now separated from candidate-worktree presence.
`require_configured_terminal_contract_repositories` validates configured code/external-memory
repositories and their separation for an archived-terminal retry without requiring worktrees that
cleanup already deleted. Ordinary live mutations still require the candidate code and leaf-memory
identities. Terminal mode is a narrow finalization authority, never a generic fallback.
