# mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Enforce source-package structural limits (260731-EFA-L6 R8).

## Code Commentary

### Logic

Module-level surface:

- `DeclarationError` (class, lines 56-57) — ``layers.toml`` says something a structural cap cannot act on.
- `Offender` (class, lines 61-79) — One construct over one limit, with everything the remedy needs to find it.
- `DirectoryDeviation` (class, lines 83-112) — A directory-scoped structural departure and the leaf required to clear it.
- `StaleDeviation` (class, lines 116-123) — A deviation and each declared cap the current tree now meets.
- `python_sources` (function, lines 126-128) — Every ``.py`` file under ``root``, in a stable order.
- `package_sources` (function, lines 131-139) — ``(display path, source text)`` for every module under ``root``, read once.
- `_display` (function, lines 142-143)
- `source_span` (function, lines 146-155) — Lines the statement spans, counting its own first line.
- `function_definitions` (function, lines 158-162) — Every ``def`` and ``async def`` in the module, nested ones included.
- `measure_functions` (function, lines 165-177) — Every function in ``source``, measured. Callers filter; this reports all of them.
- `long_functions` (function, lines 180-191) — Functions under ``root`` longer than ``limit`` lines, longest first.
- `_nested_statements` (function, lines 194-202) — Statements one level inside ``statement``, exception handlers included.
- `_class_body` (function, lines 205-218) — Every statement the class declares, including ones behind a class-body ``if``.
- `method_definitions` (function, lines 221-225) — Every method the class declares, nested classes and closures excluded.
- `_is_overload` (function, lines 228-230) — Whether the def is a ``typing.overload`` stub rather than a distinct method.
- `_decorator_name` (function, lines 233-238)
- `_name_of` (function, lines 241-246)
- `is_protocol` (function, lines 249-251) — Whether the class declares a structural TYPE rather than an implementation.
- `_is_stub` (function, lines 254-270) — Whether the def has no body: only ``...``, optionally under a docstring.
- `declares_field` (function, lines 273-298) — Whether the member declares a read-only FIELD rather than an operation.
- `public_method_names` (function, lines 301-315) — The class's public surface: distinct non-underscore method names, overloads folded.
- `_first_parameter` (function, lines 318-320)
- `_attributes_on` (function, lines 323-335) — Attributes touched on the name ``subject``, and the subset assigned to.
- `declared_attribute_names` (function, lines 338-355) — Everything the class declares a member of itself: fields, methods, ``self.x`` stores.
- `BoundFunction` (class, lines 359-370) — A public module-level function that assigns to its first parameter's attributes.
- `_annotation_name` (function, lines 373-381) — The bare class name an annotation refers to, or ``""`` if it is not a plain name.
- `bound_functions` (function, lines 384-402) — The module's top-level functions that mutate whatever is passed as their first argument.
- `_classes_bound_by` (function, lines 405-410)
- `relocated_surface` (function, lines 413-435) — Module-level functions charged to the class they are a method of, by ``(path, name)``.
- `measure_classes` (function, lines 438-463) — Every class in ``source``, measured by public surface.
- `_all_wide_classes` (function, lines 466-477) — Every class over ``limit``, before any deviation is applied.
- `wide_classes` (function, lines 480-492) — Classes over ``limit`` that no declared deviation covers, widest first.
- `module_counts` (function, lines 495-505) — Modules directly in each directory under ``root``, keyed by posix relative path.
- `crowded_directories` (function, lines 508-522) — Directories over ``limit`` modules that no declared deviation covers, worst first.
- `stale_deviations` (function, lines 525-555) — Declared deviations, and the caps they no longer depart from.
- `_worst_first` (function, lines 558-559)
- `read_directory_deviations` (function, lines 562-601) — Directory deviations declared in ``layers.toml``'s ``[sequencing.*]`` tables.
- `_deviation_from` (function, lines 604-623)
- `_limits_from` (function, lines 626-646) — The caps one deviation departs from: a non-empty list drawn from a closed vocabulary.
- `render_offenders` (function, lines 649-660) — Render the complete offender list plus the required remediation (R15).

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `DeclarationError` (lines 56-57) — ``layers.toml`` says something a structural cap cannot act on.. | `DeclarationError` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:56-57 |
| Defines the class `Offender` (lines 61-79) — One construct over one limit, with everything the remedy needs to find it.. | `Offender` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:60-79 |
| Defines the class `DirectoryDeviation` (lines 83-112) — A directory-scoped structural departure and the leaf required to clear it.. | `DirectoryDeviation` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:82-112 |
| Defines the class `StaleDeviation` (lines 116-123) — A deviation and each declared cap the current tree now meets.. | `StaleDeviation` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:115-123 |
| Defines the function `python_sources` (lines 126-128) — Every ``.py`` file under ``root``, in a stable order.. | `python_sources` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:126-128 |
| Defines the function `package_sources` (lines 131-139) — ``(display path, source text)`` for every module under ``root``, read once.. | `package_sources` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:131-139 |
| Defines the function `_display` (lines 142-143). | `_display` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:142-143 |
| Defines the function `source_span` (lines 146-155) — Lines the statement spans, counting its own first line.. | `source_span` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:146-155 |
| Defines the function `function_definitions` (lines 158-162) — Every ``def`` and ``async def`` in the module, nested ones included.. | `function_definitions` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:158-162 |
| Defines the function `measure_functions` (lines 165-177) — Every function in ``source``, measured. Callers filter; this reports all of them.. | `measure_functions` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:165-177 |
| Defines the function `long_functions` (lines 180-191) — Functions under ``root`` longer than ``limit`` lines, longest first.. | `long_functions` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:180-191 |
| Defines the function `_nested_statements` (lines 194-202) — Statements one level inside ``statement``, exception handlers included.. | `_nested_statements` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:194-202 |
| Defines the function `_class_body` (lines 205-218) — Every statement the class declares, including ones behind a class-body ``if``.. | `_class_body` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:205-218 |
| Defines the function `method_definitions` (lines 221-225) — Every method the class declares, nested classes and closures excluded.. | `method_definitions` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:221-225 |
| Defines the function `_is_overload` (lines 228-230) — Whether the def is a ``typing.overload`` stub rather than a distinct method.. | `_is_overload` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:228-230 |
| Defines the function `_decorator_name` (lines 233-238). | `_decorator_name` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:233-238 |
| Defines the function `_name_of` (lines 241-246). | `_name_of` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:241-246 |
| Defines the function `is_protocol` (lines 249-251) — Whether the class declares a structural TYPE rather than an implementation.. | `is_protocol` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:249-251 |
| Defines the function `_is_stub` (lines 254-270) — Whether the def has no body: only ``...``, optionally under a docstring.. | `_is_stub` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:254-270 |
| Defines the function `declares_field` (lines 273-298) — Whether the member declares a read-only FIELD rather than an operation.. | `declares_field` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:273-298 |
| Defines the function `public_method_names` (lines 301-315) — The class's public surface: distinct non-underscore method names, overloads folded.. | `public_method_names` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:301-315 |
| Defines the function `_first_parameter` (lines 318-320). | `_first_parameter` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:318-320 |
| Defines the function `_attributes_on` (lines 323-335) — Attributes touched on the name ``subject``, and the subset assigned to.. | `_attributes_on` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:323-335 |
| Defines the function `declared_attribute_names` (lines 338-355) — Everything the class declares a member of itself: fields, methods, ``self.x`` stores.. | `declared_attribute_names` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:338-355 |
| Defines the class `BoundFunction` (lines 359-370) — A public module-level function that assigns to its first parameter's attributes.. | `BoundFunction` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:358-370 |
| Defines the function `_annotation_name` (lines 373-381) — The bare class name an annotation refers to, or ``""`` if it is not a plain name.. | `_annotation_name` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:373-381 |
| Defines the function `bound_functions` (lines 384-402) — The module's top-level functions that mutate whatever is passed as their first argument.. | `bound_functions` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:384-402 |
| Defines the function `_classes_bound_by` (lines 405-410). | `_classes_bound_by` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:405-410 |
| Defines the function `relocated_surface` (lines 413-435) — Module-level functions charged to the class they are a method of, by ``(path, name)``.. | `relocated_surface` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:413-435 |
| Defines the function `measure_classes` (lines 438-463) — Every class in ``source``, measured by public surface.. | `measure_classes` | mcp/test_support/agents_remember_test_support/code_quality/structural_limits.py:438-463 |

## Update History

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
