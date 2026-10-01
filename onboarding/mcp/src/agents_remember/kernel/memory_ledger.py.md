# mcp/src/agents_remember/kernel/memory_ledger.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Defines the consumer memory-ledger representation: schema and row types, structural parsing,
validation, canonical serialization, and current-versus-historical row lookup. It does not derive
Git authority from those serialized rows.

## Code Commentary

### Logic

The format is a fenced JSON metadata block followed by a two-column `Code commit` / `Memory commit`
table. `parse_ledger_text_unvalidated` checks structure, schema, repository name, and sort-order
metadata without enforcing current-header agreement. Nonempty tables still require all revision
metadata. `parse_ledger_text` additionally calls `validate_ledger`.

An empty derived ledger is valid. It has no mapping rows and may leave revision metadata empty;
validation refuses an empty ledger that nevertheless claims a current code or memory mapping.
For nonempty rows, the first pair must agree with the current header and ordering remains
`newest-first`.

`prepend_mapping` returns a representation with the new pair and updated current header.
`find_mapping` selects the first matching code row; `contains_mapping` asks whether an exact pair
occurs anywhere in the data. Repeated code commits can therefore represent ordered memory states
without collapsing their history.

`write_ledger` serializes only the explicitly supplied representation. It creates no commit and
performs no staging or ref move. Runtime refresh uses `memory_cache.refresh_memory_cache` to derive
and materialize current data. `LEDGER_RELATIVE_PATH` owns the filename; `MEMORY_CACHE_EXCLUDE` is the
exact root-cache exclusion consumed by Git staging/status helpers, including ignored or unreadable
legacy cache files. The former projection-module reexport is no longer a reader contract.

### Conventions

The parser uses a narrow standard-library grammar. Representation helpers and lookup ordering are
data semantics; callers must not treat a successful parse or matching row as permission for Git
work. Runtime derivation and best-effort cache writing have their separate kernel owner.

### Invariants And Boundaries

- Empty data must not claim a current mapping; nonempty data must retain its required metadata.
- The current header matches the first row when validated.
- Current lookup and historical containment are distinct and do not impose global code-key uniqueness.
- Writing a representation does not stage or commit it.
- A cached table is disposable; only committed attribution supplies runtime mappings.

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

- Format constants, row types, and the exact cache-exclusion expression. [1]
- Structural parsing and validation distinguish empty and nonempty representations. [2]
- Serialization and data lookup stay independent from Git publication. [3]
- The runtime cache owner derives data rather than trusting a serialized table. [4]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
