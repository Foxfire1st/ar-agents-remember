# mcp/src/agents_remember/kernel/coordination_context/serialize.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`serialize.py` owns JSON-safe and text formatting for resolved coordination
contexts.

## Code Commentary

`cross_repo_entry_to_dict` always emits repo, expectedBranch, includeCode and includeMemory. State, reason, code and memory are emitted only when truthy; unset cross-repository optionals are omitted rather than null. This differs from context path fields, whose absent values use empty strings. `path_to_string` resolves filesystem paths before formatting them. cit:([`path_to_string`, `cross_repo_entry_to_dict`], mcp/src/agents_remember/kernel/coordination_context/serialize.py:15-16; mcp/src/agents_remember/kernel/coordination_context/serialize.py:42-57).

### Logic

The module converts `CoordinationContext`, storage rules, and cross-repo
entries into dictionaries with string paths and stable keys. `print_text()`
emits the legacy tab-separated text format used by the CLI.

### Invariants And Boundaries

- Serialization does not mutate the context; path formatting resolves paths through `path_to_string`.
- Empty optional paths serialize as empty strings in JSON output, preserving the
  old resolver contract.

## Evidence

### Docs References

No external documentation is needed for this local formatter.

No relevant external documentation is needed.

### Repo-Internal References

- The CLI delegates JSON/text output to this module. [1]
- The application context packet builds the packet with `context_to_dict()`. [2]

### Cross-Repo References

No cross-repository evidence is needed for this formatter.

No meaningful cross-repo references found.
