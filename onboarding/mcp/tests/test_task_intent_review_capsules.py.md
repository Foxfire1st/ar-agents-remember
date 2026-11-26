# mcp/tests/test_task_intent_review_capsules.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Test suite covering intent-review capsule wording and packaging parity, found-enclosure move and reference-folder custody, canonical `resolve_agreed_revision` resolution, and pending-intent master-order rendering.

## Code Commentary

`RoleCapsuleSyncTests` checks intent-review sentences (`go, or review first?`, `From explainer ·`, `SHA-256`, `explainer_control`, `intent-review-open`) across `operations/planning.md`, `roles/architect.md`, and `operations/coordination.md` and proves byte equality between `skills/` and `package_data/runtime/skills/`. `FoundEnclosureMoveTests` verifies `_resolve_workspace` advances a found live enclosure's leaf and master row to `inProgress`, moves nothing on refused `intent-review-open` or created/already-started leaves, surfaces `TaskLeafBindingError` as `RolePreparationError`, and seals `notes/reference/<leaf>` plus agreed explainer revision assets (excluding `binding.json`) while emitting `referenceWarning` when unsealed and missing. `AgreedRevisionResolverTests` verifies `resolve_agreed_revision` pins exact retained revision bytes and digest, marks tampered manifests unverified, rejects loose dicts or bad digests, and refuses symlinks (`agreed-revision-symlink-refused`). `MasterOrderStateTests` confirms `derive_master_order` excludes pending-intent leaves from `ready_ids` and renders `planning · intent review open`.

## Relationships

Complements `mcp/tests/test_task_intent_review.py` (imports shared constants and fixtures). Tests `cli/role_launch_workspace._resolve_workspace`, `tasks/document.resolve_agreed_revision`, `tasks/master_order.derive_master_order`, `tasks/render.render_markdown`, and `application/task_docs/task_doc_tools.task_doc_tool`.

## Evidence

- `RoleCapsuleSyncTests` verifies intent-review clauses and byte parity between canonical `skills/` and packaged runtime copies. [1]
- `FoundEnclosureMoveTests` proves `_resolve_workspace` stage moves, refusal safety, sealed reference/revision custody excluding `binding.json`, and `referenceWarning` fallback. [2]
- `AgreedRevisionResolverTests` and `MasterOrderStateTests` verify exact retained-revision digest/symlink guards and pending-intent exclusion from `ready_ids`. [3]
