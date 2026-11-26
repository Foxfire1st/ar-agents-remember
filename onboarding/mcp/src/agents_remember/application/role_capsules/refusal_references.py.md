# mcp/src/agents_remember/application/role_capsules/refusal_references.py

## Governing Overview

[application overview](../overview.md)

## Purpose

Pure re-export facade exposing the model-layer refusal-reference registry and helpers to `application/`, `cli/`, and `mcp/tools/` callers.

## Code Commentary

Re-exports `REFUSAL_REFERENCES`, `SKILL_URI_PREFIX`, `refusal_reference`, and `with_refusal_reference` verbatim from `agents_remember.models.role_capsules.refusal_references` with no local state or logic. Exists so higher layers import from `application.role_capsules` while canonical ownership remains in `models/` for `worktrees/`.

## Relationships

Delegates entirely to `models/role_capsules/refusal_references.py`. Imported by `application/knowledge_write_answer.py`, `application/memory_quality/answer.py`, `application/worktree_tools.py`, `cli/paseo_role_tools.py`, `cli/role_message_delivery.py`, `cli/role_retire.py`, `mcp/tools/knowledge.py`, and `mcp/tests/test_refusal_references.py`.

## Evidence

- The facade re-exports `REFUSAL_REFERENCES`, `SKILL_URI_PREFIX`, `refusal_reference`, and `with_refusal_reference` from `models.role_capsules.refusal_references` without adding logic. [1]
