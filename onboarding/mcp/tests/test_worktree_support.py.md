# test_worktree_support.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                       |
| path                   | `mcp/tests/test_worktree_support.py` |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated            | 2026-07-07T18:40+02:00|
| lastVerifiedCommitHash | `575a9a44b71910d151c878eda4da4ebf32bef1cb` |
| lastVerifiedCommitDate | 2026-07-07T01:41:35+02:00|

## Purpose

This unittest file validates the first worktree-support helper slice.

## Code Commentary

### Logic

The tests cover memory ledger roundtrip/prepend behavior, branchless canonical ledger output, legacy branch-metadata ledger parsing without branch-metadata blocking, malformed ledger metadata, invalid ledger top-row detection, repo-specific `c-08-ar-coordination-context-resolver` skill `task_root` output without a task name, installed-runtime coordination-root defaults, source-checkout `.env` and `.env.example` ignore behavior, dirty external-memory start blocking, compatible external-memory start reporting, internal memory start reporting, worktree contract roundtrip with wrapper task roots and legacy task-root candidates, direct contract-path status loading, closeout commit-preview with typed MCP next hints, approval-note, onboarding metadata refresh, route overview/index refresh, memory quality gating before memory commits, missing-onboarding blocking behavior, memory-worktree settings during closeout planning, long Windows path changed-file and sidecar detection, internal resolver defaults to `ar-memory` plus `temp`, drift report path placement under `temp_root` including redirection away from durable memory repos, deterministic overview/entity drift checks including entity inventory coverage, `c-09-git-worktree-manager` skill integration fast-forward/replay/conflict behavior, non-fast-forward integration refusal at `_merge_integrated_commits` without advancing the code branch, `c-09-git-worktree-manager` skill cleanup happy path/idempotence/blocking behavior, legacy cross-repo string rejection, v2 code-only inclusion, v2 memory inclusion with matching checkout branches and ledger commit metadata, `c-10-adopt-memory-baseline` skill adoption status/block/adopt behavior, `c-11-memory-carryover-from-branch` skill memory carryover plan/apply behavior including earlier-only-landed same-path commits staying `same-path-changed`/`review-required` rather than exact-landed, and benchmark runner portability coverage for non-string/unsafe manifest path guards, Windows-safe generated tree removal, stale directory symlink cleanup, Windows Codex shim resolution, cached benchmark repository reuse, missing-commit fetch behavior, force-clone behavior, copy-only skill exposure, Codex `PATH` resolution and benchmark-only execution metadata, default-sandbox omission, variant-scoped benchmark provider selection, generated benchmark provider settings with central provider log paths, workspace-local `.codex` benchmark MCP registration, and temp-file provider setup handoff.

**260703-L18 (finding 7 / friction F-R)** adds the missing-ledger-mapping recovery coverage via a
`_unmapped_external_contract` helper (a code base commit the ledger never recorded, real tmp code +
memory repos): `test_missing_mapping_block_advertises_only_consumable_choices` proves the block names
ONLY executable choices (`reconciliation`, `disabled-memory`; `custom` removed) and that passing each
does something other than return the identical block, and
`test_reconciliation_records_the_mapping_and_starts_the_worktree` proves `memory_choice="reconciliation"`
maps the unmapped code base to the ledger's memory content tip, writes + commits a `Ledger sync` in the
memory SOURCE repo (header advance + newest-first row, content tip unchanged), and proceeds to a real
started memory worktree.

`RequireUpdatedSidecarContentTests` covers the four-case closeout content gate:
in a temporary memory Git repo with a committed sidecar,
`require_updated_sidecar_content` raises for an unchanged sidecar, a
metadata-only edit, a history-only edit without the no-impact marker, and a
body edit without a new Update History entry; it passes (returning the attested
source paths) for a history-only edit carrying a `No content impact:` entry,
passes with empty attestations for a body+history update and for a new
untracked sidecar, and is a no-op when the plan has no required sidecars. The
issue #83 additions prove the `memory_verified_commit` baseline: a sidecar
body+history update committed in the memory repo before closeout passes, a
sidecar unchanged since the verified commit still blocks, and a new sidecar
committed after the verified baseline passes like an untracked one.

