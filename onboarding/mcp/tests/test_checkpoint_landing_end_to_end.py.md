# mcp/tests/test_checkpoint_landing_end_to_end.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkpoint_landing_end_to_end.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
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

`CheckpointPausesAnUnfinishedMasterTests` cit:([`CheckpointPausesAnUnfinishedMasterTests`], mcp/tests/test_checkpoint_landing_end_to_end.py:76-865) builds one real temporary Git world per case from
`test_closeout_queue.QueueFixture` (`atomic_b=True`, `memory_mode="external"`), then takes the
**series** contract from the master's canonical sibling and its leaf enclosure from the fixture's
contract map. `_unclosed_contract()` asserts the deadlock's own starting state and never fabricates
it: `closeout_status == "not-started"`, `approved_for_commit is False`, empty code and ledger cells,
`integration_status == "not-started"`.

The helpers exist so that no case can cheat the property under test:

- `checkpoint(fixture, series, *, dry_run)` cit:(["def checkpoint("], mcp/tests/checkpoint_landing_test_support.py:345-353) calls
  `worktree_tools.worktree_checkpoint_landing_tool` — the registered public entry point — rather than
  `checkpoint_landing_result` or any inner helper. The module docstring states this as a
  prohibition, not a preference.
- `_accumulate_master_line` now lives in the shared support module as `accumulate_master_line`
  cit:(["def accumulate_master_line("], mcp/tests/checkpoint_landing_test_support.py:104-120) and authors a real code+memory-content+ledger triple on the master's own
  work branches using the repository's own ledger helpers, which is the state an unfinished master
  landed at a checkpoint is
  actually in and the mapping the landing re-proves.
- `branch_checkout` checks out a branch into a disposable worktree so a commit can be authored
  directly on a work branch a series contract has no live worktree for; it moved to the same shared
  support module.
- `_close_out_leaf` is the shared support module's `close_out_leaf`
  cit:(["def close_out_leaf("], mcp/tests/checkpoint_landing_test_support.py:66-101), and it records a leaf closeout **from real commits** in the leaf's own two worktrees, because the
  ordinary integrate route's entry gate requires a closed-out contract and the ledger-divergence
  cases need a live leaf. `hand_edit_ledger_in_place` then commits a hand-edited table where a hand
  edit really reaches a leaf (its own memory worktree) and moves the recorded ledger cell to it.

Twenty cases in the one class, plus the two `setUp`/`tearDown` helpers and `_unclosed_contract`:

