# mcp/src/agents_remember/application/legacy_dataset_copies.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](overview.md)

## Purpose

The plan, apply and report owner for leftover copies of the retired knowledge database. Survey, classification and owner release live beside this module in `dataset_copy_survey.py`, which imports nothing from here at runtime.

## Code Commentary

MIK-R26 rule 6 with MIK-R82 rules 2 and 3: this module owns the reviewed dry run, its digest-bound apply, and the report. A copy is any SQLite file holding the knowledge tables, identified by content rather than name; the cleanup deletes the copies in provider-runtime directories, dead worktrees, archived-task notes, and — under rule 2 — the notes of `Completed` or `abandoned` tasks, protects tracked and symbolic-link companions, and binds its apply to the reviewed dry-run digest. `run_cleanup` treats a companion the reviewed plan keeps as successful preservation rather than a failed deletion.

## Evidence

No separate reference list: the file's sidecar carries the realization entries this leaf re-anchored.
