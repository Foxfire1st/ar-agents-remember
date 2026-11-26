# mcp/src/agents_remember/models/role_capsules/refusal_references.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Canonical model-layer registry mapping 21 MCP refusal keys across six lifecycle tool families to their served Tier-2 `skill://` guidance URIs, with fail-safe lookup and idempotent text-appending helpers.

## Code Commentary

`SKILL_URI_PREFIX` pins `skill://agents-remember/skills/l-01-agent-lifecycles`. `REFUSAL_REFERENCES` is an immutable `MappingProxyType` covering six families: `role_message` (4 keys), `task_doc` review and route-review (4 keys), `worktree_sync` (3 keys), `knowledge_write` and `memory_quality_check` (3 keys), `worktree_closeout_*` and `worktree_operation_control` (4 keys), and `retire_child` (3 keys). `refusal_reference(key)` returns `None` on unknown keys. `with_refusal_reference(text, key)` appends `See <uri>.` once, normalizing trailing `.`, `!`, or `?`, returning `See <uri>.` for blank text, and returning `text` unchanged when `key` is unknown or `uri` is already present so production refusal paths never raise on lookup.

## Relationships

Lives in `models/` (lower layer rank) so `worktrees/` modules (`closeout.py`, `curator_coherence.py`, `door_evidence.py`, `review_history.py`, `route_review.py`, `sync_transaction_results.py`) can import it without upward dependencies. Re-exported by `application/role_capsules/refusal_references.py` for `application/`, `cli/`, and `mcp/tools/`. Key registration, live file/heading anchor resolution, and AST emitter exhaustiveness are verified in `mcp/tests/test_refusal_references.py`.

## Evidence

- `REFUSAL_REFERENCES` maps all 21 refusal keys across 6 tool families to `SKILL_URI_PREFIX`-rooted served `skill://` URIs in an immutable `MappingProxyType`. [1]
- `refusal_reference` fails safe by returning `None` for unregistered keys. [2]
- `with_refusal_reference` appends `See <uri>.` once with punctuation normalization and returns input unchanged when the key is unknown or the URI is already present. [3]