| Case | What it pins |
| --- | --- |
| `test_an_unfinished_master_checkpoints_its_own_refs_end_to_end` (`:104-161`) | the preview reports `closeoutRequired: False`, `approvalRequired: True`, `ledgerMappingVerified: True` and the **live** code/ledger candidates, and moves nothing; the apply moves both destination refs to exactly those captured commits, records `checkpointed` with the captured cells, leaves `closeout_status` `not-started` and `cleanup` untouched, keeps the code worktree, the contract and the enclosure, and lands a ledger that really maps code to memory content. |
| `test_a_master_line_that_unioned_its_source_still_checkpoints` (`:163-214`) | the union-merged master's own mapping is captured and landed. |
| `test_a_unioned_master_line_still_refuses_a_content_difference` (`:216-280`) | **changed by 260913-LCA-L11.** The file-preservation rule is gone, so this case now measures what is left: only the row the world contradicts (a memory cell that exists nowhere) refuses, at both surfaces, naming the row; the reorderings **land**, which the case asserts directly beneath the refusal because a case that only asserted the refusal would read as if the file rule were still in force. The `dropped` and `duplicated` corruptions it used to iterate are deleted, with a comment saying why. |
| `test_retry_is_idempotent_and_continued_work_checkpoints_again` (`:282-319`) | a second apply re-captures the same refs and converges (a crash between the ref move and the contract write must converge on retry); after another accumulated pair the refs advance again, so the route is a publication and not a one-shot terminal move — and the new ledger still carries the earlier mapping. |
| `test_the_checkpoint_is_the_only_route_that_admits_an_unclosed_master` (`:321-344`) | the ordinary series `integrate_result` still refuses an unclosed master with `integration requires closeout.status completed`, before anything moves. |
| `test_the_closeout_preview_refuses_what_the_closeout_apply_refuses` (`:346-377`) | **instance 1**: both `worktree_closeout_preview_tool` and `worktree_closeout_apply_tool` raise `atomic-series-closeout-master-incomplete` for the same partial master, with the exact completion facts and no ref movement. |
| `test_a_leaf_closeout_preview_is_untouched_by_the_series_completion_gate` (`:379-394`) | blast radius: a leaf closeout preview still plans `would-closeout` with `commit_approval_required`, because the shared gate returns immediately for a leaf. |
| `test_the_ordinary_leaf_route_refuses_a_divergent_ledger_at_preview_and_apply` (`:396-441`) | **instance 5**: the ordinary leaf route refuses a hand-edited ledger at `dry_run=True` **and** `dry_run=False`, and neither surface moves a ref or rewrites the contract. |
| `test_a_reversed_repeated_code_mapping_now_lands_and_the_hazard_is_recorded` (`:443-496`) | **renamed and inverted by 260913-LCA-L11**, and the leaf's most important negative knowledge. Reversing a superseding pair (two normal rows for one code commit) used to be refused; it now **lands**, because order is a property of the tracked table and the table is derived state. Both rows are true, so no surviving rule refuses it. The case asserts the projection is a pure reordering (`added_rows`/`removed_rows` empty, header unchanged), that the checkpoint reports `checkpointed`, and that both rows survive the landing — and its docstring points at the L11 record for the hazard this acceptance carries. |
| `test_an_untrue_historical_row_below_a_current_one_is_refused` (`:498-554`) | a table may not carry a row the world contradicts even where no lookup reaches it — the mapping clause alone cannot catch it, which is why row truth is its own rule. |
| `test_a_rebuilt_table_still_checkpoints_and_an_untrue_row_still_refuses` (`:556-596`) | **renamed by 260913-LCA-L11.** The retry converges (the shape the old early-return shortcut existed to serve) and a fabricated row still refuses — the replacement rule must not be weaker where it counts. |
| `test_the_landing_does_not_pose_as_a_pause` (`:598-623`) | the checkpoint publication and the stop-only pause stay separate operations. |
| `test_the_leaf_route_lands_the_ledger_the_checkpoint_accepts` (`:625-689`) | **renamed and inverted by 260913-LCA-L11.** The interleaved projection a LEAF used to refuse while a checkpoint accepted it now lands on both routes — the parity the ruling restores — and the case asserts the refs **really moved**, which is the difference between a relaxed rule and a rule that stopped running. |
| `test_a_leaf_that_has_not_closed_out_is_still_refused_by_integrate` (`:691-706`) | the leaf arm of the same entry gate: `validate_integrate_contract` is untouched for the ordinary routes. |
| `test_the_open_master_refusal_names_the_route_that_can_land_it` (`:708-741`) | the refusal routes the operator to the checkpoint publication. |
| `test_a_completed_master_is_still_refused_by_the_checkpoint` (`:743-754`) | the surviving downgrade guard, through the public operation, at preview **and** apply: `atomic-series-checkpoint-master-complete`. |
| `test_a_candidate_whose_ledger_does_not_map_the_code_ref_is_refused` (`:756-770`) | the capture's own proof: a code branch advanced with no mapping row for its new tip is refused instead of captured, and nothing moves. |
| `test_a_hand_edited_master_ledger_is_refused_by_the_preview_and_the_apply` (`:772-805`) | **instance 4**, re-pointed by 260913-LCA-L11: an unfinished master landed at a checkpoint is exactly where someone might hand-edit `memory.md`, and what refuses now is the **row-truth** rule with its new message, at both surfaces, with the fabrication deliberately kept so the refusal is attributed to that rule rather than to an earlier gate. |
| `test_a_ref_race_names_the_checkpoint_as_the_tool_to_rerun` (`:807-833`) | **instance 3**: with `_compare_and_swap_ref` patched to lose, the `integration-ref-race` payload names `worktree_checkpoint_landing` — the tool that attempted the move — with `nextArgs` the contract path, and no ref or cell moved. |
| `test_checkpoint_landing_requires_explicit_developer_approval` (`:847-865`) | `approved=False` on a non-dry-run raises "explicit developer approval": the closeout exemption was not traded for the approval channel. |

### Conventions

