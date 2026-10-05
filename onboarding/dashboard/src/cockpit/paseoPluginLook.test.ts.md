# dashboard/src/cockpit/paseoPluginLook.test.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The tests preserve standalone appearance/sidebar preferences when a frame shares the browser store.

## Code Commentary

Cases save before overwrite, restore missing keys/default sidebar and distinguish frame from user writes. Genuine standalone AR-theme choice and open/closed preference remain the user's. Matching seen/writer records and write time support provenance; existing content rules govern unobserved records, with separate refusal tests.

## Invariants And Boundaries

A content inference is not recorded writer provenance or universal browser qualification.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `never overwrites` | `dashboard/src/cockpit/paseoPluginLook.test.ts:86-116` |
| Current source owner or exact assertion described above. | `records who wrote the sidebar` | `dashboard/src/cockpit/paseoPluginLook.test.ts:310-340` |
| Current source owner or exact assertion described above. | `records nothing for other keys` | `dashboard/src/cockpit/paseoPluginLook.test.ts:394-410` |
| Saves standalone look/sidebar values before storing the AR appearance, and keeps earlier saved values when the last recorded writer was a frame. | `applyEmbedLook` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:158-182` |
