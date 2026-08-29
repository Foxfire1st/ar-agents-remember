# mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-29T08:52+02:00 |
| lastVerifiedCommitHash |  `60e429d17e9fcbca3ab1c02563afcaa5761b8c5a`|
| lastVerifiedCommitDate |  2026-08-29T20:33:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[closeout integration overview](overview.md)

## Purpose

Owns exact candidate-to-judgment set validation and lifecycle capture/revalidation of each cited
evidence file's digest.

## Code Commentary

### Logic

`exact_curator_judgments` rejects duplicates, missing tuples, and extra tuples, restores the
attestation's deterministic order, resolves every explicit evidence reference, and returns recorded
judgments with lifecycle-computed SHA-256 digests. `require_recorded_judgments_current` repeats the
digest observation inside the publication CAS window and refuses evidence races.

### Conventions

This module validates and binds agent-owned decisions; it never chooses a disposition or writes a
rationale. Evidence-read failures are translated into the coherence error family.

### Invariants And Boundaries

- Set equality is exact over all three candidate identity cells.
- Evidence content, not merely the path string, is candidate-bound.
- Missing or unreadable evidence fails publication; no alternate root is attempted.

### Todos

None recorded.

## Docs References

No configured external documentation applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| This is a repository-owned evidence contract. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact set coverage and lifecycle-computed digests are established together. | `exact_curator_judgments` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py:19-54 |
| CAS revalidation catches task evidence that changes independently of candidate trees. | `require_recorded_judgments_current` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py:57-75 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| Evidence remains confined to contract-owned roots. | `resolve_curator_evidence_ref` | mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py:413-444 |

## Update History

- 2026-08-29T08:52+02:00 — Created for exact judgment coverage and evidence-byte CAS validation.
  Verification remains closeout-owned.
