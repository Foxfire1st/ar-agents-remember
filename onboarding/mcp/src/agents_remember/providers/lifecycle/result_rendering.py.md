# mcp/src/agents_remember/providers/lifecycle/result_rendering.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/result_rendering.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`result_rendering.py` owns text/JSON rendering for provider lifecycle command
results.

## Code Commentary

### Logic

The module renders plain lifecycle result fields, streams captured native
command output without wrapping it, compacts CGC/GrepAI run results into API
payloads, and routes dry-run versus live command rendering.

### Invariants And Boundaries

- Captured command stdout/stderr must be streamable as native output for run
  actions.
- Rendering helpers must not perform lifecycle mutations.
- GrepAI run rendering intentionally mirrors CGC run rendering.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The lifecycle CLI delegates result display to this module. | [cli.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle/cli.py) |
| Provider lifecycle tests verify native captured output streaming. | [test_provider_lifecycle.py](agents-remember-md/mcp/tests/test_provider_lifecycle.py) |

## Update History

- 2026-05-25T21:14+02:00: Created from the rendering portion of the former shared lifecycle common module.
