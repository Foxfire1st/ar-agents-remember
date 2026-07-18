# mcp/tests/conftest.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/conftest.py`                    |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-18T20:03+02:00                     |
| lastVerifiedCommitHash | `7ca29c3b6dd2c0184253e2690f1ebe78c511573b` |
| lastVerifiedCommitDate | 2026-07-18T20:18:51+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`conftest.py` provides session-wide pytest bootstrap that pins imports to the candidate checkout,
scrubs ambient Git repository selection before fixtures run, and supplies fallback commit identity
for throwaway repositories.

## Code Commentary

### Logic

At collection time the bootstrap removes previously imported `agents_remember` modules and places
the current worktree's `mcp/src` first on `sys.path`. It imports
`GIT_REPOSITORY_SELECTOR_ENV` from production `kernel.git_command` and removes every selector from
the process environment before a fixture can spawn Git. It then uses `setdefault` for test-only
author/committer identity so an explicit caller identity remains authoritative.

### Conventions

The production selector tuple is the sole inventory. Tests must import it rather than maintaining a
parallel list that could omit a newly supported selector.

### Invariants And Boundaries

- Selector cleanup runs at module import before fixture construction or test collection can execute
  repository commands.
- Fixture Git calls use explicit temporary `cwd`; ambient selectors may not redirect them into a
  real repository.
- Checkout-source pinning ensures verification exercises the candidate, not a sibling editable
  installation.
- Fallback identity applies only to temporary fixture commits and never overwrites an exported
  identity.

### Todos

None known for the MX-FIX-4 test bootstrap.

## Docs References

No Domain Documentation source is configured for this repository; the bootstrap mirrors production
Git isolation directly.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Production owns the eight-selector inventory and scrubbed Git environment. | L9-L42 | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| Route-index tests independently contaminate each selector and require identical output. | L595-L644 | [test_route_index.py](agents-remember/mcp/tests/test_route_index.py) |
| Worktree fixtures create and commit temporary code/memory repositories. | fixture setup | [test_worktree_support.py](agents-remember/mcp/tests/test_worktree_support.py) |

## Cross-Repo References

No sibling repository defines the pytest bootstrap contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: replaced the duplicated Git selector list with the
  production `GIT_REPOSITORY_SELECTOR_ENV` inventory and corrected the nearest governing overview.
- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added the worktree-local source/import pin so pytest
  cannot silently exercise a sibling editable install. Verification remains pinned until closeout.
- 2026-07-03T02:58+02:00 — No content impact: L13 reopen drill second cycle extended the marker
  comment; the reopened leaf ran under its original id with a fresh lifecycle.
- 2026-07-03T02:40+02:00 — No content impact: L13 reopen drill appended a marker comment; the drill
  exercised task-reopen mechanics, not fixture behavior.
- 2026-05-30T23:59+02:00 — Created after inherited `GIT_DIR` redirected temporary fixture commands;
  the import-time guard strips repository selectors and supplies fallback identity.
