# mcp/src/agents_remember/application/lifecycle/lifecycle_enclosure_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/lifecycle/lifecycle_enclosure_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T00:27+02:00 |
| lastVerifiedCommitHash | `1d446724d099517f6f52d596b47827ae2391a2a4` |
| lastVerifiedCommitDate | 2026-08-24T00:21:10+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[governing route overview](../overview.md)

## Purpose

Explicit public migration into canonical lifecycle-enclosure addressability.

## Code Commentary

### Logic

The public surface is `EnclosureAdoptionRequest`, `worktree_enclosure_adopt_tool`. This application boundary exposes a closed public result and delegates durable mutation to its owning domain seam. Expected configured-contract, location, or legacy failures are translated through typed decisions; callers do not enumerate lower-level exception families or invent alternate authority.

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
| The module defines `EnclosureAdoptionRequest`; `worktree_enclosure_adopt_tool` as its public seam. | L23-L31; L34-L102 | `mcp/src/agents_remember/application/lifecycle/lifecycle_enclosure_tools.py` |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## Update History

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/application/lifecycle/lifecycle_enclosure_tools.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