The issue #83 committed-range coverage drives full closeouts through
`committed_range_external_contract_fixture` (work-branch commits with a
baseline sidecar plus an un-onboarded `raw.txt`): preview reports the bounded
`changed_code_paths`/`changed_code_paths_committed` shapes, the non-blocking
`unonboarded` bucket, and the `stale` body-gate finding for the transported
onboarded path; apply with an updated sidecar stamps metadata to the existing
HEAD without creating a code commit, surfaces `unonboarded_changed_paths`, and
maps the ledger to that HEAD; apply with a stale sidecar still blocks. A second
closeout after `closed_external_contract_fixture` excludes the first closeout's
paths via the contract `code_commit` pointer, a merged-in moved `main` with an
advanced `code_base_commit` is excluded entirely (sync-transport intersection),
`test_committed_changed_paths_intersects_base_and_verified` proves the git
helper directly (including deletion filtering), and the bulk-commit test proves
`PATH_SAMPLE_LIMIT` count+sample bounding.

Task 30 extends the closeout/integration coverage with
`integrated_external_contract_fixture`, which performs a real closeout and
ff-only integration before reusing the leaf. The re-closeout regression proves
that preview reports `integration_reopen.would_reopen`, apply clears the stale
integrated commit fields and returns the contract to `integration-pending`, and
the normal ff-only integration path then lands the new code and memory ledger
commits. The paired no-op regression proves a clean re-closeout after
integration reports no reopen, preserves completed integration fields, keeps the
recorded closeout commits unchanged, and does not move the code or memory source
branches.

The worktree-name resolution slice (MCP 2.9.3) adds
`test_resolver_resolves_contract_by_worktree_name`,
`test_resolver_returns_empty_for_unknown_worktree_name`,
`test_resolver_prefers_task_name_over_worktree_name`, and
`test_find_worktree_contract_matches_group_or_returns_none`, built on
`_external_memory_skeleton` / `_write_task_contract` helpers and importing
`worktree_group_for`. They prove `resolve_coordination_context(worktree_name=…)`
populates contract-derived fields from the matching worktree group, returns a
blank context for an unknown worktree name, lets an explicit `task_name` win over
a competing `worktree_name`, and that `find_worktree_contract` matches by group
or returns `None`. The post-landing cleanup (task 260628_post-landing-cleanup)
adds `test_find_worktree_contract_skips_archived_contract`, proving a
group-matching contract moved under `0_archive/` is not resurrected.

