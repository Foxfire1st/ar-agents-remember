# mcp/tests/test_automatic_post_integration_cleanup.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_automatic_post_integration_cleanup.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| lastVerifiedCommitDate | 2026-09-18T18:30:35+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pins **which procedure reclaims a landed leaf**, and proves the whole path end to end over real Git
repositories: a landing retires nothing and routes to `lifecycle_finalize_task`, finalization reclaims
and completes the task edge, a cleanup that cannot complete refuses before that edge closes, and a
refused integration leaves every target exactly where it was.

The developer ruling is unchanged — a completed leaf is reclaimed automatically rather than by a
prompt. What this lane now pins is ownership, because the old ownership made the terminal edge
unreachable: integration reclaimed inside itself, so the enclosure was already at
`cleanup: completed` when the one guard that routes a landed leaf onward
(`next_step.py::_gate_after`, keyed on that exact cell) looked at it. A real landing therefore
reported `done` while the leaf's task document stayed `planning` and its master row stayed
`inProgress`. The module name is historical: reclamation is no longer a "post integration" step,
finalization owns it.

## Code Commentary

### Logic

The fixture chain builds a genuinely landed external-memory leaf:
`bound_worktree_services` cit:([`bound_worktree_services`], mcp/tests/test_automatic_post_integration_cleanup.py:74-83)
binds the default service bundle, `_landed_leaf` cit:([`_landed_leaf`], mcp/tests/test_automatic_post_integration_cleanup.py:85-88)
publishes a real closeout through the shared authority fixture, and `_integrate_apply`
cit:([`_integrate_apply`], mcp/tests/test_automatic_post_integration_cleanup.py:120-127)
drives the public integrate tool with `auto_land_on_integration=True`. Three small readers keep the
assertions about the task edge honest:
`_leaf_document` cit:([`_leaf_document`], mcp/tests/test_automatic_post_integration_cleanup.py:103-109)
resolves the contractually bound leaf document through `resolve_terminal_leaf_doc` and reads it,
`_master_row_status` cit:([`_master_row_status`], mcp/tests/test_automatic_post_integration_cleanup.py:111-118)
finds the one master row naming this leaf, and
`_local_branch_exists` / `_work_branch_sides`
cit:([`_local_branch_exists`, `_work_branch_sides`], mcp/tests/test_automatic_post_integration_cleanup.py:90-101)
drive real Git.

Four cases:

- `test_a_landed_leaf_is_reclaimed_by_finalization_and_never_by_integration` cit:(["test_a_landed_leaf_is_reclaimed_by_finalization_and_never_by_integration"], mcp/tests/test_automatic_post_integration_cleanup.py:129-129)
  — the load-bearing case. The landing's `cleanup` key is the untouched contract cell (`"pending"`),
  `"removed"`/`"notRemoved"` are absent from the payload, the summary promises reclamation at the task
  edge, and the projection names the terminal move (`phase: cleanup-pending`, `nextOperation:
  finalize`, `nextTool: lifecycle_finalize_task`, `nextRequiredArgs == ["contract_path"]`). It then
  proves **nothing was retired** — every worktree, branch, the reports directory and the enclosure
  root are still present, and the leaf document is still not `Completed` — and only then calls
  `lifecycle_finalize_task_tool`, which must produce the shaped operator report
  (`"Automatic cleanup removed 2 worktrees, 2 local branches, 1 reports directory, 1 enclosure root;
  nothing was left in place."`) with `notRemoved` empty, and must leave both the leaf document and the
  master row `Completed`.
- `test_a_refused_cleanup_blocks_finalization_and_leaves_the_task_edge_open` cit:(["test_a_refused_cleanup_blocks_finalization_and_leaves_the_task_edge_open"], mcp/tests/test_automatic_post_integration_cleanup.py:221-221)
  — the other half of the ownership split. `finalize.cleanup_result` is patched to raise
  `RuntimeError`, and the assertion is that finalization reports `cleanup-blocked` with cleanup's own
  payload passed through whole (`{"state": "blocked", "summary": "refused"}`) rather than re-shaped,
  that the leaf document and the master row stay open, and that every reclamation target is still on
  disk. Without this case the split could "succeed" by closing a task edge over work that was never
  reclaimed.
