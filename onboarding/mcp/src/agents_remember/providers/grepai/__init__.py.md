# mcp/src/agents_remember/providers/grepai/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/grepai/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[GrepAI Provider Overview](overview.md)

## Purpose

This package marker establishes `providers.grepai` as the provider-owned home
for GrepAI setup, context, and lifecycle modules.

## Code Commentary

### Logic

The file intentionally exports no runtime behavior. Callers import concrete
modules such as `providers.grepai.setup`, `providers.grepai.context`, or
`providers.grepai.lifecycle`.

### Invariants And Boundaries

- GrepAI implementation remains under this package and stays Docker-owned.
- Do not add provider orchestration to this marker file.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The package overview describes the provider-owned GrepAI route. | `# mcp/src/agents_remember/providers/grepai/ - GrepAI Provider Overview` | onboarding/mcp/src/agents_remember/providers/grepai/overview.md:1-117 |

## Update History

- 2026-08-02T16:45:41+02:00 — 260731-EFA-L6 curator W1-B10: repaired 2 citation findings (1 row); scoped recheck clean.

- 2026-05-25T21:14+02:00: Created for the provider-first module layout.
