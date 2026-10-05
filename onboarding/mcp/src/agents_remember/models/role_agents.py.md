# mcp/src/agents_remember/models/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines typed role-tool calls, results and finite refusal vocabulary.

## Code Commentary

RoleStartCall extends canonical selection with required UUID and optional override; result distinguishes launch status and saved execution status. RoleMessageCall permits agent ID or exact role references and bounded wait; response distinguishes refusal, delivered/resumed/steered/wait facts and final reply. Public detail/nextAction retain native failure causes without claiming semantic acceptance.

## Evidence

- Frozen implementation of RoleStartCall supporting the stated file behavior. [1]
- Frozen implementation of RoleMessageCall supporting the stated file behavior. [2]
- Frozen implementation of RoleStartResponse supporting the stated file behavior. [3]
- Frozen implementation of RoleMessageResponse supporting the stated file behavior. [4]