- `test_a_dry_run_finalization_reports_the_cleanup_plan_and_shapes_nothing` cit:(["test_a_dry_run_finalization_reports_the_cleanup_plan_and_shapes_nothing"], mcp/tests/test_automatic_post_integration_cleanup.py:260-260)
  — pins the report shaper's dry-run gate. A preview's payload lists what cleanup *would* remove, so
  shaping it with "removed … nothing was left in place" would assert a reclamation that never
  happened; the case asserts `state: would-finalize` with cleanup's own `would-cleanup` plan, no
  `automatic` key, and nothing retired.
- `test_refused_integration_leaves_every_worktree_and_branch_in_place` cit:(["test_refused_integration_leaves_every_worktree_and_branch_in_place"], mcp/tests/test_automatic_post_integration_cleanup.py:300-300)
  — the pre-existing negative control, extended: the dry run's `cleanup_reminder` now promises only
  the landing, the refused apply produces no reclamation report (`cleanup == "pending"`, no
  `"removed"`), no source ref moved, and the leaf document is not `Completed`.

### Conventions

Plain module-level `pytest` functions with one fixture, and the module is registered in the
`integration` lane of `mcp/tests/test-evidence-lanes.toml` (line 130) because these cases drive real
application tools over real repositories.

**The file name is historical and deliberately not renamed.** This path is declared by name in three
manifests and only one of them is fail-closed:
`mcp/tests/test-evidence-lanes.toml:131` (the lane manifest a consumer refuses to load without),
`mcp/tests/evidence-lifecycle.toml` (nine rows), and
`mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:65`. Renaming the
module would be a cross-manifest change for no behavioural gain, so the docstring records the
historical name and points readers at the real subjects instead:
`finalize::_run_or_verify_cleanup`, which runs reclamation, and
`cleanup_report::cleanup_report`, which shapes the report the first case asserts. Do not "fix" the
name on the strength of the file's contents; `finalize.py` is where the behaviour this lane tests now
lives.

### Invariants And Boundaries

- **A landing must not reclaim.** Asserting only the final state would pass for a route that reclaimed
  early and then reported correctly, so the first case asserts the *intermediate* state — every target
  still present, the leaf document open, `cleanup == "pending"` — before it finalizes.
- **A refusal must never close the task edge.** The second case exists because the ownership split
  turns a cleanup failure from "reported beside a completed landing" into "blocks finalization"; if a
  future change let finalization mark documents `Completed` on a failed cleanup, only these assertions
  would notice.
- **The shaped report is asserted by exact sentence**, because the sentence is what an operator reads
  and the counts in it are the only proof that the inventory was derived rather than synthesized.
- **A preview is never shaped.** The third case is the dry-run gate; a shaper that ran on preview
  payloads would report removals that did not happen.
