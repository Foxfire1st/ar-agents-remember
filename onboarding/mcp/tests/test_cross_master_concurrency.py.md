# mcp/tests/test_cross_master_concurrency.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_cross_master_concurrency.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T17:52+02:00 |
| lastVerifiedCommitHash | `e0820b04a499cbfb2079c78485346c50917a238a` |
| lastVerifiedCommitDate | 2026-09-13T18:02:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Cross-master concurrency on one protected source pair: the forcing test for the contract-scoped
atomic-series activation record, and (since 260831-LOCR-L36) for the reconciled series completion.

One sprint commands every atomic master from its own integration branch, so two atomic masters
commanded by the same sprint derive the SAME protected source pair (same code repository and source
branch, same memory repository and source branch; only the work branches differ). The activation
record used to be keyed by that pair, so the second master's selection replaced the first's and the
closeout projection reported the displaced master as `atomic-series-paused-by:` and held it waiting.

This module drives **real temporary Git repositories** and the **public operations** to prove the
record is now per contract, and that a master which stays unfinished, is stopped, resumes, reconciles
with a sibling's landing and then finishes does so through the ordinary public routes:

1. both masters progress concurrently and each keeps its own record;
2. each master's work stays private until it lands;
3. landing stays protected against a conflicting or stale publication;
4. a stopped master publishes nothing and no worktree tool performs the stop; and
5. a master that reconciles with a landed sibling completes through **ordinary closeout and final
   integration** — a checkpoint is never a substitute for completion; and
6. a genuine wave dependency from the sprint execution graph still gates, while a graph-less sprint
   serializes nothing between its atomic masters.

## Code Commentary

### Logic

`CrossMasterConcurrencyTests` builds one real temporary Git world in `setUp` from
`test_closeout_queue.QueueFixture(root, atomic_a=True, atomic_b=True, memory_mode="external")` —
disposable code and external-memory repositories, two atomic master documents, real series/leaf
contracts and a real `memory.md` ledger — declares the test process, and resolves each master's
canonical **series** contract through `_series(load_contract(...))` cit:([`_series`], mcp/tests/test_cross_master_concurrency.py:88-93). The behaviour is asserted against
`MASTER_A`/`MASTER_B`/`NOW` and the public operations, not against the removed pair-keyed helpers.

The nine cases, in the order the module groups them:

- `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready` cit:([`test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready`], mcp/tests/test_cross_master_concurrency.py:131-162) asserts the premise rather
  than assuming it: both series report `code_source_branch == "super"` and equal memory source
  branches, with different work branches and different `activation_path` values. `_select_both()`
  publishes `active` on B first and then A, and both observations stay `active` on their own master,
  both `project_series_activation` projections report an empty `waiting` tuple, and both closeout
  members come back `classification == "ready"` with no reasons.
- `test_master_a_experimental_code_and_memory_stay_private_until_it_lands` cit:([`test_master_a_experimental_code_and_memory_stay_private_until_it_lands`], mcp/tests/test_cross_master_concurrency.py:166-189) commits an
  A-only code file and an A-only memory file on A's own work branches, then proves neither reaches the
  pair's source branches (`super` in both repositories), the sibling master's worktree, or the other
  master's work branch — while A's own line carries it and A is still the selected owner of its own
  record.
- `test_master_b_lands_its_leaf_while_master_a_is_unfinished` cit:([`test_master_b_lands_its_leaf_while_master_a_is_unfinished`], mcp/tests/test_cross_master_concurrency.py:193-212) closes and lands B's atomic leaf through
  the public integrate route (`_close_out_and_land_leaf`), then proves B's own line moved onto B's
  master branch while A stayed exactly where it was, B's leaf contract is `completed`, and B's
  **series** contract is still `not-started`.
