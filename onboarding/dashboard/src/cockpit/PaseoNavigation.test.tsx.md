# dashboard/src/cockpit/PaseoNavigation.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The case checks provider identity, accessible native activity and stable selected-row/click behavior in the external sidebar.

## Code Commentary

Pi, Codex, Claude, Hermes, Eve and an unknown provider remain identifiable. Native state fixtures check Closed/unavailable/Error/input/busy/attention/Idle precedence while retaining the selected button and exact actor click. Disabled catalog rows cannot select.

## Invariants And Boundaries

Fixture busy/input/error/closed states are rendering evidence. The row must not turn them or Idle into PASS/accepted/completed task language.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `keeps actual harness identities` | `dashboard/src/cockpit/PaseoNavigation.test.tsx:34-64` |
| Current source owner or exact assertion described above. | `not.toMatch` | `dashboard/src/cockpit/PaseoNavigation.test.tsx:126-131` |
| Projects the actual SDK provider/activity fields and subscribed updates into the existing hierarchy transport. | `startHierarchy` | `mcp/src/agents_remember/package_data/paseo_plugin/client/hierarchy.ts:76-211` |
