# mcp/test_support/agents_remember_test_support/testing/instruction_consistency.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks that executable names in the instruction and document corpus exist: command names against the real CLI parser, tool names against live MCP tool registration, `task_doc` operations against the dispatcher, and cited repository paths against the tree.

## Code Commentary

`load_registry` builds the vocabularies by walking the CLI parser's subcommands (plus the leaf-enclosure start command), registering every tool registrar on an unstarted FastMCP server and listing its tools, and taking `VALID_OPERATIONS`. `read_corpus` reads every UTF-8 text file under `skills/` and `docs/` plus the root `README.md`. `check_consistency` reports retired terms (exempt only on a line carrying the conversion marker), unregistered commands and tools, unknown task-document operations, missing paths, and knowledge command or tool names undocumented in `skills/` or `docs/reference/`. The consistency check refuses an agents' command-table row for a name in `UNDOCUMENTED_COMMANDS` and permits mentions outside that table. The set includes `knowledge-convert-states` for the operator's one-time state conversion. `explainer-browser` is one of those names held outside the role instruction table: a person at the installation runs it to see or fetch the browser the explainer publishes with, no role has a step for it, and the install page and the guide tell it. The reader checks owner schemas and source bytes, verifies frozen budget-owner pins, and masks existence-only historical fields. The renewable digest map has no frozen owner-hash check. The current budget record's skill-relative paths must exist unless they sit in a removal list or a historical renewal sub-record. Readers are `mcp/tests/test_instruction_consistency.py` and `mcp/tests/test_role_instruction_corpus.py`.

## Evidence




- The full check applies command-table coverage and reserves entries in UNDOCUMENTED_COMMANDS outside the table. [4]

- The parser, tool registration and task-document dispatcher supply executable vocabularies. [1]
- The reader takes UTF-8 text from the instruction and document corpus. [2]
- The consistency check reports invalid terms, names, operations and paths. [3]
