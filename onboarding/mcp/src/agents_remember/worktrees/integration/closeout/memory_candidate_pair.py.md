# mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T07:05+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[worktrees overview](overview.md)

## Purpose

Owns the one read-only resolver that admits and re-proves an exact external-memory leaf pair.

## Code Commentary

`resolve_memory_candidate_pair` compares the requested address and repository with the admitted
contract, rereads that same contract, and requires an external leaf with live code, memory,
onboarding, and ledger paths. It proves both worktrees belong to the recorded repositories, the
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

## Invariants And Boundaries

- The contract is the sole pair authority; reports and queue state are consumers only.
- The ledger must be the exact `memory.md` under the selected memory worktree.
- External code and memory roots must belong to distinct Git repositories.
- Unrelated lifecycle-cell changes do not alter the pair digest.
- Missing, stale, contradictory, or wrong-checkout facts fail before scanning or acceptance.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Pair resolution and digest construction are centralized. | `resolve_memory_candidate_pair` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py:48-144 |
| Requested authority is compared before candidate work begins. | `_require_requested_authority` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py:145-175 |
| Work branch, accepted source head, and ancestry are all proven without mutation. | `_require_branch_plan` | mcp/src/agents_remember/worktrees/integration/closeout/memory_candidate_pair.py:290-353 |

## Cross-Repo References

No additional repository is consulted. The configured contract identifies both selected Git
repositories.

## Update History

- 2026-08-30T07:05+02:00 — MCAR-L03 A008: made admitted-object shape validation precede the
  exact reread, preserving both field-specific refusal and strict canonical contract writes.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: moved pair authority under closeout integration,
  admitted the exact integrated source head for completed-leaf memory-only recloseout, and retained
  strict refusal for every unrelated source move.

- 2026-08-29T21:46+02:00 — MCAR-L03: created the canonical exact-pair resolver and typed
  pre-scan refusal contract. Verification remains closeout-owned.
