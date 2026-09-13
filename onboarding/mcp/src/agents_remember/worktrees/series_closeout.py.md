# mcp/src/agents_remember/worktrees/series_closeout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/series_closeout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00|
| lastVerifiedCommitHash | `707847206d02e2ff27b11c1f674a510d85f3b972` |
| lastVerifiedCommitDate | 2026-09-13T13:20:21+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Seals an atomic block only after every canonical leaf forms one exact journaled code-and-memory landing chain, then records the named series refs without ambient workbench commits. Since 260831-LOCR-L30 it also owns the *non-final* series exit: `publish_series_checkpoint_under_authority` records a partial master's landed line under the same ref-protecting authority while dropping only the completion assumptions, so a paused master can land without being closed. 260831-LOCR-L34 repaired that exit's reachability and closed its fail-open hole: the checkpoint now captures its own candidate refs (`capture_series_checkpoint_refs`) instead of reading closeout cells it cannot have, and `expected` is required and revalidated at publication, so the refs that land are exactly the refs the preview showed.

## CCR-R12@v5 Current Series Boundary

Series closeout and integration remain recording/publication operations over already landed leaf
transactions. They re-prove canonical membership, exact code/memory ancestry, named-ref identity,
and authority before recording the pair; they do not create a normal leaf code/memory/ledger
transaction or invoke strict code quality, memory quality, selected certification, curator
coherence, or independent review. Full suites are an explicit developer request.

## Code Commentary

`_exact_atomic_landing_chain` now returns the ordered landed leaf chain, and `atomic_series_ledger_prefix` derives the newest-first ledger rows that chain contributes.

Closeout and series integration share the same canonical task/contract evidence, but only the
protected landing takes the narrow integration-authority lock. Closeout re-proves completion without
that landing-only lock. The seal verifies canonical master membership, exact enclosure
identity, code and memory repository identity, each leaf's base-to-integrated edge, content/ledger
ancestry, and final named-ref tips. Direct commits, missing leaves, foreign copied contracts, mismatched
code/memory order, and concurrent child admission cannot be absorbed into a master candidate.

Since the closeout-door cut (commit `fad9808e`) the landed-leaf proof no longer consults a door: the
`_AtomicLandingFacts` carrier and its `door`/`door_sprint`/`door_candidate` comparisons were removed
from `_require_exact_atomic_landing_chain` and `_atomic_leaf_code_matches` when `contract.closeout_door`
stopped existing.

Since 260815-DAG-L13 the atomic-master completion proof (`_require_atomic_master_complete`) and
the series-edge publication (`_publish_atomic_series_edge`) read the **effective** execution
nature (`scheduling_mode.effective_execution_nature`): a nature-less legacy master executes
atomically under the atomic-sequential default and closes out without migration (L13-R5a), and a
graph-less sprint takes the atomic-sequential series path. Graph absence does not weaken canonical
master/leaf re-proof and no projection row is completion authority.

Since 260831-closeout-door-cut the master/leaf re-proof carries no door dimension at all.

## 260831-LOCR-L30/L34 Checkpoint Authority: The Missing Partial-Master Verb, Made Reachable

`publish_series_integration_under_authority` proves the atomic master is a **finished unit** — its
task document is `Completed`, `_require_every_atomic_leaf_landed` finds a landed enclosure for every
canonical leaf, and (since 260831-LOCR-L34, because the closeout apply now evaluates
`require_closeout_publication_authority`) it has closed out. A master being paused has none of those,
so a partial master could not land its accumulated line at all through that route.

**L30 wrote the checkpoint route; L34 is what made it reachable and closed its fail-open hole.**
L30's route kept every ref-protecting authority but read the commits to land from the contract's
closeout cells, which are exactly the completion facts a paused master does not have; its own note
admitted the real ref move was never proven end to end. L34 changes two things and nothing else:

