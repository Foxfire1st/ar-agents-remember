# mcp/src/agents_remember/cli/knowledge_write_route.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

The converted knowledge CLI's file-write routes share admission, owner identity, decision inputs, report rendering, and the one remedy a refused `raise` names (MIK-R194 rule 9).

## Code Commentary

Leaf writes use the supplied enclosure and its leaf owner; named waves use their admitted repository root. Crossing writes retain their separately admitted crossing owner. Each delegates to the file writer rather than selecting a canonical database. `unconverted_write_refusal` refuses unconverted memory unconditionally with shared conversion guidance: cross from a converted source through `worktree_sync` with `merge-memory`, otherwise make the first conversion described by `c-13-install-and-onboard` and `docs/guides/first-conversion.md`. A missing memory worktree retains its own named error. Database-publication arguments are refused by their CLI front door, not accepted here as an alternative destination. The removed `_file_route_refusal` and legacy dataset writer dispatch are not current routes.

### Logic

Before calling `write_knowledge`, `run_leaf_write` reads the persisted leaf worklist and refuses unreadable or invalid-shaped input with its path and compute/recompute remedy. It passes that admitted value, rather than fabricating one. `LeafQuestions` also forwards `append_many` and the resolved destination lazily; loaded settings must resolve to the contract’s same coordination root before a task_doc port is created. This does not add a leaf-worklist prerequisite to wave/crossing owners.

- `leaf_owner`: the leaf is the contract's `leaf_id` (else task name); the task is `task.json` `id`, else the
  leaf ID's prefix before `-L<n>`.
- **`run_leaf_write` passes a `CommandRoute`, not settings.** It reads the hand-off document and the contract
  first, takes the label `handoff_label(list_path, contract.task_root)` returns, and builds the route from
  `command_settings`, the list's resolved absolute path, that label, the contract's resolved absolute path
  and the authorization reference; the worklist preflight runs inside the shared route, after the document is
  read. The same label is the submission's `handoff_path`, so the mounted call the refusal names records the
  hand-off exactly as this command would.
- **`command_settings` decides no cause.** It delegates to
  `knowledge_write_command.discovered_settings` over `Path.cwd()`, handing it this command's own three moves —
  `discover_config`, `checkout_cli_location`, `load_config` — and the error family a load may raise
  (`AgentsRememberError`, `OSError`, `ValueError`). It answers the settings or the one fixed clause naming the
  cause; no error's own text is embedded. The clause is the guard's clause when the checkout guard refuses, so
  an undeclared run from the primary checkout is told the mounted `knowledge_write` call that works rather
  than a route that is then refused. `CHECKOUT_GUARD_CLAUSE` carries that sentence in this module too; the
  clause a refusal actually receives is the one `application.knowledge_write_command` returns.
- **`LeafQuestions` (MIK-R14) lives in `application/knowledge_write_route.py`.** It is a `dataclass` over the
  contract and either the mounted server's `config` or this command's `CommandRoute`, implementing the writer's
  `OpenQuestions` port lazily: the settings loader runs only when a `raise` needs them (`check` or `append`).
  A returned clause becomes `UnavailableOpenQuestions` carrying the `mounted_route` text — the cause, then
  `contractPath`, `handoffPath`, `handoffName` and `authorizationRef` with "preview, then commit: true" — so the
  `raise` is refused and nothing is written and the Curator is handed the route that publishes the same
  hand-off. Settings for another coordination root are refused the same way, naming both roots. A run with only
  `still_rejected` rows never reads settings. The worker's real evidence ran the scratch answer with
  `declare_execution_mode("test")`, because checkout-CLI mode substitutes synthetic settings for a discovered
  one; the installed-mode check is carried to L37 (review F10).
- `run_wave_write` (`knowledge-bootstrap`): a bootstrap has no leaf, so it writes as the wave `--wave` names
  (`[A-Za-z0-9._-]`); its history file is `knowledge/history/<wave>.json` (MIK-R07 rule 8); the task is
  the bootstrap scope (architect ruling 2). Since MIK-R13 it takes an optional keyword `coordination_root` (default `None`) and
  passes it to `WriteRequest`; `cli/knowledge_bootstrap._run` passes the admitted authority's root. Without
  it every requirement endpoint is reported `requirement-task-plane-unavailable`. A wave has no contract and no
  `raise`, so it passes no route and reads no settings.
- Exit status: 0 written or planned, 1 refused, 2 invocation refused. `--json` prints `WriteReport.to_document()`. A refused state alone is not universal zero-publication evidence: separately reported question publication and native rollback outcomes retain their exact custody. Do not repeat a mutator to recover its result.
- **`run_leaf_write` passes `code_base=contract.code_base_commit`** (L37, review R1 F10b): the commit a
  trailerless unconverted `HEAD` is converted at, which is the gate's and the worklist's fallback, so the three
  share one converted-base cache key.

`_leaf_memory_base` resolves the memory commit paired to the contract code base on the memory source branch. `run_leaf_write` passes that result to WriteRequest: the paired base governs counted-card comparison. Missing pairing inputs or lookup failure yield None, retaining the downstream fallback rather than inventing a base. Lazy settings/question ownership is unchanged.

### Conventions

- Imported by `cli/knowledge_ingest.py` and `cli/knowledge_bootstrap.py`; not registered as its own subcommand.
- `command_settings` is a plain zero-argument callable, which is why `CommandRoute` holds it rather than a
  resolved value: nothing resolves settings until a `raise` row asks.

### Invariants And Boundaries

- No database write happens on this route, and no argument is silently ignored.
- `--commit` stays the commit word: without it the run plans, validates and reports.
- **No argument supplies settings.** The adapter declares no `--config` and imports no `require_config_path`;
  the command resolves its own settings or names, in one fixed clause, why it cannot.
- **A refused raise names the mounted call, never a route that also refuses.** The clause says which cause was
  met and the remedy is `knowledge_write`, so the Curator is not sent to a worktree the root check then refuses
  (MIK-R194 rule 9).

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence

- The adapter declares no settings option and imports no `require_config_path`: a caller cannot pass the authority a `raise` would need. [36]
- `run_leaf_write` builds the command route from `command_settings`, the hand-off list's resolved absolute path, the recorded label, the contract's resolved absolute path and the authorization reference, and passes the same label as the submission's hand-off. [37]
- `command_settings` delegates to `knowledge_write_command.discovered_settings` with this command's discover, guard and load moves plus the unreadable error family, returning settings or one fixed clause. [38]
- The guard's clause is also spelled in this module; the clause a refusal receives is the one the command module returns. [39]
- The wave route writes a taskless wave and takes no route, so a bootstrap reads no settings. [40]
