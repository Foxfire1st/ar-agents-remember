# mcp/src/agents_remember/providers/lifecycle/__main__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/__main__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle CLI parser and main function live in `cli.py`. | `build_parser`; `main` | mcp/src/agents_remember/providers/lifecycle/cli.py:172-267; mcp/src/agents_remember/providers/lifecycle/cli.py:344-359 |

## Update History

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 1 citation item; scoped citation check now passes.

- 2026-05-25T21:14+02:00: Created when `providers.lifecycle` became a package facade.
