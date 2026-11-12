# skills/l-01-agent-lifecycles/reference/knowledge/commands.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Maps the public knowledge, workflow, runtime and settings commands and the knowledge-related MCP tools to their effects, callers, bindings and owning sources, for all eight roles. It grants no write, review, commit, integration or cleanup authority.

## Code Commentary

Task contracts, role gates and independent acceptance stay in force: producer lists describe observed code, and the Curator authors knowledge judgments. Examples use illustrative repository, root, contract and evidence paths that callers replace with their supplied bindings, and leaf readers keep their complete supplied `task_context`. CLI work is bound through `serving-build.md`; an `agents-remember` command found through `PATH` can select an older build, and leaf-produced code cannot write its own memory.

The CLI tables cover the knowledge and memory subcommands (`handoff-check`, `knowledge-ingest`, `knowledge-bootstrap`, `knowledge-format`, `knowledge-validate`, `knowledge-index`, `knowledge-worklist`, `knowledge-routes`, `memory-citations`) and runtime commands (`dashboard`, `paseo` with `provision`, `status` and `stop`, `tool-log-stats`), each with effect, caller and example; `start-leaf-enclosure` is an internal dashboard dispatcher branch, not an agent's worktree route. The tool tables cover `knowledge_read`, `knowledge_diff`, `knowledge_integrity_check` and `knowledge_write`, then supporting workflow tools from server information and context through citation, memory, carryover, coherence, sync and closeout tools, keeping their write effects, previews and role gates rather than treating all of them as read-only. Asynchronous quality and citation runs are polled with their returned run identifier, and a started run is not clean.

The producer-check section runs `handoff-check` with the serving interpreter against the exact frozen tree before a freeze's producer list is sent; it checks list shape, targets, proofs and repoint shapes through writer readers, leaves fired-link judgment to the writer, writes nothing, reports exit codes 0, 1 and 2, and a `PASS` does not prove later writer admission. The last section names the CLI and MCP registration sources that own arguments and request shapes, so no parallel tool surface is invented.

## Evidence

- The reference grants no authority, keeps task contracts and binds examples and CLI work to supplied bindings and the serving build. [1]
- The public CLI tables give each subcommand's effect, caller and example, and name the internal dispatcher branch. [2]
- The knowledge and workflow tool tables keep write effects, previews and role gates. [3]
- Asynchronous results are polled with their run identifier, and a started run is not clean. [4]
- Producer checking resolves the named frozen tree and leaves writer judgment and publication separate. [5]
- The owning CLI and MCP sources are named. [6]
