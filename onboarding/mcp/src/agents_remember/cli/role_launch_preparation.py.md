# mcp/src/agents_remember/cli/role_launch_preparation.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Resolves role defaults, workspace, admitted reader scope, compiled capsule and handover before native creation.

## Code Commentary

prepare_role_handover validates selection before workspace/enclosure changes. _ar_mcp_context carries exact taskDocReadArgs and per-call taskContext; leaf enclosure roots come from canonical authority, while real sprint/master roles share their selected Projects task workspace. _compile_handover records launcher/native parent ownership, operation, source build and canonical artifact/report locations; Revive only compares saved/current leaf scope. MIK-R93@v1 makes both host values depend on one condition: any role with a starting parent receives the parent-routed `developerQuestions` that sends the developer's decision to the parent agent id with `role_message` and keeps working, and `_owner_relation(started_by, role=...)` names the parent — for a leaf Worker, Reviewer or Curator with the direct sibling seat routes and no routine result to the parent — while every parentless or dashboard launch keeps the base sentence. All other ownership data, parent identity, tool grants and the L72 coordinating-role text stay byte-identical.

## 260928-MIK-L99 — a leaf's agents hand over to each other

`_compile_handover` appends exactly one value for a leaf Worker, Reviewer or Curator: `leafSeats` with the three seat roles and, for each other seat, the exact `role_message` arguments containing the canonical sprint, master and leaf references and no sibling agent id. Every other role's handover keeps its values byte for byte under identical compiled inputs; the declarative addition is the leaf's only production runtime change, while the derived capsule and skill-revision digests change with the source revision, so the preservation claim is same-input, not cross-revision.

## 260928-MIK-R93 — parent-presence handover values

The condition is now parent presence: every parentable role (orchestrator, manager, worker, reviewer, curator, system-specialist) gets the parent-routed `developerQuestions` naming the actual parent agent id, and the leaf Worker, Reviewer and Curator additionally get `leafSeats` peer routes with no routine result ordered to the parent. Every parentless or dashboard launch keeps the base sentence byte for byte; the native parent identity, the L72 coordinator text and all tool grants stay unchanged.

## Evidence

- Frozen implementation of prepare_role_handover supporting the stated file behavior. [1]
- Frozen implementation of _ar_mcp_context supporting the stated file behavior. [2]
- The `_resolve_workspace` implementation now lives in its extracted owner. [3]

- Frozen implementation of the narrow parented-coordinator handover values. [4]

- Checks reuse, explicit refresh and changed daemon home in the key. [5]
- Checks rejected choices create no receipt, workspace, agent or enclosure. [6]
- Changed/missing saved scope refuses with both pairs, no bridge/write/enclosure creation. [7]

## MIK-R95 Workspace Owner Extracted

The enclosure preparation owner moved to `role_launch_workspace.py`: `_leaf_contract_path`, `_resolve_workspace`, `_ensure_leaf_enclosure` and the new `_recorded_parent`/`_preparation_refusal`/`_start_leaf_enclosure` live there, and this module imports `_leaf_contract_path`/`_resolve_workspace` from it. `prepare_role_handover` keeps the capsule/handover compilation and owner-relation values unchanged.
