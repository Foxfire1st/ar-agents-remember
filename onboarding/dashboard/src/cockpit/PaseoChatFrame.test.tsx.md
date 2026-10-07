# dashboard/src/cockpit/PaseoChatFrame.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The suite exercises the real dashboard frame component/controller/model and role-pane wiring with explicit backend/channel fixtures.

## Code Commentary

Grouped-navigation cases are removed with the dashboard's own sidebar (MIK-R75 rule 7). The remaining cases reject exact-origin/window lookalikes and malformed selection values, match pending agent replies, scope Parent errors to a currently selected source and exercise unavailable control/Retry; the plugin-side pill cases cover an unknown front source (no pill) and a known wide selection (pill returns).

## Invariants And Boundaries

These fixtures establish source/component behavior, not live native failure transitions. Clipboard policy has its own browser e2e probe; neither suite implies whole-PNT qualification.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `reports Parent failure only for a current visible native tab, including split panes, with no pending dashboard request` | `dashboard/src/cockpit/PaseoChatFrame.test.tsx:100-134` |
| Current source owner or exact assertion described above. | `accepts the selection-set protocol and ignores dashboard-only catalog messages` | `dashboard/src/cockpit/PaseoChatFrame.test.tsx:135-189` |
| Current source owner or exact assertion described above. | `steers the mounted frame and keeps it across launcher selections without dashboard navigation` | `dashboard/src/cockpit/PaseoChatFrame.test.tsx:596-666` |
| Reads only visible positive-bounds aria-selected native agent tabs and returns the deduplicated plural DOM candidate set. | `watchSelectedChats` | `mcp/src/agents_remember/package_data/paseo_plugin/client/selection.ts:21-51` |
| Rechecks live bridge lifetime, the visible source candidate and the current SDK parent edge after agent refresh before navigation or source-scoped failure. | `installBridge` | `mcp/src/agents_remember/package_data/paseo_plugin/client/bridge.ts:104-206` |