`RequireUpdatedRouteOverviewContentTests` covers the route-overview body gate:
with committed root and `src/app` overviews, the nearest-governing overview of
a changed path fails when stale or when its body update lacks a history entry,
passes via a `No route impact:` marked entry (returned as attested) or a
body+history update, the ancestor/root overview is reported as
`stamped_without_body_review` instead of failing, the root overview gates when
it is itself the nearest governor, and an empty plan is a no-op. The seven
direct-closeout end-to-end tests and their `direct_external_memory_fixture`
were removed with the direct-closeout surface (issue #62); the gate behavior
itself stays covered by these dedicated test classes, and the coverage the
direct tests carried moved to worktree-closeout equivalents:
`test_closeout_blocks_memory_commit_when_memory_quality_fails` (mocked failing
`run_memory_quality_check` blocks the memory commit with the formatted-findings
message) and `test_closeout_refreshes_entity_fingerprint_after_code_commit`
(seeded entity catalog row recomputed into `entities.md` after the worktree
code commit, before the memory commit).

### Conventions

The test imports helper modules directly from the MCP package path and uses only Python standard-library `unittest` and temporary directories. Drift-specific helpers build minimal route overview and entity catalog fixtures for deterministic `c-02-memory-quality-control` skill coverage, including realistic `Entity Inventory` headings paired with fingerprint rows. Benchmark runner portability tests import the package-local `agents_remember.benchmarks.runner` module from `mcp/src`.

### Invariants And Boundaries

These tests are focused smoke coverage, not exhaustive `c-09-git-worktree-manager` skill lifecycle integration tests. The `c-09-git-worktree-manager` skill coverage uses real temporary Git repos and worktrees, checks dirty-memory start blocking, checks closeout preview before approval, checks typed next hints instead of `next_command`, checks approval-note enforcement and recording, checks closeout metadata refresh to the new code commit before memory commit, checks route overview/index refresh before memory commit, checks memory quality failure blocks the memory commit and ledger update, checks entity fingerprint refresh planning and post-code-commit rewriting into `entities.md` before the memory commit, checks missing onboarding blocking before code commit, checks memory-worktree settings override source-memory settings during preview planning, checks long Windows paths in changed-file and sidecar existence probes, checks fast-forward integration, checks replay integration after parallel non-overlapping source changes, checks conflict blocking before source branches move, checks `_merge_integrated_commits` raises "not a fast-forward" before advancing the code branch so there is no half-integrated state, and checks cleanup after successful integration. The `c-02-memory-quality-control` skill drift additions use temporary repos to prove clean and changed route-local overviews, clean and changed entity fingerprints, missing entity evidence paths, missing fingerprint tables, inventory entries without fingerprint rows, and orphaned fingerprint rows. The `c-10-adopt-memory-baseline` skill coverage uses temporary code and memory repos, writes minimal verified onboarding, captures command output when exercising the CLI-style entry point, checks that adoption drift reports stay out of task folders, and checks that adoption writes `memory.md` plus the bootstrap `.gitkeep`. The `c-11-memory-carryover-from-branch` skill coverage uses temporary code and memory repos to prove landed source branch code carries new onboarding into official memory, same-path but different official changes remain review-required, a single earlier landed same-path commit stays `same-path-changed`/`review-required` instead of being treated as `exact-landed-commit` when a later same-path commit never landed, and unlanded source branch memory is rejected. Benchmark runner portability coverage intentionally stays at helper level so it can validate Windows-safe behavior, copy-only skill exposure, Codex `PATH` resolution, benchmark-only execution metadata, default-sandbox omission, variant-scoped provider setup, generated provider settings including `logs/providers/...` provider log paths, workspace-local `.codex` MCP registration, and local Git repository preparation semantics without network clones or benchmark token spend.

### Todos

Add fuller Git fixture tests for compatible external-memory start. Refresh verification metadata after the benchmark checkout cache tests are committed.

### Docs References

No external documentation is needed for this standard-library test.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding                                                                                                                                                                                                                                                                                                                           | Citations            | Source Path                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| The test module imports `c-09-git-worktree-manager` skill, `c-10-adopt-memory-baseline` skill, `c-11-memory-carryover-from-branch` skill, drift, resolver, ledger, contract, and benchmark helpers from MCP package modules and creates minimal file-level onboarding fixtures for adoption and carryover checks.                                                                                                             | L41-L68; L88-L106    | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| The common integration fixture creates real code and memory worktrees, closes a contract with code, memory content, and ledger commits, then reuses that fixture across integration tests.                                                                                                                                        | L203-L233            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| The resolver regression test proves `c-08-ar-coordination-context-resolver` skill returns `ar-coordination/tasks/<repo>` when no task name is supplied.                                                                                                                                                                                                                       | L302-L318            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| External-memory start blocks dirty source memory repos before worktree creation.                                                                                                                                                                                                                                                    | L338-L367            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Worktree contract tests check wrapper task roots without `-ar`, worktree groups with `-ar`, current-plus-legacy task-root candidates, and direct contract-path status loading.                                                                                                                                                    | L413-L448            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Closeout tests cover dry-run preview without approval, metadata refresh plan output, real closeout blocking without an approval note, approval-note persistence, onboarding metadata refresh to the new code commit, and missing onboarding blocking; the closeout **preview** path still reports `commit-approval-pending` / `request_commit_approval` (closeout owns the commit gate). | L451-L661            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| `test_status_reports_integration_pending_for_dirty_closed_contract` (slice 09) pins the corrected `status_payload` behavior: a closed-out contract reports its honest lifecycle position (`integration-pending` / `request_integration_decision`) even when the worktree is dirty — `git status` no longer fabricates `commit-approval-pending`. | L1302-L1314 | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| New closeout regression tests cover memory-worktree settings during planning and long Windows paths in changed-file and sidecar probes. | closeout regression tests | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| `c-09-git-worktree-manager` skill integration and cleanup tests cover ff-only source fast-forwarding, cleanup-pending status, cleanup removal, idempotent cleanup, cleanup blocking before integration, replay after parallel non-overlapping changes with a fresh ledger mapping, code conflict blocking before main moves, and `_merge_integrated_commits` refusing a non-fast-forward integrated code commit with a "not a fast-forward" `RuntimeError` while leaving `HEAD` unmoved. | `c-09-git-worktree-manager` skill integration tests | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Resolver and drift-report path tests check `code_repository_name`, `temp_root`, default report placement under `temp/drift-reports`, relative report resolution, parent-directory escape fallback, absolute-path containment, and explicit memory-root report redirection back to temp.                                           | L765-L811            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Deterministic `c-02-memory-quality-control` skill drift tests build route overview and entity catalog fixtures, then cover clean route scopes, changed route scopes, clean fingerprints, changed fingerprints, missing evidence paths, missing fingerprint tables, missing fingerprint rows, and orphaned fingerprint rows. | L112-L175; L1062-L1256 | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Resolver tests cover arbitrary installed runtime roots by making a non-`ar-coordination` directory with `skills/`, `system/`, `tasks/`, and `memory-repos/`, then proving `c-08-ar-coordination-context-resolver` skill uses it as the coordination root; adjacent tests prove source-checkout `.env` and `.env.example` no longer override coordination-root selection. | L852-L875 | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| `c-10-adopt-memory-baseline` skill tests cover ready status without a ledger, `code_repository_name`/`code_repository_root` resolver args, drift report placement outside task folders, drift blocking without explicit acceptance, and initial ledger creation with docs `.gitkeep`.                                                                           | L852-L923            | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| `c-11-memory-carryover-from-branch` skill tests pass `code_repository_name` and `code_repository_root`, then cover auto-carry for landed source branch code with new onboarding, refreshed official verification metadata, official ledger prepending, review-required same-path ambiguity, earlier-only-landed same-path commits yielding `same-path-changed`/`review-required` rather than `exact-landed-commit`, rejected unlanded source branch memory, and mapping an unmapped official code HEAD (e.g. a PR merge commit) to current memory content when nothing is actionable to carry (`ledger-mapped-head`).                                | `c-11-memory-carryover-from-branch` skill tests | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |
| Benchmark runner portability tests cover manifest path containment, non-string path rejection, manifest path component validation, read-only generated tree removal, stale directory symlink removal without deleting the target, Windows `.cmd` shim selection for `codex`, Codex `PATH` resolution and benchmark-only execution metadata, default-sandbox omission, variant-scoped provider selection, generated provider settings without coordinator `system/settings.json` and with central provider log paths, workspace-local `.codex` benchmark MCP registration, temporary provider setup settings handoff, cached repository reuse without clone or fetch, changed-pinned-commit fetching, force-clone cache discard, and copy-only benchmark skill exposure without the deleted shell installer. | L1577-L2225          | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No sibling repository evidence is needed for the test itself.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Series-Contract Notes

Worktree support coverage includes the master-start path that creates a root integration contract plus a leaf enclosure contract, and keeps closeout/onboarding/status tests aligned with leaf contract paths. It also covers the L3 memory-base regression: `_memory_base_for_source` records the memory base from the source-branch tip, not the repo HEAD when the memory repo is checked out on an unrelated branch.

## Update History

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 7 / friction F-R): added the
  missing-mapping recovery coverage — `_unmapped_external_contract` helper plus
  `test_missing_mapping_block_advertises_only_consumable_choices` (only executable choices named,
  `custom` gone, each consumable) and `test_reconciliation_records_the_mapping_and_starts_the_worktree`
  (reconciliation records the ledger mapping + `Ledger sync` commit and proceeds to a started worktree).
  Verification metadata pinned until closeout stamps the L18 commit.
