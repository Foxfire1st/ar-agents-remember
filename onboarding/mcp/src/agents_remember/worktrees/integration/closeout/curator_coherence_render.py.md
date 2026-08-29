# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
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

### Conventions

The renderer is one-way. Consumers regenerate and byte-compare this projection; no parser exists.

### Invariants And Boundaries

- Rendered output contains no clock entropy and is deterministic for the same record.
- The projection is never machine authority.
- Every evidence reference is shown with the digest captured by publication.

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

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The file introduces no external boundary. | — | — |

## Update History

- 2026-08-29T08:52+02:00 — Created for the digest-bound human projection of structured coherence.
  Verification remains closeout-owned.
