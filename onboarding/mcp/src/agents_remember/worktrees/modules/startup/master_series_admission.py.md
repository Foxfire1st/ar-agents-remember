# mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `../overview.md` |

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

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Typed admission evidence and bounded refusal projection. | `MasterSeriesContractSpecLike`; `_master_series_admission_refusal` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:100-159 |
| Existing contracts are classified before the separate edge checks. | `_existing_master_series_contract` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:153-215 |
| External memory is checked through real repository/worktree identity without a ledger-path argument. | `_repository_root`; `_same_master_repository_edge` | mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:253-385; mcp/src/agents_remember/worktrees/modules/startup/master_series_admission.py:253-269 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:02 UTC — Removed the documented ledger-path equality requirement from the series memory edge; retained real Git-root/worktree, task, memory-mode, branch, and bounded-refusal behavior. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-08T19:16:43+02:00 — CCR-L38 CQ04 preparation rebound the refusal projector after oversized malformed-contract diagnostics were reproduced. Public and observed detail now retain bounded parser evidence; focused proof remains non-certifying and closeout-owned.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ04 preparation reconciled the authoritative contract reread and preserved concrete `ContractError` parser detail in typed observed evidence. The validator/test result is source evidence only; verification remains closeout-owned with no acceptance claim.
- 2026-09-08T17:36:08+02:00 — CCR-L38 source-grounded preparation added the one-to-one sidecar for the current `master_series_admission.py` edge validator and refusal projector. The source remains uncommitted; the base metadata is retained and closeout owns the eventual verification stamp. No acceptance or Gate 5 claim.
