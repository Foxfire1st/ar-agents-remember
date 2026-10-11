# dashboard/src/cockpit/PaseoChatFrame.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite exercises the real dashboard frame component/controller/model and role-pane wiring with explicit backend/channel fixtures.

## Code Commentary

Grouped-navigation cases are removed with the dashboard's own sidebar (MIK-R75 rule 7). The remaining cases reject exact-origin/window lookalikes and malformed selection values, match pending agent replies, scope Parent errors to a currently selected source and exercise unavailable control/Retry; the plugin-side pill cases cover an unknown front source (no pill) and a known wide selection (pill returns). Since MIK-R122 the fallback cases pin one agent-URL load with Retry reloading, the no-second-load case pins the settle behavior, and the workspace cases pin message moves without reload.

## Invariants And Boundaries

These fixtures establish source/component behavior, not live native failure transitions. Clipboard policy has its own browser e2e probe; neither suite implies whole-PNT qualification.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- The fallback cases load the agent URL once and reload on Retry. [1]
- The no-second-load case pins the settle behavior. [2]
- The workspace cases move by message without reload. [3]
