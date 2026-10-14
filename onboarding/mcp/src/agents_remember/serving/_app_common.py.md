# mcp/src/agents_remember/serving/_app_common.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Shared serving collaborators, the runtime bundle, and projection/SSE helpers. This module carries optional review and reader ports across the layering boundary; it owns no terminal route bodies, WebSocket bridge, inbox registrar or capsule-launch resolver.

## Code Commentary

ServingCollaborators holds the distinct subject-review, entry-list, source-content, intent-summary, tree-view and path-reader ports plus tree-view shutdown and extra-route hooks. An omitted port is a missing capability, not an empty result. The runtime contains configuration, projector, clock, build, interval and the tree-child shutdown hook; it is not a terminal host. LiveProjectionInputs resolves unset provider/landing/change-watch toggles from the replay seam. The projection dump is memoized by published instance, copied before the serve-time build tail, and reused for SSE snapshots; deltas remain individual nodes.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [12]
- [13]
- [14]
- [15]
- [16]
- [17]
- [20]
- [21]
- [22]
- [23]
- [24]
- [27]
- [28]
- [30]

