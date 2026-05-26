# mcp/src/agents_remember/kernel/coordination_context/serialize.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/serialize.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T20:57+02:00                     |
| lastVerifiedCommitHash | `c310611a6678051c9e37b912c522b367530c0686` |
| lastVerifiedCommitDate | 2026-05-26T02:17:03+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`serialize.py` owns JSON-safe and text formatting for resolved coordination
contexts.

## Code Commentary

### Logic

The module converts `CoordinationContext`, storage rules, and cross-repo
entries into dictionaries with string paths and stable keys. `print_text()`
emits the legacy tab-separated text format used by the CLI.

### Invariants And Boundaries

- Serialization does not resolve paths or mutate context; it formats already
  resolved model instances.
- Empty optional paths serialize as empty strings in JSON output, preserving the
  old resolver contract.

## Docs References

No external documentation is needed for this local formatter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The CLI delegates JSON/text output to this module. | CLI adapter | [cli.py](agents-remember-md/mcp/src/agents_remember/kernel/coordination_context/cli.py) |
| Controllers consume `context_to_dict()` through the public facade. | context packet controller | [context_packet.py](agents-remember-md/mcp/src/agents_remember/controllers/context_packet.py) |

## Cross-Repo References

No cross-repository evidence is needed for this formatter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-25T20:57+02:00: Created by extracting C-08 JSON/text serialization from the monolithic resolver.
