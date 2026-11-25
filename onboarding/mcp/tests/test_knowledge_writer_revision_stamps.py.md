# mcp/tests/test_knowledge_writer_revision_stamps.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

The leaf writer preview leaves the ignore bytes and Git status unchanged and creates no brief. The applied record write adds the tracked ignore rule and writes the derived brief with the current memory tree header.


Checks provenance and revision behavior of the shared writer using bound fixture callers.

The crossing stamp case writes the prepared open sync from `build_crossing_world` and calls `crossing_write_report` with no patched worktree locations. A typed `writer` field is refused, and the resolved invariant and its crossing history row in the sync's memory worktree carry the caller's stamp.

## Evidence

- The stored stamp uses the bound caller and its receipt. [1]
- A repeated write of one owned revision renews its attribution. [2]
- A reopened attempt leaves the earlier attempt's stamp intact. [3]
