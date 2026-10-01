# mcp/src/agents_remember/models/lifecycles/memory_candidate.py

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

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

- The frozen pair identity retains ledgerPath as information excluded from its authority digest. [1]
- The strict frozen pair wire contract declares every required authority cell. [2]
- The resolver is the sole producer of this identity. [3]

### Cross-Repo References

No cross-repository implementation reference applies; configured Agents Remember authority owns
both repository addresses.


No separate external implementation source applies to this file.
