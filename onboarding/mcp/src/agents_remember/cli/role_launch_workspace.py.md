# mcp/src/agents_remember/cli/role_launch_workspace.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The role start's preparation owner: it derives the folder a role class may use, creates or finds the leaf enclosure through the existing child, and translates every refusal into the owner's status, reason and next action.

## Code Commentary

`_recorded_parent` reads the master's existing series contract and passes its recorded `parent_task_name` as the materializer hint; only a master with no contract yet falls back to the commanding sprint's folder name, so the first start bootstraps the contract and later starts read what it recorded. `_ensure_leaf_enclosure` refuses both published terminal generations before using or materializing any root (`reopen-required`) and raises typed failures for conflicting enclosure bindings and unavailable contract-owned directories. `_start_leaf_enclosure` delegates to the existing checked child, so preparing a leaf neither consults nor changes the calling agent's persistent lifecycle, and the public `worktree_start` semantics stay untouched. `_preparation_refusal` preserves the native status and reason and names the recovery — the stale-base choice, the tool call the owner returned, `task_reopen`, the series-edge reconciliation, or an inspection before repair. `_resolve_workspace` returns the validated group folder plus enclosure metadata (`created` or `found`) for the receipt.

## Evidence

- The recorded master contract supplies the parent hint; an absent contract falls back to the sprint only to bootstrap. [1]
- A refusal keeps the native status and reason and names an owner-derived next action. [2]
- The canonical enclosure path is derived from the leaf document and conflicting bindings are refused. [3]
- The common resolver creates or finds the enclosure and returns its validated roots and preparation outcome. [4]
- Terminal generations refuse before any root use or materialization, and a missing enclosure is created through the child. [5]
- Both entry points prepare through the one checked child without touching the caller lifecycle. [6]
