# mcp/tests/test_cold_start.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Offline cold-start and corrupt vendored tokenizer refusal.

## Code Commentary

### Logic

A child process starts the server with cold caches and network access blocked before import. A separate in-process case flips one byte in a disposable vocabulary copy and requires TokenizerVocabularyError before tiktoken reads or repairs it.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

Do not import tokens at collection time or corrupt the shipped vocabulary. Warm parent caches cannot stand in for the child probe; arithmetic belongs to the tokenizer tests.

### Todos

No file-local implementation change is requested by this reconciliation.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- The server starts with cold caches and no network. [1]
- A counter will not build on a corrupt copy. [2]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.
