# mcp/tests/conftest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/conftest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:51:32+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
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
invalid or exceeded budgets. Pyproject supplies the operative 1000 unit/150 integration values;
the parser’s standalone integration fallback is 100, so it must not be mistaken for repository policy.

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
| Budget config and explicit certification option | `pytest_addoption` | mcp/tests/conftest.py:72-81 |
| Single lane read and genuine certification admission | `pytest_configure` | mcp/tests/conftest.py:84-107 |
| Skip integration imports for default units | `pytest_ignore_collect` | mcp/tests/conftest.py:110-117 |
| Selected item budgets and explicit tradeoff refusal | `pytest_collection_finish` | mcp/tests/conftest.py:127-138 |
| Explicit bind/reset application composition | `worktree_services` | mcp/tests/conftest.py:151-163 |
| Restore environment and remove temporary root | `pytest_unconfigure` | mcp/tests/conftest.py:166-170 |

## Cross-Repo References

No separate cross-repository authority is established by this file.

## Update History

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