- 2026-06-29T23:18+02:00 — Memory-base fix (L3): added `test_memory_base_for_source_uses_source_branch_tip_not_head` — proves `worktree_start` records the memory base from the source-branch tip, not the repo HEAD (repo on a divergent branch). Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T20:30+02:00 — Post-landing cleanup (task 260628_post-landing-cleanup): added `test_find_worktree_contract_skips_archived_contract` covering the `0_archive/` skip in `find_worktree_contract`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): documented the MCP 2.9.3 worktree-name resolution tests (`test_resolver_resolves_contract_by_worktree_name`, `…returns_empty_for_unknown_worktree_name`, `…prefers_task_name_over_worktree_name`, `test_find_worktree_contract_matches_group_or_returns_none`) and the `worktree_group_for` import. Grafted onto the series' task-30 re-closeout / leaf-enclosure coverage.
- 2026-06-27T21:10+02:00 — Task 30: added
  `integrated_external_contract_fixture` and re-closeout regressions proving an
  already-integrated leaf is reopened only when a new unlanded closeout exists,
  then reintegrates through the normal ff-only path; the no-op case preserves
  completed integration and source branch heads. Verification metadata pinned
  until closeout stamps the task-30 code commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: worktree support tests now cover master start creating a root integration contract plus leaf enclosure, new `task_resolver` helpers, closeout against leaf contracts, and schema/path updates across status, onboarding refresh, and provider setup fixtures. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-23T07:25+02:00 — slice 09 (gate-signal adoption, S1): the dirty-closed `status_payload` test was renamed to `test_status_reports_integration_pending_for_dirty_closed_contract` and now asserts `integration-pending` / `request_integration_decision` (was `commit-approval-pending`), pinning the corrected `lifecycle_guidance` — a dirty tree is no longer read as a commit-approval gate. Updated the closeout-tests Repo-Internal row (which had conflated this with the closeout-preview gate) and added a dedicated row for the renamed test; the closeout-**preview** `command_closeout` path still asserts `commit-approval-pending` (closeout owns the gate) and is unchanged. Verification metadata pinned until closeout stamps the slice-09 code commit.
