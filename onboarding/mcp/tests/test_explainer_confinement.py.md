# mcp/tests/test_explainer_confinement.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Every writer of the environment's durable facts checks the physical confinement of its target before writing, so a planted link is held and nothing behind it sees a byte.

## Code Commentary

- A symlinked task folder refuses every writer at once — binding, counter, marker, ledger and lock — with zero outside effects.
- A symlinked workspace, counter, ledger or lock is held by its own writers before the file is opened.
- Removing a workspace holds a nested link instead of letting the recursive delete follow it.
- An Update faulted in a pre-bind write leaves the old generation coherent and takes the partial next snapshot with it.

## Evidence

- The case `test_every_metadata_writer_refuses_a_planted_task_folder_ancestor_link` protects a symlinked task folder refusing every writer with no outside effect. [1]
- The case `test_the_generation_writers_refuse_a_planted_counter_link` protects a symlinked counter being refused while the outside file keeps its bytes. [2]
- The case `test_the_seat_lock_refuses_a_planted_lock_link_before_locking` protects a symlinked lock file being admitted physically before the kernel opens it. [3]
- The case `test_workspace_removal_holds_a_nested_link_instead_of_rmtree_following_it` protects a nested link holding a workspace removal. [4]
- The case `test_an_update_faulted_in_a_pre_bind_write_leaves_the_old_generation_coherent` protects the old generation staying coherent when an Update faults before the bind. 

- Retired at the fifth freeze d59c3493: mcp/tests/test_explainer_confinement.py::test_an_update_faulted_in_a_pre_bind_write_leaves_the_old_generation_coherent - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 5f8398b32760677c370e3145add73cfa8388357b. Retired means the anchor no longer stands, not that the cited subject was deleted.
