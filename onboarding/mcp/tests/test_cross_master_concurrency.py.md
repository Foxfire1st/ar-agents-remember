# mcp/tests/test_cross_master_concurrency.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_cross_master_concurrency.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Verify independent atomic masters sharing one protected source pair, private work, conflicting publication refusal, and ordinary completion after sibling reconciliation.

## Code Commentary

### Logic

QueueFixture builds two atomic masters with the same code/memory source branches and distinct work branches. The nine scenarios verify independent activation records/readiness, A-only private content, B leaf landing while A remains unfinished, activation release without publication, stale/non-fast-forward publication refusal, explicit checkpoint availability, genuine graph dependencies, and graph-less concurrency.

The full completion scenario lands A's first leaf and completes B through ordinary closeout/integration. A's stopped interval is represented by before/after private-state snapshots; this is not execution coverage of the public pause tool. A then uses the public sync, starts its remaining leaf, and completes through ordinary closeout/integration without a checkpoint substitute.

Leaf helpers author code plus one attributed memory commit and refresh the cache outside Git. Sync reconciles real content; the former cache-union and ledger-only reconciled-pair write are removed. The final assertions prove both masters' code/memory ancestry and read committed attribution through derive_memory_ledger. No cached row order or mapping for an un-attributed merge commit is required.

### Conventions

Scenarios compose the shared queue, checkpoint, and closeout fixtures under a declared test process. Real fixture repositories establish local operation behavior, not a live orchestration run. Release, stopped-work snapshots, checkpoint publication, and final completion stay separate claims.

### Invariants And Boundaries

- A sibling selection, release, or landing cannot replace another master's activation record.
- Unpublished work remains private and a stale publication cannot overwrite a sibling.
- A reconciled master finishes through ordinary closeout and integration.
- Both masters' real code and memory histories survive; cache bytes are not retention proof.
- Only the authored dependency graph creates predecessor waiting; graph absence does not serialize independent masters.

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
| Independent activation, private content, and sibling leaf landing. | `test_releasing_master_a_activation_publishes_nothing_and_leaves_master_b_eligible` | mcp/tests/test_cross_master_concurrency.py:409-456 |
| Release and conflicting publication preserve sibling state. | `test_a_conflicting_publication_cannot_overwrite_master_b` | mcp/tests/test_cross_master_concurrency.py:473-507 |
| Ordinary resume/reconciliation/completion preserves actual histories. | "def test_master_a_resumes_reconciles_and_completes_after_master_b_landed" | mcp/tests/test_cross_master_concurrency.py:509-568 |
| The stopped interval is represented by snapshots, not a pause-tool call. | "def _private_master_a_facts"; "def _require_pause_left_a_private" | mcp/tests/test_cross_master_concurrency.py:358-389; mcp/tests/test_cross_master_concurrency.py:570-586 |
| Checkpoint and authored/absent dependency behavior remain distinct. | `test_explicit_checkpoint_landing_remains_available_when_requested` | mcp/tests/test_cross_master_concurrency.py:685-718 |
| Fixture commits are two actual outputs with Git-owned attribution. | "def _land_leaf_contract" | mcp/tests/test_cross_master_concurrency.py:224-240 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Migrated leaf and master scenarios to actual code/memory outputs; removed ledger-only reconciliation and cached-row reads, and strengthened retained-history assertions with direct Git ancestry. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): corrected the Conventions
  paragraph that still named `_accumulate_master_line`, `_checkpoint`, `_memory_repository` and
  `_rev` as coming from `test_checkpoint_landing_end_to_end`. They are `accumulate_master_line`,
  `checkpoint`, `memory_repository` and `rev` in the shared `checkpoint_landing_test_support`, as
  this card's own reference rows already say; the two halves of the card contradicted each other.
  Every case range was re-read and still holds. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (frozen-tree re-read): the code worktree is frozen
  and these helpers live in the shared support module now, not in this one. Corrected the paragraphs
  to the constructs that exist: `accumulate_master_line`
  (checkpoint_landing_test_support.py:104-120), `branch_checkout`, and `close_out_leaf`
  (checkpoint_landing_test_support.py:66-101), and named `hand_edit_ledger_in_place` with the name
  it actually carries. The substance of each claim holds — the triple is still authored with the
  repository's own ledger helpers, and the closeout still records real commits from the leaf's two
  worktrees — so only the ownership and the anchors changed. Verification metadata remains
  closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 3
  claim(s) whose anchor no longer sat in its cited range and normalised 15 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
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
