# mcp/tests/test_checkpoint_landing_end_to_end.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkpoint_landing_end_to_end.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:10+02:00 |
| lastVerifiedCommitHash | `707847206d02e2ff27b11c1f674a510d85f3b972` |
| lastVerifiedCommitDate | 2026-09-13T13:20:21+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Plan/apply parity for the routes 260831-LOCR-L34 repaired, driven over **real temporary Git
repositories** through the **public** operations. The module is the boundary proof for two things
`mcp/tests/test_checkpoint_landing.py` can only pin seam by seam:

1. the checkpoint half — an unfinished atomic master whose `closeout_status` is still `not-started`
   checkpoints end to end, with both destination refs and the ledger verified, the retry idempotent,
   continued work advancing the refs again, and every refusal firing at both surfaces; and
2. the parity half — **a dry run must refuse exactly what its apply refuses** — for the ordinary
   integrate route's ledger projection and for the closeout route's atomic-completion gate, the
   original instance of the whole family.

It exists because the checkpoint route shipped unreachable in both directions and no seam-level test
noticed: every other checkpoint case is a unit proof of one seam, and the defect lived in the
composition of the seams.

## Code Commentary

### Logic

`CheckpointPausesAnUnfinishedMasterTests` cit:([`CheckpointPausesAnUnfinishedMasterTests`], mcp/tests/test_checkpoint_landing_end_to_end.py:268-656) builds one real temporary Git world per case from
`test_closeout_queue.QueueFixture` (`atomic_b=True`, `memory_mode="external"`), then takes the
**series** contract from the master's canonical sibling and its leaf enclosure from the fixture's
contract map. `_unclosed_contract()` asserts the deadlock's own starting state and never fabricates
it: `closeout_status == "not-started"`, `approved_for_commit is False`, empty code and ledger cells,
`integration_status == "not-started"`.

The helpers exist so that no case can cheat the property under test:

- `_checkpoint(fixture, series, *, dry_run)` cit:([`_checkpoint`], mcp/tests/test_checkpoint_landing_end_to_end.py:235-245) calls
  `worktree_tools.worktree_checkpoint_landing_tool` — the registered public entry point — rather than
  `checkpoint_landing_result` or any inner helper. The module docstring states this as a
  prohibition, not a preference.
- `_accumulate_master_line` cit:([`_accumulate_master_line`], mcp/tests/test_checkpoint_landing_end_to_end.py:125-141) authors a real code+memory-content+ledger triple on the master's own
  work branches using the repository's own ledger helpers, which is the state a paused master is
  actually in and the projection the landing re-proves.
- `_branch_checkout` checks out a branch into a disposable worktree so a commit can be authored
  directly on a work branch a series contract has no live worktree for.
- `_close_out_leaf` cit:([`_close_out_leaf`], mcp/tests/test_checkpoint_landing_end_to_end.py:87-122) records a leaf closeout **from real commits** in the leaf's own two worktrees, because the
  ordinary integrate route's entry gate requires a closed-out contract and the ledger-divergence
  cases need a live leaf. `_hand_edit_ledger_in_place` then commits a hand-edited table where a hand
  edit really reaches a leaf (its own memory worktree) and moves the recorded ledger cell to it.

Twelve cases in the one class:

