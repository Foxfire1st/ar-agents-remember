# test_cgc_index_concurrency.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_cgc_index_concurrency.py`  |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_cgc_index_concurrency.py` protects the `cgc_index_concurrency` fan-in
cap that prevents a multi-repo workspace from overwhelming the shared FalkorDB
query queue during `reindex-all`. Tests confirm default capping, env-override
behaviour, and all boundary conditions (zero repos, env exceeds repo count,
non-integer env).

## Code Commentary

### Logic

`IndexConcurrencyTests` calls `cgc_index_concurrency(n)` with various repo
counts and `AR_CGC_INDEX_CONCURRENCY` env-var values:

- `test_default_caps_below_repo_count`: without the env var, 8 repos → `DEFAULT_CGC_INDEX_CONCURRENCY` (2).
- `test_never_exceeds_repo_count`: env=10, repos=3 → capped at 3.
- `test_at_least_one`: env=0 or env=1 with 5 repos → 1.
- `test_env_override_raises_cap`: env=6, repos=20 → 6.
- `test_bad_override_falls_back_to_default`: env="lots" → `DEFAULT_CGC_INDEX_CONCURRENCY`.
- `test_zero_layouts_returns_one`: env=4, repos=0 → 1 (never zero workers).

All tests use `mock.patch.dict` to isolate env state.

### Conventions

No Docker, FalkorDB, or network access required. Tests call the pure function
directly after clearing or overriding the env var.

### Invariants And Boundaries

The tests protect that: the cap defaults to 2 so a large workspace degrades
to "slower" instead of breaking; the cap is never zero; the cap never exceeds
the number of repos; an invalid env var is silently ignored in favour of the
default.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `cgc_index_concurrency` and `DEFAULT_CGC_INDEX_CONCURRENCY` live in the CGC process-control module. | [process_control.py](agents-remember/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-01T00:00+02:00 — Created onboarding for the new CGC index-concurrency fan-in cap tests.
