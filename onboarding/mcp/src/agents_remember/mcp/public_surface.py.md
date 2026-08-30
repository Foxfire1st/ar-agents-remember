# mcp/src/agents_remember/mcp/public_surface.py

| Field                  | Value                                                   |
| ---------------------- | ------------------------------------------------------- |
| repository             | agents-remember                                         |
| path                   | `mcp/src/agents_remember/mcp/public_surface.py`         |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-30T17:08:05+02:00                               |
| lastVerifiedCommitHash | `dc03c64a91947cee470622c560c516854eec86b5`              |
| lastVerifiedCommitDate | 2026-08-30T17:41:53+02:00|
| governingOverview      | `../../../overview.md`                                  |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The validator reconciles every public authority and returns content-addressed evidence. | `validate_public_surface`; `PublicSurfaceEvidence` | mcp/src/agents_remember/mcp/public_surface.py:54-60; mcp/src/agents_remember/mcp/public_surface.py:201-212 |
| Dispatch input ownership is one closed four-field vocabulary. | `DISPATCH_AGENT_INPUT_FIELDS`; `_validate_dispatch_schema` | mcp/src/agents_remember/mcp/public_surface.py:25-25; mcp/src/agents_remember/mcp/public_surface.py:146-149 |
| The real-server acceptance enters through public FastMCP APIs. | `test_live_registration_matches_every_public_authority_in_order` | mcp/tests/test_public_surface_conformance.py:233-239 |

## Update History

- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: simplified inventory assertions through
  one fail-closed requirement helper and removed redundant duplicate checks already implied by the
  unique canonical inventory plus exact live order. Verification remains closeout-owned.

- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4: created for the permanent public-surface
  validator. Final verification provenance remains closeout-owned.
