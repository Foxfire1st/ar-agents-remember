# mcp/src/agents_remember/models/lifecycles/enclosure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/enclosure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Strict immutable records for lifecycle enclosure addressability.

## Code Commentary

### Logic

The public surface is `LifecycleEnclosureManifest`, `LifecycleEnclosureLocator`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

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
| The module defines `LifecycleEnclosureManifest`; `LifecycleEnclosureLocator` as its public seam. | L21-L40; L43-L109 | `mcp/src/agents_remember/models/lifecycles/enclosure.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Terminal And Successor Contract

Enclosure models now carry successor-enclosure publication, an exact predecessor terminal link,
external terminal receipt, and bounded archived canonical entries with path/digest/byte validation.
Cleanup and abandon have distinct exact argument models. A terminal locator is authoritative only
with matching archive and receipt proof; a successor manifest, locator, and contract must all carry
the same exact predecessor. Missing worktree state never manufactures succession authority.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded the archive/receipt/terminal-predecessor enclosure state machine. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