- **The checkpoint captures its own candidate.**
  `capture_series_checkpoint_refs(contract)` cit:([`capture_series_checkpoint_refs`], mcp/src/agents_remember/worktrees/series_closeout.py:106-138) returns the frozen
  `SeriesCheckpointRefs` cit:([`SeriesCheckpointRefs`], mcp/src/agents_remember/worktrees/series_closeout.py:93-103) built from the **live** `code_work_branch` tip and the live
  `memory_work_branch` tip — captured, never inherited from a stale contract cell. It proves the
  code-to-memory mapping through `exact_series_memory_closeout`, **the same reader the final series
  closeout uses**, so the two routes cannot drift into two definitions of "the ledger maps this
  code". A capture that cannot prove the mapping raises, which makes "the refs are recorded only once
  their ledger mapping holds" a property of the value rather than a separate check a caller could
  skip. A non-`series` contract raises; an unresolvable code branch refuses
  (`atomic-series-checkpoint-no-code-ref`).
- **Publication revalidates that candidate.** `publish_series_checkpoint_under_authority(contract,
  publication, expected)` cit:([`publish_series_checkpoint_under_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:161-194) now takes `expected` as a **required, never
  defaulted** third argument. A default would be a fail-open hole in exactly the repair it was
  written for: an omitted argument would silently admit whatever the live refs happened to be, i.e. a
  pair the preview never showed. `_require_checkpoint_candidate_unchanged` re-reads the live refs and
  re-proves their ledger mapping at the protected boundary, immediately before the irreversible ref
  move, and refuses `atomic-series-checkpoint-candidate-moved` when they differ.

The checkpoint route keeps every authority that protects *other* owners' refs — the series contract
binding, the atomic landing authority, the source-lineage proof, the replay/ff source-state gate and
the master-handover gate all still run in the caller (`integrate.py::checkpoint_landing_result`) — and
drops only the completion assumptions. It retires nothing: no cleanup runs, and the recorded state is
`checkpointed` rather than `completed`.

It still refuses, and the refusals are what keep the weaker claim from becoming a replacement for the
stronger one:

- `contract.kind != "series"` raises on both the capture and the authority (an ordinary leaf lands
  through `worktree_integrate`).
- A master whose task document already reads `Completed` raises
  `CloseoutQueueError("atomic-series-checkpoint-master-complete", ...)` and is pointed at the final
  route, so a checkpoint can never downgrade a finished integration. Since L34 that refusal lives in
  `require_series_checkpoint_authority` cit:([`require_series_checkpoint_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:139-160), **one definition with two callers**: the
  checkpoint's preflight (`integrate.py::checkpoint_landing_eligibility`) evaluates it so the dry run
  and the apply refuse identically and for the same named reason, and publication re-evaluates it so a
  master that completes *between* preflight and the ref move is refused there too.
- The contract is re-read after the master check and must still equal the passed contract, so the
  protected landing cannot run against a contract that changed underneath it.

## The One Closeout Gate Both Surfaces Read (260831-LOCR-L34)

`require_closeout_publication_authority(contract)` cit:([`require_closeout_publication_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:34-60) is the extracted body of the old
`publish_closeout_under_authority` gate. Its first statement is `if contract.kind == "leaf": return`,
which is exactly the shape the publication had, so no leaf closeout changes. Two callers read it:

- `publish_closeout_under_authority` (the apply) cit:([`publish_closeout_under_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:61-73), which is now a thin wrapper; and
- `worktrees/modules/closeout.py::closeout_preview_payload` (the dry run), which previously ran the
  workbench-commit refusal and nothing else.

Before L34 the atomic-completion gate existed **only behind the apply**, which is why a partial
master's closeout preview answered `would-closeout` and then refused on every completion blocker (19
of them on LOCR). Closeout does not move a protected integration ref, so this gate deliberately does
not acquire the landing-only integration authority lock. **This is instance 1 of the preview/apply
parity invariant recorded on the `worktrees/overview.md` route and in
`memory_quality/overview.md`.**

## Invariants And Boundaries

- Atomic membership comes from exact master task rows and canonical parent relations, not sibling-file discovery.
- The series history equals the ordered leaf landing chain from recorded bases to current named refs.
- Every external memory pair proves base-to-content and content-to-ledger ancestry plus exact ledger mapping.
- Series closeout records named refs and never commits ambient repository-root worktrees.
- The effective nature, not graph presence alone, gates the atomic closeout path; graph-less
  atomic-sequential is valid.
- **Completion is proved, never assumed, on the final route — and never claimed on the checkpoint
  route.** `publish_series_checkpoint_under_authority` may not be extended to also prove the master
  complete: the two routes exist precisely so that "landed" and "finished" stay separate claims, and
  the checkpoint route's `atomic-series-checkpoint-master-complete` refusal is the boundary between
  them.
- **The checkpoint's `expected` argument must never gain a default (260831-LOCR-L34).** It is the
  candidate the preview showed; defaulting it would re-open the fail-open hole the repair closed, by
  admitting whatever the live refs happen to be at publication time. Revalidation against the live
  tips immediately before the ref move is the entire reason the route can promise a pair.
- **The closeout gate has exactly one definition (260831-LOCR-L34).** `closeout_preview_payload` and
  `publish_closeout_under_authority` both call `require_closeout_publication_authority`; do not
  re-inline a copy behind either surface. A preview that plans a closeout its apply refuses is the
  defect this extraction removed, and it misled a human into writing a false note on LOCR.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout re-proves canonical completion without the landing lock; integration repeats it under the narrow protected-landing lock; the checkpoint route keeps every ref authority and drops only the completion assumptions. | `publish_closeout_under_authority`, `publish_series_integration_under_authority`, `publish_series_checkpoint_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:61-73; mcp/src/agents_remember/worktrees/series_closeout.py:74-92; mcp/src/agents_remember/worktrees/series_closeout.py:161-194 |
| The closeout completion gate is extracted into one definition with one body, and its first statement exempts a leaf, so the closeout preview and the closeout apply refuse identically. | `require_closeout_publication_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:34-60 |
| The checkpoint captures its own live candidate refs and proves their ledger mapping through the same reader the final series closeout uses. | `SeriesCheckpointRefs`; `capture_series_checkpoint_refs`; `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:93-103; mcp/src/agents_remember/worktrees/series_closeout.py:106-138; mcp/src/agents_remember/worktrees/series_closeout.py:508-540 |
| A checkpoint of an already-completed master is refused, and that refusal is one definition read by both the checkpoint preflight and publication. | `require_series_checkpoint_authority`; "atomic-series-checkpoint-master-complete" | mcp/src/agents_remember/worktrees/series_closeout.py:139-160 |
| Publication revalidates the captured candidate against the live tips at the protected boundary and refuses a candidate that moved. | `_require_checkpoint_candidate_unchanged`; "atomic-series-checkpoint-candidate-moved" | mcp/src/agents_remember/worktrees/series_closeout.py:195-211 |
| The complete leaf set and exact pair chain are proved before sealing. | `_require_every_atomic_leaf_landed`, `_require_exact_atomic_landing_chain` | mcp/src/agents_remember/worktrees/series_closeout.py:212-215; mcp/src/agents_remember/worktrees/series_closeout.py:241-271 |
| Each leaf enclosure, code edge, and memory edge is bound exactly. | `_atomic_leaf_documents`, `_require_atomic_leaf_landed`, `_atomic_leaf_code_matches`, `_atomic_leaf_memory_matches` | mcp/src/agents_remember/worktrees/series_closeout.py:305-345; mcp/src/agents_remember/worktrees/series_closeout.py:346-376; mcp/src/agents_remember/worktrees/series_closeout.py:377-412; mcp/src/agents_remember/worktrees/series_closeout.py:413-448 |
| Atomic-master completion resolves the effective nature under the atomic-sequential default. | `_require_atomic_master_complete` | mcp/src/agents_remember/worktrees/series_closeout.py:449-488 |
| Exact series closeout rejects workbench changes and records the named memory pair. | `refuse_series_workbench_commit`, `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:489-506; mcp/src/agents_remember/worktrees/series_closeout.py:508-540 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE Atomic Completion Re-Proof

Series closeout no longer creates or mutates an initial queue state. It re-proves the atomic master
is complete and every atomic leaf is landed from canonical task/contract evidence, then repeats
that proof under the landing-only integration authority lock immediately before protected
publication. Door candidate/sprint identities no longer participate in the landed-leaf proof — that
comparison was deleted with the contract field by the closeout-door cut (commit `fad9808e`).
Scheduling projection absence is irrelevant to atomic completion truth.

## Update History
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:40+00:00 — 260831-LOCR-L34 reachability repair: recorded that the L30 checkpoint
  route was unreachable in both directions (a partial master could not reach the closeout-gated
  route; a complete one was refused) and never proved its real ref move, and what L34 changed —
  `capture_series_checkpoint_refs`/`SeriesCheckpointRefs` capturing the live code and memory work
  branch tips and proving their mapping through the same `exact_series_memory_closeout` the final
  route uses, the now-required and revalidated `expected` argument with its
  `atomic-series-checkpoint-candidate-moved` refusal, and `require_series_checkpoint_authority` as one
  definition with two callers. Recorded the closeout gate's extraction into
  `require_closeout_publication_authority` (leaf-exempt, read by both the preview and the apply) as
  instance 1 of the preview/apply parity invariant. Re-derived every reference range in this card for
  the new symbol block. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: added `publish_series_checkpoint_under_authority`,
  the missing partial-master verb that keeps every ref-protecting authority while dropping the
  "master is complete" and "every atomic leaf landed" assumptions; recorded the
  `atomic-series-checkpoint-master-complete` refusal that stops a checkpoint from downgrading a
  finished integration, the contract re-read before protected landing, and the invariant that the
  checkpoint route may not grow a completion proof. Re-derived every reference range in this card
  (the new function is inserted at L72, shifting all later symbols by ~37 lines). Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_require_atomic_master_complete` repointed to mcp/src/agents_remember/worktrees/series_closeout.py:309-346. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T12:02+02:00 — Closeout-door cut reconciliation at code commit `fad9808e`: removed the door dimension from the landed-leaf proof claim — `_AtomicLandingFacts` and its `door`/`door_sprint`/`door_candidate` comparisons were deleted with `contract.closeout_door`. Verification metadata remains pinned because only the cut-affected claims were reconciled; source documentation only, no acceptance claim.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.

- 2026-09-09T14:45+02:00 — CCR-L42 curator reconciliation: re-read affected claims against the frozen current source and corrected only their source anchors/ranges; verification stamps remain closeout-owned.

- 2026-08-29T17:23+02:00 — No content impact: reviewed the Python 3.13 local type-parameter migration for closeout and integration publication callbacks and confirmed that series authority remains as documented. Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: replaced initial queue-state publication with exact atomic completion and claimed-door re-proof at landing. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only imports the extracted `initial_queue_state` owner and calls the same initializer with the same arguments. Verified at code commit `1d446724`.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`) and the `unittest.main` tail guard removed where present; reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13: atomic closeout gates on the effective execution
  nature (nature-less legacy masters close out atomically under the default, L13-R5a), and a
  graph-less sprint's series edge publishes queue-free because the live series contract already
  owns the sequential lane (L13-R1). Verification remains closeout-owned.

- 2026-08-18T09:10+02:00 — No content impact: renamed the atomic 'barrier' concept to 'blocker' throughout; behavior unchanged. Verification remains closeout-owned.

- 2026-08-17T12:30+02:00 — 260815-DAG-L5: added `atomic_series_ledger_prefix` and made `_exact_atomic_landing_chain` return the ordered leaf chain. Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: created atomic series closeout authority onboarding from the frozen integration-authority candidate. Verification remains closeout-owned.
