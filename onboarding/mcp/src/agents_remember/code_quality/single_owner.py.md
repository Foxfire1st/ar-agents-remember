# mcp/src/agents_remember/code_quality/single_owner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/code_quality/single_owner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Enforce single owners for git, atomic publish, and task-document publication.

## Code Commentary

### Logic

Module-level surface:

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

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Offender` (lines 75-84) — One place the primitive is reached outside its owner.. | `Offender` | mcp/src/agents_remember/code_quality/single_owner.py:74-84 |
| Defines the function `package_modules` (lines 91-93) — Every module the rules apply to, in a stable order.. | `package_modules` | mcp/src/agents_remember/code_quality/single_owner.py:91-93 |
| Defines the function `names_git` (lines 96-102) — Whether a program token names the git binary.. | `names_git` | mcp/src/agents_remember/code_quality/single_owner.py:96-102 |
| Defines the function `string_constants` (lines 105-128) — Names bound to a string literal, so ``BINARY = "git"`` cannot launder the program word.. | `string_constants` | mcp/src/agents_remember/code_quality/single_owner.py:105-128 |
| Defines the function `imported_names` (lines 131-142) — Bare names this module bound via ``from <module_name> import <wanted>``.. | `imported_names` | mcp/src/agents_remember/code_quality/single_owner.py:131-142 |
| Defines the function `_module_package` (lines 145-148) — The dotted package containing a module path relative to ``agents_remember``.. | `_module_package` | mcp/src/agents_remember/code_quality/single_owner.py:145-148 |
| Defines the function `_import_from_origin` (lines 151-160) — Resolve one absolute or relative ``from`` import to its dotted module.. | `_import_from_origin` | mcp/src/agents_remember/code_quality/single_owner.py:151-160 |
| Defines the function `_task_writer_bindings` (lines 163-187) — Return bare writer aliases and module aliases bound by imports.. | `_task_writer_bindings` | mcp/src/agents_remember/code_quality/single_owner.py:163-187 |
| Defines the function `_dotted_name` (lines 190-196). | `_dotted_name` | mcp/src/agents_remember/code_quality/single_owner.py:190-196 |
| Defines the function `_task_writer_call` (lines 199-213). | `_task_writer_call` | mcp/src/agents_remember/code_quality/single_owner.py:199-213 |
| Defines the function `module_task_document_writer_sites` (lines 216-233) — Every canonical task-document writer definition/call in one production module.. | `module_task_document_writer_sites` | mcp/src/agents_remember/code_quality/single_owner.py:216-233 |
| Defines the function `_token` (lines 236-242) — The string this expression is statically known to be, or ``None``.. | `_token` | mcp/src/agents_remember/code_quality/single_owner.py:236-242 |
| Defines the function `_argv_head` (lines 245-249) — The program word of an argv display, or ``None`` when this is not one.. | `_argv_head` | mcp/src/agents_remember/code_quality/single_owner.py:245-249 |
| Defines the function `_spawn_kind` (lines 252-265) — ``"program"``, ``"shell"``, ``"argv"`` -- how this spawn names what it runs.. | `_spawn_kind` | mcp/src/agents_remember/code_quality/single_owner.py:252-265 |
| Defines the function `_program_token` (lines 268-283) — What this spawn will execute, when that can be read off the syntax tree.. | `_program_token` | mcp/src/agents_remember/code_quality/single_owner.py:268-283 |
| Defines the function `_git_spawn_offenders` (lines 286-306) — Spawns of git, plus the argv nodes those spawns already account for.. | `_git_spawn_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:286-306 |
| Defines the function `_git_argv_offenders` (lines 309-322) — Git argv under construction, wherever it is later spawned.. | `_git_argv_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:309-322 |
| Defines the function `module_git_offenders` (lines 325-330) — Every git-program reference in one parsed module, ordered by line.. | `module_git_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:325-330 |
| Defines the function `module_replace_offenders` (lines 333-342) — Every reach for the replace syscall in one parsed module, ordered by line.. | `module_replace_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:333-342 |
| Defines the function `_replace_offender` (lines 345-362). | `_replace_offender` | mcp/src/agents_remember/code_quality/single_owner.py:345-362 |
| Defines the function `_sweep` (lines 365-374) — Apply one per-module rule to every module except the primitive's owner.. | `_sweep` | mcp/src/agents_remember/code_quality/single_owner.py:365-374 |
| Defines the function `git_program_offenders` (lines 377-379) — Every place outside :data:`GIT_RUNNER_OWNER` that names the git program.. | `git_program_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:377-379 |
| Defines the function `os_replace_offenders` (lines 382-384) — Every place outside :data:`ATOMIC_WRITE_OWNER` that reaches the replace syscall.. | `os_replace_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:382-384 |
| Defines the function `task_document_writer_sites` (lines 387-394) — The executable census of production task-document publication authorities.. | `task_document_writer_sites` | mcp/src/agents_remember/code_quality/single_owner.py:387-394 |
| Defines the function `task_document_writer_offenders` (lines 397-403) — Task-document writer sites outside the reviewed authority set.. | `task_document_writer_offenders` | mcp/src/agents_remember/code_quality/single_owner.py:397-403 |
| Defines the function `report` (lines 406-415) — The whole offender list with the fix named -- never just the first failure.. | `report` | mcp/src/agents_remember/code_quality/single_owner.py:406-415 |

## Update History

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
