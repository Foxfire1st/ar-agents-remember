# mcp/tests/test_code_quality_targeted.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_targeted.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | db57101a9001ede8c681ff9de4eb0147d8b636bc |
| lastVerifiedCommitDate | 2026-09-02T16:49:50+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The L17 proof suite for the change-set-scoped leaf gate: derivation selectors,
the reverse-import closure, the refusal shape, and real targeted wrapper runs. L19
recast the fail-closed contract: an incompletely owned targeted change now refuses
with a zero population instead of broadening to safe-full, and the suite forces the
content-addressed selector result shape end to end.

## Code Commentary

### Logic

`TargetedScopeDerivationTests` builds real miniature Git repositories with a synthetic canonical
evidence catalog. It proves selection is dependency-owned and typed: production imports select
their consumers, shared test-support imports select only their static consumers, catalogued
fixtures select their declared consumers, and each selected test carries a
`SelectionReasonKind`. A `conftest.py` change globally invalidates the Python test population.
Unknown support, deleted tests, unowned production, and unowned scripts do not pretend selection
is complete; they fail closed — with L19 the derived population is empty and the unresolved inputs
carry the reasons, so Gate 2 blocks instead of selecting the safe full population. Documentation
remains visible in the changed-path report while producing no Python scope. A deleted test that was
never selected resolves complete with an `deleted-test-removed-from-population` input decision
rather than poisoning ownership.

The remote-literal generated-projection case proves `.generated/rules.mdc` change selects its
observed literal consumer before any irrelevance decision. The selector-result cases force the
`repository-selector-result/v2` shape: every unresolved input is published without expansion,
empty/targeted/declared-full populations are distinct, and a changed dashboard input is an explicit
`global-invalidate` for the declared dashboard suite rather than silent irrelevance.

This replaces the earlier contract that an unowned production module simply refused and that
scripts-only changes produced an empty test selection but still ran pytest. L19 asserts scripts-only
runs refuse before Gate 2 with `test-selection-ownership-incomplete` naming
`scripts/sync.py`.

`TargetedWrapperRunTests` drives the real wrapper contract: every rail receives the derived scope,
the typed derivation is printed, Radon sees changed production modules, no-Python changes
short-circuit honestly, tests-only runs mark measurement rails not applicable, and a scripts-only
run refuses before executing any rail.

The miniature repository now declares both a product package and a Dagger-style verification
package. A focused derivation case changes only the verification package and proves that it remains
in lint and type scope while `coverage_paths` stays empty and the derived Coverage.py root list
contains only the product package. Import-root derivation is consumed through the dedicated
`quality_subprocess_environment` module; this suite preserves the product-versus-verification
boundary while the child-environment owner is tested separately.

### Conventions

Fixtures are real git repositories with `pyproject.toml` quality config so the
scope derives from `git ls-files`/`pytest_testpaths` exactly as production does.

### Invariants And Boundaries

- Selection authority comes from the canonical dependency/evidence model; tests do not reproduce
  private AST selection helpers.
- An incomplete or globally invalidated impact never shrinks to an optimistic subset and never
  broadens to safe-full; it publishes an empty population with typed unresolved reasons that block
  Gate 2.
- Diff is always measured against the passed base revision.
- The suite never mocks the wrapper's scope derivation for the real-run class.
- Importable verification infrastructure cannot silently acquire product measurement authority.
- The selector result emitted by the suite is validated through the canonical v2 contract.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for the targeted suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper contract the real-run class drives. | "def quality_steps("; "def run_quality_check(" | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:136-168; mcp/test_support/agents_remember_test_support/code_quality/check.py:148-198 |
| The printed derivation lines the suite asserts. | `targeted_scope_lines` | mcp/test_support/agents_remember_test_support/code_quality/scope_reporting.py:278-314 |
| Targeted configuration refuses incomplete ownership before any command. | `config_from_args` | mcp/test_support/agents_remember_test_support/code_quality/check.py:781-786 |
| The selector result contract the suite validates. | `RepositorySelectionResult`; `build_repository_selection_result` | mcp/src/agents_remember/certification/repository_profiles/selection_results.py:89-130; mcp/src/agents_remember/certification/repository_profiles/selection_results.py:203-241 |
| Unowned production and unknown test support refuse with empty populations. | `test_changed_production_module_without_owner_refuses_without_broadening`; `test_unknown_test_support_and_deleted_test_fail_closed`; `test_unowned_script_change_refuses_before_any_test_command` | mcp/tests/test_code_quality_targeted.py:266-283; mcp/tests/test_code_quality_targeted.py:357-397; mcp/tests/test_code_quality_targeted.py:585-596 |
| Selector-result and dashboard-lane cases force the exact v2 publication shape. | `test_selector_result_publishes_every_unresolved_input_without_expansion`; `test_selector_result_distinguishes_empty_targeted_and_declared_full`; `test_dashboard_change_is_explicitly_global_to_its_declared_suite` | mcp/tests/test_code_quality_targeted.py:485-506; mcp/tests/test_code_quality_targeted.py:508-530; mcp/tests/test_code_quality_targeted.py:532-583 |
| Wrapper runs refuse scripts-only changes before Gate 2. | `test_scripts_only_run_refuses_before_gate_two` | mcp/tests/test_code_quality_targeted.py:839-857 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260824-PDLS Admission Boundary

Every targeted-wrapper configuration now carries `QUALITY_TEST_ADMISSION` from the certifying
bootstrap. Target selection and changed-line semantics are unchanged; the suite additionally proves
the targeted planner cannot be invoked as a diagnostic fallback.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 exact-ownership
  recast — unowned production/unknown support/scripts-only changes now refuse with empty test
  populations (or refuse config before Gate 2), deleted tests resolve complete, and the suite
  forces the `repository-selector-result/v2` selector result and dashboard global-invalidation
  lanes. Verification is pinned to the owning commit.

- 2026-08-27T18:33+02:00 — Reconciled the suite with the dedicated child-environment/import-root
  owner; targeted product-versus-verification semantics are unchanged.
- 2026-08-27T14:04+02:00 — Added an explicit product-versus-verification fixture and regression
  proof that targeted scope never turns a changed Dagger/test-support package into product
  coverage or CRAP scope.
- 2026-08-26T10:44:52+02:00 — Rewrote the targeted-gate contract around canonical dependency ownership, typed selection reasons, global invalidation, and explicit fail-closed full-population fallback.

- 2026-08-24T21:23+02:00 — Added typed Dagger admission to targeted quality fixtures.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new targeted-derivation suite; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
