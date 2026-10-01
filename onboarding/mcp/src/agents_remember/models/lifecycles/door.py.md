# mcp/src/agents_remember/models/lifecycles/door.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Journal-owned closeout-door generation and publication evidence. The door moved out of the
worktree contract, so this vocabulary carries no contract-byte pair to hash, compare, or re-read;
the intent names the generation and proving it is the journal's own state transition.

## Code Commentary

### Logic

Door generations retain code/memory candidates and bases, task identity, review/coherence,
admission, and scheduling evidence. They contain no `ledgerMemoryCommit` or `ledgerProvenance`,
and dependency construction has no ledger edge. Refreshing or deleting the cache cannot stale a
generation through a cache-provenance fingerprint.

The public surface is `CloseoutDoorGeneration`, `DoorPublicationEvidence`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

Under CCR-R03@v1 the immutable door generation also carries a typed direct-dependency declaration.
`DoorDependencyInputs` freezes the exact code/memory candidate trees, task-topology fingerprint,
digest-bearing task intent, and the review/memory/admission/scheduling provenance records a
source generation reads; `closeout_door_dependencies` builds the `closeout-door/v1` declaration
(the candidate code tree, optional memory tree, semantic-topology and task-intent identities, the
review and coherence provenance-record edges, admission, scheduling, validator, and predecessor edge), and
`require_closeout_door_dependencies` refuses `closeout-door-dependencies-stale` when a generation's
declared inputs no longer match its canonical source facts
cit:([`DoorDependencyInputs`, `closeout_door_dependencies`, `require_closeout_door_dependencies`], mcp/src/agents_remember/models/lifecycles/door.py:146-155; mcp/src/agents_remember/models/lifecycles/door.py:158-196; mcp/src/agents_remember/models/lifecycles/door.py:199-226).

The door cut narrowed a persisted model, so `DoorPublicationEvidence` also tolerates its own
retired bytes on read. `_RETIRED_DOOR_CONTRACT_DIGEST_FIELDS` names the three contract-byte
digests the model carried while the door lived in the worktree contract
(`expectedBeforeContractSha256`, `expectedPublishedContractSha256`,
`observedPublishedContractSha256`); a `model_validator(mode="before")` strips exactly those names
before validation. They are not fields and cannot be written again, but operation records already
on disk still carry them, and `LifecycleOperationRecord.model_validate` reads them back —
including when cleanup archives and reads back a leaf's canonical terminal enclosure evidence.
Only these three names are tolerated, so every other unknown key stays a hard `extra_forbidden`
refusal. This is the treatment a retired `closeout_door:` contract key already gets: tolerant on
read, gone on the next rewrite
cit:([`_RETIRED_DOOR_CONTRACT_DIGEST_FIELDS`, `_drop_retired_contract_digests`], mcp/src/agents_remember/models/lifecycles/door.py:232-236; mcp/src/agents_remember/models/lifecycles/door.py:252-269).

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection. Door dependency edges reuse the shared `ar-evidence-dependencies/v1` encoding instead of a door-private digest scheme.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.
- Door dependencies are declared, never inferred: missing, extra, wrong-version, or stale dependency
  inputs refuse publication/currentness instead of broadening to a universal candidate tuple.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

No configured external domain-documentation source applies.

### Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

- Door generation and dependency construction bind consumed evidence without a ledger identity or provenance edge. [1]
- The module defines `CloseoutDoorGeneration`; `DoorPublicationEvidence` as its public seam. [2]
- The three retired contract-byte digest names and the read-time strip that keeps older persisted operation records loadable while every other unknown key still fails. [3]
- The R03 door dependency vocabulary owned by this record type. [4]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No separate external implementation source applies to this file.

## 260821-CLIVE Canonical Door Contract

The canonical source has exactly four dispositions: `waiting`, `deferred`, `withdrawn`, and
`claimed`. Its immutable generation identity includes candidate, master, sprint, contract and tree
facts, task-topology fingerprint, code/memory/review/admission/scheduling provenance, and
predecessor edges. `claimed` additionally requires the exact operation identity. Cancel, retire,
supersede, commit, certification, and integration outcomes belong to the lifecycle journal, not the
door vocabulary. Public actions are limited to status, declare, defer, resume, withdraw, and
provenance update with an exact action-specific payload matrix.

## 260831-CCR-R03 Declared Door Dependencies

Generation identity now includes the `dependencies` declaration, and the door source/successor
owners recompute it from the exact candidate tree, topology, intent, and provenance records at
currentness time (worker handover: notes/reports/260902-CCR-L03-worker-delivery.md).
