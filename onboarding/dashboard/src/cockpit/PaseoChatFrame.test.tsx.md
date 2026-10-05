# dashboard/src/cockpit/PaseoChatFrame.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite exercises the real dashboard frame component/controller/model and role-pane wiring with explicit backend/channel fixtures.

## Code Commentary

Grouped-navigation cases distinguish launcher intent, shown acknowledgement and plural native selected sets; Hide/Show keeps frame identity. Other cases reject exact-origin/window lookalikes and malformed catalog/activity/selection values, show catalog failures separately from empty data, match pending agent replies, scope Parent errors and exercise unavailable control/Retry.

## Invariants And Boundaries

These fixtures establish source/component behavior, not live native failure transitions. Clipboard policy has its own browser e2e probe; neither suite implies whole-PNT qualification.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `navigates explicit sidebar clicks` | `dashboard/src/cockpit/PaseoChatFrame.test.tsx:125-155` |
| Current source owner or exact assertion described above. | `accepts only the exact normalized` | `dashboard/src/cockpit/PaseoChatFrame.test.tsx:240-270` |
| Current source owner or exact assertion described above. | `steers the mounted frame` | `dashboard/src/cockpit/PaseoChatFrame.test.tsx:717-747` |
| Reads only visible positive-bounds aria-selected native agent tabs and returns the deduplicated plural DOM candidate set. | `watchSelectedChats` | `mcp/src/agents_remember/package_data/paseo_plugin/client/selection.ts:12-41` |
| Rechecks live bridge lifetime, the visible source candidate and the current SDK parent edge after agent refresh before navigation or source-scoped failure. | `installBridge` | `mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts:104-206` |
