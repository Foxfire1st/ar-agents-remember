# mcp/src/agents_remember/models/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Exports-only model initializer: concrete strict/flexible MCP response contracts, token helpers, canonical memory mode and retained domain response names.

## Code Commentary

Token-count exports remain in the package vocabulary and are resolved from the canonical models.tokens module on first access; importing the model package alone no longer loads tiktoken.

Actual imports and __all__ expose TOOL_RESPONSE_MODELS from models.tools.tool_registry, not the removed public-registry projection. The conversations package is not imported or re-exported. SlimContextPacket and ContextPacketV2 remain distinct reader/internal model names; PingResponse, ResolveContextResponse and the role start/message/binding trio are not facade exports. A model export advertises no tool or agent allocation. Behavior authority stays in the defining modules; this initializer declares only the import surface.

## Evidence boundary

Current source interpretation only; no fresh execution or grade.

## Source-bound reference inputs

- [1]
- [2]

## The skill-install export is gone

`SkillsInstallResponse` is no longer imported or exported: the skills install surface it described is removed, and the models package exposes no replacement, because the tool server serves skills from the packaged copy instead of installing them into a harness root.

- Token-count exports remain in the package vocabulary and are resolved from the canonical models.tokens module on first access; importing the model package alone no longer loads tiktoken. [3]
