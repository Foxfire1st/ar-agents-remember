# mcp/tests/test_leaf_doc_master_link_binding.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proof that a leaf authored before its series contract exists gets its master link bound at start, over a real coordination root, code repository and Git-backed memory repository.

## Code Commentary

Each case builds one scratch coordination root, one code repository and one external memory repository, authors both documents through the real `task_doc` plane, and drives the real public start. `_start_leaf` runs `worktree_start` with `memory_mode="external"`, so the binding proof exercises the only supported topology. The retained binding cases assert: the pre-contract leaf gets its series-contract path, enclosure ref and lifecycle stamp at start; an already-damaged document is repaired additively; a leaf explicitly supplied with `master=None` is refused with `Sub-task publication requires a master.` and leaves both task-directory JSON/Markdown populations and master/leaf paths absent; and master-first planning stays usable with leaves unstamped until start.

Start publishes `inProgress` on the leaf and exact parent row without marking the first step done. Restart after abandonment restores that stage and worktree. Duplicate parent rows refuse abandon before terminal archive or worktree deletion. An injected master write failure rolls back both task stages and all four captured document files, then retry succeeds.

## Evidence

- Abandoned leaf restart promotes both stages and restores the code worktree. [21]
- Invalid parent refuses preview and apply without terminal authority or deletion. [22]
- Parent write failure restores captured leaf/master files; retry promotes both stages. [23]


- Start runs with external memory [16]

- Pre-contract leaf gains its link at start [17]

- Damaged document repaired additively by its next start [18]
- Master-first planning leaves stay unstamped until start [20]

- Explicit master=None refuses with the exact master-required message and leaves all task JSON/Markdown and master/leaf paths absent. [19]
