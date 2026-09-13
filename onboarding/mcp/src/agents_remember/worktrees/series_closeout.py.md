# mcp/src/agents_remember/worktrees/series_closeout.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/series_closeout.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T17:38+02:00|
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Seals an atomic block only after every canonical leaf forms one exact journaled code-and-memory
landing chain, then records the named series refs without ambient workbench commits. Since
260831-LOCR-L30/L34 it also owns the *non-final* series exit:
`publish_series_checkpoint_under_authority` records a partial master's landed line under the same
ref-protecting authority while dropping only the completion assumptions. That route is a partial
**publication**, not a pause: it moves the master's committed code and memory refs onto its super
branch, where every other master sees them, and it requires the same explicit developer approval
the final route requires. Since 260831-LOCR-L36 the atomic completion proof orders the leaf chain
by the leaves' **own landed ancestry** instead of walking from the recorded base pair, and the
series closeout can record the pair a master **reconciled** with a sibling's landing through
`worktree_sync`.

## CCR-R12@v5 Current Series Boundary

Series closeout and integration remain recording/publication operations over already landed leaf
transactions. They re-prove canonical membership, exact code/memory ancestry, named-ref identity,
and authority before recording the pair; they do not create a normal leaf code/memory/ledger
transaction or invoke strict code quality, memory quality, selected certification, curator
coherence, or independent review. Full suites are an explicit developer request.

## Code Commentary

`_exact_atomic_landing_chain` cit:([`_exact_atomic_landing_chain`], mcp/src/agents_remember/worktrees/series_closeout.py:222-246) collects one exact enclosure per canonical leaf and
returns the ordered landed chain; `atomic_series_ledger_prefix` cit:([`atomic_series_ledger_prefix`], mcp/src/agents_remember/worktrees/series_closeout.py:550-572) derives the newest-first
ledger rows that chain contributes.

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

## 260831-LOCR-L30/L34 Checkpoint Authority: The Partial-Publication Verb, Made Reachable

`publish_series_integration_under_authority` proves the atomic master is a **finished unit** — its
task document is `Completed`, `_require_every_atomic_leaf_landed` cit:([`_require_every_atomic_leaf_landed`], mcp/src/agents_remember/worktrees/series_closeout.py:218-221) finds a landed enclosure for every
canonical leaf, and (since 260831-LOCR-L34, because the closeout apply now evaluates
`require_closeout_publication_authority`) it has closed out. An unfinished master has none of those,
so it could not land its accumulated line at all through that route.

**L30 wrote the checkpoint route; L34 is what made it reachable and closed its fail-open hole.**
L30's route kept every ref-protecting authority but read the commits to land from the contract's
closeout cells, which are exactly the completion facts an unfinished master does not have; its own note
admitted the real ref move was never proven end to end. L34 changes two things and nothing else:

- **The checkpoint captures its own candidate.**
  `capture_series_checkpoint_refs(contract)` cit:([`capture_series_checkpoint_refs`], mcp/src/agents_remember/worktrees/series_closeout.py:112-144) returns the frozen
  `SeriesCheckpointRefs` cit:([`SeriesCheckpointRefs`], mcp/src/agents_remember/worktrees/series_closeout.py:100-111) built from the **live** `code_work_branch` tip and the live
  `memory_work_branch` tip — captured, never inherited from a stale contract cell. It proves the
  code-to-memory mapping through `exact_series_memory_closeout` cit:([`exact_series_memory_closeout`], mcp/src/agents_remember/worktrees/series_closeout.py:825-842), the **exact-mapping** reader; the
  *final* series route reads the pair through `series_memory_closeout` instead (see the L36 section),
  so the checkpoint's claim is deliberately the narrower one. A capture that cannot prove the mapping
  raises, which makes "the refs are recorded only once their ledger mapping holds" a property of the
  value rather than a separate check a caller could skip. A non-`series` contract raises; an
  unresolvable code branch refuses (`atomic-series-checkpoint-no-code-ref`).
