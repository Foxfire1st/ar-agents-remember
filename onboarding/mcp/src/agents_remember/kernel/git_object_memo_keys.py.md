# mcp/src/agents_remember/kernel/git_object_memo_keys.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Own the exact-object eligibility predicates used by the request-scoped Git runner memo. State, keys, native execution and successful-result retention stay in `git_command.py`.

## Code Commentary

Bare object names must be exact 40/64-character hex values. Supported tree/commit peels qualify only with replacement disabled; malformed or suffixed inputs, replacement-sensitive reads, mutable ref/index reads and content/type reads remain native. The runner separately admits the exact `rev-parse --path-format=absolute --git-path index --show-toplevel` location query for successful-result reuse within one request under the same effective execution. This execution-pure query locates the index and repository root; it does not read or reuse mutable index contents. Full matching preserves the newline/suffix refusal boundary. The runner imports the predicates directly.

## Evidence

- Exact-object and supported-peel predicates decide eligibility without holding memo state. [1]

- The runner admits one exact execution-pure index-location argv, and the retained test asserts that two identical queries start one child. This is distinct from mutable index reads. [2]
