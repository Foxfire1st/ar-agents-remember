# mcp/src/agents_remember/providers/lifecycle_modules/cgc/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle_modules/cgc/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cgc.py` is the CodeGraphContext lifecycle export facade. It groups the split
CGC implementation modules behind one import surface for `providers.lifecycle`.

## Code Commentary

### Logic

The module re-exports CGC backend, core settings/layout, installation/patching,
and process lifecycle functions. It intentionally contains no behavior beyond
those exports.

### Invariants And Boundaries

- Keep this module import-only.
- Put CGC implementation in the focused `cgc_*` modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports this CGC facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |
| CGC core, backend, install, and process modules make up the exported surface. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/core.py); [backend.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/backend.py); [installation.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/installation.py); [process.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle_modules/cgc/process.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created as the CodeGraphContext lifecycle export facade.
