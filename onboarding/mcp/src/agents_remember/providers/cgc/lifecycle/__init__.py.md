# mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/__init__.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `2e2117a194ab1576c860dbca39b6acff0d1c20fa` |
| lastVerifiedCommitDate | 2026-05-26T14:55:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`cgc.py` is the CodeGraphContext lifecycle export facade. It groups the split
CGC implementation modules behind one import surface for `providers.lifecycle`.

## Code Commentary

### Logic

The module re-exports CGC backend, core settings/layout, runner, installation,
process-control, refresh, and query lifecycle functions. It intentionally
contains no behavior beyond those exports.

### Invariants And Boundaries

- Keep this module import-only.
- Put CGC implementation in the focused `cgc_*` modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The parent lifecycle facade imports this CGC facade. | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/__init__.py) |
| CGC core, backend, runner, install, process-control, refresh, and query modules make up the exported surface. | [core.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/core.py); [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py); [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py); [installation.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/installation.py); [process_control.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py); [refresh.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py); [query.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/query.py) |

## Update History

- 2026-05-26T12:51+02:00: Updated after exporting the CGC Docker runner lifecycle helpers.
- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created as the CodeGraphContext lifecycle export facade.
