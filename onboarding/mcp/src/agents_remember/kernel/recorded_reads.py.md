# mcp/src/agents_remember/kernel/recorded_reads.py

## Governing Overview

[mcp package overview](../../../overview.md)

## Purpose

Records what a computation read outside any Git tree, so that a result computed from Git trees and plain
files can be reused only while those files and path selections are unchanged. A recording block collects
`{key: identity}` rows. The module also re-checks a recorded set against the file system, validates rows that
arrive from another process, and gives readers four helpers that perform a path operation and record it in
one step. The gate's memo and the reviewer's leaf-view memo keep every result together with the rows recorded
for it.

## Code Commentary

### The rows

- A **byte row** has the file's POSIX path as key. Its identity is `sha256:<hex>` of the exact bytes read,
  `absent` (`ABSENT`) when the file does not exist, or `unreadable (<error type>)` when the read failed.
- A **selection row** records a path operation, not bytes. `resolve:<absolute logical path>` holds
  `resolved:<target>`, and `exists:<absolute logical path>` holds `present` or `absent`. Either can hold
  `unreadable (<error type>)`.
- A **listing row** `json-files:<absolute root>` records the exact direct `*.json` listing a task lookup
  consumed: the byte identity of the NUL-separated sorted direct paths, including an empty listing, or
  `unreadable (<error type>)` when the listing failed.
- A key recorded twice with two different identities inside one block becomes `conflicting reads`
  (`CONFLICTING`). The file or the selection changed while the computation ran.

### Recording

- `recorded_reads()` is a context manager. It puts a fresh dictionary into the context variable `_READS`,
  yields it and restores the previous value on exit. A nested block therefore collects its own rows, and the
  outer block sees only what is replayed into it afterwards.
- `record_read(path, identity=None)` records one byte row: the identity the reader passes, or the file's
  identity at this moment (`file_identity`). `_record` applies the conflict rule.
- Outside a recording block every recording call does nothing.
- `replay_reads(reads)` records a mapping of rows through the same conflict rule. It carries rows from a
  nested block, from a kept memo entry and from the reviewer's worklist child process into the caller's
  block.

### Readers that record

Each helper performs the operation once and records what that one operation saw. Outside a recording block
each returns what the plain call returns and raises what it raises.

- `observed_text(path)` reads the bytes once, records their SHA-256 and returns them decoded as UTF-8 with
  `\r\n` and `\r` turned into `\n`. A missing file records `absent`, another `OSError` records
  `unreadable (...)`; both are raised again.
- `observed_exists(path)` returns `path.exists()`. A false probe records `exists:<absolute logical path>`
  = `absent` — the existence predicate that was actually used, not a failed byte read (a parent that is a
  file gives the same answer). A probe that raises records `unreadable (...)` under the file's byte key. A
  present file gets no row from the probe; its row comes from the read, when one follows.
- `observed_json_files(root)` returns the sorted direct `*.json` files of a folder and records
  `json-files:<absolute root>` with the listing's exact digest — the byte identity of the NUL-separated
  sorted direct paths, empty listing included; a failed listing records `unreadable (...)`.
- `observed_path_exists(path)` returns `path.exists()` and records an `exists:` row in every case. It is the
  probe for a directory, which has no bytes to hash.
- `observed_resolve(path)` returns `path.resolve()` (non-strict) and records a `resolve:` row keyed by the
  absolute unresolved path.

### Checking a recorded set

- `observation_identity(key)` repeats the recorded operation: it resolves the path for a `resolve:` key, tests
  existence for an `exists:` key, re-lists the direct `*.json` files for a `json-files:` key and hashes the
  file for a byte key.
- `changed_observations(reads)` returns the keys whose identity differs from the recorded one. It checks the
  selection rows first — `resolve:`, `exists:` and `json-files:` keys — and returns only them when one
  moved. Byte rows are read only when every selection still gives its recorded answer, so a locator that
  was retargeted never causes a read of its new target.
- `has_failed_observation(reads)` is true when a row is `conflicting reads` or starts with `unreadable (`.
  Both memos refuse to keep a result with such a row.
- `valid_observation(key, identity)` checks one row from another process: no NUL byte, an absolute logical
  path for a selection key, an identity of the kind that belongs to the key — `present`/`absent` for
  `exists:`, `resolved:<absolute>` for `resolve:`, a non-`absent` `sha256:` listing identity for
  `json-files:` — and for a byte key a non-empty key with a `sha256:` identity of 64 hexadecimal digits,
  `absent`, or a failure identity.

### Who records and who checks

- Recording blocks are opened by the gate's evaluation (`application/knowledge_gate/gate.py`), by the
  leaf-view key lookup and the leaf-wide computation of the reviewer (`application/review_leaf_view_memo.py`,
  `application/review_tree_knowledge.py`), by the worklist child (`application/reviewer_worklist_child.py`)
  and by the strict task lookup (`tasks/leaf_decisions.py`).
- Rows come from the task document reader (`tasks/store.py`), the requirement manifest and packet readers
  (`memory/knowledge/requirement_endpoint.py`, `tasks/task_intent.py`), the contract loader
  (`worktrees/worktree_contract.py`), the ledger loader (`kernel/memory_ledger.py`), the settings parsers and
  the root selection of `kernel/coordination_context/`, and `kernel/memory_mode.py`.

## Evidence

- The module docstring: the three byte identities, the two selection namespaces and the conflict rule. [7]
- The identity of a file at this moment. [8]
- The recording block sets and restores the context variable. [9]
- One read is recorded with the passed identity or the file's identity. [10]
- Two different identities for one key become a conflict. [11]
- Rows of another block or process are recorded through the same conflict rule. [12]
- The validation of a row that arrives from another process. [13]
- The recheck repeats the recorded operation. [14]
- Selections are rechecked before bytes, and bytes only when no selection moved. [15]
- A conflict or an unreadable row marks the set as failed. [16]
- The recorded resolution keeps the absolute logical path as its key. [17]
- The recorded existence probe of a path, also for a directory. [18]
- A false existence probe records `exists:<absolute logical path>` = absent, distinct from a failed byte read. [19]
- One read of the bytes, recorded, then decoded with newline translation. [20]
- The absent higher-priority settings file, the absent JSON sibling and the consumed Markdown file are rows of one recording. [21]
- A retargeted packet locator is seen through its resolve row, and no byte outside the task is read for the recheck. [22]
- A failed root probe is recorded as unreadable and the view is not kept. [23]
- A malformed row from the child is refused by the parent. [24]
- Every file the gate reads is in its read set, and a conflicting read is never kept. [25]
- The direct JSON listing of a folder is recorded as one `json-files:` row, empty listing included. [26]