- **The lane row is not optional metadata.** The manifest is fail-closed, so an unregistered tracked
  module is a hard load failure rather than a silent gap.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own application tools over real Git fixtures, so the retained source is the
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring that records the ownership story and the historical name. | "Reclamation is automatic and unprompted, and finalization is what runs it." | mcp/tests/test_automatic_post_integration_cleanup.py:1-28 |
| The reclamation runner and report-shaping gate these cases exercise through `lifecycle_finalize_task`. | `_run_or_verify_cleanup`; "cleanup_report(contract, result.payload)" | mcp/src/agents_remember/worktrees/modules/finalize.py:277-311; mcp/src/agents_remember/worktrees/modules/finalize.py:310-310 |
| The report shaper whose exact sentence and inventory the first case asserts. | `cleanup_report`; "ALREADY_CLEAN = \"already-clean\"" | mcp/src/agents_remember/worktrees/modules/cleanup_report.py:23-53 |
| The landing route whose no-reclamation the cases assert, including the payload's untouched `cleanup` cell. | `_integrated_result` | mcp/src/agents_remember/worktrees/modules/integrate.py:574-607 |
| The projection that names the finalization move. | `_post_integration_phase` | mcp/src/agents_remember/worktrees/modules/guidance.py:245-328 |
| The terminal operation the first case calls. | `lifecycle_finalize_task_tool` | mcp/src/agents_remember/application/worktree_tools.py:855-886 |
| The fail-closed lane this module must be listed in, and the dependency-classification entry that also names it. | "integration = ["; `AMBIENT_ROLE_RUNNER_PATH`; "mcp/tests/test_automatic_post_integration_cleanup.py" | mcp/tests/test-evidence-lanes.toml:192-192; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:62-70; mcp/tests/test-evidence-lanes.toml:194-194; mcp/tests/test-evidence-lanes.toml:195-195; mcp/tests/test-evidence-lanes.toml:196-196; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:196-196 |
| The fail-closed lane this module must be listed in, and the dependency-classification entry that also names it. | "integration = ["; `AMBIENT_ROLE_RUNNER_PATH` | mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:196-196 |

## Cross-Repo References

These are in-process application-tool assertions against real repositories created in a temporary
directory; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-18T16:13:35+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:196-196. No content impact: mechanical anchor-range projection bound to citation source snapshot e93679ab5a75f0a02b7b5f3d8b80c429fc541ff3ead9181d4e4fbf176c901462; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:195-195. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:194-194. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:192-192. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:170-170. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: `AMBIENT_ROLE_RUNNER_PATH`; "integration = [" repointed to mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:168-168. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 10 generated projection bullet(s) by hand while resolving the memory sync** — `AMBIENT_ROLE_RUNNER_PATH`, `integration = [`, `Path(\`, `)`, `_integrated_result`, `_post_integration_phase`, `lifecycle_finalize_task_tool`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand** — `AMBIENT_ROLE_RUNNER_PATH`, `integration = [`, `Path(\`, `)`, `_integrated_result`, `_post_integration_phase`, `lifecycle_finalize_task_tool`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: ``AMBIENT_ROLE_RUNNER_PATH`; "integration = ["` → `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:162-162`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:160-160` -> `mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:47-47; mcp/tests/test-evidence-lanes.toml:161-161`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T20:42:17+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:574-607. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_post_integration_phase` repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:245-328. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:855-886. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "integration = ["; "Path(\"mcp/tests/test_automatic_post_integration_cleanup.py\")" repointed to mcp/tests/test-evidence-lanes.toml:161-161; mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:65-65. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T17:20:55+00:00: Generated citation repair: `lifecycle_finalize_task_tool` repointed to mcp/src/agents_remember/application/worktree_tools.py:862-893. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43:00+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.

- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T08:49:05+00:00: Generated citation repair: `_integrated_result` repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:598-633. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T17:50:00+00:00 — Created by the 260831-LOCR-L31 curator pass. This module had no card
- 2026-09-12T19:50+02:00 — Created by the 260831-LOCR-L31 curator pass. This module had no card
  before, and its change set is exactly where the leaf's central decision lives, so the record belongs
  beside it: the four cases (landing retires nothing and routes to finalization; finalization reclaims,
  publishes the shaped report and completes the leaf document and master row; a refused cleanup blocks
  finalization and leaves the edge open; a dry run is never shaped), the fixture chain that makes the
  first case a real end-to-end path, and **the historical file name** — this path is declared in three
  manifests (only `mcp/tests/test-evidence-lanes.toml` is fail-closed) and is deliberately not renamed,
  with the docstring pointing at `finalize::_run_or_verify_cleanup` and
  `cleanup_report::cleanup_report` as the real subjects. Verification metadata is pinned to the leaf
  base commit and remains closeout-owned; source documentation only, no acceptance claim.
