# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/start_memory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `f95487ec993b58d34911bba0206a7fa6ef9684eb`|
| lastVerifiedCommitDate |  2026-08-24T15:28:18+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Own external-memory admission and preparation during worktree start.

## Code Commentary

### Logic

The module settles the source memory branch, creates or reuses the memory worktree, synchronizes safe mtimes, detects divergence, and loads ledger/mapping state before start can publish a contract.

### Invariants And Boundaries

- External-memory state is resolved before ledger authority is consumed.
- Missing repository, mapping, or divergent paths return typed public failure evidence.
- Disabled memory is an explicit contract choice, not a fallback.
- No inferred compatibility branch substitutes for configured memory authority.

### Todos

None recorded.

## Docs References

No configured domain-documentation source applies to this repository-internal route.

## Repo-Internal References

| Finding | Source Range | Source Path |
| --- | --- | --- |
| Memory source settlement precedes worktree and ledger preparation. | L23-L78 | [source](mcp/src/agents_remember/worktrees/modules/startup/start_memory.py) |
| Mtime synchronization and divergence detection preserve exact file-state evidence. | L79-L136 | [source](mcp/src/agents_remember/worktrees/modules/startup/start_memory.py) |
| Disabled, missing-repository, ledger, and mapping outcomes are explicit. | L137-L203 | [source](mcp/src/agents_remember/worktrees/modules/startup/start_memory.py) |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
