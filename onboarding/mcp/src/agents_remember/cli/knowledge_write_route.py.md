# mcp/src/agents_remember/cli/knowledge_write_route.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The converted knowledge CLI's file-write routes share admission, owner identity, decision inputs and report rendering.

## Code Commentary

Leaf writes use the supplied enclosure and its leaf owner; named waves use their admitted repository root. Crossing writes retain their separately admitted crossing owner. Each delegates to the file writer rather than selecting a canonical database. `unconverted_write_refusal` refuses unconverted memory unconditionally with shared conversion guidance: cross from a converted source through `worktree_sync` with `merge-memory`, otherwise make the first conversion described by `c-13-install-and-onboard` and `docs/guides/first-conversion.md`. A missing memory worktree retains its own named error. Database-publication arguments are refused by their CLI front door, not accepted here as an alternative destination. The removed `_file_route_refusal` and legacy dataset writer dispatch are not current routes.

### Logic

Before calling `write_knowledge`, `run_leaf_write` reads the persisted leaf worklist and refuses unreadable or invalid-shaped input with its path and compute/recompute remedy. It passes that admitted value, rather than fabricating one. `LeafQuestions` also forwards `append_many` and the resolved destination lazily; loaded settings must resolve to the contract’s same coordination root before a task_doc port is created. This does not add a leaf-worklist prerequisite to wave/crossing owners.

- `leaf_owner`: the leaf is the contract's `leaf_id` (else task name); the task is `task.json` `id`, else the
  leaf ID's prefix before `-L<n>`.
- **`LeafQuestions` (MIK-R14).** A `dataclass` over the parsed arguments and the contract that implements the
  writer's `OpenQuestions` port lazily: the MCP authority settings are read only when a `raise` needs them (`check`
  or `append`), from `--config` (`require_config_path`) or else by `discover_config(Path.cwd())`. A settings error
  (`AgentsRememberError`, `ConfigDiscoveryError`, `OSError`, `ValueError`) yields `UnavailableOpenQuestions` with
  "no MCP authority settings to reach task_doc (…); pass --config", so the `raise` is refused and nothing is
  written; otherwise `TaskDocOpenQuestions` addresses the contract's repository, contract path, task root and leaf
  (`leaf_id`, else the task name). A run with only `still_rejected` rows never reads settings. The worker's real
  evidence ran the scratch answer with `declare_execution_mode("test")`, because checkout-CLI mode substitutes
  synthetic settings for `--config`; the installed-mode check is carried to L37 (review F10).
- `run_wave_write` (`knowledge-bootstrap`): a bootstrap has no leaf, so it writes as the wave `--wave` names
  (`[A-Za-z0-9._-]`); its history file is `knowledge/history/<wave>.json` (MIK-R07 rule 8); the task is
  the bootstrap scope (architect ruling 2). Since MIK-R13 it takes an optional keyword `coordination_root` (default `None`) and
  passes it to `WriteRequest`; `cli/knowledge_bootstrap._run` passes the admitted authority's root. Without
  it every requirement endpoint is reported `requirement-task-plane-unavailable`.
- Exit status: 0 written or planned, 1 refused, 2 invocation refused. `--json` prints `WriteReport.to_document()`. A refused state alone is not universal zero-publication evidence: separately reported question publication and native rollback outcomes retain their exact custody. Do not repeat a mutator to recover its result.
- **`run_leaf_write` passes `code_base=contract.code_base_commit`** (L37, review R1 F10b): the commit a
  trailerless unconverted `HEAD` is converted at, which is the gate's and the worklist's fallback, so the three
  share one converted-base cache key.

`_leaf_memory_base` resolves the memory commit paired to the contract code base on the memory source branch. `run_leaf_write` passes that result to WriteRequest: the paired base governs counted-card comparison. Missing pairing inputs or lookup failure yield None, retaining the downstream fallback rather than inventing a base. Lazy settings/question ownership is unchanged.

- Leaf writer request binds the independently resolved paired memory base. [34]

### Conventions

- Imported by `cli/knowledge_ingest.py` and `cli/knowledge_bootstrap.py`; not registered as its own subcommand.

### Invariants And Boundaries

- No database write happens on this route, and no argument is silently ignored.
- `--commit` stays the commit word: without it the run plans, validates and reports.

## Evidence

- Leaf writes preflight the persisted worklist; lazy question forwarding uses batched publication and same-coordination-root authority. [35]


### Repo-Internal References

- `run_leaf_write` owns the current boundary described above. [17]
- `run_wave_write` owns the current boundary described above. [18]
- `run_crossing_write` owns the current boundary described above. [19]
- `unconverted_write_refusal` owns the current boundary described above. [20]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The layout-marker test. [21]
- The unconditional write refusal for an unconverted leaf tree names crossing from a converted source or the first conversion; converted memory elsewhere is not an admission prerequisite. [22]
- The owner from the contract and `task.json`. [23]
- The task owner's decision resolver for the leaf (MIK-R11). [24]
- The leaf route, which binds that resolver and, since MIK-R14, the lazy task-document port and the persisted worklist. [25]
- The lazy port: settings read only when a `raise` needs them, from `--config` or discovery; unavailable settings refuse the `raise`. [26]
- The wave route. [27]
- The ingest dispatch on the loaded contract. [28]
- The bootstrap dispatch on the admitted memory root. [29]
- Planning writes nothing; unconverted memory is not this route. [30]
- Blank authorization refused and recorded. [31]
- The crossing owner's route: the sync's memory worktree, the series' code work branch as C. [32]
- Which worktree holds the open crossing history file, or why the run is refused. [33]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
