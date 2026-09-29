# mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T17:20:02+02:00 |
| lastVerifiedCommitHash |  `e40c314ca55305f7e4334b4e8e16a10297f6f175`|
| lastVerifiedCommitDate |  2026-09-29T18:13:06+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation sources are configured for this repository-internal input boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation was available after checking the configured source registry. | n/a | n/a |

## Repo-Internal References

The source and focused application tests prove the raw-shape and no-write boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The helper validates the entire raw list before copying and scaffolding only missing registers. | `scaffold_register_sections`; `_validated_section_list`; `_requires_register_scaffolding` | mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:17-37; mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:40-51; mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:54-55 |
| `_build_doc` routes create and replace candidates through this helper (after the `kind` default) and only then through `_validate`, the canonical model validation. | `_build_doc`; "scaffold_register_sections(data)" | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:585-618 |
| Register section scaffolding has one production entry point and validates the supplied section collection. | `scaffold_register_sections` | mcp/src/agents_remember/application/task_docs/task_doc_section_scaffolding.py:17-37 |

## Cross-Repo References

No cross-repository boundary is owned by this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository references were found. | n/a | n/a |

## Update History

- 2026-09-29T17:20:02+02:00 — 260928-MIK-L08 curator (uncommitted change set on `ar/260928-mik-l08`, code base `e49ba07865b3848cd36759cea6b37bba7d0d51c3` plus the working-tree delta and untracked files): **reopened `_build_doc` claim re-read against the current construct and re-measured.** `_build_doc` still defaults `kind`, calls `scaffold_register_sections(data)` and returns `_validate(data)`, so the claim holds; the row now names the call order and `_validate`, is anchored on the call as well, and cites the function's current extent `585-618` (the committed `554-584` had fallen behind `task_doc_tools.py`'s growth; MIK-R08 added one more line to `_MUTABLE_FIELDS`). This file's own source is unchanged, and so is this card's account of it.
- 2026-08-24T13:43+02:00 — Created for DAGQC L1: raw section list/member validation now
  precedes register scaffolding without duplicating the canonical section schema. Verification
  remains closeout-owned because the source is uncommitted.
