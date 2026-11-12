# mcp/src/agents_remember/package_data/paseo_plugin/client/look.ts

## Governing Overview

[Route overview](../../../../../overview.md)

## Purpose

The helper applies embedded AR appearance while preserving standalone theme/fonts/sidebar preferences across shared storage.

## Code Commentary

Remembered user values are persisted before AR overwrite. Exact writer/seen/time records distinguish frame writes from genuine standalone updates; restoration puts frame-owned values back and keeps user changes. Existing content rules handle unobserved writes. One startup migration reads the host's stored sidebar state and opens an old stored-closed list once through the host's own toggle, marked per browser so it never repeats; an early user menu/descendant click takes ownership (MIK-R75 rule 8).

## Invariants And Boundaries

Storage keys, whole-app writes, the host toggle's aria-expanded and the shared clock are pinned unsupported dependencies. The migration never touches the list on later loads and never repeats its automatic click. Styling/polling literals stay local; no new compatibility branch is introduced.

The early menu-click guard uses a structural optional `closest` probe rather than the DOM library's `Element` type, because this plugin package compiles without that library. It keeps the same null and optional-method runtime checks; the type-only substitution does not change who owns the sidebar choice.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Current source owner or exact assertion described above. [1]
- Current source owner or exact assertion described above. [2]
- Current source owner or exact assertion described above. [3]
- Current source owner or exact assertion described above. [4]
- The standalone preference is persisted before the application settings can be overwritten with the embedded appearance. [5]
