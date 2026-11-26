# mcp/tests/test_automatic_post_integration_cleanup.py

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

The test uses default worktree services with a fixture citation-guard override
cit:([`bound_worktree_services`], mcp/tests/test_automatic_post_integration_cleanup.py:80-88).
`_landed_leaf` creates a completed external-memory closeout fixture backed by real Git commits
and seeds a review report
cit:([`_landed_leaf`], mcp/tests/test_automatic_post_integration_cleanup.py:91-98; mcp/tests/integration_branch_authority_test_support.py:119-157).
`_integrate_apply` calls the production application handler with the bound contract,
`strategy="ff-only"`, and `dry_run=False`
cit:([`_integrate_apply`], mcp/tests/test_automatic_post_integration_cleanup.py:131-137).
`_leaf_document` reads the bound leaf and `_master_row_status` reads its unique master row
cit:([`_leaf_document`, `_master_row_status`], mcp/tests/test_automatic_post_integration_cleanup.py:114-128).
The branch readers check actual Git
cit:([`_local_branch_exists`, `_work_branch_sides`], mcp/tests/test_automatic_post_integration_cleanup.py:101-111).

Four cases:

- `test_a_landed_leaf_is_reclaimed_by_finalization_and_never_by_integration` cit:(["test_a_landed_leaf_is_reclaimed_by_finalization_and_never_by_integration"], mcp/tests/test_automatic_post_integration_cleanup.py:140-229)
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
- `test_a_refused_cleanup_blocks_finalization_and_leaves_the_task_edge_open` cit:(["test_a_refused_cleanup_blocks_finalization_and_leaves_the_task_edge_open"], mcp/tests/test_automatic_post_integration_cleanup.py:232-268)
  — the other half of the ownership split. `finalize.cleanup_result` is patched to raise
  `RuntimeError`, and the assertion is that finalization reports `cleanup-blocked` with cleanup's own
  payload passed through whole (`{"state": "blocked", "summary": "refused"}`) rather than re-shaped,
   that the leaf document and master row stay open, and that both worktrees, the group
   and branches remain present.
- `test_a_dry_run_finalization_reports_the_cleanup_plan_and_shapes_nothing` cit:(["test_a_dry_run_finalization_reports_the_cleanup_plan_and_shapes_nothing"], mcp/tests/test_automatic_post_integration_cleanup.py:271-308)
  — pins the report shaper's dry-run gate. A preview's payload lists what cleanup *would* remove, so
  shaping it with "removed … nothing was left in place" would assert a reclamation that never
  happened; the case asserts `state: would-finalize` with cleanup's own `would-cleanup` plan, no
  `automatic` key, and nothing retired.
- `test_refused_integration_leaves_every_worktree_and_branch_in_place` cit:(["test_refused_integration_leaves_every_worktree_and_branch_in_place"], mcp/tests/test_automatic_post_integration_cleanup.py:311-369)
  — the pre-existing negative control, extended: the dry run's `cleanup_reminder` now promises only
  the landing, the refused apply produces no reclamation report (`cleanup == "pending"`, no
  `"removed"`), no source ref moved, and the leaf document is not `Completed`.

### Conventions

Plain module-level `pytest` functions use one fixture. The lane catalog assigns this module
to integration at `mcp/tests/test-evidence-lanes.toml:674`. Its cases drive production
application operations over temporary Git repositories.

The historical filename appears in the lane catalog, twelve lifecycle consumer rows,
and the certification-profile dependency projection at
`mcp/test_support/agents_remember_test_support/code_quality/dependency_ownership.py:67-76`.

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own application tools over real Git fixtures, so the retained source is the
direct evidence.

No external domain claim is required.

### Repo-Internal References

- The module docstring that records the ownership story and the historical name. [1]

> Retained earlier citation wording: - The reclamation runner and report-shaping gate these cases exercise through `lifecycle_finalize_task`. A completed cleanup cell still archives its recorded terminal agents.

> Retained earlier citation wording: - The report shaper whose exact sentence and inventory the first case asserts. [3]

- The landing route whose no-reclamation the cases assert, including the payload's untouched `cleanup` cell. [4]

- The projection that names the finalization move. [5]


- The terminal operation the first case calls. [6]


> Retained earlier citation wording: - The dependency-classification entry that names this module as a consumer of the certification profile. Source caption: `AMBIENT_ROLE_RUNNER_PATH`

### Cross-Repo References

These are in-process application-tool assertions against real repositories created in a temporary
directory; no sibling repository or external system participates.

No meaningful cross-repo references found.


- The reclamation runner and report-shaping gate these cases exercise through `lifecycle_finalize_task`. A completed cleanup cell still archives its recorded terminal agents. [2]


- The report shaper whose exact sentence and inventory the first case asserts.  Anchor: "ALREADY_CLEAN = \"already-clean\"" [3]

- The dependency classifier lists this module among the consumers of the certification profile. [10]
