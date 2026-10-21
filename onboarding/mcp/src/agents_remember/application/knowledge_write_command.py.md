# mcp/src/agents_remember/application/knowledge_write_command.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The command-line write route's own value and the causes it can meet, plus the one remedy a refused `raise` names (MIK-R194 rule 9).** A command-line leaf write publishes a `raise` only where it can load trusted settings: with no trusted settings at or above the working directory, the checkout guard refusing the run, an unloadable settings file, or settings for another coordination root, the question cannot be published and the refusal names the mounted route. This module holds what the command knows about itself (`CommandRoute`), the sorting of the causes into fixed clauses (`discovered_settings`, `checked_guard`, `CHECKOUT_GUARD_CLAUSE`) and the sentence that sends the same hand-off through the mounted `knowledge_write` (`mounted_route`). The command's own value, causes and remedy are here, and `cli/knowledge_write_route.py` keeps its own copy of the guard constant beside the calls that use it.

## Code Commentary

### Logic

- `CommandRoute` is a frozen dataclass. `settings` is a zero-argument loader that either resolves the MCP authority settings or returns the one clause saying why it cannot; `handoff_path`, `handoff_name`, `contract_path` and `authorization_ref` are what the mounted call needs to repeat this exact hand-off.
- `mounted_route(route, clause)` composes the refusal: this command cannot reach the leaf's task document, the clause naming the cause, then the mounted `knowledge_write` call with `contractPath` (absolute), `handoffPath` (absolute), `handoffName` (the label the command records), `authorizationRef`, and "preview, then commit: true". Nothing in the text mentions `--config`, which no route reads.
- `checked_guard(guard)` runs the checkout guard and answers `None` when it admits the run, `CHECKOUT_GUARD_CLAUSE` when it raises — whatever the exception's own text is, because a clause is never an error's own text.
- `discovered_settings(cwd, discover=…, guard=…, load=…, unreadable=…)` sorts the causes in the order the write meets them: no trusted settings at or above `cwd`; the checkout guard's clause; a settings file that cannot be loaded; otherwise the loaded settings. The fourth cause — settings naming another coordination root — is the caller's comparison against the contract, so this module does not perform it.
- The three moves are parameters rather than imports, so this module holds the sorting and imports nothing from the command layer; `cli/knowledge_write_route.command_settings()` supplies the real `discover_config`, `checkout_cli_location` and `load_config`, and its `unreadable` tuple is the error family a load may raise.

### Conventions

- A clause is a fixed sentence, never an error's own text and never a second route; the one route a refusal names is the mounted call that runs the same writer.
- The value is frozen, and its loader is called at most once per write: `LeafQuestions` resolves it lazily, only when a `raise` row needs the task document.

### Invariants And Boundaries

- **This module decides no write.** It names causes and a remedy; the contract guard, the worklist checks and the refusal set stay with `application/knowledge_write_route.py`. Both routes refuse under the same conditions (INV-AG8G8C).
- **The command route publishes no raise where it cannot load trusted settings.** A run in a refused checkout or with no usable settings states why and names the mounted tool as the remedy; with agreeing settings the same `_command` path returns `_task_doc`, so the raise is published as the mounted route publishes it, and the port is built in `LeafQuestions._task_doc`.
- **The mounted route's texts are unchanged.** Only the command route's remedy names a route; the mounted route keeps its own sentences.

## Evidence Scope

This is a current source account, not an executed test, CODE/MEMORY grade, live producer grant or landing result. No Domain Documentation source is configured for this slice; no external-system guarantee is inferred.

## Evidence


- The command-line route's own value, its sorted causes and the remedy sentence live in this module and are what a refusal emits; `mcp/src/agents_remember/cli/knowledge_write_route.py` keeps its own copy of the guard constant. [7]

- `CommandRoute` is a frozen dataclass holding the settings loader and the hand-off path, hand-off label, contract path and authorization reference the mounted call repeats. [2]
- The refusal names one clause, then the mounted `knowledge_write` call with contractPath, handoffPath, handoffName, authorizationRef and "preview, then commit: true", and mentions no settings option. [3]

- The guard's clause is a module constant here, so the same sentence reaches a refusal whichever cause met it, and the CLI module's own constant is a copy this module does not read. [8]

- `checked_guard` answers `None` when the guard admits the run and the fixed clause when it raises, embedding no exception text. [5]
- `discovered_settings` sorts the causes in the order met — no trusted settings at or above the working directory, the guard, an unloadable settings file, else the loaded settings — and leaves the other-root comparison to the caller. [6]
