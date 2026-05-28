# grepai.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/requirements/grepai.txt` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T14:21:08+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

`grepai.txt` is the package-owned provider requirement pin for the managed
GrepAI Docker runner image.

## Code Commentary

### Logic

The file pins GrepAI to `grepai==0.35.0`. The runtime installer requires this file as part of `mcp/src/agents_remember/package_data/runtime/providers/`, rebuilds `ar-coordination/providers/` from source defaults during reinstall, and copies it to `ar-coordination/providers/requirements/grepai.txt`. Provider lifecycle tooling reads the installed pin and uses it to build the Docker-owned GrepAI runner image; no managed host `_bin/grepai` binary is installed.

### Conventions

- Keep one exact GrepAI requirement line in this file.
- Update Docker runner image release handling when changing the pin format.
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
| The requirement file pins GrepAI to `grepai==0.35.0`. | L1-L2 | [grepai.txt](agents-remember-md/mcp/src/agents_remember/package_data/runtime/providers/requirements/grepai.txt) |
| The MCP runtime installer requires both CGC and GrepAI provider requirement files before copying provider defaults into the coordination root. | n/a | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| The provider helper exposes the GrepAI pin and writes the managed requirements file through the package provider helper. | n/a | [context.py](agents-remember-md/mcp/src/agents_remember/providers/context.py) |
| The lifecycle installer reads the GrepAI pin and builds the Docker-owned runner image through the lifecycle facade. | n/a | [lifecycle.py](agents-remember-md/mcp/src/agents_remember/providers/lifecycle.py) |

## Cross-Repo References

No sibling repository evidence is needed.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-28T14:21:08+02:00: Updated after the source comment was clarified
  from provider binary wording to Docker runner wording.
- 2026-05-25T19:16+02:00: Updated after GrepAI became Docker-owned and the legacy `provider_lifecycle.py` compatibility module was removed.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T17:50+02:00: Updated references after provider helpers became MCP package modules and the old source script/shared routes were removed.
- 2026-05-23T05:32+02:00: Updated the lifecycle-script reference after provider Python scripts moved out of installed runtime and into source/package-owned `scripts/`.
- 2026-05-21T02:10+02:00: Updated for the disposable `providers/` reinstall model; this pin is source-recopied while durable provider data remains outside the wiped provider scaffold.
- 2026-05-21T01:47+02:00: Created onboarding for the GrepAI provider requirement pin copied by the runtime installer and consumed by provider lifecycle tooling.
