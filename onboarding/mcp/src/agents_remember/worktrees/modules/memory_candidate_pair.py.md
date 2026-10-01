# mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py

## Governing Overview

[worktrees modules overview](overview.md)

## Purpose

Owns the one read-only resolver that admits and re-proves an exact external-memory leaf pair.

## Code Commentary

### Logic

`ledgerPath` is derived as `<memoryRoot>/memory.md` for consumers and is excluded from
`contractDigest`. Resolution does not require the cache file to exist or parse and does not admit
a caller-supplied cache path. The memory source head is checked against the actual accepted
`integrated_memory_content_commit`, while repository identity, work branches, bases, and ancestry
remain authoritative.

`resolve_memory_candidate_pair` compares the requested address and repository with the admitted
contract, rereads that same contract, and requires an external leaf with live code, memory,
and onboarding paths. It proves both worktrees belong to the recorded repositories, the
recorded work branches are actually checked out, each source head equals its recorded base or the
exact recorded integrated landing for a completed leaf, and each base is an ancestor of its work
branch. It then emits the strict pair identity and its canonical digest. This completed-leaf
allowance preserves memory-only settings recloseout without accepting an unrelated source move.

Every refusal is a `MemoryCandidatePairError` with one named field, bounded expected/observed
facts, and a contract-addressed repair action. A moved source branch points to `worktree_sync`.
The resolver never searches for another checkout, falls back to official memory, mutates Git, or
switches a branch.

The admitted object is shape-checked before the filesystem reread. This keeps the resolver total
when an upstream caller supplies a malformed in-memory contract while preserving the canonical
writer's own refusal of invalid persisted contracts. Only after that check does the resolver
reread the exact path and require equality, so the shape check is not a substitute for stale-byte
detection.

### Conventions

Resolve the exact admitted contract and report field-specific expected/observed facts. The derived cache location remains a consumer detail.

### Invariants And Boundaries

- The contract is the sole pair authority; reports and queue state are consumers only.
- The ledger location describes the cache under the selected memory worktree; its bytes and
  existence are not pair authority.
- External code and memory roots must belong to distinct Git repositories.
- Unrelated lifecycle-cell changes do not alter the pair digest.
- Missing, stale, contradictory, or wrong-checkout repository facts fail before scanning or acceptance.

### Todos

No additional file-local TODO is established by this candidate review.

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

- The pair resolver derives the consumer cache path, excludes it from the digest, and proves real branch/base authority. [1]
- Pair resolution and digest construction are centralized. [2]
- Requested authority is compared before candidate work begins. [3]
- Work branch, accepted source head, and ancestry are all proven without mutation. [4]

### Cross-Repo References

No additional repository is consulted. The configured contract identifies both selected Git
repositories.


No separate external implementation source applies to this file.
