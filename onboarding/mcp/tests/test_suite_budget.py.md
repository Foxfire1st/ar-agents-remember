# mcp/tests/test_suite_budget.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves selected-case budget admission without recursive pytest collection.

## Code Commentary

### Logic

Four cases, and they now split the two things the old version of this module ran together. `test_selected_case_budgets` is the parametrized one: it feeds the actual collection-finish hook a **synthetic** selected item population — 1000 unit/250 integration passes, 1001 unit or 251 integration raises the refusal requiring an explicit tradeoff — so those two numbers are the *test's inputs*, deliberately not the repository's rails, and the marker-shaped item double classifies each already-collected item. Three further cases pin the rail itself: `test_the_effective_budgets_are_the_repository_rails` asserts that the running configuration's `inifile` **is** the repository-root `pyproject.toml` and that the two ini values equal the root file's own declarations, reading the enforced configuration rather than either file's text; `test_the_option_declarations_state_no_budget_of_their_own` walks `conftest.py`'s AST and refuses a `default=` on either `addini` declaration, so the dead number cannot come back; and `test_an_absent_rail_refuses_by_name_instead_of_running_unbounded` states that an absent rail resolves to `0` and is refused by the `budget < 1` guard rather than read as "no ceiling". This is boundary arithmetic and refusal evidence, not a second inventory scan or a real nested pytest session.

### Conventions

These are focused unit cases under the canonical evidence-lane manifest. Reuse their behavior
boundary when changing policy rather than adding duplicate metric or collection assertions.

### Invariants And Boundaries

There is **no per-declaration default budget to state.** `mcp/tests/conftest.py` registers the two ini names with `addini` and carries no `default=`; the enforced pair lives once, in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]`, and was **2300 unit / 400 integration** when this was written — read it there, it moves. The 1000/250 figures inside the parametrized case are that case's own inputs. Coverage is diagnostic; production
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
- Refuses a `default=` on either budget declaration, so a dead number cannot return to the tree. [3]
- States that an absent rail resolves to `0` and is refused by name instead of running unbounded. [4]

### Cross-Repo References

No cross-repository protocol is exercised by these unit cases.

No external boundary is claimed.
