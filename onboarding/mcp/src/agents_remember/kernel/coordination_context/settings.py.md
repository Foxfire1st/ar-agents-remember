# mcp/src/agents_remember/kernel/coordination_context/settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external documentation is needed for this package-local settings selector.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| JSON parsing owns the preferred settings format. | `parse_json_settings` | mcp/src/agents_remember/kernel/coordination_context/json_settings.py:25-40 |
| Markdown parsing owns the legacy fenced-settings fallback and invokes the parser body. | `parse_settings_block`; `parse` | mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py:34-38; mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py:68-77 |
| The settings facade prefers sibling JSON and otherwise scans fenced Markdown through `parse_coordination_settings`. | `parse_coordination_settings` | mcp/src/agents_remember/kernel/coordination_context/settings.py:50-72 |

## Cross-Repo References

No cross-repository evidence is needed for settings selection.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: anchored the JSON, Markdown, and resolver consumers of the settings facade, including the Markdown parser body and JSON-first fallback branch.
- 2026-05-25T20:57+02:00: Created as the JSON-first settings facade after parser details moved into focused modules.
