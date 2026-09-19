# mcp/tests/conftest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/conftest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:02+02:00 |
| lastVerifiedCommitHash | `f05ba167cd6dfb56b48a775f3da5d45528c09c82`|
| lastVerifiedCommitDate | 2026-09-18T17:19:31+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l4-ar` uncommitted source; base `0dd04d6adbca3e8ba61849b605ece3137005829e` |
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
| Budget config and explicit certification option | `pytest_addoption` | mcp/tests/conftest.py:88-102 |
| Single lane read and genuine certification admission | `pytest_configure` | mcp/tests/conftest.py:105-128 |
| Skip integration imports for default units | `pytest_ignore_collect` | mcp/tests/conftest.py:131-138 |
| Selected item budgets and explicit tradeoff refusal | `pytest_collection_finish` | mcp/tests/conftest.py:148-159 |
| Explicit bind/reset application composition | `worktree_services` | mcp/tests/conftest.py:172-184 |
| Restore environment and remove temporary root | `pytest_unconfigure` | mcp/tests/conftest.py:187-191 |

## Cross-Repo References

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

## Update History
- 2026-09-18T17:02+02:00 — 260918-TSIP-L4 curator (uncommitted change set on `ar/260918-tsip-l4-ar`, base `0dd04d6a`): the `evidence_lanes` plugin registered (`T48`), the Git-checkout consequence stated, and the card's own pyproject-budget paragraph corrected to 2000/300 against the parser's 1100/300 defaults (`T45`). Verification metadata stays at the recorded verification because the candidate is uncommitted and the governed closeout owns the real code commit; `lastUpdated` advances with this body edit.
- 2026-09-18T14:49:10+00:00: Generated citation repair: `pytest_addoption` repointed to mcp/tests/conftest.py:88-97. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: `pytest_ignore_collect` repointed to mcp/tests/conftest.py:126-133. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: `pytest_collection_finish` repointed to mcp/tests/conftest.py:143-154. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T14:49:10+00:00: Generated citation repair: `pytest_unconfigure` repointed to mcp/tests/conftest.py:182-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 4fb0a4d92072964079a2a144c1f1da15ff07327804a09730959bc69f38a7e98f; claim bytes unchanged; generated by ccr-r10@v1.

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
