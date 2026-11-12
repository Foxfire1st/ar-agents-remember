# mcp/tests/test_suite_budget.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves selected-case budget admission without recursive pytest collection.

## Code Commentary

### Logic

The parametrized `test_selected_case_budgets` drives the actual collection-finish hook with synthetic selected item populations: the declared 10,000 unit/2,000 integration pair passes, one unit case or one integration case above its own rail raises the explicit-tradeoff refusal. `STUB_UNIT`/`STUB_INTEGRATION` deliberately duplicate the declared pair, and `test_the_stub_matches_the_declared_pair` ties both constants to the root configuration so a stale mirror cannot keep proving an obsolete ceiling. The marker-shaped item double classifies already-collected items; no recursive pytest collection is spawned. The other checks pin the effective repository-root inifile and both runtime ini values, prohibit a `default=` on either ini declaration, and require an absent rail to resolve to 0 and refuse by name rather than run unbounded. These are enforcement boundaries, not an inventory scan or an execution-time measurement.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

There is **no per-declaration default budget to state.** `mcp/tests/conftest.py` registers the two ini names with `addini` and carries no `default=`; the enforced pair lives once, in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]`, and was **2300 unit / 400 integration** when this was written — read it there, it moves. The stub now follows the declared 10,000/2,000 pair; the 2300/400 figure above is only the dated reading, not a current input. The boundary proof and its tie to the declaration are separate checks. Coverage is diagnostic; production
CRAP 20 triggers review without failing delivery. Full suites and whole-candidate review occur at
master completion. A green unit result is not a certification certificate.

### Todos

Verification metadata remains closeout-owned; this card records source inspection only.

## Evidence

### Docs References

No Domain Documentation source is configured; this behavior is repository-owned.

No external domain claim is needed.

### Repo-Internal References


The exact functions below establish the tested boundary and its test doubles.

- Proves selected-case budget admission without recursive pytest collection, over a synthetic population. [1]
- Proves the enforced inifile and the running configuration's values are the root `pyproject.toml`'s own declarations. [2]




- Refuses a default on either budget declaration, so a dead number cannot return to the tree.  Anchor: `test_the_option_declarations_state_no_budget_of_their_own` [3]


- States that an absent rail resolves to `0` and is refused by name instead of running unbounded. [4]

### Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

No external boundary is claimed.



- The current root declaration is 10000 unit and 2000 integration; the synthetic stub and both guard-relative boundary cases follow it. [5]
