# mcp/tests/test_memory_candidate_pair.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_candidate_pair.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T07:05+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

Forces MCAR-R03's exact-pair authority and its no-wrong-checkout/no-fallback boundaries.

## Code Commentary

The suite builds two real leaf code/memory pairs and proves their complete identities differ. It
then places one valid checkout into another leaf's contract, verifies the branch mismatch is named,
proves neither Git head moved, and proves the memory scanner was never called. Additional cases
force source-base staleness to the exact sync route, lifecycle-cell-independent pair digests,
contract-addressed closeout recovery, and the bounded typed refusal envelope. The expanded matrix
also forces every address, contract-shape, path-kind, repository-membership, branch-read, ancestry,
and completed-integration recloseout boundary.

Malformed contract-shape cases are supplied as admitted in-memory objects rather than written as
invalid canonical contracts. This separately proves the resolver's total field-specific refusal
while leaving `write_contract` strict. A configured-admission case also proves the canonical public
refusal projection crosses into the exact-pair error without caller-owned fallback reconstruction.

## Invariants And Boundaries

- A valid checkout is still invalid when it is not the contract's exact checkout.
- Wrong-scope refusal precedes the expensive memory scan.
- Resolver tests use real temporary Git repositories and branches.
- The tests assert read-only behavior as well as refusal classification.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Two independently valid leaf pairs produce distinct full identities. | `test_two_leaf_checkouts_produce_distinct_exact_pair_identities` | mcp/tests/test_memory_candidate_pair.py:42-58 |
| A wrong valid checkout is refused before scan and without Git mutation. | `test_valid_but_wrong_checkout_is_refused_before_it_can_be_a_candidate` | mcp/tests/test_memory_candidate_pair.py:61-99 |
| A moved source points to exact contract sync instead of stale acceptance. | `test_source_branch_advance_requires_sync_instead_of_reusing_old_base` | mcp/tests/test_memory_candidate_pair.py:102-120 |
| Recovery and typed refusal retain the exact contract address. | `test_closeout_recovery_rereads_the_exact_contract_pair`; `test_pair_refusal_is_typed_and_prevents_memory_scanning` | mcp/tests/test_memory_candidate_pair.py:140-148; mcp/tests/test_memory_candidate_pair.py:151-195 |

## Cross-Repo References

No external implementation reference applies; the suite creates all Git evidence locally.

## Update History

- 2026-08-30T07:05+02:00 — MCAR-L03 A008: separated malformed admitted-object proof from
  canonical writer validation, covered the strict configured-refusal adapter, and forced both
  optional `nextArgs` branches in coherence projection.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: expanded the forcing matrix for the exact failures
  exposed by the first full targeted gate, including completed-leaf memory-only recloseout.

- 2026-08-29T21:46+02:00 — MCAR-L03: created the exact-pair, wrong-checkout, stale-base,
  recovery, and no-scan forcing suite. Dagger verification remains closeout-owned.
