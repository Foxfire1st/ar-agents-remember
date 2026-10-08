# mcp/tests/test_knowledge_cutover.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

Checks the converted-memory cutover lock across the admitted write/closeout/sync routes and the refusal of canonical database reads.

## Code Commentary

The probes distinguish a definite repository absence from an unreadable or ambiguous Git repository, cover a converted worktree locking an unconverted route, and permit the converting candidate only through its gate. A read case asserts that no read selects a database for a converted tree; another validates hand-off evidence as strings. The old database-writer-freeze test is removed and cannot be cited as a current writer execution. These source assertions are not a current run certificate.

## Evidence

### Repo-Internal References

- `test_every_route_refuses_unconverted_memory_once_the_repository_holds_converted_memory` owns the current boundary described above. [11]
- `test_no_read_selects_the_database_of_a_converted_tree` owns the current boundary described above. [12]
- `test_a_converted_worktree_locks_too_and_an_unanswered_probe_refuses` owns the current boundary described above. [13]
