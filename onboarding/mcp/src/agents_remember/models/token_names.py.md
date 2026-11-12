# mcp/src/agents_remember/models/token_names.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The tokenizer's name, declared in a module light enough that a page header can read it without loading the counter.

## Code Commentary

- The counter's own module imports `tiktoken`; a reader that wants only the name should not pay that import cost at startup, so the string has one light owner here.
- The name stays beside the counter in meaning and apart from it in import cost, and the two are pinned together so they cannot drift.
- Nothing but the annotations future is imported, which is what keeps reading the name free of the tokenizer.

## Evidence

- The tokenizer's name is one literal with no computation at import [1]
- Only the name is exported, so this module offers no counter [2]
- Reading the name imports nothing that loads the tokenizer [3]
