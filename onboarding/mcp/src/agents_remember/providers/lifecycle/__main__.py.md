# mcp/src/agents_remember/providers/lifecycle/__main__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/__main__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`__main__.py` keeps `python -m agents_remember.providers.lifecycle` working
after `providers.lifecycle` changed from a module file into a package facade.

## Code Commentary

### Logic

The entrypoint imports `main` from the lifecycle package facade and exits with
that command's return code.

### Invariants And Boundaries

- CLI argument parsing stays in `cli.py`.
- This file is only the package execution adapter.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The lifecycle CLI parser and main function live in `cli.py`. | [cli.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/cli.py) |

## Update History

- 2026-05-25T21:14+02:00: Created when `providers.lifecycle` became a package facade.
