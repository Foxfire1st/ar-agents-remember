# mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Moves exact code and external-memory integration refs with prepared-capability compare-and-swap, ledger proof, and checkout refresh.

## Code Commentary

`IntegrationSources` is now a frozen dataclass with a `replay_required` property; `require_integrated_ledger_mapping` accepts the memory source commit, an expected series ledger prefix, and (since 260831-LOCR-L34) a `checkpoint` flag naming which history proof the landing owes.

**Since 260831-LOCR-L34 the route-specific landing facts travel as one value.**
`LandingAdmission` cit:([`LandingAdmission`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:92-106) replaces `prepare_integration_ref_move`'s single keyword-only
`expected_series_ledger_prefix` argument. It carries the completed-leaf-chain prefix the **final**
series route must carry and the captured `checkpoint_candidate` a **checkpoint** lands (mutually
exclusive: an unfinished master landed at a checkpoint has no finished chain to prefix against). The difference between the two
routes therefore lives in the transaction's data rather than in a second copy of the transaction.
`_require_landing_output_authority`
cit:([`_require_landing_output_authority`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:400-433) is the one place that decides which authorization the output
owes: the ordinary route lands the closeout candidate recorded on the contract
(`require_authorized_integration_commits`), while the checkpoint route's output must equal exactly the
candidate its own live capture admitted — re-proved against the live refs immediately before this
call by `publish_series_checkpoint_under_authority`.

`require_integrated_ledger_mapping(..., checkpoint: bool = False)`
cit:([`require_integrated_ledger_mapping`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:282-328) threads that shape into `_LedgerLanding`
cit:([`_LedgerLanding`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:329-341), which now carries the flag beside the landing facts rather than as a loose parameter.
`_require_preserved_ledger_history` cit:([`_require_preserved_ledger_history`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:344-399) takes the leaf-chain-prefix form only for
`contract.kind == "series" and not landing.checkpoint`; a checkpoint of a still-open master takes the
same **projection** form a leaf uses, because the complete leaf chain is one of the completion facts
its route deliberately does not require. That is a smaller promise, not a dropped one: the rows are
still recomputed from the world and a hand-edited table is still refused.

The transaction's own boundary read remains authoritative and is re-taken under the transaction
immediately before the irreversible ref move; the earlier preview-side proof added by 260831-LOCR-L34
in `worktrees/modules/integrate.py::_require_ledger_projection` exists only so the dry run refuses
exactly what the apply refuses.

Ledger proof reads the newest mapping as current authority. A true no-change integration reuses an
already-current code/memory pair; a memory-only change for unchanged code must prepend exactly one
new current row while retaining the complete source history. Repeated code SHAs in that preserved
history are valid.

`prepare_integration_ref_move` snapshots exact canonical refs only after the admitted output authority
and the live source-tip reads. `merge_integrated_commits` consumes that prepared capability, advances
the named refs with expected-old CAS, verifies the external-memory ledger/content ancestry, and
refreshes the owned checkouts. Checkout refresh accepts clean old or already-new state, refuses
untracked/concurrent changes, and never uses ambient HEAD as the target authority. Mid-crash recovery
entry points no longer exist: after a crash between the two ref moves the operator re-runs
`worktree_integrate` against the live refs.

## Invariants And Boundaries

- The lowest ref writer requires an unforgeable prepared-move capability.
- Every ref update names `refs/heads/<canonical>` and includes the expected old object id.
- External code and memory movement is one compare-and-swapped pair; rollback never clobbers a concurrently advanced ref, and a torn pair is repaired by re-running integration rather than an in-process recovery chain.
- The mapped memory-content commit must descend from the prior memory tip and be reachable from the ledger commit.
- Atomic-series ledger publication either preserves an already-current exact pair or prepends one
  exact row over the entire prior history; global code-key uniqueness is not an invariant.
- **The route difference is data, never a second transaction (260831-LOCR-L34).** One
  `prepare_integration_ref_move` serves both the final route and the checkpoint route; which commits are
  admitted, and which ledger history form is owed, travel in `LandingAdmission`. Do not fork the
  transaction or re-derive the admission at the boundary.
- **A checkpoint's ledger is proved as a projection, never against the completion census.** The
  ordered leaf-landing prefix is a completion fact the checkpoint route deliberately does not
  require, so `_require_preserved_ledger_history` takes the leaf projection form for it. The rows are
  still recomputed from the world, so a hand-edited table is still refused.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Preparation binds current sources, exact targets, and journal authority. | `prepare_integration_ref_move` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:118-179 |
| The route-specific admission a landing owes: the finished-chain prefix, or the checkpoint's own captured candidate. | `LandingAdmission`; `_require_landing_output_authority` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:92-106; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:400-433 |
| The integration transaction owns ordered CAS and pair recovery facts. | `merge_integrated_commits` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:180-254 |
| Ledger mapping and ancestry are re-proved at the irreversible owner, in the history form the landing shape names. | `require_integrated_ledger_mapping`; `_LedgerLanding`; `_require_preserved_ledger_history` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:282-328; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:329-341; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:344-399 |
| Recovery and checkout refresh: mid-crash integration-ref recovery is deleted, and checkout refresh is exact and idempotent. | `refresh_owned_checkout` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:566-594 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegrationSources`, `IntegrationRefRace`, `IntegratedCommits`. Protected ref publication uses exact expected/observed compare-and-swap evidence. A CAS loss or moved source ref is classified into the same landing generation for reconciliation; it is never silently discarded or retried as a new operation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `IntegrationSources`, `IntegrationRefRace`, `IntegratedCommits` at this ownership boundary. | `IntegrationSources`; `IntegrationRefRace`; `IntegratedCommits` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:40-51; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:54-66; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:72-78 |

## Update History
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: the checkpoint route's subject is an
  unfinished master that is partially published, not a paused one, so `LandingAdmission`'s
  `checkpoint_candidate` is described as what a checkpoint lands and the leaf-projection invariant as
  "a checkpoint's ledger". Wording only; the transaction's data-carried route difference is unchanged
  and no verification stamp advanced.
- 2026-09-13T12:29:52+00:00: Generated citation repair: `refresh_owned_checkout` repointed to mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:566-594. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:45+00:00 — 260831-LOCR-L34: recorded `LandingAdmission` replacing the single
  keyword-only prefix argument — the route difference (finished leaf-chain prefix vs the checkpoint's
  own captured candidate) now travels as data through one transaction — plus
  `_require_landing_output_authority` as the one place the output authorization is chosen, the
  `checkpoint` flag on `require_integrated_ledger_mapping`/`_LedgerLanding`, and
  `_require_preserved_ledger_history` taking the leaf projection form for an unfinished master because the
  completion census is one of the facts its route does not require. Recorded that the boundary read
  stays authoritative and the preview-side proof exists only for parity. Re-derived the reference
  ranges. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:05:00+00:00: Repaired the recovery/checkout-refresh claim. It named `recover_integration_ref`, `refresh_owned_checkout` and `refresh_recovered_checkout` at lines 323-438; the mid-crash integration-ref recovery chain was deleted as a capability (its only input was the journaled pre-move ref value, which has no durable source), so only `refresh_owned_checkout` survives and the claim now cites its exact current extent 456-484 and records re-run-integrate as the replacement. Card prose claiming journal-bound CAS and torn-pair recovery was corrected with it.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `merge_integrated_commits` repointed to mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:167-239. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T14:32+02:00 — Corrected irreversible ledger proof for settings-only memory changes:
  current authority is the newest mapping, and a changed memory state for unchanged code requires
  exactly one new prefix row while retaining all source history. Verification remains
  closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.
- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T16:55+02:00 — 260815-DAG-L5 repair: `require_integrated_ledger_mapping` now short-circuits a no-change leaf (whose landed code commit is already in the source ledger) before the preserved-history and ancestor checks, since such a leaf has no new code or memory content to verify. Verification remains closeout-owned.

- 2026-08-17T12:35+02:00 — 260815-DAG-L5: `IntegrationSources` became a frozen dataclass and the ledger proof now takes the memory source commit plus an expected series prefix. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created named-ref integration transaction onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
