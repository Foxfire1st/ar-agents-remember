# mcp/tests/conftest.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Composes ordinary isolated pytest and an explicit Dagger-only certification option. Default host unit/integration development is supported without pretending to be a lifecycle worker, MCP process or certifying executor.

## Code Commentary

### Logic

The candidate’s source and test-support roots are placed first on `sys.path`. Existing hermetic
bootstrap installs the actual pytest-process environment. A disposable HOME/XDG/CODEX tree and
isolated Git configuration prevent fixture subprocesses from inheriting the developer’s setup;
live opt-ins, spawn identity and credential variables are scrubbed before tests import product code.

The lane manifest is read once into an integration-file set. Default `not integration` collection
skips those files before importing them; collected integration members receive their marker.
`pytest_collection_finish` counts selected parametrized items directly and raises UsageError for
invalid or exceeded budgets — a budget below `1` is refused by that same guard, so an absent rail fails
closed instead of running unbounded. **The rails live once**, in the repository-root `pyproject.toml`
under `[tool.pytest.ini_options]` (`unit_case_budget` / `integration_case_budget`; they were 2300 / 400
when this was written — read them there, they move), which is the `inifile` pytest actually reads,
because `mcp/pyproject.toml` declares no `[tool.pytest.ini_options]`. `pytest_addoption` therefore only
**registers** the two ini names with `addini` and carries **no `default=`**: a default here would never
be in effect and would put a second, contradictory number in the tree for a terminal reader to find
(D-20), and with no default the `int` type default `0` is exactly what the guard refuses.

`--certify` explicitly requests genuine Dagger admission and then imports the certifying service
plugin. Ordinary integration tests bind/reset worktree services through their fixture; units request
that fixture only when necessary. Shared bootstrap owns test-state restoration. Unconfigure restores
the prior environment and removes the disposable tree.

### Invariants And Boundaries

- Direct host pytest is development feedback; it does not mint a certificate.
- Missing Dagger authority refuses `--certify`; no fake capability or role identity is supplied.
- Budget enforcement counts the selected population without a nested collection or source census.
- Unit collection avoids unnecessary application composition and integration imports.
- Explicit environment/global restoration and cleanup remain mandatory.

## Evidence

### Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

### Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

- Candidate paths and disposable scrubbed environment [1]
- Budget config and explicit certification option [2]
- Single lane read and genuine certification admission [3]
- Skip integration imports for default units [4]
- Selected item budgets and explicit tradeoff refusal [5]
- Explicit bind/reset application composition [6]
- Restore environment and remove temporary root [7]

### Cross-Repo References

No separate cross-repository authority is established by this file.

## 260918-TSIP-L4 — The Lane Hook Armed, And The Git-Checkout Requirement (`T48`)

`pytest_plugins` now registers **two** plugins: the existing
`agents_remember_test_support.testing.pytest_bootstrap` and the new
`agents_remember_test_support.testing.evidence_lanes` (**`:68-84`**, the tuple at `:81-84`). The
old single-line assignment at `:68` was replaced by a 13-line comment plus the tuple, so **every
line at or below the old `:69` moved `+16`** (`pytest_addoption` `72-81 → 88-97`,
`pytest_configure` `84-107 → 100-123`, `pytest_ignore_collect` `110-117 → 126-133`,
`pytest_collection_finish` `127-138 → 143-154`, `worktree_services` `151-163 → 167-179`,
`pytest_unconfigure` `166-170 → 182-186`; file **170 → 186 lines**).

`evidence_lanes` carries the hook that makes the lane manifest load-bearing:
`pytest_collection_modifyitems` calls `load_lane_manifest` and raises `pytest.UsageError` when it
refuses. The hook was defined but never registered, so no run on this repository had ever asked
the loader its verdict (`T48`). `mcp/tests/test_evidence_lanes.py` now asserts the registration, so
it cannot be dropped again silently.

**A consequence, reported rather than hidden: with the hook armed, collection requires a Git
checkout.** `load_lane_manifest` enumerates the population through `git ls-files`, so an exported
(`git archive`/tarball) tree fails collection with `ScopeError … fatal: not a git repository`
instead of running. Git is already a prerequisite of the delivery path
(`code_quality/scope.py` scopes by index and diff, `quality_plan.py` runs in a worktree), and
`git init && git add -A` restores an exported tree. The requirement is now stated where an operator
reads test policy — `docs/design/python-pytest-bootstrap.md:22-24` — as well as at this
registration site.

**The card's own budget paragraph was wrong and is corrected above.** `pyproject.toml` now declares
`unit_case_budget = 2000` (`:168`) and `integration_case_budget = 300` (`:176`), not "1100
unit/300"; and the parser's standalone `addini` defaults in this file are **1100 unit / 300
integration**, so they are *not* the declared values and a direct `pytest_addoption` read disagrees
with repository policy by 900 unit cases. Found by the `T45` grep, not by any check.
