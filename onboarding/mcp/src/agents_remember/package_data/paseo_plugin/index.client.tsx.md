# mcp/src/agents_remember/package_data/paseo_plugin/index.client.tsx

## Governing Overview

[Route overview](../../../../overview.md)

## Purpose

The canonical entry wires supported theme/screen/RPC contributions to isolated web helpers.

## Code Commentary

OpenTarget uses the contributed screen's native navigation prop for actor/workspace requests. contribute registers the AR theme/open screen, gathers currentPage and starts the decision helper with the typed embed-list RPC. Native/non-web gets no page bridge; unsupported web dependencies live under client/.

## Invariants And Boundaries

Dashboard tests/typechecks helper modules; entry/server compilation is separate qualification. Declared wiring does not prove live framing or future compatibility.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `OpenTarget` | `mcp/src/agents_remember/package_data/paseo_plugin/index.client.tsx:45-75` |
| Current source owner or exact assertion described above. | `contribute` | `mcp/src/agents_remember/package_data/paseo_plugin/index.client.tsx:55-76` |
