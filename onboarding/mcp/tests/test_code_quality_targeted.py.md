# mcp/tests/test_code_quality_targeted.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_code_quality_targeted.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The L17 proof suite for the change-set-scoped leaf gate: derivation selectors,
the reverse-import closure, the refusal shape, and real targeted wrapper runs.

## Code Commentary

### Logic

`TargetedScopeDerivationTests` builds real miniature Git repositories with a synthetic canonical
evidence catalog. It proves selection is dependency-owned and typed: production imports select
their consumers, shared test-support imports select only their static consumers, catalogued
fixtures select their declared consumers, and each selected test carries a
`SelectionReasonKind`. A `conftest.py` change globally invalidates the Python test population.
Unknown support, deleted tests, unowned production, and unowned scripts do not pretend selection
is complete; they fail closed to the safe full test population. Documentation remains visible in
the changed-path report while producing no Python scope.

This replaces the earlier contract that an unowned production module simply refused and that
scripts-only changes produced an empty test selection. The safe fallback is explicit and carries
incomplete-impact evidence; it is not a silent heuristic. Tests-only changes still leave product
coverage empty, and unknown Git bases or Git transport failures remain typed `ScopeError`s.

`TargetedWrapperRunTests` drives the real wrapper contract: every rail receives the derived scope,
the typed derivation is printed, Radon sees changed production modules, no-Python changes
short-circuit honestly, tests-only runs mark measurement rails not applicable, and scripts-only
runs execute the fail-closed test population while leaving coverage rails out.

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
- An incomplete or globally invalidated impact never shrinks to an optimistic subset; the safe
  population is selected and the reason remains visible.
- Diff is always measured against the passed base revision.
- The suite never mocks the wrapper's scope derivation for the real-run class.
- Importable verification infrastructure cannot silently acquire product measurement authority.

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
