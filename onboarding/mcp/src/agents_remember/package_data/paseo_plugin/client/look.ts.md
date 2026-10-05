# mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper applies embedded AR appearance while preserving standalone theme/fonts/sidebar preferences across shared storage.

## Code Commentary

Remembered user values are persisted before AR overwrite. Exact writer/seen/time records distinguish frame writes from genuine standalone updates; restoration puts frame-owned values back and keeps user changes. Existing content rules handle unobserved writes. One startup menu collapse acts only when expanded and yields to earlier user menu/descendant clicks.

## Invariants And Boundaries

Storage keys, whole-app writes, menu aria-expanded and shared clock are pinned unsupported dependencies. Styling/polling literals stay local; no new compatibility branch is introduced.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `applyEmbedLook` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:158-182` |
| Current source owner or exact assertion described above. | `restoreStandaloneLook` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:195-234` |
| Current source owner or exact assertion described above. | `recordAppWrite` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:242-263` |
| Current source owner or exact assertion described above. | `collapseNativeSidebarAtLoad` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:270-291` |
| The standalone preference is persisted before the application settings can be overwritten with the embedded appearance. | `never overwrites the user's look before it is kept` | `dashboard/src/cockpit/paseoPluginLook.test.ts:86-116` |
