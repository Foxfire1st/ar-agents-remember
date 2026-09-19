# mcp/src/agents_remember/models/lifecycles/memory_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/memory_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

Declares the immutable wire identity for one exact external-memory leaf candidate pair.

## Code Commentary

### Logic

`ledgerPath` remains a consumer location in the wire identity, but `contractDigest` excludes
it. The digest binds repository, contract, candidate roots, source/work branches, bases, and
onboarding root. A cache refresh or absent cache cannot change this accepted pair identity.

`MemoryCandidatePairIdentity` carries the contract address and pair-authority digest together with
the exact code/memory roots, source and work branches, base commits, onboarding root, ledger path,
and repository id. The model is frozen and extra-forbid so acceptance evidence cannot silently
drop or invent an identity cell.

The digest covers this pair-authority projection rather than unrelated mutable lifecycle cells.
Consequently a review/closeout status update does not manufacture a new pair, while any root,
branch, base, onboarding, repository, or contract-address change does. The informational ledger
location is excluded from that digest.

### Conventions

Keep the identity frozen and extra-forbid; only its resolver computes the authority digest. Wire information and digest inputs are distinct.

### Invariants And Boundaries

- The schema identifies a relationship between two exact candidates, never a repository alone.
- Branch names are not sufficient identity; roots and bases are mandatory.
- The model contains identity only. It neither resolves paths nor switches branches.
- Candidate trees and delivery attempts remain separate identities owned by their respective
  acceptance records.

### Todos

No additional file-local TODO is established by this candidate review.

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The frozen pair identity retains ledgerPath as information excluded from its authority digest. | `MemoryCandidatePairIdentity` | mcp/src/agents_remember/models/lifecycles/memory_candidate.py:10-33 |
| The strict frozen pair wire contract declares every required authority cell. | `MemoryCandidatePairIdentity`; "Every contract cell that selects one worktree-backed memory candidate pair." | mcp/src/agents_remember/models/lifecycles/memory_candidate.py:10-33 |
| The resolver is the sole producer of this identity. | `resolve_memory_candidate_pair` | mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py:48-131 |

## Cross-Repo References

No cross-repository implementation reference applies; configured Agents Remember authority owns
both repository addresses.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separate external implementation source applies to this file. | — | — |
## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Separated the retained ledger-path consumer field from candidate-pair authority. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: repointed the resolver citation to its relocated `memory_quality/memory_candidate_pair.py` path (commit `0b63d6fc`). Verification metadata remains pinned because only the cut-affected reference was reconciled; source documentation only, no acceptance claim.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: moved the lifecycle identity under the lifecycle
  model package so the root models package remains within its structural limit; semantics are
  unchanged.

- 2026-08-29T21:46+02:00 — MCAR-L03: created the strict exact-pair identity. Candidate
  verification remains closeout-owned.
