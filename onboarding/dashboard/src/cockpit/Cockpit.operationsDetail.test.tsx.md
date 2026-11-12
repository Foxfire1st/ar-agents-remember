# dashboard/src/cockpit/Cockpit.operationsDetail.test.tsx

## Governing Overview

[Area overview](../overview.md)

## Purpose

The Operations detail explains the selected task before any selection, then loads the selected leaf’s steps, review, requirements and role reports. This regression protects the task-page boundary after gate UI removal, not a host-chat or landing flow.

## Code Commentary

### Logic

The fixtures build a master, leaf, running enclosure and independent API responses. The first case requires the Detail heading and prompt without a gate word or mounted task page. The second selects Leaf One and checks each named block, the Worker report, removal of the prompt, exactly one task-body fetch and exactly one role-report fetch. localStorage is cleared between cases.

### Invariants And Boundaries

The body requirement comes from /api/task-document rather than the projected summary. Assertions over rendered content and requests do not prove a real host launch or real server integration.

## Evidence

No Domain Documentation source is configured for this repository-specific boundary.

- Operations detail without selection: implementation/assertion boundary described above. [1]
