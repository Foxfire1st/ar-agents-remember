# mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper applies embedded AR appearance while preserving standalone theme/fonts/sidebar preferences across shared storage.

## Code Commentary

Remembered user values are persisted before AR overwrite. Exact writer/seen/time records distinguish frame writes from genuine standalone updates; restoration puts frame-owned values back and keeps user changes. Existing content rules handle unobserved writes. One startup migration reads the host's stored sidebar state and opens an old stored-closed list once through the host's own toggle, marked per browser so it never repeats; an early user menu/descendant click takes ownership (MIK-R75 rule 8).

## Invariants And Boundaries

Storage keys, whole-app writes, the host toggle's aria-expanded and the shared clock are pinned unsupported dependencies. The migration never touches the list on later loads and never repeats its automatic click. Styling/polling literals stay local; no new compatibility branch is introduced.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `applyEmbedLook` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:160-184` |
| Current source owner or exact assertion described above. | `restoreStandaloneLook` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:197-236` |
| Current source owner or exact assertion described above. | `recordAppWrite` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:244-265` |
| Current source owner or exact assertion described above. | `openNativeSidebarOnce` | `mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts:272-315` |
| The standalone preference is persisted before the application settings can be overwritten with the embedded appearance. | `never overwrites the user's look before it is kept` | `dashboard/src/cockpit/paseoPluginLook.test.ts:86-97` |
