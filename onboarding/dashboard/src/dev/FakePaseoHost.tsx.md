# dashboard/src/dev/FakePaseoHost.tsx

## Governing Overview

[dashboard/src overview](../overview.md)

## Purpose

Development-only fake Paseo host for the cross-workspace chat fixture at `/dev/fake-paseo-host`.
The page models a Paseo application with two workspaces and runs the REAL plugin client part
(`startClientPart` into `installBridge`) against a stubbed SDK, so the dashboard side under test
talks to genuine bridge code. Never shipped: `App` loads `DevApp` only under `import.meta.env.DEV`.

## Code Commentary

`FakePaseoHost` boots the real client part once in an effect and renders native-faithful markup:
visible selected agent tabs (`workspace-tab-agent_<id>`) in its wide layout and a switcher
trigger with the mounted agent chat scroll in its compact mode. `createFakeClient` models pinned
Paseo 0.16.2 navigation. An open names the agent alone, and the fake resolves the workspace from
its own agent table. `?stall=1` leaves every open unapplied; `?compact=1` renders
the narrow layout; `?open=agent:<id>` deep-links the first visit.

## Invariants And Boundaries

The development fixture models two fixed workspaces and four fixed agents. The stubbed
directory returns one snapshot and no continuation pages.

## Evidence

- The page runs the real plugin client part against the stubbed two-workspace SDK. [1]

- The fake resolves an opened agent’s workspace from its own agent table. [2]
