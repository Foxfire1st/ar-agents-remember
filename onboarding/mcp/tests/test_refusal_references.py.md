# mcp/tests/test_refusal_references.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Unit and CI proof suite for Poka-Yoke MCP refusal guidance pointers across all six emitter families, URI/anchor resolution, and AST emitter-key exhaustiveness.

## Code Commentary

Verifies fail-safe and idempotent lookup (`test_production_lookup_is_fail_safe_and_idempotent`), checks that every `REFUSAL_REFERENCES` URI resolves to an existing file under `skills/l-01-agent-lifecycles/` with a valid GFM heading anchor (`_markdown_anchors`, `test_every_registered_refusal_pointer_resolves_to_file_and_anchor`), and AST-scans all production modules under `mcp/src/agents_remember/` to ensure every `with_refusal_reference` and `refusal_reference` call passes a registered string literal and no registered key is unused (`test_every_production_refusal_emitter_key_is_registered`). Behavioral tests prove runtime pointer emission—and non-emission on ordinary holds and planned writes—across all six families.

## Relationships

Tests `models/role_capsules/refusal_references.py`, `application/role_capsules/refusal_references.py`, the refusal-emitting production modules across all six families, and the target anchors in `skills/l-01-agent-lifecycles/reference/`. Reuses `RoleToolsTestCase`/`binding` from `test_paseo_role_tools.py`, `retire` from `test_native_retire.py`, and GFM/fence helpers from `agents_remember_test_support`.

## Evidence

- Fail-safe lookup, punctuation normalization, empty-text formatting, and idempotency are asserted directly on the helpers. [1]
- Every registered `REFUSAL_REFERENCES` URI is verified against `skills/l-01-agent-lifecycles/` file containment and GFM heading anchors. [2]
- AST scanning enforces literal-string keys and bidirectional parity between production emitters and `REFUSAL_REFERENCES`. [3]
- Behavioral tests cover Families 1–6 refusal emission while keeping ordinary holds, planned writes, and non-archived retirement refusals clean. [4]
