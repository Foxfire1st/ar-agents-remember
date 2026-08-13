# mcp/src/agents_remember/code_quality/targeted.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/code_quality/targeted.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-08T02:00+02:00                     |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d` |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

The deterministic change-set scope authority for leaf-edge quality gates
(260731-EFA-L17). The quality ladder keeps leaf-edge checks mandatory but points
them at the leaf's own change set instead of the whole tree: ruff/ruff-format
over the changed Python files, pyright over the changed files plus the
reverse-import closure, pytest over the derived test subset, and
coverage/CRAP/radon over the changed production modules. The derivation is
computed on every run — no maintained map file, no per-leaf declaration for a
manager to validate — and printed for review.

## Code Commentary

### Logic

`TargetedScopeResult` (class, lines 43-67) carries every derived input the
targeted run prints and hands to `GateScope` via `to_gate_scope`: changed paths,
lint/type/coverage/test paths, the reverse-import closure, and the changed
files the file-size rail measures.

The derivation chain in `derive_targeted_scope` (lines 342-391):

1. `changed_python_paths` (lines 77-103) diffs base-to-working-tree with
   `--diff-filter=ACMR` so the run certifies the bytes the leaf is about to push
   or commit; deletions are filtered because there is nothing left to lint.
2. `import_roots_for` / `module_for_path` (lines 104-136) map tracked files to
   dotted module names under the top-level package roots; files outside the
   roots (scripts, tests) are still linted/type-checked but have no import
   identity for closure or test mapping.
3. `_reverse_import_closure` (lines 215-233) walks every tracked importer of a
   changed module transitively, so a cross-file type break in an unchanged
   importer is still caught by pyright.
4. `_tests_for_changed_modules` (lines 272-292) unions three deterministic
   selectors per changed module: transitive importers that live under a test
   root (`_transitive_importers`, lines 293-320 — this is what reaches a
   changed internal module through its public re-export home), name matches
   (`name_match_tests`, lines 194-210: `test_<module_suffix>.py`), and
   whole-word dotted-path string references (`_string_reference_tests`, lines
   321-341 — the MCP registration suite's string-based wiring tests).
5. A changed production module with no derived test subset is **refused**
   (`ScopeError` naming the module), never certified with a narrower run.

`resolve_relative_import` / `dotted_ancestors` (lines 137-156) handle relative
imports and the package-prefix loading semantics (`import a.b.c` also imports
`a` and `a.b`).

### Conventions

The module reuses `code_quality.scope` primitives (`git_ls_files`,
`pytest_testpaths`, `top_level_packages`) and `kernel.git_command.run_git`
instead of spawning git itself. `TargetedScopeResult.to_gate_scope` keeps
`scope_roots` and `untracked_paths` from the full scope so a targeted run still
reports untracked exposure.

### Invariants And Boundaries

- The diff is always base-to-working-tree; the caller's `--diff-base` (the
  leaf's recorded base commit) is what makes the changed-lines coverage floor
  measure the leaf's own diff.
- An uncovered changed production module refuses the run (R5 refusal shape).
- Tests-only and no-Python-changed leaves derive empty production coverage and
  the caller prints honest not-applicable lines instead of vacuous rails.
- Coverage.py instruments the top-level package root (same proven shape as the
  full wrapper) — per-module `--cov` on FastMCP/pydantic files crashed
  collection and is deliberately not used.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo
(`system/sources.md` has no entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is configured for the targeted derivation. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper consumes the derived scope for every rail and prints the derivation on a targeted run. | `quality_steps`, `run_quality_check` | mcp/src/agents_remember/code_quality/check.py:320-366; mcp/src/agents_remember/code_quality/check.py:420-469 |
| The targeted run's printed derivation and per-rail provenance lines. | `targeted_scope_lines`, `wrapper_scope_line`, `fixed_step_scope_line` | mcp/src/agents_remember/code_quality/scope_reporting.py:235-263; mcp/src/agents_remember/code_quality/scope_reporting.py:136-163; mcp/src/agents_remember/code_quality/scope_reporting.py:164-234 |
| The changed-lines floor and CRAP consume the same coverage JSON as the full wrapper. | `run_diff_coverage`; `run_crap_calculator` | mcp/src/agents_remember/code_quality/post_coverage.py:121-170; mcp/src/agents_remember/code_quality/post_coverage.py:35-101 |
| Proofs for the derivation selectors, the transitive-import closure, the refusal shape, and real-run radon input. | `TargetedScopeDerivationTests`, `TargetedWrapperRunTests` | mcp/tests/test_code_quality_targeted.py:142-357; mcp/tests/test_code_quality_targeted.py:360-629 |

## Cross-Repo References

No meaningful cross-repo references found — the targeted derivation is
repository-local gate machinery.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: created this file-level
  onboarding card for the new change-set derivation module; content derived from
  the current worktree source. Verification metadata pinned until closeout
  stamps the 260731-EFA-L17 commit.
