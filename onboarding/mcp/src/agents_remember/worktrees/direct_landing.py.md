# mcp/src/agents_remember/worktrees/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea` |
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
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

### 260928-MIK-L09 The Mandatory Gate At Direct Landing (MIK-R09 Rule 3)

Direct landing is one of MIK-R09's leaf-publication routes. On converted memory (the layout marker in the checkout's
working tree or `HEAD`) it gates before admission; unconverted memory lands exactly as before (probed before anything
is captured or written: `count-objects` and `status` unchanged in the unconverted test; `unconverted.sh` finds the
preview payload and object count identical to base).

- **The gate.** `_direct_gate_owner(contract, code_commit)` probes `checkout_memory_converted`, captures the exact tree
  the memory-content commit would record (`_memory_content_tree`: a private index under the worktree group's
  `reports/`, `MEMORY_CONTENT_EXCLUDES`), and asks `direct_gate_verdict` through the port; any refusal raises
  `direct-landing-knowledge-gate-refused`. It returns the leaf that owns the one open history file (ruling
  2026-09-30T14:38:47 gap 2). The preview calls it too, so it refuses exactly as the apply.
- **The closing and the exact tree.** `_close_gated_leaf` gates, closes the owner's history file
  (`close_owner_history`, MIK-R07 rule 7), and validates the exact tree it will commit through
  `memory_commit_refusal(..., leaf_publication=True)` against `HEAD` (`direct-landing-knowledge-validation-refused`).
  Any refusal or exception restores the file.
- **The closing lives until the generation is decided (review R1 F3; R2-2, R2-5; R3-1).** `_start_or_observe_direct_landing`
  first settles the kept closings (`_settle_kept_closing`; an unreadable receipt refuses as
  `direct-landing-closing-receipt-unreadable`), then checks `_in_flight_retry`: an exact retry of the series'
  in-flight generation (same contract path, code commit, candidate tree, effective input and approval note,
  `_same_request`) prepares **without** the gate and reaches `_create_direct_landing`'s existing-generation check,
  which resumes it or reports the conflict; that generation was gated when it was admitted.
  `_prepare_direct_landing_candidate(identity, *, gated)` returns the input, the candidate and the closing (restored if
  building the input fails). `_admit_direct_landing` writes the generation's receipt (`keep_direct_closing`) before
  creating it and keeps the closing only when the journal **creates** a generation; an input conflict, a failing
  create, any exception, or a replayed generation restores it in process and drops only this call's receipt
  (`_undo_closing`). A receipt Git cannot write (`hash-object` failing) restores and refuses as
  `direct-landing-closing-receipt-unwritable`. The kept closings are settled again after a replayed completion and
  after execution (`_generation_state`: landed, cancelled or in flight); cancellation settles them too
  (`integration/lifecycle/control/cancellation.py`).
- **Tests:** `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal` and, through the
  public entry `direct_landing(config, request, series)`, the preview/apply, input-conflict, exact-retry, cancel,
  another-generation (N12), crash-before-create (N05), unreadable-receipt (R2-5), exact-tree (N09) and
  already-landed (R3-1, SHA-1 and SHA-256) cases in `test_knowledge_gate_routes.py`.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring's gate and closing paragraphs. | "On converted memory (the layout marker on either side) the mandatory" | mcp/src/agents_remember/worktrees/direct_landing.py:28-43 |
| The preview refuses as the apply. | "the preview refuses exactly as the apply" | mcp/src/agents_remember/worktrees/direct_landing.py:328-328 |
| Settle, exact retry, prepare, admit, and settle again. | `_start_or_observe_direct_landing`; `_generation_state`; `_settle_kept_closing`; `_in_flight_retry`; `_same_request` | mcp/src/agents_remember/worktrees/direct_landing.py:390-497 |
| Only a created generation keeps the closing. | `_admit_direct_landing`; `_undo_closing` | mcp/src/agents_remember/worktrees/direct_landing.py:500-531 |
| The prepared input, the candidate and the closing. | `_prepare_direct_landing_candidate`; `_operation_candidate` | mcp/src/agents_remember/worktrees/direct_landing.py:550-598 |
| The exact memory tree, the gate and the closing validated as a leaf publication. | `_memory_content_tree`; `_direct_gate_owner`; `_close_gated_leaf` | mcp/src/agents_remember/worktrees/direct_landing.py:601-667 |

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
| Policy, normalized request, exact code proof, and the preview, which writes no memory content and since MIK-R09 refuses exactly as the apply on converted memory. | `DirectLandingRequest`; `require_direct_landing_enabled`; `_verify_code_commit`; `_direct_landing_preview` | mcp/src/agents_remember/worktrees/direct_landing.py:118-168; mcp/src/agents_remember/worktrees/direct_landing.py:228-286; mcp/src/agents_remember/worktrees/direct_landing.py:319-341 |
| Memory admission captures the prepared content snapshot and typed candidate (since MIK-R09 in `_operation_candidate`, after the gate's closing). | `_direct_memory_admission_snapshot` | mcp/src/agents_remember/worktrees/direct_landing.py:344-387 |
| Generation creation and action-required public projection. | `_create_direct_landing`; `_direct_landing_observation` | mcp/src/agents_remember/worktrees/direct_landing.py:670-704; mcp/src/agents_remember/worktrees/direct_landing.py:707-724 |
| The application owns configured admission and execution serialization. | `direct_landing_tool` | mcp/src/agents_remember/application/lifecycle/direct_landing.py:64-113 |
| The focused integration scenario verifies cache-independent publication and recovery. | `test_direct_landing_publishes_memory_and_recovers_independently_of_cache` | mcp/tests/test_direct_landing.py:171-272 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): **body updated for MIK-R09.** New subsection "260928-MIK-L09 The Mandatory Gate At Direct Landing (MIK-R09 Rule 3)": the gate before admission on converted memory (the leaf inferred as the one open history file's owner, gap 2 of 14:38:47), the preview refusing as the apply, the closing and its exact-tree validation as a leaf publication (review R1 F1), and the closing kept until the generation is decided with per-generation receipts (F3, R2-2, R2-5, R3-1); six rows. **Reopened claim reworded:** the policy/preview row (the preview now also gates on converted memory, so "read-only preview" became "writes no memory content"); the admission-snapshot row notes the split into `_operation_candidate`. The generation rows the installed fixer declined were re-pointed by the exact base-to-staged line shift, every anchor checked in both ranges.
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