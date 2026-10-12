# dashboard/src/cockpit/RoleChatsView.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Render the shared launcher, receipt-selected native frame and report takeover.

## Code Commentary

The view derives the frame target from the selected execution and scope, passes readiness/progress/errors to the shared RoleLauncher, and hides rather than unmounts the pane during a report takeover. Bound document rows render the launcher without a second native frame.

## Boundaries

Presentation only: launch HTTP, options adoption, storage and request identity guards remain in the controls and transport owners. No chat list or report reader is recreated here.

## Evidence

- RoleChatsView is a current owner of the behavior described above. [1]
