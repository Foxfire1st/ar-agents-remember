# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Renders the deterministic human-readable Markdown projection of one structured coherence record.

## Code Commentary

### Logic

`render_curator_coherence` prints the separately bound requirement revision, delivery attempt,
candidate trees, topology, attestation, predecessor, publisher, and every source-candidate judgment
in attestation order. Cell escaping keeps arbitrary rationale text inside the generated table.

Since 260831-CCR (commit `99dc249b`) the renderer emits a `Task intent:` line immediately after
the task topology fingerprint when the record carries a `TaskIntentIdentity`
(`isinstance(record.taskIntent, TaskIntentIdentity)`, line 53-56), so the human projection shows
the exact canonical `task-intent/v1` schema and digest bound by coherence publication.

### Conventions

The renderer is one-way. Consumers regenerate and byte-compare this projection; no parser exists.

### Invariants And Boundaries

- Rendered output contains no clock entropy and is deterministic for the same record.
- The projection is never machine authority.
- Every evidence reference is shown with the digest captured by publication.
- The task-intent line appears only for a canonical identity; a missing-intent record renders
  without it and is never treated as current.

### Todos

None recorded.

## Docs References

No configured external documentation applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The projection format is repository-owned. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Rendering is a deterministic one-way projection of the structured record. | `render_curator_coherence` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py:8-63 |
| The canonical task-intent identity line emitted after the topology fingerprint. | `TaskIntentIdentity` check + line insert | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py:53-56 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file introduces no external boundary. | — | — |

## MCAR-L03 Human Pair Projection

Generated Markdown now renders the contract/digest, both roots, source/work branches and bases,
onboarding root, and ledger path from the structured record. Markdown remains a projection and is
never reparsed as authority.

## CCR-R02@v2 Intent Binding In The Projection

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, coherence records bind the
canonical intent identity; the human projection now shows it so reviewers can verify that evidence
was accepted against the exact obligation bytes. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the coherence renderer now emits the canonical `Task intent:` schema+digest line after the
  topology fingerprint when the record carries a `TaskIntentIdentity`. Verified at code commit
  99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-29T21:46+02:00 — MCAR-L03: rendered the complete structured pair for human scope
  verification. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for the digest-bound human projection of structured coherence.
  Verification remains closeout-owned.
