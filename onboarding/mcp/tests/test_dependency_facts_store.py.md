# mcp/tests/test_dependency_facts_store.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves the disposable dependency-facts store preserves source-derived facts while avoiding repeated
AST parsing. Reuse is measured through parse/read counts and exact field equality, never speed.

## Code Commentary

The fixture supplies repository-relative inventory paths. Tests compare stored and no-store facts,
then change source, module/package identity, Python version, implementation bytes and population.
Only changed identities are reparsed. Population shrinkage and obsolete or invalid store rows
exercise bounded compaction. Syntax and dynamic-plugin failures remain visible on repeated builds.
Unreadable, malformed, wrong-shaped, foreign-owned, symlink and directory stores cannot decide
correct source analysis or damage a foreign target. Deep malformed entries exercise recursion
failure and leave no temporary file.

## Evidence

These repository-owned cache controls require no external domain claim.


- Equal facts and parse counts prove reuse, invalidation and compaction. [1]
- Bad source and dynamic plugins are reparsed and refused on every build. [2]
- Unsafe stores recompute correctly without changing the foreign target. [3]
- Module, package, Python and implementation identities govern reuse. [4]
- Deep wrong-shaped entries preserve no-store facts and reclaim temporary files. [5]
