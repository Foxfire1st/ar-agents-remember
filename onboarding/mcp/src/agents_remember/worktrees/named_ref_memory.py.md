# mcp/src/agents_remember/worktrees/named_ref_memory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/named_ref_memory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51 |
| lastVerifiedCommitHash | `420669c459aab3650cdaa5b3e5271e71d7d94c0e` |
| lastVerifiedCommitDate | 2026-09-17T10:54:08+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Returns a consumer `MemoryLedger` derived from one exact local memory branch, independently of
the ambient checkout and cached ledger files.

## Code Commentary

### Logic

`load_named_ref_ledger(repository, branch)` canonicalizes the branch through `local_branch_ref`
and passes that explicit `refs/heads/...` ref to `derive_memory_ledger`. It reads committed
attribution and returns the existing ledger data shape. A same-named tag or different checked-out
branch cannot substitute for the requested local branch.

Neither a committed `memory.md` blob nor its working copy is parsed. An unattributed history
contributes no mappings; an unreadable Git ref raises the attribution reader's error. This API has
no code-repository argument, so code-object filtering belongs to consumers that supply that
authority, such as `read_ledger_source(..., code_repository=...)`.

### Conventions

The kernel owns derivation and ledger representation; the shared Git module owns local-ref
normalization. This module adds no alternate lookup, table fallback, or write behavior.

### Invariants And Boundaries

- Only the explicit local branch's committed history is read.
- Cache absence, corruption, or forged rows cannot supply or override mappings.
- Genuine Git lookup failures remain distinguishable from an empty derived ledger.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reader derives attribution at the explicit normalized local branch. | `load_named_ref_ledger` | mcp/src/agents_remember/worktrees/named_ref_memory.py:12-15 |
| Local ref normalization and ledger derivation have shared owners. | `local_branch_ref` | mcp/src/agents_remember/worktrees/modules/git.py:79-85 |
| The kernel derives rows and current/base metadata from committed attribution. | `derive_memory_ledger` | mcp/src/agents_remember/kernel/memory_cache.py:22-41 |
| A tag sharing the source branch name cannot redirect the read, even with a damaged cache. | `test_cache_misses_preserve_contract_and_named_ref_history` | mcp/tests/test_memory_ledger.py:338-360 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T00:51 UTC — Replaced exact-ref memory.md blob parsing with exact-local-ref attribution derivation; documented empty-history and Git-failure behavior and updated the nearer worktrees overview link. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created named-ref memory ledger reader onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.

