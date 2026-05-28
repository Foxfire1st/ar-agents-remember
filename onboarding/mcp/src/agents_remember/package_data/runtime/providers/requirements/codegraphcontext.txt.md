# codegraphcontext.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/requirements/codegraphcontext.txt` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `a8ee8440dfa920d1153a4bb4bb43cc77534c3c90` |
| lastVerifiedCommitDate | 2026-05-25T15:22:52+02:00|
| governingOverview      | `../../../../../../overview.md`                              |

## Governing Overview

[overview.md](../../../../../../overview.md)

## Purpose

This requirements file pins the CodeGraphContext provider dependencies used by Agents Remember's provider lifecycle tooling.

## Code Commentary

### Logic

The file pins `codegraphcontext==0.4.10` plus the Tree-Sitter parser packages
CGC needs for symbol extraction. CGC 0.4.10 declares the parser dependencies
behind a `python_version != "3.13"` marker; without explicit pins, a Python 3.13
environment can install CGC successfully but build only a file-level graph with
zero functions/classes/modules. Runtime installation copies this package
default into `ar-coordination/providers/requirements/codegraphcontext.txt`; the
managed CGC Docker runner build consumes that installed requirements file.

### Conventions

Provider dependency pins live under
`mcp/src/agents_remember/package_data/runtime/providers/requirements/` in the
source checkout and install into `ar-coordination/providers/requirements/`.
Package-owned provider defaults are source-reproducible scaffolding; CGC
execution is Docker-owned in managed mode, while durable database state belongs
under `ar-coordination/providers/data/`.

### Invariants And Boundaries

Provider versions should stay pinned before patching so version-specific patch checks are meaningful. The parser dependencies are part of the CGC provider contract, not optional local setup. Do not point this file at user-global environments or unpinned package ranges.

## Docs References

No external documentation is needed for the pin itself.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The provider requirements file pins CodeGraphContext to version 0.4.10 plus Tree-Sitter parser dependencies needed for symbol extraction. | L1-L4 | [codegraphcontext.txt](agents-remember-md/mcp/src/agents_remember/package_data/runtime/providers/requirements/codegraphcontext.txt) |
| The MCP runtime installer requires and copies `mcp/src/agents_remember/package_data/runtime/providers` into the coordination root. | n/a | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| The CGC runner build uses the installed requirements pin when building the Docker runner image. | n/a | [runner.py](agents-remember-md/mcp/src/agents_remember/providers/cgc/lifecycle/runner.py) |

## Cross-Repo References

No sibling repository evidence is needed for this provider pin.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-05-28T12:32+02:00: Updated after managed CGC execution moved to Docker runner images instead of provider virtual environments.
- 2026-05-25T19:16+02:00: Updated the provider helper reference after `context_providers.py` was replaced by the direct `providers.context` facade and context modules.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T17:50+02:00: Updated references after provider helpers became MCP package modules and the old source script/shared routes were removed.
- 2026-05-23T05:32+02:00: Corrected the durable provider data path to `providers/data` and clarified that provider dependency reinstall is MCP/package-local lifecycle work.
- 2026-05-21T02:50+02:00: Added explicit Tree-Sitter parser dependency pins after CGC on Python 3.13 installed without parsers and produced a file-only graph.
- 2026-05-21T02:10+02:00: Updated for the disposable `providers/` reinstall model and separate durable `provider-data/` location.
- 2026-05-20T19:11+02:00: Created onboarding for the pinned CodeGraphContext provider requirement.
