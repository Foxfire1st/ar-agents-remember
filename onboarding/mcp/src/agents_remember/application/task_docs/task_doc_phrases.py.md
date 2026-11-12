# mcp/src/agents_remember/application/task_docs/task_doc_phrases.py

## Governing Overview

[Task-document application overview](overview.md)

## Purpose

Own the compact changed-unit/value phrase for a successful task-document write. This presentation module shares its mutable-field allowlist with the write owner; it neither writes a document nor determines whether a write is authorized.

## Code Commentary

intentReview is an admitted mutable native field, so set_field records the developer answer instead of silently ignoring it.

`_updated_phrase` dispatches by operation to a phrase builder, with an operation-applied fallback for an unlisted operation. New values are rendered whole when short and clipped after 120 characters otherwise. That phrase is a compact account, not a replacement for the full persisted document or its diff.

Step updates describe only `_STEP_UPDATE_KEYS`; parent and id address the step and are not claimed as changes. Field phrases select only `_MUTABLE_FIELDS`, omitting ignored keys. Creation/replacement identify the slug, status comes from the supplied fields, and review/retirement/archive/linkage phrases use their operation's result. These distinct sources must stay aligned with the applier rather than using a generic input dump.

The shared allowlist now includes `nonGoals`, `acceptance`, and `waitsFor`. `_phrase_set_field` still claims only allowlisted keys; dependency validation and write authorization do not live in this presentation owner.

## Evidence

- A displayed new value has a fixed character clipping rule, independent of the delivered token guard. [1]
- Step phrases separate addressing keys from allowed changes. [2]

- Field phrases omit keys outside the shared allowlist, now also containing `nonGoals`, `acceptance`, and `waitsFor`; this is a presentation filter, not dependency admission. [3]


- Operation-specific phrase builders have one dispatch owner and an explicit fallback. [4]

- intentReview is an admitted mutable native field, so set_field records the developer answer instead of silently ignoring it. [5]