| Case | What it pins |
| --- | --- |
| `test_an_unfinished_master_checkpoints_its_own_refs_end_to_end` (`:296-355`) | the preview reports `closeoutRequired: False`, `approvalRequired: True`, `ledgerMappingVerified: True` and the **live** code/ledger candidates, and moves nothing; the apply moves both destination refs to exactly those captured commits, records `checkpointed` with the captured cells, leaves `closeout_status` `not-started` and `cleanup` untouched, keeps the code worktree, the contract and the enclosure, and lands a ledger that really maps code to memory content. |
| `test_retry_is_idempotent_and_continued_work_checkpoints_again` (`:357-394`) | a second apply re-captures the same refs and converges (a crash between the ref move and the contract write must converge on retry); after another accumulated pair the refs advance again, so the route is a pause and not a one-shot terminal move — and the new ledger still carries the earlier mapping. |
| `test_the_checkpoint_is_the_only_route_that_admits_an_unclosed_master` (`:396-419`) | the ordinary series `integrate_result` still refuses an unclosed master with `integration requires closeout.status completed`, before anything moves. |
| `test_the_closeout_preview_refuses_what_the_closeout_apply_refuses` (`:421-452`) | **instance 1**: both `worktree_closeout_preview_tool` and `worktree_closeout_apply_tool` raise `atomic-series-closeout-master-incomplete` for the same partial master, with the exact completion facts and no ref movement. |
| `test_a_leaf_closeout_preview_is_untouched_by_the_series_completion_gate` (`:454-469`) | blast radius: a leaf closeout preview still plans `would-closeout` with `commit_approval_required`, because the shared gate returns immediately for a leaf. |
| `test_the_ordinary_leaf_route_refuses_a_divergent_ledger_at_preview_and_apply` (`:471-516`) | **instance 5**: the ordinary leaf route refuses a hand-edited ledger at `dry_run=True` **and** `dry_run=False`, with both refusal sentences, and neither surface moves a ref or rewrites the contract. |
| `test_a_leaf_that_has_not_closed_out_is_still_refused_by_integrate` (`:518-532`) | the leaf arm of the same entry gate: `validate_integrate_contract` is untouched for the ordinary routes, so the exemption really is local to the checkpoint preflight. |
| `test_a_completed_master_is_still_refused_by_the_checkpoint` (`:534-545`) | the surviving downgrade guard, through the public operation, at preview **and** apply: `atomic-series-checkpoint-master-complete`. |
| `test_a_candidate_whose_ledger_does_not_map_the_code_ref_is_refused` (`:547-563`) | the capture's own proof: a code branch advanced with no mapping row for its new tip is refused instead of captured, and nothing moves. |
| `test_a_hand_edited_master_ledger_is_refused_by_the_preview_and_the_apply` (`:565-596`) | **instance 4**: a paused master is exactly where someone might hand-edit `memory.md`, so the projection refusal fires at both surfaces, with the row the capture needs deliberately kept so this is genuinely the projection refusal and not an earlier one. |
| `test_a_ref_race_names_the_checkpoint_as_the_tool_to_rerun` (`:598-624`) | **instance 3**: with `_compare_and_swap_ref` patched to lose, the `integration-ref-race` payload names `worktree_checkpoint_landing` — the tool that attempted the move — with `nextArgs` the contract path, and no ref or cell moved. |
| `test_checkpoint_landing_requires_explicit_developer_approval` (`:638-656`) | `approved=False` on a non-dry-run raises "explicit developer approval": the closeout exemption was not traded for the approval channel. |

### Conventions

The module is a `unittest` class in the `mcp/tests` convention, one real temporary world per case
with `TemporaryDirectory` cleanup in `tearDown`. It is registered in the **integration** lane of
`mcp/tests/test-evidence-lanes.toml` (row 132) — the manifest is fail-closed, so an unregistered
tracked module is a hard load failure rather than a silent gap — and declares two evidence-lifecycle
consumer edges: `closeout_input_test_support.py` (row 304) and `curator_coherence_test_support.py`
(row 357), both reached transitively through `QueueFixture`.

`QueueFixture` and the `git` helper come from `test_closeout_queue` and `test_worktree_support`
rather than from a local re-implementation, so this module composes the existing fixture ownership
instead of adding a second one.

### Invariants And Boundaries

- **The public operation is the subject.** A case that calls `checkpoint_landing_result` or
  `publish_series_checkpoint_under_authority` directly would pass while the registered tool stayed
  broken; the module docstring forbids it, and `test_checkpoint_landing_requires_explicit_developer_approval`
  is the one case that clears the `dry_run` flag on the typed call to reach the approval refusal.
- **`closeout_status` is never pre-populated for the checkpoint cases.** The deadlock's prerequisite
  is the point of the route; only the closeout case sets the cell, and only where it has authored the
  real commits that back it, because the closeout route cannot be entered otherwise.
- **Both surfaces are asserted for every ledger refusal.** An apply-only assertion is what let
  instance 1 and instance 4 ship; each divergence case iterates `(True, False)` and names the surface
  in its assertion message.
