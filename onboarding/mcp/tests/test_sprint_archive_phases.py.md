# mcp/tests/test_sprint_archive_phases.py

## Governing Overview

[mcp/tests/overview.md](overview.md)

## Purpose

Sprint archive phases: first-phase rollback, hook-failure retry, repeat rules.

## Code Commentary

MIK-R82 rule 1: a failure before the moves end restores every folder and removes the record; a hook failure after the moves keeps the archive with per-folder deleted and failed lists; repeating the same request retries only the remaining cleanup, and a changed request is refused.

## Evidence


- Phase rollback, hook-failure retention with retry, and repeat comparison are pinned. [1]
