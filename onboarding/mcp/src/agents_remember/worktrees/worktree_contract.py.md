# mcp/src/agents_remember/worktrees/worktree_contract.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

The model, the reader and the writer of a series contract and of a leaf enclosure contract. A contract is
a small Markdown file whose front-matter block records which task, repositories, branches, base commits
and worktrees belong together and where the task stands in review, closeout, integration and cleanup.
Every worktree tool reads its contract through `load_contract`, and every rewrite regenerates the whole
document from the `WorktreeContract` value.

## Code Commentary

### The model

- `WorktreeContract` is a frozen dataclass: task identity (`task_id`, `task_name`, `repo_name`, `kind`,
  `leaf_id`, parent task and parent contract), paths (`coordination_root`, `task_root`, `contract_path`,
  `task_artifact`, `worktree_group`), the code side (repository, source branch, work branch, base commit,
  worktree), the memory side (the same four facts, the worktree, the ledger path and a state), the review,
  closeout, integration and cleanup facts, `lifecycle_id`, `sync_log` and `unknown_cells`.
- `kind` is `series` or `leaf` (`VALID_KINDS`).
- Six cells have closed vocabularies that are imported once and turned into frozen sets with `get_args`:
  workflow kind, memory mode, human review status, closeout status, integration status and cleanup. Their
  defaults are `light-task`, `pending-review`, `not-started`, `not-started` and `pending`
  (`DEFAULT_*`); the memory mode has no constant default.
- `ContractCells` names those six cells as optional fields, and `amend_contract` copies a contract with
  the cells that are given, so a write of one of them is checked by the type checker.
- `CONTRACT_SCHEMA` is `ar-series-contract/v1`. `CONTRACT_SCHEMA_VERSION` is the control plane's
  `SCHEMA_VERSION`.

### Reading

`load_contract(path)` is the one read entry.

1. It probes the file with `observed_exists` and raises `ContractError("worktree contract does not exist:
   <path>")` when it is missing.
2. It reads the text once with `observed_text` and parses it with `parse_contract_text`.
3. It logs one warning when the parse quarantined cells, naming the file and the cells.

The read walks no task tree: it resolves no leaf reference, iterates no other contract and globs nothing.
A legacy stem-shaped `leaf_id` is returned as written.

Inside a recording block of `agents_remember.kernel.recorded_reads` the read leaves one row under the
path it was given: the SHA-256 of the exact bytes read, `absent` for a missing file, or
`unreadable (<error type>)` for a failed read, which is raised. A computation that keeps a result with
its recorded rows therefore depends on the contract's bytes as they were consumed, not on a second look
at the file afterwards. Outside a recording block nothing is recorded. For every caller the text is
decoded as UTF-8 with `\r\n` and `\r` turned into `\n`, and an error of the read itself is raised
unchanged.

`parse_contract_text(text, path=...)` extracts the front matter (a file that does not start with `---`, or
whose block is not closed, is refused naming the file), parses the limited YAML subset of scalar fields
and one-level sections, builds the contract and validates it.

- An unknown major `schemaVersion` is refused; a missing one is read as version 1.0 and an unknown minor
  is accepted.
- A required path cell that is empty is refused, naming `section.key` and the file.
- A vocabulary cell that holds a token outside its vocabulary is not refused. It is read as the cell's
  default (`_vocabulary_cell`) and recorded in `unknown_cells` as `<field>=<token> read as <fallback>`.
  An unreadable memory mode is read as `external` when the memory section records a worktree or a ledger
  and as `disabled` otherwise (`_memory_mode_fallback`).
- One token is the exception: a *removed* memory mode. `_parsed_vocabulary` checks the recorded memory
  mode before the six cells and calls `refuse_removed_memory_mode` with the contract's path, so a
  contract that records a removed mode is refused by name — not loaded, healed or quarantined — and the
  file is left byte-identical pending the developer's decision.

### Writing

- `validate_contract(contract, path=...)` is the write gate, and the read path runs it too. It refuses
  missing required fields, a kind outside `VALID_KINDS`, a vocabulary cell outside its vocabulary, a leaf
  contract without `leaf_id`, and an external-memory leaf contract without memory repository, memory
  worktree or ledger path. Every refusal names the file.
- `contract_publication_text(path, contract)` normalizes the leaf ID, validates and renders with
  `contract_to_text`; `write_contract` writes that text atomically. `unknown_cells` is not written back,
  so a rewrite heals a quarantined cell to the value that was in force.

### Building and healing

- `default_contract(task, leaf=..., code=..., memory=...)` builds a leaf enclosure contract and
  `default_series_contract(...)` a series contract. Both narrow the requested workflow kind and memory mode
  through `_task_vocabulary`, which refuses the removed memory mode by name and any other unknown token
  with `ContractError`.
- `worktree_group_for` is `<coordination root>/worktrees/<repository>/<slug>-ar`.
- `normalize_contract_leaf_id` maps a legacy stem-shaped leaf ID to the task document's ID when the task
  tree proves the mapping. `heal_contract_leaf_ids(coordination_root, dry_run=False)` applies that to every
  active leaf enclosure contract once, rewrites only contracts whose ID changes, and returns a report of
  healed, canonical and unchanged contracts and errors. No read path calls it.

## Evidence

- The schema name and the schema version constant. [21]
- The six vocabularies as frozen sets, the kinds and the defaults. [22]
- A cell outside its vocabulary is read as its default and quarantined. [23]
- The fallback of an unreadable memory mode. [24]
- A requested workflow kind and memory mode are narrowed strictly. [25]
- The six cells as one typed amendment. [26]
- The contract model. [27]
- The leaf enclosure contract factory. [28]
- The one read entry: recorded probe, one recorded read, parse, warning. [29]
- Parsing the retained text: front matter, limited YAML, model, validation. [30]
- The text a write publishes. [31]
- The one-time leaf ID sweep. [32]
- The write gate and its refusals. [33]
- A file without a closed front-matter block is refused naming the file. [34]
- An unknown major schema version is refused. [35]
- A contract changed and restored while it is read is recorded with the bytes that were parsed. [36]
- A contract read that fails is recorded as unreadable under the contract's path. [37]
- A removed memory mode is refused by name with the contract's path before the cells are read. [38]
