# mcp/src/agents_remember/models/lifecycles/memory_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/memory_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash |  `7cbda30d9a9a4c2944382fbef46ac58b85329935`|
| lastVerifiedCommitDate |  2026-09-15T05:15:42+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured external domain source applies. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The frozen pair identity retains ledgerPath as information excluded from its authority digest. | L10-L33 | [mcp/src/agents_remember/models/lifecycles/memory_candidate.py](mcp/src/agents_remember/models/lifecycles/memory_candidate.py) |
| The strict frozen pair wire contract declares every required authority cell. | L10-L33 | [mcp/src/agents_remember/models/lifecycles/memory_candidate.py](mcp/src/agents_remember/models/lifecycles/memory_candidate.py) |
| The resolver is the sole producer of this identity. | L48-L129 | [mcp/src/agents_remember/memory_quality/memory_candidate_pair.py](mcp/src/agents_remember/memory_quality/memory_candidate_pair.py) |

## Cross-Repo References

No cross-repository implementation reference applies; configured Agents Remember authority owns
both repository addresses.


| Finding | Citations | Source Path |
| --- | --- | --- |
| No separate external implementation source applies to this file. | N/A | N/A |
## Update History

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Separated the retained ledger-path consumer field from candidate-pair authority. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


- 2026-09-11T10:26:37+02:00 — De-entanglement cut cleanup at code commit `2fa5e81f`: repointed the resolver citation to its relocated `memory_quality/memory_candidate_pair.py` path (commit `0b63d6fc`). Verification metadata remains pinned because only the cut-affected reference was reconciled; source documentation only, no acceptance claim.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: moved the lifecycle identity under the lifecycle
  model package so the root models package remains within its structural limit; semantics are
  unchanged.

- 2026-08-29T21:46+02:00 — MCAR-L03: created the strict exact-pair identity. Candidate
  verification remains closeout-owned.
