# mcp/src/agents_remember/application/task_docs/task_sprint_archive_records.py

## Governing Overview

[mcp/src/agents_remember/application/task_docs/overview.md](overview.md)

## Purpose

Sprint-archive record I/O and slot reconstruction.

## Code Commentary

MIK-R82 rule 1: the record `notes/reports/sprint-archive.json` is written into the sprint folder before the first folder moves, moves with the sprint folder under `0_archive/`, and protects the archive the way a retirement record protects a retirement. A repeated request is compared with it by reason and selection; a request that differs is refused. Slot reconstruction rebuilds the commanded-master slots from the record so the retry and recovery paths read the same selection the first attempt wrote.

## Evidence

- The archive record protects reason and selection across retries; slots reconstruct from the record. [1]