- **Publication revalidates that candidate.** `publish_series_checkpoint_under_authority(contract,
  publication, expected)` cit:([`publish_series_checkpoint_under_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:167-200) takes `expected` as a **required, never
  defaulted** third argument. A default would be a fail-open hole in exactly the repair it was
  written for: an omitted argument would silently admit whatever the live refs happened to be, i.e. a
  pair the preview never showed. `_require_checkpoint_candidate_unchanged` cit:([`_require_checkpoint_candidate_unchanged`], mcp/src/agents_remember/worktrees/series_closeout.py:201-217) re-reads the live refs and
  re-proves their ledger mapping at the protected boundary, immediately before the irreversible ref
  move, and refuses `atomic-series-checkpoint-candidate-moved` when they differ.

The checkpoint route keeps every authority that protects *other* owners' refs — the series contract
binding, the atomic landing authority, the source-lineage proof, the replay/ff source-state gate and
the master-handover gate all still run in the caller (`integrate.py::checkpoint_landing_result`) — and
drops only the completion assumptions. It retires nothing: no cleanup runs, and the recorded state is
`checkpointed` rather than `completed`.

**This route is a publication, not a pause (260831-LOCR-L36; the stop itself arrived in
260831-LOCR-L37).** A pause publishes nothing, moves no ref, and leaves the master's branch, worktrees
and enclosure private. At L36 no worktree tool performed it, and the registered description was
corrected to stop inviting an agent to reach this publication for an ordinary stop. L37 then added the
stop as its own verb — `worktree_pause`, in the working half of the surface, releasing the master's
activation selection and proposing no next call — so the sentence "no tool performs it" is no longer the
state of the tree and must not be repeated. Nothing about this checkpoint's weaker claim licenses
calling it the pause; the two are separate operations with separate registered descriptions
(`mcp/registration/worktrees.py::worktree_pause` and
`mcp/registration/closeout.py::worktree_checkpoint_landing`).

It still refuses, and the refusals are what keep the weaker claim from becoming a replacement for the
stronger one:

- `contract.kind != "series"` raises on both the capture and the authority (an ordinary leaf lands
  through `worktree_integrate`).
- A master whose task document already reads `Completed` raises
  `CloseoutQueueError("atomic-series-checkpoint-master-complete", ...)` and is pointed at the final
  route, so a checkpoint can never downgrade a finished integration. Since L34 that refusal lives in
  `require_series_checkpoint_authority` cit:([`require_series_checkpoint_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:145-166), **one definition with two callers**: the
  checkpoint's preflight (`integrate.py::checkpoint_landing_eligibility`) evaluates it so the dry run
  and the apply refuse identically and for the same named reason, and publication re-evaluates it so a
  master that completes *between* preflight and the ref move is refused there too.
- The contract is re-read after the master check and must still equal the passed contract, so the
  protected landing cannot run against a contract that changed underneath it.

## The One Closeout Gate Both Surfaces Read (260831-LOCR-L34)

`require_closeout_publication_authority(contract)` cit:([`require_closeout_publication_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:40-66) is the extracted body of the old
`publish_closeout_under_authority` gate. Its first statement is `if contract.kind == "leaf": return`,
which is exactly the shape the publication had, so no leaf closeout changes. Two callers read it:

- `publish_closeout_under_authority` (the apply) cit:([`publish_closeout_under_authority`], mcp/src/agents_remember/worktrees/series_closeout.py:67-79), which is now a thin wrapper; and
- `worktrees/modules/closeout.py::closeout_preview_payload` (the dry run), which previously ran the
  workbench-commit refusal and nothing else.

Before L34 the atomic-completion gate existed **only behind the apply**, which is why a partial
master's closeout preview answered `would-closeout` and then refused on every completion blocker (19
of them on LOCR). Closeout does not move a protected integration ref, so this gate deliberately does
not acquire the landing-only integration authority lock. **This is instance 1 of the preview/apply
parity invariant recorded on the `worktrees/overview.md` route and in
`memory_quality/overview.md`.**

## 260831-LOCR-L36: The Reconciled Series Completion

The completion proof used to walk the leaf chain from `series.code_base_commit` /
`series.memory_base_commit` and require each leaf's recorded base to equal the previous landing.
`worktree_sync` advances that recorded pair to the official line the master absorbed, while a leaf
landed before the reconciliation keeps the base it really started from — so the walk could not even
find its first leaf, and a master reconciling with a sibling's landing failed
`atomic-series-leaf-chain-invalid`. The proof now reads the order from the **landings themselves**,
and the series closeout accepts the pair the reconciliation produced.

**Order from landed ancestry.** `_ordered_atomic_landing_chain` cit:([`_ordered_atomic_landing_chain`], mcp/src/agents_remember/worktrees/series_closeout.py:272-304) proves every leaf landed
(`_require_atomic_leaf_landed` cit:([`_require_atomic_leaf_landed`], mcp/src/agents_remember/worktrees/series_closeout.py:663-693)) and then repeatedly takes the one remaining leaf whose landing
precedes every other remaining leaf on both sides of the pair —
`_leaf_landing_precedes` cit:([`_leaf_landing_precedes`], mcp/src/agents_remember/worktrees/series_closeout.py:305-329): the code commit must be a proper ancestor (`==` is not an ordering)
and, for external memory, the ledger commit must be an ancestor too. A non-unique choice still
refuses `atomic-series-leaf-chain-invalid`.

**Origin.** `_require_chain_origin` cit:([`_require_chain_origin`], mcp/src/agents_remember/worktrees/series_closeout.py:330-363) applies two rules. With no recorded sync, the oldest leaf must
still start at the recorded base **exactly**, which is the rule the old walk enforced for every
step. Once a sync exists, the oldest leaf's base and the position the first sync advanced from —
`_series_pre_sync_base` cit:([`_series_pre_sync_base`], mcp/src/agents_remember/worktrees/series_closeout.py:364-373) reads `codeBaseFrom`/`memoryBaseFrom` from `sync_log[0]` — must lie on one
line (`_require_same_line` cit:([`_require_same_line`], mcp/src/agents_remember/worktrees/series_closeout.py:374-388), either direction, because a leaf may have landed
before or after the sync), and every leaf must start at or after the chain origin
(`_require_leaf_starts_on_the_chain` cit:([`_require_leaf_starts_on_the_chain`], mcp/src/agents_remember/worktrees/series_closeout.py:389-414)).

**Spine.** `_require_landing_spine_side` cit:([`_require_landing_spine_side`], mcp/src/agents_remember/worktrees/series_closeout.py:415-458) proves one series ref is exactly the leaf landings joined by
the reconciled source line, on the code side and (for external memory) the memory side. Every
landing must be an ancestor of the ref; each step from one landing to the next must add nothing
beyond the previous landing plus the official positions this contract actually synced with —
`_require_admitted_step` cit:([`_require_admitted_step`], mcp/src/agents_remember/worktrees/series_closeout.py:493-530) asks `git rev-list --no-merges later --not earlier <positions>` and refuses any
surviving commit, so a merge is the reconciliation device rather than a loophole; the step from the
last landing to the ref is proved the same way, and a ref that simply *is* the last landing (every
master that reconciled before its final leaf landed) needs no step at all. The admitted positions
are `_landing_source_positions` cit:([`_landing_source_positions`], mcp/src/agents_remember/worktrees/series_closeout.py:540-549) — the recorded base plus every `codeBaseTo`/`memoryBaseTo` in the
sync log. On the memory side a commit that rewrites **only** `memory.md`
(`_is_ledger_recording` cit:([`_is_ledger_recording`], mcp/src/agents_remember/worktrees/series_closeout.py:531-539)) is admitted: a reconciled master records its own ledger
bookkeeping on its memory line, and the evidence for that is the landed table itself.

**The master's own rows.** `atomic_series_ledger_prefix` returns the leaf rows newest-landing-first
and, when the contract has a sync log, `_reconciled_ledger_prefix` cit:([`_reconciled_ledger_prefix`], mcp/src/agents_remember/worktrees/series_closeout.py:573-591) adds one row per reconciliation. Those
rows are read back from the landed table `observed_ledger_state` names and are never taken on trust:
`_is_reconciliation_row` cit:([`_is_reconciliation_row`], mcp/src/agents_remember/worktrees/series_closeout.py:592-621) accepts a row only when its code commit is a merge of the
master's own first-parent line whose every *other* parent is reachable from an official position this
contract synced with, and that is still an ancestor of the code work-branch tip. A leaf landing's
merge fails that test — its other parent is the leaf's own branch — which keeps this a census of the
master's own recorded rows rather than a licence for any merge at all.

**The recorded pair.** `exact_series_memory_closeout` cit:([`exact_series_memory_closeout`], mcp/src/agents_remember/worktrees/series_closeout.py:825-842) is unchanged in shape: it reads the exact
memory ref, requires the landed ledger to map the exact code commit, and proves the mapped memory
content reachable from that ref
(`_require_series_memory_reachable` cit:([`_require_series_memory_reachable`], mcp/src/agents_remember/worktrees/series_closeout.py:903-913), over `_series_ledger_mapping` cit:([`_series_ledger_mapping`], mcp/src/agents_remember/worktrees/series_closeout.py:885-895) and
`_series_ledger` cit:([`_series_ledger`], mcp/src/agents_remember/worktrees/series_closeout.py:896-902)). `series_memory_closeout` cit:([`series_memory_closeout`], mcp/src/agents_remember/worktrees/series_closeout.py:843-884)
first tries exactly that, so the ordinary shape is read exactly as before. When the exact mapping is
absent it accepts the **reconciled** pair instead, but only after proving the same two facts
integration later recomputes: the master's own chain tip is still a row of the landed table with its
memory content reachable (otherwise `reconciled series closeout requires the ledger to still map the
master's own chain tip`), and the landed table is the exact projection of its source plus this
branch's own true rows — `_require_series_ledger_projection` cit:([`_require_series_ledger_projection`], mcp/src/agents_remember/worktrees/series_closeout.py:914-930) evaluates
`ledger_projection.contract_ledger_projection` and requires `is_fixed_point`, so a dropped,
reordered or replaced source row is refused. The recorded pair is then the reconciled code tip
against the memory ref the same sync landed. A closeout of a code commit that is not the chain tip
and is not mapped still refuses — integration branches are not closeout workbenches.

**No public tool records the reconciled pair.** A sync creates the code merge commit *after* the
retained memory conflict is resolved, so no closeout or resolution pass could have written a row
naming it; the workflow's own due step is an **agent-owned `memory.md` write** on the memory work
branch (the test helper `_record_reconciled_pair` performs exactly that write and nothing else).
There is deliberately **no public operation** for it — a follow-up pass that would have made the
recording a public tool was cancelled by the developer.

## Invariants And Boundaries

- Atomic membership comes from exact master task rows and canonical parent relations, not sibling-file discovery.
- **The leaf chain is ordered by the landings' own ancestry, not by the recorded base pair.** A leaf's
  recorded base is the position it really started from, so it stops matching the master's recorded base
  as soon as `worktree_sync` advances that base; ordering from bases cannot survive a reconciliation.
- **Every step on a series ref is admitted, never assumed.** Between two landings, and from the last
  landing to the ref, only the previous landing plus the official positions this contract itself
  synced with may enter history; a merge introduces no commit of its own, and on the memory side only
  a ledger-only recording commit is additionally admitted.
- **A reconciliation row is proved from the table and the repository.** It is read back from the
  landed ledger and re-checked as a merge of the master's own first-parent line with a synced official
  position; it is never guessed from closeout cells.
- **The reconciled pair is recorded only when the landed table is the exact projection of its source
  plus this line's own true rows.** Accepting the reconciled tip never weakens the row-set promise.
- **Recording that pair is agent-owned.** No public tool performs it.
- Every external memory pair proves base-to-content and content-to-ledger ancestry plus exact ledger mapping.
- Series closeout records named refs and never commits ambient repository-root worktrees.
- The effective nature, not graph presence alone, gates the atomic closeout path; graph-less
  atomic-sequential is valid.
- **Completion is proved, never assumed, on the final route — and never claimed on the checkpoint
  route.** `publish_series_checkpoint_under_authority` may not be extended to also prove the master
  complete: the two routes exist precisely so that "landed" and "finished" stay separate claims, and
  the checkpoint route's `atomic-series-checkpoint-master-complete` refusal is the boundary between
  them.
- **The checkpoint publishes; it does not pause.** Its ref move is a protected-branch publication
  that other masters see, and its description must keep saying so. A pause is an ordinary stop that
  moves no ref.
- **The checkpoint's `expected` argument must never gain a default (260831-LOCR-L34).** It is the
  candidate the preview showed; defaulting it would re-open the fail-open hole the repair closed, by
  admitting whatever the live refs happen to be at publication time. Revalidation against the live
  tips immediately before the ref move is the entire reason the route can promise a pair.
- **The checkpoint and the final series route read the pair through different readers, on purpose.**
  The checkpoint proves the *exact* mapping (`exact_series_memory_closeout`); the final route may
  accept the reconciled pair (`series_memory_closeout`). Neither may borrow the other's claim.
- **The closeout gate has exactly one definition (260831-LOCR-L34).** `closeout_preview_payload` and
  `publish_closeout_under_authority` both call `require_closeout_publication_authority`; do not
  re-inline a copy behind either surface. A preview that plans a closeout its apply refuses is the
  defect this extraction removed, and it misled a human into writing a false note on LOCR.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Closeout re-proves canonical completion without the landing lock; integration repeats it under the narrow protected-landing lock; the checkpoint route keeps every ref authority and drops only the completion assumptions. | `publish_closeout_under_authority`, `publish_series_integration_under_authority`, `publish_series_checkpoint_under_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:67-79; mcp/src/agents_remember/worktrees/series_closeout.py:80-99; mcp/src/agents_remember/worktrees/series_closeout.py:167-200 |
| The closeout completion gate is extracted into one definition with one body, and its first statement exempts a leaf, so the closeout preview and the closeout apply refuse identically. | `require_closeout_publication_authority` | mcp/src/agents_remember/worktrees/series_closeout.py:40-66 |
| The checkpoint captures its own live candidate refs from the live code and memory work-branch tips and proves their exact ledger mapping. | `SeriesCheckpointRefs`; `capture_series_checkpoint_refs`; `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:100-111; mcp/src/agents_remember/worktrees/series_closeout.py:112-144; mcp/src/agents_remember/worktrees/series_closeout.py:825-842 |
| A checkpoint of an already-completed master is refused, and that refusal is one definition read by both the checkpoint preflight and publication. | `require_series_checkpoint_authority`; "atomic-series-checkpoint-master-complete" | mcp/src/agents_remember/worktrees/series_closeout.py:145-166; mcp/src/agents_remember/worktrees/series_closeout.py:161-161 |
| Publication revalidates the captured candidate against the live tips at the protected boundary and refuses a candidate that moved. | `_require_checkpoint_candidate_unchanged`; "atomic-series-checkpoint-candidate-moved" | mcp/src/agents_remember/worktrees/series_closeout.py:201-217 |
| The complete leaf set is proved and the landing order is read from the landings' own ancestry on both sides of the pair. | `_require_every_atomic_leaf_landed`; `_exact_atomic_landing_chain`; `_ordered_atomic_landing_chain`; `_leaf_landing_precedes` | mcp/src/agents_remember/worktrees/series_closeout.py:218-221; mcp/src/agents_remember/worktrees/series_closeout.py:222-246; mcp/src/agents_remember/worktrees/series_closeout.py:272-304; mcp/src/agents_remember/worktrees/series_closeout.py:305-329 |
| The chain origin is the recorded base exactly without a sync, and one line with the first sync's pre-state once a sync exists; every leaf starts on that line. | `_require_chain_origin`; `_series_pre_sync_base`; `_require_same_line`; `_require_leaf_starts_on_the_chain` | mcp/src/agents_remember/worktrees/series_closeout.py:330-363; mcp/src/agents_remember/worktrees/series_closeout.py:364-373; mcp/src/agents_remember/worktrees/series_closeout.py:374-388; mcp/src/agents_remember/worktrees/series_closeout.py:389-414 |
| One series ref equals the leaf landings joined by the reconciled source line, and only a ledger-only recording commit is additionally admitted on the memory side. | `_require_landing_spine_side`; `_require_admitted_step`; `_is_ledger_recording`; `_landing_source_positions` | mcp/src/agents_remember/worktrees/series_closeout.py:415-458; mcp/src/agents_remember/worktrees/series_closeout.py:493-530; mcp/src/agents_remember/worktrees/series_closeout.py:531-539; mcp/src/agents_remember/worktrees/series_closeout.py:540-549 |
| The master's own reconciliation rows are read back from the landed table and each is proved to be a merge of its first-parent line with a synced official position. | `atomic_series_ledger_prefix`; `_reconciled_ledger_prefix`; `_is_reconciliation_row` | mcp/src/agents_remember/worktrees/series_closeout.py:550-572; mcp/src/agents_remember/worktrees/series_closeout.py:573-591; mcp/src/agents_remember/worktrees/series_closeout.py:592-621 |
| The final series closeout records the exact pair when the ledger maps the code tip, and otherwise the reconciled pair after proving the master's own chain tip is still mapped and the landed table is the projection of its source plus this line's own rows. | `series_memory_closeout`; `_require_series_ledger_projection`; `_series_ledger_mapping`; `_series_ledger`; `_require_series_memory_reachable` | mcp/src/agents_remember/worktrees/series_closeout.py:843-884; mcp/src/agents_remember/worktrees/series_closeout.py:914-930; mcp/src/agents_remember/worktrees/series_closeout.py:885-895; mcp/src/agents_remember/worktrees/series_closeout.py:896-902; mcp/src/agents_remember/worktrees/series_closeout.py:903-913 |
| The exact-mapping reader is kept for the checkpoint route, and the exact closeout still refuses a code commit that is not mapped. | `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:825-842 |
| Each leaf enclosure, code edge, and memory edge is bound exactly. | `_atomic_leaf_documents`, `_require_atomic_leaf_landed`, `_atomic_leaf_code_matches`, `_atomic_leaf_memory_matches` | mcp/src/agents_remember/worktrees/series_closeout.py:622-662; mcp/src/agents_remember/worktrees/series_closeout.py:663-693; mcp/src/agents_remember/worktrees/series_closeout.py:694-729; mcp/src/agents_remember/worktrees/series_closeout.py:730-759 |
| Atomic-master completion resolves the effective nature under the atomic-sequential default. | `_require_atomic_master_complete` | mcp/src/agents_remember/worktrees/series_closeout.py:766-805 |
| Exact series closeout rejects workbench changes and records the named memory pair. | `refuse_series_workbench_commit`, `exact_series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:806-824; mcp/src/agents_remember/worktrees/series_closeout.py:825-842 |
| The reconciled-pair recording is an agent-owned `memory.md` write with no public tool behind it. | `_record_reconciled_pair` | mcp/tests/test_cross_master_concurrency.py:384-412 |

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
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: corrected this card's L36 sentence that "no worktree tool
  performs it". The stop now exists as its own public verb (`worktree_pause`, registered by the
  working-half registrar), so the card states the L36 state as history and names the two separate
  registered descriptions that now point at each other. The checkpoint's own publication account is
  unchanged. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T17:38+02:00 -- 260831-LOCR-L36 curator reconciliation against the changed code
  candidate. Recorded that the atomic completion proof no longer anchors the leaf chain at
  `series.code_base_commit`/`series.memory_base_commit` (which `worktree_sync` advances): the order
  now comes from the leaves' own landed ancestry (`_ordered_atomic_landing_chain`,
  `_leaf_landing_precedes`), the origin is the recorded base exactly only without a sync and one
  line with the first sync's pre-state once a sync exists (`_require_chain_origin`,
  `_series_pre_sync_base`, `_require_same_line`, `_require_leaf_starts_on_the_chain`), and one
  series ref is proved to be the leaf landings joined only by the official positions this contract
  synced with (`_require_landing_spine_side`, `_require_admitted_step`, `_is_ledger_recording`,
  `_landing_source_positions`). Recorded the new reconciled-pair path: `atomic_series_ledger_prefix`
  now includes the master's own proved reconciliation merges, and the series closeout accepts the
  reconciled tip through `series_memory_closeout` only after proving the master's own chain tip is
  still mapped and the landed table is the exact projection of its source plus this line's own true
  rows (`_require_series_ledger_projection`). Corrected the earlier claim that the checkpoint and
  the final series closeout share one reader: the checkpoint reads the exact mapping through
  `exact_series_memory_closeout`, the final route may accept the reconciled pair through
  `series_memory_closeout`. Stated that recording the reconciled pair remains an agent-owned
  `memory.md` write (the test helper `_record_reconciled_pair`) with **no public tool**, because the
  developer cancelled the follow-up pass that would have made it public. Recorded that a checkpoint
  is a partial PUBLICATION, not a pause: it moves both refs onto the super branch under explicit
  developer approval, while a pause publishes nothing and moves no ref. Re-derived every reference
  range in this card for the rewritten symbol block. Verification metadata remains closeout-owned;
  no acceptance claim.
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
