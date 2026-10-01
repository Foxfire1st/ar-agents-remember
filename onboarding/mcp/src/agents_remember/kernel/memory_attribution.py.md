# mcp/src/agents_remember/kernel/memory_attribution.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Owns the shared `Code-Commit` key, memory-message renderer, and committed-attribution reader. The
attribution is part of the memory commit object; this module does not create commits or files.

## Code Commentary

### Logic

`render_memory_content_message` appends a separate final attribution block after the supplied
body. Keeping the writer beside the key prevents producer-local spellings from drifting away from
the reader. Carryover may receive a multi-paragraph public body; baseline uses its own adoption
subject, and closeout-shaped producers delegate through the effective input model.

`attributed_commits` reads Git's trailer values for every commit reachable from the requested tip,
optionally excluding another history. It uses the full ancestry rather than only first parents,
so a mapping introduced on a merged branch remains visible. NUL-delimited records preserve commit
boundaries. A readable commit with no matching attribution is returned with `code_commit=None`;
an unreadable history raises `MemoryAttributionError` instead of looking like empty attribution.

`_trailer_value_from` accepts the declared hash-shaped value and keeps the last matching value.
`parse_code_commit_trailer` is the message-level parser; it returns the last matching anchored
trailer line and ignores a mere in-line mention. `ledger_rows_from_attribution` preserves the Git
walk's ordering and omits unattributed commits. `AttributedCommit.row(code_repository=...)` optionally
checks that the named code commit exists.

The documentation correction removes the former runtime-table fallback story. This reader's
runtime implementation remains trailer-based. Explicit historical-table migration is owned by
`memory_backfill`, not activated by missing attribution in this module.

### Conventions

One frozen `AttributedCommit` value and module-level functions expose the reader. SHA-shaped text
is syntax; the optional code-repository check establishes object existence. The writer returns a
message string only and owns no publication or backfill policy.

### Invariants And Boundaries

- No cached or historical table is a runtime fallback for absent attribution.
- Unattributed commits and unreadable Git history remain different facts.
- The full reachable ancestry includes merge-side attribution.
- The shared key and renderer remain the only production spelling/format owner.
- Code-object validation applies when the caller supplies the code repository.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- The single key, log format, renderer, and attribution value. [1]
- The history walk and message/value parsers define the actual read behavior. [2]
- Row conversion and optional object validation. [3]
- Runtime ledger derivation never consults cache text. [4]
- The source census and behavioral renderer case keep the producer seam visible. [5]
- None [6]
- None [7]
- None [8]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
