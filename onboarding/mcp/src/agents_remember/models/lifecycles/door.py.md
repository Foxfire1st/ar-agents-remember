# mcp/src/agents_remember/models/lifecycles/door.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/door.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Contract-owned closeout-door generation and publication evidence.

## Code Commentary

### Logic

The public surface is `CloseoutDoorGeneration`, `DoorPublicationEvidence`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

### Conventions

The file exposes typed values or one narrow operation boundary. Callers consume those values directly rather than reconstructing lower-level state from strings, mutable task documents, or queue projection.

### Invariants And Boundaries

- Preserve the module's single ownership seam; do not add a fallback reader or duplicate authority.
- Expected refusal states remain typed and bounded, while unexpected programming faults remain loud.
- Durable lifecycle facts live in the canonical root journal; scheduling projections may only consume them.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file itself is the current evidence for this file-specific contract.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The module defines `CloseoutDoorGeneration`; `DoorPublicationEvidence` as its public seam. | L22-L54; L57-L79 | `mcp/src/agents_remember/models/lifecycles/door.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Canonical Door Contract

The canonical source has exactly four dispositions: `waiting`, `deferred`, `withdrawn`, and
`claimed`. Its immutable generation identity includes candidate, master, sprint, contract and tree
facts, task-topology fingerprint, code/memory/ledger/review/admission/scheduling provenance, and
predecessor edges. `claimed` additionally requires the exact operation identity. Cancel, retire,
supersede, commit, certification, and integration outcomes belong to the lifecycle journal, not the
door vocabulary. Public actions are limited to status, declare, defer, resume, withdraw, and
provenance update with an exact action-specific payload matrix.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: reconciled the full door-generation and request vocabulary. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
