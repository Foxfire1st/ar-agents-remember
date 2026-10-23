# dashboard/src/panels/lifecycle-list/bellSubjects.test.tsx

## Governing Overview

[overview](overview.md)

## Purpose

Pins the bell's task and agent rows against the real consumers in the shell, on the rule that a mock receiving a
string proves nothing about either.

## Code Commentary

The task cases select the leaf the row names and show that the Operations page opens that document, including a
terminal leaf whose enclosure was already cleaned up, which is revealed and selected out of the closed fold; the
tree row is `aria-selected` and plain click and left-arrow still work.

The agent cases drive the real Cockpit: a taskless seat opens through the Chats view with a role-only scope, the
row's agent is asked for through `ar.open`, the observed chat is taken only from the frame's own `shown` report,
and no `/api/role-launch/dispatch` call is made. A task-bound seat carries its role and its own document on the
same route.

The file builds the shell pieces it needs (the Operations tree, the bell, the chats frame and the stub
dashboard) rather than mocking the navigation, because the identity mapping is exactly what these cases exist to
prove.

## Evidence boundary

Source-level React tests at the reviewed freeze, in the dashboard suite. No test was run for this leaf, so they
are not an executed witness, and they are not a live-page witness either:
MIK-R200 evidence item 6 is unrun and carried to L36, and the CPU/resource measurement of item 7 is unrun.
