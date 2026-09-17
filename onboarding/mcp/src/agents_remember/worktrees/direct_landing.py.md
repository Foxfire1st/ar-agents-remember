# mcp/src/agents_remember/worktrees/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/direct_landing.py` |
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

Coordinates branch-addressed delivery for a sanctioned leaf implemented without its own worktree
enclosure. It verifies already committed code, accepts an exact memory candidate, and creates or
observes one direct-landing journal generation. Ordinary series closeout and integration are
separate routes.

## Code Commentary

### Logic

`DirectLandingRequest` carries the exact code commit, memory message, approval intent, optional
candidate tree, and dry-run selection. The policy gate requires `directExecutionEnabled`.
`_direct_landing_after_policy` requires a series contract, normalizes the effective memory message,
requires intent, and rereads configured contract authority. The application boundary owns configured
admission and serialized execution; this module consumes the admitted contract.

`_verify_code_commit` first proves that the requested commit is the exact local series-branch HEAD,
then resolves its tree. Apply requires the supplied pre-commit candidate tree to match. This module
checks the candidate proof; it neither creates the code commit nor runs the caller's quality gate.
Preview reads repository/ref facts and does not parse or mutate a ledger.

For apply, `_direct_memory_admission_snapshot` verifies the checked-out memory branch. Real content
dirt triggers reversible cache preparation before the accepted snapshot is captured; cache-only
dirt does not. Memory snapshots exclude the consumer cache while retaining actual ref and object
identity. `_prepare_direct_landing_candidate` stores code/tree and memory repository/ref/snapshot
facts in the typed input. Ledger paths, bytes, digests, and commit messages are absent from that input.

`_create_direct_landing` admits the request itself: contract, code commit/tree, candidate, and
normalized inputs. It carries no closeout-door publication. The runtime executes or reconciles the
same generation. Success includes the lifecycle-operation projection; an existing generation that
requires action returns the closed public `refused` outcome with that evidence nested.

### Conventions

Execution is synchronous and journaled. Concurrency serialization is owned by configured
application authority, while crash recovery is owned by the durable operation. The code leg is
verified-existing, and the only mutation message is the memory-content message.

### Invariants And Boundaries

- Apply requires external memory and the exact pre-commit candidate tree.
- Series shape alone does not turn ordinary closeout or integration into direct execution.
- Real code, memory repository, branch, and content evidence retain their authority.
- Cached rows, bytes, or absence have no admission or recovery authority.
- There is no ledger third leg, ledger-only commit, closeout-door dependency, or repeat-from-scratch recovery route.

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
| Policy, normalized request, exact code proof, and read-only preview. | `DirectLandingRequest` | mcp/src/agents_remember/worktrees/direct_landing.py:86-100 |
| Memory admission captures the prepared content snapshot and typed candidate. | `_direct_memory_admission_snapshot` | mcp/src/agents_remember/worktrees/direct_landing.py:310-353 |
| Generation creation and action-required public projection. | `_create_direct_landing` | mcp/src/agents_remember/worktrees/direct_landing.py:460-494 |
| The application owns configured admission and execution serialization. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:55-104 |
| The focused integration scenario verifies cache-independent publication and recovery. | `test_direct_landing_publishes_memory_and_recovers_independently_of_cache` | mcp/tests/test_direct_landing.py:171-272 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T00:51 UTC — Replaced the memory-plus-ledger admission narrative with exact code/content evidence and one memory publication; recorded reversible cache preparation, typed input retirement, retained request-owned generation admission, and the nearer worktrees overview. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.

- 2026-09-11T23:05:00+00:00: Repaired the R03 claim, which anchored `_claim_waiting_direct_landing` at lines 678-701 of a 576-line file. That helper no longer exists anywhere in the tree and the closeout-door cut (commit `fad9808e`) already removed the door reads; `_create_direct_landing` (473-507) now admits a fresh generation from the request itself (series contract, branch HEAD commit and tree, effective commit messages) with no door publication and no bound `lifecycle_operation_dependencies`.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `direct_landing` repointed to mcp/src/agents_remember/worktrees/direct_landing.py:117-129. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: recorded that all five door reads are gone and admission is now the request itself plus the `directExecutionEnabled` policy gate; replaced the `_claim_waiting_direct_landing` binding claim with the current dependency declaration (candidate, plan, input — no door). Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the direct-landing claim dependency binding and its launch/currentness re-requirement; prior policy-gated and journaled-execution prose preserved.

- 2026-08-31T20:30+02:00 — 260831-DER: made the direct-execution boundary explicit. Direct landing
  is the policy-gated delivery route for a leaf intentionally implemented without its own enclosure;
  ordinary series/master closeout and integration remain lifecycle operations and do not use the
  direct-execution flag.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: normalized existing action-required journal observation to the closed public refused outcome while retaining nested lifecycle evidence. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: citation-only repair repointed moved lifecycle, tool-model, direct-landing, legacy, or startup evidence to its canonical committed source path; this card's own documented behavior is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout stamps the landed code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: created for L16-R7/R8 — the direct landing operation:
  code-commit verification plus sequential memory and ledger commits under the integration
  authority lock, with the strictly pre-commit staged-candidate gate. Verified at code commit
  a9d50e08; the crash-durability boundary was clarified by 260821-CLIVE-L1.