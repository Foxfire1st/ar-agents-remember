# mcp/src/agents_remember/models/lifecycles/preparation.py

## Governing Overview

[Owning overview](overview.md)

## Purpose

Closed preparation intent, genuine existing memory proof and raw commit output vocabulary.

## Code Commentary

### Logic

`PreparationLeg` is `code` or `memory-content`. Existing memory reuse binds the exact
`logicalHeadCommit` and raw `logicalHeadTree`, plus a separate `certifiedContentTree` for the
cache-free memory view. It requires no ledger blob or code-to-memory cache row. A reused intent
must retain that exact historical HEAD/tree and cannot also enable a new write.

Intents bind one operation/generation/leg to logical roots, common repository, expected-old and preparation-parent identities, admitted tree, observed configuration/hooks and original frozen-run/candidate/certificate references. Enabled writes require a real private path and message. Existing code forbids invented private inputs. Existing memory reuse requires an exact HEAD/tree and certified-content proof. Memory intents require a Gate-5 certificate reference, whose actual authority is checked above the model layer. The raw-byte factory derives commit/tree/parents/identity/date/message/signature-presence digests and validates their exact intent relationship. Signature presence is not signature verification; private existence is not delivery or certification.

### Conventions

Use the named source owners directly. The original source was introduced in commit `245057ab16e19afdaabd5c188c9576b22e0c0870`; the current uncommitted LCA-L9 candidate changes its reuse proof. Historical verification metadata remains distinct from that candidate review.

### Invariants And Boundaries

The documented types and paths do not themselves establish execution, certification, delivery or acceptance. Those claims require the corresponding owning runtime evidence.

### Todos

No source-local TODO is asserted here.

## Evidence

### Docs References

No configured domain documentation applies.

### Repo-Internal References

- Memory reuse binds exact raw HEAD/tree plus certified content and cannot simultaneously request a new write. [1]
- `_canonical_preparation_path` owns the corresponding behavior described above. [2]
- `ExistingMemoryPreparationProof` owns the corresponding behavior described above. [3]
- `_one_header` owns the corresponding behavior described above. [4]
- `_identity_date` owns the corresponding behavior described above. [5]
- `_require_output_headers` owns the corresponding behavior described above. [6]
- `require_prepared_output_matches_intent` owns the corresponding behavior described above. [7]

### Cross-Repo References

No cross-repository source is needed for this card.
