# mcp/src/agents_remember/providers/lifecycle/runtime_environment.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/runtime_environment.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f` |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Overview](overview.md)

## Purpose

`runtime_environment.py` owns small runtime environment defaults used by
provider lifecycle commands.

## Code Commentary

### Logic

The module infers the coordination root from the installed package
location, configures stdout/stderr for UTF-8, and builds subprocess
environments that force UTF-8 Python IO.

### Invariants And Boundaries

- Environment helpers are provider-agnostic.
- Command execution belongs in `command_runner.py`; this module only supplies
  environment defaults.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The lifecycle CLI uses these root and stdio helpers. | [cli.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/cli.py) |
| Command execution uses the subprocess environment helper. | [command_runner.py](agents-remember/mcp/src/agents_remember/providers/lifecycle/command_runner.py) |

## Update History

- 2026-05-31T12:30+02:00 — Dropped runtime_root_from_script; Logic now describes only the coordination root inference (1.0.0 review remediation).
- 2026-05-25T21:14+02:00: Created from the environment portion of the former shared lifecycle common module.
