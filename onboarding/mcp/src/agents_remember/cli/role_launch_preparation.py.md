# mcp/src/agents_remember/cli/role_launch_preparation.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Resolves role defaults, workspace, admitted reader scope, compiled capsule and handover before native creation.

## Code Commentary

prepare_role_handover validates selection before workspace/enclosure changes. _ar_mcp_context carries exact taskDocReadArgs and per-call taskContext; leaf enclosure roots come from canonical authority, while real sprint/master roles share their selected Projects task workspace. _compile_handover records launcher/native parent ownership, operation, source build and canonical artifact/report locations; Revive only compares saved/current leaf scope.

## Evidence

- Frozen implementation of prepare_role_handover supporting the stated file behavior. [1]
- Frozen implementation of _ar_mcp_context supporting the stated file behavior. [2]
- Frozen implementation of _resolve_workspace supporting the stated file behavior. [3]
- Frozen implementation of _compile_handover supporting the stated file behavior. [4]
- Checks reuse, explicit refresh and changed daemon home in the key. [5]
- Checks rejected choices create no receipt, workspace, agent or enclosure. [6]
- Changed/missing saved scope refuses with both pairs, no bridge/write/enclosure creation. [7]
