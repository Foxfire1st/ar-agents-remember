# mcp/src/agents_remember/providers/cgc/bundle.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`bundle.py` rewrites CodeGraphContext seed bundle contents from a source repository root to a target repository root.

## Code Commentary

### Logic

It builds path replacement pairs for POSIX and platform string variants, safely extracts the source zip bundle, rewrites JSON, JSONL, Markdown, and text files, and writes a new target zip bundle with rewritten paths.

### Invariants And Boundaries

- Zip entries are checked to ensure extraction cannot escape the temporary root.
- Only JSON, JSONL, Markdown, and text files are rewritten.
- The function reports rewritten files and replacement count for seed diagnostics.

## Evidence

### Repo-Internal References

- CGC seed orchestration calls this module between export and load. [1]
