# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `fbc89847233b1c5959f56475f2cb51f936d5ef0b` |
| lastVerifiedCommitDate | 2026-09-02T07:47:04+02:00|
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

Under CCR-R03@v1 `_record` now builds the immutable record's `curator-coherence/v1` dependency
declaration from the observed code/memory candidate trees, task-topology fingerprint,
digest-bearing task intent, attestation and report digests, every judgment evidence digest, and the
predecessor authority digest — so the published generation is a declared content-addressed consumer
of exactly its inputs cit:([`_record`], mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:227-321).

### Conventions

Only the exact leaf curator or owning sprint architect may publish. Content-addressed generations
are immutable; a byte collision is a developer-decision failure rather than overwrite permission.
Dependency declarations are built with the shared evidence-dependency encoding, exactly as the
currentness validator re-derives them.

### Invariants And Boundaries

- The stable authority is written only after a complete generation and final CAS checks.
- No partial generation can become live.
- Malformed predecessor bytes are replaceable only through an exact prepared digest.
- No clock value enters canonical content, preserving retry identity.
- Snapshot naming uses delivery attempt plus record digest; it cannot version the requirement.
- Publication never invents semantic judgments.
- The declared dependency set is part of the generation installed under CAS: it binds the published
  record to the exact candidate, topology, intent, attestation, and evidence inputs, and no
  unrelated change can stale it.

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
| Immutable generation installation is directory-atomic and collision-safe. | `_publish_generation` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:457-494 |
| Attempt snapshots point at immutable generation artifacts. | `_publish_snapshot` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:495-530 |
| R03 record construction binds the declared dependency set. | `_record` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py:227-321 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The task publication lock is scoped to the configured coordination repository. | `task_publication_lock` | mcp/src/agents_remember/controlplane/task_publication_lock.py:18-36 |

## MCAR-L03 Pair-Bound Publication

The immutable record, observation identity, publication fingerprint, race check, prepared/published
payloads, and validation checklist all include the exact pair. A pair change therefore invalidates
publication and idempotent replay even when candidate files are otherwise valid.

## 260831-CCR-R03 Dependency-Declared Publication

Publication now stamps the record's `curator-coherence/v1` dependency declaration from the exact
observed inputs before CAS installation (worker handover:
notes/reports/260902-CCR-L03-worker-delivery.md).

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the dependency declaration built by `_record` during publication; prior CAS, retry-identity, and pair publication prose preserved.

- 2026-08-29T21:46+02:00 — MCAR-L03: bound publication, CAS/race identity, and validation output
  to the exact code/memory pair. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for deterministic, exact-CAS, crash-safe coherence authority
  publication. Verification remains closeout-owned.