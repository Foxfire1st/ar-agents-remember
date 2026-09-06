# test_worktree_support.py

| Field                  | Value                                                    |
| ---------------------- | -------------------------------------------------------- |
| repository             | agents-remember                                       |
| path                   | `mcp/tests/test_worktree_support.py` |
| doc_type               | `file-level-onboarding`                                  |
| lastUpdated | 2026-09-07T00:28+02:00 |
| lastVerifiedCommitHash | `cfd0938103b1392e471144b6997c51a41591ad2b` |
| lastVerifiedCommitDate | 2026-09-04T08:34:11+02:00 |
| governingOverview      | `overview.md`                                            |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Shared temporary Git, external-memory, task-lineage and closeout-component fixtures for retained worktree tests. The current module has no collected `test_*` methods; `WorktreeSupportTests` supplies helper methods to consumers.

## Code Commentary

### Logic

`open_external_contract_fixture` creates real temporary code and memory repositories, a selected fixture profile, a ledger baseline, task lineage and an external-memory contract. Variant fixtures add committed ranges, closed or integrated state. File, overview and entity helpers create controlled onboarding inputs; their existence is not a coverage claim.

`closeout_publication_facts` uses the actual pair, route-review, attestation and memory-check owners and stages the fixture candidate. It labels the code-quality result `component-fixture` with `acceptanceClaim=False`. `run_authorized_closeout_mechanics` exercises the publication component using those facts; it does not certify the selected lifecycle operation or execute its gates.

### Invariants And Boundaries

- Fixture-created commits and mappings belong to temporary repositories.
- A writer-component fixture must not be reported as full closeout or gate acceptance.
- Consumer tests determine actual protection. Removed slice matrices and their historical outcomes are not current executable coverage.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| External-memory fixture supplies real isolated Git repositories and current contract inputs. | `open_external_contract_fixture` | mcp/tests/test_worktree_support.py:420-508 |
| Publication facts retain an explicit non-acceptance component-fixture result. | `closeout_publication_facts` | mcp/tests/test_worktree_support.py:831-882 |
| Writer mechanics call the publication component without claiming gate acceptance. | `run_authorized_closeout_mechanics` | mcp/tests/test_worktree_support.py:885-896 |
| The base class provides helper methods rather than collected test cases. | `WorktreeSupportTests` | mcp/tests/test_worktree_support.py:948-1023 |

## Update History

- 2026-09-07T00:28+02:00 — Reconciled this retained helper module to its actual fixture role; removed obsolete sliced-suite coverage prescriptions while preserving historical entries and verification pins.

- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass for cfd09381 (CCR-R12@v4): recorded the `ReportBindings` publication cutover in the shared closeout-quality fixture helper.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile fixture installation, TEST_CERTIFICATION_PROFILE_REFERENCE, publish_passing_closeout_quality, and the publish_code_quality mechanics flag.


- 2026-08-29T11:41+02:00 — Extended the shared external-closeout success fixture with complete
  task topology and production-owned structured coherence publication. Verification remains
  closeout-owned.

- 2026-08-26T08:15+02:00 — Added the shared canonical `seed_memory_ledger` fixture used by
  paired-source activation/bootstrap tests and refreshed this card's shifted exact source ranges.
  Verification metadata remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this test card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-20T05:12+02:00 — L11 landed-wave refresh: the leaf-segment graph-model commit
  (f2e2f4b9) touched this source; card re-verified against the current file, verification stamp
  advanced to f2e2f4b9. Body unchanged — the documented contract still holds.

- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: support integration cases preserve
  task-addressed durable closeout/integration observation, current lineage, and exact recovery
  guidance across restart boundaries.

- 2026-08-13T12:53+02:00 — L23 lineage-fixture repair: external committed/closed leaf fixtures now
  carry a real parent series contract and master code/memory worktrees, so lifecycle tests prove the
  full task-derived source chain instead of bypassing it. Verification provenance remains
  closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: linked the central external-closeout fixture to a real parent series so closeout lineage admission is exercised by default. Verification metadata remains closeout-owned.

- 2026-08-12T20:10+02:00 — L23 curator: documented the reusable contract-backed lineage fixture; verification remains closeout-owned.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: this test module was split in place into a family under 1,200 lines (L7-R5); the card remains the family entry point and the name set was reconciled item for item. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-05T22:55+02:00 — 260731-EFA-L16 curator: recorded the two closeout citation-gate tests — a changed construct completes with the stamp advanced to the new code commit, and a deleted construct refuses in the citation gate BEFORE the code commit with `citation_anchor_absent_from_range` (no commit spent) — plus the phase-payload contract (citation pair before the refresh, sanity checks after). Follow-up: `_refresh_regenerated_documents` coverage (stamps only touched citation documents; skips planned/excluded/no-metadata/prose-only; empty without a memory tree). Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: narrowed and rebound integration, cleanup, and carryover claims to their complete test bodies under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T20:53:56+02:00 — W2-B04 curator: repaired 34 citation findings; scoped check passed.

