# mcp/src/agents_remember/models/lifecycles/direct_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/lifecycles/direct_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-23T16:08+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d` |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Durable direct-landing accepted input and ledger mutation intent.

## Code Commentary

### Logic

The public surface is `DirectLandingOperationInput`, `DirectLandingLedgerIntent`. This module is strict evidence vocabulary, not an I/O or scheduling owner. Its models keep generation, publication, enclosure, termination, legacy, and direct-landing facts explicit so partial or contradictory state fails validation instead of being inferred from queue rows or task prose.

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines `DirectLandingOperationInput`; `DirectLandingLedgerIntent` as its public seam. | `DirectLandingOperationInput`; `DirectLandingLedgerIntent` | mcp/src/agents_remember/models/lifecycles/direct_landing.py:15-47; mcp/src/agents_remember/models/lifecycles/direct_landing.py:50-68 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input model package relocation; direct-landing accepted-input and ledger-intent contracts are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.

