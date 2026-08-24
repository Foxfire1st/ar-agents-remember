# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T21:43+02:00 |
| lastVerifiedCommitHash | `23d35f7799153e0c7f3d126291fe2da1662fb87b` |
| lastVerifiedCommitDate | 2026-08-24T21:41:52+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[worktree integration overview](../overview.md)

## Purpose

Canonical locator -> enclosure manifest -> lifecycle journal authority.

## Code Commentary

### Logic

The public surface is `LifecycleOperationLocation`, `EnclosurePublicationArtifacts`, `LifecycleOperationLocationError`, `lifecycle_operation_locator_path`, `lifecycle_enclosure_manifest_path`, `prepare_enclosure_publication`. This is the sole normal location authority: address-only locator to immutable root manifest to canonical root journal, with confinement, repository, identity, and digest cross-checks. Mutable task documents, names, caller-supplied worktree paths, and fallback readers cannot locate normal lifecycle state.

The hard-limit repair extracted pure binding identity, canonical JSON/digest, and bounded-conflict
construction to sibling `lifecycle_operation_binding.py`. This file still owns all path confinement,
locking, exact publication/readback, state transitions, terminal proof, and journal location. The
split creates no second locator or compatibility route.

### Conventions

Pure classifiers return typed observations; mutation owners publish write-ahead intent and exact evidence before advancing. Public projections carry bounded expected/observed facts and executable task-addressed next actions without leaking private operation identity.

### Invariants And Boundaries

- The canonical root journal, located through the address-only locator and immutable enclosure manifest, owns normal lifecycle state.
- Accepted input and proven commits are immutable; retry and recovery stay on the same generation until evidence admits a successor.
- Queue rows and mutable task documents are not lifecycle evidence or fallback location authorities.

### Todos

None recorded beyond the explicit terminal-archive boundary recorded by the governing overview.

## Docs References

No configured Domain Documentation source applies to this repository-internal lifecycle seam.

## Repo-Internal References

The source file is the direct evidence for this file-specific ownership boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module defines the location and publication artifacts at its public seam while re-exporting the canonical error. | `LifecycleOperationLocationError`; `LifecycleOperationLocation`; `EnclosurePublicationArtifacts` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:42-43; mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py:78-125 |

## Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

## 260821-CLIVE Locator-To-Terminal State Machine

Canonical location authority is the exact locator→manifest→journal chain. First publication
reserves the address before manifest/contract proof makes it usable. A terminal locator advances
only through verified external archive and receipt. Successor reservation requires the exact
restartable predecessor, collected prior root, and exact-byte contract replacement. Present-invalid
state fails closed; scans, inference, and missing-root recovery are forbidden.

## Update History

- 2026-08-24T21:43+02:00 — File-size repair: extracted pure enclosure binding/serialization helpers
  to `lifecycle_operation_binding.py`; retained the complete locator-manifest publication state
  machine here. Verified at source commit `23d35f77`.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented the complete reserve/resume/terminal/successor location state machine. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
