# mcp/src/agents_remember/models/lifecycles/memory_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/memory_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T05:55+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

Declares the immutable wire identity for one exact external-memory leaf candidate pair.

## Code Commentary

`MemoryCandidatePairIdentity` carries the contract address and pair-authority digest together with
the exact code/memory roots, source and work branches, base commits, onboarding root, ledger path,
and repository id. The model is frozen and extra-forbid so acceptance evidence cannot silently
drop or invent an identity cell.

The digest covers this pair-authority projection rather than unrelated mutable lifecycle cells.
Consequently a review/closeout status update does not manufacture a new pair, while any root,
branch, base, onboarding, ledger, repository, or contract-address change does.

## Invariants And Boundaries

- The schema identifies a relationship between two exact candidates, never a repository alone.
- Branch names are not sufficient identity; roots and bases are mandatory.
- The model contains identity only. It neither resolves paths nor switches branches.
- Candidate trees and delivery attempts remain separate identities owned by their respective
  acceptance records.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The strict frozen pair wire contract declares every required authority cell. | `MemoryCandidatePairIdentity` | mcp/src/agents_remember/models/lifecycles/memory_candidate.py:10 |
| The resolver is the sole producer of this identity. | `resolve_memory_candidate_pair` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py:48-144 |

## Cross-Repo References

No cross-repository implementation reference applies; configured Agents Remember authority owns
both repository addresses.

## Update History

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: moved the lifecycle identity under the lifecycle
  model package so the root models package remains within its structural limit; semantics are
  unchanged.

- 2026-08-29T21:46+02:00 — MCAR-L03: created the strict exact-pair identity. Candidate
  verification remains closeout-owned.
