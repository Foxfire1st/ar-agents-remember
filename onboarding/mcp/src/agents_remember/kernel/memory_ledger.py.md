# mcp/src/agents_remember/kernel/memory_ledger.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

## Purpose

The representation of a memory ledger: its schema and row types, the structural parse, the validation, the
canonical text, the two loaders and the lookups of a mapping between a code commit and a memory commit. The
module reads and writes the file it is given and starts no Git command. Apart from the package's error
base class and the kernel's read recorder it uses only the standard library.

## Code Commentary

- **Format.** A ledger is a fenced `json ar-memory-ledger` metadata block followed by the first Markdown
  table whose header is `Code commit | Memory commit`. `LEDGER_RELATIVE_PATH` is `memory.md`.
  `MEMORY_CACHE_EXCLUDE` is the Git pathspec that excludes exactly that root file.
- **Structural parse.** `parse_ledger_text_unvalidated` requires the fence, a JSON object, the fields
  `schema`, `repoName` and `sortOrder`, one of the two accepted schema names, the table header followed by
  a separator row, and two cells in every row. A ledger with rows must carry all four commit fields. It does not compare the header with the
  first row.
- **Validation.** `validate_ledger` requires `sortOrder` `newest-first`. An empty ledger must not name a
  current code or memory commit. With rows, the first row must equal `lastVerifiedCodeCommit` and
  `lastMemoryContentCommit`. `parse_ledger_text` is the structural parse followed by this validation.
- **Loading.** `load_ledger(path)` raises `LedgerError` when the file does not exist and otherwise parses
  and validates its text. `load_ledger_unvalidated(path)` does the same with the structural parse only.
  Both probe and read through `observed_exists` and `observed_text`: inside a recording block a missing
  ledger is recorded as `absent`, a read ledger with the SHA-256 of the bytes read, and a failed read as
  `unreadable (...)`. The text is decoded as UTF-8 with `\r\n` and `\r` turned into `\n`. Outside a
  recording block the loaders record nothing. This holds for every caller, among them the context packet,
  the dashboard's analytics snapshots and the cross-repository context
  (`kernel/coordination_context/cross_repo.py`).
- **Writing and lookups.** `ledger_to_text` validates and renders the canonical text; `write_ledger` writes
  it and neither stages nor commits. `prepend_mapping` returns a ledger with a new first row and the header
  set to it. `find_mapping` returns the first row of a code commit; `contains_mapping` tests one exact pair
  anywhere in the rows. `create_initial_ledger` builds a one-row ledger.

## Evidence

- Schema names, the fence pattern, the file name and the exclusion pathspec. [5]
- The structural parse and its required fields. [6]
- The validation of order, empty ledgers and the first row. [7]
- The validating loader probes and reads through the recorder. [8]
- The structural loader probes and reads through the recorder. [9]
- Writing serializes the given ledger and touches no Git state. [10]
- The first-row lookup of a code commit. [11]
- The exact-pair lookup. [12]
- A ledger read by the reviewer's worklist is recorded with the bytes read, its absence and its read failure. [13]