- 2026-08-01T10:04+02:00 — 260731-EFA-L4 curator: No content impact: five one-for-one line
  replacements, none of which this card describes. Four are fixture values moving to the narrowed
  `WorkflowKind` — `workflow_kind="chat"` becoming `"chat-task"` in the external-contract fixtures
  and atomic-integrate contract — forced by the two-value workflow contract. The fixture definitions
  and contract vocabulary were re-read directly: cit:([`open_external_contract_fixture`, `committed_range_external_contract_fixture`, `closed_external_contract_fixture`], mcp/tests/test_worktree_support.py:474-564; mcp/tests/test_worktree_support.py:698-772; mcp/tests/test_worktree_support.py:787-870); cit:([`DEFAULT_WORKFLOW_KIND`], mcp/src/agents_remember/worktrees/worktree_contract.py:84-84).
  The fifth is inside `test_status_reports_integration_pending_for_dirty_closed_contract`, where
  `payload["nextTool"]` became `payload.get("nextTool")`: `status_payload` now returns a
  `WorktreeStatusPayload` whose `nextTool` is `NotRequired` (omitted rather than `""`), so the
  subscript is a type error. Same expected value, `"worktree_integrate"`, and the paired
  `assertNotIn("next_command", payload)` is untouched — the card's claim for that row is the
  `integration-pending` / `request_integration_decision` position, which is unchanged, and the card
  names `nextTool` nowhere. All Repo-Internal citations were re-read against their named helpers,
  tests, and benchmark class; no test method was added, removed or renamed.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: the PLR0913 pass moved the call shapes this
  suite uses. `default_contract` now takes a `ContractTask` plus `leaf`/`code`/`memory` objects,
  `resolve_coordination_context` takes `hints=CoordinationHints(...)` and
  `selector=EnclosureSelector(...)`, `_merge_integrated_commits` takes one `IntegratedCommits`, and
  the benchmark helpers take `BenchmarkWorkspace` (with `BenchmarkRun` plus `BenchmarkTask` for
  `run_one`). Corrected the worktree-name resolution claim to the `selector=` form and added a
  Conventions paragraph recording those call shapes together with the codex run-metadata fixture,
  which now patches `benchmark_runner.subprocess.run` to a plain successful `CompletedProcess`
  instead of a `fake_run` that wrote into the JSONL. Re-anchored all thirteen self-citations in
  Repo-Internal References against the current 3845-line file; several had drifted badly before
  this leaf, for example benchmark portability was cited at L1577-L2225 but actually spans
  L2949-L3582. No test method was added, removed, or renamed.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: initialized external-memory fixtures now write and
  commit explicit supported onboarding storage/path-rule authority before success-path mutations.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: added default light-task `start_result` coverage for
  doc-id persistence and wrong-ref refusal, and retargeted the memory-base helper regression to the
  public `start_contract.memory_base_for_source` name. Verification metadata pinned until closeout
  stamps the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: master-start coverage now expects canonical doc-id leaf
  contract persistence and the canonical leaf enclosure path after resolving a legacy leaf ref. Verification
  metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 7 / friction F-R): added the
  missing-mapping recovery coverage — `_unmapped_external_contract` helper plus
  `test_missing_mapping_block_advertises_only_consumable_choices` (only executable choices named,
  `custom` gone, each consumable) and `test_reconciliation_records_the_mapping_and_starts_the_worktree`
  (reconciliation records the ledger mapping + `Ledger sync` commit and proceeds to a started worktree).
  Verification metadata pinned until closeout stamps the L18 commit.
- 2026-07-07T06:10+02:00 — PR #100 review fix (Codex P1, merge `e358c4a`): added
  `test_reconciliation_refuses_when_memory_repo_is_on_another_branch` — reconciliation refuses
  (naming both branches, nothing committed) when the official memory repo is checked out off the
  memory source branch. Post-merge onboarding refresh (developer-approved) verified against main
  @ e358c4a.
- 2026-06-29T23:18+02:00 — Memory-base fix in L3: added `test_memory_base_for_source_uses_source_branch_tip_not_head` — proves `worktree_start` records the memory base from the source-branch tip, not the repo HEAD (repo on a divergent branch). Verification metadata pinned until closeout stamps the code commit.
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
