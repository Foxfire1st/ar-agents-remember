# mcp/src/agents_remember/worktrees/worktree_contract.py

## Governing Overview

[worktrees route overview](overview.md)

## Purpose

The model, the reader and the writer of a series contract and of a leaf enclosure contract. A contract is a small Markdown file whose front-matter block records which task, repositories, branches, base commits and worktrees belong together and where the task stands in review, closeout, integration and cleanup. Every worktree tool reads its contract through `load_contract`, and every rewrite regenerates the whole document from the `WorktreeContract` value.

## Code Commentary

`WorktreeContract` is a frozen dataclass: task identity, paths, the code side, the memory side (repositories, branches, base commit, worktree, ledger path and state), the review/closeout/integration/cleanup facts, `lifecycle_id`, `sync_log` and `unknown_cells`. `kind` is `series` or `leaf`. The six vocabulary cells are imported once and turned into frozen sets with `get_args`; `ContractCells` names those six as optional fields, and `amend_contract` copies a contract with the cells given, so a write of one of them is checked by the type checker. `CONTRACT_SCHEMA` is `ar-series-contract/v1`.

**Two vocabularies for the mode, split by direction.** `WorktreeContract.memory_mode` is `ReadableMemoryMode`: a contract on disk may carry the removed `disabled` mode and still load, so status, attach, and guarded abandon can answer it. `ContractCells.memory_mode` — the write path — is `MemoryMode`: producing the removed mode is a type error at the writer, and `default_contract` always builds an external-memory leaf (memory worktree plus ledger path, no disabled branch). `VALID_MEMORY_MODES` is the external-only set.

**Reading.** `load_contract` probes, reads once, parses with `parse_contract_text`, and logs one warning when the parse quarantined cells. A vocabulary cell holding an off-vocabulary token is read as its default and recorded in `unknown_cells` — except one token: a removed mode other than `disabled` is refused by name with the contract's path, never loaded, healed, or quarantined. An unreadable memory mode degrades off the section it governs: `external` when the memory section records a worktree or a ledger, otherwise the removed `disabled` the section's shape was left in (`_memory_mode_fallback`). The request side (`_task_vocabulary`, used by both default constructors) refuses a removed mode by name and any other unknown token with `ContractError`.

**The initial pair.** `original_base_pair(contract)` is the code/memory pair the first recorded sync advanced from — `codeBaseFrom` and `memoryBaseFrom` — or the contract's own base commits when no sync is logged. Checkpoints advance the source refs, so this is the pair the series' pre-sync origin and the master's cumulative document debt are measured from.

**Writing.** `validate_contract` is the write gate and the read path runs it too: missing required fields, an off-vocabulary cell, a leaf without `leaf_id`, and an external-memory leaf without memory repository, worktree, or ledger path are all refused naming the file. `unknown_cells` is not written back, so a rewrite heals a quarantined cell to the value in force.

`worktree_group_for` is `<coordination root>/worktrees/<repository>/<slug>-ar`. Leaf-id healing (`normalize_contract_leaf_id`, `heal_contract_leaf_ids`) is a one-shot sweep, never a per-read side effect. Its shared enclosure walk excludes notes and archives. `_load_sweep_contract` records unreadable or malformed files in `errors`; a loaded contract whose task artifact resolves outside the positional repository tasks folder instead goes to `skipped`, with its path and reason, and is never healed. Successful healing, canonical and unchanged counts retain their separate meanings.

## Evidence

- Removed-but-not-`disabled` refused at read; `disabled` loads [64]
- Unreadable mode degrades to external or removed-disabled [65]
- Request side refuses removed modes by name [66]
- Started contracts are always external [67]
- Write path is external-only by type [68]
- Read record carries the readable vocabulary [69]
- Runtime vocabulary set is external-only [70]

- Healing reports foreign contracts as skipped and unreadable contracts as errors without treating either as a healable enclosure. [71]
