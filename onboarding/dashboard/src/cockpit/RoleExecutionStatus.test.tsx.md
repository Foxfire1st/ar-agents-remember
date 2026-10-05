# dashboard/src/cockpit/RoleExecutionStatus.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite verifies honest execution fields and selected-execution Result/Revive wiring.

## Code Commentary

Status/detail, last reply and report availability are displayed from backend values. Host failure labels last-known status, and Revive appears only with canRevive. Launcher cases refresh another turn, treat a launch lock separately from refusal, keep stale status visible, and revive the exact selected request while retaining a refused alert.

## Invariants And Boundaries

These fixtures prove UI behavior rather than native actor resume or task acceptance.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `shows the status, the detail` | `dashboard/src/cockpit/RoleExecutionStatus.test.tsx:25-55` |
| Current source owner or exact assertion described above. | `offers Revive only` | `dashboard/src/cockpit/RoleExecutionStatus.test.tsx:66-96` |
| Current source owner or exact assertion described above. | `revives the selected execution` | `dashboard/src/cockpit/RoleExecutionStatus.test.tsx:182-201` |
