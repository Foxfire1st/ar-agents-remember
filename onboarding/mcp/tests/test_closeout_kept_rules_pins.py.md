# mcp/tests/test_closeout_kept_rules_pins.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_kept_rules_pins.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d` |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Named pins for the closeout rules that survive the door/operation/journal cut. With that plane gone
these rules *are* closeout, so each case names the rule it pins: **R1** the trifecta (code, memory
and ledger, all three, always), **R2** a valid nonblank shaped commit message on each enabled leg,
**R3** correct ancestry before closeout passes, and **R4** ref movement read as live Git ancestry
rather than as a durable record.

R2 is enforced as a side effect of `normalize_closeout_input` / `resolve_closeout_plan` rather than by
a standalone guard, so the R2 cases pin that side effect at the boundary where it happens.

## Code Commentary

### Logic

Two fixture builders keep the cases about one fact each. `_contract(*, kind="leaf",
memory_mode="external")` cit:([`_contract`], mcp/tests/test_closeout_kept_rules_pins.py:40-58) is the
minimal leaf; `_enabled_plan(*, kind="leaf", memory_mode="external")`
cit:([`_enabled_plan`], mcp/tests/test_closeout_kept_rules_pins.py:61-70) resolves all three legs
`enabled`. The Git half has its own pair: `_git_repo(tmp_path)`
cit:([`_git_repo`], mcp/tests/test_closeout_kept_rules_pins.py:190-203) creates a real repository with
`main`, `ar/task-one` and a candidate commit and returns `(git, repo, base, candidate)`, and
`_git_contract(repo, **overrides)` cit:([`_git_contract`], mcp/tests/test_closeout_kept_rules_pins.py:206-214)
replaces those facts onto the base contract.

**R2 — every enabled leg carries a nonblank shaped message.**

- `test_r2_each_enabled_leg_requires_a_nonblank_commit_message` cit:(["test_r2_each_enabled_leg_requires_a_nonblank_commit_message"], mcp/tests/test_closeout_kept_rules_pins.py:75-75)
  — parametrized over each leg and over `None` / `""` / `"   "` / `"\n\t "`; whitespace-only counts
  as absent because the value is stripped first, and the refusal reports *all* enabled legs still
  lacking intent so supplying one leg cannot mask another.
- `test_r2_all_three_blank_legs_refuse_together` cit:(["test_r2_all_three_blank_legs_refuse_together"], mcp/tests/test_closeout_kept_rules_pins.py:100-100)
  — the empty call refuses on all three legs at once.
- `test_r2_supplied_messages_are_shape_normalized_and_carried_on_every_leg` cit:(["test_r2_supplied_messages_are_shape_normalized_and_carried_on_every_leg"], mcp/tests/test_closeout_kept_rules_pins.py:118-118)
  — supplied messages come back shape-normalized and present on every leg.

**R1 — the trifecta is all-or-nothing.**
`test_r1_the_trifecta_is_required_as_a_whole_never_partially` cit:(["test_r1_the_trifecta_is_required_as_a_whole_never_partially"], mcp/tests/test_closeout_kept_rules_pins.py:150-150)
supplies two of three enabled legs, asserts the refusal names exactly the missing leg
(`("ledger", "enabled-ledger-message-required")`), and asserts the all-three call resolves every leg
`enabled`. No path silently drops an enabled leg.

**R3 — correct ancestry, including the head a checkpoint landed.**

- `test_r3_closeout_ancestry_passes_when_the_source_is_still_at_the_recorded_base` cit:(["test_r3_closeout_ancestry_passes_when_the_source_is_still_at_the_recorded_base"], mcp/tests/test_closeout_kept_rules_pins.py:217-217)
  — source at base, candidate ahead: `_validate_closeout_source_heads` does not raise.
