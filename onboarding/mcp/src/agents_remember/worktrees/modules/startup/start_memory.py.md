# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/start_memory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:48+02:00 |
| lastVerifiedCommitHash |  `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`|
| lastVerifiedCommitDate |  2026-08-26T08:10:26+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Own external-memory admission and preparation during worktree start.

## Code Commentary

### Logic

The module settles the source memory branch, creates or reuses the memory worktree, synchronizes safe mtimes, detects divergence, and loads ledger/mapping state before start can publish a contract.

Mtime reuse skips `.git`, non-files, target-only files and known divergent paths; dry-run writes nothing. Missing source files are counted without failing the sync. Source-computable divergence keeps changed files fresh for indexing; an uncomputable divergence is explicitly reported by the current implementation. See `mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:79-134`.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| Memory source settlement precedes worktree and ledger preparation. | `prepare_memory_for_start`; `_ensure_memory_source_branch` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:39-64; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:67-76 |
| Mtime synchronization and divergence detection preserve exact file-state evidence. | `_sync_worktree_memory_mtimes`; `_memory_divergence_paths` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:79-118; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:121-134 |
| Disabled, missing-repository, ledger, and mapping outcomes are explicit. | `_disabled_memory_choice`; `_missing_memory_repo_state`; `_load_memory_ledger`; `_missing_mapping_state` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:137-140; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:143-151; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:154-179; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:182-196 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-06T22:00:40+00:00 — Preserved concrete mtime reuse boundaries from the retired test card against current source; previous verification pins remain unchanged.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.