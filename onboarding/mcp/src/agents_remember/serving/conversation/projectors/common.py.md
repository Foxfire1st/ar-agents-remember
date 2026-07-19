# mcp/src/agents_remember/serving/conversation/projectors/common.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/common.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T17:35+02:00 |
| lastVerifiedCommitHash | `41b2fd6452ee572799fa10c4f9c820ab549ec3d2`|
| lastVerifiedCommitDate | 2026-07-19T19:12:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The shared frame-mapping infrastructure for all three per-harness projectors: strict schema
parsing primitives, the four mapper output types the engine consumes, and the provenance
builders that keep producer claims honest (never guessed, never defaulted).

## Code Commentary

### Logic

`required_object`/`required_list`/`required_text` (L33-L48) are the parse-by-schema gate: any
shape that misses an exact required key or type raises `UnmappableShape` (L23-L24), which the
engine converts into preserved `unknown-vendor` evidence — malformed known shapes never kill
the stream and never acquire guessed semantics. The frozen output dataclasses (L55-L94) are the
only things a mapper may emit: `MappedItem` (a fully built item; the engine assigns the real
ordinal/revision), `MappedBlockDelta` (streaming text into one existing item block),
`MappedTurnOutcome` (a native turn settlement feeding canonical status), and
`MappedUnknownVendor` (an unrecognized-but-preserved shape whose raw payload stays server-side).
`provenance`/`harness_provenance`/`unknown_input_provenance` (L97-L140) build the
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
- User-role items without a proven producer keep `unknown-input` lane semantics through
  `unknown_input_provenance`; the provenance batch later resolves exact sources exactly once.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries. This module carries no vendor
semantics of its own; each harness mapper sidecar cites its own schema authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available for this shared module. | — | — |

## Repo-Internal References

The engine catches `UnmappableShape` and mints the fallback unknown-vendor item; the store
consumes the output types; the strict `ProvenanceEvidence`/`ConversationItem` wire models
validate every emitted product.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The engine maps `UnmappableShape` to preserved unknown-vendor evidence, never a stream failure. | L453-L472 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| The store applies `MappedItem`/`MappedBlockDelta` and rebuilds user items through provenance resolution. | L515-L533 | [projector.py](agents-remember/mcp/src/agents_remember/serving/conversation/active/projector.py) |
| `ProvenanceEvidence` and the strict item validator define the products these builders fill. | L315-L403 | [models.py](agents-remember/mcp/src/agents_remember/serving/conversation/models.py) |

## Cross-Repo References

No cross-repository implementation participates in this shared module.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the shared
  mapper infrastructure — strict parsing, the four mapper output types, honest provenance
  builders. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
