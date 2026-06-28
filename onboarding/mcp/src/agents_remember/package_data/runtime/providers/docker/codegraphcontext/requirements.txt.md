# mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-26T23:59+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../../requirements/codegraphcontext.txt.md`                              |

## Governing Overview

[CodeGraphContext requirements onboarding](../../requirements/codegraphcontext.txt.md)

## Purpose

This requirements file is the package-owned dependency input for the
CodeGraphContext Docker runner image. It pins the third-party CGC package and
tree-sitter dependencies installed during Docker build.

## Code Commentary

### Logic

The file lists the exact Python packages installed by the CGC Dockerfile before
the patch script runs: `codegraphcontext==0.4.10`, `tree-sitter==0.25.2`,
`tree-sitter-language-pack==0.13.0`, and `tree-sitter-c-sharp==0.23.5`.

### Invariants And Boundaries

- This file is Docker runner image input, not the host runtime install
  requirements file.
- Dependency changes must remain coordinated with `patch_cgc.py`; patch target
  snippets depend on the installed `codegraphcontext` version.
- Lifecycle Python should read committed Docker assets instead of generating a
  requirements file at runtime.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | L1-L3 | [system/sources.md](../../../../../../../../../../../../../system/sources.md) |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The requirements file pins CodeGraphContext and tree-sitter dependencies for the Docker runner image. | L1-L4 | [requirements.txt](agents-remember/mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt) |
| The CGC Dockerfile installs this requirements file before running `patch_cgc.py`. | L7-L13 | [Dockerfile](agents-remember/mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/Dockerfile) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary is required beyond installing pinned third-party dependencies in the Docker image. | n/a | n/a |

## Update History

- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
