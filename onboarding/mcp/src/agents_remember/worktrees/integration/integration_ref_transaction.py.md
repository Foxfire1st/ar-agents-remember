# mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T11:58+02:00 |
| lastVerifiedCommitHash | `187414cef8150a8004fc1b023a8377f77b24e873` |
| lastVerifiedCommitDate | 2026-09-14T12:13:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Moves exact code and external-memory integration refs with prepared-capability compare-and-swap, ledger proof, and checkout refresh.

## Code Commentary

`IntegrationSources` is a frozen dataclass with a `replay_required` property.
`require_integrated_ledger_mapping` cit:([`require_integrated_ledger_mapping`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:274-344) takes the memory source commit and
proves the landed commits on their own terms. Its `expected_series_prefix` and `checkpoint`
parameters are **gone** (260913-LCA-L11): the route difference no longer reaches the ledger proof
at all, because the ledger-history form it used to select was the tracked file's.

**Since 260913-LCA-L11 the landing is judged on the commits, never on the tracked table.** The
developer's ruling of 2026-09-14T08:15+02:00 (master `260913_ledger-commit-attribution`) settles the
collision L10's refused integration exposed: the rebuild takes priority over the legacy checker.
The check that enforced "preserve the complete source ledger history: no source row dropped,
reordered or replaced" protected `memory.md`, and `memory.md` is derived state — the projection
recomputes it from the memory commits' own `Code-Commit:` attribution — so a table that differs
from the file it replaced is the normal result of a rebuild, not damage. It is **removed, not
weakened**: not behind a flag, not made opt-out, with no compatibility path. The asymmetric cost
settled it — the checkpoint route already tolerated merge-produced interleaving while the leaf
route did not, so the same table was accepted on one road and refused on the other, and L10's real
repair (13 rows dropped, 455 reordered) was refused as damage.

**What was removed, and what survives.** Deleted outright: `_require_preserved_ledger_history` and
its whole file-preservation rule (both the series leaf-chain prefix branch and the projection fixed
point), its evidence renderers `_ledger_projection_refusal` / `_landing_ledger_rule` /
`_projection_divergence_evidence` / `_ledger_row_list` / `_ledger_row_text`, the `_LedgerLanding`
carrier, `_integrated_ledger_pair` (its source-blob read is gone with it), and
`LandingAdmission.expected_series_ledger_prefix` — the removed rule's whole surface, so no producer
is left without a consumer. Four protections were **not** about the file and all four still fire,
each with its own mutation proof recorded by the worker:

1. **the landed ledger maps the landed code commit to the landed memory content** —
   `find_mapping`; a table that names the code commit with different memory content is refused too,
   so the entry must be *this landing's*;
2. **every row of the landed table is true** — `_require_true_rows` cit:([`_require_true_rows`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:345-380) checks each row against the two
   repositories: the code commit must exist (`code_commit_exists`) and the memory content must be
   reachable from the landed ledger commit. A fabricated or stale row cannot ride along on a
   landing whose own pair happens to be correct, and the offending row is named in the refusal;
3. **the landed memory content descends from the exact memory source** — now **conditional on the
   landing not having happened yet** (`not is_ancestor(commits.ledger, memory_source_commit)`),
   the condition the file rule used to carry silently. Once the refs have moved, the memory source
   branch *is* the landed ledger commit, and asking the question then would refuse the idempotent
   retry that must converge;
4. **the ledger header names its own first row** — `_integrated_ledger` cit:([`_integrated_ledger`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:245-273) reads the landed ledger with the
   **validated** parse (`parse_ledger_text`), and its refusal now carries the closeout re-run remedy
   itself rather than borrowing the projection check's message.

**The known, deliberate gap this removal carries — not something the code prevents.** With the
file rule gone, a reordering that moves an OLDER row above a NEWER one **for the same code commit**
can now land and nothing at the landing reports it. `find_mapping` returns the FIRST row naming a
code commit, so such a reversal silently changes what that code commit resolves to. The landed code
commit's own pair is still safe — it is the mapping clause of promise 1 — so the exposure is every
*other* code commit the landed table names. The worker briefly re-added a "resolution preservation"
rule, found that it refused a correct ledger (re-establishing the file as authority by the back
door), and removed it; the affected end-to-end case now asserts the acceptance and carries the
hazard in its docstring. It is recorded here as a known gap **pending a decision**, never as
something a rule catches. The module docstring's numbered list still claims a fifth promise ("no
code commit the landed table still names resolves to a different memory commit than it resolved to
on the memory source"); no code implements it and the change's own test asserts the opposite, so
that sentence is a code-side doc defect reported to the owning seat rather than curated as truth.

**The order is part of the contract, not incidental.** The row-truth loop runs *before* the
memory-content reachability check and before the conditional source-ancestry question, so a table
whose own pair is wrong is refused by the clause about the table, and only a table that is internally
true reaches the ancestry questions.

**Since 260831-LOCR-L34 the route-specific landing facts travel as one value.**
`LandingAdmission` cit:([`LandingAdmission`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:88-98) replaces `prepare_integration_ref_move`'s single keyword-only
`expected_series_ledger_prefix` argument. Since 260913-LCA-L11 it carries exactly one fact: the
captured `checkpoint_candidate` a **checkpoint** lands, or `None` for the final routes, which land
the closeout candidate recorded on the contract. The difference between the two routes therefore
lives in the transaction's data rather than in a second copy of the transaction.
`_require_landing_output_authority`
cit:([`_require_landing_output_authority`], mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:381-414) is the one place that decides which authorization the output
owes: the ordinary route lands the closeout candidate recorded on the contract
(`require_authorized_integration_commits`), while the checkpoint route's output must equal exactly the
candidate its own live capture admitted — re-proved against the live refs immediately before this
call by `publish_series_checkpoint_under_authority`.

The transaction's own boundary read remains authoritative and is re-taken under the transaction
immediately before the irreversible ref move; the earlier preview-side proof added by 260831-LOCR-L34
in `worktrees/modules/integrate.py::_require_ledger_projection` exists only so the dry run refuses
exactly what the apply refuses.

Ledger proof reads the newest mapping as current authority. A true no-change integration reuses an
already-current code/memory pair; a memory-only change for unchanged code prepends one new current
row. Repeated code SHAs are valid, and the landing no longer has an opinion about the *order* or the
*completeness* of the table it publishes — only about whether each row it carries is true.

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
- The mapped memory-content commit must descend from the prior memory tip and be reachable from the ledger commit — the first clause while the landing is still to happen, the second always.
- **The landing judges the commits, never the tracked table (260913-LCA-L11).** Every promise this
  transaction makes about a ledger is a fact about the landed commits: the landed pair is mapped,
  every row of the landed table is true against the two repositories, the landed memory content
  descends from the exact memory source (while the source is still behind the landing), and the
  header names its own first row. There is **no** comparison against the source file's row list or
  row order and no compatibility path that re-adds one: `memory.md` is derived state, and a rebuild
  that drops an unprovable row or normalises order is the normal result.
- **The removal's known gap is recorded, not papered over.** A reordering that puts an older row
  above a newer one *for the same code commit* can land unreported for any code commit other than
  the landed one, because `find_mapping` resolves the first row naming a commit. A "resolution
  preservation" rule that would have closed it was written, found to refuse a correct ledger, and
  removed; it is a gap pending a decision, and no card or code comment may describe it as blocked.
- **The route difference is data, never a second transaction (260831-LOCR-L34).** One
  `prepare_integration_ref_move` serves both the final route and the checkpoint route; which commits are
  admitted travels in `LandingAdmission`. Do not fork the transaction or re-derive the admission at
  the boundary.
- **The ledger-history form is no longer part of the admission.** `LandingAdmission` now carries
  only `checkpoint_candidate`. Do not reintroduce a ledger-shape field on it: the shapes it used to
  name were the tracked file's, and selecting one is exactly how the file became authority again.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Preparation binds current sources, exact targets, and journal authority. | `prepare_integration_ref_move` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:110-169 |
| The route-specific admission a landing owes: the checkpoint's own captured candidate, or nothing extra for the final routes. | `LandingAdmission`; `_require_landing_output_authority` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:88-98; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:381-414 |
| The integration transaction owns ordered CAS and pair recovery facts. | `merge_integrated_commits` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:170-243 |
| Ledger mapping and ancestry are re-proved at the irreversible owner. The landed table is judged on its own rows rather than against the source file, and the source-ancestry clause is asked only while the landing is still to happen. | `require_integrated_ledger_mapping`; `_integrated_ledger`; `_require_true_rows` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:274-344; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:245-273; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:345-380 |
| The two repository-level row-truth clauses whose refusals name the offending row. | "which the code repository does not hold"; "does not name memory content the landed ledger commit carries" | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:367-378 |
| Recovery and checkout refresh: mid-crash integration-ref recovery is deleted, and checkout refresh is exact and idempotent. | `refresh_owned_checkout` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:429-459 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `IntegrationSources`, `IntegrationRefRace`, `IntegratedCommits`. Protected ref publication uses exact expected/observed compare-and-swap evidence. A CAS loss or moved source ref is classified into the same landing generation for reconciliation; it is never silently discarded or retried as a new operation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `IntegrationSources`, `IntegrationRefRace`, `IntegratedCommits` at this ownership boundary. | `IntegrationSources`; `IntegrationRefRace`; `IntegratedCommits` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:36-49; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:50-67; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:68-76 |

## Update History
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
