# mcp/src/agents_remember/providers/lifecycle/state_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/state_files.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`state_files.py` owns JSON state file reads and writes for provider lifecycle
modules.

## Code Commentary

### Logic

The module returns an empty dict for absent JSON state files and writes
deterministic, sorted, indented JSON with a trailing newline.

### Invariants And Boundaries

- State file helpers do not interpret provider state.
- Callers own schema decisions and error handling around loaded data.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC and GrepAI lifecycle modules use these helpers for provider state and image locks. | [cgc backend](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py); [grepai backend](agents-remember-md/mcp/src/agents_remember/providers/grepai/lifecycle/backend.py) |
| Provider settings reads reuse the JSON loader. | [provider_settings.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/provider_settings.py) |

## Update History

- 2026-05-25T21:14+02:00: Created from the JSON state portion of the former shared lifecycle common module.
