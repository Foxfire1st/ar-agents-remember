# mcp/src/agents_remember/kernel/coordination_context/json_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/json_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`json_settings.py` parses machine-readable `c-08-ar-coordination-context-resolver` skill settings from
`settings.json`.

## Code Commentary

### Logic

The module validates the settings JSON root, applies storage mode/defaults,
parses path rules with include/exclude paths and file types, and parses
`crossRepo.allow` through shared setting-value helpers. It supports the current
`onboarding` wrapper shape while still accepting root-level settings keys.

### Invariants And Boundaries

- JSON settings are the preferred machine-readable source when present beside
  `settings.md`.
- Validation errors are explicit and path-rule parsing does not perform
  filesystem or Git checks.

## Docs References

No external documentation is needed for this project settings parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Settings selection prefers this JSON parser before Markdown fallback. | settings selector | [settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/settings.py) |
| Example settings exercise storage path rules and cross-repo configuration shape. | settings fixture | [settings.example.json](agents-remember-md/examples/mcp/settings.example.json) |
| Resolver parity tests cover JSON settings output shape. | resolver tests | [test_resolver_parity.py](agents-remember-md/mcp/tests/test_resolver_parity.py) |

## Cross-Repo References

No cross-repository evidence is needed for this settings parser.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting JSON settings parsing from the `c-08-ar-coordination-context-resolver` skill resolver.