- `test_r3_closeout_accepts_the_source_head_a_checkpoint_landed` cit:(["test_r3_closeout_accepts_the_source_head_a_checkpoint_landed"], mcp/tests/test_closeout_kept_rules_pins.py:228-228)
  — 260831-LOCR-L30: the source branch is merged forward (a checkpoint's own move) and the contract
  records that merge commit as `integrated_code_commit` with `integration_status="checkpointed"`; the
  validator accepts it. Before the widening this case failed, and it failed with the checkpoint's own
  landed commit named as foreign movement. `test_r3_closeout_refuses_when_the_source_branch_moved`
  cit:(["test_r3_closeout_refuses_when_the_source_branch_moved"], mcp/tests/test_closeout_kept_rules_pins.py:251-251)
  is the companion that keeps the refusal real: a source that moved somewhere else still raises
  `code source branch moved`.
- `test_r4_integration_replay_requirement_is_git_ancestry_not_a_record` cit:(["def test_r4_integration_replay_requirement_is_git_ancestry_not_a_record("], mcp/tests/test_closeout_kept_rules_pins.py:264-264)
  — the replay requirement is an `is_ancestor` read of the live source tip, not a door, claim or
  operation record.
- `test_r4_no_crash_recovery_path_exists_after_a_torn_ref_move` cit:(["test_r4_no_crash_recovery_path_exists_after_a_torn_ref_move"], mcp/tests/test_closeout_kept_rules_pins.py:286-286)
  — mid-crash integration-ref recovery was removed as a capability and must not reappear: the
  recovery entry points do not exist on `integration_ref_transaction`, and re-running
  `worktree_integrate` is the operator-visible behaviour.

### Conventions

Plain module-level `pytest` functions with `pytest.raises(...)` assertions rather than a `unittest`
class. The R2/R1 cases are fully hermetic; the R3/R4 cases build a real repository through the
shared `test_worktree_support` helpers (`git`, `init_repo`) and use `git` identity from that support
module rather than repository or global Git configuration.

### Invariants And Boundaries

- **The rule is the name.** Each case is named for the rule it pins (`R1`/`R2`/`R3`/`R4`), so deleting
  a rule's coverage is visible in a diff rather than implied by a count.
- **R2 is pinned where it happens.** The messages are validated inside `normalize_closeout_input`, so
  the cases assert the refusal's `invalid_fields` shape instead of re-testing a guard that does not
  exist.
- **The Git facts are pinned against a real repository.** R3 and R4 are ancestry questions; a mocked
  `is_ancestor` would make both cases vacuous, so the fixture creates the commits.
- **The checkpoint case must keep a refusal beside it.** Accepting a checkpoint's landed head is only
  correct because a source that moved elsewhere is still refused; keep the two cases together.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own closeout rules, so the retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ancestry validator the R3 cases pin, including the expected-head set. | `_validate_closeout_source_heads`; `_landed_source_heads` | mcp/src/agents_remember/worktrees/modules/closeout.py:145-159; mcp/src/agents_remember/worktrees/modules/closeout.py:295-322 |
| The widened condition that admits a checkpoint's recorded head. | "contract.integration_status in {\"completed\", \"checkpointed\"} and integrated" | mcp/src/agents_remember/worktrees/modules/closeout.py:157-157 |
| The replay requirement the R4 case pins. | "def _integration_replay_requirements(contract: WorktreeContract) -> IntegrationSources:" | mcp/src/agents_remember/worktrees/modules/integrate.py:279-279 |
| The removed recovery entry points the last case proves absent. | "recover_integration_ref"; "refresh_recovered_checkout" | mcp/tests/test_closeout_kept_rules_pins.py:299-300 |
| The closed-input normalizer R1/R2 are pinned through. | `normalize_closeout_input` | mcp/src/agents_remember/worktrees/closeout_input.py:123-177 |

## Cross-Repo References

These are in-process assertions over constructed contracts and a temporary repository; no sibling
repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 2 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "def _integration_replay_requirements(contract: WorktreeContract) -> IntegrationSources:" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:280-280. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "contract.integration_status in {\"completed\", \"checkpointed\"} and integrated" repointed to mcp/src/agents_remember/worktrees/modules/closeout.py:157-157. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:57:35+00:00: Generated citation repair: `_integration_replay_requirements` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:255-275. No content impact: mechanical anchor-range projection bound to citation source snapshot dce71f6378174bd8feac846f76d402a9e99ea632224e7425ead23ceab817985f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T04:10+02:00 — Created by the 260831-LOCR-L30 follow-up curator pass. Documents the R1-R4
  rule pins, the two hermetic / two real-repository fixture split, and the new
  `test_r3_closeout_accepts_the_source_head_a_checkpoint_landed` case with its
  `test_r3_closeout_refuses_when_the_source_branch_moved` companion. Verification metadata is pinned
  to the leaf base commit and remains closeout-owned.
