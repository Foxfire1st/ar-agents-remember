# dashboard/src/dev/FakePaseoHost.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

DEV-only fake Paseo host for the MIK-R121 cross-workspace chat repair rig (`/dev/fake-paseo-host`).
The page models a Paseo application with two workspaces and runs the REAL plugin client part
(`startClientPart` into `installBridge`) against a stubbed SDK, so the dashboard side under test
talks to genuine bridge code. Never shipped: `App` loads `DevApp` only under `import.meta.env.DEV`.

## Code Commentary

`FakePaseoHost` boots the real client part once in an effect and renders native-faithful markup:
visible selected agent tabs (`workspace-tab-agent_<id>`) on wide layouts, and below the desktop
breakpoint the switcher trigger with the mounted agent chat scroll. `createFakeClient` models the
pinned native navigation truth: an open names the agent alone and the application resolves its
workspace from its own agent table. `?stall=1` leaves every open unapplied; `?compact=1` renders
the narrow layout; `?open=agent:<id>` deep-links the first visit.

## Invariants And Boundaries

DEV-only test rig for the MIK-R121 repair; it carries no product contract. The two workspaces
and four agents are fixed literals; the stubbed directory answers snapshot once and never pages.

## Evidence

- The page runs the real plugin client part against the stubbed two-workspace SDK. [1]
- An opened agent's workspace is resolved from the fake's own agent table, never from the frame. [2]
