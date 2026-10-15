# mcp/src/agents_remember/application/task_docs/task_doc_field_homes.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Keep new prose in its structured field homes and validate explicitly written dependency lists, without turning display order into start permission.

## Code Commentary

Reserved freeform headings and header labels are matched after trimming and case folding. Counters of original occurrences grandfather edits/removals of existing entries, not extra reserved duplicates. Structured sections bypass the freeform check; a sprint order-heading refusal points to execution-graph authoring rather than leaf waitsFor.

Only an explicitly supplied, nonempty waitsFor on create/replace/set_field invokes dependency checks. It must belong to a subTask, exclude self, resolve an ordinary master, and name listed non-abandoned rows. Membership and abandoned status come from the master index row; a readable child's explicit master link supplies the separate cross-master check, not status authority. A readable target explicitly bound to another master refuses; an unreadable/missing child alone is not an extra refusal. Candidate-containing cycles among loaded children refuse, while unrelated legacy cycles remain readable. Empty/null clears bypass this nonempty-field check. IDs are not normalized, and these are write-time checks, not scheduler/start guards.

## Evidence

- Original-occurrence prose grandfathering and explicit nonempty waitsFor write validation have separate predicates. [1]
