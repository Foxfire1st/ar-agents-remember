# mcp/tests/test_writer_merge_bases.py

## Governing Overview

[MCP test overview](overview.md)

## Purpose

Prove that during a real in-progress memory merge the knowledge writer and the memory-quality check validate against both merge parents, `HEAD` and `MERGE_HEAD`, and that a parent they cannot read or convert refuses by name.

## Code Commentary

Every case runs `git merge --no-ff --no-commit` in a disposable converted memory repository, so `MERGE_HEAD` resolves while the writer runs.

During the merge, the writer plans without an `R22.6-anchor-path` refusal for the anchor the incoming side carries and reports it as `R22.6-carried-stale`; `writer_bases` names `memory@HEAD` and `memory@MERGE_HEAD` with the files of each parent, and the check's base port (`context_check_base`) sees the same two bases, so `converted_knowledge_check` raises no finding the writer was allowed to write. Outside a merge (a completed merge soft-reset onto `HEAD`), `HEAD` is the only base and the same anchor refuses as newly written. A `MERGE_HEAD` blob that is missing, or an incoming parent that cannot be converted, makes the writer refuse with a sentence naming the memory worktree's `MERGE_HEAD`.

## Relationships

It exercises `application/knowledge_writer/base_side.writer_bases`, `application/memory_quality/converted_base.context_check_base` and `memory_quality/converted_check.converted_knowledge_check`, through `writer_worklist_test_support.write_knowledge`. Converted fixtures come from `knowledge_conversion_test_support`.

## Evidence

- The writer and the check validate a real merge against both parents. [1]
- Outside a merge the writer keeps its one `HEAD` base and refuses the new anchor. [2]
- An unreadable or unconvertible `MERGE_HEAD` refuses by name. [3]
