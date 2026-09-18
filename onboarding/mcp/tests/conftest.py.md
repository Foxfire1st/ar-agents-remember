# mcp/tests/conftest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/conftest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25`|
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate paths and disposable scrubbed environment | `REPOSITORY_ROOT` | mcp/tests/conftest.py:15-68 |
| Budget config and explicit certification option | `pytest_addoption` | mcp/tests/conftest.py:72-86 |
| Single lane read and genuine certification admission | `pytest_configure` | mcp/tests/conftest.py:89-112 |
| Skip integration imports for default units | `pytest_ignore_collect` | mcp/tests/conftest.py:115-122 |
| Selected item budgets and explicit tradeoff refusal | `pytest_collection_finish` | mcp/tests/conftest.py:132-143 |
| Explicit bind/reset application composition | `worktree_services` | mcp/tests/conftest.py:156-168 |
| Restore environment and remove temporary root | `pytest_unconfigure` | mcp/tests/conftest.py:171-175 |

## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History

- 2026-09-18T18:52+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **corrected the one sentence that stated this file's budget declaration, and re-derived the seven citation ranges the delivery moved.** `260915-KS-L23`'s item 12 (worker W1) removed the two never-effective `default=1100/300` declarations from `pytest_addoption`: the parser now only **registers** `unit_case_budget` and `integration_case_budget` by `addini`, with no `default=`, and the comment beside them states that the rails live once in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]` because `mcp/pyproject.toml` declares no `[tool.pytest.ini_options]` (D-20). The card said the opposite in three ways at once — "Pyproject supplies the operative 1100 unit/300 integration values", "the parser's standalone defaults are those same declared values", "a direct `pytest_addoption` read cannot disagree with repository policy" — and every clause is now false: the values are **2300 / 400**, and there are no parser defaults to agree or disagree with. The paragraph now states the registration/no-default rule, where the pair actually lives, that it moves, and the guard's `budget < 1` half that makes an absent rail fail closed. **The seven reference rows were re-derived by AST from the delivered file** (`pytest_addoption` `:72-86`, `pytest_configure` `:89-112`, `pytest_ignore_collect` `:115-122`, `pytest_collection_finish` `:132-143`, `worktree_services` `:156-168`, `pytest_unconfigure` `:171-175`) — the last of them **was anchor-absent from its old `:166-170` range**, so this repair also clears a live citation finding rather than only a stale number. Content was read against the delivered but **uncommitted** working tree, so **the verification stamp is not advanced**: no commit carries this file's current bytes and closeout stamps the real code commit. No other claim in this card was re-read in this pass.
- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-08-28T11:32+02:00 — No content impact: shortened a stale explanatory comment; collection,
  lane classification, and Dagger admission behavior are unchanged.

- 2026-08-28T10:03:40+02:00 — Reconciled the current certifying composition after Candidate A
  retirement; no host Python entrypoint or compatibility bypass remains.

- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T21:23+02:00 — 260824-PDLS replaced the monolithic root guard/fixture implementation
  with explicit admission, hermetic bootstrap, shared hooks, and certifying-only service composition.
- 2026-08-10T18:31+02:00 — The predecessor established explicit checkout test mode and owned-global
  restoration; that still-valid behavior moved to production testing modules.
- 2026-08-05T00:00+02:00 — The predecessor established Dagger-only collection, candidate path/Git
  isolation, disposable identity, cache isolation, deterministic order, and service binding; PDLS
  preserves those contracts behind separate owners.
