# mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py

## Governing Overview

[task-doc application overview](overview.md)

## Purpose

Establish the minimum safe raw `sections` shape before planning-register scaffolding touches task
authoring input. It keeps hostile input in the typed task-document error dialect while leaving all
section semantics with the canonical task model and register validator.

## Code Commentary

### Logic

- `scaffold_register_sections(data)` distinguishes an absent `sections` field from an explicit
  value, validates every explicit container/member before copying or appending, and scaffolds only
  orchestration masters.
- `_validated_section_list(value)` accepts a list whose every member is a mapping; all other
  containers and indexed malformed members raise `TaskDocError` before `.get` or mutation.
- `_requires_register_scaffolding(data)` is the single narrow predicate: `kind == "master"` and a
  non-empty `orchestrates` list.

### Conventions

The helper proves only the list/mapping operations it needs. It copies the list, preserves caller
members and order, and appends each missing canonical register once.

### Invariants And Boundaries

- Raw container/member validation is atomic: every member is checked before the copied list is
  installed or any scaffold is appended.
- Invalid values are refused, never coerced, wrapped, dropped, or partly authored.
- Pydantic `TaskDocument` validation and `require_register_sections_valid` remain the semantic
  authorities for section content and register table shape.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation sources are configured for this repository-internal input boundary.

No relevant external documentation was available after checking the configured source registry.

### Repo-Internal References

The source and focused application tests prove the raw-shape and no-write boundary.

- The helper validates the entire raw list before copying and scaffolding only missing registers. [1]
- `_build_doc` routes create and replace candidates through this helper (after the `kind` default) and only then through `_validate`, the canonical model validation. [2]
- Register section scaffolding has one production entry point and validates the supplied section collection. [3]

### Cross-Repo References

No cross-repository boundary is owned by this file.

No meaningful cross-repository references were found.
