# mcp/test_support/agents_remember_test_support/testing/memory_orphan_checkpoint.py

## Governing Overview

[overview](overview.md)

## Purpose

The module drives the crash checkpoint of one parked-candidate sync regression in `mcp/tests/test_sync_parked_candidate.py`: a native sync is stopped just before it publishes its operation journal, killed, and rerun, and no parked memory file may be lost.

## Code Commentary

The fixture memory worktree holds 500 expected files. A forked child installs an audit hook and runs the sync; at the `os.rename` onto the journal path it records a checkpoint, asserts the pending record is in phase `running-code` with a `parked memory WIP` stash equal to `refs/stash`, a clean status and no published journal, and stops itself. The parent verifies the checkpoint, kills the child's process group, requires no journal, and reruns sync. The rerun must keep the same memory stash in its journal and end `synced` with every file restored and an empty stash list, or `memory-resolution-required` with the stash retained and every expected blob in its untracked-files tree. Evidence JSON files are kept in a temporary directory whose path is printed.

## Evidence

- The child stops at the journal publish after asserting the parked memory stash and unpublished journal. [1]
- The parent waits for the stop, kills the child, requires no journal and reruns recovery. [2]
- Recovery ends synced with all files restored or resolution-required with all files retained in the stash. [3]
