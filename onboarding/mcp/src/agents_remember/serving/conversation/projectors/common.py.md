# mcp/src/agents_remember/serving/conversation/projectors/common.py

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The shared frame-mapping infrastructure for all three per-harness projectors: strict schema
parsing primitives, the four mapper output types the engine consumes, and the provenance
builders that keep producer claims honest (never guessed, never defaulted).

## Code Commentary

### Logic

`required_object`/`required_list`/cit:([`required_text`], mcp/src/agents_remember/serving/conversation/projectors/common.py:46-49) are the parse-by-schema gate: any
shape that misses an exact required key or type raises cit:([`UnmappableShape`], mcp/src/agents_remember/serving/conversation/projectors/common.py:26-27), which the
engine converts into preserved `unknown-vendor` evidence — malformed known shapes never kill
the stream and never acquire guessed semantics. cit:([`MappedItem`, `MappedBlockDelta`, `MappedTurnOutcome`, `MappedUnknownVendor`], mcp/src/agents_remember/serving/conversation/projectors/common.py:56-60; mcp/src/agents_remember/serving/conversation/projectors/common.py:63-69; mcp/src/agents_remember/serving/conversation/projectors/common.py:72-78; mcp/src/agents_remember/serving/conversation/projectors/common.py:81-95) are the
only things a mapper may emit: `MappedItem` (a fully built item; the engine assigns the real
ordinal/revision), `MappedBlockDelta` (streaming text into one existing item block),
`MappedTurnOutcome` (a native turn settlement feeding canonical status), and
`MappedUnknownVendor` (an unrecognized-but-preserved shape whose raw payload stays server-side).
`MappedUnknownVendor` also carries an
optional `agent: ConversationAgentRef` (L92-L96; fix-round review finding 4): a malformed AGENT-thread frame's preserved
evidence belongs to that agent's view, never the parent's; `None` means the parent conversation.
`provenance`/`harness_provenance`/cit:([`unknown_input_provenance`], mcp/src/agents_remember/serving/conversation/projectors/common.py:136-144) build the
`ProvenanceEvidence` values; `unknown_input_provenance` is the honest user-input product when no
producer can be proven — it never defaults to operator or the bus.

### Conventions

Mappers are pure: no IO, no clock, no engine state. Every vendor-specific module imports its
parsing and provenance vocabulary from here so the three projectors cannot drift apart in how
they fail or how they attribute evidence.

### Invariants And Boundaries

- A mapper never assigns `global_ordinal`, real revisions, or envelope fields — that is the
  engine/store boundary.
- `UnmappableShape` is the only failure channel for shape mismatches; mappers never fabricate a
  message, tool, or control meaning for an unrecognized frame.
- Degrade-not-fatal stays agent-honest: unknown-vendor evidence minted for a
  malformed sub-agent-thread frame must stay bound to that agent via the `agent` field — it
  never leaks into the parent conversation's view.
- User-role items without a proven producer keep `unknown-input` lane semantics through
  `unknown_input_provenance`; the provenance batch later resolves exact sources exactly once.

### Todos

None.

## Evidence

### Docs References

The resolved `Domain Documentation` registry has no entries. This module carries no vendor
semantics of its own; each harness mapper sidecar cites its own schema authority.

No configured domain documentation was available for this shared module.

### Repo-Internal References

The engine catches `UnmappableShape` and mints the fallback unknown-vendor item; the store
consumes the output types; the strict `ProvenanceEvidence`/`ConversationItem` wire models
validate every emitted product.

- Native evidence ingestion maps `UnmappableShape` (and an over-budget truncated frame) to preserved `MappedUnknownVendor` evidence, never a stream failure; thread binding and roster reconciliation still apply to malformed agent-thread frames. [1]
- Echo ingestion takes the same containment for a submission echo it cannot parse. [2]
- `ProjectionMutationStream.apply_outputs` routes `MappedItem`/`MappedBlockDelta`/`MappedUnknownVendor` into the store and buffers `MappedTurnOutcome` as the pending terminal. [3]
- The rebuild coordinator resolves pending user-item provenance in a bounded batch and applies each record to the store. [4]
- `ProvenanceEvidence` and the strict item validator define the products these builders fill. [5]

### Cross-Repo References

No cross-repository implementation participates in this shared module.

No meaningful cross-repo references found.
