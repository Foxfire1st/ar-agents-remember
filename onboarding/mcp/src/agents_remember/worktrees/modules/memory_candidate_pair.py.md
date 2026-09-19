# mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T18:40+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pair resolver derives the consumer cache path, excludes it from the digest, and proves real branch/base authority. | `resolve_memory_candidate_pair` | mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py:48-131 |
| Pair resolution and digest construction are centralized. | `resolve_memory_candidate_pair` | mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py:48-131 |
| Requested authority is compared before candidate work begins. | `_require_requested_authority` | mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py:132-164 |
| Work branch, accepted source head, and ancestry are all proven without mutation. | `_require_branch_plan` | mcp/src/agents_remember/worktrees/modules/memory_candidate_pair.py:286-351 |

## Cross-Repo References

No additional repository is consulted. The configured contract identifies both selected Git
repositories.


| Finding | Anchor | Source |
| --- | --- | --- |
| No separate external implementation source applies to this file. | — | — |
## Update History
- 2026-09-18T18:40+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **moved this sidecar to the path its source actually has, and advanced the verification stamp to the revision read.** Code commit `806649b9` relocated the module out of `memory_quality/` into `worktrees/modules/` as a **pure rename** — the blob is byte-identical before, at, and after the move (`95544419b0b670b95be5e07d8fae1cdffc3d4c88` at `806649b9^`, at `806649b9`, and at `c5a74a85`) — and the card stayed at the retired path, where `integrity.onboarding_drift_check.summary` reported it `orphaned` while no card existed at the new path at all. Nothing in the body was rewritten: the `Repo-Internal References` rows already cite `worktrees/modules/memory_candidate_pair.py`, and each cited anchor (`resolve_memory_candidate_pair` `:48-131`, `_require_requested_authority` `:132-164`, `_require_branch_plan` `:286-351`) was re-read against the current source in this pass and none moved. What changed is the title, the `path` metadata row, the governing-overview link (now the modules route overview) and this record. The stamp advances to `c5a74a85` because the old stamp predates the new path, so the check would otherwise read the move itself as a source change; closeout re-stamps. No claim bytes were deleted, substituted or weakened.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Made the ledger location informational while retaining exact code/memory pair and ancestry proof. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.


- 2026-09-11T10:26:37+02:00 — Moved the mirrored sidecar from `mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py` to `mcp/src/agents_remember/memory_quality/memory_candidate_pair.py`. Relocated with the de-entanglement cut (commit `0b63d6fc`, "relocate the two memory-candidate roots out of closeout") so the pre-closeout `memory_quality` service owns its exact-pair resolver. The source blob is byte-identical to the pre-move file; every cited anchor range was re-verified against the new path and is unchanged. Governing overview link repointed to the memory quality overview. Verification metadata refreshed to code commit `2fa5e81f4da44a0a87f1a700c5363a9d563e7f9d`.

- 2026-08-30T07:05+02:00 — MCAR-L03 A008: made admitted-object shape validation precede the
  exact reread, preserving both field-specific refusal and strict canonical contract writes.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: moved pair authority under closeout integration,
  admitted the exact integrated source head for completed-leaf memory-only recloseout, and retained
  strict refusal for every unrelated source move.

- 2026-08-29T21:46+02:00 — MCAR-L03: created the canonical exact-pair resolver and typed
  pre-scan refusal contract. Verification remains closeout-owned.
