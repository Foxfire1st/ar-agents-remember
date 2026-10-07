# dashboard/src/cockpit/RoleExecutionStatus.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component renders the launcher's one failure line and separately exposes backend-authorized Revive.

## Code Commentary

The line combines an action failure, an unreachable host and an unresolved launch; it returns nothing when no failure holds, and a successful explicit action clears it. RoleReviveControl renders only for canRevive=true and delegates to its owner callback with the current enabled flag. Execution detail, reply text and report availability are no longer printed here (MIK-R75 rules 1 to 3).

## Invariants And Boundaries

This file does not poll, launch actors or decide semantic task acceptance. A written report is observation, and revival capability belongs to the backend. The line is independent of any reply, so the bar's height does not follow a message.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `RoleExecutionStatus` | `dashboard/src/cockpit/RoleExecutionStatus.tsx:10-40` |
| Current source owner or exact assertion described above. | `RoleReviveControl` | `dashboard/src/cockpit/RoleExecutionStatus.tsx:34-51` |
