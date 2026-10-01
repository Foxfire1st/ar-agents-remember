# mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py

## Governing Overview

[Nearest governing overview](../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Validates an existing master-series contract against the commanding sprint's declared task,
repository/memory, and branch edges, and returns bounded actionable startup refusals.

## Code Commentary

### Logic

`MasterSeriesContractSpecLike` describes the required identity inputs. The evidence/error types
retain contract location and expected/observed edge values. `_master_series_admission_refusal`
projects that evidence into the shared atomic-series response with bounded parser details and a
contract-addressed read-only `worktree_status` action.

`_existing_master_series_contract` treats absence as bootstrap, preserves unreadable/wrong-kind
errors, and treats terminal cleanup artifacts as no longer owning a live lane. A live series must
match task identity, actual repository identity/memory mode, and exact source/work branches.

The repository helpers require real Git roots and compare shared repository identity rather than
path spelling. `_same_series_memory_edge` now checks only the actual memory repository and optional
worktree relationship. With no external repository, no external memory worktree may remain; with
one, the repository must resolve and any worktree must belong to it. Cache path equality is no
longer part of this admission edge.

### Conventions

Expected contract mismatches return typed startup evidence rather than exposing tracebacks.
The three edge groups remain separate so a refusal identifies the actual mismatch. This module
validates existing state; it does not repair contracts or move branches.

### Invariants And Boundaries

- Task, repository/memory mode, and branch identity retain independent checks.
- External-memory admission depends on actual repository/worktree ownership, not memory.md location.
- Cache absence or a different cache path is not a replacement for a real repository mismatch.
- Terminal artifacts may permit fresh bootstrap; live mismatched artifacts still refuse.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- Typed admission evidence and bounded refusal projection. [1]
- Existing contracts are classified before the separate edge checks. [2]
- External memory is checked through real repository/worktree identity without a ledger-path argument. [3]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
