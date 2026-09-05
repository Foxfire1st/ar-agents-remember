# mcp/tests/test_conversation_model_architecture.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_conversation_model_architecture.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-05T06:47:44+00:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | 2026-08-25T08:12:56+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Keeps three architecture contracts after the conversation model split: removed module paths stay absent, wire types are imported from their owner, and model forward references resolve.

## Code Commentary

### Logic

The first test probes six retired module names and rejects surviving compatibility shims. The second parses Python files under mcp/src and mcp/tests, reporting shared conversation names imported from the harness control facade. The third imports each conversation model module, rebuilds its locally owned Pydantic model classes and checks that they are complete.

### Conventions

The forbidden wire-name set comes from conversations.__all__. Import violations include repository-relative path, line and symbol for diagnosis.

### Invariants And Boundaries

The import rule examines ImportFrom nodes naming the exact control facade within the two declared roots. The forward-reference check skips imported classes owned outside the conversation package.

### Todos

None recorded.

## Docs References

No domain documentation is configured. This card describes repository source only.

## Repo-Internal References

These constructs establish the behavior described above.

| Finding | Anchor | Source |
| --- | --- | --- |
| Retired paths must have no surviving compatibility modules | `REMOVED_MODEL_MODULES`; `test_removed_conversation_model_modules_have_no_compatibility_shims` | mcp/tests/test_conversation_model_architecture.py:15-28 |
| Source and test imports must use the conversation wire owner | `CONTROL_FACADE`; `test_conversation_wire_types_are_not_imported_through_the_control_facade` | mcp/tests/test_conversation_model_architecture.py:23-44 |
| Locally owned model classes must finish rebuilding forward references | `test_conversation_models_have_resolved_forward_references`; `model_rebuild` | mcp/tests/test_conversation_model_architecture.py:47-56 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

## Update History

- 2026-09-05T06:47:44+00:00 — Created during L31 full-population memory recovery from frozen ea359649; verification records the actual source-touching commit. Documentation evidence only.
