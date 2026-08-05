# mcp/src/agents_remember/providers/cgc/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The package overview describes the provider-owned CGC route. | `# mcp/src/agents_remember/providers/cgc/ - CodeGraphContext Provider Overview` | onboarding/mcp/src/agents_remember/providers/cgc/overview.md:1-151 |

## Update History

- 2026-08-02T21:13:32+02:00 — 260731-EFA-L6 curator W2-B10: repaired 2 citation findings (1 reference row); scoped recheck clean.

- 2026-05-25T21:14+02:00: Created for the provider-first module layout.
