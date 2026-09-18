# mcp/src/agents_remember/worktrees/modules/startup/start_memory.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/startup/start_memory.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `../overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](../overview.md)

## Purpose

Own external-memory admission and preparation during worktree start.

## Code Commentary

### Logic

`prepare_memory_for_start` settles internal, disabled, or external memory, requires the exact configured memory source branch, and creates or reuses the memory worktree. Its `lastVerifiedCodeCommit` and `lastMemoryContentCommit` response data come from `derive_memory_ledger` at the recorded memory base. An unattributed history produces empty informational values; a missing, stale, or malformed cached `memory.md` is not an admission condition.

Mtime reuse skips `.git`, non-files, missing source files, and known divergent paths. Missing source files are counted. A computable source/worktree diff leaves changed paths fresh for indexing; an uncomputable diff is explicitly reported. Dry-run does not create a worktree or synchronize mtimes.

### Conventions

Named branch and repository facts establish the memory source. The existing disabled-memory choice remains explicit; this module does not create a substitute protected source branch.

### Invariants And Boundaries

- The memory repository and exact source branch must exist for an external-memory start.
- Cache rows never select the code base or establish compatibility.
- Derived metadata reports only committed attribution; it does not invent a mapping for the selected code base.
- Worktree creation and mtime handling retain their existing dry-run boundary.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Source state, named-branch admission, and informational Git-derived metadata. | `_memory_source_state`; `memory_branch_state` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:19-32; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:48-48 |
| Mtime reuse and divergence handling preserve the current indexing behavior. | `_sync_worktree_memory_mtimes`; `_memory_divergence_paths` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:72-111; mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:74-113 |
| Missing external repository and explicit disabled-memory outcomes. | `_disabled_memory_choice`; `_missing_memory_repo_state` | mcp/src/agents_remember/worktrees/modules/startup/start_memory.py:136-144 |
| The informational ledger is reconstructed from commit attribution without a cache read. | `derive_memory_ledger`; "without consulting a cached file or a ledger commit" | mcp/src/agents_remember/kernel/memory_cache.py:22-41 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Removed the cached-file read and exact-row admission gate; retained repository/source validation, derived informational metadata, worktree creation, and mtime behavior. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-09-06T22:00:40+00:00 — Preserved concrete mtime reuse boundaries from the retired test card against current source; previous verification pins remain unchanged.


- 2026-08-24T14:48+02:00 — DAGQC cumulative CLIVE final-gap curation: created the strict source-mirroring card from current code. Verification hash/date remain blank for architect-owned final stamping.
