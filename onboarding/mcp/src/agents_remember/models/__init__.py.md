# mcp/src/agents_remember/models/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Exports-only model initializer: concrete strict/flexible MCP response contracts, token helpers, canonical memory mode and retained domain response names.

## Code Commentary

Actual imports and __all__ expose TOOL_RESPONSE_MODELS from models.tools.tool_registry, not the removed public-registry projection. The conversations package is not imported or re-exported. SlimContextPacket and ContextPacketV2 remain distinct reader/internal model names; PingResponse, ResolveContextResponse and the role start/message/binding trio are not facade exports. A model export advertises no tool or agent allocation. Behavior authority stays in the defining modules; this initializer declares only the import surface.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- [1]
- [2]
