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

The file lists the exact Python packages required by the CGC Docker runner:
`codegraphcontext==0.4.10`, `tree-sitter==0.25.2`,
`tree-sitter-language-pack==0.13.0`, and `tree-sitter-c-sharp==0.23.5`.

### Invariants And Boundaries

- This file is Docker runner image input, not the host runtime install
  requirements file.
- The dependency list is committed Docker image input; lifecycle code does not
  generate this file at runtime.

## Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation source is configured for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The CodeGraphContext package pin. | "codegraphcontext==0.4.10" | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt:1-1 |
| The tree-sitter package pin. | "tree-sitter==0.25.2" | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt:2-2 |
| The tree-sitter language-pack pin. | "tree-sitter-language-pack==0.13.0" | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt:3-3 |
| The tree-sitter C# pin. | "tree-sitter-c-sharp==0.23.5" | mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt:4-4 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is required beyond installing pinned third-party dependencies in the Docker image. | n/a | n/a |

## Update History
- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.

- 2026-05-26T23:59+02:00: Created for the provider Compose migration and closeout missing-onboarding gate.
