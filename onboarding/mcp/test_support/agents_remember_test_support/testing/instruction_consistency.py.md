# mcp/test_support/agents_remember_test_support/testing/instruction_consistency.py

## Governing Overview

[overview](overview.md)

## Purpose

The module checks that executable names in the instruction and document corpus exist: command names against the real CLI parser, tool names against live MCP tool registration, `task_doc` operations against the dispatcher, and cited repository paths against the tree.

## Code Commentary

`load_registry` builds the vocabularies by walking the CLI parser's subcommands (plus the leaf-enclosure start command), registering every tool registrar on an unstarted FastMCP server and listing its tools, and taking `VALID_OPERATIONS`. `read_corpus` reads every UTF-8 text file under `skills/` and `docs/` plus the root `README.md`. `check_consistency` reports retired terms (exempt only on a line carrying the conversion marker), unregistered commands and tools, unknown task-document operations, missing paths, and knowledge command or tool names undocumented in `skills/` or `docs/reference/`. A migration command name that serves only an earlier installation is not required to have a documentation row, and a row of the agents' command table that names one is refused; a mention is not refused. Existence-only fields of the capsule-budget and digest-map records are masked as history after their owner pins are checked; the current budget record's skill-relative paths must exist unless they sit in a removal list or a historical renewal sub-record. Readers are `mcp/tests/test_instruction_consistency.py` and `mcp/tests/test_role_instruction_corpus.py`.

## Evidence

- Commands, tools and operations come from the real parser, live registration and the dispatcher, without starting a server. [1]
- The corpus is every text file in skills and docs plus the root README. [2]
- Per-line findings cover retired terms, unregistered names, unknown operations and missing paths. [3]

- The full check adds knowledge-name coverage; a migration command of an earlier installation needs no documentation row. [4]