- **Nothing is asserted about refs after a refusal unless it must not have moved.** Every refusal case
  re-reads both destination refs and the contract, so a refusal that moved something fails here.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo. These assertions concern
this repository's own ref movement, contract cells and ledger projection, so the retained source is
the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public checkpoint entry point this module drives instead of an inner helper. | `worktree_checkpoint_landing_tool` | mcp/src/agents_remember/application/worktree_tools.py:427-469 |
| The one eligibility decision the preview and the apply both read, and the captured candidate it revalidates. | "class CheckpointLanding:"; "def checkpoint_landing_eligibility(contract: WorktreeContract) -> CheckpointLanding:"; "class SeriesCheckpointRefs:"; "def capture_series_checkpoint_refs(contract: WorktreeContract) -> SeriesCheckpointRefs:" | mcp/src/agents_remember/worktrees/modules/integrate.py:371-405; mcp/src/agents_remember/worktrees/modules/integrate.py:406-453; mcp/src/agents_remember/worktrees/series_closeout.py:94-105; mcp/src/agents_remember/worktrees/series_closeout.py:106-138 |
| The shared ledger proof whose preview-side evaluation instances 4 and 5 depend on. | `_require_ledger_projection`; `_route_commits` | mcp/src/agents_remember/worktrees/modules/integrate.py:479-507; mcp/src/agents_remember/worktrees/modules/integrate.py:508-521 |
| The required operation name that makes instance 3's `nextTool` the checkpoint. | `_publish_integration_edge` | mcp/src/agents_remember/worktrees/modules/integrate.py:846-921 |
| The closeout gate the preview and the apply now both read (instance 1) and its leaf exemption. | "def require_closeout_publication_authority(contract: WorktreeContract) -> None:"; "def closeout_preview_payload(contract, args: WorktreeArgs) -> dict[str, object]:" | mcp/src/agents_remember/worktrees/series_closeout.py:34-60; mcp/src/agents_remember/worktrees/modules/closeout.py:235-294 |
| The projection proof a paused master's ledger owes, and the fact that it is the leaf form. | `_require_preserved_ledger_history`; `LandingAdmission` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:344-399; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:92-106 |
| The lane row the fail-closed manifest requires. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:132-132 |
| The two shared-support consumer edges this module adds to the lifecycle catalog, in both artifact blocks. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:283-333; mcp/tests/evidence-lifecycle.toml:336-386 |

## Cross-Repo References

These are contract, ref and ledger assertions against repositories created in a temporary directory
by the module's own fixture; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Recorded Flake

An `UNREPRODUCED FLAKE` comment dated 2026-09-13 (leaf 260831-LOCR-L34) sits above
`test_checkpoint_landing_requires_explicit_developer_approval`
cit:(["UNREPRODUCED FLAKE, RECORDED 2026-09-13"], mcp/tests/test_checkpoint_landing_end_to_end.py:626-637).
It records that the case was reported FAILED **once** during a mutation run that deleted the shared
preflight ledger proof while checking that the mutation fails exactly the two ledger-divergence cases.
The flake was seen **only on that mutated build, never on the real tree**; the case passes in
isolation under the same mutation, did not reproduce in eight subsequent identical replays of the
mutated build or in three clean-tree runs, and the failure text was not captured. It is recorded
rather than dropped so the next person who sees it does not start from zero — if it recurs, capture
the assertion text and treat it as a real flake in this case rather than in the closeout/landing code.

## Update History
- 2026-09-13T09:10+00:00 — Created by the 260831-LOCR-L34 curator pass. Documents the module as the
  boundary proof for plan/apply parity: the twelve cases and what each pins, the public-operation and
  never-pre-populate prohibitions the module docstring states, the fixture composition
  (`QueueFixture` + `_close_out_leaf` + `_accumulate_master_line` + `_branch_checkout`), the
  integration-lane row and the two evidence-lifecycle consumer edges, and the recorded
  `UNREPRODUCED FLAKE` note with its conditions and its "not on the real tree" scope. Verification
  metadata is pinned to the leaf base commit and remains closeout-owned; no acceptance claim.
