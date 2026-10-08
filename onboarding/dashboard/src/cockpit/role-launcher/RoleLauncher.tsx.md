# dashboard/src/cockpit/role-launcher/RoleLauncher.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The extracted role launcher: one row of controls that fills or accepts a selection, reports preparation progress and one failure line, and dispatches a start.

## Code Commentary

`RoleLauncher` renders the role and native agent/model/effort controls from its admitted selection and options. A bound caller (the document rail) hides the reference fields it already knows, disables a role with an open execution and labels the occupant as running, and keeps an uncertain request's exact identity. The row is one fixed-height control strip: during a start it shows the preparation phase from `useRoleLaunchProgress`, and a refusal, lock or failed action produces exactly one failure line with the owner's remedy. The component was extracted from `RoleChats.tsx` so the Chats pane and the document rail share one launcher; it adds no list of workspaces and no execution prose.

## Evidence

- A bound row decides startability from the bound role, the live occupant and the canStart answer. [1]
- Bound mode omits the reference fields the selection already determines. [2]
- The row is one control strip that can carry the preparation line. [3]

## Investigator scope and request identity

Ordinary singleton and Projects bound rows still adopt an open request and disable a second start. Selected sprint/master Investigator rows may start another per-request execution under backend capacity admission; existing uncertainty still preserves the exact request for Retry. The exception changes receipt cardinality without adding controls, execution prose, report navigation or primary-chat replacement.


- The current source implements this file’s stated Investigator boundary. [5]


## Refreshed current evidence

- The exported launcher renders controls, progress and the single failure line for both hosts. [4]