The module is a `unittest` class in the `mcp/tests` convention, one real temporary world per case
with `TemporaryDirectory` cleanup in `tearDown`. It is registered in the **integration** lane of
`mcp/tests/test-evidence-lanes.toml` (row 134) — the manifest is fail-closed, so an unregistered
tracked module is a hard load failure rather than a silent gap — and declares two evidence-lifecycle
consumer edges: `closeout_input_test_support.py` (its consumer row is `:304`) and
`curator_coherence_test_support.py` (its consumer row is `:384`), both reached transitively through
`QueueFixture`.

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
- **A case that now ACCEPTS a table says so out loud (260913-LCA-L11).** Three cases in this module
  changed direction: a reordered source region, a reversed superseding pair, and the interleaved
  projection on the leaf route all **land** now. Each asserts the acceptance (and, for the leaf case,
  that the destination refs really moved) rather than dropping the scenario, because a silently
  deleted case would hide the change and a case that only asserted the surviving refusal would read
  as if the file rule were still in force. The hazard the reversal case carries — nothing at the
  landing reports an older row reordered above a newer one for the same code commit — is recorded on
  the transaction card and in that case's docstring, as a gap pending a decision.
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
| The public checkpoint entry point this module drives instead of an inner helper. | `worktree_checkpoint_landing_tool` | mcp/src/agents_remember/application/worktree_tools.py:427-467 |
| The one eligibility decision the preview and the apply both read, and the captured candidate it revalidates. | "class CheckpointLanding:"; "def checkpoint_landing_eligibility(contract: WorktreeContract) -> CheckpointLanding:"; "class SeriesCheckpointRefs:"; "def capture_series_checkpoint_refs(contract: WorktreeContract) -> SeriesCheckpointRefs:" | mcp/src/agents_remember/worktrees/modules/integrate.py:389-423; mcp/src/agents_remember/worktrees/modules/integrate.py:424-471; mcp/src/agents_remember/worktrees/series_closeout.py:99-110; mcp/src/agents_remember/worktrees/series_closeout.py:111-143 |
| The shared landing proof whose preview-side evaluation instances 4 and 5 depend on. Since 260913-LCA-L11 it trades no ledger-history form between the surfaces, so the two agree by construction. | `_require_ledger_projection`; `_route_commits` | mcp/src/agents_remember/worktrees/modules/integrate.py:484-507; mcp/src/agents_remember/worktrees/modules/integrate.py:510-521 |
| The required operation name that makes instance 3's `nextTool` the checkpoint. | `_publish_integration_edge` | mcp/src/agents_remember/worktrees/modules/integrate.py:847-920 |
| The closeout gate the preview and the apply now both read (instance 1) and its leaf exemption. | "def require_closeout_publication_authority(contract: WorktreeContract) -> None:"; "def closeout_preview_payload(contract, args: WorktreeArgs) -> dict[str, object]:" | mcp/src/agents_remember/worktrees/series_closeout.py:39-65; mcp/src/agents_remember/worktrees/modules/closeout.py:235-294 |
| **What a checkpoint's ledger owes since 260913-LCA-L11:** the landed pair is mapped, every row of the landed table is true against the two repositories, the landed memory content descends from the exact memory source while the source is still behind the landing, and the header names its own first row. `_require_preserved_ledger_history` and its projection proof are **deleted**; `LandingAdmission` now carries only the captured candidate. | `require_integrated_ledger_mapping`; `_require_true_rows`; `_integrated_ledger`; `LandingAdmission` | mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:245-271; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:274-359; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:362-395; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:88-98 |
| The lane row the fail-closed manifest requires. | "mcp/tests/test_checkpoint_landing_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:134-134 |
| The two shared-support consumer edges this module adds to the lifecycle catalog, in both artifact blocks. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:282-341; mcp/tests/evidence-lifecycle.toml:362-421 |

## Cross-Repo References

These are contract, ref and ledger assertions against repositories created in a temporary directory
by the module's own fixture; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Recorded Flake

