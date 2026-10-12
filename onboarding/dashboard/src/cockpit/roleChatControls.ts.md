# dashboard/src/cockpit/roleChatControls.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

Own scoped request/receipt/error state and connect role-chat actions.

## Code Commentary

Scoped tab storage restores request identity and retry selection. Stable writer callbacks connect the options loader, dispatch and Result transport; Result applies only while the canonical scope and selected UUID still agree. Start uses the latest live-notification callback at acceptance, retains uncertain retry identity, and clears busy state in the dispatch lifecycle.

## Boundaries

The hook composes actions and state, not catalog ordering, native navigation or backend admission. Receipts are runtime evidence, never semantic task acceptance.

## Evidence

- useRoleChatControls is a current owner of the behavior described above. [1]
- useRoleChatRunState is a current owner of the behavior described above. [2]
- useRoleChatRunActions is a current owner of the behavior described above. [3]
- refreshRoleResult is a current owner of the behavior described above. [4]
