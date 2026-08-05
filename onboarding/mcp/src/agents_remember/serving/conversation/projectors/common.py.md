# mcp/src/agents_remember/serving/conversation/projectors/common.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/projectors/common.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-26T15:34 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation projectors overview](overview.md)

## Purpose

The shared frame-mapping infrastructure for all three per-harness projectors: strict schema
parsing primitives, the four mapper output types the engine consumes, and the provenance
builders that keep producer claims honest (never guessed, never defaulted).

## Code Commentary

### Logic

`required_object`/`required_list`/cit:([`required_text`], mcp/src/agents_remember/serving/conversation/projectors/common.py:46-49) are the parse-by-schema gate: any
shape that misses an exact required key or type raises cit:([`UnmappableShape`], mcp/src/agents_remember/serving/conversation/projectors/common.py:24-25), which the
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

## Docs References

The resolved `Domain Documentation` registry has no entries. This module carries no vendor
semantics of its own; each harness mapper sidecar cites its own schema authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this shared module. | — | — |

## Repo-Internal References

The engine catches `UnmappableShape` and mints the fallback unknown-vendor item; the store
consumes the output types; the strict `ProvenanceEvidence`/`ConversationItem` wire models
validate every emitted product.

| Finding | Anchor | Source |
| --- | --- | --- |
| Native evidence ingestion maps `UnmappableShape` (and an over-budget truncated frame) to preserved `MappedUnknownVendor` evidence, never a stream failure; thread binding and roster reconciliation still apply to malformed agent-thread frames. | `NativeEvidenceIngestion` | mcp/src/agents_remember/serving/conversation/active/projector/native_ingestion.py:44-268 |
| Echo ingestion takes the same containment for a submission echo it cannot parse. | `EchoIngestion` | mcp/src/agents_remember/serving/conversation/active/projector/echo_ingestion.py:35-187 |
| `ProjectionMutationStream.apply_outputs` routes `MappedItem`/`MappedBlockDelta`/`MappedUnknownVendor` into the store and buffers `MappedTurnOutcome` as the pending terminal. | `ProjectionMutationStream` | mcp/src/agents_remember/serving/conversation/active/projector/mutation_stream.py:49-197 |
| The rebuild coordinator resolves pending user-item provenance in a bounded batch and applies each record to the store. | `RebuildCoordinator` | mcp/src/agents_remember/serving/conversation/active/projector/rebuild_coordinator.py:63-192 |
| `ProvenanceEvidence` and the strict item validator define the products these builders fill. | `ProvenanceEvidence` | mcp/src/agents_remember/serving/conversation/models.py:193-199 |

## Cross-Repo References

No cross-repository implementation participates in this shared module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T03:00:00+02:00 — 260731-EFA-L6-W3-B01 curator: curated 5 Repo-Internal citation claims with exact ingestion, mutation, rebuild, and mapper-output anchors. Verification metadata remains unchanged for closeout.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 2 cross-file line citations broken by the `active/projector.py` -> `active/projector/` package split, expanding them into 4 rows because the consumers landed in different modules. `UnmappableShape` containment plus thread binding/roster reconciliation is `native_ingestion.py` L159-L200; the echo-side equivalent is `echo_ingestion.py` L165-L178; the `MappedItem`/`MappedBlockDelta`/`MappedUnknownVendor` routing into the store is `ProjectionMutationStream.apply_outputs` in `mutation_stream.py` L85-L100; the user-item provenance rebuild is `RebuildCoordinator._resolve_provenance` in `rebuild_coordinator.py` L179-L192.

- 2026-07-26T15:34 — 260718-CHATS-L7: `MappedUnknownVendor` gained the optional
  `agent: ConversationAgentRef` field (L92-L96, fix-round review finding 4) so a malformed
  AGENT-thread frame's preserved evidence stays in that agent's view, never the parent's.
  Sidecar: documented the field and its degrade-not-fatal-but-agent-honest invariant; refreshed
  citations (parse gate L34-L49, outputs L56-L99, builders L102-L145) and re-pointed the
  projector.py citations displaced by the L7 multiplexed-projection rewrite (L453-L472 →
  L856-L879; L515-L533 → L969/L986-L1004) plus the models.py product lines (L315-L403 →
  L197-L204/L341-L431). Uncommitted; closeout re-stamps verification.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: created the sidecar for the shared
  mapper infrastructure — strict parsing, the four mapper output types, honest provenance
  builders. Verification is blank because the new source file is uncommitted; closeout owns its
  first source stamp.