An `UNREPRODUCED FLAKE` comment dated 2026-09-13 (leaf 260831-LOCR-L34) sits above
`test_checkpoint_landing_requires_explicit_developer_approval`
cit:(["UNREPRODUCED FLAKE, RECORDED 2026-09-13"], mcp/tests/test_checkpoint_landing_end_to_end.py:835-835).
It records that the case was reported FAILED **once** during a mutation run that deleted the shared
preflight ledger proof while checking that the mutation fails exactly the two ledger-divergence cases.
The flake was seen **only on that mutated build, never on the real tree**; the case passes in
isolation under the same mutation, did not reproduce in eight subsequent identical replays of the
mutated build or in three clean-tree runs, and the failure text was not captured. It is recorded
rather than dropped so the next person who sees it does not start from zero — if it recurs, capture
the assertion text and treat it as a real flake in this case rather than in the closeout/landing code.

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the shared-support
  extraction moved the whole class, so every one of the twenty case ranges in the table was
  pre-extraction numbering. Re-derived all twenty against the frozen file (`:104-161` … `:847-865`),
  repointed the checkpoint helper to the support module's `checkpoint` (`:345-353`), corrected the
  lane row to 134 and this module's consumer rows to `:304` / `:384` inside the blocks at `:282-341`
  / `:362-421`. The case prose, the L11 removals and the flakiness note were re-read and stand.
  Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/tests/test_checkpoint_landing_end_to_end.py` carries local unstaged changes not represented
  in HEAD. Re-read the card against the frozen on-disk source and re-checked its claims and cited
  ranges: nothing this card asserts is falsified by the change, so no wording changed. Verification
  metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (frozen-tree re-read): the code worktree is frozen
  and these helpers live in the shared support module now, not in this one. Corrected the paragraphs
  to the constructs that exist: `accumulate_master_line`
  (checkpoint_landing_test_support.py:104-120), `branch_checkout`, and `close_out_leaf`
  (checkpoint_landing_test_support.py:66-101), and named `hand_edit_ledger_in_place` with the name
  it actually carries. The substance of each claim holds — the triple is still authored with the
  repository's own ledger helpers, and the closeout still records real commits from the leaf's two
  worktrees — so only the ownership and the anchors changed. Verification metadata remains
  closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 4 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T11:58+02:00 — 260913-LCA-L11 curator (uncommitted change set on `ar/260913-lca-l11-ar`,
  base `4214d7a1`): this module is the leaf's behavioural boundary proof and six of its cases were
  rewritten, so the card was re-derived against the current source. Corrected the class extent
  (`268-656` → `412-1211`); replaced the twelve-case L34 table with the current twenty-case inventory
  and every case's real range; and marked what the leaf did to each case it touched — two renamed and
  **inverted** (a reversed superseding pair now lands, which is the hazard case; the interleaved
  projection now lands on the leaf route too, asserted by the destination refs really moving), one
  renamed (the rebuilt table still checkpoints and an untrue row still refuses), one narrowed (only
  the untrue row refuses — the `dropped`/`duplicated` corruptions are deleted with a comment saying
  why, and the reorderings are asserted as landing), and one re-pointed at the row-truth refusal text
  (instance 4 keeps its fabricated row so the refusal is attributed to the new rule rather than to an
  earlier gate). Corrected the two helper ranges that had drifted (`_accumulate_master_line`
  `125-141` → `132-148`, `_close_out_leaf` `87-122` → `94-129`), replaced the reference row that still
  cited `_require_preserved_ledger_history` with the four promises a landing now owes, and re-pointed
  the recorded `UNREPRODUCED FLAKE` comment (`1162` → `1181-1191`). Added the invariant that a case
  which now accepts a table must assert the acceptance instead of disappearing, and recorded the
  reversal hazard as a known gap pending a decision rather than as something prevented. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T18:02+02:00 — 260831-LOCR-L36 terminology: the checkpoint route partially publishes an
  unfinished master, so `_accumulate_master_line`'s state, instance 4's hand-edit scenario, and the
  `_require_preserved_ledger_history` reference row now say "an unfinished master landed at a
  checkpoint" / "a checkpoint's ledger" where they said "a paused master". Wording only; the cases,
  their ranges and the projection proof are unchanged and no verification stamp advanced.
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shifted `modules/integrate.py`: the shared-ledger-proof row was rebound to `integrate.py:498-526` (`_require_ledger_projection`) and `integrate.py:527-539` (`_route_commits`). Claim wording unchanged.
- 2026-09-13T12:29:52+00:00: Generated citation repair: `_checkpoint` repointed to mcp/tests/test_checkpoint_landing_end_to_end.py:373-383. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "UNREPRODUCED FLAKE, RECORDED 2026-09-13" repointed to mcp/tests/test_checkpoint_landing_end_to_end.py:1162-1162. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:10+00:00 — Created by the 260831-LOCR-L34 curator pass. Documents the module as the
  boundary proof for plan/apply parity: the twelve cases and what each pins, the public-operation and
  never-pre-populate prohibitions the module docstring states, the fixture composition
  (`QueueFixture` + `_close_out_leaf` + `_accumulate_master_line` + `_branch_checkout`), the
  integration-lane row and the two evidence-lifecycle consumer edges, and the recorded
  `UNREPRODUCED FLAKE` note with its conditions and its "not on the real tree" scope. Verification
  metadata is pinned to the leaf base commit and remains closeout-owned; no acceptance claim.
