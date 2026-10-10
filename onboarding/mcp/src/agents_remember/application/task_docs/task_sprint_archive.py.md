# mcp/src/agents_remember/application/task_docs/task_sprint_archive.py

## Governing Overview

[mcp/src/agents_remember/application/task_docs/overview.md](overview.md)

## Purpose

Archiving a sprint: one operation, one record, two phases.

## Code Commentary

MIK-R82 rule 1: `archive_sprint` is called on the sprint document with a reason; a dry run reports exactly what would change. Preconditions run before anything changes, in a dry run as in a real one, and each refusal names the row or file and the clearing action: the sprint is `Completed`, every commanding row is terminal (including legacy seat-document rows), and every commanded master passes the retire readiness check. The record binds reason and selection; a same-request retry is compared against it, and a resumed move failure restores before reporting. Masters another live sprint also commands stay, named with the keeping sprint.

## Evidence

- One explicit operation archives a completed sprint with its commanded masters, guarded by terminal-row and readiness preconditions. [1]
