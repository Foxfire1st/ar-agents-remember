# mcp/src/agents_remember/package_data/runtime/providers/docker/codegraphcontext/requirements.txt

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

## Evidence

### Docs References

No external domain documentation is configured for this repository; the
resolved `system/sources.md` currently contains no entries.

No relevant external documentation source is configured for this file.

### Repo-Internal References

- The CodeGraphContext package pin. [1]
- The tree-sitter package pin. [2]
- The tree-sitter language-pack pin. [3]
- The tree-sitter C# pin. [4]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is required beyond installing pinned third-party dependencies in the Docker image.
