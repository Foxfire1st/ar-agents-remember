# grepai.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `runtime/providers/requirements/grepai.txt` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-21T02:10+02:00                     |
| lastVerifiedCommitHash | `0462de46a1da1bf1997e3979f4cc5bc53d1132f6` |
| lastVerifiedCommitDate | 2026-05-21T08:30:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`grepai.txt` is the package-owned provider requirement pin for the managed GrepAI provider binary.

## Code Commentary

### Logic

The file pins GrepAI to `grepai==0.35.0`. The runtime installer requires this file as part of `runtime/providers/`, rebuilds `ar-coordination/providers/` from source defaults during reinstall, and copies it to `ar-coordination/providers/requirements/grepai.txt`. Provider lifecycle tooling reads the installed pin, maps it to the matching GitHub release asset for the current OS and CPU architecture, and installs the binary into `ar-coordination/providers/_bin/grepai` or `grepai.exe`.

### Conventions

- Keep one exact GrepAI requirement line in this file.
- Update provider lifecycle release handling when changing the pin format.
- Reinstall may recreate this requirement file and other `providers/` scaffolding, but it must not delete durable provider data such as GrepAI indexes or CGC backend data.

### Invariants And Boundaries

This file is package metadata, not runtime state. It should not contain machine-local paths, generated status, or search indexes.

### Todos

None.

## Docs References

No external documentation is needed for this pin file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The requirement file pins GrepAI to `grepai==0.35.0`. | L1-L2 | [grepai.txt](agents-remember-md/runtime/providers/requirements/grepai.txt) |
| The installer requires both CGC and GrepAI provider requirement files before copying provider defaults into the coordination root. | L198-L204 | [installer](agents-remember-md/installer/install-runtime.py) |
| The provider helper exposes the GrepAI pin and writes the managed requirements file through the shared provider requirements helper. | L24; L294-L295 | [context_providers.py](agents-remember-md/runtime/skills/U-01-core-skills/_shared/agents_remember/context_providers.py) |
| The lifecycle installer reads the GrepAI pin and installs the matching platform release binary into `providers/_bin`. | L1420-L1489 | [provider-lifecycle.py](agents-remember-md/runtime/scripts/provider-lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-21T02:10+02:00: Updated for the disposable `providers/` reinstall model; this pin is source-recopied while durable provider data remains outside the wiped provider scaffold.
- 2026-05-21T01:47+02:00: Created onboarding for the GrepAI provider requirement pin copied by the runtime installer and consumed by provider lifecycle tooling.
