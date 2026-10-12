# mcp/tests/test_enclosure_without_remains.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

An enclosure with nothing left ends without adoption.

## Code Commentary

MIK-R82 rule 5: a leaf with no locator whose worktree folder and work branches do not exist finishes through abandon or cleanup with nothing to archive and nothing to delete. The real run persists its reason in the contract; the external memory branch stays outside the exception.

The populated-series-log regression calls `_abandon_directories` directly: it snapshots the group's byte tree, verifies dry-run leaves it unchanged, then verifies apply removes `logs/`. Both responses contain exactly `reports` and `lifecycle`. This is helper-level preview/removal evidence, not a public terminal-admission or real-host execution witness.

## Evidence

- No-remains abandon and cleanup with persisted reason are pinned. [1]
