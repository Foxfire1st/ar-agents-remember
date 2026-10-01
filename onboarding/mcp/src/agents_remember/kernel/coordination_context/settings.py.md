# mcp/src/agents_remember/kernel/coordination_context/settings.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`settings.py` is the settings-selection facade for the `c-08-ar-coordination-context-resolver` skill implementation
package.

## Code Commentary

### Logic

`parse_coordination_settings()` builds fallback storage/cross-repo settings,
prefers a sibling `settings.json` when present, and otherwise scans fenced
Markdown settings blocks. The module also re-exports parser helpers used by the
public resolver facade.

### Invariants And Boundaries

- JSON settings remain the preferred machine-readable source.
- Missing settings files produce default storage/cross-repo settings rather
  than failing context resolution.
- Concrete JSON, Markdown, and scalar parsing details live in focused modules.

## Evidence

### Docs References

No external documentation is needed for this package-local settings selector.

No relevant external documentation is needed.

### Repo-Internal References

- JSON parsing owns the preferred settings format. [1]
- Markdown parsing owns the legacy fenced-settings fallback and invokes the parser body. [2]
- The settings facade prefers sibling JSON and otherwise scans fenced Markdown through `parse_coordination_settings`. [3]

### Cross-Repo References

No cross-repository evidence is needed for settings selection.

No meaningful cross-repo references found.
