# mcp/tests/conftest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/conftest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T11:32+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Defines only the certifying pytest composition: pin the candidate checkout, require Dagger
admission, activate the reusable hermetic environment, declare the test process, then load the
certifying-only plugin, which in turn loads the shared route-neutral plugin. Ordinary raw host
pytest refuses. Candidate A's former direct entrypoint was deleted, so no supported Python route
avoids this certifying composition from the host.

## Code Commentary

### Logic

Before the first production import, the module derives `REPOSITORY_ROOT` and puts that candidate's
`mcp/src` first on `sys.path`. Because this happens before any `agents_remember` import, an
editable-install path cannot make the certifying process validate one checkout and collect another.

`prepare_certifying_pytest_bootstrap` translates admission/bootstrap failures into
`pytest.UsageError` before plugin loading or collection. The resulting `CERTIFYING_BOOTSTRAP`
contains the private admission capability and candidate process. `activate_current_pytest_environment`
scrubs Git repository selectors and installs the disposable Git identity plus candidate
`PYTHONPATH` in the current process; its lease records the prior values for exact restoration.
`begin_pytest_process` declares test mode before the plugins are imported.

The root `pytest_plugins` tuple loads
`agents_remember_test_support.testing.pytest_certifying_bootstrap`. That certifying-only plugin binds worktree
services and declares `agents_remember_test_support.testing.pytest_bootstrap` as its own plugin. The shared
plugin then owns:

- route-neutral cache isolation;
- deterministic random-order hooks;
- per-test owned-state restoration and leak failure; and
- test-process cleanup.

At unconfigure, root composition closes the environment lease and restores the caller's exact
prior values. Shared-plugin cleanup ends test-process state; certifying fixtures reset bound
worktree services.

### Conventions

Root conftest is composition, not an implementation bucket. Admission lives in
`testing.dagger_admission`; candidate isolation in `testing.hermetic_bootstrap`; shared hooks in
`testing.pytest_bootstrap`; service fixtures in `testing.pytest_certifying_bootstrap`; and owned
state/randomization in their own testing modules.

### Invariants And Boundaries

- Candidate path pinning precedes every production import.
- Dagger admission precedes candidate planning, plugin loading, collection, execution, and artifact
  publication.
- Missing/malformed/mismatched admission is a certifying refusal, never a diagnostic route selector.
- No host Python diagnostic route or compatibility import bypasses this conftest.
- Git repository selectors and developer identity do not leak into fixture subprocesses.
- Environment and owned globals restore on every pytest exit path.
- No compatibility import of `code_quality.dagger_environment`, `_global_state`, or `_random_order`
  remains.

### Todos

None.

## Docs References

Repository-local design is explained in `docs/design/python-pytest-bootstrap.md`; no external domain
documentation defines this boundary.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate pinning precedes the first production import. | `REPOSITORY_ROOT`; `MCP_SRC` | mcp/tests/conftest.py:13-14 |
| Certifying composition translates failures before plugin loading. | `prepare_certifying_pytest_bootstrap`; `CERTIFYING_BOOTSTRAP` | mcp/tests/conftest.py:34-40; mcp/tests/conftest.py:43-43 |
| Only the certifying service plugin is loaded from root composition. | `pytest_plugins` | mcp/tests/conftest.py:53-53 |
| Current-process environment is restored at unconfigure. | `pytest_unconfigure` | mcp/tests/conftest.py:54-56 |
| Shared hooks own order, cache, state restoration, and process cleanup. | `reject_owned_global_state_leaks`; `pytest_collection_modifyitems`; `pytest_unconfigure` | mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:22-24; mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:41-44; mcp/test_support/agents_remember_test_support/testing/pytest_bootstrap.py:60-70 |

## Cross-Repo References

No sibling repository supplies or overrides pytest admission/bootstrap.


## PDLS Reconciliation

The certifying plugin path now targets the root `agents_remember_test_support.pytest_certifying_bootstrap`, avoiding execution of the testing package initializer before admission/bootstrap composition.

The test continues to exercise production-owned behavior. No diagnostic result is treated as
certifying evidence and no fallback or threshold exception was introduced.
## Update History

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
