# mcp/src/agents_remember/mcp/public_surface.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

`public_surface.py` is the permanent executable agreement between the independently declared MCP
surface authorities: ordered `PUBLIC_TOOLS`, reserved names, the response-model registry, a live
FastMCP `list_tools` result, and the public `dispatch_agent` input schema and description.

## Code Commentary

### Logic

`validate_public_surface(live_tools)` consumes only FastMCP's public tool objects. It refuses
duplicate or overlapping inventories, response-registry drift, public leakage of the internal
`spawn_agent_session` primitive, missing or duplicated `dispatch_agent`, live-order drift, an open
or malformed dispatch schema, role-enum drift, and a description that omits the plane-versus-
ambient caller contract. On success it returns ordered tool names plus a content-addressed schema
digest and the exact response-model name.

`validate_dispatch_advertisement(...)` is the same canonical dispatch-description and closed-
schema validator at the real-client boundary. It accepts the consumer-observed name, description,
and input schema, then returns the same content-addressed schema digest. A client that exposes a
single deferred-search result can therefore prove the dispatch contract without reconstructing or
weakening the full MCP inventory validation.

The dispatch schema is deliberately closed to undeclared inputs. In particular, model/effort or
other spend controls cannot be silently ignored or routed around the settings-owned profile.

### Invariants And Boundaries

- This module validates independent authorities; it does not generate one authority from another
  and therefore cannot make a self-referential parity test green.
- `dispatch_agent` is the sole public spawn vocabulary. `spawn_agent_session` remains internal while
  retaining its typed response-model mapping for trusted composition.
- Live tool order must equal `PUBLIC_TOOLS`; sorting or set comparison cannot hide drift.
- Schema refs are resolved only inside the supplied schema. External refs and malformed nodes fail.
- The validator never reaches into FastMCP private registries or adds a compatibility fallback.
- Full public-surface validation and one-tool consumer acceptance share the same dispatch contract;
  neither route owns a second schema interpretation.

## Evidence

### Repo-Internal References

- The validator reconciles every public authority and returns content-addressed evidence. [1]
- Dispatch input ownership is one closed four-field vocabulary. [2]
