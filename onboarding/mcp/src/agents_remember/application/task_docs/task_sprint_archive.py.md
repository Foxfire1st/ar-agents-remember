# mcp/src/agents_remember/application/task_docs/task_sprint_archive.py

## Governing Overview

[mcp/src/agents_remember/application/task_docs/overview.md](overview.md)

## Purpose

Archiving a sprint: one operation, one record, two phases.

## Code Commentary

Sprint preview names the task and the same would-retire environment line; failures retain the existing retry account.

MIK-R82 rule 1: `archive_sprint` is called on the sprint document with a reason; a dry run reports exactly what would change. Preconditions run before anything changes, in a dry run as in a real one, and each refusal names the row or file and the clearing action: the sprint is `Completed`, every commanding row is terminal (including legacy seat-document rows), and every commanded master passes the retire readiness check. The record binds reason and selection; a same-request retry is compared against it, and a resumed move failure attempts restoration of the whole recorded prefix. Complete restoration removes the record; incomplete restoration retains it and names the unresolved folders. Masters another live sprint also commands stay, named with the keeping sprint.

Readiness surveys every still-live commanded master before returning one refusal naming each blocked master and its clearing action. A pending preview reports commanded masters without rows and nonempty row statuses that differ from the master document under `rowSurvey`; it repairs no row.

Enclosure retirement reads each moving master's contracts from its current live or archived folder, calls the existing abandon directory routine with `force=False`, and returns per-master directory results. Staying masters are skipped. Missing contracts are named as `no-enclosure`; unreadable contracts and refused removal are reported rather than inferred as successful retirement.

A resumed preview uses that same retirement routine in dry-run mode. Pending enclosure paths appear in `taskArchive.enclosures` and in `wouldChange`; the top-level state stays `would-clean-up` while those removals remain. Only a preview with no pending cleanup reports `archived` and an empty change list.

## Evidence



- One explicit operation archives a completed sprint with its commanded masters, guarded by terminal-row and readiness preconditions. [1]





- Sprint preview names the task and the same would-retire environment line; failures retain the existing retry account. Anchor: `_preview_cleanup_changes` [2]



- Readiness surveys all still-live commanded masters before one aggregate refusal. \[3] [3]
- A pending preview reports missing rows and differing nonempty statuses without repair. \[4] [4]
- Moving masters' current-folder contracts feed safe directory retirement, with per-master outcomes. \[5] [5]
- A resumed preview includes pending enclosure removal before choosing completed state. \[6] [6]
