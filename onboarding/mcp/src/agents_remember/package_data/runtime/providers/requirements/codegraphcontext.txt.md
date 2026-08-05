# codegraphcontext.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/requirements/codegraphcontext.txt` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T12:32+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The provider requirements file pins CodeGraphContext to version 0.4.10 plus Tree-Sitter parser dependencies needed for symbol extraction. | "codegraphcontext==0.4.10"; "tree-sitter==0.25.2"; "tree-sitter-language-pack==0.13.0"; "tree-sitter-c-sharp==0.23.5" | mcp/src/agents_remember/package_data/runtime/providers/requirements/codegraphcontext.txt:1-4 |
| The MCP runtime installer requires and copies `mcp/src/agents_remember/package_data/runtime/providers` into the coordination root. | `require_runtime_tree`; `install_runtime` | mcp/src/agents_remember/install/runtime.py:317-328; mcp/src/agents_remember/install/runtime.py:462-553 |
| The CGC runner build uses the installed requirements pin when building the Docker runner image. | `cgc_runner_image_build` | mcp/src/agents_remember/providers/cgc/lifecycle/runner.py:37-74 |

## Cross-Repo References

No sibling repository evidence is needed for this provider pin.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:46+02:00 — 260731-EFA-L6 curator W1-B03: repaired 3 citation rows with exact anchors and source paths; scoped citation recheck recorded separately. Verification metadata remains pinned until closeout.

- 2026-05-28T12:32+02:00: Updated after managed CGC execution moved to Docker runner images instead of provider virtual environments.
- 2026-05-25T19:16+02:00: Updated the provider helper reference after `context_providers.py` was replaced by the direct `providers.context` facade and context modules.
- 2026-05-24T18:10+02:00: Moved onboarding to mirror the packaged runtime source route under `mcp/src/agents_remember/package_data/runtime/` after F-10 packaged runtime asset discovery.
- 2026-05-23T17:50+02:00: Updated references after provider helpers became MCP package modules and the old source script/shared routes were removed.
- 2026-05-23T05:32+02:00: Corrected the durable provider data path to `providers/data` and clarified that provider dependency reinstall is MCP/package-local lifecycle work.
- 2026-05-21T02:50+02:00: Added explicit Tree-Sitter parser dependency pins after CGC on Python 3.13 installed without parsers and produced a file-only graph.
- 2026-05-21T02:10+02:00: Updated for the disposable `providers/` reinstall model and separate durable `provider-data/` location.
- 2026-05-20T19:11+02:00: Created onboarding for the pinned CodeGraphContext provider requirement.
