# mcp/src/agents_remember/providers/cgc/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[CodeGraphContext Provider Overview](overview.md)

## Purpose

This package marker establishes `providers.cgc` as the provider-owned home for
CodeGraphContext setup, context, and lifecycle modules.

## Code Commentary

### Logic

The file intentionally exports no runtime behavior. Callers import concrete
modules such as `providers.cgc.setup`, `providers.cgc.context`, or
`providers.cgc.lifecycle`.

### Invariants And Boundaries

- Do not add provider orchestration to this marker file.
- Keep provider behavior in the named child modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package overview describes the provider-owned CGC route. | [overview.md](overview.md) |

## Update History

- 2026-05-25T21:14+02:00: Created for the provider-first module layout.
