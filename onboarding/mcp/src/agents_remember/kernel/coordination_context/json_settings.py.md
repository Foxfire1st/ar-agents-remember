# mcp/src/agents_remember/kernel/coordination_context/json_settings.py

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

## Evidence

### Docs References

No external documentation is needed for this project settings parser.

No relevant external documentation is needed.

### Repo-Internal References

- Settings selection prefers this JSON parser before Markdown fallback. [1]
- The example settings file demonstrates the JSON coordination-root storage shape. [2]
- JSON settings parsing composes current typed storage, path-rule and cross-repository settings. [3]

### Cross-Repo References

No cross-repository evidence is needed for this settings parser.

No meaningful cross-repo references found.
