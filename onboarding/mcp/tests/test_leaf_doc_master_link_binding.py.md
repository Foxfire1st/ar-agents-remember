# mcp/tests/test_leaf_doc_master_link_binding.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proof that a leaf authored before its series contract exists gets its master link bound at start, over a real coordination root, code repository and Git-backed memory repository.

## Code Commentary

Each case builds one scratch coordination root, one code repository and one external memory repository, authors both documents through the real `task_doc` plane, and drives the real public start. `_start_leaf` runs `worktree_start` with `memory_mode="external"`, so the binding proof exercises the only supported topology. The four cases are unchanged in intent: the pre-contract leaf gets its series-contract path, enclosure ref and lifecycle stamp at start; an already-damaged document is repaired additively; a leaf with no master document is refused with its remedy and writes nothing; and master-first planning stays usable with leaves unstamped until start.

## Evidence

- Start runs with external memory [16]
- Pre-contract leaf gains its link at start [17]
- Damaged document repaired additively by its next start [18]
- Leaf with no master document refused with remedy, nothing written [19]
- Master-first planning leaves stay unstamped until start [20]
