# dashboard/src/cockpit/RoleExecutionStatus.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component presents the selected backend execution and separately exposes backend-authorized Revive.

## Code Commentary

Status/detail, optional last reply and report availability are display-only fields. Host failure adds a last-known-status line and explicit reason. RoleReviveControl renders only for canRevive=true and delegates to its owner callback with the current enabled flag.

## Invariants And Boundaries

This file does not poll, launch actors or decide semantic task acceptance. A written report is observation, and revival capability belongs to the backend.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `RoleExecutionStatus` | `dashboard/src/cockpit/RoleExecutionStatus.tsx:10-40` |
| Current source owner or exact assertion described above. | `RoleReviveControl` | `dashboard/src/cockpit/RoleExecutionStatus.tsx:48-65` |
