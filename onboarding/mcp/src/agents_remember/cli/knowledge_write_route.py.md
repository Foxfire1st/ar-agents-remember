# mcp/src/agents_remember/cli/knowledge_write_route.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**The file-writer route of `knowledge-ingest` and `knowledge-bootstrap` (MIK-R12 rule 7).** Both
commands keep one spelling; the memory tree they write decides the writer. A **converted** tree (it holds
`knowledge/layout.json`) is written by `write_knowledge`; an **unconverted** tree keeps the database ingest
exactly as before in a repository that holds no converted memory; once it does, the cutover lock refuses the
write and names the crossing sync (L37; MIK-R09 rule 6, MIK-R24 rule 9; architect ruling 1 covered the time
before the cutover).

## Code Commentary

### Logic

- `is_converted` tests the layout marker; `load_leaf_contract` loads the contract or returns `None` (the
  database route then reports why); `converted_contract` combines the two.
- `leaf_owner`: the leaf is the contract's `leaf_id` (else task name); the task is `task.json` `id`, else the
  leaf ID's prefix before `-L<n>`.
- `run_leaf_write` (`knowledge-ingest`): a blank `--authorization-ref` exits 2 with the database route's
  message; the database-only flags (`--candidate-directory`, `--baseline`, `--rebase-baseline`,
  `--publish-to`, `--publish`, `--expected-destination`) are refused **by name**, exit 2; an unreadable list
  exits 2; then `write_knowledge` writes into the contract's memory worktree, with the hand-off path
  relative to the task root. Since MIK-R11 the request also carries `decisions=leaf_decisions(contract)`:
  `leaf_decisions` binds the task owner's `tasks/leaf_decisions.leaf_decision_refusal` to the contract's
  task root and leaf, so a planned `dropped` row's cited decision is resolved at write time through the
  strict leaf lookup (ruling F1). `run_wave_write` binds none, so a wave refuses a `dropped` planned row.
  Since MIK-R13 the request also carries `coordination_root=contract.coordination_root`, so the writer resolves
  each requirement endpoint through its owning task and reports it (`requirementEndpoints`); an unresolved
  endpoint never refuses the run. Since MIK-R14 it also carries `questions=LeafQuestions(args, contract)` and
  `worklist=read_leaf_worklist(contract.contract_path)`: the leaf's persisted worklist, so a `still_rejected` row
  refreshes the links whose trigger fired on its item, and a lazy port to the leaf task document's
  `openQuestions` for `raise` rows.
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
- `unconverted_write_refusal` (MIK-R24 rule 9): for a leaf contract whose memory worktree is **unconverted**,
  it asks `worktrees/knowledge_crossing.unconverted_line_refusal` whether the official memory branch's tip
  is already converted. If it is, `knowledge-ingest` prints the refusal, naming the crossing sync, and exits
  refused before the database route reads anything. Otherwise it returns `None` and the database route runs
  as before. **Inert until the official line is converted (architect ruling, 2026-09-29):** no line is
  converted before MIK-R37, so no run changes today.
- Exit status: 0 written or planned, 1 refused (every problem in the report, nothing written), 2 invocation
  refused. `--json` prints `WriteReport.to_document()`.
- **`run_crossing_write(args, contract)` (L37, MIK-R24 rule 8 step 4)** is `knowledge-ingest --crossing`. It
  refuses a blank authorization or a database-only flag (`_file_route_refusal`), then asks
  `_crossing_memory_root`, which refuses by name: a contract that cannot be loaded or is not a series contract;
  an id that is not `<this master's task id>-crossing-<n>`; a history file that is absent, is not that
  crossing's, or is closed. The memory root is the sync's memory worktree (`side_locations(contract,
  "memory")`). The code snapshot C is the series' code work branch (`CodeSnapshot.at_commit`), the sync's paired
  code, and the same ref is passed as `code_base`. The owner is `Owner(kind="crossing", id=<crossing>)`, so the
  writer resolves existing records and writes rows only.
- **`run_leaf_write` passes `code_base=contract.code_base_commit`** (L37, review R1 F10b): the commit a
  trailerless unconverted `HEAD` is converted at, which is the gate's and the worklist's fallback, so the three
  share one converted-base cache key.

### Conventions

- Imported by `cli/knowledge_ingest.py` and `cli/knowledge_bootstrap.py`; not registered as its own subcommand.

### Invariants And Boundaries

- No database write happens on this route, and no argument is silently ignored.
- `--commit` stays the commit word: without it the run plans, validates and reports.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R12@v2` of task
`260928_maintained-invariant-knowledge` (with its architect rulings in the task's leaf document
`12_category-authoring-through-the-curator-workflow.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The dispatch test and the two routes.

- The database-only flags refused by name. [1]
- The layout-marker test. [2]
- The write refusal for an unconverted leaf tree: rule 9 when its official line is converted, else the cutover lock. [3]
- The owner from the contract and `task.json`. [4]
- The task owner's decision resolver for the leaf (MIK-R11). [5]
- The leaf route, which binds that resolver and, since MIK-R14, the lazy task-document port and the persisted worklist. [6]
- The lazy port: settings read only when a `raise` needs them, from `--config` or discovery; unavailable settings refuse the `raise`. [7]
- The wave route. [8]
- The ingest dispatch on the loaded contract. [9]
- The bootstrap dispatch on the admitted memory root. [10]
- Planning writes nothing; unconverted memory is not this route. [11]
- Blank authorization refused and recorded. [12]
- The leaf route and the wave route pass the coordination root requirement endpoints resolve against (MIK-R13). [13]

- The crossing owner's route: the sync's memory worktree, the series' code work branch as C. [14]
- Which worktree holds the open crossing history file, or why the run is refused. [15]
- The file route refuses a blank authorization and database-only flags. [16]

### Cross-Repo References

No cross-repo boundary is crossed: the writer reads the paired code worktree and writes the paired memory
worktree of one repository.

No cross-repo boundary is crossed by this file.
