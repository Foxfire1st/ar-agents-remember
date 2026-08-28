# mcp/tests/test_projection_types_codegen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_projection_types_codegen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
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

## 260821-DAGQC Runtime Refinement Coverage

The focused generator suite now proves both sides of the refinement boundary. A supported `pattern`
and a nested `items.minLength` survive as deterministic TypeScript `JSON Schema refinements`
documentation beside the affected properties. An unknown `format` keyword still raises
`ProjectionTypeGenerationError` with the exact `GateNode.state` path, preservation remediation,
and the explicit no-silent-drop contract.

The existing schema identity, deterministic/idempotent generation, required-field parity, literal
rendering, drift detection, provenance guard, and mirror guard remain unchanged. This test module is
the focused proof for the generator contract; it does not make TypeScript comments a runtime
validator.

## PDLS Wave 005 Current Delta

The script execution environment must resolve both `mcp/src` product code and
`mcp/test_support` verification tooling. The focused pyright assertion prevents either package
root from disappearing while projection generation remains owned by the verification package.

## Update History

- 2026-08-28T06:40+02:00 — Moved the generator import to
  `agents_remember_test_support` and required both source roots in the scripts pyright environment.
- 2026-08-24T15:04+02:00 — Added focused supported-refinement preservation and unknown-keyword
  fail-closed coverage. Verification metadata remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T00:08+02:00 — No content impact: schema-drift subtests report relative paths as
  serializable POSIX strings for xdist; generated-schema comparisons are unchanged. Verification
  metadata remains pinned until closeout.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
