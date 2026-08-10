# mcp/src/agents_remember/serving/sprint_role_binding.py

| Field                  | Value                                                                  |
| ---------------------- | ---------------------------------------------------------------------- |
| repository             | agents-remember                                                        |
| path                   | `mcp/src/agents_remember/serving/sprint_role_binding.py`               |
| doc_type               | `file-level-onboarding`                                                |
| lastUpdated            | 2026-08-10T04:39+02:00                                                 |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded`                             |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview      | `overview.md`                                                          |

## Governing Overview

[serving overview](overview.md)

## Purpose

This module is the single policy home for immutable repository+sprint provenance on named
orchestration command seats. It prevents architect, orchestrator, and manager sessions from being
created or moved as workspace-global identities while preserving migration support for a legacy
top-level architect's first qualified attachment.

## Code Commentary

### Logic

`sprint_binding_from_leaf` parses only canonical `repo/sprint/leaf` keys. Spawn resolution combines
the declared leaf/replacement binding with a proven direct parent's stored binding, refuses missing
or conflicting evidence, and permits a parentless named seat only for an architect with declared
scope. Attachment resolution makes the pair write-once: an existing pair must match, while only a
legacy parentless architect may acquire its first binding. Reopen resolution validates paired
supplied fields, declared leaf scope, and existing catalog provenance before the shared opener can
perform any host side effect.

### Conventions

The policy returns a `(binding, refusal)` pair. Refusals are the stable
`sprint-binding-required` and `sprint-binding-conflict` values; callers project them unchanged.
`NAMED_SPRINT_ROLES` is a finite identity-policy set and must not be reused as notifier subordinate
membership, which is structural and open to future role names.

### Invariants And Boundaries

- The stored repository+sprint pair is immutable after first successful binding.
- A descendant named command seat inherits only from its exact recorded spawner.
- Partial supplied scope and cross-sprint disagreement fail before terminal creation or mutation.
- This module decides binding only; terminal creation, catalog persistence, routing, and rendering
  remain with their owning modules.

### Todos

No known follow-up is required.

## Docs References

No external domain documentation is needed; this is a repository-owned identity policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking the configured source registry, which contains no Domain Documentation entries. | n/a | n/a |

## Repo-Internal References

The source itself defines the complete binding policy and its stable refusal vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Named roles, binding/refusal models, and canonical leaf parsing define the policy vocabulary. | `NAMED_SPRINT_ROLES`; `SprintRoleBinding`; `sprint_binding_from_leaf` | mcp/src/agents_remember/serving/sprint_role_binding.py:12-45 |
| Spawn binding requires declared or inherited matching scope and refuses missing/conflicting evidence. | `sprint_binding_for_spawn` | mcp/src/agents_remember/serving/sprint_role_binding.py:48-71 |
| Attachment preserves an existing pair and permits first binding only for a legacy parentless architect. | `sprint_binding_for_attachment` | mcp/src/agents_remember/serving/sprint_role_binding.py:74-94 |
| Reopen validates supplied, declared, existing, and parent-derived scope before returning a binding. | `sprint_binding_for_reopen`; `_validate_supplied_binding`; `_reopen_inherited_binding`; `_parent_binding` | mcp/src/agents_remember/serving/sprint_role_binding.py:97-153 |

## Cross-Repo References

No cross-repository boundary is owned by this module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-10T04:39+02:00 — 260713-TES-L6: created the one-to-one onboarding card for immutable
  sprint provenance on named command seats. Verification metadata will be stamped by closeout after
  the source commit exists.