- `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible` cit:([`test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible`], mcp/tests/test_cross_master_concurrency.py:465-512) records both source revisions
  and A's own line, releases A's activation selection, and proves the release published nothing (both
  `super` refs and A's work branch are unchanged), A's work survived, B is still `active` on B's own
  master, and a rebuilt status still classifies **both** members `ready` with no reasons. Its
  docstring is explicit that this is deliberately **not** the pause: the release is the state
  transition the sync-cancel and terminal routes need, and calling it is not what pausing a master
  means. The pause itself — an ordinary stop that publishes nothing and advances nothing — is covered
  by the completion case below through `_require_pause_left_a_private`.
- `test_a_conflicting_publication_cannot_overwrite_master_b` cit:([`test_a_conflicting_publication_cannot_overwrite_master_b`], mcp/tests/test_cross_master_concurrency.py:529-563) first lands B's accumulated line through
  `_land_master_b_line` (which publishes through the public checkpoint route and asserts the ledger
  ref landed), then attempts A's non-fast-forwardable checkpoint: it is refused as `blocked-non-ff`
  with both source refs and B's landing intact, B's ledger mapping still resolves through
  `find_mapping`, and a stale hand-made candidate is refused as
  `atomic-series-checkpoint-candidate-moved` while still moving nothing.
- `test_master_a_resumes_reconciles_and_completes_after_master_b_landed` cit:([`test_master_a_resumes_reconciles_and_completes_after_master_b_landed`], mcp/tests/test_cross_master_concurrency.py:565-623) is the completion case, and it uses
  **no checkpoint**. A lands its first leaf and stays private while B completes and integrates
  normally; `_require_pause_left_a_private` then proves that stopping A published nothing, moved no
  ref and advanced no unstarted leaf (the commanded A2 row and its document are untouched, no
  enclosure and no worktree exist, and its single step is still `pending`), while B's landing stands.
  A then resumes and reconciles B's landing through the **public sync path** (`_public_sync`),
  validates and records the resulting code/memory pair, starts its remaining never-started leaf on
  the reconciled line, lands that leaf, and completes through the public closeout and integrate
  routes (`_closeout_and_land_master`, which asserts `state == "integrated"`).
  `_require_both_ledger_histories` proves the landed series ledger maps B's landing, both of A's
  candidates and A's final pair, that A's own row is first, and that the contract reads
  `integration_status == "completed"` with `cleanup == "pending"`.
- `test_explicit_checkpoint_landing_remains_available_when_requested` cit:([`test_explicit_checkpoint_landing_remains_available_when_requested`], mcp/tests/test_cross_master_concurrency.py:720-753) proves the explicit route is
  unchanged for an open master: the preview reports `would-checkpoint` with `closeoutRequired: False`,
  `approvalRequired: True` and `ledgerMappingVerified: True` and moves nothing; the apply moves both
  refs, records `checkpointed`, leaves `closeout_status` `not-started`, keeps the code worktree, and
  leaves the sibling unfinished master `active`.
- `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` cit:([`test_a_dependent_master_still_waits_for_its_unfinished_predecessor`], mcp/tests/test_cross_master_concurrency.py:754-782) rebuilds the world with
  `edge=True` — the sprint execution graph's real `MASTER_A -> MASTER_B` edge — and proves that with
  activation exclusivity gone B is still `active` in its own record, the predecessor member is
  `ready`, and the dependent member is `waiting` with exactly
  `predecessor-incomplete: <MASTER_A.key>`. The sprint's own wave gate is what still holds B.
- `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` cit:([`test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters`], mcp/tests/test_cross_master_concurrency.py:786-854) is the ruling's graph-less half. It rewrites the
  sprint document with `executionGraph=None` and asserts the resolved `SchedulingMode` is exactly
  `atomic-sequential`, that both commanded masters (`MASTER_A`, `MASTER_B`) are in `mode.masters`, and
  that `mode.facts` is the one new single-element tuple `"executionGraph absent: atomic-sequential
  default — every commanded master executes atomically and no dependency is declared, so nothing
  serializes the masters"`. It then selects both masters and proves each observation is
  `state == "active"` naming its own `selected_master`, with `project_series_activation(...).waiting
  == ()` for both — so no master is held because a sibling is selected; the graph-less projection
  classifies both members `ready` with no reasons. The case closes at the seam that still refuses a
  caller whose already-resolved graph the canonical document no longer carries:
  `graph_context(..., authored_graph=...)` raises `CloseoutQueueError` with status
  `task-execution-topology-migration-required`, and the detail contains `nothing serializes the
  masters` and no `source-pair` text. The sprint-with-a-graph half of the same ruling stays with the
  wave case above, which is why this case asserts only the graph-less half.

The helpers keep the cases honest. `_close_out_and_land_leaf` cit:([`_close_out_and_land_leaf`], mcp/tests/test_cross_master_concurrency.py:214-222) drives the public integrate route for one atomic leaf;
`_land_leaf_contract` cit:([`_land_leaf_contract`], mcp/tests/test_cross_master_concurrency.py:224-289) authors and lands one leaf's code, memory content and ledger mapping the way the fixture does;
`_complete_master_documents` cit:([`_complete_master_documents`], mcp/tests/test_cross_master_concurrency.py:291-311) marks the master and every canonical leaf row `Completed`, which is the plan
fact ordinary closeout requires; `_closeout_and_land_master` cit:([`_closeout_and_land_master`], mcp/tests/test_cross_master_concurrency.py:313-338) runs the **public** closeout apply and
integrate tools and asserts `closed` and `integrated`; and `_public_sync` cit:([`_public_sync`], mcp/tests/test_cross_master_concurrency.py:340-374) drives `worktree_sync_tool`, resolving a retained memory
conflict the way the workflow requires by keeping every mapping from both sides and continuing the
same contract-addressed sync.

The reconciled pair is recorded by `_record_reconciled_pair` cit:([`_record_reconciled_pair`], mcp/tests/test_cross_master_concurrency.py:384-412), and that helper is deliberately an **agent-owned
`memory.md` write**: it adds a worktree on the memory work branch, prepends one mapping row for the
reconciled code tip against the memory ref the same sync landed, commits, and removes the worktree
again. Nothing more exists, because the workflow owes that row and a sync creates the code merge
*after* the retained conflict was resolved — **no public tool records the reconciled pair** (a
follow-up pass that would have made it public was cancelled by the developer).
`_private_master_a_facts` cit:([`_private_master_a_facts`], mcp/tests/test_cross_master_concurrency.py:414-445) and `_require_pause_left_a_private` cit:([`_require_pause_left_a_private`], mcp/tests/test_cross_master_concurrency.py:624-640) take the
before/after snapshot a stop must leave untouched; `_paused_fixture` cit:([`_paused_fixture`], mcp/tests/test_cross_master_concurrency.py:447-461) rebuilds the world with the still-unstarted second
canonical leaf; `_reconcile_master_a` cit:([`_reconcile_master_a`], mcp/tests/test_cross_master_concurrency.py:642-662) and `_land_remaining_master_a_leaf` cit:([`_land_remaining_master_a_leaf`], mcp/tests/test_cross_master_concurrency.py:664-678) carry the resume half;
`_require_ledger_maps` cit:([`_require_ledger_maps`], mcp/tests/test_cross_master_concurrency.py:680-692) and `_require_both_ledger_histories` cit:([`_require_both_ledger_histories`], mcp/tests/test_cross_master_concurrency.py:694-716) prove the landed mappings; and
`_checkpoint_with_candidate` cit:([`_checkpoint_with_candidate`], mcp/tests/test_cross_master_concurrency.py:857-875) publishes through the route's own candidate-validation
boundary (`publish_series_checkpoint_under_authority`) and returns the refusal status instead of
asserting it. `_member` cit:([`_member`], mcp/tests/test_cross_master_concurrency.py:94-99) and `_tree` cit:([`_tree`], mcp/tests/test_cross_master_concurrency.py:100-104) read one member row and one branch's tree
listing.

### Conventions

A `unittest` class in the `mcp/tests` convention: one real temporary Git world per case, cleaned up in
`tearDown`, with the wave and completion cases rebuilding their own world because they need the graph
edge or a second unstarted leaf. It composes existing fixtures instead of adding new ones —
`QueueFixture` and the shared constants come from `test_closeout_queue`, the Git/ledger helpers
(`_accumulate_master_line`, `_checkpoint`, `_memory_repository`, `_rev`) from
`test_checkpoint_landing_end_to_end`, `git` from `test_worktree_support`, and the closeout support
helpers from `closeout_input_test_support` — and `setUp` calls `declare_test_process()` before
touching real repositories.

It is registered in the **integration** lane of `mcp/tests/test-evidence-lanes.toml` (row 143) and as
a consumer in both shared-support artifacts of `mcp/tests/evidence-lifecycle.toml`; that manifest is
fail-closed, so an unregistered tracked module is a hard load failure rather than a silent gap.
Registration is classification only, and lane membership is never execution or acceptance evidence.

### Invariants And Boundaries

- The shared protected source pair is asserted, not assumed: one sprint command means one pair, and
  only the work branches differ.
- One activation record per series contract. A sibling's selection, pause or landing never replaces
  or holds another contract's record.
- **Publishing, stopping and pausing are three different things.** A checkpoint (the explicit route)
  publishes committed refs onto the protected source branch under developer approval and records
  `checkpointed`; a *release* of the activation selection moves no ref and is what sync-cancel and
  terminal cleanup need; a *pause* is an ordinary stop that publishes nothing, moves no ref, advances
  no unstarted leaf, and is performed by no worktree tool. A stopped master is not a waiting master
  and blocks no sibling.
- **Completion is ordinary.** A master that reconciles with a landed sibling still finishes through
  the public closeout and integrate routes and reads `integration_status == "completed"` with
  `cleanup == "pending"`; a checkpoint is never accepted in place of either, and this module's
  completion case never calls one.
- **The reconciled pair is recorded by an agent-owned `memory.md` write, not a tool.** The helper
  performs exactly that write; there is no public operation for it.
- Landing is a compare-and-swap against the pair: a candidate that is not fast-forwardable is refused
  as `blocked-non-ff` and a moved candidate is refused as
  `atomic-series-checkpoint-candidate-moved`; both leave the source refs and the already-landed ledger
  mapping exactly as they were.
- Only the sprint execution graph's own wave dependency holds a dependent master
  (`predecessor-incomplete:`). Nothing serializes a graph-less sprint: `atomic-sequential` describes
  the sprint's SHAPE — every commanded master executes atomically — not a serialization mechanism, so
  independent masters proceed concurrently and no master is held because another is selected. This
  module does not re-implement scheduling; its graph-less case asserts the resolved mode and the
  per-contract projections rather than owning them.
- The cases concern repositories created inside a temporary directory by the fixture; they do not
  establish a live control-plane run, production scheduler behaviour, or acceptance.

### Todos

None.

## Docs References

No Domain Documentation entries are configured in this memory root (`system/sources.md` declares no
entries). Every claim here is about this repository's own activation record, refs, contracts and
ledger projection, so the retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain evidence applies. | N/A | N/A |

## Repo-Internal References

The current source cases below establish the concurrency behaviour; this inventory is not execution
evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Two unfinished masters share one protected source pair and both stay ready. | `test_two_unfinished_masters_share_one_source_pair_and_both_stay_ready` | mcp/tests/test_cross_master_concurrency.py:131-162 |
| An unfinished master's experimental code and memory stay private until it lands. | `test_master_a_experimental_code_and_memory_stay_private_until_it_lands` | mcp/tests/test_cross_master_concurrency.py:166-189 |
| Master B lands its leaf while master A is unfinished, and B's series contract stays open. | `test_master_b_lands_its_leaf_while_master_a_is_unfinished` | mcp/tests/test_cross_master_concurrency.py:193-212 |
| Releasing master A's activation publishes nothing and leaves master B eligible; this is deliberately not the pause. | `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible` | mcp/tests/test_cross_master_concurrency.py:465-512 |
| A conflicting publication cannot overwrite master B's landed line, and a stale candidate is refused without moving anything. | `test_a_conflicting_publication_cannot_overwrite_master_b` | mcp/tests/test_cross_master_concurrency.py:529-563 |
| Master A is stopped without publishing, resumes through the public sync, lands its remaining leaf and completes through ordinary closeout and integration without losing B's mapping. | `test_master_a_resumes_reconciles_and_completes_after_master_b_landed` | mcp/tests/test_cross_master_concurrency.py:565-623 |
| The explicit checkpoint landing route is unchanged for an open master. | `test_explicit_checkpoint_landing_remains_available_when_requested` | mcp/tests/test_cross_master_concurrency.py:720-753 |
| A genuine sprint-graph wave dependency still gates a dependent master. | `test_a_dependent_master_still_waits_for_its_unfinished_predecessor` | mcp/tests/test_cross_master_concurrency.py:754-782 |
| A graph-less sprint resolves to the atomic-sequential shape and serializes nothing: both commanded masters hold their own activation concurrently with no waiting reason, and the stale-graph seam still refuses with the ruling in its detail. | `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` | mcp/tests/test_cross_master_concurrency.py:786-854 |
| The stop snapshot helper: everything a pause must leave exactly as it was for an unfinished private master. | `_private_master_a_facts`; `_require_pause_left_a_private` | mcp/tests/test_cross_master_concurrency.py:414-445; mcp/tests/test_cross_master_concurrency.py:624-640 |
| The closeout-and-land helper drives the public closeout apply and integrate tools and asserts `closed` then `integrated`. | `_closeout_and_land_master`; `_complete_master_documents` | mcp/tests/test_cross_master_concurrency.py:313-338; mcp/tests/test_cross_master_concurrency.py:291-311 |
| The public sync helper reconciles the contract and resolves a retained memory conflict by keeping every mapping from both sides. | `_public_sync` | mcp/tests/test_cross_master_concurrency.py:340-374 |
| The reconciled pair is recorded by an agent-owned `memory.md` write; no public tool performs it. | `_record_reconciled_pair` | mcp/tests/test_cross_master_concurrency.py:384-412 |
| The resume half: reconcile A, then start and land A's remaining never-started leaf. | `_reconcile_master_a`; `_land_remaining_master_a_leaf` | mcp/tests/test_cross_master_concurrency.py:642-662; mcp/tests/test_cross_master_concurrency.py:664-678 |
| The landed-mapping proofs the completion case reads. | `_require_ledger_maps`; `_require_both_ledger_histories` | mcp/tests/test_cross_master_concurrency.py:680-692; mcp/tests/test_cross_master_concurrency.py:694-716 |
| The checkpoint candidate-validation boundary helper the stale-candidate case uses. | `_checkpoint_with_candidate` | mcp/tests/test_cross_master_concurrency.py:857-875 |
| The leaf-landing helper the private-work and privacy cases reuse. | `_close_out_and_land_leaf`; `_land_leaf_contract` | mcp/tests/test_cross_master_concurrency.py:214-222; mcp/tests/test_cross_master_concurrency.py:224-289 |
| The record path is keyed by the contract fingerprint rather than any source pair. | "def contract_fingerprint("; "def activation_path(" | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:130-144 |
| The selection transition writes only the addressed contract's own record. | `publish_atomic_series_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:155-214 |
| Only this contract's own reconciling state is a waiting reason. | `activation_waiting_reason` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:275-289 |
| A record whose fingerprint or contract path belongs to another contract is refused on read. | `_require_record_identity` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation.py:360-374 |
| The release transition requires the exact selection it addresses. | `release_atomic_series_selection` | mcp/src/agents_remember/worktrees/activation/atomic_series_activation_release.py:23-55 |
| The closeout projection consumes the record's own waiting reason, so a sibling master is never projected as a blocker. | `project_series_activation` | mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py:29-53 |
| The series completion the case reaches is the reconciled-pair closeout, not a checkpoint. | `series_memory_closeout` | mcp/src/agents_remember/worktrees/series_closeout.py:843-884 |
| The real temporary Git world, the two atomic masters and the optional wave edge are the shared fixture's. | `QueueFixture` | mcp/tests/test_closeout_queue.py:181-192 |
| The sprint execution graph's single wave edge that still gates the dependent master. | "A supplies B." | mcp/tests/test_closeout_queue.py:264-264 |
| The accumulated code+memory+ledger pair helper this module reuses. | `_accumulate_master_line` | mcp/tests/test_checkpoint_landing_end_to_end.py:132-149 |
| The public checkpoint entry point the landing cases drive. | `_checkpoint` | mcp/tests/test_checkpoint_landing_end_to_end.py:373-383 |
| The lane row the fail-closed manifest requires. | "mcp/tests/test_cross_master_concurrency.py" | mcp/tests/test-evidence-lanes.toml:143-143 |

## Cross-Repo References

The code and memory repositories the cases assert against are created inside a temporary directory by
the module's own fixture; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-13T17:52+02:00 — 260831-LOCR-L36 curator reconciliation against the changed candidate.
  Rewrote the case inventory: the checkpoint-based "completion" case is gone and
  `test_master_a_resumes_reconciles_and_completes_after_master_b_landed` now completes through
  ordinary public closeout + final integration (asserting `state == "integrated"`), with the stop
  verified by `_require_pause_left_a_private` and the reconcile run through the public sync path.
  Recorded that `_record_reconciled_pair` is an agent-owned `memory.md` write with **no public tool**
  (the follow-up pass that would have made it public was cancelled). Renamed the fourth case's anchor
  to `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible` and stated
  in its row that the release is deliberately not the pause; replaced the removed
  `_reconcile_master_line_with_source` helper rows with `_reconcile_master_a`,
  `_record_reconciled_pair`, `_land_remaining_master_a_leaf`, `_closeout_and_land_master`,
  `_complete_master_documents`, `_public_sync`, `_require_ledger_maps`,
  `_require_both_ledger_histories`, `_private_master_a_facts`, `_require_pause_left_a_private`,
  `_close_out_and_land_leaf` and `_land_leaf_contract`. Rebound all nine case ranges and the
  `_checkpoint_with_candidate` range to the moved definitions, and recorded the pause/publication/
  release distinction in the invariants. Verification metadata remains closeout-owned; no execution
  or acceptance claim.

- 2026-09-13T15:00:56+02:00 — Documented the new ninth case `test_a_graph_less_sprint_serializes_nothing_between_its_atomic_masters` (line 483): `executionGraph=None` resolves to mode `atomic-sequential`, both commanded masters stay in `mode.masters`, `mode.facts` is exactly the new single-string tuple ("executionGraph absent: atomic-sequential default — every commanded master executes atomically and no dependency is declared, so nothing serializes the masters"), both selections observe `active` on their own master with an empty `waiting` tuple, and the stale-graph seam still refuses with `task-execution-topology-migration-required` and `nothing serializes the masters` in its detail. Stated the developer ruling in the invariants (nothing serializes a graph-less sprint; `atomic-sequential` describes sprint SHAPE, not a serialization mechanism) and removed the stale `deferred-no-graph-default` reference. Rebound every stale case range to the moved definitions (all eight existing cases had shifted) and the two helper rows the citation findings reported reopened: `_checkpoint_with_candidate` is now `554-572` (the construct is a real top-level def in this revision, not absent) and `_reconcile_master_line_with_source` is now `575-605`; `_close_out_and_land_leaf` moved to `214-283`. Added the graph-less reference row. Verification metadata remains closeout-owned; no execution or acceptance claim.

- 2026-09-13T14:20:09+02:00 — Created by the 260831-LOCR-L36 curator pass as the one-to-one sidecar for the leaf's forcing module. Documents the shared-source-pair premise, all eight cases (both masters stay ready, per-master privacy before landing, B's leaf landing while A is unfinished, A's pause publishing nothing, the conflicting and stale publication refusals, A's reconcile-and-complete, the unchanged explicit checkpoint route, and the surviving sprint-graph wave gate), the fixture composition, the integration-lane row, and the invariant that only the sprint execution graph still holds a dependent master. Verification metadata mirrors the sibling cards' current pair base commit and remains closeout-owned; no acceptance claim.
