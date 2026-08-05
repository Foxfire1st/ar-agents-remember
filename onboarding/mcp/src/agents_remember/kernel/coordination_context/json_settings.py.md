# mcp/src/agents_remember/kernel/coordination_context/json_settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/json_settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Settings selection prefers this JSON parser before Markdown fallback. | `parse_coordination_settings` | mcp/src/agents_remember/kernel/coordination_context/settings.py:50-72 |
| The example settings file demonstrates the JSON coordination-root storage shape. | "coordinationRoot" | examples/mcp/settings.example.json:3-3 |
| Resolver parity tests cover JSON settings output shape. | `test_external_memory_resolution_reports_expected_context` | mcp/tests/test_resolver_parity.py:57-74 |

## Cross-Repo References

No cross-repository evidence is needed for this settings parser.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-02T21:18:27+02:00 — 260731-EFA-L6 curator W2-B06: repaired 3 citation claims; removed the unsupported cross-repo clause and retained the supported coordination-root shape; scoped result 0 findings.

- 2026-05-25T20:57+02:00: Created by extracting JSON settings parsing from the `c-08-ar-coordination-context-resolver` skill resolver.
