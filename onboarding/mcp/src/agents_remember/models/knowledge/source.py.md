# mcp/src/agents_remember/models/knowledge/source.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Shared source locator values: a whole file, an inclusive one-based line range, or a qualified symbol. `SourceLocator` is their discriminated union.

## Code Commentary

### Logic

`LineRangeLocator` refuses an end preceding its start; `SymbolLocator` requires nonblank language and qualified name. The symbol reader uses the shipped extractor over recorded bytes, reports an unbound name as a mismatch and an unavailable grammar as unsupported. Failure to resolve a locator does not erase its claim.

### Invariants And Boundaries

This module performs no I/O. Canonical Git-blob identity and source-anchor draft/stored models and their row-writing APIs are retired under MIK-R26; no anchor writer is replaced by a locator value. Recorded locators remain readable values even when a reader cannot resolve them.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References


- The three source locator values and their discriminated union. [2]


- The retained decoder uses shared locator values; the canonical anchor-row encoding and decoding APIs are retired. [7]

The later requirement packets this vocabulary is declared shared with: requirement packets `KS-R07` and `KS-R08`, which live in the coordination root, outside both the code and the memory repository, so the citation grammar cannot address them.

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
