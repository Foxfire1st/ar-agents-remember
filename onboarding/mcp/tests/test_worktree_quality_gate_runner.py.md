# mcp/tests/test_worktree_quality_gate_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_quality_gate_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T15:11:59+00:00 |
| lastVerifiedCommitHash | `c69d5171187fa1957025e393270db9f5a864ab14` |
| lastVerifiedCommitDate | 2026-09-06T16:32:29+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[tests overview](overview.md)

## Purpose

Owns profile-required Dagger command planning, preview, host refusal, memory-cap policy, report replacement and failure transport. These runner tests remain separate from closeout commit and publication mechanics.

## Code Commentary

### Logic

`CodeQualityGateTests` requires an explicit repository profile whenever code would commit and returns the no-code-commit preview only when no commit is planned. A separate consumer repository with its own registered profile follows the same policy. Missing profiles refuse before the injected executor starts.

The successful outcome helper observes the real temporary Git candidate and comparison base, preserves the admitted source selection, writes a complete fixture catalog and publishes it through the real host report owner. Runner tests inspect the typed result, exact diff-base forwarding, profile adapter command and requested full-mode cap. The report cases replace one completed enclosure report and preserve its previous bytes on interruption.

### Conventions

The self-profile checkout and catalog are shared with `gate_certification_test_support.py`; the generic checkout and target helpers remain in `test_worktree_closeout_quality_gate.py`. Rail execution is injected. Physical fixture publication and typed consumer validation do not certify a live Dagger run or perform leaf finalization.

### Invariants And Boundaries

- Profiles are mandatory for code certification regardless of repository name; wrapper presence alone is not admission authority.
- Targeted and full modes are explicit plan inputs, and the real Git comparison base reaches the executor request and report.
- Explicit caps report `mode=explicit-cap`; absent caps report `mode=container-host-managed`. Both retain container-host-managed swap and profile-adapter-owned process policy.
- Host quality execution refuses before running a profile.
- The enclosure report path is stable: completed runs replace it, while interruption preserves the prior completed report.
- Unknown modes refuse, and failure output remains bounded.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured for this repository-local runner suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Profiles are required for planned code commits and symbolic previews. | `test_preview_requires_the_explicit_repository_profile_for_code` | mcp/tests/test_worktree_quality_gate_runner.py:85-113 |
| Another configured repository has the same strict profile authority. | `test_profile_authority_is_repository_generic_without_a_name_special_case` | mcp/tests/test_worktree_quality_gate_runner.py:158-176 |
| Missing profile authority prevents executor invocation. | `test_gate_refuses_to_run_when_the_profile_is_missing` | mcp/tests/test_worktree_quality_gate_runner.py:178-196 |
| The successful fixture publishes exact candidate and source-selection catalog bytes through the host owner. | `_successful_quality_outcome` | mcp/tests/test_worktree_quality_gate_runner.py:32-73 |
| Full mode, exact base, cap and profile identity reach the injected executor. | `test_dagger_executor_uses_the_same_staged_candidate_and_never_runs_host_rails` | mcp/tests/test_worktree_quality_gate_runner.py:204-242 |
| Completed runs replace the single report. | `test_gate_replaces_one_test_report_instead_of_accumulating_runs` | mcp/tests/test_worktree_quality_gate_runner.py:244-278 |
| Interruption preserves the previous completed report. | `test_interrupted_gate_keeps_the_previous_completed_test_report` | mcp/tests/test_worktree_quality_gate_runner.py:280-300 |
| The real leaf base reaches the request and report without a separate CLI diff-base argument. | `test_gate_measures_the_leaf_diff_not_the_whole_branch` | mcp/tests/test_worktree_quality_gate_runner.py:302-329 |
| The command uses only the declared adapter and its default memory policy. | `test_command_planning_uses_only_the_declared_profile_adapter` | mcp/tests/test_worktree_quality_gate_runner.py:354-376 |
| Explicit caps retain profile-owned process and host-managed swap policy. | `test_full_gate_preview_names_the_memory_cap_and_policy` | mcp/tests/test_worktree_quality_gate_runner.py:407-429 |
| Gate failures transport only bounded adapter output. | `test_gate_failure_includes_bounded_profile_adapter_output` | mcp/tests/test_worktree_quality_gate_runner.py:558-587 |
| Generic checkout authority remains in the closeout test owner. | `_checkout_with_profile` | mcp/tests/test_worktree_closeout_quality_gate.py:79-94 |
| The target helper binds repository and profile explicitly. | `_quality_target` | mcp/tests/test_worktree_closeout_quality_gate.py:97-108 |

## Cross-Repo References

The generic consumer fixture remains same-repository test evidence; it proves that a configured profile, rather than a repository-name special case, controls applicability.

| Finding | Anchor | Source |
| --- | --- | --- |
| No separate cross-repository protocol is introduced by this test module. | N/A | N/A |

## L23 Host-Execution Removal

The surviving local diagnostic entry point is a refusal surface. Its test requires the host-quality prohibition before any profile execution; the removed interpreter and host memory-cap machinery is not reconstructed here.

## R39 Runner Policy Proofs

Current policy is expressed through explicit profile admission for both the self repository and a consumer fixture. Missing-profile refusal replaces the former wrapper-presence policy, while Dagger remains the declared acceptance adapter.

## R43 Builder-Level Dagger Refusal

Current builder tests assert the exact profile adapter command and memory-policy payload. The suite no longer passes a local executor argument to these builders; direct host execution remains covered by the separate refusal test.

## 260824-PDLS Lifecycle Evidence Proof

The successful fixture returns `CleanQualityOutcome` carrying the exact candidate tree, decoder digest and original published manifest. Full catalog validation then supplies the record seam with observed fixture bytes; a zero subprocess exit alone is insufficient.

## Update History

- 2026-09-06T15:11:59+00:00 — L33 pending candidate curation: Re-read the prepared source, reconciled profile-required planning and shared fixture ownership, preserved report/cap/host-refusal contracts, and replaced obsolete wrapper/local-builder claims with their current tests. Verification names the real prepared source commit c69d5171187fa1957025e393270db9f5a864ab14; this entry does not claim CCR acceptance.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the profile-target cutover of the quality gate runner tests.


- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the quality gate and clean executor package relocations; runner outcome and evidence assertions are unchanged.
- 2026-08-24T21:23+02:00 — Replaced zero-exit-only fakes with candidate-bound certifying outcomes.

- 2026-08-14T12:13:26+02:00 — R43 curator: recorded builder-level non-Dagger refusal and aligned
  missing-wrapper wording. Verification remains closeout-owned.

- 2026-08-14T11:27+02:00 — R39 curator: reconciled the test card with self-policy, immediate host
  refusal, and the simplified Dagger-only adapter. Verification remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: quality-runner tests require Dagger-only
  execution, explicit mode/diff base, exact candidate materialization, fail-closed status, and no
  host or direct-Docker compatibility path.
- 2026-08-12T20:10+02:00 — L23 curator: documented short native temp-root propagation through the quality runner; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 replaced a platform branch in the test expectation with an equivalent lookup; host-managed and explicit-cap runtime behavior is unchanged.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: added the
  host-managed full command/report proofs and resource-policy payload coverage;
  retained explicit-cap failure proofs. Verification metadata remains pinned
  until closeout stamps L24.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: created from `CodeQualityGateTests` in the
  closeout quality-gate suite; retained shared helpers and separated runner policy from closeout
  mutation while bringing both files below the hard size gate.
