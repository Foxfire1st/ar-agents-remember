# mcp/src/agents_remember/providers/lifecycle/result_rendering.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/result_rendering.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T21:14+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle CLI delegates result display to this module. | `render_cli_result` | mcp/src/agents_remember/providers/lifecycle/cli.py:333-341 |
| Provider lifecycle tests verify native captured output streaming. | `ProviderLifecycleRenderTests` | mcp/tests/test_provider_lifecycle.py:30-107 |

## Update History

- 2026-08-02T17:12:10+02:00 — W1-B04 curator: repaired 2 citation claims; scoped recheck clean (0 findings).

- 2026-05-25T21:14+02:00: Created from the rendering portion of the former shared lifecycle common module.
