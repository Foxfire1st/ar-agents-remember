# mcp/src/agents_remember/tasks/consolidation_task.py

## Governing Overview

[overview](overview.md)

## Purpose

Determines from a task document or task-document file whether a leaf is a consolidation task and returns its ordered seat roles (`("consolidator", "reviewer")` vs `("worker", "reviewer", "curator")`).

## Code Commentary

Declares `CONSOLIDATION_LIST_KEY = "consolidationList"`, `ORDINARY_LEAF_SEATS = ("worker", "reviewer", "curator")`, and `CONSOLIDATION_LEAF_SEATS = ("consolidator", "reviewer")`. `names_consolidation_list(document)` accepts either a parsed `TaskDocument` or a raw JSON mapping and returns `True` iff `consolidationList` holds at least one non-empty ID list. `is_consolidation_task(path)` reads and parses the JSON file directly without resolving the full task hierarchy; any `OSError`, `UnicodeDecodeError`, or `json.JSONDecodeError` returns `False` so the caller's normal document resolution refuses the file with its own diagnostic. `leaf_seat_roles(document)` and `leaf_seat_roles_of(coordination_root, ref)` select `CONSOLIDATION_LEAF_SEATS` or `ORDINARY_LEAF_SEATS`; `leaf_seat_roles_of` resolves `ref` via `TaskDocumentTopology.path_for_ref` and falls back to `ORDINARY_LEAF_SEATS` on `TaskDocumentRefError` (leaving ref refusal to selection resolution).

## Relationships

Imported by `cli/leaf_set_seats.py` (`CONSOLIDATION_LEAF_SEATS`, `ORDINARY_LEAF_SEATS`, `leaf_seat_roles_of`), `cli/leaf_seat_handover.py` (`leaf_seat_roles`), and `cli/seat_variant_rows.py` (`names_consolidation_list`). Depends on `models.task_document_ref.TaskDocumentRef`, `tasks.document.TaskDocument`, and `tasks.document_refs` (`TaskDocumentTopology`, `TaskDocumentRefError`).

## Evidence

- `CONSOLIDATION_LEAF_SEATS` defines `("consolidator", "reviewer")` beside `ORDINARY_LEAF_SEATS` (`("worker", "reviewer", "curator")`) and `CONSOLIDATION_LIST_KEY`. [1]
- `names_consolidation_list` inspects either a `TaskDocument` or a raw JSON mapping for a non-empty `consolidationList`. [2]
- `is_consolidation_task` reads the document file directly and returns `False` on `OSError`, UTF-8, or JSON parse errors rather than masking downstream resolution errors. [3]
- `leaf_seat_roles_of` resolves a `TaskDocumentRef` via `TaskDocumentTopology` and falls back to `ORDINARY_LEAF_SEATS` on `TaskDocumentRefError`. [4]
