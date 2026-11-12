# mcp/src/agents_remember/application/task_docs/task_doc_content_edits.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Apply scalar and prose edits to an already prepared task-document dictionary; the dispatcher retains validation and publication ownership.

## Code Commentary

The candidate guard rejects erasure, non-Architect hosted changes and open stage transitions. Raw set_status/set_field checks the review before writing; setting an existing review to null explicitly refuses intent-review-erasure-refused.

Status edits require a non-null status; field edits intersect the shared mutable-field allowlist and refuse when no recognized key remains. Decision appends require a nonempty object. These helpers mutate prepared content, not durable task truth.

Subtask upserts select the first exact number, preserve omitted name/file/status/scope values on an existing row, and default a new row name from its number. Section upserts similarly select the first exact heading and preserve omitted kind/body cells. Neither helper proves schema validity, route-review permission or retirement authority.

## Evidence

- Prepared mutation helpers preserve omitted upsert cells and delegate semantic validation and publication to callers. [1]

- The candidate guard rejects erasure, non-Architect hosted changes and open stage transitions. Raw set_status/set_field checks the review before writing; setting an existing review to null explicitly refuses intent-review-erasure-refused. [2]
