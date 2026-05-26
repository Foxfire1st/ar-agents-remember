# mcp/src/agents_remember/providers/cgc/lifecycle/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/lifecycle/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:09+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`core.py` owns CodeGraphContext lifecycle settings and layout derivation.

## Code Commentary

### Logic

The module resolves CGC runtime layout from either settings-backed provider
roots or manual CLI overrides, validates configured roots, selects the active
root by repo ID, and derives managed backend settings such as FalkorDB image,
ports, data roots, container name, and image lock path.

### Invariants And Boundaries

- Settings-backed CGC commands must select configured roots from provider
  settings rather than guessing repository paths.
- Backend settings must be concrete before Docker lifecycle code uses them.
- This module should not start processes or containers.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC backend container lifecycle consumes backend settings from this module. | [backend.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/backend.py) |
| CGC lifecycle actions consume the selected runtime layout from this module. | [process_control.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py); [refresh.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/refresh.py); [query.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/query.py) |

## Update History

- 2026-05-25T19:09+02:00: Moved into the provider-specific subpackage and dropped the filename prefix while preserving behavior.
- 2026-05-25T19:01+02:00: Created from CGC settings and layout logic extracted out of provider lifecycle.
