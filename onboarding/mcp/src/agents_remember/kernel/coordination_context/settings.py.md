# mcp/src/agents_remember/kernel/coordination_context/settings.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/settings.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| JSON parsing owns the preferred settings format. | JSON parser | [json_settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/json_settings.py) |
| Markdown parsing owns legacy fenced settings fallback. | Markdown parser | [markdown_settings.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/markdown_settings.py) |
| Resolver assembly calls this selector before building the final context. | resolver | [resolver.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/resolver.py) |

## Cross-Repo References

No cross-repository evidence is needed for settings selection.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created as the JSON-first settings facade after parser details moved into focused modules.
