# mcp/test_support/agents_remember_test_support/code_quality/single_owner.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Enforce single owners for git, atomic publish, and task-document publication.

## Code Commentary

### Logic

Module-level surface:

The task-document publication census recognizes all three canonical store calls:
`write_task_doc`, `write_task_docs`, and cross-root `write_task_doc_batch`. Direct imports,
renamed imports, module aliases, and relative imports resolve to the same API set, and only the
reviewed writer-authority modules may call them.

- `Offender` (class, lines 75-84) — One place the primitive is reached outside its owner.
- `package_modules` (function, lines 91-93) — Every module the rules apply to, in a stable order.
- `names_git` (function, lines 96-102) — Whether a program token names the git binary.
- `string_constants` (function, lines 105-128) — Names bound to a string literal, so ``BINARY = "git"`` cannot launder the program word.
- `imported_names` (function, lines 131-142) — Bare names this module bound via ``from <module_name> import <wanted>``.
- `_module_package` (function, lines 145-148) — The dotted package containing a module path relative to ``agents_remember``.
- `_import_from_origin` (function, lines 151-160) — Resolve one absolute or relative ``from`` import to its dotted module.
- `_task_writer_bindings` (function, lines 163-187) — Return bare writer aliases and module aliases bound by imports.
- `_dotted_name` (function, lines 190-196)
- `_task_writer_call` (function, lines 199-213)
- `module_task_document_writer_sites` (function, lines 216-233) — Every canonical task-document writer definition/call in one production module.
- `_token` (function, lines 236-242) — The string this expression is statically known to be, or ``None``.
- `_argv_head` (function, lines 245-249) — The program word of an argv display, or ``None`` when this is not one.
- `_spawn_kind` (function, lines 252-265) — ``"program"``, ``"shell"``, ``"argv"`` -- how this spawn names what it runs.
- `_program_token` (function, lines 268-283) — What this spawn will execute, when that can be read off the syntax tree.
- `_git_spawn_offenders` (function, lines 286-306) — Spawns of git, plus the argv nodes those spawns already account for.
- `_git_argv_offenders` (function, lines 309-322) — Git argv under construction, wherever it is later spawned.
- `module_git_offenders` (function, lines 325-330) — Every git-program reference in one parsed module, ordered by line.
- `module_replace_offenders` (function, lines 333-342) — Every reach for the replace syscall in one parsed module, ordered by line.
- `_replace_offender` (function, lines 345-362)
- `_sweep` (function, lines 365-374) — Apply one per-module rule to every module except the primitive's owner.
- `git_program_offenders` (function, lines 377-379) — Every place outside :data:`GIT_RUNNER_OWNER` that names the git program.
- `os_replace_offenders` (function, lines 382-384) — Every place outside :data:`ATOMIC_WRITE_OWNER` that reaches the replace syscall.
- `task_document_writer_sites` (function, lines 387-394) — The executable census of production task-document publication authorities.
- `task_document_writer_offenders` (function, lines 397-403) — Task-document writer sites outside the reviewed authority set.
- `report` (function, lines 406-415) — The whole offender list with the fix named -- never just the first failure.

The single-owner registry now names `worktrees/modules/start.py` and `worktrees/organizational_completion.py` instead of the retired `tasks/leaf_doc.py`. Since 260815-DAG-L14 it also admits `application/task_sprint_linkage.py` as a reviewed task-document writer authority — attach/detach publish through the same locked, queue-guarded `write_task_doc_batch` boundary as graph authoring.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `Offender` (lines 75-84) — One place the primitive is reached outside its owner.. [1]
- Defines the function `package_modules` (lines 91-93) — Every module the rules apply to, in a stable order.. [2]
- Defines the function `names_git` (lines 96-102) — Whether a program token names the git binary.. [3]
- Defines the function `string_constants` (lines 105-128) — Names bound to a string literal, so ``BINARY = "git"`` cannot launder the program word.. [4]
- Defines the function `imported_names` (lines 131-142) — Bare names this module bound via ``from <module_name> import <wanted>``.. [5]
- Defines the function `_module_package` (lines 145-148) — The dotted package containing a module path relative to ``agents_remember``.. [6]
- Defines the function `_import_from_origin` (lines 151-160) — Resolve one absolute or relative ``from`` import to its dotted module.. [7]
- Defines the function `_task_writer_bindings` (lines 163-187) — Return bare writer aliases and module aliases bound by imports.. [8]
- Defines the function `_dotted_name` (lines 190-196). [9]
- Defines the function `_task_writer_call` (lines 199-213). [10]
- Defines the function `module_task_document_writer_sites` (lines 216-233) — Every canonical task-document writer definition/call in one production module.. [11]
- Defines the function `_token` (lines 236-242) — The string this expression is statically known to be, or ``None``.. [12]
- Defines the function `_argv_head` (lines 245-249) — The program word of an argv display, or ``None`` when this is not one.. [13]
- Defines the function `_spawn_kind` (lines 252-265) — ``"program"``, ``"shell"``, ``"argv"`` -- how this spawn names what it runs.. [14]
- Defines the function `_program_token` (lines 268-283) — What this spawn will execute, when that can be read off the syntax tree.. [15]
- Defines the function `_git_spawn_offenders` (lines 286-306) — Spawns of git, plus the argv nodes those spawns already account for.. [16]
- Defines the function `_git_argv_offenders` (lines 309-322) — Git argv under construction, wherever it is later spawned.. [17]
- Defines the function `module_git_offenders` (lines 325-330) — Every git-program reference in one parsed module, ordered by line.. [18]
- Defines the function `module_replace_offenders` (lines 333-342) — Every reach for the replace syscall in one parsed module, ordered by line.. [19]
- Defines the function `_replace_offender` (lines 345-362). [20]
- Defines the function `_sweep` (lines 365-374) — Apply one per-module rule to every module except the primitive's owner.. [21]
- Defines the function `git_program_offenders` (lines 377-379) — Every place outside :data:`GIT_RUNNER_OWNER` that names the git program.. [22]
- Defines the function `os_replace_offenders` (lines 382-384) — Every place outside :data:`ATOMIC_WRITE_OWNER` that reaches the replace syscall.. [23]
- Defines the function `task_document_writer_sites` (lines 387-394) — The executable census of production task-document publication authorities.. [24]
- Defines the function `task_document_writer_offenders` (lines 397-403) — Task-document writer sites outside the reviewed authority set.. [25]
- Defines the function `report` (lines 406-415) — The whole offender list with the fix named -- never just the first failure.. [26]

## 260815-DAG Master Full-Gate Repair

`TASK_DOCUMENT_WRITER_AUTHORITIES` paths updated to the moved package locations (`application/task_docs/{task_doc_tools,task_execution_topology,task_sprint_linkage}.py`, `worktrees/integration/organizational_completion.py`); the authority set is unchanged.

## 260821-CLIVE-L2 Task-Document Writer Census

The static single-owner census now recognizes `task_doc_publication.py` as the publication owner and
removes the superseded organizational-completion writer entry. This is an authority-list correction,
not a compatibility alias: current writes must route through the owners named by the census.

- The task-document writer allowlist names the extracted publication owner and no longer names organizational completion. [27]