- 2026-06-12T19:06+02:00 — Issue #83: added `committed_range_external_contract_fixture` plus closeout coverage for committed-range preview/apply (bounded payload shapes, non-blocking `unonboarded`, stamping to existing HEAD), stale-sidecar blocking for transported paths, second-closeout exclusion via `code_commit`, sync-transport exclusion, `committed_changed_paths` unit behavior, `PATH_SAMPLE_LIMIT` bounding, and the verified-baseline classifier cases; existing preview assertions adopted the count+sample shapes and plan literals gained `unonboarded`.
- 2026-06-11T14:12+02:00: No content impact: the repository rename sweep replaced `agents-remember-md` with `agents-remember` in the source file; the card already uses the new name and its semantics are unchanged.
- 2026-06-11T09:10+02:00 — Issue #62 follow-up: added `test_closeout_blocks_memory_commit_when_memory_quality_fails` and `test_closeout_refreshes_entity_fingerprint_after_code_commit` — worktree-closeout replacements for coverage the deleted direct tests carried; CI's `--fail-on-crap-threshold` gate had flagged `parse_entity_fingerprint_rows`, `_fingerprint_table_header`, and `_format_memory_quality_finding` over the CRAP threshold from the coverage loss.
- 2026-06-11T06:47+02:00 — Issue #62 worktree-only closeout: removed the seven `test_direct_closeout_*` end-to-end tests and the `direct_external_memory_fixture`; the sidecar/route-overview body-gate behavior remains covered by `RequireUpdatedSidecarContentTests` / `RequireUpdatedRouteOverviewContentTests` and the worktree closeout tests.
- 2026-06-10T05:20+02:00 — Issue #56 sub-task 2: added `RequireUpdatedRouteOverviewContentTests` (nearest-governor gating, ancestor reporting, marker attestation, untraced body edits, root-as-governor) and payload assertions for `route_overviews_attested_no_impact`; route-overview fixture gains a `No route impact:` entry.
- 2026-06-10T04:47+02:00 — Issue #56 sub-task 1: extended `RequireUpdatedSidecarContentTests` to the four-case gate (metadata-only, unmarked history-only, marked no-impact attestation, untraced body edit, body+history, new untracked sidecar) and paired the direct-closeout fixture's sidecar body edit with an Update History entry.
- 2026-06-02T04:00+02:00: Added `test_memory_carryover_maps_unmapped_official_head_when_nothing_to_carry` covering the new `ledger-mapped-head` result — carryover maps an unmapped official code HEAD (e.g. a PR merge commit) to current memory content when nothing is actionable to carry; the review-required case still returns `nothing-to-carryover`. Added `find_mapping`/`load_ledger` test imports. (`l-01-session-job-lifecycle` skill series, Sub-task C, mcp 1.1.0.)
- 2026-05-31T12:30+02:00 — Added coverage notes for new `_merge_integrated_commits` non-fast-forward integration refusal (no `HEAD` mutation) and the `c-11-memory-carryover-from-branch` skill earlier-only-landed same-path commit staying `same-path-changed`/`review-required`; the existing default-sandbox omission test is unchanged, so benchmark phrasing kept (1.0.0 review remediation).
- 2026-05-30T21:51+02:00: Re-verified against `825a172`; the only change was an installed-runtime config assertion adopting the renamed `timeout_caps["providerSetupSeconds"]` key. Coverage otherwise unchanged.
- 2026-05-29T18:35+02:00: Typed capture/payload/plan locals as `dict[str, Any]`, typed the `_setup` plan as `OnboardingRefreshPlan`, and added per-method `assert contract.memory_worktree/memory_repo_path is not None` narrowing; behavior-preserving (commit `0549b28`).
- 2026-05-29T07:36+02:00: Added `RequireUpdatedSidecarContentTests` covering the closeout content gate (`require_updated_sidecar_content`): blocks a changed source with an unmodified sidecar, passes when the sidecar body is updated, and no-ops with no required sidecars.
- 2026-05-28T15:24+02:00: Updated after direct closeout tests began asserting route overview/index refresh before memory commit and memory quality failure blocking before memory/ledger commits. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-28T12:32+02:00: Updated after benchmark provider settings tests began asserting central `logs/providers/...` log paths.
- 2026-05-24T18:51+02:00: Added closeout regression coverage for memory-worktree settings and long Windows path changed-file/sidecar probes.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` covered `.codex` benchmark registration, default sandbox, and ignored `.env` resolver files.
- 2026-05-24T09:52+02:00: Updated after resolver tests removed the source-checkout `.env` override path and asserted `.env`/`.env.example` are ignored.
- 2026-05-24T09:23+02:00: Updated after benchmark portability tests moved child-workspace MCP registration and skill exposure from `.agents` to `.codex`.
- 2026-05-24T08:56+02:00: Updated after benchmark portability tests began covering child-workspace MCP registration and default-sandbox Codex command construction.
- 2026-05-24T06:57+02:00: Updated after benchmark tests began asserting Codex `PATH` resolution and benchmark-only execution metadata.
- 2026-05-24T05:48+02:00: Updated after benchmark portability tests began covering variant-scoped provider selection and generated benchmark provider settings without coordinator `system/settings.json`.
- 2026-05-24T05:03+02:00: Updated after worktree support tests began asserting typed MCP next hints and absence of legacy `next_command` payload fields.
- 2026-05-23T17:50+02:00: Moved onboarding to `mcp/tests` after the tests moved out of `runtime/skills/tests` and updated imports to MCP package modules only.
- 2026-05-23T14:20+02:00: Updated after benchmark skill exposure became copy-only and test imports began explicitly preserving both shared runtime and MCP package paths.
- 2026-05-23T13:46+02:00: Updated after benchmark runner tests switched to package-local MCP module imports and source scripts were removed.
- 2026-05-23T05:32+02:00: Updated after benchmark runner tests switched from installed runtime scripts to top-level source/package-owned scripts.
- 2026-05-18T22:01+02:00: Added benchmark runner cache regressions for reusing an existing pinned checkout, fetching when the manifest commit is absent, and force-cloning on request.
- 2026-05-16T20:14+02:00: Updated benchmark runner portability coverage after adding regressions for stale directory symlink cleanup and Windows `codex.cmd` shim resolution.
- 2026-05-16T20:07+02:00: Refreshed benchmark runner portability coverage notes after manifest path validation started rejecting non-string values in addition to unsafe strings.
- 2026-05-16T19:52+02:00: Added benchmark runner portability coverage for manifest path validation, Windows-safe generated tree removal, and copy/auto skill exposure without requiring Bash.
- 2026-05-16T18:17+02:00: Added `c-09-git-worktree-manager` skill direct closeout coverage for entity fingerprint refresh planning and post-code-commit fingerprint rewriting before the memory commit.
- 2026-05-15T12:57+02:00: Added `c-02-memory-quality-control` skill regression coverage for entity inventory entries without fingerprint tables, missing fingerprint rows, orphaned fingerprint rows, and removed/renamed/moved guidance on missing evidence paths. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T11:46+02:00: Added deterministic `c-02-memory-quality-control` skill tests for route-local overview drift and repo entity fingerprints. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T01:45+02:00: Added coverage for installed-runtime coordination roots with arbitrary directory names. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-15T01:07+02:00: Added coverage for repo-specific `c-08-ar-coordination-context-resolver` skill `task_root` output when no task name is supplied. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-12T10:59: Updated coverage summary after branch fields were removed from canonical ledgers and legacy branch metadata became non-blocking.
- 2026-05-11T19:42: Refreshed verification metadata to `aa85d3862bf21fed791e3170e6957f9288c319e8` and corrected stale/placeholder test citation ranges after source verification.
- 2026-05-11T18:34: Updated after resolver-facing and `c-11-memory-carryover-from-branch` skill test namespaces switched from ambiguous repo args to `code_repository_name` and `code_repository_root`.
- 2026-05-11T03:00: Updated after adding `c-11-memory-carryover-from-branch` skill memory carryover fixtures for landed, ambiguous, and unlanded source branch memory.
- 2026-05-10T03:11: Updated after drift report path coverage began asserting explicit memory-root paths are redirected to coordination temp.
- 2026-05-10T03:01: Updated after adding `c-09-git-worktree-manager` skill direct checkout closeout fixture and dry-run/success/missing-onboarding tests.
- 2026-05-10T01:55: Updated after adding closeout metadata refresh and missing-onboarding regression coverage.
- 2026-05-10T01:19: Updated after adding closeout commit-approval preview and approval-note tests.
- 2026-05-10T01:04: Updated after adding direct contract-path status coverage.
- 2026-05-10T00:56: Updated after adding dirty external-memory start blocking and blocked integration status assertions.
- 2026-05-10T00:47: Updated after adding wrapper task-root assertions and `c-09-git-worktree-manager` skill cleanup lifecycle tests.
- 2026-05-10T00:36: Refreshed verification metadata after integration tests landed on main and removed a stale task-artifact reference.
- 2026-05-09T23:55: Updated coverage summary after adding `c-09-git-worktree-manager` skill integration fast-forward, replay, and conflict-blocking tests.
- 2026-05-09T23:22: Updated coverage summary after adding temp-root drift report path assertions.
- 2026-05-09T22:46: Updated coverage summary for `c-10-adopt-memory-baseline` skill adoption status, drift blocking, and ledger creation tests.
- 2026-05-09T22:10: Updated test coverage summary for malformed metadata, branch-mismatch blocking, compatible external-memory reporting, internal memory reporting, and cross-repo v2 include states.
- 2026-05-09T21:59: Created onboarding for the worktree-support smoke tests.
