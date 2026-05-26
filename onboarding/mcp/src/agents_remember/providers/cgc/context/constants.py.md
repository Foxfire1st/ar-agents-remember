# mcp/src/agents_remember/providers/cgc/context/constants.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/constants.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T13:58+02:00                     |
| lastVerifiedCommitHash | `2e2117a194ab1576c860dbca39b6acff0d1c20fa` |
| lastVerifiedCommitDate | 2026-05-26T14:55:50+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/constants.py` owns CGC provider identifiers, pins, Docker runner image,
watcher naming defaults, shared Docker network name, backend defaults, source
artifact names, env exclusion keys, default `.cgcignore` text, and upstream
patch snippets.

## Code Commentary

### Logic

CGC runtime, runner, and patch modules import this file for stable names and
marker text. It also reads source `.gitignore` patterns for managed
`.cgcignore` generation.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| CGC runtime layout uses provider constants and default ignore text from this module. | [core.py](core.py.md) |
| CGC Docker runner command/build helpers use runner image and watcher container constants from this module. | [runner.py](../lifecycle/runner.py.md) |
| CGC patch application uses marker and snippet constants from this module. | [patches.py](patches.py.md) |

## Update History

- 2026-05-26T13:58+02:00: Updated after adding the shared CGC Docker network constant.
- 2026-05-26T12:51+02:00: Updated after adding CGC Docker runner image and watcher naming constants.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
