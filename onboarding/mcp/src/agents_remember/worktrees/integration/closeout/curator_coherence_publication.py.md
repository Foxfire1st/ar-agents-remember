# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns status, prepare, publish, and validate dispatch plus crash-safe, idempotent compare-and-swap
publication of curator-coherence generations and optional attempt snapshots.

## Code Commentary

### Logic

`prepare` returns all current identities and the raw stable-authority predecessor digest.
`publish` validates caller-supplied expectations and exact judgments before entering the short task
publication lock. Inside the lock it rereads the contract, rechecks predecessor, source identities,
and evidence bytes, atomically installs a deterministic content-addressed record/report directory,
optionally freezes the attempt pointer, rechecks again, and writes the stable authority last.
`validate` delegates to the shared currentness validator. Publication fingerprints contain all
semantic input, so exact retries converge even after a crash left a generation but not the pointer.

### Conventions

Only the exact leaf curator or owning sprint architect may publish. Content-addressed generations
are immutable; a byte collision is a developer-decision failure rather than overwrite permission.

### Invariants And Boundaries

- The stable authority is written only after a complete generation and final CAS checks.
- No partial generation can become live.
- Malformed predecessor bytes are replaceable only through an exact prepared digest.
- No clock value enters canonical content, preserving retry identity.
- Snapshot naming uses delivery attempt plus record digest; it cannot version the requirement.
- Publication never invents semantic judgments.

### Todos

None recorded.

## Docs References

No external documentation governs this local transaction.

| Finding | Anchor | Source |
| --- | --- | --- |
| The publication transaction is repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The public action dispatcher keeps one tool surface. | `curator_coherence_action` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:56-66 |
| Publication rechecks contract, predecessor, candidates, attestation, topology, and evidence before selecting authority. | `_publish` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:128-208 |
| Immutable generation installation is directory-atomic and collision-safe. | `_publish_generation` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:374-409 |
| Attempt snapshots point at immutable generation artifacts. | `_publish_snapshot` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:412-445 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The task publication lock is scoped to the configured coordination repository. | `task_publication_lock` | mcp/src/agents_remember/controlplane/task_publication_lock.py:18-36 |

## Update History

- 2026-08-29T08:52+02:00 — Created for deterministic, exact-CAS, crash-safe coherence authority
  publication. Verification remains closeout-owned.
