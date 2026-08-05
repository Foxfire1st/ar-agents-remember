# mcp/tests/test_gate_scope.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_gate_scope.py`             |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T15:32+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This is the file that makes "the gate's scope is the tree" true rather than intended.
`check.derive_scope` reads scope off `git ls-files`, but a derivation can still miss a
corner of the tree — a directory nobody thought of, or a language whose rail nobody wired
up. This module recomputes the tracked set independently, builds the commands the wrapper
actually runs, and asserts those commands reach every tracked file.

## There Is No Allowlist

**Read this before adding one.** Three empty allowlists stood in this module —
`ALLOWED_UNGATED_PYTHON`, `ALLOWED_UNGATED_TYPESCRIPT`, `ALLOWED_UNTYPED_TYPESCRIPT` —
each shrink-only, each with a comment saying it should stay empty. They were **deleted**
along with the complexity baseline they were shaped like: an empty exemption list is a
place to put the next offender. Every population they were built for was brought onto a
rail instead of being recorded:

- Ruff and pyright reach all 698 tracked Python files.
- `.pi/extensions/tsconfig.json` was added as the rail for the Pi harness extension.
- `tsconfig.driver.json` covers the Playwright/perf driver layer, and `panda.config.ts`
  joined `tsconfig.node.json`.

A file that genuinely cannot be gated is a change to a rail, not a line in a list. Each of
the four failure messages says so explicitly ("There is no allowlist to record it in").

## Code Commentary

### Logic

Four tests across two classes.

**`PythonGateScopeTests`**

- `test_every_tracked_python_file_is_linted_and_type_checked` — `wrapper_steps()` calls
  `check.derive_scope(REPO_ROOT)`, builds a real `CheckConfig`, and asks
  `check.quality_steps` for the actual `Step` objects. The assertion is made against the
  real `ruff` and `pyright` **argument vectors**, not against the `GateScope` dataclass
  that produced them — a scope that is declared but not passed to a tool is not a scope.
  The failure reports a mapping of path → the rails that missed it.
- `test_python_coverage_and_test_rails_reach_their_trees` — pins
  `scope.coverage_paths == [Path("mcp/src/agents_remember")]` (so a change to the tracked
  top-level package set is noticed, because coverage and CRAP scope move with it) and
  asserts pytest's `testpaths` reaches every tracked `mcp/tests/**/*.py`.

**`TypeScriptGateScopeTests`**

The frontend rail lives in per-directory `eslint.config.*` and `tsconfig*.json` files, so
those are read from the tree too. `typescript_lint_roots` treats a tracked
`eslint.config.*` as marking its own directory (ESLint flat config applies to the
directory it sits in). `typescript_type_roots` (`@cache`) builds include/exclude matchers
from every tracked `tsconfig*.json`; a bare entry (`"src"`, `"vite.config.ts"`) is matched
literally **and** as a directory prefix, matching how TypeScript reads a directory entry
versus a file entry.

`glob_to_regex` translates TypeScript's glob vocabulary (`**`, `*`, `?`) by hand because
`fnmatch`'s `*` crosses `/`, which would silently widen every pattern and make the module
claim coverage it does not have.

- `test_every_tracked_typescript_file_is_on_a_frontend_rail` — satisfied by **either** lint
  or type-check.
- `test_every_linted_typescript_file_is_also_type_checked` — the stricter rail, kept
  separate. "Linted but never type-checked" is the same shape of gap as the Python scope
  hole this leaf closed. `untyped_typescript_paths` deliberately **excludes** files on no
  rail at all, so one fix never produces two failures.

### Invariants And Boundaries

- The scope assertion is made against the wrapper's real argument vectors. Changing
  `derive_scope` without changing what the steps receive will not fool this module.
- This module recomputes `git ls-files` itself rather than reusing `check.git_ls_files`,
  so a bug in the derivation cannot hide inside the test that checks the derivation.
- No allowlist, no exemption constant, no reason string. Reintroducing one reintroduces the
  pattern the leaf removed.
- The `.ts`/`.tsx` rail and the type-check rail are asserted separately and both must be
  empty.

### Todos

None known for this leaf.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The derivation under test, and the `Step`/`GateScope`/`CheckConfig` types this module builds real commands from. | `derive_scope` | mcp/src/agents_remember/code_quality/check.py:54-55 |
| Complementary wrapper-side tests that scope is derived rather than written down, and that an out-of-package script reaches both rails. | `GateScopeDerivationTests` | mcp/tests/test_code_quality_check.py:514-700 |
| The frontend rails this module reads: eslint flat configs and tsconfig projects. | `tseslint` | dashboard/eslint.config.js:1-12; dashboard/tsconfig.json:1-8 |
| The TypeScript rail added for the Pi harness extension so it needed no exemption. | `compilerOptions` | .pi/extensions/tsconfig.json:1-19 |

## Update History

- 2026-08-04T18:20+02:00 — 260731-EFA-L6 S18-B15 curator: resolved 8 citation findings and one stale
  count. Ruff and pyright reach all 698 tracked Python files (the card said 607). Re-anchored the four
  rows with exact spans: the derivation under test (`derive_scope`, check.py:54-180), the wrapper-side
  derivation tests (514-558), the frontend rails (eslint flat config + tsconfig projects), and the Pi
  extension tsconfig (1-19). Scoped recheck clean.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: **corrected**. The previous revision of
  this card documented three allowlists, their contents, `MINIMUM_REASON_LENGTH`, the
  40-character reason rule and `assert_allowlist_shrinks` / `AllowlistDisciplineTests`.
  None of that exists: the allowlists were deleted with the complexity baseline and every
  population was brought onto a rail. Card now describes the four tests that remain and
  states the no-allowlist rule. Verification metadata is pinned to the leaf's reformat
  commit until closeout stamps the code commit.
- 2026-07-31T06:30+02:00 — 260731-EFA-L2 created the scope-coverage test (requirements
  L2-R10 and L2-R11), mid-leaf, while the allowlists still stood.
