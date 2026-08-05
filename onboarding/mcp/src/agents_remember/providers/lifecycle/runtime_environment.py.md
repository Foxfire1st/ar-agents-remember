# mcp/src/agents_remember/providers/lifecycle/runtime_environment.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/runtime_environment.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle CLI uses these root and stdio helpers. | ["default=default_coordination_root()", "configure_utf8_stdio()"] | mcp/src/agents_remember/providers/lifecycle/cli.py:47-47; mcp/src/agents_remember/providers/lifecycle/cli.py:345-345 |
| Command execution uses the subprocess environment helper. | ["subprocess_env(None)"] | mcp/src/agents_remember/providers/lifecycle/command_runner.py:25-25 |

## Update History

- 2026-08-02T20:45:43+02:00 — L6 W2-B02 curator: anchored 2 repository-internal references for lifecycle CLI environment setup and command execution; final scoped result 0 (checker-clean).

- 2026-05-31T12:30+02:00 — Dropped runtime_root_from_script; Logic now describes only the coordination root inference (1.0.0 review remediation).
- 2026-05-25T21:14+02:00: Created from the environment portion of the former shared lifecycle common module.
