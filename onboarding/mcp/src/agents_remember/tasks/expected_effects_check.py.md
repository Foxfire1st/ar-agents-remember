# mcp/src/agents_remember/tasks/expected_effects_check.py

## Governing Overview

[overview](overview.md)

## Purpose

Performs the whole-document validation rules for a task document's `expectedKnowledgeEffects` list, separated from per-entry Pydantic field validation.

## Code Commentary

Defines minimal structural protocols `_Declared` (`subject`, `effect`, `requirementRef`) and `_Packet` (`stableId`, `version`) so the check has no import dependency on `tasks.document`. `check_expected_knowledge_effects(kind, effects, packets)` returns immediately when `effects is None`, and otherwise raises `ValueError` if: `kind == "master"`, `effects` is empty (`null` must be used to clear it), `packets` is non-empty and any `effect.requirementRef` is not in `{f"{p.stableId}@{p.version}"}`, or any `f"{effect.subject}#{effect.effect}"` pair appears more than once (even under different requirement refs). Performs schema-level cross-field validation only; it neither reads requirement packet contents nor verifies knowledge record existence.

## Relationships

Called by `tasks/document.py` (`TaskDocument` model validator). Standalone pure module using only standard-library `collections.Counter` and `typing.Protocol`.

## Evidence

- `_Declared` defines the structural protocol (`subject`, `effect`, `requirementRef`) expected on each declared effect item. [1]
- `_Packet` defines the structural protocol (`stableId`, `version`) used to build the set of declared requirement references. [2]
- `check_expected_knowledge_effects` refuses master documents, empty effect lists, `requirementRef` values missing from non-empty `packets`, and duplicate `<subject>#<effect>` keys. [3]
