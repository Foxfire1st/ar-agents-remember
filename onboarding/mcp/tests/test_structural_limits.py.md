# mcp/tests/test_structural_limits.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_structural_limits.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Tests for the function, class-surface, and directory structural caps.

## Code Commentary

### Logic

Module-level surface:

- `declared_deviations` (function, lines 66-67)
- `deviation` (function, lines 70-79) — A complete deviation for a fixture package, so no test builds a half-formed one.
- `write_package` (function, lines 82-91) — A throwaway package shaped like this one, from ``{relative path: source}``.
- `function_of_length` (function, lines 94-97) — A function whose measured length is exactly ``body_lines`` + 1.
- `class_with_public_methods` (function, lines 100-104)
- `relocated_parser` (function, lines 107-130) — A state machine and a sibling module of free functions that drive its cursor.
- `FunctionLengthTests` (class, lines 133-148) — No function in the package may exceed the measured cap.
- `ClassSurfaceTests` (class, lines 151-179) — A class's public surface is its declared, non-underscore method names.
- `RelocationTests` (class, lines 182-276) — Moving a method to the next file does not remove it from the class's surface.
- `DirectorySizeTests` (class, lines 279-294) — A directory holds a bounded number of modules, or the contract says why not.
- `DeclaredDeviationTests` (class, lines 297-351) — Keep the sequencing register bounded, owned, scoped, and non-stale.
- `DeviationDeclarationTests` (class, lines 354-491) — A deviation with no owner cannot be honoured -- that is what an allowlist is.
- `KnownGoodConstructTests` (class, lines 494-877) — Constructs this repository contains that the checks must never flag.
- `ProbeTests` (class, lines 880-1024) — Each check, shown rejecting a deliberate violation (R16).

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
| Defines the function `declared_deviations` (lines 66-67). | `declared_deviations` | mcp/tests/test_structural_limits.py:66-67 |
| Defines the function `deviation` (lines 70-79) — A complete deviation for a fixture package, so no test builds a half-formed one.. | `deviation` | mcp/tests/test_structural_limits.py:70-79 |
| Defines the function `write_package` (lines 82-91) — A throwaway package shaped like this one, from ``{relative path: source}``.. | `write_package` | mcp/tests/test_structural_limits.py:82-91 |
| Defines the function `function_of_length` (lines 94-97) — A function whose measured length is exactly ``body_lines`` + 1.. | `function_of_length` | mcp/tests/test_structural_limits.py:94-97 |
| Defines the function `class_with_public_methods` (lines 100-104). | `class_with_public_methods` | mcp/tests/test_structural_limits.py:100-104 |
| Defines the function `relocated_parser` (lines 107-130) — A state machine and a sibling module of free functions that drive its cursor.. | `relocated_parser` | mcp/tests/test_structural_limits.py:107-130 |
| Defines the class `FunctionLengthTests` (lines 133-148) — No function in the package may exceed the measured cap.. | `FunctionLengthTests` | mcp/tests/test_structural_limits.py:133-148 |
| Defines the class `ClassSurfaceTests` (lines 151-179) — A class's public surface is its declared, non-underscore method names.. | `ClassSurfaceTests` | mcp/tests/test_structural_limits.py:151-179 |
| Defines the class `RelocationTests` (lines 182-276) — Moving a method to the next file does not remove it from the class's surface.. | `RelocationTests` | mcp/tests/test_structural_limits.py:182-276 |
| Defines the class `DirectorySizeTests` (lines 279-294) — A directory holds a bounded number of modules, or the contract says why not.. | `DirectorySizeTests` | mcp/tests/test_structural_limits.py:279-294 |
| Defines the class `DeclaredDeviationTests` (lines 297-351) — Keep the sequencing register bounded, owned, scoped, and non-stale.. | `DeclaredDeviationTests` | mcp/tests/test_structural_limits.py:297-351 |
| Defines the class `DeviationDeclarationTests` (lines 354-491) — A deviation with no owner cannot be honoured -- that is what an allowlist is.. | `DeviationDeclarationTests` | mcp/tests/test_structural_limits.py:354-491 |
| Defines the class `KnownGoodConstructTests` (lines 494-877) — Constructs this repository contains that the checks must never flag.. | `KnownGoodConstructTests` | mcp/tests/test_structural_limits.py:494-877 |
| Defines the class `ProbeTests` (lines 880-1024) — Each check, shown rejecting a deliberate violation (R16).. | `ProbeTests` | mcp/tests/test_structural_limits.py:880-1024 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
