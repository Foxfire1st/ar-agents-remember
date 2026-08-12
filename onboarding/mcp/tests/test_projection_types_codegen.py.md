# mcp/tests/test_projection_types_codegen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_projection_types_codegen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T00:08+02:00 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32` |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Projection schema/TypeScript generation and its fail-on-diff gate.

## Code Commentary

### Logic

Module-level surface:

- `ProjectionSchemaGenerationTests` (class, lines 44-166)
- `ProjectionSchemaDriftTests` (class, lines 169-307)

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
| Defines the class `ProjectionSchemaGenerationTests` (lines 44-166). | `ProjectionSchemaGenerationTests` | mcp/tests/test_projection_types_codegen.py:44-166 |
| Defines the class `ProjectionSchemaDriftTests` (lines 169-307). | `ProjectionSchemaDriftTests` | mcp/tests/test_projection_types_codegen.py:169-296 |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T00:08+02:00 — No content impact: schema-drift subtests report relative paths as
  serializable POSIX strings for xdist; generated-schema comparisons are unchanged. Verification
  metadata remains pinned until closeout.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
