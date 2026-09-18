# mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Prepare and publish exact code/memory ref moves with expected-old compare-and-swap and safe refresh of owned checkouts.

## Code Commentary

### Logic

`IntegratedCommits` contains code and memory-content commits only. `LandingAdmission` optionally carries the checkpoint's captured candidate; ordinary integration instead matches the recorded closeout pair. Preparation verifies output authority, current named source tips, source-to-candidate ancestry, and substantive checkout cleanliness before returning its private prepared-move capability.

`require_integrated_memory_ancestry` checks the accepted code object exists and the accepted memory output descends from the exact memory source. It does not parse a ledger, inspect rows, compare headers, or require a trailer mapping for the selected code commit.

Publication CASes code first and memory second. If memory loses a race, code may already be landed; the error retains expected before/intended pair facts and preserves the competing memory ref. There is no hard-reset rollback that can clobber it. Owned checkout refresh requires the named ref at the accepted new tip and permits only old or already-new substantive trees/indexes. On the memory side it excludes root `memory.md`, discarding only that derived path's local state when native checkout needs it.

### Conventions

The lowest ref writer requires the private preparation capability. `CheckoutRefresh` carries side, old, and new identities; code-side files retain ordinary semantics even if named memory.md.

### Invariants And Boundaries

- A compare-and-swap always includes the expected old object id.
- A torn pair remains visible; concurrent memory work is never reset to make the result look atomic.
- Cache state is excluded only for the memory domain and cannot select a delivered commit.
- Unrelated untracked files, substantive content changes, missing objects, or moved refs still refuse.
- Checkpoint and final integration share one transaction with route-specific candidate data.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Two-output and route-specific candidate data. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |
| Preparation validates accepted output and source/checkout state. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |
| Ordered expected-old CAS retains a torn pair on a memory race. | n/a | [mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py](mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py) |
| Owned checkout refresh excludes only memory cache state. | `refresh_owned_checkout` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:300-336 |
| Real Git regression for cache independence and competing memory CAS. | `test_external_pair_cas_retains_torn_pair_without_clobbering_memory_race` | mcp/tests/test_integration_branch_authority.py:80-170 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Replaced ledger mapping/row/header proof and the third output with real memory ancestry and a two-commit CAS; added memory-domain cache exclusion to owned checkout refresh without weakening content/ref checks. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 10 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): recorded the developer ruling of 2026-09-14T08:15+02:00 and the removal it
  ordered. The integration-side ledger-preservation check is **gone, not weakened** — the file rule
  protected the tracked `memory.md`, which is derived state, so it was hazardous; L10's real repair
  (13 rows dropped, 455 reordered) was refused by it while the checkpoint route accepted the same
  table's interleaving. Listed the whole removed surface (`_require_preserved_ledger_history`, its
  five evidence renderers, `_LedgerLanding`, `_integrated_ledger_pair`, and
  `LandingAdmission.expected_series_ledger_prefix`) and the **four surviving protections** with their
  current ranges: the landed pair's mapping, `_require_true_rows`' per-row truth against the two
  repositories, the memory content's descent from the exact source (now explicitly conditional on
  the landing not having happened yet), and the header naming its own first row through the
  newly-validated `_integrated_ledger` read. Recorded the removal's **known deliberate gap** — an
  older/newer row reversal for the same code commit can now land unreported for any code commit
  other than the landed one, the "resolution preservation" rule that would have closed it refused a
  correct ledger and was removed, and the affected test now asserts the acceptance — as pending a
  decision rather than as something prevented. Recorded that the module docstring's numbered
  "five promises" still claims the reversal protection that no code implements and that this
  change's own test contradicts, as a code-side doc defect reported to the owning seat. Repointed
  every reference range after the module shrank from 594 to 466 lines. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.
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
